"""Reference class for generating BibTeX entries."""

from __future__ import annotations

import re
import textwrap
from dataclasses import dataclass

import unidecode
from pyiso4.ltwa import Abbreviate
from pylatexenc.latexencode import unicode_to_latex

abbreviator = Abbreviate.create()


@dataclass
class Name:
    """Person name."""

    first: str | None
    last: str | None
    suffix: str | None = None

    def __str__(self) -> str:
        """Generate a name string."""
        if self.first is None or self.last is None:
            raise ValueError(
                f"First name ({self.first}) or last name ({self.last}) is missing."
            )
        if self.suffix is not None:
            return f"{self.first} {{{self.last} {self.suffix}}}"
        elif " " in self.last:
            return f"{self.first} {{{self.last}}}"
        return f"{self.first} {self.last}"


@dataclass
class Reference:
    """A reference to a scholarly article."""

    author: list[Name] | None = None
    title: str | None = None
    journal: str | None = None
    year: int | None = None
    volume: int | None = None
    issue: int | None = None
    pages: tuple[int] | tuple[int, int] | None = None
    annote: str | None = None
    doi: str | None = None

    @property
    def journal_abbr(self) -> str | None:
        """Abbreviated journal name."""
        if self.journal is None:
            return None
        return abbreviator(self.journal.title(), remove_part=True)

    @property
    def key(self) -> str:
        """Generate a BibTeX key."""
        if self.author is None or len(self.author) == 0:
            raise ValueError("No author is found.")
        if self.author[0].last is None:
            raise ValueError("The first author has no last name.")
        journal_abbr = self.journal_abbr
        if journal_abbr is None:
            raise ValueError("No journal is found.")
        return "{last}_{journal}_{year}_v{volume}_p{page}".format(
            last=unidecode.unidecode(self.author[0].last).replace(" ", ""),
            journal=re.sub(r"[\ \-\.]", "", journal_abbr),
            year=self.year,
            volume=self.volume,
            page=self.pages[0] if self.pages is not None else None,
        )

    @property
    def bibtex(self) -> str:
        """Generate a BibTeX entry."""
        if self.author is None:
            author_string = None
        else:
            author_string = " and ".join(str(aa) for aa in self.author)
        if self.pages is None:
            page_string = None
        else:
            page_string = "--".join(str(x) for x in self.pages)

        data = {
            "author": author_string,
            "title": self.title,
            "journal": self.journal_abbr,
            "year": self.year,
            "volume": self.volume,
            "issue": self.issue,
            "pages": page_string,
            "doi": self.doi,
            "annote": self.annote,
        }
        start = f"@Article{{{self.key},"
        end = "}\n"
        items = [start]
        for key, value in data.items():
            if value is None:
                continue
            if isinstance(value, int) or (isinstance(value, str) and value.isdigit()):
                valuestr = str(value)
            else:
                valuestr = ("\n" + " " * 13).join(
                    textwrap.wrap(
                        unicode_to_latex(
                            value,
                            non_ascii_only=True,
                            replacement_latex_protection="braces-all",
                        ),
                        70,
                    )
                )
                if key == "title":
                    valuestr = "{{%s}}" % valuestr
                else:
                    valuestr = "{%s}" % valuestr
            valuestr += ","
            keystr = " " * 4 + (key + " =").ljust(11, " ")
            items.append(keystr + valuestr)
        items.append(end)
        return "\n".join(items)

    def __or__(self, other: Reference | None) -> Reference:
        """Combine two references."""
        if other is None:
            return self
        return Reference(
            author=self.author or other.author,
            title=self.title or other.title,
            journal=self.journal or other.journal,
            year=self.year or other.year,
            volume=self.volume or other.volume,
            issue=self.issue or other.issue,
            pages=self.pages or other.pages,
            annote=self.annote or other.annote,
            doi=self.doi or other.doi,
        )

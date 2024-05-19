"""Feeder base class."""

from __future__ import annotations

from typing import TYPE_CHECKING, overload

if TYPE_CHECKING:
    from wenxian.reference import Reference


class Feeder:
    """Feeder base class."""

    def from_doi(self, doi: str) -> Reference | None:
        """Fetch a reference from a DOI."""

    def from_arxiv(self, arxiv: str) -> Reference | None:
        """Fetch a reference from an arXiv identifier."""

    def from_pmid(self, pmid: str) -> Reference | None:
        """Fetch a reference from a PubMed identifier."""

    @overload
    def _int(self, string: str) -> int: ...

    @overload
    def _int(self, string: None) -> None: ...

    def _int(self, string: str | None) -> int | None:
        """Convert string to int, return None if string is None."""
        return int(string) if string is not None else None

    @overload
    def _pages(self, string: str) -> tuple[int]: ...

    @overload
    def _pages(self, string: None) -> None: ...

    def _pages(self, string: str | None) -> tuple[int] | tuple[int, int] | None:
        """Convert a page string to a tuple of integers."""
        if string is None:
            return
        return tuple(map(int, string.split("-")))

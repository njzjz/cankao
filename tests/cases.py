"""Test cases."""

from __future__ import annotations

import textwrap

from wenxian.reference import Author, Reference

TEST_CASES = [
    (
        # mainly from pubmed
        Reference(
            author=[
                Author(first="Jinzhe", last="Zeng"),
                Author(first="Yujun", last="Tao"),
                Author(first="Timothy J.", last="Giese"),
                Author(first="Darrin M.", last="York"),
            ],
            title="QDπ: A Quantum Deep Potential Interaction Model for Drug Discovery",
            journal="Journal of chemical theory and computation",
            year=2023,
            volume=19,
            issue=4,
            pages=(1261, 1275),
            annote=textwrap.dedent(
                """\
            We report QDπ-v1.0 for modeling the internal energy of drug molecules
            containing H, C, N, and O atoms. The QDπ model is in the form of a
            quantum mechanical/machine learning potential correction (QM/Δ-MLP)
            that uses a fast third-order self-consistent density-functional
            tight-binding (DFTB3/3OB) model that is corrected to a quantitatively
            high-level of accuracy through a deep-learning potential (DeepPot-SE).
            The model has the advantage that it is able to properly treat
            electrostatic interactions and handle changes in charge/protonation
            states. The model is trained against reference data computed at the
            ωB97X/6-31G* level (as in the ANI-1x data set) and compared to several
            other approximate semiempirical and machine learning potentials
            (ANI-1x, ANI-2x, DFTB3, MNDO/d, AM1, PM6, GFN1-xTB, and GFN2-xTB). The
            QDπ model is demonstrated to be accurate for a wide range of intra- and
            intermolecular interactions (despite its intended use as an internal
            energy model) and has shown to perform exceptionally well for relative
            protonation/deprotonation energies and tautomers. An example application
            to model reactions involved in RNA strand cleavage catalyzed by protein
            and nucleic acid enzymes illustrates QDπ has average errors less than
            0.5 kcal/mol, whereas the other models compared have errors over an
            order of magnitude greater. Taken together, this makes QDπ highly
            attractive as a potential force field model for drug discovery.
            """
            )
            .strip()
            .replace("\n", " "),
            doi="10.1021/acs.jctc.2c01172",
        ),
        textwrap.dedent(r"""
        @Article{Zeng_JChemTheoryComput_2023_v19_p1261,
            author =   {Jinzhe Zeng and Yujun Tao and Timothy J. Giese and Darrin M. York},
            title =    {{QD{\ensuremath{\pi}}: A Quantum Deep Potential Interaction Model for
                     Drug Discovery}},
            journal =  {J. Chem. Theory Comput.},
            year =     2023,
            volume =   19,
            issue =    4,
            pages =    {1261--1275},
            doi =      {10.1021/acs.jctc.2c01172},
            annote =   {We report QD{\ensuremath{\pi}}-v1.0 for modeling the internal energy
                     of drug molecules containing H, C, N, and O atoms. The
                     QD{\ensuremath{\pi}} model is in the form of a quantum
                     mechanical/machine learning potential correction
                     (QM/{\ensuremath{\Delta}}-MLP) that uses a fast third-order self-
                     consistent density-functional tight-binding (DFTB3/3OB) model that is
                     corrected to a quantitatively high-level of accuracy through a deep-
                     learning potential (DeepPot-SE). The model has the advantage that it
                     is able to properly treat electrostatic interactions and handle
                     changes in charge/protonation states. The model is trained against
                     reference data computed at the {\ensuremath{\omega}}B97X/6-31G* level
                     (as in the ANI-1x data set) and compared to several other approximate
                     semiempirical and machine learning potentials (ANI-1x, ANI-2x, DFTB3,
                     MNDO/d, AM1, PM6, GFN1-xTB, and GFN2-xTB). The QD{\ensuremath{\pi}}
                     model is demonstrated to be accurate for a wide range of intra- and
                     intermolecular interactions (despite its intended use as an internal
                     energy model) and has shown to perform exceptionally well for relative
                     protonation/deprotonation energies and tautomers. An example
                     application to model reactions involved in RNA strand cleavage
                     catalyzed by protein and nucleic acid enzymes illustrates
                     QD{\ensuremath{\pi}} has average errors less than 0.5 kcal/mol,
                     whereas the other models compared have errors over an order of
                     magnitude greater. Taken together, this makes QD{\ensuremath{\pi}}
                     highly attractive as a potential force field model for drug discovery.},
        }
    """).strip(),
    )
]

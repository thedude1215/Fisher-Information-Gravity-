# Fisher-Information Gravity (FIG): A Covariant Extension to General Relativity

**Author:** Arnav Kumar  
**Affiliation:** Independent Researcher, Nepal  
**Status:** Manuscript Under Review at [Journal Name]  
**Topic:** Theoretical Physics, Modified Gravity, Information Geometry

---

## 🚀 Overview
**Is spacetime geometry shaped by information?**

This project constructs a new relativistic field theory where gravity couples not just to the *mass* of matter, but to its *information content* (specifically, the Fisher Information of the baryon density field). 

The goal was to formulate a mathematically consistent theory that could explain "Dark Matter" phenomena (like Galaxy Rotation Curves) as an emergent property of information geometry, without introducing new particles.

## 📄 Key Research Outcomes
This repository contains the full derivation, stability analysis, and cosmological validation of the theory.

* **Field Equations:** Derived modified Einstein Field Equations using a constrained variational principle (Action Principle).
* **Conservation Laws:** Proved that the theory satisfies the conservation of energy-momentum ($\nabla_\mu T^{\mu\nu} = 0$) using diffeomorphism invariance.
* **Cosmology:** Demonstrated that the "Information Fluid" behaves as a stiff fluid ($w=1$) in the early universe, redshifting as $a^{-6}$, ensuring it doesn't break Big Bang Nucleosynthesis limits.
* **Phenomenology:** Identified a "Screening Mechanism" that hides these effects in the Solar System (matching GR experiments) but allows them to emerge on galactic scales (matching RAR trends).

## 📂 Repository Contents

### `/manuscript`
* `Fisher_Information_Gravity.pdf`: The complete research paper including all mathematical proofs and references.

### `/derivations`
Detailed mathematical notebooks expanding on the condensed appendices of the paper:
* **Metric Variation:** Explicit steps for deriving the Fisher Stress Tensor ($T_{\mu\nu}^{FI}$).
* **Noether Currents:** Proofs of the conservation theorems associated with the Shift Symmetry and Baryon Number conservation.

### `/code`
Python scripts used for the "Phenomenological Methods" section of the paper:
* `axisymmetric_solver.py`: Solves the modified Poisson equation using Hankel Transforms to predict forces in galactic disks.
* `cosmology_plots.py`: Modeling the evolution of the Hubble parameter with the added Fisher Information term.

## 🛠️ Mathematical Framework
The theory adds a Fisher Information functional to the Einstein-Hilbert Action:

$$S = \int \sqrt{-g} \left( \frac{R}{16\pi G} + \mathcal{L}_m + \lambda g^{\mu\nu}\nabla_\mu \chi \nabla_\nu \chi \right) d^4x$$

Where $\chi = \ln(n)$ represents the information potential of the baryon density $n$.

## 📬 Contact
 arnavkumar1197@gmail.com

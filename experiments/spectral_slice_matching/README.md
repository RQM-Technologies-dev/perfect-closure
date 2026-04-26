# Spectral Slice Matching

This experiment asks:

**Which zeta-zero spectral slices, if any, align with known charged-lepton mass shells under a shared closure scale \(L_\ast\)?**

It is intentionally different from `experiments/zeta_mass_calibration`:

- `zeta_mass_calibration` tests fixed **rank-lock** assignments.
- `spectral_slice_matching` tests direct **anchor-scan spectral-slice matching**.

## Core equation

\[
E_n(L_\ast) = \frac{\hbar c}{L_\ast} t_n,
\]

with:

- \(E\) in MeV,
- \(\hbar c = 197.3269804\ \text{MeV fm}\),
- \(L_\ast\) in fm.

## Family and scan

The first family is charged leptons loaded from:

- `experiments/zeta_mass_calibration/data/particle_masses_mev.csv`

using:

- electron = 0.51099895 MeV
- muon = 105.6583755 MeV
- tau = 1776.86 MeV

Anchor scan:

- anchor particle: electron
- anchor index range: \(a=1\) to \(40\)
- for each anchor, set electron \(\to t_a\), infer \(L_\ast\), then nearest-match muon and tau targets.

## Zeta-zero ordinates used

This run uses:

- exact first 40 ordinates copied from the existing calibration script;
- Riemann–von Mangoldt inverse approximation for higher indices (
  Newton inversion of
  \(N(T)\approx\frac{T}{2\pi}(\log(\frac{T}{2\pi})-1)+\frac78\)
  ) when nearest targets exceed index 40.

So high-index assignments in this first run are **approximate** and should be treated as exploratory.

## Null comparisons

For each of 600 trials, the script computes the best anchor MAPE under two null spectra:

1. Poisson-spacing null with local mean spacing
   \(\Delta(T)\approx\frac{2\pi}{\log(T/(2\pi))}\).
2. Lattice null with matched local spacing and random phase offset.

## Run

```bash
python experiments/spectral_slice_matching/scripts/run_spectral_slice_matching.py
```

## Outputs

- `results/anchor_scan_top10.csv`
- `results/best_assignment.csv`
- `results/report.json`
- `outputs/figures/` (reserved for figures)

## Non-claim boundary

This experiment does **not** claim:

- zeta zeros are particles,
- particle masses are derived,
- RH is proved.

It only reports whether direct spectral-slice matching survives this exploratory test and null comparison.

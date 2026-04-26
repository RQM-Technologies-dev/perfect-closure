# Spectral Slice Matching Experiment

**Run date:** 2026-04-26  
**Status:** first-pass direct matching test complete.

This experiment tests the direct question behind the Perfect Closure series:

> If zeta zeros are complex spectral traces of quaternionic closure eigenvalues, which zeta-zero ordinates can match known mass-shell values under a shared closure scale \(L_\ast\)?

The previous `zeta_mass_calibration` experiment tested fixed rank-lock assignments. This experiment instead performs a direct spectral-slice match.

## Core map

For a zeta-zero ordinate \(t_n\), the mass-shell energy scale is

\[
E_n(L_\ast)=\frac{\hbar c}{L_\ast}t_n.
\]

For a known rest energy \(E_j\), the inferred closure length is

\[
L_{\ast,j,n}=\frac{\hbar c\,t_n}{E_j}.
\]

A shared closure family requires the same \(L_\ast\) to work across multiple particles.

## First test: charged leptons

The first clean target family is the charged leptons:

\[
e,\quad \mu,\quad \tau.
\]

The scan anchors the electron to one of the first ten zeta zeros, then finds the nearest zeta zero to the implied muon and tau targets.

## First-run result

The best electron anchor among \(t_1\) through \(t_{10}\) was:

\[
e\to t_{10},\qquad \mu\to t_{10486},\qquad \tau\to t_{254072}.
\]

This gives a shared closure length around

\[
L_\ast \approx 1.92206\times 10^4\ \mathrm{fm}.
\]

The relative errors are small:

- electron: exact by anchor construction;
- muon: \(-9.64\times 10^{-6}\);
- tau: \(-7.12\times 10^{-7}\).

However, the null comparison says this is **not statistically exceptional** under a local-density Poisson nearest-zero model. In the first null test, approximately 71% of null runs produced a best error as good as or better than the zeta result.

## Interpretation

This experiment answers the “which one?” question for the first charged-lepton scan:

| Particle | Zeta-zero index |
|---|---:|
| electron | 10 |
| muon | 10486 |
| tau | 254072 |

But it does **not** support a success claim. The match is visually striking but not statistically meaningful yet, because high zeta zeros are dense enough that nearest-zero matching can produce close ratios by chance.

## Run

```bash
python experiments/spectral_slice_matching/scripts/run_spectral_slice_matching.py
```

The script requires `mpmath`.

## Outputs

- `results/anchor_scan_leptons.csv`
- `results/best_matches.csv`
- `results/null_report.json`
- `results/report.md`

## Non-claim boundary

This experiment does **not** claim zeta zeros are particles. It does **not** derive lepton masses. It does **not** prove RH. It only tests whether a shared \(L_\ast\) spectral-slice interpretation survives a first direct matching and null comparison.

# Zeta-Mass Calibration Experiment

This experiment asks whether **real particle mass shells** can be pull-backed to
Riemann zeta zero ordinates using a single stable calibration length scale `L*`.

## Reproducibility

- Deterministic RNG seed: `314159`
- Fixed dataset: `data/particle_masses_mev.csv`
- Fixed assignment rules (predeclared; no adaptive search)
- Fixed null spectra and falsification thresholds

Run:

```bash
python experiments/zeta_mass_calibration/scripts/run_calibration.py
```

Outputs:

- `results/summary.csv`
- `results/report.json`

## Predeclared assignment rules

For particles sorted by ascending mass, with zeta zero ordinates
`gamma_n = Im(rho_n)`:

1. `rank_lock_offset_1`: particle rank `i` -> `gamma_(1+i)`
2. `rank_lock_offset_8`: particle rank `i` -> `gamma_(8+i)`
3. `rank_lock_offset_16`: particle rank `i` -> `gamma_(16+i)`

These are fixed before seeing fit quality.

## Null spectra

Each rule is compared against three null models:

1. **Permutation null:** randomly permute particle masses.
2. **Log-uniform synthetic null:** draw masses from log-uniform range over observed mass interval.
3. **Poisson-spaced gamma null:** replace zeta spacing by an exponential-spacing process with matched mean spacing.

Each null is simulated for 600 rounds.

## Falsification criteria

A rule is marked `not_supported` if **any** of these fail:

1. MAPE <= p95(permutation null)
2. MAPE <= p95(log-uniform synthetic null)
3. MAPE <= p95(Poisson gamma null)
4. Bootstrap CV of `L*` <= 0.10
5. Maximum absolute relative pullback error <= 0.35

The experiment-level result is:

- `success_claim_allowed` only if all rules pass.
- otherwise `do_not_claim_success`.

This enforces the instruction: *do not claim success unless statistics support it*.

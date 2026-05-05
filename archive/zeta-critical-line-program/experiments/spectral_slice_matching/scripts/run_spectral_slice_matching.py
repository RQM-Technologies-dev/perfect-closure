#!/usr/bin/env python3
"""Direct spectral-slice matching scan for charged leptons."""

from __future__ import annotations

import csv
import json
import math
import random
from pathlib import Path
from statistics import mean, pstdev

HBAR_C_MEV_FM = 197.3269804
SEED = 314159
NULL_TRIALS = 600
ANCHOR_MIN = 1
ANCHOR_MAX = 40

EXACT_FIRST_40_ZEROS = [
    14.134725141734693,
    21.022039638771554,
    25.01085758014569,
    30.424876125859512,
    32.93506158773919,
    37.58617815882567,
    40.9187190121475,
    43.32707328091499,
    48.00515088116716,
    49.7738324776723,
    52.97032147771446,
    56.44624769706339,
    59.34704400260235,
    60.83177852460981,
    65.11254404808161,
    67.07981052949417,
    69.54640171117398,
    72.06715767448191,
    75.70469069908393,
    77.1448400688748,
    79.33737502024937,
    82.91038085408603,
    84.73549298051705,
    87.42527461312523,
    88.80911120763447,
    92.49189927055848,
    94.65134404051989,
    95.87063422824531,
    98.83119421819369,
    101.31785100573139,
    103.72553804047834,
    105.44662305232699,
    107.1686111842764,
    111.02953554316968,
    111.87465917699264,
    114.32022091545272,
    116.22668032085755,
    118.790782865976,
    121.37012500242065,
    122.94682929355259,
]


def load_family_masses(csv_path: Path, family: list[str]) -> list[dict[str, float | str]]:
    rows: dict[str, float] = {}
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows[row["particle"]] = float(row["mass_mev"])
    return [{"particle": p, "energy_mev": rows[p]} for p in family]


def N_of_T(T: float) -> float:
    x = T / (2.0 * math.pi)
    return x * (math.log(x) - 1.0) + 0.875


def spacing_at_t(T: float) -> float:
    x = max(T / (2.0 * math.pi), 1.0000001)
    return 2.0 * math.pi / math.log(x)


def invert_N_to_t(n: int) -> float:
    if n <= 40:
        return EXACT_FIRST_40_ZEROS[n - 1]
    t = 2.0 * math.pi * n / max(math.log(max(n, 3)), 1.0)
    t = max(t, EXACT_FIRST_40_ZEROS[-1] + 1.0)
    for _ in range(12):
        x = t / (2.0 * math.pi)
        f = x * (math.log(x) - 1.0) + 0.875 - n
        fp = math.log(x) / (2.0 * math.pi)
        t_new = t - f / fp
        if abs(t_new - t) < 1e-12 * max(1.0, t):
            t = t_new
            break
        t = max(t_new, EXACT_FIRST_40_ZEROS[-1] + 1e-6)
    return t


def estimate_index_from_t(target_t: float) -> int:
    n_hat = int(round(N_of_T(max(target_t, EXACT_FIRST_40_ZEROS[0]))))
    return max(1, n_hat)


def nearest_zero(target_t: float) -> tuple[int, float]:
    n0 = estimate_index_from_t(target_t)
    lo = max(1, n0 - 8)
    hi = n0 + 8
    best_n = lo
    best_t = invert_N_to_t(lo)
    best_d = abs(best_t - target_t)
    for n in range(lo + 1, hi + 1):
        tn = invert_N_to_t(n)
        d = abs(tn - target_t)
        if d < best_d:
            best_n, best_t, best_d = n, tn, d
    return best_n, best_t


def run_anchor(anchor_idx: int, family_rows: list[dict[str, float | str]]) -> tuple[list[dict], dict]:
    e_row = family_rows[0]
    t_anchor = invert_N_to_t(anchor_idx)
    L_star = HBAR_C_MEV_FM * t_anchor / e_row["energy_mev"]

    assignments: list[dict] = []
    rel_errors = []
    inferred_Ls = []

    for row in family_rows:
        particle = row["particle"]
        energy = row["energy_mev"]
        target_t = t_anchor * energy / e_row["energy_mev"]
        n_near, t_near = nearest_zero(target_t)

        pred_energy = HBAR_C_MEV_FM * t_near / L_star
        rel_error = (pred_energy - energy) / energy
        inferred_L = HBAR_C_MEV_FM * t_near / energy

        assignments.append(
            {
                "anchor_index": anchor_idx,
                "anchor_t": t_anchor,
                "particle": particle,
                "energy_mev": energy,
                "target_t": target_t,
                "nearest_zero_index": n_near,
                "nearest_zero_t": t_near,
                "predicted_energy_mev": pred_energy,
                "relative_error": rel_error,
                "inferred_L_star_fm": inferred_L,
            }
        )
        rel_errors.append(abs(rel_error))
        inferred_Ls.append(inferred_L)

    metrics = {
        "anchor_index": anchor_idx,
        "anchor_t": t_anchor,
        "mape": mean(rel_errors),
        "max_abs_rel": max(rel_errors),
        "L_cv": pstdev(inferred_Ls) / mean(inferred_Ls),
    }
    return assignments, metrics


def null_nearest_t_poisson(target_t: float, rng: random.Random) -> float:
    spacing = spacing_at_t(target_t)
    dist = rng.expovariate(2.0 / spacing)
    sign = -1.0 if rng.random() < 0.5 else 1.0
    return target_t + sign * dist


def null_nearest_t_lattice(target_t: float, rng: random.Random) -> float:
    spacing = spacing_at_t(target_t)
    phase = rng.uniform(0.0, spacing)
    k = round((target_t - phase) / spacing)
    return phase + k * spacing


def run_null_trial(family_rows: list[dict[str, float | str]], rng: random.Random, kind: str) -> float:
    e_energy = family_rows[0]["energy_mev"]
    best = float("inf")
    for anchor_idx in range(ANCHOR_MIN, ANCHOR_MAX + 1):
        t_anchor = invert_N_to_t(anchor_idx)
        L_star = HBAR_C_MEV_FM * t_anchor / e_energy
        errs = []
        for row in family_rows:
            energy = row["energy_mev"]
            if row["particle"] == "electron":
                t_used = t_anchor
            else:
                target_t = t_anchor * energy / e_energy
                if kind == "poisson":
                    t_used = null_nearest_t_poisson(target_t, rng)
                else:
                    t_used = null_nearest_t_lattice(target_t, rng)
            pred = HBAR_C_MEV_FM * t_used / L_star
            errs.append(abs((pred - energy) / energy))
        best = min(best, mean(errs))
    return best


def percentile_rank_lower_is_better(value: float, samples: list[float]) -> float:
    return 100.0 * sum(1 for s in samples if s <= value) / len(samples)


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    root = Path(__file__).resolve().parents[3]
    masses_csv = root / "experiments" / "zeta_mass_calibration" / "data" / "particle_masses_mev.csv"
    result_dir = root / "experiments" / "spectral_slice_matching" / "results"

    family = ["electron", "muon", "tau"]
    family_rows = load_family_masses(masses_csv, family)

    all_metrics: list[dict] = []
    all_assignments: list[dict] = []

    for anchor_idx in range(ANCHOR_MIN, ANCHOR_MAX + 1):
        assignments, metrics = run_anchor(anchor_idx, family_rows)
        all_assignments.extend(assignments)
        all_metrics.append(metrics)

    all_metrics_sorted = sorted(all_metrics, key=lambda r: r["mape"])
    top10 = all_metrics_sorted[:10]
    best_anchor = top10[0]["anchor_index"]

    best_assignment = [r for r in all_assignments if r["anchor_index"] == best_anchor]
    best_assignment_indices = {r["particle"]: int(r["nearest_zero_index"]) for r in best_assignment}

    rng = random.Random(SEED)
    poisson_best_dist = [run_null_trial(family_rows, rng, "poisson") for _ in range(NULL_TRIALS)]
    lattice_best_dist = [run_null_trial(family_rows, rng, "lattice") for _ in range(NULL_TRIALS)]

    best_mape = top10[0]["mape"]
    poisson_pct = percentile_rank_lower_is_better(best_mape, poisson_best_dist)
    lattice_pct = percentile_rank_lower_is_better(best_mape, lattice_best_dist)

    claim_boundary = (
        "exploratory_match_found_requires_exact_zeros_and_stronger_nulls"
        if (poisson_pct <= 5.0 and lattice_pct <= 5.0)
        else "no_support_under_current_test"
    )

    write_csv(
        result_dir / "anchor_scan_top10.csv",
        ["anchor_index", "anchor_t", "mape", "max_abs_rel", "L_cv"],
        top10,
    )
    write_csv(
        result_dir / "best_assignment.csv",
        [
            "anchor_index",
            "anchor_t",
            "particle",
            "energy_mev",
            "target_t",
            "nearest_zero_index",
            "nearest_zero_t",
            "predicted_energy_mev",
            "relative_error",
            "inferred_L_star_fm",
        ],
        best_assignment,
    )

    report = {
        "family_tested": family,
        "anchor_particle": "electron",
        "anchor_scan_range": [ANCHOR_MIN, ANCHOR_MAX],
        "zero_ordinate_method": "exact_first_40_from_calibration_script_plus_riemann_von_mangoldt_inverse_approximation_for_n_gt_40",
        "best_anchor_index": best_anchor,
        "best_mape": best_mape,
        "best_max_abs_rel": top10[0]["max_abs_rel"],
        "best_L_cv": top10[0]["L_cv"],
        "best_assignment_indices": best_assignment_indices,
        "null_percentile_best_zeta_mape_vs_poisson": poisson_pct,
        "null_percentile_best_zeta_mape_vs_lattice": lattice_pct,
        "claim_boundary": claim_boundary,
        "constants": {"hbar_c_mev_fm": HBAR_C_MEV_FM},
        "null_trials": NULL_TRIALS,
        "seed": SEED,
    }
    (result_dir / "report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

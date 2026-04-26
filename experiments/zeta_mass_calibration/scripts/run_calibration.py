#!/usr/bin/env python3
"""Reproducible zeta-mass pullback calibration experiment (stdlib-only)."""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
from dataclasses import dataclass
from pathlib import Path
from statistics import mean, pstdev

HBAR_MEV_S = 6.582119569e-22
C_M_PER_S = 299_792_458.0

SEED = 314159

ZETA_ZERO_ORDINATES = [
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

BOOTSTRAP_ROUNDS = 400
NULL_ROUNDS = 600


@dataclass(frozen=True)
class Rule:
    name: str
    description: str


RULES = [
    Rule("rank_lock_offset_1", "Rank i -> gamma_(1+i) after ascending-mass sort."),
    Rule("rank_lock_offset_8", "Rank i -> gamma_(8+i) after ascending-mass sort."),
    Rule("rank_lock_offset_16", "Rank i -> gamma_(16+i) after ascending-mass sort."),
]


def load_particles(path: Path) -> list[dict[str, float | str]]:
    rows = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append({"particle": row["particle"], "mass_mev": float(row["mass_mev"])})
    return sorted(rows, key=lambda r: r["mass_mev"])


def zeta_ordinates(n_max: int) -> list[float]:
    if n_max > len(ZETA_ZERO_ORDINATES):
        raise ValueError(f"Need {n_max} zeta zeros but only {len(ZETA_ZERO_ORDINATES)} are pretabulated")
    return ZETA_ZERO_ORDINATES[:n_max]


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def fit_lstar(masses_mev: list[float], gamma: list[float]) -> float:
    numer = dot(masses_mev, gamma)
    denom = dot(masses_mev, masses_mev)
    return HBAR_MEV_S * numer / (denom * C_M_PER_S**2)


def percentile(values: list[float], p: float) -> float:
    if not values:
        raise ValueError("empty values")
    s = sorted(values)
    k = (len(s) - 1) * (p / 100.0)
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return s[int(k)]
    return s[f] * (c - k) + s[c] * (k - f)


def evaluate_rule(masses: list[float], gamma_pool: list[float], offset: int) -> dict:
    gamma = gamma_pool[offset : offset + len(masses)]
    l_star = fit_lstar(masses, gamma)
    gamma_hat = [(m * C_M_PER_S**2 * l_star / HBAR_MEV_S) for m in masses]
    residual = [gh - g for gh, g in zip(gamma_hat, gamma)]
    rel_err = [r / g for r, g in zip(residual, gamma)]
    return {
        "offset": offset + 1,
        "l_star_m": l_star,
        "rmse": math.sqrt(mean([r * r for r in residual])),
        "mae": mean([abs(r) for r in residual]),
        "mape": mean([abs(e) for e in rel_err]),
        "max_abs_rel": max(abs(e) for e in rel_err),
    }


def bootstrap_stability(masses: list[float], gamma_pool: list[float], offset: int, rng: random.Random) -> dict:
    gamma = gamma_pool[offset : offset + len(masses)]
    n = len(masses)
    draws = []
    for _ in range(BOOTSTRAP_ROUNDS):
        idx = [rng.randrange(n) for _ in range(n)]
        mb = [masses[i] for i in idx]
        gb = [gamma[i] for i in idx]
        draws.append(fit_lstar(mb, gb))
    mu = mean(draws)
    sigma = pstdev(draws)
    return {"bootstrap_mean": mu, "bootstrap_std": sigma, "bootstrap_cv": sigma / mu}


def score_mape(candidate_masses: list[float], gamma: list[float]) -> float:
    l_star = fit_lstar(candidate_masses, gamma)
    gamma_hat = [(m * C_M_PER_S**2 * l_star / HBAR_MEV_S) for m in candidate_masses]
    rel = [abs((gh - g) / g) for gh, g in zip(gamma_hat, gamma)]
    return mean(rel)


def null_scores(masses: list[float], gamma_pool: list[float], offset: int, rng: random.Random) -> dict:
    n = len(masses)
    gamma = gamma_pool[offset : offset + n]

    perm_scores = []
    for _ in range(NULL_ROUNDS):
        p = masses[:]
        rng.shuffle(p)
        perm_scores.append(score_mape(p, gamma))

    log_min, log_max = math.log(min(masses)), math.log(max(masses))
    synthetic_scores = []
    for _ in range(NULL_ROUNDS):
        s = [math.exp(rng.uniform(log_min, log_max)) for _ in range(n)]
        synthetic_scores.append(score_mape(s, gamma))

    spacing = [b - a for a, b in zip(gamma_pool[offset : offset + n], gamma_pool[offset + 1 : offset + n + 1])]
    mean_spacing = mean(spacing)
    poisson_scores = []
    for _ in range(NULL_ROUNDS):
        g = [gamma[0]]
        for _ in range(1, n):
            u = max(rng.random(), 1e-12)
            exp_step = -mean_spacing * math.log(u)
            g.append(g[-1] + exp_step)
        poisson_scores.append(score_mape(masses, g))

    return {
        "perm_p95": percentile(perm_scores, 95),
        "synthetic_p95": percentile(synthetic_scores, 95),
        "poisson_p95": percentile(poisson_scores, 95),
    }


def to_offset(rule_name: str) -> int:
    return int(rule_name.rsplit("_", 1)[-1]) - 1


def write_summary(path: Path, rows: list[dict]) -> None:
    cols = [
        "rule",
        "description",
        "offset",
        "l_star_m",
        "mape",
        "rmse",
        "max_abs_rel",
        "bootstrap_cv",
        "perm_p95",
        "synthetic_p95",
        "poisson_p95",
        "falsification_status",
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=cols)
        writer.writeheader()
        for row in sorted(rows, key=lambda r: r["mape"]):
            writer.writerow(row)


def run(data_path: Path, outdir: Path) -> dict:
    rng = random.Random(SEED)
    particles = load_particles(data_path)
    masses = [r["mass_mev"] for r in particles]

    max_offset = max(to_offset(r.name) for r in RULES)
    gamma_pool = zeta_ordinates(max_offset + len(masses) + 2)

    rows = []
    statuses = []
    for rule in RULES:
        offset = to_offset(rule.name)
        metrics = evaluate_rule(masses, gamma_pool, offset)
        stability = bootstrap_stability(masses, gamma_pool, offset, rng)
        null = null_scores(masses, gamma_pool, offset, rng)

        falsified = any(
            [
                metrics["mape"] > null["perm_p95"],
                metrics["mape"] > null["synthetic_p95"],
                metrics["mape"] > null["poisson_p95"],
                stability["bootstrap_cv"] > 0.10,
                metrics["max_abs_rel"] > 0.35,
            ]
        )
        status = "not_supported" if falsified else "supported_under_current_tests"
        statuses.append(status)

        rows.append(
            {
                "rule": rule.name,
                "description": rule.description,
                "offset": metrics["offset"],
                "l_star_m": metrics["l_star_m"],
                "mape": metrics["mape"],
                "rmse": metrics["rmse"],
                "max_abs_rel": metrics["max_abs_rel"],
                "bootstrap_cv": stability["bootstrap_cv"],
                "perm_p95": null["perm_p95"],
                "synthetic_p95": null["synthetic_p95"],
                "poisson_p95": null["poisson_p95"],
                "falsification_status": status,
            }
        )

    outdir.mkdir(parents=True, exist_ok=True)
    write_summary(outdir / "summary.csv", rows)

    report = {
        "seed": SEED,
        "bootstrap_rounds": BOOTSTRAP_ROUNDS,
        "null_rounds": NULL_ROUNDS,
        "falsification_criteria": {
            "criterion_1": "MAPE <= p95 permutation null",
            "criterion_2": "MAPE <= p95 log-uniform synthetic null",
            "criterion_3": "MAPE <= p95 Poisson-spaced gamma null",
            "criterion_4": "bootstrap CV(L*) <= 0.10",
            "criterion_5": "max abs relative pullback error <= 0.35",
        },
        "overall": "success_claim_allowed" if all(s != "not_supported" for s in statuses) else "do_not_claim_success",
    }
    (outdir / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=Path(__file__).resolve().parents[1] / "data" / "particle_masses_mev.csv")
    parser.add_argument("--outdir", type=Path, default=Path(__file__).resolve().parents[1] / "results")
    args = parser.parse_args()
    print(json.dumps(run(args.data, args.outdir), indent=2))


if __name__ == "__main__":
    main()

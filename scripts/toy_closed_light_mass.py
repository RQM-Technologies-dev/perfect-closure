#!/usr/bin/env python3
"""Toy closure spectrum for closed lightlike phase routes.

This is a pedagogical sanity model:
- impose a closure length L;
- enforce k_n L = 2*pi*n;
- compute E_n = hbar*c*k_n and M_n = E_n/c^2.

It is not a particle-mass derivation.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


HBAR = 1.054_571_817e-34  # J*s (exact CODATA 2018 value)
C = 299_792_458.0  # m/s (exact)
EV_PER_J = 1.0 / 1.602_176_634e-19


def closure_modes(length_m: float, n_values: list[int]) -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    for n in n_values:
        k_n = (2.0 * math.pi * n) / length_m
        e_n_j = HBAR * C * k_n
        m_n_kg = e_n_j / (C**2)
        rows.append(
            {
                "L_m": length_m,
                "n": n,
                "k_n_per_m": k_n,
                "E_n_J": e_n_j,
                "E_n_eV": e_n_j * EV_PER_J,
                "M_n_kg": m_n_kg,
            }
        )
    return rows


def format_markdown(rows: list[dict[str, float]]) -> str:
    lines = [
        "# Toy Closed-Light Mass Spectrum",
        "",
        "Toy model only (closure quantization sanity check).",
        "",
        r"Using $k_n L = 2\pi n$, $E_n=\hbar c k_n$, $M_n=E_n/c^2$.",
        "",
        "| L (m) | n | k_n (1/m) | E_n (eV) | M_n (kg) |",
        "|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['L_m']:.3e} | {int(row['n'])} | {row['k_n_per_m']:.3e} | "
            f"{row['E_n_eV']:.6e} | {row['M_n_kg']:.6e} |"
        )
    lines.extend(
        [
            "",
            "Interpretation: once a closure length is imposed, the closed-phase toy model has a discrete mass scale.",
            "This table is pedagogical and does not derive observed particle masses.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_csv(path: Path, rows: list[dict[str, float]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["L_m", "n", "k_n_per_m", "E_n_J", "E_n_eV", "M_n_kg"],
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate toy closed-light mass spectrum.")
    parser.add_argument(
        "--lengths",
        type=float,
        nargs="+",
        default=[1e-9, 1e-10, 1e-12],
        help="Closure lengths L in meters.",
    )
    parser.add_argument(
        "--n-max",
        type=int,
        default=5,
        help="Maximum mode number n (inclusive), starting at 1.",
    )
    parser.add_argument(
        "--csv-out",
        type=Path,
        default=Path("assets/data/toy-closed-light-mass.csv"),
        help="Output CSV path.",
    )
    parser.add_argument(
        "--md-out",
        type=Path,
        default=Path("assets/data/toy-closed-light-mass.md"),
        help="Output Markdown table path.",
    )
    args = parser.parse_args()

    if args.n_max < 1:
        raise ValueError("n-max must be >= 1")
    if any(length <= 0 for length in args.lengths):
        raise ValueError("all closure lengths must be > 0")

    n_values = list(range(1, args.n_max + 1))
    rows: list[dict[str, float]] = []
    for length in args.lengths:
        rows.extend(closure_modes(length, n_values))

    args.csv_out.parent.mkdir(parents=True, exist_ok=True)
    args.md_out.parent.mkdir(parents=True, exist_ok=True)
    write_csv(args.csv_out, rows)
    args.md_out.write_text(format_markdown(rows), encoding="utf-8")

    print("Toy closed-light spectrum generated.")
    print(f"CSV: {args.csv_out}")
    print(f"Markdown: {args.md_out}")


if __name__ == "__main__":
    main()

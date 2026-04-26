#!/usr/bin/env python3
"""Generate figure set for the Perfect Closure paper series.

Outputs both SVG (for docs/markdown) and PNG (for LaTeX compatibility).
"""

from __future__ import annotations

import math
import shutil
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, Rectangle


FIG_DIR = Path(__file__).resolve().parents[1] / "assets" / "figures"
DOC_FIG_DIR = Path(__file__).resolve().parents[1] / "docs" / "assets" / "figures"
DPI = 220


def style_axes(ax):
    ax.set_facecolor("#fcfcfd")
    ax.grid(True, alpha=0.22, linewidth=0.7)
    for spine in ax.spines.values():
        spine.set_alpha(0.35)


def save_figure(fig, name: str):
    svg_path = FIG_DIR / f"{name}.svg"
    png_path = FIG_DIR / f"{name}.png"
    fig.savefig(svg_path, bbox_inches="tight")
    fig.savefig(png_path, dpi=DPI, bbox_inches="tight")
    plt.close(fig)


def figure_series_arc():
    fig, ax = plt.subplots(figsize=(14, 3.8))
    ax.axis("off")
    x = np.linspace(0.08, 0.92, 5)
    y = np.full(5, 0.5)
    labels = [
        "Paper 1\nComplex zeta trace",
        "Paper 2\nQuaternionic closure geometry",
        "Paper 3\nMass-shell norm",
        "Paper 4\nEigenvalue bridge",
        "Paper 5\nCalibration / prediction test",
    ]
    colors = ["#6baed6", "#74c476", "#fd8d3c", "#9e9ac8", "#fb6a4a"]

    for i, (xi, yi) in enumerate(zip(x, y)):
        rect = FancyArrowPatch(
            (xi - 0.075, yi - 0.12),
            (xi + 0.075, yi + 0.12),
            arrowstyle="-",
            mutation_scale=10,
            linewidth=0,
        )
        ax.add_patch(rect)
        ax.add_patch(
            Rectangle(
                (xi - 0.09, yi - 0.14),
                0.18,
                0.28,
                facecolor=colors[i],
                edgecolor="#2b2b2b",
                linewidth=1.0,
                alpha=0.93,
            )
        )
        ax.text(xi, yi, labels[i], ha="center", va="center", fontsize=10.5, color="white")

    for i in range(4):
        arr = FancyArrowPatch(
            (x[i] + 0.10, y[i]),
            (x[i + 1] - 0.10, y[i + 1]),
            arrowstyle="-|>",
            mutation_scale=15,
            linewidth=1.6,
            color="#303030",
        )
        ax.add_patch(arr)

    ax.text(
        0.5,
        0.15,
        "Core spine:  Xi(t_n)=0  →  A_u χ_{t_n}=t_n χ_{t_n}  →  P P̄=(ℏ t_n / L_*)²",
        ha="center",
        va="center",
        fontsize=11,
    )
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    save_figure(fig, "perfect-closure-series-arc")


def figure_main_pipeline():
    fig, ax = plt.subplots(figsize=(12, 3.8))
    ax.axis("off")
    boxes = [
        (0.12, "Xi(t_n)=0\ncomplex spectral trace", "#6baed6"),
        (0.50, "A_u χ_{t_n}=t_n χ_{t_n}\nquaternionic closure eigenvalue", "#74c476"),
        (0.86, "P P̄=(ℏ t_n/L_*)²\nmass-shell norm after scaling", "#fd8d3c"),
    ]
    for x, text, color in boxes:
        ax.add_patch(
            Rectangle((x - 0.16, 0.35), 0.32, 0.30, facecolor=color, edgecolor="#2b2b2b", alpha=0.95)
        )
        ax.text(x, 0.50, text, ha="center", va="center", fontsize=11, color="white")
    for a, b in [(0.28, 0.34), (0.66, 0.70)]:
        ax.add_patch(
            FancyArrowPatch((a, 0.50), (b, 0.50), arrowstyle="-|>", mutation_scale=20, linewidth=1.8, color="#333333")
        )
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    save_figure(fig, "zeta-to-mass-shell-pipeline")


def figure_square_root_mirror():
    fig, ax = plt.subplots(figsize=(8.5, 8.5))
    style_axes(ax)
    theta = np.linspace(0, 2 * np.pi, 500)
    r = 1.0
    ax.plot(r * np.cos(theta), r * np.sin(theta), color="#6baed6", linewidth=2, label="Equal amplitude 1/√p")
    t = 1.2
    phi = t * np.log(5)
    ax.arrow(0, 0, 0.85 * np.cos(-phi), 0.85 * np.sin(-phi), width=0.015, color="#2c7fb8")
    ax.arrow(0, 0, 0.85 * np.cos(phi), 0.85 * np.sin(phi), width=0.015, color="#31a354")
    ax.text(0.92 * np.cos(-phi), 0.92 * np.sin(-phi), "p^{-(1/2+it)}", color="#2c7fb8", fontsize=11)
    ax.text(0.92 * np.cos(phi), 0.92 * np.sin(phi), "p^{-(1/2-it)}", color="#31a354", fontsize=11)
    ax.text(0.0, -1.22, "Opposite phase directions at equal amplitude on Re(s)=1/2", ha="center", fontsize=10)
    ax.set_title("Square-root mirror prime routes")
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    save_figure(fig, "square-root-mirror-prime-routes")


def figure_prime_imbalance_curve():
    fig, ax = plt.subplots(figsize=(9, 5))
    style_axes(ax)
    delta = np.linspace(-0.6, 0.6, 300)
    primes = [2, 5, 11]
    colors = ["#3182bd", "#31a354", "#e6550d"]
    for p, c in zip(primes, colors):
        bp = 2 * (p ** (-0.5)) * np.abs(np.sinh(delta * np.log(p)))
        ax.plot(delta, bp, color=c, linewidth=2, label=f"p={p}")
    ax.axvline(0, color="#111111", linewidth=1.2, linestyle="--")
    ax.text(0.01, ax.get_ylim()[1] * 0.93, "δ=0 (zero imbalance)", fontsize=10)
    ax.set_xlabel("δ in σ = 1/2 + δ")
    ax.set_ylabel("B_p(1/2+δ)")
    ax.set_title("Illustrative prime imbalance curve")
    ax.legend(frameon=True)
    save_figure(fig, "prime-imbalance-curve")


def figure_quaternionic_slices():
    fig, ax = plt.subplots(figsize=(9, 6))
    style_axes(ax)
    t = np.linspace(-3, 3, 100)
    slopes = [0.2, 0.5, 1.0, -0.6]
    colors = ["#9ecae1", "#74c476", "#ef3b2c", "#9e9ac8"]
    for s, c in zip(slopes, colors):
        ax.plot(0.5 + 0 * t, s * t, color=c, linewidth=2)
    ax.plot(0.5 + 0 * t, t, color="#08519c", linewidth=3, label="Complex slice u=i")
    ax.axvline(0.5, color="#2b2b2b", linestyle="--", linewidth=1.4)
    ax.text(0.52, 2.6, "Re=1/2", fontsize=10)
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(-3.2, 3.2)
    ax.set_xlabel("Real component")
    ax.set_ylabel("Imaginary / slice coordinate")
    ax.set_title("Quaternionic critical slices: q_u(t)=1/2 + u t")
    ax.legend()
    save_figure(fig, "quaternionic-critical-slices")


def figure_six_step_gate():
    fig, ax = plt.subplots(figsize=(7.8, 7.8))
    ax.axis("off")
    ax.set_aspect("equal", adjustable="box")
    th = np.linspace(0, 2 * np.pi, 600)
    ax.plot(np.cos(th), np.sin(th), color="#4a6fa5", linewidth=2)
    for k in range(6):
        a = k * np.pi / 3
        x, y = np.cos(a), np.sin(a)
        ax.plot([0, x], [0, y], color="#999999", linewidth=1)
        ax.add_patch(Circle((x, y), 0.05, color="#31a354"))
        ax.text(1.14 * x, 1.14 * y, f"Q^{k}", ha="center", va="center", fontsize=10)
    ax.text(0, 0, "Q=e^{uπ/3}", ha="center", va="center", fontsize=12)
    ax.text(0, -1.28, "Q^3=-1   and   Q^6=1", ha="center", va="center", fontsize=11)
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.4, 1.4)
    save_figure(fig, "six-step-closure-gate")


def figure_mass_shell_norm():
    fig, ax = plt.subplots(figsize=(9, 5.8))
    ax.axis("off")
    ax.add_patch(Ellipse((0.30, 0.55), 0.44, 0.62, facecolor="#deebf7", edgecolor="#2c7fb8", linewidth=2))
    ax.add_patch(Ellipse((0.72, 0.55), 0.44, 0.62, facecolor="#e5f5e0", edgecolor="#31a354", linewidth=2))
    ax.text(0.30, 0.55, "Null / open\nP P̄ = 0", ha="center", va="center", fontsize=13, color="#08519c")
    ax.text(0.72, 0.55, "Massive / closed\nP P̄ = m²c² > 0", ha="center", va="center", fontsize=13, color="#006d2c")
    ax.add_patch(
        FancyArrowPatch((0.43, 0.55), (0.58, 0.55), arrowstyle="-|>", mutation_scale=18, linewidth=2, color="#333333")
    )
    ax.text(0.505, 0.62, "closure", ha="center", fontsize=10)
    save_figure(fig, "mass-shell-norm")


def figure_operator_bridge():
    fig, ax = plt.subplots(figsize=(13, 5))
    ax.axis("off")
    steps = [
        (0.08, "internal scale\nρ"),
        (0.22, "eigenmode\nχ_t(ρ)=ρ^{-1/2-u t}"),
        (0.38, "closure generator\nA_u"),
        (0.53, "zeta selector\nXi(A_u)"),
        (0.69, "kernel mode\nat t_n"),
        (0.86, "mass-shell lift\nthrough L_*"),
    ]
    for x, txt in steps:
        ax.add_patch(
            Rectangle((x - 0.07, 0.36), 0.14, 0.28, facecolor="#f0f0f0", edgecolor="#444444", linewidth=1.1)
        )
        ax.text(x, 0.50, txt, ha="center", va="center", fontsize=10)
    for i in range(len(steps) - 1):
        ax.add_patch(
            FancyArrowPatch(
                (steps[i][0] + 0.072, 0.50),
                (steps[i + 1][0] - 0.072, 0.50),
                arrowstyle="-|>",
                mutation_scale=13,
                linewidth=1.5,
                color="#2f2f2f",
            )
        )
    ax.text(0.5, 0.18, "Bridge supports  Xi(t_n)=0  →  A_u χ_{t_n}=t_n χ_{t_n}  →  P P̄=(ℏ t_n/L_*)²", ha="center", fontsize=11)
    save_figure(fig, "closure-operator-bridge")


def figure_calibration_regimes():
    fig, ax = plt.subplots(figsize=(10, 4.8))
    style_axes(ax)
    labels = ["Particle-specific L_*", "Family-specific L_*", "Universal L_*"]
    scores = [1.0, 2.1, 3.0]
    colors = ["#9ecae1", "#74c476", "#fb6a4a"]
    y = np.arange(len(labels))
    ax.barh(y, scores, color=colors, edgecolor="#444444")
    ax.set_yticks(y, labels=labels)
    ax.set_xlabel("Predictive strength / falsifiability (illustrative scale)")
    ax.set_xlim(0, 3.3)
    ax.set_title("Calibration regimes")
    ax.text(1.0, y[0], "weak / calibrating", va="center", ha="left", fontsize=9)
    ax.text(2.1, y[1], "potentially predictive", va="center", ha="left", fontsize=9)
    ax.text(3.0, y[2], "strongest / most falsifiable", va="center", ha="left", fontsize=9)
    save_figure(fig, "calibration-regimes")


def figure_inverse_test():
    fig, ax = plt.subplots(figsize=(12, 4.2))
    ax.axis("off")
    nodes = [
        (0.09, "Mass shell\nP P̄ = m²c²"),
        (0.29, "Compton curvature\nk_C = mc/ℏ"),
        (0.50, "Pulled-back ordinate\nτ = mcL_*/ℏ"),
        (0.73, "Zeta compatibility\nR_ζ(m;L_*) = |Xi(τ)|²"),
    ]
    for x, text in nodes:
        ax.add_patch(
            Rectangle((x - 0.10, 0.35), 0.20, 0.32, facecolor="#f7fbff", edgecolor="#1f78b4", linewidth=1.2)
        )
        ax.text(x, 0.51, text, ha="center", va="center", fontsize=10)
    for i in range(len(nodes) - 1):
        ax.add_patch(
            FancyArrowPatch(
                (nodes[i][0] + 0.102, 0.51),
                (nodes[i + 1][0] - 0.102, 0.51),
                arrowstyle="-|>",
                mutation_scale=13,
                linewidth=1.6,
                color="#2e2e2e",
            )
        )
    ax.text(0.50, 0.18, "Inverse test: map observed mass scales back to zeta-compatibility residual", ha="center", fontsize=11)
    save_figure(fig, "mass-to-zeta-inverse-test")


def main():
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    figure_series_arc()
    figure_main_pipeline()
    figure_square_root_mirror()
    figure_prime_imbalance_curve()
    figure_quaternionic_slices()
    figure_six_step_gate()
    figure_mass_shell_norm()
    figure_operator_bridge()
    figure_calibration_regimes()
    figure_inverse_test()
    DOC_FIG_DIR.mkdir(parents=True, exist_ok=True)
    for svg in FIG_DIR.glob("*.svg"):
        shutil.copy2(svg, DOC_FIG_DIR / svg.name)
    print(f"Generated figures in {FIG_DIR}")


if __name__ == "__main__":
    main()

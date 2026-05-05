#!/usr/bin/env python3
"""Generate curated visuals for the Perfect Closure thesis.

Outputs SVG (Markdown), PNG (LaTeX), and PDF (optional print workflows).
"""

from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401


FIG_DIR = Path(__file__).resolve().parents[1] / "assets" / "figures"
DPI = 260

plt.rcParams.update(
    {
        "font.size": 10.5,
        "axes.titlesize": 12,
        "axes.labelsize": 10.5,
        "legend.framealpha": 0.95,
        "savefig.facecolor": "white",
        "figure.facecolor": "white",
    }
)


def style_axes(ax):
    ax.grid(True, alpha=0.25, linewidth=0.8)
    for spine in ax.spines.values():
        spine.set_alpha(0.35)


def save_figure(fig, name: str):
    fig.savefig(FIG_DIR / f"{name}.svg", bbox_inches="tight")
    fig.savefig(FIG_DIR / f"{name}.png", dpi=DPI, bbox_inches="tight")
    fig.savefig(FIG_DIR / f"{name}.pdf", bbox_inches="tight")
    plt.close(fig)


def rounded_box(ax, x, y, w, h, text, fontsize=10):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.015,rounding_size=0.03",
        linewidth=1.2,
        edgecolor="black",
        facecolor="white",
    )
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fontsize)


def figure_light_to_mass_closure():
    fig, ax = plt.subplots(figsize=(11.8, 4.6))
    ax.axis("off")

    rounded_box(ax, 0.04, 0.35, 0.22, 0.30, "free light\nnon-closing phase", fontsize=11)
    rounded_box(ax, 0.31, 0.35, 0.22, 0.30, "phase closure\nself-return", fontsize=11)
    rounded_box(ax, 0.58, 0.35, 0.22, 0.30, "mass shell\nstanding resonance", fontsize=11)
    rounded_box(ax, 0.85, 0.35, 0.11, 0.30, "atomic\nspectrum", fontsize=10.5)

    for start, end in [
        ((0.26, 0.50), (0.31, 0.50)),
        ((0.53, 0.50), (0.58, 0.50)),
        ((0.80, 0.50), (0.85, 0.50)),
    ]:
        ax.add_patch(
            FancyArrowPatch(
                start,
                end,
                arrowstyle="-|>",
                mutation_scale=15,
                linewidth=1.4,
                color="black",
            )
        )

    ax.text(
        0.5,
        0.16,
        "Core thesis map: free propagation -> closure -> mass shell -> spectrum.",
        ha="center",
        fontsize=10.8,
    )
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    save_figure(fig, "light-to-mass-closure")


def figure_free_vs_closed_phase():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.8, 5.0))
    style_axes(ax1)
    style_axes(ax2)

    t = np.linspace(0, 7.5, 450)
    ax1.plot(t, np.sin(3.0 * t), linewidth=1.8, color="black")
    ax1.plot(t, np.sin(3.0 * t + np.pi / 3), linewidth=1.2, linestyle="--", color="black", alpha=0.6)
    ax1.set_title("Free light: non-closing phase transport")
    ax1.set_xlabel("propagation coordinate")
    ax1.set_ylabel("phase amplitude")
    ax1.text(0.3, 1.18, r"$P\bar P=0$", fontsize=10)

    theta = np.linspace(0, 2 * np.pi, 500)
    r = 1.0 + 0.14 * np.cos(4 * theta)
    ax2.plot(r * np.cos(theta), r * np.sin(theta), linewidth=2.0, color="black")
    for angle in [0.2, 1.5, 2.8, 4.0, 5.2]:
        ax2.add_patch(
            FancyArrowPatch(
                (0.72 * np.cos(angle), 0.72 * np.sin(angle)),
                (0.72 * np.cos(angle + 0.4), 0.72 * np.sin(angle + 0.4)),
                arrowstyle="-|>",
                mutation_scale=11,
                linewidth=1.1,
                color="black",
            )
        )
    ax2.set_aspect("equal", adjustable="box")
    ax2.set_title("Closed light: standing-wave closure")
    ax2.set_xlabel("closure axis 1")
    ax2.set_ylabel("closure axis 2")
    ax2.text(-1.35, 1.28, r"$P\bar P=m^2c^2$", fontsize=10)
    ax2.set_xlim(-1.55, 1.55)
    ax2.set_ylim(-1.55, 1.55)

    fig.suptitle("Phase regimes: free propagation vs stable closure", fontsize=12)
    save_figure(fig, "free-vs-closed-phase")


def figure_hydrogen_shell_locking():
    fig, ax = plt.subplots(figsize=(9.8, 5.4))
    style_axes(ax)

    n = np.arange(1, 9)
    s = np.sqrt(2 * n)
    energy = -13.605693 / (n**2)

    ax2 = ax.twinx()
    ax.plot(n, s**2 / 2, marker="o", linewidth=1.8, color="black", label=r"$n=s^2/2$")
    ax2.plot(n, energy, marker="s", linewidth=1.6, linestyle="--", color="black", alpha=0.75, label=r"$E_n=-\mathrm{Ry}/n^2$")

    ax.set_xlabel("shell index n")
    ax.set_ylabel(r"shell-lock value $s^2/2$")
    ax2.set_ylabel(r"energy (eV)")
    ax.set_title("Hydrogen shell locking on S^3 x R_s")

    ax.text(1.15, 7.4, r"$\hat N=\sqrt{-\Delta_{S^3}+1}$", fontsize=10)
    ax.text(1.15, 6.6, r"$\hat N=s^2/2$", fontsize=10)
    ax2.text(4.3, -10.2, r"$E(s)=-4\mathrm{Ry}/s^4$", fontsize=10)

    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, loc="upper right")

    save_figure(fig, "hydrogen-shell-locking")


def figure_series_arc():
    fig, ax = plt.subplots(figsize=(14, 4.8))
    ax.axis("off")
    x_vals = np.linspace(0.04, 0.82, 5)
    y = 0.52
    width, height = 0.15, 0.24
    labels = [
        "Paper 1\nComplex spectral trace\n$\\Xi(t_n)=0$",
        "Paper 2\nQuaternionic slices\n$q_u(t)$",
        "Paper 3\nMass-shell norm\n$P\\bar P=m^2c^2$",
        "Paper 4\nOperator bridge\n$\\mathcal{A}_u$",
        "Paper 5\nCalibration tests\n$L_*$ regimes",
    ]

    for idx, x in enumerate(x_vals):
        rounded_box(ax, x, y - height / 2, width, height, labels[idx], fontsize=10.2)
        if idx < len(x_vals) - 1:
            ax.add_patch(
                FancyArrowPatch(
                    (x + width + 0.01, y),
                    (x_vals[idx + 1] - 0.01, y),
                    arrowstyle="-|>",
                    mutation_scale=14,
                    linewidth=1.4,
                    color="black",
                )
            )

    ax.text(
        0.5,
        0.16,
        "Narrative spine: complex trace  ->  quaternionic geometry  ->  mass shell  ->  eigenvalue bridge  ->  calibration.",
        ha="center",
        va="center",
        fontsize=10.8,
    )
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    save_figure(fig, "perfect-closure-series-arc")


def figure_main_pipeline():
    fig, ax = plt.subplots(figsize=(12.8, 4.2))
    ax.axis("off")
    rounded_box(ax, 0.05, 0.33, 0.25, 0.34, "$\\Xi(t_n)=0$\ncomplex spectral trace", fontsize=11)
    rounded_box(
        ax,
        0.38,
        0.33,
        0.25,
        0.34,
        "$\\mathcal{A}_u\\chi_{t_n}=t_n\\chi_{t_n}$\nquaternionic closure eigenmode",
        fontsize=10.5,
    )
    rounded_box(
        ax,
        0.71,
        0.33,
        0.25,
        0.34,
        "$P\\bar P=(\\hbar t_n/L_*)^2$\nmass-shell realization",
        fontsize=11,
    )
    for start, end in [((0.30, 0.50), (0.38, 0.50)), ((0.63, 0.50), (0.71, 0.50))]:
        ax.add_patch(
            FancyArrowPatch(
                start,
                end,
                arrowstyle="-|>",
                mutation_scale=16,
                linewidth=1.5,
                color="black",
            )
        )
    ax.text(0.5, 0.16, "Shared eigenvalue interpretation (visual summary, not an independent proof).", ha="center")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    save_figure(fig, "zeta-to-mass-shell-pipeline")


def figure_square_root_mirror():
    fig, ax = plt.subplots(figsize=(8.2, 7.8))
    style_axes(ax)
    p = 5
    t = 1.0
    radius = p ** (-0.5)
    phi = t * np.log(p)

    theta = np.linspace(0, 2 * np.pi, 400)
    ax.plot(radius * np.cos(theta), radius * np.sin(theta), linewidth=1.8, label=r"Equal magnitude $1/\sqrt{p}$")

    vectors = [
        (-phi, r"$\frac{1}{\sqrt{p}}e^{-it\log p}$"),
        (phi, r"$\frac{1}{\sqrt{p}}e^{+it\log p}$"),
    ]
    for angle, label in vectors:
        ax.add_patch(
            FancyArrowPatch(
                (0, 0),
                (radius * np.cos(angle), radius * np.sin(angle)),
                arrowstyle="-|>",
                mutation_scale=14,
                linewidth=2.0,
                color="black",
            )
        )
        ax.text(1.1 * radius * np.cos(angle), 1.1 * radius * np.sin(angle), label, fontsize=10, ha="center")

    ax.plot([0, radius], [0, 0], linestyle="--", linewidth=1.0, color="black", alpha=0.65)
    ax.text(radius * 0.55, 0.03, r"phase reference", fontsize=9)
    ax.text(0, -radius * 1.45, r"Critical line $\Re(s)=1/2$: equal magnitude, opposite phase directions", ha="center")
    ax.set_title("Square-root mirror of conjugate prime routes")
    ax.set_xlabel("Real component")
    ax.set_ylabel("Imaginary component")
    ax.set_aspect("equal", adjustable="box")
    lim = radius * 1.9
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.legend(loc="upper right")
    save_figure(fig, "square-root-mirror-prime-routes")


def figure_prime_imbalance_curve():
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    style_axes(ax)
    delta = np.linspace(-0.52, 0.52, 500)
    for p in [2, 3, 5, 11]:
        imbalance = 2 * (p ** (-0.5)) * np.abs(np.sinh(delta * np.log(p)))
        ax.plot(delta, imbalance, linewidth=2.0, label=f"p = {p}")

    ax.axvline(0, linestyle="--", linewidth=1.3, color="black")
    ymax = ax.get_ylim()[1]
    ax.annotate(
        r"$\sigma=1/2$ gives $B_p=0$",
        xy=(0, 0),
        xytext=(0.09, ymax * 0.56),
        arrowprops=dict(arrowstyle="->", linewidth=1.2),
        fontsize=10,
    )
    ax.set_xlabel(r"$\delta$ in $\sigma=\frac{1}{2}+\delta$")
    ax.set_ylabel(r"$B_p(\sigma)=2p^{-1/2}|\sinh(\delta\log p)|$")
    ax.set_title("Prime-route imbalance around the critical line")
    ax.legend()
    save_figure(fig, "prime-imbalance-curve")


def _unit_vectors():
    return [
        (1.0, 0.0, 0.0, r"$u_1=i$"),
        (0.0, 1.0, 0.0, r"$u_2=j$"),
        (0.0, 0.0, 1.0, r"$u_3=k$"),
        (1 / math.sqrt(3), 1 / math.sqrt(3), 1 / math.sqrt(3), r"$u_4$"),
    ]


def figure_quaternionic_slices():
    fig = plt.figure(figsize=(10.8, 7.4))
    ax = fig.add_subplot(111, projection="3d")

    t = np.linspace(-2.5, 2.5, 120)
    for ux, uy, uz, label in _unit_vectors():
        x = np.full_like(t, 0.5)
        y = ux * t
        z = uy * t + 0.2 * uz * t
        linewidth = 2.6 if label == r"$u_1=i$" else 1.8
        ax.plot(x, y, z, linewidth=linewidth, label=label)

    ax.set_xlabel(r"$\Re(q)$")
    ax.set_ylabel(r"$i$-axis component")
    ax.set_zlabel(r"$j/k$-axis component")
    ax.set_xlim(0.2, 0.8)
    ax.set_ylim(-2.7, 2.7)
    ax.set_zlim(-2.7, 2.7)
    ax.set_title(r"Quaternionic critical slices $q_u(t)=1/2+ut$")
    ax.text(0.52, 2.3, 2.2, r"Complex slice: $u=i$", fontsize=10)
    ax.legend(loc="upper left")
    save_figure(fig, "quaternionic-critical-slices")


def figure_six_step_gate():
    fig, ax = plt.subplots(figsize=(8.0, 8.0))
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")

    theta = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(theta), np.sin(theta), linewidth=1.8, color="black")

    for k in range(6):
        angle = k * np.pi / 3
        x, y = np.cos(angle), np.sin(angle)
        ax.plot([0, x], [0, y], linewidth=0.9, color="black", alpha=0.6)
        ax.add_patch(Circle((x, y), 0.045, edgecolor="black", facecolor="white", linewidth=1.0))
        ax.text(1.14 * x, 1.14 * y, rf"$Q^{k}$", ha="center", va="center", fontsize=11)

    ax.text(0, 0.03, r"$Q=e^{u\pi/3}$", ha="center", fontsize=12)
    ax.text(0, -1.27, r"Cadence checkpoints: $Q^3=-1$, $Q^6=1$", ha="center", fontsize=11)
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.4, 1.4)
    save_figure(fig, "six-step-closure-gate")


def _draw_light_cone(ax):
    x = np.linspace(-2.2, 2.2, 200)
    ax.plot(x, np.abs(x), linewidth=1.5, linestyle="--", color="black", label=r"null cone: $P\bar P=0$")
    ax.plot(x, -np.abs(x), linewidth=1.5, linestyle="--", color="black")
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-0.1, 2.4)
    ax.set_xlabel("space-like component")
    ax.set_ylabel("time-like component")
    ax.set_title("Null flow")
    ax.annotate(
        r"$P\bar P=0$",
        xy=(1.2, 1.2),
        xytext=(0.2, 2.0),
        arrowprops=dict(arrowstyle="->", linewidth=1.1),
        fontsize=10,
    )


def _draw_mass_shell(ax):
    x = np.linspace(-2.2, 2.2, 260)
    shell = np.sqrt(1.1**2 + x**2)
    ax.plot(x, shell, linewidth=1.8, color="black", label=r"mass shell: $P\bar P=m^2c^2$")
    ax.plot(x, -shell, linewidth=1.8, color="black")
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-2.4, 2.4)
    ax.set_xlabel("space-like component")
    ax.set_ylabel("time-like component")
    ax.set_title("Massive flow")
    ax.annotate(
        r"$P\bar P=m^2c^2$",
        xy=(0.0, 1.1),
        xytext=(-1.8, 1.95),
        arrowprops=dict(arrowstyle="->", linewidth=1.1),
        fontsize=10,
    )


def figure_mass_shell_norm():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.4, 4.8))
    style_axes(ax1)
    style_axes(ax2)
    _draw_light_cone(ax1)
    _draw_mass_shell(ax2)
    fig.suptitle(r"Conceptual contrast: null/open propagation vs massive/closed shell", fontsize=12)
    save_figure(fig, "mass-shell-norm")


def figure_operator_bridge():
    fig, ax = plt.subplots(figsize=(13.6, 4.9))
    ax.axis("off")
    steps = [
        r"internal scale" + "\n" + r"$\rho$",
        r"closure eigenmode" + "\n" + r"$\chi_t(\rho)$",
        r"quaternionic generator" + "\n" + r"$\mathcal{A}_u$",
        r"zeta selector" + "\n" + r"$\Xi(\mathcal{A}_u)$",
        r"kernel mode at zeros" + "\n" + r"$\Xi(t_n)=0$",
        r"mass-shell lift" + "\n" + r"$L_*$",
    ]
    x_vals = np.linspace(0.03, 0.83, len(steps))
    width, height = 0.13, 0.30

    for i, text in enumerate(steps):
        rounded_box(ax, x_vals[i], 0.35, width, height, text, fontsize=10)
        if i < len(steps) - 1:
            ax.add_patch(
                FancyArrowPatch(
                    (x_vals[i] + width, 0.50),
                    (x_vals[i + 1], 0.50),
                    arrowstyle="-|>",
                    mutation_scale=13,
                    linewidth=1.3,
                    color="black",
                )
            )
    ax.text(
        0.5,
        0.16,
        r"Pipeline logic: $\rho \to \chi_t(\rho) \to \mathcal{A}_u \to \Xi(\mathcal{A}_u) \to$ mass-shell map.",
        ha="center",
        fontsize=10.6,
    )
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    save_figure(fig, "closure-operator-bridge")


def figure_two_faces_of_tn():
    fig, ax = plt.subplots(figsize=(10.8, 4.6))
    ax.axis("off")
    rounded_box(ax, 0.40, 0.38, 0.20, 0.24, r"shared eigenvalue" + "\n" + r"$t_n$", fontsize=12)
    rounded_box(ax, 0.06, 0.30, 0.28, 0.38, r"complex spectral face" + "\n" + r"$\Xi(t_n)=0$", fontsize=11)
    rounded_box(
        ax,
        0.66,
        0.30,
        0.28,
        0.38,
        r"mass-shell face"
        + "\n"
        + r"$P\bar P=\left(\frac{\hbar t_n}{L_*}\right)^2$",
        fontsize=11,
    )
    ax.add_patch(FancyArrowPatch((0.40, 0.50), (0.34, 0.50), arrowstyle="-|>", mutation_scale=14, linewidth=1.5))
    ax.add_patch(FancyArrowPatch((0.60, 0.50), (0.66, 0.50), arrowstyle="-|>", mutation_scale=14, linewidth=1.5))
    ax.text(0.5, 0.16, "One ordinate, two interpretive faces after selecting sector and scale.", ha="center")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    save_figure(fig, "tn-two-faces-bridge")


def figure_calibration_regimes():
    fig, ax = plt.subplots(figsize=(10.5, 5.1))
    style_axes(ax)
    regimes = ["particle-specific $L_*$", "family-specific $L_*$", "universal $L_*$"]
    strength = [1.0, 2.2, 3.1]
    y = np.arange(len(regimes))
    bars = ax.barh(y, strength, edgecolor="black", linewidth=1.0)
    for idx, bar in enumerate(bars):
        ax.text(bar.get_width() + 0.07, bar.get_y() + bar.get_height() / 2, f"tier {idx + 1}", va="center", fontsize=9.5)
    ax.set_yticks(y, labels=regimes)
    ax.set_xlim(0, 3.5)
    ax.set_xlabel("Predictive strictness / falsifiability (illustrative)")
    ax.set_title("Calibration regimes for closure-conversion scale")
    ax.invert_yaxis()
    save_figure(fig, "calibration-regimes")


def figure_inverse_test():
    fig, ax = plt.subplots(figsize=(12.8, 4.8))
    ax.axis("off")
    nodes = [
        r"real mass shell" + "\n" + r"$P\bar P=m^2c^2$",
        r"Compton curvature" + "\n" + r"$k_C=mc/\hbar$",
        r"pulled-back ordinate" + "\n" + r"$\tau=mcL_*/\hbar$",
        r"zeta residual" + "\n" + r"$R_\zeta=|\Xi(\tau)|^2$",
    ]
    x_vals = [0.03, 0.29, 0.55, 0.80]
    width, height = 0.17, 0.34

    for i, text in enumerate(nodes):
        rounded_box(ax, x_vals[i], 0.33, width, height, text, fontsize=10.4)
        if i < len(nodes) - 1:
            ax.add_patch(
                FancyArrowPatch(
                    (x_vals[i] + width, 0.50),
                    (x_vals[i + 1], 0.50),
                    arrowstyle="-|>",
                    mutation_scale=13,
                    linewidth=1.4,
                    color="black",
                )
            )
    ax.text(0.5, 0.16, "Inverse-test workflow: from measured mass data back to zeta-compatibility diagnostics.", ha="center")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    save_figure(fig, "mass-to-zeta-inverse-test")


def main():
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    figure_light_to_mass_closure()
    figure_free_vs_closed_phase()
    figure_hydrogen_shell_locking()
    figure_series_arc()
    figure_main_pipeline()
    figure_square_root_mirror()
    figure_prime_imbalance_curve()
    figure_quaternionic_slices()
    figure_six_step_gate()
    figure_mass_shell_norm()
    figure_operator_bridge()
    figure_two_faces_of_tn()
    figure_calibration_regimes()
    figure_inverse_test()

    print(f"Generated figures in {FIG_DIR}")


if __name__ == "__main__":
    main()

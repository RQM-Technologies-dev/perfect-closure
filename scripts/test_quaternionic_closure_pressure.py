#!/usr/bin/env python3
"""Numerical residue diagnostic for closure-pressure near critical-line zeros.

This script computes xi'(s)/xi(s) for the completed zeta function using mpmath,
evaluates the radial closure-pressure functional Q near known zero heights, and
optionally produces a heatmap around the first zero if matplotlib is available.

Important: this is a numerical local residue diagnostic, not a proof of RH.
"""

from __future__ import annotations

from pathlib import Path

import mpmath as mp

# First known nontrivial zero heights on the critical line (imaginary parts).
ZERO_HEIGHTS = [
    mp.mpf("14.134725141734693"),
    mp.mpf("21.022039638771555"),
    mp.mpf("25.010857580145689"),
    mp.mpf("30.424876125859513"),
    mp.mpf("32.935061587739190"),
]


def xi(s: mp.mpc) -> mp.mpc:
    """Completed zeta xi(s)."""
    return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def xi_prime_over_xi(s: mp.mpc) -> mp.mpc:
    """Compute xi'(s)/xi(s) via numerical differentiation of xi."""
    xival = xi(s)
    if abs(xival) == 0:
        raise ZeroDivisionError("xi(s) is zero at sample point; move to a punctured neighborhood.")
    xip = mp.diff(xi, s)
    return xip / xival


def q_detector(delta: mp.mpf, tau: mp.mpf, gamma: mp.mpf) -> mp.mpf:
    """Radial closure-pressure functional Q(delta, t; gamma) with t = gamma + tau."""
    t = gamma + tau
    s = mp.mpf("0.5") + delta + 1j * t
    lder = xi_prime_over_xi(s)
    return delta * mp.re(lder) - (t - gamma) * mp.im(lder)


def run_table() -> None:
    """Print a small table showing Q≈1 near the listed zero heights."""
    deltas = [mp.mpf("1e-3"), mp.mpf("-1e-3"), mp.mpf("2e-3")]
    taus = [mp.mpf("1e-3"), mp.mpf("-1e-3"), mp.mpf("2e-3")]

    print("Numerical closure-pressure check (Q near simple critical-line zeros)")
    print("All samples are punctured offsets; this is residue diagnostics, not RH proof.")
    print()
    print(f"{'gamma':>18}  {'mean(Q)':>18}  {'max|Q-1|':>18}")
    print("-" * 60)

    for gamma in ZERO_HEIGHTS:
        q_values = []
        for d in deltas:
            for tau in taus:
                q_values.append(q_detector(d, tau, gamma))
        mean_q = mp.fsum(q_values) / len(q_values)
        max_dev = max(abs(qv - 1) for qv in q_values)
        print(f"{mp.nstr(gamma, 15):>18}  {mp.nstr(mean_q, 12):>18}  {mp.nstr(max_dev, 12):>18}")


def maybe_make_heatmap() -> None:
    """Optionally generate a Q heatmap near the first zero if matplotlib is available."""
    try:
        import matplotlib.pyplot as plt
    except Exception:
        print("\nmatplotlib not available; skipping heatmap generation.")
        return

    gamma = ZERO_HEIGHTS[0]
    span = mp.mpf("0.01")
    n = 61
    deltas = [(-span + 2 * span * i / (n - 1)) for i in range(n)]
    taus = [(-span + 2 * span * j / (n - 1)) for j in range(n)]

    # Avoid the exact pole center (delta, tau)=(0,0) by replacing with tiny offset.
    eps = mp.mpf("1e-8")
    data_q = []
    data_dev = []
    for tau in taus:
        row_q = []
        row_dev = []
        for delta in deltas:
            d = eps if abs(delta) < eps and abs(tau) < eps else delta
            tt = eps if abs(delta) < eps and abs(tau) < eps else tau
            qv = q_detector(d, tt, gamma)
            row_q.append(float(qv))
            row_dev.append(float(abs(qv - 1)))
        data_q.append(row_q)
        data_dev.append(row_dev)

    figures_dir = Path("figures")
    figures_dir.mkdir(parents=True, exist_ok=True)

    extent = [float(-span), float(span), float(-span), float(span)]

    fig1 = plt.figure(figsize=(6.0, 4.8))
    ax1 = fig1.add_subplot(111)
    im1 = ax1.imshow(data_q, origin="lower", extent=extent, aspect="auto")
    ax1.set_title("Radial closure-pressure Q near first zero")
    ax1.set_xlabel(r"$\delta$")
    ax1.set_ylabel(r"$\tau = t-\gamma$")
    fig1.colorbar(im1, ax=ax1, label="Q")
    fig1.tight_layout()
    out1 = figures_dir / "quaternionic_closure_pressure_q_heatmap.png"
    fig1.savefig(out1, dpi=180)
    plt.close(fig1)

    fig2 = plt.figure(figsize=(6.0, 4.8))
    ax2 = fig2.add_subplot(111)
    im2 = ax2.imshow(data_dev, origin="lower", extent=extent, aspect="auto")
    ax2.set_title(r"Deviation $|Q-1|$ near first zero")
    ax2.set_xlabel(r"$\delta$")
    ax2.set_ylabel(r"$\tau = t-\gamma$")
    fig2.colorbar(im2, ax=ax2, label=r"$|Q-1|$")
    fig2.tight_layout()
    out2 = figures_dir / "quaternionic_closure_pressure_q_deviation.png"
    fig2.savefig(out2, dpi=180)
    plt.close(fig2)

    print(f"\nSaved heatmaps to: {out1} and {out2}")


def main() -> None:
    mp.mp.dps = 50
    run_table()
    maybe_make_heatmap()


if __name__ == "__main__":
    main()

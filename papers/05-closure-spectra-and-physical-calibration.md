# Closure Spectra and Physical Calibration: From Eigenvalues to Testable Mass Scales

**John Van Geem / RQM Technologies**  
*Research Note — April 2026*

## Abstract

This paper sets the calibration and falsifiability layer for the Perfect Closure research program. From Papers 1–4, the formal bridge is
$$
m_n=\frac{\hbar}{cL_*}|t_n|.
$$
The central question is whether \(L_*\) is independently fixed or stably shared by a physical family. Without that, the bridge is structural calibration rather than prediction. We define resolved closure triples, calibration regimes, ratio and stability tests, failure modes, and falsification criteria.

## Reader Guide

This paper asks whether the bridge predicts anything testable or merely restates known structures. It does not add a new formal operator; it evaluates when the operator bridge from Paper 4 becomes a candidate predictive structure.

## 1. Introduction

Papers 1–4 built a chain from zeta ordinates to closure eigenmodes and then to mass-shell expressions. This final paper asks the scientific question: when does that chain become predictive rather than post hoc?

## 2. Recap of the formal bridge

Let \(t_n\) be a critical-line closure ordinate and define
$$
k_n=\frac{t_n}{L_*},\qquad k_C=\frac{mc}{\hbar}.
$$
Matching \(k_n=k_C\) gives
$$
m_n=\frac{\hbar}{cL_*}|t_n|.
$$
This equation is the calibration target. It does not by itself pick \(n\) or determine \(L_*\).

## 3. Deriving \(L_*\) from resolved closure

From
$$
\frac{t_n}{L_*}=\frac{mc}{\hbar},
$$
one obtains
$$
L_*=t_n\frac{\hbar}{mc}=t_n\bar\lambda_C,
$$
where
$$
\bar\lambda_C=\frac{\hbar}{mc}
$$
is the reduced Compton length.

Interpretation: \(L_*\) is a closure-conversion length from internal log-scale closure to physical curvature scale. This is a consistency relation, not independent evidence for the bridge.

## 4. Resolved Perfect Closure

### Definition 4.1 (Resolved closure triple)

A triple \((t_n,L_*,m_n)\) is a **resolved closure** if
- \(\Xi(t_n)=0\),
- \(\mathcal A_{\mathbf u}\chi_{t_n}=t_n\chi_{t_n}\),
- \(P\bar P=m_n^2c^2=(\hbar t_n/L_*)^2\).

This definition bundles the three faces of the same eigenvalue. It still does not imply that the mapping is predictive in nature.

## 5. Calibration regimes

### A. Particle-specific \(L_*\)
Always fit-able; weakest predictive content.

### B. Family-specific \(L_*\)
Potentially meaningful if stability appears within predeclared families.

### C. Universal \(L_*\)
Strongest and most falsifiable regime.

The progression above tells the reader what level of constraint is being tested. Only constrained regimes can support strong claims.

## 6. Ratio tests

If one \(L_*\) is shared in a family, then
$$
\frac{m_a}{m_b}=\frac{t_m}{t_n}.
$$
This is the simplest consequence to test experimentally. It does not work as evidence unless assignments are predeclared.

Protocol requirements:
- predeclare assignments;
- forbid cherry-picking;
- include measurement uncertainty and tolerance rules;
- use enough points to penalize free choices.

## 7. Scale-stability tests

For assigned pairings \((\text{particle},n)\), compute
$$
L_*(\text{particle},n)=\frac{\hbar t_n}{m_{\text{particle}}c}.
$$
A credible family should show clustering/stability in inferred \(L_*\). If no stable scale appears, the zeta–mass link remains structural rather than predictive.

### Proposed algorithm (pseudocode)

1. Input zeta ordinates list \(\{t_n\}\) and particle masses \(\{m_j\}\).
2. Predeclare assignment map \(j\mapsto n(j)\).
3. Compute inferred \(L_*^{(j)}=\hbar t_{n(j)}/(m_jc)\).
4. Report dispersion metrics (mean, median absolute deviation, robust CV).
5. Hold out one or more masses and test out-of-sample prediction.

No numerical claims are made in this paper.

## 8. What the Synthesis Would Predict

If a shared \(L_*\) is real for a physical family, then mass ratios should track closure-eigenvalue ratios through
\(m_a/m_b=t_m/t_n\) after assignment.

If no stable \(L_*\) appears under predeclared protocols, then the zeta–mass connection remains a structural correspondence and not a predictive law.

This is the point where the series becomes falsifiable: either calibration stabilizes and predicts, or it fails and remains interpretive.

## 9. Avoiding curve fitting

Failure modes include:
- arbitrary zero assignment after seeing data,
- too many adjustable parameters,
- tolerance inflation,
- ratio coincidences without mechanism,
- selective reporting.

This section is included to protect the non-claim boundary and keep inference standards clear.

## 10. Physical mechanism requirement

A predictive theory still requires independent dynamics, including:
- stable quaternionic closed-loop field solutions,
- principled choice of zeta-zero subsets,
- mechanism fixing \(L_*\) (or family scales),
- additional observables beyond fitted masses.

## 11. Evidence standards

Evidence would include:
- predeclared assignment yielding stable \(L_*\),
- successful prediction of withheld masses,
- additional predicted quantum numbers/selection rules,
- independent field simulation recovering the same scale.

## 12. Falsification criteria

The program is falsified (in current form) if:
- no stable \(L_*\) exists for any natural family,
- only post hoc fits are possible,
- no independent mechanism is found,
- no predictions arise beyond re-expression of known masses.

## 13. Conclusion

The disciplined endpoint of the series is:

> Perfect Closure becomes physically meaningful only when closure eigenvalues resolve into stable Compton-scale curvature through an independently justified \(L_*\).

Until then, the bridge remains a formal structural framework requiring calibration, not a completed predictive theory.

## References

1. K. G. Wilson, “The renormalization group and critical phenomena,” *Rev. Mod. Phys.* 55 (1983).
2. R. P. Feynman, *QED: The Strange Theory of Light and Matter*, Princeton Univ. Press, 1985.
3. S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields*, Oxford Univ. Press, 1995.
4. A. M. Odlyzko, tables and computations of zeta zero ordinates (for future computational tests).

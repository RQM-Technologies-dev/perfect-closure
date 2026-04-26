# Closure Spectra and Physical Calibration: From Eigenvalues to Testable Mass Scales

**John Van Geem / RQM Technologies**  
*Research Note — April 2026*

## Abstract

This paper sets the calibration and falsifiability layer for the Perfect Closure research program. From Papers 1–4, the formal bridge is
$$
m_n=\frac{\hbar|t_n|}{cL_*}.
$$
The central question is whether $L_*$ is independently fixed or stably shared by a physical family. Without that, the bridge is calibration rather than prediction. We define resolved closure triples, calibration regimes, ratio and stability tests, failure modes, evidence standards, and falsification criteria.

## 1. Introduction

Papers 1–4 built a formal chain from zeta ordinates to closure eigenmodes and then to mass-shell expressions. This paper asks the scientific question: when does that chain become predictive rather than post hoc?

## 2. Recap of the formal bridge

Let $t_n$ be a critical-line closure ordinate and define
$$
k_n=\frac{t_n}{L_*},\qquad k_C=\frac{mc}{\hbar}.
$$
Matching $k_n=k_C$ gives
$$
m_n=\frac{\hbar|t_n|}{cL_*}.
$$

## 3. Deriving $L_*$ from resolved closure

From
$$
\frac{t_n}{L_*}=\frac{mc}{\hbar},
$$
one obtains
$$
L_*=\frac{t_n\hbar}{mc}=t_n\bar\lambda_C,
$$
where
$$
\bar\lambda_C=\frac{\hbar}{mc}
$$
is the reduced Compton length.

Interpretation: $L_*$ is a closure-conversion length from internal log-scale closure to physical curvature scale.

## 4. Resolved Perfect Closure

### Definition 4.1 (Resolved closure triple)

A triple $(t_n,L_*,m_n)$ is a **resolved closure** if
- $\Xi(t_n)=0$,
- $A_u\chi_{t_n}=t_n\chi_{t_n}$,
- $P\bar P=m_n^2c^2=(\hbar t_n/L_*)^2$.

This is consistency, not yet predictive sufficiency.

## 5. Calibration regimes

### A. Particle-specific $L_*$
Always fit-able; weakest predictive content.

### B. Family-specific $L_*$
Potentially meaningful if stability appears within predeclared families (e.g., leptons, selected hadrons).

### C. Universal $L_*$
Strongest and most falsifiable regime.

## 6. Ratio tests

If one $L_*$ is shared in a family, then
$$
\frac{m_a}{m_b}=\frac{t_m}{t_n}.
$$
Protocol requirements:
- predeclare assignments;
- forbid cherry-picking;
- include measurement uncertainty and tolerance rules;
- use enough points to penalize free choices.

## 7. Scale-stability tests

For assigned pairings $(\text{particle},n)$ compute
$$
L_*(\text{particle},n)=\frac{\hbar t_n}{m_{\text{particle}}c}.
$$
A credible family should exhibit clustering/stability in this inferred scale.

### Proposed algorithm (pseudocode)

1. Input zeta ordinates list $\{t_n\}$ and particle masses $\{m_j\}$.
2. Predeclare assignment map $j\mapsto n(j)$.
3. Compute inferred $L_*^{(j)}=\hbar t_{n(j)}/(m_jc)$.
4. Report dispersion metrics (mean, median absolute deviation, robust CV).
5. Hold out one or more masses and test out-of-sample prediction.

No numerical claims are made here.

## 8. Avoiding curve fitting

Failure modes include:
- arbitrary zero assignment after seeing data,
- too many adjustable parameters,
- tolerance inflation,
- ratio coincidences without mechanism,
- selective reporting.

## 9. Physical mechanism requirement

A predictive theory requires independent dynamics, including:
- stable quaternionic closed-loop field solutions,
- principled choice of zeta-zero subsets,
- mechanism fixing $L_*$ (or family scales),
- additional observables beyond fitted masses.

## 10. Evidence standards

Evidence would include:
- predeclared assignment yielding stable $L_*$,
- successful prediction of withheld masses,
- additional predicted quantum numbers/selection rules,
- independent field simulation recovering same scale.

## 11. Falsification criteria

The program is falsified (in current form) if:
- no stable $L_*$ exists for any natural family,
- only post hoc fits are possible,
- no independent mechanism is found,
- no predictions arise beyond re-expression of known masses.

## 12. Conclusion

The disciplined endpoint of the series is:

> Perfect Closure becomes physically meaningful only when closure eigenvalues resolve into stable Compton-scale curvature through an independently justified $L_*$.

Until then, the bridge remains a calibration framework, not a completed predictive theory.

## References

1. K. G. Wilson, “The renormalization group and critical phenomena,” *Rev. Mod. Phys.* 55 (1983).
2. R. P. Feynman, *QED: The Strange Theory of Light and Matter*, Princeton Univ. Press, 1985.
3. S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields*, Oxford Univ. Press, 1995.
4. A. M. Odlyzko, tables and computations of zeta zero ordinates (for future computational tests).

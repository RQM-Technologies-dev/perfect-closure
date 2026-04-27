# Predictive Closure and the Conversion Scale: When Zeta-Mass Matching Becomes Testable

**John Van Geem / RQM Technologies**  
*Preprint - April 2026*

## Abstract

This paper studies the scientific status of the conversion scale \(L_*\) in the zeta-mass bridge. From \(m_n=(\hbar/(cL_*))|t_n|\), the bridge is descriptive if \(L_*\) is tuned separately for each mass and predictive only when \(L_*\) is fixed independently or stabilized over a predeclared family. We define four testing protocols—fixed-scale prediction, family-stabilized scale, out-of-sample matching, and null tests—and explain why these protocols are the decisive criterion for independent physical content.

## 1. Introduction

Papers 1--4 established a coherent chain: zeta closure labels \(t_n\), quaternionic representation, operator selection, and mass-shell realization. Paper 5 asks the methodological question: when does this chain predict anything new?

The answer hinges on one number, \(L_*\). If that scale can move freely for each target, agreement can be retrospective. If the scale is fixed before fitting, agreement can be tested.

## 2. Core calibration equation

From Paper 4,
\[
m_n=\frac{\hbar}{cL_*}|t_n|,
\]
or equivalently
\[
L_*=t_n\frac{\hbar}{m_nc}.
\]
This equation should be read in two directions. Forward direction predicts \(m_n\) from \(t_n\) and a pre-fixed \(L_*\). Backward direction infers \(L_*\) from assigned pairs.

The bridge becomes meaningful only when the forward direction survives predeclared tests.

## 3. Descriptive versus predictive use of \(L_*\)

### Definition 1 (Descriptive scaling)
A fit is descriptive if \(L_*\) is chosen independently for each mass target.

### Definition 2 (Predictive scaling)
A fit is predictive if \(L_*\) is fixed independently of the target masses before comparison.

### Definition 3 (Family-stabilized scaling)
A fit is family-stabilized when a single predeclared \(L_*\) is used for a predeclared class and remains stable under held-out checks.

These definitions separate mathematical compatibility from empirical content.

![Calibration regimes chart](../assets/figures/calibration-regimes.svg)

*Figure 1. Predictive strength increases as freedom in \(L_*\) decreases.*

## 4. Testing protocols

### Protocol A: Fixed-scale prediction
Choose \(L_*\) from external criteria before any mass matching. Predict masses for assigned \(t_n\) values. Evaluate residuals without retuning \(L_*\).

### Protocol B: Family-stabilized scale
Predeclare a family and pairing rule. Estimate one \(L_*\) on a training subset, then test on a held-out subset from the same family.

### Protocol C: Out-of-sample mass matching
After fixing \(L_*\), predict masses for a second family not used in calibration. This is the strongest practical check against hidden overfitting.

### Protocol D: Null tests
Apply random or deliberately mismatched pairings under the same scoring rule. A viable bridge should outperform null baselines by a clear margin.

## 5. Quantitative diagnostics

Useful diagnostics include:
\[
\text{CV}(L_*)=\frac{\text{std}(L_*^{(j)})}{\text{mean}(L_*^{(j)})},
\]
for family stability, and held-out prediction error
\[
\varepsilon_{\text{test}}=\frac{1}{N}\sum_{j=1}^N\frac{|m_j^{\text{pred}}-m_j^{\text{obs}}|}{m_j^{\text{obs}}}.
\]

For ratio checks with shared \(L_*\),
\[
\frac{m_a}{m_b}\approx\frac{t_{n_a}}{t_{n_b}}.
\]
This removes \(L_*\) and tests internal proportionality directly.

![Mass-to-zeta inverse test](../assets/figures/mass-to-zeta-inverse-test.svg)

*Figure 2. Inverse evaluation pipeline for null and out-of-sample testing.*

## 6. Discussion

The scientific criterion for this series is not whether one can write a bridge equation; that part is easy. The criterion is whether \(L_*\) carries independent constraint. If not, the bridge remains a descriptive identity.

What this does not show is a proof of RH or a derivation of the Standard Model spectrum. It shows how to ask a falsifiable question about independent physical content.

## 7. Conclusion

The role of \(L_*\) is decisive. Per-target \(L_*\) is descriptive; independently fixed \(L_*\) is predictive; stable \(L_*\) over predeclared families is testable. Paper 5 therefore closes the series by turning methodological discipline into part of the mathematical claim itself.

## References

[1] K. G. Wilson, “The renormalization group and critical phenomena,” *Rev. Mod. Phys.* 55 (1983).  
[2] E. C. Titchmarsh and D. R. Heath-Brown, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford Univ. Press, 1986.  
[3] S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields*, Oxford Univ. Press, 1995.

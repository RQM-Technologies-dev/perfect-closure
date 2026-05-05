# Closure Spectra and Physical Calibration: When Zeta-Mass Matching Becomes Testable

**John Van Geem / RQM Technologies**  
*Preprint - April 2026*

## Abstract

This paper treats calibration as the decisive scientific step in the closure program. The mathematical bridge from selected spectral values to mass-shell values is easy to write, but scientific content appears only when the conversion scale is constrained independently of the targets being matched. The paper distinguishes descriptive fitting from predictive testing, introduces family-stabilized calibration as an intermediate regime, and proposes out-of-sample protocols with explicit failure criteria. The goal is to ensure that spectral-mass matching is evaluated as a falsifiable research program rather than as symbolic pattern matching.

## 1. Introduction

The previous papers built a formal chain from completed residual selection to mass-shell compatibility. Paper 5 asks the methodological question that determines whether the chain has empirical force: can the scale parameter be fixed independently enough to make failures possible?

Without this step, one can always retune parameters and recover agreement retrospectively. With this step, the framework becomes testable.

For that reason, this paper is not an appendix to the mathematics; it is the methodological center of physical interpretation. Calibration decides whether the proposed bridge can ever be wrong in a meaningful way.

## 2. Mathematical Background

The bridge equation from Paper 4 is
\[
m_n=\frac{\hbar}{cL_*}|t_n|.
\]
Equivalently,
\[
L_*=t_n\frac{\hbar}{m_nc}.
\]
The same formula can be used in two opposite ways. Forward use predicts mass from a predeclared scale. Backward use infers scale from known mass. Only the first route carries predictive risk.

## 3. Main Construction

Calibration regimes can be ordered by decreasing parameter freedom.

1. **Per-target scaling:** a different scale is chosen for each target; this is descriptive.
2. **Family-stabilized scaling:** one scale is fixed for a predeclared class and tested on held-out members.
3. **Global predeclared scaling:** a single externally motivated scale is fixed before all comparisons.

The scientific value increases as freedom decreases.

The ordering above should be read as a hierarchy of evidential strength, not merely as a list of computational options. A method that cannot fail under independent tests cannot supply physical support, even if it produces visually impressive matches.

![Calibration regimes](../assets/figures/calibration-regimes.svg)

*Figure 1. Predictive strength rises as the number of free calibration choices falls.*

## 4. Formal Definitions and Results

### Definition 1 (Descriptive match)
A match is descriptive if \(L_*\) is tuned separately for each mass target.

### Definition 2 (Predictive match)
A match is predictive if \(L_*\) is fixed independently of the target data before scoring.

### Definition 3 (Family stabilization)
A family is stabilized when one predeclared \(L_*\) remains within a narrow tolerance under held-out tests in that same family.

### Proposition 1 (Falsifiability criterion)
The bridge has empirical content only when the calibration protocol allows potential rejection under predeclared error thresholds.

### Protocol recommendations

- **Pre-registration:** declare pairing rules, admissible spectral indices, and score functions before fitting.
- **Split design:** reserve a held-out subset that is never used during scale selection.
- **Null benchmarking:** compare against shuffled assignments and random baselines under the same metric.
- **Sensitivity audit:** report how predictions vary under small perturbations of the declared protocol.

### Diagnostic quantities
A useful stability index is
\[
\mathrm{CV}(L_*)=\frac{\mathrm{std}(L_*^{(j)})}{\mathrm{mean}(L_*^{(j)})}.
\]
A useful held-out error is
\[
\varepsilon_{\mathrm{test}}=\frac{1}{N}\sum_{j=1}^N\frac{|m_j^{\mathrm{pred}}-m_j^{\mathrm{obs}}|}{m_j^{\mathrm{obs}}}.
\]

## 5. Interpretation

Calibration is where descriptive mathematics either becomes predictive science or remains a compatibility map. If a new scale can be chosen for every target, apparent success carries little evidential value. If the scale is fixed first and still performs well on new data, the result becomes informative.

Out-of-sample design is therefore mandatory. It should include null pairings, shuffled assignments, and predeclared acceptance thresholds. Failure should be counted as informative, not as a nuisance to be tuned away.

Clear failure criteria are essential. Examples include unstable calibrated scale values across adjacent data splits, held-out error that is not distinguishable from null baselines, or sensitivity so high that minor protocol edits reverse conclusions. Any of these outcomes should be treated as evidence against predictive status.

## 6. Relation to the Series

Paper 5 closes the logical arc:
- Paper 1 supplied completed residual selection,
- Paper 2 supplied conservative slice lifting,
- Paper 3 supplied invariant mass-shell norm structure,
- Paper 4 supplied operator mapping,
- and Paper 5 supplies the calibration discipline required for testability.

Without this final step, the series risks remaining symbolic.

## 7. Conclusion

The central methodological claim is simple: calibration discipline determines scientific status. Per-target scales are descriptive, independently fixed scales are predictive, and family-stable behavior under held-out tests is candidate evidence. The closure program therefore stands or falls on out-of-sample performance under predeclared rules.

In that sense, Paper 5 is the guardrail paper of the series. It prevents the earlier operator bridge from being interpreted as a guaranteed discovery pipeline and recasts it as a testable proposal with explicit criteria for success and failure.

## References

[1] K. G. Wilson, “The renormalization group and critical phenomena,” *Rev. Mod. Phys.*, 1983.  
[2] E. C. Titchmarsh and D. R. Heath-Brown, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford Univ. Press, 1986.  
[3] S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields*, Oxford Univ. Press, 1995.

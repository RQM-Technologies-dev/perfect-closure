# The Zeta-Mass Closure Operator: Perfect Closure as a Shared Spectral Eigenvalue Law

**John Van Geem / RQM Technologies**  
*Preprint - April 2026*

## Abstract

This paper builds an operator bridge between critical-line spectral data and relativistic mass-shell structure. A dilation-type operator with a half shift is introduced because that form naturally isolates the critical-line coordinate used in the earlier papers. The spectral mode is then chosen so that eigenvalue extraction can be shown step by step, and the completed residual is used as a selector of admissible spectral points. In this framework a zero condition is converted into a kernel condition, after which the same selected value is mapped into a mass-shell expression. The paper emphasizes that the conversion scale determines whether the bridge is merely descriptive or genuinely predictive.

## 1. Introduction

Papers 1 through 3 prepared three pieces: a completed residual criterion, a conservative quaternionic lift, and a relativistic norm target. Paper 4 combines these pieces in an explicit operator law.

The aim is not rhetorical synthesis. The aim is to show the exact route by which one scalar spectral parameter can appear in both analytic and mass-shell expressions.

## 2. Mathematical Background

A natural starting point is the dilation generator
\[
D=-i\left(x\frac{d}{dx}+\frac12\right).
\]
The half shift is included so that the Mellin-side correspondence aligns with the symmetric critical-line placement. This shift is structural, not decorative.

For a slice direction \(u\), define the slice operator
\[
\mathcal A_u=-u\left(x\frac{d}{dx}+\frac12\right).
\]
The operator acts on mode functions that are compatible with Mellin-type scaling behavior.

## 3. Main Construction

Choose the mode
\[
\chi_t(x)=x^{-1/2+ut}.
\]
Then
\[
\begin{aligned}
\mathcal A_u\chi_t
&=-u\left(x\frac{d}{dx}+\frac12\right)x^{-1/2+ut}\\
&=-u(ut)\,x^{-1/2+ut}
=t\,\chi_t,
\end{aligned}
\]
so \(t\) is the eigenvalue. This step makes the shared scalar variable explicit.

Next define a residual-selected operator
\[
\mathcal K_u=\Xi(\mathcal A_u),
\]
where \(\Xi\) is the completed residual map from Paper 1. For any selected ordinate \(t_n\) with \(\Xi(t_n)=0\), one obtains
\[
\mathcal K_u\chi_{t_n}=0.
\]
Thus a completed-zero condition becomes a kernel condition.

![Closure operator bridge](../assets/figures/closure-operator-bridge.svg)

*Figure 1. The selected spectral ordinate appears both as an operator eigenvalue and as a mass-shell input variable.*

## 4. Formal Definitions and Results

### Definition 1 (Residual-selected mode)
A mode \(\chi_t\) is residual-selected when \(\Xi(t)=0\).

### Proposition 1
If \(\chi_t\) is an eigenmode of \(\mathcal A_u\) with eigenvalue \(t\), then residual selection implies \(\chi_t\in\ker\mathcal K_u\).

### Definition 2 (Mass mapping)
Given a length scale \(L_*\), define
\[
m_t=\frac{\hbar}{cL_*}|t|.
\]
Then
\[
P\bar P=m_t^2c^2=\left(\frac{\hbar t}{L_*}\right)^2.
\]

### Remark
The map above is a compatibility law unless \(L_*\) is independently fixed before comparison to data.

## 5. Interpretation

The operator law has three logically distinct steps: spectral extraction, residual selection, and physical scaling. The first two are purely mathematical. The third introduces empirical content and therefore calibration risk.

This separation is essential for honest interpretation. Without it, symbolic consistency can be mistaken for prediction.

## 6. Relation to the Series

Paper 4 is the hinge paper. It receives the critical-line residual from Paper 1, the slice language from Paper 2, and the mass-shell invariant from Paper 3. Paper 5 then asks whether the scale required here can be set in a testable way.

## 7. Conclusion

A dilation-style operator with half shift yields a clean eigenvalue law in which the critical-line height variable is explicit. Residual vanishing then acts as a spectral selector, and selected values map into a mass-shell expression through a conversion scale. The bridge is mathematically coherent, but predictive status depends entirely on independent calibration of that scale.

## References

[1] E. C. Titchmarsh and D. R. Heath-Brown, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford Univ. Press, 1986.  
[2] J. B. Conrey, “The Riemann Hypothesis,” *Notices of the AMS*, 2003.  
[3] S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields*, Oxford Univ. Press, 1995.

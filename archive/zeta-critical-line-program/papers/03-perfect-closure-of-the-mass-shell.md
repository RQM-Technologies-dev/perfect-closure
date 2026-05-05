# Mass-Shell Perfect Closure: Closed Quaternionic Light and Relativistic Norm Structure

**John Van Geem / RQM Technologies**  
*Preprint - April 2026*

## Abstract

This paper reformulates the relativistic mass-shell relation in a quaternion-compatible norm language and explains why that reformulation matters for the closure series. The invariant target is obtained by pairing a momentum expression with its conjugate so that orientation data cancels and a scalar norm remains. This makes it possible to distinguish null propagation from massive closure in one algebraic template. The paper treats the phrase that closed light appears as mass as an interpretation grounded in invariant norm structure rather than as a microscopic dynamical claim, and it introduces Compton curvature as the bridge to the operator construction of the next paper.

## 1. Introduction

Special relativity already contains a closure principle: many coordinate descriptions reduce to one invariant scalar. Paper 3 emphasizes this reduction explicitly and links it to the quaternionic representation language introduced in Paper 2.

The tone remains cautious. We do not alter the standard relativistic equation. We repackage it so that the same invariant appears as a conjugate norm product.

## 2. Mathematical Background

The relativistic shell relation is
\[
E^2=p^2c^2+m^2c^4,
\]
or equivalently
\[
\frac{E^2}{c^2}-|\mathbf p|^2=m^2c^2.
\]
The right-hand side is the invariant target. Any alternative notation is acceptable only if it returns this same scalar quantity.

To prepare for quaternionic packaging, introduce a formal imaginary unit \(I\) with \(I^2=-1\), and define
\[
P=\frac{E}{c}+I\mathbf p,
\qquad
\bar P=\frac{E}{c}-I\mathbf p.
\]

## 3. Main Construction

Multiply by the conjugate:
\[
\begin{aligned}
P\bar P
&=\left(\frac{E}{c}+I\mathbf p\right)\left(\frac{E}{c}-I\mathbf p\right)\\
&=\left(\frac{E}{c}\right)^2-(I\mathbf p)^2
=\frac{E^2}{c^2}-|\mathbf p|^2.
\end{aligned}
\]
Using the relativistic shell relation gives
\[
P\bar P=m^2c^2.
\]

The explanatory value of this step is that orientation information carried by \(I\mathbf p\) is neutralized in the product. What remains is exactly the invariant scalar.

![Mass-shell norm structure](../assets/figures/mass-shell-norm.svg)

*Figure 1. Conjugate multiplication removes orientation data and returns the relativistic invariant.*

## 4. Formal Definitions and Results

### Definition 1 (Null propagation)
A mode is null when
\[
P\bar P=0.
\]
This corresponds to massless propagation.

### Definition 2 (Massive closure)
A mode is massive when
\[
P\bar P>0,
\]
with invariant value \(m^2c^2\).

### Proposition 1
The conjugate product \(P\bar P\) is Lorentz-invariant and equal to the standard mass-shell scalar.

**Interpretation.** This proposition identifies the invariant as the closure target: open null transport gives zero invariant, while closed massive structure gives positive invariant.

### Remark (Interpretive language)
The phrase “light that has closure becomes mass” should be read as a compact description of this norm transition. It is not a claim that a complete microscopic generation mechanism has been derived.

## 5. Interpretation

The null-to-massive distinction is transparent in the norm picture. Null propagation corresponds to unresolved trajectory closure in invariant terms. Massive modes correspond to a closed invariant norm that survives conjugate cancellation of orientation. This is why the conjugate product form is useful pedagogically: it makes invariant closure visible.

Compton curvature enters as the physical conversion map
\[
k_C=\frac{mc}{\hbar}.
\]
It translates between mass scale and characteristic inverse length. In this series, it prepares the bridge from relativistic norm statements to spectral operator statements.

## 6. Relation to the Series

Paper 1 supplied the completed residual on the critical line. Paper 2 showed that the same scalar closure data can be carried across quaternionic slice orientations. Paper 3 now supplies the relativistic norm target that later receives spectral input.

Thus Paper 3 is the physical normalization step: it states what quantity must be matched if a zeta-linked operator law is to have physical meaning.

## 7. Conclusion

The mass shell can be written as a conjugate norm product without changing its physics. That rewrite distinguishes null and massive modes in a closure-compatible form and clarifies the interpretive status of closure language. Compton curvature then provides the conversion bridge required for the operator law in Paper 4.

## References

[1] A. Einstein, *Zur Elektrodynamik bewegter Korper*, 1905.  
[2] W. Pauli, *Theory of Relativity*, Dover, 1981.  
[3] S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields*, Oxford Univ. Press, 1995.

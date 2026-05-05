# The Quaternionic Lift of the Critical Line: Complex Planes at Every Slice

**John Van Geem / RQM Technologies**  
*Preprint - April 2026*

## Abstract

This paper studies the quaternionic lift space that contains the classical critical line as one slice among many complex planes. Each unit imaginary direction in quaternion space defines a valid complex slice, so the ordinary complex line is recovered as a special case rather than discarded. The height parameter is preserved while the orientation axis is allowed to vary, and the completed residual is packaged slice by slice with unchanged scalar norm. The construction is therefore an embedding of complex analysis into a larger representation space, not a replacement of complex analysis.

## 1. Introduction

The first paper identified a scalar closure score on the critical line. The present paper asks whether the same score can be represented in a larger geometric setting without altering analytic meaning. Quaternion space provides exactly this possibility because it contains many internal complex planes.

The conservative intent is crucial. We do not introduce a new zeta function and we do not claim new zero locations. We reorganize representation, not analytic content.

Why this matters pedagogically is that many readers first encounter the critical line as a rigid picture in one complex plane. Quaternionic language shows that the same analytic data can be carried by many internal orientations. This reframes the critical line from a single drawing into a slice family while preserving the underlying scalar content.

## 2. Mathematical Background

A quaternion can be written as
\[
q=a+b\mathbf i+c\mathbf j+d\mathbf k,
\]
with the Hamilton relations \(\mathbf i^2=\mathbf j^2=\mathbf k^2=\mathbf i\mathbf j\mathbf k=-1\). Any unit pure imaginary quaternion \(u\) satisfies \(u^2=-1\), so it behaves like an imaginary unit inside its own slice.

### Definition 1 (Quaternionic slice)
For a unit imaginary \(u\), define
\[
\mathbb C_u=\{a+ub:\ a,b\in\mathbb R\}.
\]

### Proposition 1
Each \(\mathbb C_u\) is algebraically isomorphic to the ordinary complex plane.

**Interpretation.** Quaternion space contains a sphere of complex planes. The usual complex plane is one member of this family.

In classroom terms, one can think of each unit imaginary direction as choosing a compass needle for phase rotation. The algebraic rules do not break when the needle changes; each choice gives a valid complex arithmetic inside the larger quaternion algebra. This is the technical reason the lift is an embedding.

## 3. Main Construction

The classical critical line uses
\[
s=\frac12+it.
\]
The lifted family is
\[
q_u(t)=\frac12+ut,
\]
with the same real height parameter \(t\). The only change is orientation axis.

This is why the lift is conservative: the scalar progression in \(t\) is untouched. The construction embeds the complex plane rather than replacing it.

It is useful to stress what does not change. The completed residual remains the same scalar function of the same real height variable. The only moving part is the internal imaginary axis used to display the pair of real and imaginary components. Therefore no new critical-line parameter is created.

![Quaternionic critical slices](../assets/figures/quaternionic-critical-slices.svg)

*Figure 1. The critical line viewed as one slice in a quaternionic family of complex planes.*

## 4. Formal Definitions and Results

### Definition 2 (Slice packaging of the completed residual)
Let
\[
\Xi(t)=\xi\!\left(\frac12+it\right).
\]
For a chosen unit imaginary \(u\), define
\[
\xi_{\mathbb H}\!\left(\frac12+ut\right)=\Re\Xi(t)+u\Im\Xi(t).
\]

### Proposition 2 (Norm preservation)
For every unit imaginary \(u\),
\[
\left\|\xi_{\mathbb H}\!\left(\frac12+ut\right)\right\|^2=|\Xi(t)|^2.
\]

**Proof sketch.** Any slice element has form \(x+uy\) with norm-square \(x^2+y^2\). Substituting \(x=\Re\Xi(t)\), \(y=\Im\Xi(t)\) yields the claim.

### Remark (Conservative lift)
Because the scalar norm is unchanged, this lift preserves the closure score of Paper 1 exactly.

## 5. Interpretation

The geometric gain is conceptual clarity. Quaternions show that there is no single privileged imaginary axis in representation space. What is privileged is the scalar closure data carried by \(t\) and by \(|\Xi(t)|\). The orientation axis can vary without changing that scalar content.

This also explains why norm preservation matters. If the norm changed with slice choice, the lift would alter the closure criterion and therefore cease to be conservative.

Another way to say this is that slice freedom is a gauge-like freedom of representation, not a freedom to change scalar predictions. Invariant norm is the compatibility condition that prevents the lift from drifting into a different theory.

## 6. Relation to the Series

Paper 2 prepares the algebraic language needed later for mass-shell packaging. The six-step closure cadence remains a secondary motif:
\[
Q=e^{u\pi/3},\qquad Q^3=-1,\qquad Q^6=1.
\]
This cadence is geometric intuition, not a theorem about zero placement.

Readers should therefore treat the six-step pattern as a geometric mnemonic. It is helpful when visualizing repeated phase turns in a selected slice, but it is not the mathematical engine of the residual criterion.

## 7. Conclusion

Quaternion space provides a family of complex slices, each generated by a unit imaginary direction. The critical line lifts to every slice while preserving the scalar height parameter and the scalar residual norm. The resulting framework is a representation-theoretic extension that keeps complex analysis intact and sets up the norm-based physics bridge of the next papers.

## References

[1] W. R. Hamilton, *Elements of Quaternions*, 1866.  
[2] S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields*, Oxford Univ. Press, 1995.  
[3] E. C. Titchmarsh and D. R. Heath-Brown, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford Univ. Press, 1986.

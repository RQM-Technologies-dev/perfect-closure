# Quaternionic Lift Space for Complex Critical-Line Slices

**John Van Geem / RQM Technologies**  
*Technical Manuscript - April 2026*

## 1. Abstract

This paper introduces a quaternionic lift space for the critical-line coordinate used in Paper 1. The key representation idea is that quaternion algebra \(\mathbb H\) contains a family of embedded complex planes \(\mathbb C_{\mathbf u}\), one for each unit imaginary quaternion \(\mathbf u\) with \(\mathbf u^2=-1\). In this view, the classical coordinate \(s=1/2+it\) is recovered as the special slice \(\mathbf u=i\), while the lifted family is \(q_{\mathbf u}(t)=1/2+\mathbf u t\). We then package the completed residual slice-wise via \(\Xi(t)=\xi(1/2+it)\) and \(\xi_{\mathbb H}(1/2+\mathbf u t)=\Re\Xi(t)+\mathbf u\Im\Xi(t)\), and prove the scalar norm identity \(\|\xi_{\mathbb H}(1/2+\mathbf u t)\|^2=|\Xi(t)|^2\). The result is a conservative dimensional lift: it embeds complex critical-line data into a higher-dimensional orientation family without replacing complex analysis or asserting a quaternionic proof of zero placement. Perfect Closure remains the series context rather than the primary claim of this paper.

## 2. Keywords

quaternionic lift space; critical line; complex slices; completed residual; representation-preserving embedding; perfect closure series.

## 3. Introduction

Paper 1 worked on the classical complex critical line \(s=1/2+it\). Paper 2 asks a representation question: can the same critical-line structure be placed inside a higher-dimensional quaternionic space without losing the original complex plane? The answer is yes. Quaternion algebra \(\mathbb H\) contains infinitely many complex slices \(\mathbb C_{\mathbf u}\), each indexed by a unit imaginary quaternion \(\mathbf u\).

This matters because the line \(1/2+it\) is usually presented in one fixed orientation (the \(i\)-axis). In quaternionic language, that classical orientation is a special case inside a broader slice family. The dimensional lift therefore adds orientation freedom while preserving the real height parameter \(t\).

The paper is intentionally conservative. The lift does not replace complex analysis; it embeds it. The construction does not generate new zeta zeros; it repackages the same completed residual data in a slice-wise coordinate family that will be reused in the operator and mass-shell papers.

## 4. Contributions

1. We define quaternionic lift space \(\mathbb H\) as a family of embedded complex planes \(\mathbb C_{\mathbf u}\).
2. We show that choosing \(\mathbf u=i\) recovers the ordinary complex plane and the classical critical line.
3. We define \(q_{\mathbf u}(t)=1/2+\mathbf u t\) as the slice lift of the critical-line coordinate.
4. We distinguish affine slice lift coordinates from unit-quaternion phase motion \(Q=e^{\mathbf u\phi}\).
5. We define slice-wise packaging of the completed residual and prove scalar norm preservation:
   \[
   \|\xi_{\mathbb H}(1/2+\mathbf u t)\|^2=|\Xi(t)|^2.
   \]
6. We explain how this coordinate language prepares Paper 3 (mass-shell norm form) and Paper 4 (operator bridge).

## 5. Quaternionic Preliminaries

A quaternion is
\[
q=a+b\mathbf i+c\mathbf j+d\mathbf k,\qquad a,b,c,d\in\mathbb R,
\]
with Hamilton rules \(\mathbf i^2=\mathbf j^2=\mathbf k^2=\mathbf i\mathbf j\mathbf k=-1\). The real part is \(\Re(q)=a\), and the imaginary part is \(b\mathbf i+c\mathbf j+d\mathbf k\).

Unlike \(\mathbb C\), where there is one distinguished imaginary unit \(i\), quaternions have a 2-sphere of unit imaginary directions. Any unit vector
\[
\mathbf u=u_1\mathbf i+u_2\mathbf j+u_3\mathbf k,\qquad u_1^2+u_2^2+u_3^2=1,
\]
satisfies \(\mathbf u^2=-1\). This multiplicity of imaginary axes is the geometric source of the slice family.

**Definition 1 (Unit imaginary quaternion).** A quaternion \(\mathbf u\in\mathbb H\) is unit imaginary if \(\Re(\mathbf u)=0\), \(\|\mathbf u\|=1\), and \(\mathbf u^2=-1\).

## 6. Complex Slices Inside Quaternion Space

For each unit imaginary \(\mathbf u\), define
\[
\mathbb C_{\mathbf u}=\{a+\mathbf u b:\ a,b\in\mathbb R\}.
\]

**Definition 2 (Quaternionic complex slice).** \(\mathbb C_{\mathbf u}\) is the 2D real affine plane spanned by \(1\) and \(\mathbf u\), with multiplication inherited from \(\mathbb H\).

Within any fixed slice \(\mathbb C_{\mathbf u}\), algebra behaves exactly like complex arithmetic because \(\mathbf u^2=-1\). Thus the familiar complex form \(a+ib\) becomes \(a+\mathbf u b\) without changing the two-real-parameter structure.

**Proposition 1.** Each \(\mathbb C_{\mathbf u}\) is algebraically isomorphic to \(\mathbb C\).

*Proof sketch.* Define \(\varphi_{\mathbf u}:\mathbb C\to\mathbb C_{\mathbf u}\) by \(\varphi_{\mathbf u}(a+ib)=a+\mathbf u b\). The map is bijective and preserves addition and multiplication since both use a unit squaring to \(-1\). Therefore \(\varphi_{\mathbf u}\) is an algebra isomorphism.

The point is representation breadth, not replacement: complex analysis remains valid on each slice, and \(\mathbb C\) is recovered exactly when \(\mathbf u=i\).

![Quaternionic critical slices](../assets/figures/quaternionic-critical-slices.svg)

*Figure 1. The classical critical line appears as the \(\mathbf u=i\) trace inside the quaternionic slice family \(q_{\mathbf u}(t)\).* 

## 7. Lifting the Critical Line

The classical critical-line coordinate is
\[
s=\frac12+it,\qquad t\in\mathbb R.
\]
The quaternionic slice lift is
\[
q_{\mathbf u}(t)=\frac12+\mathbf u t.
\]

**Definition 3 (Critical-line slice lift).** For fixed unit imaginary \(\mathbf u\), the map \(t\mapsto q_{\mathbf u}(t)\) is the affine trace of the critical-line parameter in slice \(\mathbb C_{\mathbf u}\).

This lift is conservative:
- \(t\) is unchanged as the same real height parameter;
- only orientation unit changes from \(i\) to \(\mathbf u\);
- selecting \(\mathbf u=i\) gives the original line exactly.

**Proposition 2.** The choice \(\mathbf u=i\) recovers the classical critical line.

*Proof sketch.* Substitute \(\mathbf u=i\) into \(q_{\mathbf u}(t)\): \(q_i(t)=1/2+it=s\). No reparameterization is required.

It is also useful to separate affine lift coordinates from phase trajectories on the unit sphere:
\[
Q=e^{\mathbf u\phi}=\cos\phi+\mathbf u\sin\phi.
\]
The former is translated-line geometry in \(\Re(q)=1/2\), while the latter is unit-norm rotation. They are related motifs but distinct objects.

## 8. Slice Preservation of the Completed Residual

Define the standard completed residual on the classical line:
\[
\Xi(t)=\xi\!\left(\frac12+it\right).
\]
Package it slice-wise by
\[
\xi_{\mathbb H}\!\left(\frac12+\mathbf u t\right)=\Re\Xi(t)+\mathbf u\Im\Xi(t).
\]

This is not a new zeta function; it is a quaternionic packaging of the same real and imaginary components of \(\Xi(t)\) along the same parameter \(t\).

**Proposition 3.** The slice-packaged residual preserves scalar norm:
\[
\left\|\xi_{\mathbb H}\!\left(\frac12+\mathbf u t\right)\right\|^2=|\Xi(t)|^2.
\]

*Proof sketch.* For a quaternion of the form \(x+\mathbf u y\), norm-square is \(x^2+y^2\). Here \(x=\Re\Xi(t)\), \(y=\Im\Xi(t)\), so
\[
\|\xi_{\mathbb H}(1/2+\mathbf u t)\|^2=(\Re\Xi(t))^2+(\Im\Xi(t))^2=|\Xi(t)|^2.
\]
Hence scalar residual magnitude is slice-invariant under this embedding.

## 9. Relationship to Perfect Closure

In the series arc, Paper 1 provided local/global closure language on \(\mathbb C\); this paper provides the shared quaternionic coordinate space used later for operator transport and mass-shell coupling.

A secondary geometric motif is the six-step cadence for unit phases. If \(Q=e^{\mathbf u\phi}\) with \(\Re(Q)=1/2\), then \(\cos\phi=1/2\), so \(\phi=\pi/3\) modulo \(2\pi\), giving
\[
Q^3=-1,\qquad Q^6=1.
\]
This cadence is an orientation mnemonic for unit-phase motion. It is not a theorem about zeta-zero placement.

![Six-step closure gate](../assets/figures/six-step-closure-gate.svg)

*Figure 2. Six-step phase cadence for \(Q=e^{\mathbf u\pi/3}\), included as a secondary geometric motif.* 

## 10. Discussion

The quaternionic lift space offers a single sentence summary: same scalar data, more orientation freedom. The critical-line parameter \(t\) and completed residual magnitudes remain exactly the same objects as in the complex formulation, but they can be represented on any slice \(\mathbb C_{\mathbf u}\).

This clarifies interpretive boundaries embedded throughout the paper. The lift does not replace complex analysis; it embeds it. The construction does not create new zeta zeros. The six-step cadence provides geometric intuition for phase structure, not an analytic zero-placement theorem.

As preparation for the next papers, this slice language supplies a common coordinate interface: Paper 3 uses quaternion-compatible norm structure for mass shell, and Paper 4 uses operator transport with explicit scale assumptions.

## 11. Conclusion

Paper 2 establishes quaternionic lift space as a family of complex slices inside \(\mathbb H\). The ordinary complex plane is recovered as the \(\mathbf u=i\) slice, and the classical critical line is represented slice-wise by \(q_{\mathbf u}(t)=1/2+\mathbf u t\). The completed residual can be packaged as \(\xi_{\mathbb H}(1/2+\mathbf u t)=\Re\Xi(t)+\mathbf u\Im\Xi(t)\) without changing scalar norm, since \(\|\xi_{\mathbb H}(1/2+\mathbf u t)\|^2=|\Xi(t)|^2\). This conservative lift provides the shared higher-dimensional coordinate language used by Papers 3 and 4.

## 12. References

[1] W. R. Hamilton, *Elements of Quaternions*, Longmans, Green, and Co., 1866.  
[2] S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields*, Oxford Univ. Press, 1995.  
[3] E. C. Titchmarsh and D. R. Heath-Brown, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford Univ. Press, 1986.  
[4] H. M. Edwards, *Riemann's Zeta Function*, Dover, 2001.

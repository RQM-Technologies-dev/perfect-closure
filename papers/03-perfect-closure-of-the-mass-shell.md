# Mass-Shell Perfect Closure: Closed Quaternionic Light and Relativistic Norm Structure

**John Van Geem / RQM Technologies**  
*Preprint - April 2026*

## Abstract

This paper rewrites the relativistic mass shell in quaternion-compatible norm language and explains why that rewrite is useful for the closure series. Starting from \(E^2/c^2-|\mathbf p|^2=m^2c^2\), we define \(P=E/c+I\mathbf p\) and its conjugate \(\bar P=E/c-I\mathbf p\). The product \(P\bar P\) removes orientation data and returns the invariant scalar mass shell. This lets us distinguish null/open propagation \((P\bar P=0)\) from closed/massive norm structure \((P\bar P>0)\). We then introduce Compton curvature \(k_C=mc/\hbar\) as the conversion bridge used by the operator construction in Paper 4.

## 1. Introduction

The standard mass shell is already a closure-like statement: many coordinate descriptions collapse to one scalar invariant. Paper 3 adopts that perspective directly. We are not changing relativity; we are teaching its invariant content in a norm language compatible with the earlier quaternionic lift.

The phrase “light that has closure becomes mass” should be read cautiously. It is interpretive shorthand for the transition from null norm to positive invariant norm, not a full microscopic mechanism.

## 2. Relativistic invariant target

The basic equation is
\[
E^2=p^2c^2+m^2c^4,
\]
which is equivalently
\[
\frac{E^2}{c^2}-|\mathbf p|^2=m^2c^2.
\]
This equation should be read as the invariant target. Any reformulation must return this same scalar.

## 3. Quaternionic momentum packaging

Define
\[
P=\frac{E}{c}+I\mathbf p,\qquad \bar P=\frac{E}{c}-I\mathbf p,
\]
with \(I^2=-1\). Multiplying gives
\[
\begin{aligned}
P\bar P
&=\left(\frac{E}{c}+I\mathbf p\right)\left(\frac{E}{c}-I\mathbf p\right)\\
&=\left(\frac{E}{c}\right)^2-(I\mathbf p)^2
=\frac{E^2}{c^2}-|\mathbf p|^2
= m^2c^2.
\end{aligned}
\]

### Proposition 1
The scalar \(P\bar P\) is exactly the relativistic mass-shell invariant.

The reason for this proposition is conceptual: conjugation strips orientation and leaves invariant magnitude.

![Mass-shell norm diagram](../assets/figures/mass-shell-norm.svg)

*Figure 1. Norm interpretation of null/open and massive/closed regimes.*

## 4. Open and closed norm regimes

- \(P\bar P=0\): null/open propagation (massless limit).
- \(P\bar P>0\): closed/massive invariant norm.

The important point is that closure language here is norm-based. It does not claim that photons literally convert by this equation alone; it marks how invariant structure distinguishes null and massive sectors.

## 5. Compton curvature as bridge variable

Define reduced Compton wavelength and curvature:
\[
\bar\lambda_C=\frac{\hbar}{mc},\qquad k_C=\frac{1}{\bar\lambda_C}=\frac{mc}{\hbar}.
\]
This quantity prepares the next paper. Paper 4 compares spectral ordinates \(t_n\) with physical inverse-length scales through a conversion length \(L_*\).

## 6. Discussion

This reformulation is intentionally conservative. It preserves the textbook invariant and only changes presentation. In that sense, quaternionic notation is a packaging device that makes the “remove orientation, keep scalar” principle transparent.

What this does not show is a derivation of observed particle masses. It gives the invariant norm side of the bridge, nothing more.

## 7. Conclusion

Mass-shell Perfect Closure is the statement that \(P\bar P\) returns the invariant scalar \(m^2c^2\). Null and massive regimes are separated by whether this scalar vanishes or remains positive. With \(k_C=mc/\hbar\), the construction is ready for Paper 4, where zeta-side spectral labels are coupled to this norm structure through operator methods.

## References

[1] A. Einstein, *Zur Elektrodynamik bewegter Koerper*, 1905.  
[2] W. R. Hamilton, *Elements of Quaternions*, 1866.  
[3] S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields*, Oxford Univ. Press, 1995.

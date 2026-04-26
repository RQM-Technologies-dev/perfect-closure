# Perfect Closure Is Quaternionic: The Riemann Critical Line as a Complex Shadow

**John Van Geem / RQM Technologies**  
*Research Note — April 2026*

## Abstract

This paper develops the quaternionic-geometry layer of the Perfect Closure program. We define quaternionic slices \(\mathbb C_{\mathbf u}\), the critical hyperslice \(\Sigma_{1/2}=\{q\in\mathbb H: \operatorname{Re}(q)=1/2\}\), and the affine family \(q_{\mathbf u}(t)=1/2+\mathbf u t\). We separate affine spectral location from unit-phase multiplicative closure and show the six-step gate \(Q^6=1\) at \(\operatorname{Re}(Q)=1/2\). We then define a slice-lifted completed-zeta residual that agrees with the classical residual on each slice. No proof of RH or full quaternionic zeta theory is claimed.

## Reader Guide

This paper explains why the complex critical line can be viewed as one slice of quaternionic closure geometry. The goal is geometric reframing, not a new theorem about zeta zeros. Read it as the orientation-space layer that prepares the operator bridge in Paper 4.

## 1. Introduction and thesis

Paper 1 isolated the square-root mirror on the complex critical line. The present paper asks how that line sits inside quaternionic orientation space.

**Thesis.** The classical line \(\operatorname{Re}(s)=1/2\) may be interpreted as one complex slice of a broader quaternionic closure slice \(\operatorname{Re}(q)=1/2\).

## 2. Quaternions and complex slices

A quaternion is
$$
q=a+bi+cj+dk,\qquad a,b,c,d\in\mathbb R,
$$
with \(i^2=j^2=k^2=ijk=-1\). Its real part is \(\operatorname{Re}(q)=a\).

Let \(\mathbf u\) be a unit imaginary quaternion (\(\mathbf u^2=-1\)). The corresponding complex slice is
$$
\mathbb C_{\mathbf u}=\{a+\mathbf u b:\;a,b\in\mathbb R\}.
$$
This definition gives a family of complex planes indexed by direction \(\mathbf u\). It does not by itself define a quaternionic extension of the full zeta function.

## 3. Quaternionic critical slice

Define
$$
\Sigma_{1/2}=\{q\in\mathbb H:\operatorname{Re}(q)=1/2\},
$$
and for each unit \(\mathbf u\),
$$
q_{\mathbf u}(t)=\frac12+\mathbf u t,\qquad t\in\mathbb R.
$$
When \(\mathbf u=i\), this is the classical critical line \(s=1/2+it\). The reader should notice this as a geometric inclusion statement, not a proof that all zeros come from quaternionic dynamics.

## 4. Affine slice versus unit phase

Two objects must be kept distinct:

- **Affine slice:** \(q=1/2+\mathbf u t\) (spectral location).
- **Unit phase:** \(Q=e^{\mathbf u\phi}=\cos\phi+\mathbf u\sin\phi\) (multiplicative closure).

The first is additive geometry; the second is multiplicative phase closure. Keeping them separate prevents over-interpretation.

## 5. Six-step closure gate

If \(\operatorname{Re}(Q)=1/2\), then \(\cos\phi=1/2\), so \(\phi=\pi/3\) (mod \(2\pi\)). Therefore
$$
Q=e^{\mathbf u\pi/3},\qquad Q^3=e^{\mathbf u\pi}=-1,\qquad Q^6=e^{\mathbf u2\pi}=1.
$$
This gives a reusable closure cadence that later informs the log-scale period discussion. It does not produce zeta zeros by itself.

## 6. Quaternionic prime phase

On the critical slice,
$$
p^{-(1/2+\mathbf u t)}=p^{-1/2}e^{-\mathbf u t\log p},\qquad
p^{-(1/2-\mathbf u t)}=p^{-1/2}e^{+\mathbf u t\log p}.
$$
This is the quaternionic version of Paper 1’s square-root mirror. It appears here to show continuity between complex and quaternionic notation.

## 7. Slice-lifted completed zeta

Define
$$
\Xi(t)=\xi\!\left(\frac12+it\right)
$$
and lift it on slice \(\mathbf u\) by
$$
\xi_{\mathbb H}(1/2+\mathbf u t)=\Re\,\Xi(t)+\mathbf u\Im\,\Xi(t).
$$
Then define
$$
C_{\mathbb H,\mathbf u}(t)=\|\xi_{\mathbb H}(1/2+\mathbf u t)\|^2.
$$
By construction,
$$
C_{\mathbb H,\mathbf u}(t)=|\Xi(t)|^2.
$$
The point is compatibility across slices, not a full noncommutative analytic theory.

## 8. Meaning and non-meaning

### Claims

- The critical line admits a quaternionic slice interpretation.
- Quaternionic closure provides the native geometry of which the complex critical line is a slice.

### Non-claims

- No proof of RH.
- No claim of a full quaternionic zeta function over all of \(\mathbb H\).
- No replacement of analytic number theory.

## 9. Relation to neighboring papers

- Paper 1: complex square-root mirror and prime imbalance.
- Paper 2 (this paper): quaternionic slice geometry.
- Paper 3: mass-shell closure interpretation in biquaternionic spacetime.

## References

1. W. R. Hamilton, *Elements of Quaternions*, 1866.
2. S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields*, Oxford Univ. Press, 1995.
3. J. C. Baez, “The Octonions,” *Bull. Amer. Math. Soc.* 39 (2002), sections on quaternions.
4. E. C. Titchmarsh and D. R. Heath-Brown, *The Theory of the Riemann Zeta-Function*, 2nd ed., 1986.
5. H. M. Edwards, *Riemann’s Zeta Function*, 2001.

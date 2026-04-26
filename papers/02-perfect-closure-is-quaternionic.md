# Perfect Closure Is Quaternionic: The Riemann Critical Line as a Complex Shadow

**John Van Geem / RQM Technologies**  
*Research Note — April 2026*

## Abstract

This paper develops the quaternionic-geometry layer of the Perfect Closure program. The central thesis is: **Perfect Closure is visible in complex phase but native to quaternionic orientation space**. We define quaternionic slices $\mathbb C_u$, the critical hyperslice $\Sigma_{1/2}=\{q\in\mathbb H: \operatorname{Re}(q)=1/2\}$, and the affine family $q_u(t)=1/2+ut$. We separate affine spectral location from unit-phase multiplicative closure and show the six-step gate $Q^6=1$ at $\operatorname{Re}(Q)=1/2$. We then define a slice-lifted completed-zeta residual that agrees with the classical residual on each slice. No proof of RH or full quaternionic zeta theory is claimed.

## 1. Introduction and thesis

Paper 1 isolated the square-root mirror on the complex critical line. The present paper asks how that line sits inside quaternionic orientation space.

**Thesis.** The classical line $\operatorname{Re}(s)=1/2$ is a complex trace of the quaternionic closure slice $\operatorname{Re}(q)=1/2$.

## 2. Quaternions and complex slices

A quaternion is
$$
q=a+bi+cj+dk,\qquad a,b,c,d\in\mathbb R,
$$
with $i^2=j^2=k^2=ijk=-1$. Its real part is $\operatorname{Re}(q)=a$.

Let $u$ be a unit imaginary quaternion ($u^2=-1$). The corresponding complex slice is
$$
\mathbb C_u=\{a+ub:\;a,b\in\mathbb R\}.
$$
The ordinary complex plane is the special case $u=i$.

## 3. Quaternionic critical slice

Define
$$
\Sigma_{1/2}=\{q\in\mathbb H:\operatorname{Re}(q)=1/2\},
$$
and for each unit $u$,
$$
q_u(t)=\frac12+ut,\qquad t\in\mathbb R.
$$
When $u=i$, this is the classical critical line $s=1/2+it$. Therefore $\operatorname{Re}(s)=1/2$ is a complex shadow of $\operatorname{Re}(q)=1/2$.

## 4. Affine slice versus unit phase

Two objects must be kept distinct:

- **Affine slice:** $q=1/2+ut$ (spectral location).
- **Unit phase:** $Q=e^{u\phi}=\cos\phi+u\sin\phi$ (multiplicative closure).

The first is additive/affine geometry; the second is multiplicative phase geometry.

## 5. Six-step closure gate

If $\operatorname{Re}(Q)=1/2$, then $\cos\phi=1/2$ so $\phi=\pi/3$ (mod $2\pi$), and
$$
Q=e^{u\pi/3},\qquad Q^3=e^{u\pi}=-1,\qquad Q^6=e^{u2\pi}=1.
$$
The six-step law is already present in the ordinary complex unit circle ($u=i$). Quaternionic geometry generalizes it to an axis-free family over all $u\in S^2$.

## 6. Quaternionic prime phase

On the critical slice,
$$
p^{-(1/2+ut)}=p^{-1/2}e^{-ut\log p},
$$
with conjugate
$$
p^{-(1/2-ut)}=p^{-1/2}e^{+ut\log p}.
$$
This is the quaternionic version of the square-root mirror from Paper 1.

## 7. Slice-lifted completed zeta

Define
$$
\xi_{\mathbb H}(1/2+ut)=\Re\,\xi(1/2+it)+u\,\Im\,\xi(1/2+it).
$$
Define the slice residual
$$
C_{\mathbb H,u}(t)=\|\xi_{\mathbb H}(1/2+ut)\|^2.
$$
By construction,
$$
C_{\mathbb H,u}(t)=|\xi(1/2+it)|^2
$$
on each slice.

## 8. Meaning and non-meaning

### Claims
- The critical line admits a quaternionic slice interpretation.
- Perfect Closure becomes axis-free in quaternionic orientation space.

### Non-claims
- No proof of RH.
- No claim of a full quaternionic zeta function over all of $\mathbb H$.
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

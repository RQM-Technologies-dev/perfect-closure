# The Perfect Closure of the Mass Shell: Mass as Closed Quaternionic Light

**John Van Geem / RQM Technologies**  
*Research Note - April 2026*

## Abstract

This paper defines the mass shell in quaternionic norm language. With biquaternionic momentum
$$
P=\frac{E}{c}+I\mathbf p,\qquad I^2=-1,
$$
the relativistic invariant becomes
$$
P\bar P=m^2c^2.
$$
Null modes satisfy \(P\bar P=0\); massive modes satisfy \(P\bar P>0\). We also record Compton curvature
$$
k_C=\frac{mc}{\hbar}
$$
as the scale quantity that later receives closure-eigenvalue matching in Paper 4.

## Reader Guide

This paper answers: **what is a mass shell in quaternionic norm language?**

The paper is intentionally preparatory. It does not connect to zeta zeros yet. It establishes a norm equation and interpretation framework so that the Paper 4 bridge has a clear physical target.

## 1. Relativistic mass shell

Start from the standard energy-momentum relation
$$
E^2=p^2c^2+m^2c^4.
$$
Dividing by \(c^2\) gives
$$
\frac{E^2}{c^2}-|\mathbf p|^2=m^2c^2.
$$
This equation is the Minkowski invariant in scalar form. The left side combines energy and three-momentum into one frame-invariant quantity; the right side is rest-mass content.

The purpose of this section is to identify exactly what must be reproduced by quaternionic norm notation. Any alternative notation is acceptable only if it preserves this invariant value.

## 2. Biquaternionic momentum norm

Define
$$
P=\frac{E}{c}+I\mathbf p,
$$
where \(I\) is a commuting imaginary unit (\(I^2=-1\)) and \(\bar{\mathbf p}=-\mathbf p\). Then
$$
\bar P=\frac{E}{c}-I\mathbf p.
$$
Multiplying gives
$$
\begin{aligned}
P\bar P
&=\left(\frac{E}{c}+I\mathbf p\right)\left(\frac{E}{c}-I\mathbf p\right) \\
&=\left(\frac{E}{c}\right)^2-(I\mathbf p)^2 \\
&=\left(\frac{E}{c}\right)^2-|\mathbf p|^2.
\end{aligned}
$$
So the mass shell is exactly
$$
P\bar P=m^2c^2.
$$
The important reading is that \(P\bar P\) is not a decorative rewrite. It is an invariant norm statement equivalent to the standard relativistic equation.

## 3. Open/null and closed/massive interpretation

- \(P\bar P=0\): null or open propagation.
- \(P\bar P>0\): massive or closed invariant norm.

The terms "open" and "closed" are interpretation labels for the value of the invariant norm. They are not additional postulates.

When \(P\bar P=0\), the mode behaves as lightlike in the standard kinematic sense. When \(P\bar P=m^2c^2>0\), there is nonzero rest-mass content and associated finite Compton scale.

![Mass-shell norm diagram](../assets/figures/mass-shell-norm.svg)

*Figure: Conceptual split between null/open propagation \(P\bar P=0\) and massive/closed invariant norm \(P\bar P=m^2c^2>0\). It clarifies the interpretation of Section 3 and is not a full spacetime derivation.*

## 4. Compton curvature scale

Define reduced Compton wavelength and its inverse:
$$
\bar\lambda_C=\frac{\hbar}{mc},\qquad k_C=\frac{mc}{\hbar}=\bar\lambda_C^{-1}.
$$
These equations give a direct map between mass and intrinsic curvature scale. Larger mass means smaller \(\bar\lambda_C\), hence larger \(k_C\).

Paper 4 will match this physical curvature quantity to a lifted closure-eigenvalue quantity. This is where the zeta-side parameter \(t_n\) becomes dimensionally tied to \(m\) through a conversion length.

### Reading the equations as a workflow

The three central equations of this paper can be read as a chain, not as isolated identities:

1. Start from
$$
\frac{E^2}{c^2}-|\mathbf p|^2=m^2c^2.
$$
This identifies the invariant target quantity.

2. Rewrite that target as a norm:
$$
P\bar P=m^2c^2.
$$
This packages energy and momentum into one algebraic object while preserving the same scalar invariant.

3. Convert mass to curvature scale:
$$
k_C=\frac{mc}{\hbar}.
$$
This prepares dimensional compatibility for Paper 4, where spectral ordinates are converted into physical scales.

Seen this way, the paper is not introducing three unrelated formulas. It is introducing a single invariant story told in three coordinate languages: Minkowski scalar form, biquaternionic norm form, and Compton-scale form.

### Why the conjugate product is emphasized

Using \(P\bar P\) makes the closure language explicit. A quantity multiplied by its conjugate strips orientation data and returns a scalar norm. That is why this notation is useful for the series: it makes the \"closed invariant\" interpretation precise without changing relativistic content.

This is also why the transition to Paper 4 is natural. The operator side of the program also uses spectral objects that are selected by scalar closure conditions. The mass-shell side already has that closure structure through \(P\bar P\).

## 5. Non-claims and transition

- No derivation of known particle masses.
- No replacement of QFT.
- No Standard Model completion claim.

Transition sentence: Paper 4 is where the zeta spectral trace \(\Xi(t_n)=0\) and the mass-shell norm \(P\bar P=m^2c^2\) are connected through a shared closure eigenvalue and a conversion scale.

## References

1. A. Einstein, *Zur Elektrodynamik bewegter Koerper* (1905).
2. W. R. Hamilton, *Elements of Quaternions* (1866).
3. S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields*, Oxford Univ. Press, 1995.


# The Zeta–Mass Closure Operator: Perfect Closure as an Eigenvalue Law

**John Van Geem / RQM Technologies**  
*Research Note — April 2026*

## Abstract

This paper gives the operator bridge of the Perfect Closure series. We define the quaternionic closure generator
$$
\mathcal A_{\mathbf u}
=
\mathbf u\left(\rho\frac{d}{d\rho}+\frac12\right),\qquad \mathbf u^2=-1,
$$
with eigenmodes
$$
\chi_t(\rho)=\rho^{-1/2-\mathbf u t}.
$$
Using
$$
\Xi(t)=\xi\!\left(\frac12+it\right),
$$
we set the zeta closure selector
$$
\mathcal Z_{\mathbf u}=\Xi(\mathcal A_{\mathbf u}).
$$
If \(\Xi(t_n)=0\), then \(\mathcal Z_{\mathbf u}\chi_{t_n}=0\). After introducing a scale \(L_\ast\), the same eigenvalue can be realized in mass-shell form through
$$
P\bar P=\left(\frac{\hbar t_n}{L_\ast}\right)^2,
$$
and
$$
m_n=\frac{\hbar}{cL_\ast}|t_n|.
$$
Zeta zeros may be interpreted as complex spectral traces of quaternionic Perfect Closure eigenmodes. Within this framework, the critical line may be understood as a complex spectral slice of a broader quaternionic closure-mass-shell structure. This is a formal bridge, not a proof of RH and not a particle-mass derivation.

## Reader Guide

This paper is the bridge: it shows how the same closure eigenvalue can appear as a zeta-zero condition and as a mass-shell norm after scaling. Read each equation as part of a mapping pipeline, and keep the non-claim boundary in view: this is structural and candidate-predictive only after calibration.

## 1. Introduction

Papers 1–3 established three pieces: zeta closure residuals, quaternionic closure geometry, and mass-shell closure form. This paper connects them at operator level.

The synthesis claim is carefully limited: the Riemann critical line may be interpreted as a complex spectral slice of a broader quaternionic closure-mass-shell structure. The paper does not claim that zeta zeros are particles, and it does not derive a physical spectrum without external calibration.

## 2. Internal scale space

Let \(\rho>0\) be internal scale and \(y=\log\rho\). Prime phases depend on \(\log p\), so dilation in \(\rho\) is the natural generator variable.

This section chooses coordinates for spectral closure analysis. It does not yet attach physical length units.

## 3. Quaternionic closure generator and eigenmodes

Define
$$
\mathcal A_{\mathbf u}
=
\mathbf u\left(\rho\frac{d}{d\rho}+\frac12\right).
$$
This operator measures scaled dilation while carrying a quaternionic phase axis \(\mathbf u\). It appears here because closure modes are naturally logarithmic in \(\rho\).

Define eigenmodes
$$
\chi_t(\rho)=\rho^{-1/2-\mathbf u t}.
$$
Then
$$
\mathcal A_{\mathbf u}\chi_t=t\chi_t.
$$
So \(t\) is the closure eigenvalue. This is an operator statement inside the formal setup, not a statement yet about measured masses.

## 4. Prime evaluation

At \(\rho=p\) (prime),
$$
\chi_t(p)=p^{-1/2-\mathbf u t}=p^{-1/2}e^{-\mathbf u t\log p}.
$$
For slice \(\mathbf u=i\), this reproduces the square-root phase form from Paper 1. The reader should notice continuity of notation across papers.

## 5. Zeta closure selector and kernel condition

Set
$$
\Xi(t)=\xi\!\left(\frac12+it\right).
$$
This is the complex spectral slice function carried through the series.

Define
$$
\mathcal Z_{\mathbf u}=\Xi(\mathcal A_{\mathbf u}).
$$
If \(t_n\) is a critical-line ordinate with
$$
\Xi(t_n)=0,
$$
then
$$
\mathcal Z_{\mathbf u}\chi_{t_n}=0.
$$
This is the quaternionic closure eigenmode condition. It identifies kernel modes selected by zeta-slice zeros; it does not prove RH.

## 6. Closure period in log-scale

Mode phase is \(e^{-\mathbf u t_n\log\rho}\). Full \(2\pi\) closure occurs over
$$
\Lambda_n=\frac{2\pi}{t_n},
$$
and six-step increment is
$$
\Delta_n=\frac{\pi}{3t_n}.
$$
This links back to the \(\pi/3\) gate from Paper 2. It is a geometric cadence, not a mass prediction.

## 7. Mass-shell lift and resolved closure length

Introduce physical length \(L_\ast\) by
$$
\log\rho=\frac{\ell}{L_\ast}.
$$
Then the physical wavenumber is \(k_n=t_n/L_\ast\), and matching with Compton curvature yields
$$
m_n=\frac{\hbar}{cL_\ast}|t_n|.
$$
Conversely, for a resolved instance,
$$
L_\ast=t_n\frac{\hbar}{mc}=t_n\bar\lambda_C.
$$
These formulas define the conversion map. They do not fix \(L_\ast\); calibration is deferred to Paper 5.

## 8. Biquaternionic mass-shell realization

Using the mass-shell norm
$$
P\bar P=m^2c^2,
$$
the closure lift takes the form
$$
P\bar P=\left(\frac{\hbar t_n}{L_\ast}\right)^2.
$$
This is the mass-shell face of the same eigenvalue \(t_n\). It is a structural realization, not yet a physical particle-mass prediction.

## 9. Complex Spectral Slices of Quaternionic Mass Shells

The bridge can now be stated in three aligned conditions:

1. **Complex zeta-slice condition**
   $$
   \Xi(t_n)=0.
   $$
2. **Quaternionic closure eigenmode condition**
   $$
   \Xi(\mathcal A_{\mathbf u})\chi_{t_n}=0.
   $$
3. **Mass-shell norm realization after scaling**
   $$
   P\bar P=\left(\frac{\hbar t_n}{L_\ast}\right)^2.
   $$

Therefore the same eigenvalue \(t_n\) has a zeta face and a mass-shell face within this framework. In this sense, the critical line functions as a complex spectral slice of a broader quaternionic closure-mass-shell structure. This is a formal bridge and candidate predictive structure that still requires calibration.

## 10. Coupled closure system

A compact formal system is
$$
\Xi(\mathcal A_{\mathbf u})\Psi=0,
$$
$$
P\bar P\,\Psi=\frac{\hbar^2}{L_\ast^2}\mathcal A_{\mathbf u}^2\Psi.
$$
The first equation selects closure modes; the second maps eigenvalues into norm form. Neither equation alone supplies a dynamical mechanism for particle families.

## 11. Main theorem

### Theorem 11.1 (Closure eigenvalue lift)

If \(\chi_{t_n}\) satisfies \(\mathcal A_{\mathbf u}\chi_{t_n}=t_n\chi_{t_n}\) and \(\Xi(t_n)=0\), then:
1. \(\chi_{t_n}\in\ker\Xi(\mathcal A_{\mathbf u})\);
2. under scale map \(L_\ast\), the same eigenvalue yields mass
$$
m_n=\frac{\hbar}{cL_\ast}|t_n|.
$$

**Proof.** Part (1):
$$
\Xi(\mathcal A_{\mathbf u})\chi_{t_n}=\Xi(t_n)\chi_{t_n}=0.
$$
Part (2): define \(k_n=t_n/L_\ast\) and identify with \(k_C=mc/\hbar\), giving the stated mass formula. \(\square\)

## 12. Non-claims

- No proof of RH.
- No claim that zeta zeros are particles.
- No derived universal value of \(L_\ast\) in this paper.
- No Standard Model mass derivation.

## 13. Bridge to Paper 5

Paper 5 asks whether a shared, stable \(L_\ast\) exists in predeclared physical families. That is where the present formal bridge becomes falsifiable.

## References

1. E. C. Titchmarsh and D. R. Heath-Brown, *The Theory of the Riemann Zeta-Function*, 1986.
2. H. M. Edwards, *Riemann’s Zeta Function*, 2001.
3. S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields*, 1995.
4. M. V. Berry and J. P. Keating, “H=xp and the Riemann zeros” (Hilbert–Pólya context).
5. W. Rindler, *Introduction to Special Relativity*.

# The Zeta–Mass Closure Operator: Perfect Closure as an Eigenvalue Law

**John Van Geem / RQM Technologies**  
*Research Note — April 2026*

## Abstract

This paper gives the operator bridge of the Perfect Closure series. We define a quaternionic dilation generator
$$
A_u=u\left(\rho\frac{d}{d\rho}+\frac12\right),\qquad u^2=-1,
$$
with eigenmodes $\chi_t(\rho)=\rho^{-1/2-ut}$. Using $\Xi(t)=\xi(1/2+it)$, we define the closure selector $Z_u=\Xi(A_u)$ (formal functional calculus). If $\Xi(t_n)=0$, then $Z_u\chi_{t_n}=0$. A physical scale map $\log\rho=\ell/L_*$ then yields $k_n=t_n/L_*$ and
$$
m_n=\frac{\hbar|t_n|}{cL_*}.
$$
The theorem is algebraic and formal: no RH proof, no Standard Model derivation, and no claim that zeta zeros are particles.

## 1. Introduction

Papers 1–3 established three pieces: zeta closure residuals, quaternionic closure geometry, and mass-shell closure interpretation. This paper connects them at operator level.

**Core thesis.** A zeta zero is an internal closure eigenvalue; a mass shell is the physical realization of that eigenvalue after a scale lift.

## 2. Internal scale space

Let $\rho>0$ be internal scale and $y=\log\rho$. Prime phases naturally involve $\log p$, so dilation in $\rho$ is the natural generator.

## 3. Quaternionic dilation generator

Define
$$
A_u=u\left(\rho\frac{d}{d\rho}+\frac12\right),\qquad u^2=-1.
$$
Consider
$$
\chi_t(\rho)=\rho^{-1/2-ut}=\rho^{-1/2}e^{-ut\log\rho}.
$$
Then
$$
\left(\rho\frac{d}{d\rho}+\frac12\right)\chi_t=-ut\chi_t,
$$
and therefore
$$
A_u\chi_t=t\chi_t.
$$

## 4. Prime evaluation

At $\rho=p$ (prime),
$$
\chi_t(p)=p^{-1/2-ut}=p^{-1/2}e^{-ut\log p}.
$$
For slice $u=i$, this is the square-root prime phase of Paper 1.

## 5. Zeta closure selector

Set
$$
\Xi(t)=\xi\!\left(\frac12+it\right).
$$
Define (formally) by functional calculus:
$$
Z_u=\Xi(A_u).
$$
If $t_n$ is a critical-line zero ordinate, $\Xi(t_n)=0$. Acting on eigenmode $\chi_{t_n}$,
$$
Z_u\chi_{t_n}=\Xi(A_u)\chi_{t_n}=\Xi(t_n)\chi_{t_n}=0.
$$
Thus zeta zeros correspond to kernel modes of the closure selector.

## 6. Closure period in log-scale

Mode phase is $e^{-ut_n\log\rho}$. Full $2\pi$ closure occurs over
$$
\Lambda_n=\frac{2\pi}{t_n},
$$
and six-step increment is
$$
\Delta_n=\frac{\pi}{3t_n}.
$$
This is consistent with the $\pi/3$ gate in Paper 2.

## 7. Mass-shell lift

Introduce physical length $L_*$ by
$$
\log\rho=\frac{\ell}{L_*}.
$$
Then phase becomes $e^{-u(t_n/L_*)\ell}$ with physical closure wavenumber
$$
k_n=\frac{t_n}{L_*}.
$$
Matching Compton curvature $k_C=mc/\hbar$ gives
$$
m_n=\frac{\hbar|t_n|}{cL_*}.
$$

## 8. Biquaternionic mass-shell form

Using $P=E/c+I\mathbf p$ and $P\bar P=m^2c^2$, closure lift gives
$$
P\bar P=\left(\frac{\hbar t_n}{L_*}\right)^2.
$$

## 9. Coupled closure system

A formal coupled system is
$$
\Xi(A_u)\Psi=0,
$$
$$
P\bar P\,\Psi=\frac{\hbar^2}{L_*^2}A_u^2\Psi.
$$
The first selects internal closure modes; the second realizes their mass-shell norm after scale conversion.

## 10. Main theorem

### Theorem 10.1 (Closure eigenvalue lift)

If $\chi_{t_n}$ satisfies $A_u\chi_{t_n}=t_n\chi_{t_n}$ and $\Xi(t_n)=0$, then:
1. $\chi_{t_n}\in\ker\Xi(A_u)$;
2. under scale map $L_*$, the same eigenvalue yields mass
$$
m_n=\frac{\hbar|t_n|}{cL_*}.
$$

**Proof.** Part (1) is spectral substitution:
$$
\Xi(A_u)\chi_{t_n}=\Xi(t_n)\chi_{t_n}=0.
$$
For (2), define $k_n=t_n/L_*$. Identifying with Compton curvature $k_C=mc/\hbar$ gives $m_n=\hbar|t_n|/(cL_*)$. $\square$

## 11. Non-claims

- No proof of RH.
- No claim zeta zeros are particles.
- No derived value of $L_*$ in this paper.
- No Standard Model mass derivation.

## 12. Bridge to Paper 5

Paper 5 addresses whether $L_*$ can be independently fixed or stabilized across physical families, and how to test/falsify the calibration.

## References

1. E. C. Titchmarsh and D. R. Heath-Brown, *The Theory of the Riemann Zeta-Function*, 1986.
2. H. M. Edwards, *Riemann’s Zeta Function*, 2001.
3. S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields*, 1995.
4. M. V. Berry and J. P. Keating, “H=xp and the Riemann zeros” (Hilbert–Pólya context).
5. W. Rindler, *Introduction to Special Relativity*.

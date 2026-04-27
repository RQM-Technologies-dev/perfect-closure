# The Zeta-Mass Closure Operator: Perfect Closure as a Shared Spectral Eigenvalue Law

**John Van Geem / RQM Technologies**  
*Preprint - April 2026*

## Abstract

This paper builds the operator bridge between zeta closure labels and mass-shell norm structure. We define a dilation-based generator \(A_u=u(\rho\,d/d\rho+1/2)\), show that \(\chi_t(\rho)=\rho^{-1/2-ut}\) is an eigenmode with eigenvalue \(t\), and use \(\Xi(A_u)\) as a spectral selector. Thus \(\Xi(t_n)=0\) implies \(\Xi(A_u)\chi_{t_n}=0\). With conversion scale \(L_*\), the same label gives \(P\bar P=(\hbar t_n/L_*)^2\). The paper emphasizes interpretation: this is a compatibility law, and its physical content depends on whether \(L_*\) is independently fixed.

## 1. Introduction

Paper 1 provided scalar closure \(\Xi(t)\), Paper 2 provided quaternionic slice representation, and Paper 3 provided relativistic norm structure. Paper 4 asks how to carry one spectral label through all three contexts without changing its mathematical role.

The reason a dilation operator appears is that the variable \(\rho\) is a scale variable. Differentiation in \(\log\rho\) naturally measures scale frequency.

## 2. Main construction

Let \(u^2=-1\) and \(\rho>0\). Define
\[
A_u=u\left(\rho\frac{d}{d\rho}+\frac12\right).
\]
The \(+1/2\) shift should be read as centering the mode exponents around the critical-line half shift.

Define
\[
\chi_t(\rho)=\rho^{-1/2-ut}.
\]
Then step by step,
\[
\rho\frac{d}{d\rho}\chi_t=\left(-\frac12-ut\right)\chi_t,
\]
\[
\left(\rho\frac{d}{d\rho}+\frac12\right)\chi_t=-ut\chi_t,
\]
\[
A_u\chi_t=u(-ut)\chi_t=t\chi_t.
\]
So \(\chi_t\) is an eigenmode of \(A_u\) with eigenvalue \(t\).

## 3. Spectral selection by \(\Xi(A_u)\)

Set
\[
\Xi(t)=\xi\!\left(\frac12+it\right).
\]
Using functional calculus on eigenmodes,
\[
\Xi(A_u)\chi_t=\Xi(t)\chi_t.
\]
Therefore if \(\Xi(t_n)=0\), then
\[
\Xi(A_u)\chi_{t_n}=0.
\]

This equation should be read as a selector statement: the operator kills exactly those eigenmodes whose labels lie at completed-residual zeros.

![Closure operator bridge](../assets/figures/closure-operator-bridge.svg)

*Figure 1. From eigenmodes to kernel selection under \(\Xi(A_u)\).* 

## 4. Mass-shell realization with conversion scale

Paper 3 gave \(P\bar P=m^2c^2\). Introduce a conversion length \(L_*\) and define
\[
m_n=\frac{\hbar}{cL_*}|t_n|.
\]
Then
\[
P\bar P=(m_nc)^2=\left(\frac{\hbar t_n}{L_*}\right)^2.
\]

The important point is the role of \(L_*\). If it is chosen freely for each target, the relation is descriptive. If it is fixed independently, the relation becomes predictive.

![Two faces of \(t_n\)](../assets/figures/tn-two-faces-bridge.svg)

*Figure 2. The same \(t_n\) appears as a zeta label and as a mass-shell scale label.*

## 5. Discussion

The bridge is mathematically clean: one label \(t_n\) appears as
- a zero label in \(\Xi(t)\),
- an eigenvalue label of \(A_u\),
- a scale label in \(P\bar P\).

What this does not show is ontological identity between zeta zeros and particles. It shows compatibility of labeling under stated assumptions.

## 6. Conclusion

The zeta-mass closure operator is a shared spectral-eigenvalue law: \(A_u\chi_t=t\chi_t\), \(\Xi(A_u)\chi_t=\Xi(t)\chi_t\), and zero labels are carried into the operator kernel. Combined with \(L_*\), the same labels produce a mass-shell realization. The decisive scientific question now becomes calibration discipline for \(L_*\), which is taken up in Paper 5.

## References

[1] E. C. Titchmarsh and D. R. Heath-Brown, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford Univ. Press, 1986.  
[2] H. M. Edwards, *Riemann's Zeta Function*, Dover, 2001.  
[3] S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields*, Oxford Univ. Press, 1995.

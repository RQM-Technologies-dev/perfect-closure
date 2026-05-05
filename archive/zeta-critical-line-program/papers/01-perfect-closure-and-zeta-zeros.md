# Zeta-Zero Perfect Closure: The Critical Line as a Square-Root Mirror

**John Van Geem / RQM Technologies**  
*Preprint - April 2026*

## Abstract

This paper presents a two-level account of Perfect Closure on the prime-spectrum side. At the local level, each prime route splits into a size component and a rotational component, and the critical line is the unique location where reflected routes have equal size. At the global level, closure is defined by vanishing of the completed residual rather than by local route matching alone. The paper shows how a prime-route imbalance quantity detects departure from mirror balance, explains why local balance should not be read as a proof of the Riemann Hypothesis, and clarifies that Perfect Closure means completed return or completed cancellation rather than emptiness.

## 1. Introduction

The first paper in this series begins with a simple pedagogical principle: one should separate what is locally visible from what is globally decisive. The local picture comes from individual prime routes. The global picture comes from the completed analytic object that combines all routes into one function. Many misunderstandings arise when these two levels are mixed too early.

The central claim is intentionally modest. The critical line is distinguished because reflected prime routes are equally weighted there. This statement should not be read as a proof of the Riemann Hypothesis. It is a structural observation about local balancing geometry. The actual zero condition remains global.

## 2. Mathematical Background

For a complex variable written as \(s=\sigma+it\), each prime contribution can be written in the split form
\[
p^{-s}=p^{-\sigma}e^{-it\log p}.
\]
The first factor controls amplitude. The second controls phase rotation. This separation is not cosmetic; it explains why the critical line behaves as a mirror.

When one reflects \(s\) across the critical line, the amplitude weights become \(p^{-\sigma}\) and \(p^{-(1-\sigma)}\). Equal weighting requires \(\sigma=1-\sigma\), hence \(\sigma=1/2\). The critical line is therefore the square-root line for every prime route.

## 3. Main Construction

On the critical line one obtains
\[
p^{-(1/2\pm it)}=\frac{1}{\sqrt p}e^{\mp it\log p},
\]
so both reflected routes carry the same square-root amplitude and opposite phase direction. Off the line, one route is weighted more heavily than the other. This local asymmetry is what motivates an explicit imbalance diagnostic.

To measure this, define
\[
B_p(\sigma)=\left|p^{-\sigma}-p^{-(1-\sigma)}\right|.
\]
Write \(\sigma=1/2+\delta\). Then
\[
B_p(1/2+\delta)=2p^{-1/2}|\sinh(\delta\log p)|.
\]
This formula makes interpretation immediate: the hyperbolic factor measures signed departure from mirror location, while the square-root prefactor rescales by the prime size.

![Square-root mirror prime routes](../assets/figures/square-root-mirror-prime-routes.svg)

*Figure 1. Equal square-root amplitudes and opposite phases at the critical line.*

## 4. Formal Definitions and Results

### Definition 1 (Prime-route mirror balance)
For a fixed prime \(p\), mirror balance at \(\sigma\) means equality of reflected amplitudes:
\[
p^{-\sigma}=p^{-(1-\sigma)}.
\]

### Proposition 1
For each prime \(p>1\), mirror balance holds if and only if \(\sigma=1/2\).

**Proof.** By definition, mirror balance is equivalent to \(p^{-\sigma}=p^{-(1-\sigma)}\). Taking logarithms gives \(-\sigma\log p=-(1-\sigma)\log p\). Since \(\log p\neq 0\), we obtain \(\sigma=1/2\). The converse is immediate. \(\square\)

### Definition 2 (Local imbalance)
The local imbalance at prime \(p\) and real part \(\sigma\) is the nonnegative quantity
\[
B_p(\sigma)=\left|p^{-\sigma}-p^{-(1-\sigma)}\right|.
\]

### Proposition 2
For each prime \(p>1\), \(B_p(\sigma)=0\) exactly at \(\sigma=1/2\).

**Interpretation.** Proposition 2 should be read as a local uniqueness statement. It says that each prime has one mirror location. It does not say that global cancellation has occurred.

![Prime imbalance curve](../assets/figures/prime-imbalance-curve.svg)

*Figure 2. The prime-route imbalance vanishes only at the critical line.*

## 5. Interpretation

The completed residual
\[
\Xi(t)=\xi\!\left(\frac12+it\right)
\]
encodes global closure. A closure event is \(\Xi(t_n)=0\), equivalently \(|\Xi(t_n)|^2=0\). The crucial methodological point is that local balance and global vanishing answer different questions. Local balance identifies where reflected routes are equally weighted. Global vanishing determines whether all contributions complete to zero.

This distinction is where caution belongs. Local mirror balance is strong geometric evidence for the special role of the critical line. It is not by itself a zero-placement theorem.

## 6. Relation to the Series

Paper 1 establishes the base language for the series:
- local mirror geometry from prime routes,
- global closure through the completed residual,
- and a conservative boundary between geometric motivation and analytic proof.

Paper 2 will keep the same scalar height parameter and lift the critical line into quaternionic slice families. The present results are therefore foundational rather than terminal.

## 7. Conclusion

Perfect Closure on the prime-spectrum side should be understood as completed return, not as symbolic emptiness. The critical line is the unique square-root mirror for local prime amplitudes. This local structure motivates, but does not replace, the global completed-zero condition. In that sense, the paper provides a disciplined starting point: it explains why the line is special while preserving the difference between structural plausibility and full proof.

## References

[1] B. Riemann, *Ueber die Anzahl der Primzahlen unter einer gegebenen Groesse*, 1859.  
[2] E. C. Titchmarsh and D. R. Heath-Brown, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford Univ. Press, 1986.  
[3] H. M. Edwards, *Riemann's Zeta Function*, Dover, 2001.

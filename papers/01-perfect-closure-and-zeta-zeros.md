# Perfect Closure and Zeta Zeros: The Critical Line as a Square-Root Mirror

**John Van Geem / RQM Technologies**  
*Research Note — April 2026*

## Abstract

This paper develops a focused formalization of **Perfect Closure** in the setting of the Riemann zeta function. Perfect Closure is defined as the condition in which conjugate displacement resolves without residue. We show that, for each prime route, the line $\operatorname{Re}(s)=\tfrac12$ is the unique local amplitude-balance line: it is the square-root mirror where conjugate routes have equal magnitude. We introduce a local imbalance functional and prove a primewise proposition characterizing this uniqueness. We then frame zeta zeros as global closure events of the completed zeta structure via the residual $C(t)=|\xi(\tfrac12+it)|^2$. The paper does **not** claim a proof of the Riemann Hypothesis; it offers a framework and interpretation that motivates further formalization.

## 1. Introduction

The Riemann critical line $\operatorname{Re}(s)=\tfrac12$ occupies a central role in analytic number theory. This note introduces a constrained interpretation of that line using the concept of Perfect Closure, deliberately limited to the zeta context.

### Definition 1 (Perfect Closure)

**Perfect Closure is the condition in which conjugate displacement resolves without residue.**

In this paper, “without residue” is represented by a vanishing residual quantity built from the completed zeta function.

## 2. Prime Routes and the Square-Root Mirror

Let
$$
s=\sigma+it, \qquad p>1 \text{ prime}.
$$
Then
$$
p^{-s}=p^{-\sigma}e^{-it\log p}.
$$
On the critical line $\sigma=\tfrac12$:
$$
p^{-(1/2+it)}=\frac{1}{\sqrt p}e^{-it\log p}.
$$
Its conjugate route is
$$
p^{-(1/2-it)}=\frac{1}{\sqrt p}e^{+it\log p}.
$$
Thus both routes have equal magnitude $p^{-1/2}$ and opposite phase direction. In this framework, this is the local square-root mirror property.

## 3. Local Imbalance Functional

Define the local prime-route imbalance:
$$
B_p(\sigma)=\left|p^{-\sigma}-p^{-(1-\sigma)}\right|.
$$
Write $\sigma=\tfrac12+\delta$. Then
$$
B_p\!\left(\frac12+\delta\right)
=\left|p^{-1/2-\delta}-p^{-1/2+\delta}\right|
=2p^{-1/2}\left|\sinh(\delta\log p)\right|.
$$

### Proposition 1
For every prime $p>1$, $B_p(\sigma)=0$ if and only if $\sigma=\tfrac12$.

**Proof.** Since $p^{-1/2}>0$, one has
$$
B_p\!\left(\frac12+\delta\right)=0
\iff \sinh(\delta\log p)=0.
$$
Because $\log p\neq 0$ for $p>1$ and $\sinh(x)=0$ iff $x=0$, this is equivalent to $\delta=0$, i.e. $\sigma=\tfrac12$. Conversely, $\sigma=\tfrac12$ gives equal terms and hence $B_p(\sigma)=0$. $\square$

This proposition is local and primewise: it establishes unique local amplitude balance, not a global theorem about all zeros.

## 4. Completed Zeta and Global Closure Residual

Define the completed zeta function:
$$
\xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma\!\left(\frac s2\right)\zeta(s).
$$
Define the critical-line residual:
$$
C(t)=\left|\xi\!\left(\frac12+it\right)\right|^2.
$$
A **Perfect Closure event** is the condition
$$
C(t)=0.
$$
In this framework, zeta zeros are interpreted as global closure events of the completed zeta structure. They are not interpreted as cancellation of an individual prime term.

## 5. Bridge to Quaternionic Closure

A useful transition to a broader geometry is the quaternionic phase form
$$
Q=e^{u\phi}=\cos\phi+u\sin\phi, \qquad u^2=-1.
$$
If $\operatorname{Re}(Q)=\tfrac12$, then $\cos\phi=\tfrac12$, so $\phi=\pi/3$. Therefore
$$
Q^3=-1,\qquad Q^6=1.
$$
The real part $\tfrac12$ also appears as a closure gate in unit complex and quaternionic phase, where $\operatorname{Re}(Q)=\tfrac12$ implies a six-step return. This motivates Paper 2.

## 6. What This Does and Does Not Claim

### Does not claim
- This paper does **not** prove the Riemann Hypothesis.
- It does **not** claim the Euler product converges on the critical line.
- It does **not** claim one prime cancels the zeta function.

### Does claim
- The critical line is the unique local amplitude-balance line for prime conjugate routes.
- Zeta zeros are proposed as global Perfect Closure events of the completed zeta structure.

## References

1. B. Riemann, *Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse* (1859).
2. E. C. Titchmarsh and D. R. Heath-Brown, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford Univ. Press, 1986.
3. H. M. Edwards, *Riemann's Zeta Function*, Dover, 2001.

# Perfect Closure and Zeta Zeros: The Critical Line as a Square-Root Mirror

**John Van Geem / RQM Technologies**  
*Research Note — April 2026*

## Abstract

We formalize a zeta-specific notion of **Perfect Closure** and isolate a rigorous local statement: for each prime route, the critical line $\operatorname{Re}(s)=\tfrac12$ is the unique amplitude-balance line. The proof uses the local imbalance functional
$$
B_p(\sigma)=\left|p^{-\sigma}-p^{-(1-\sigma)}\right|.
$$
We then extend to finite prime sets via
$$
B_N(\sigma)^2=\sum_{p\le p_N} B_p(\sigma)^2,
$$
and show $B_N(\sigma)=0$ iff $\sigma=\tfrac12$. We also record the prime-power expansion of $\log\zeta(s)$ in its convergence domain and define a global closure residual
$$
C(t)=\left|\Xi(t)\right|^2,\qquad \Xi(t)=\xi\!\left(\tfrac12+it\right).
$$
In this framework, zeros of $\Xi$ are interpreted as global Perfect Closure events. This note does **not** prove the Riemann Hypothesis.

## 1. Introduction

The line $\operatorname{Re}(s)=\tfrac12$ is central in analytic number theory because of its role in the functional equation and zero distribution of the Riemann zeta function. The aim of this paper is narrower than a full RH treatment: we formulate a mathematically disciplined closure language in which the critical line appears as a unique local balance line for prime routes.

The term **Perfect Closure** is used here as a formalization within a research program. In this paper, it is tied to explicit residual quantities and precise non-claims.

## 2. Perfect Closure in the zeta setting

### Definition 2.1 (Perfect Closure, zeta form)

A **Perfect Closure event** is a vanishing of a designated closure residual constructed from zeta data.

At local prime level, residuals are imbalance functionals such as $B_p$. At global completed-zeta level, the residual is $C(t)=|\Xi(t)|^2$.

### Remark 2.2

This paper uses “Perfect Closure” as an interpretation and formalization device; it is not introduced as a new theorem of analytic number theory.

## 3. Three reflections in the critical strip

Let $s=\sigma+it$. Define three involutions:
$$
J(s)=\overline{s},\qquad F(s)=1-s,\qquad R(s)=1-\overline{s}=F\circ J(s)=J\circ F(s).
$$
The map $R$ fixes the critical line:
$$
R\!\left(\tfrac12+it\right)=\tfrac12+it.
$$
So $\operatorname{Re}(s)=\tfrac12$ is the fixed-point set of $R$ in the strip.

## 4. Prime routes and the square-root mirror

For prime $p>1$ and $s=\sigma+it$,
$$
p^{-s}=p^{-\sigma}e^{-it\log p}.
$$
On the critical line,
$$
p^{-(1/2+it)}=\frac{1}{\sqrt p}e^{-it\log p},
$$
and its conjugate route is
$$
p^{-(1/2-it)}=\frac{1}{\sqrt p}e^{+it\log p}.
$$
Hence both routes have the same amplitude $p^{-1/2}$ and opposite phase direction. We call this the **square-root mirror**.

## 5. Local prime imbalance

Define
$$
B_p(\sigma)=\left|p^{-\sigma}-p^{-(1-\sigma)}\right|.
$$
Write $\sigma=\tfrac12+\delta$:
\begin{align*}
B_p\!\left(\tfrac12+\delta\right)
&=\left|p^{-1/2-\delta}-p^{-1/2+\delta}\right|\\
&=p^{-1/2}\left|e^{-\delta\log p}-e^{\delta\log p}\right|\\
&=2p^{-1/2}\left|\sinh(\delta\log p)\right|.
\end{align*}

### Proposition 5.1

For every $p>1$, $B_p(\sigma)=0$ if and only if $\sigma=\tfrac12$.

**Proof.** Since $p^{-1/2}>0$,
$$
B_p\!\left(\tfrac12+\delta\right)=0
\iff \sinh(\delta\log p)=0.
$$
Because $\log p\neq 0$ for $p>1$ and $\sinh x=0$ iff $x=0$, we obtain $\delta=0$, i.e. $\sigma=\tfrac12$. The converse is immediate. $\square$

## 6. Finite global imbalance over primes

Let $p_1<p_2<\cdots<p_N$ be the first $N$ primes, and define
$$
B_N(\sigma)^2=\sum_{j=1}^{N} B_{p_j}(\sigma)^2.
$$

### Proposition 6.1

For every finite prime set $\{p_1,\dots,p_N\}$ with $p_j>1$,
$$
B_N(\sigma)=0 \iff \sigma=\tfrac12.
$$

**Proof.** If $\sigma=\tfrac12$, each term $B_{p_j}(\sigma)=0$ by definition, so $B_N(\sigma)=0$. Conversely, if $B_N(\sigma)=0$, then a sum of nonnegative terms is zero, so each $B_{p_j}(\sigma)=0$. By Proposition 5.1, this forces $\sigma=\tfrac12$. $\square$

### Remark 6.2

This is a finite-prime statement. It does not by itself imply global results about all zeros of $\zeta$.

## 7. Prime-power echo field

In the half-plane $\operatorname{Re}(s)>1$, one has
$$
\log\zeta(s)=\sum_p\sum_{k\ge 1}\frac{p^{-ks}}{k}.
$$
We call the $k=1$ terms **primitive routes** and the $k\ge 2$ terms **echo routes** (prime-power echoes).

This terminology is formal and only used inside the convergence domain where the expansion is valid.

## 8. Completed zeta and global closure residual

Define
$$
\xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma\!\left(\frac s2\right)\zeta(s),
$$
$$
\Xi(t)=\xi\!\left(\frac12+it\right),
$$
$$
C(t)=|\Xi(t)|^2.
$$
A global Perfect Closure event is
$$
C(t)=0 \iff \Xi(t)=0.
$$
This formulation uses the completed function, not an individual prime factor.

## 9. Proven statements vs interpretations

### Proven in this paper

- The critical line is the unique local prime-route amplitude-balance line (Proposition 5.1).
- For every finite prime set, the finite global imbalance vanishes only on $\sigma=\tfrac12$ (Proposition 6.1).

### Interpreted/formalized

- Zeta zeros are interpreted as global Perfect Closure events of the completed zeta residual $C(t)$.

### Not claimed

- No proof of the Riemann Hypothesis.
- No claim that Euler product formulas converge on $\operatorname{Re}(s)=\tfrac12$.
- No claim that any single prime term cancels $\zeta$.

## 10. Short bridge to Paper 2

Let
$$
Q=e^{u\phi}=\cos\phi+u\sin\phi,\qquad u^2=-1.
$$
If $\operatorname{Re}(Q)=\tfrac12$, then $\phi=\pi/3$, hence
$$
Q^3=-1,\qquad Q^6=1.
$$
Paper 2 studies this six-step gate in quaternionic orientation space and relates it to the critical-line geometry.

## References

1. B. Riemann, *Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse* (1859).
2. E. C. Titchmarsh and D. R. Heath-Brown, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford Univ. Press, 1986.
3. H. M. Edwards, *Riemann's Zeta Function*, Dover, 2001.
4. B. Mazur and W. Stein, *Prime Numbers and the Riemann Hypothesis*, Cambridge Univ. Press, 2016.
5. E. Bombieri, “The Riemann Hypothesis,” Clay Mathematics Institute problem description.

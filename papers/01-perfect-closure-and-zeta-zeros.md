# Perfect Closure and Zeta Zeros: The Critical Line as a Square-Root Mirror

**John Van Geem / RQM Technologies**  
*Research Note — April 2026*

## Abstract

We formalize a zeta-specific notion of **Perfect Closure** and isolate a rigorous local statement: for each prime route, the critical line \(\operatorname{Re}(s)=\tfrac12\) is the unique amplitude-balance line. The proof uses the local imbalance functional
$$
B_p(\sigma)=\left|p^{-\sigma}-p^{-(1-\sigma)}\right|.
$$
We then extend to finite prime sets via
$$
B_N(\sigma)^2=\sum_{p\le p_N} B_p(\sigma)^2,
$$
and show \(B_N(\sigma)=0\) iff \(\sigma=\tfrac12\). We also define
$$
\Xi(t)=\xi\!\left(\frac12+it\right),\qquad C(t)=\left|\Xi(t)\right|^2.
$$
Within this framework, zeros of \(\Xi\) are treated as global closure events. The main proven result is local and finite-prime balance; this paper does **not** prove RH.

## Reader Guide

This paper introduces Perfect Closure in the safest setting: the zeta critical line. The main proven result is local prime-route balance, not RH. Later papers will reinterpret this residual structure in quaternionic and mass-shell language; here we establish the baseline mathematics and non-claim boundary.

## 1. Introduction

The line \(\operatorname{Re}(s)=\tfrac12\) is central in analytic number theory because of its role in the functional equation and zero distribution of the Riemann zeta function. The aim of this paper is narrower than a full RH treatment: we formulate closure residuals and prove local balance properties.

The term **Perfect Closure** is used as formal language for this series. It packages residual vanishing statements; it does not replace existing analytic number theory.

## 2. Perfect Closure in the zeta setting

### Definition 2.1 (Perfect Closure, zeta form)

A **Perfect Closure event** is a vanishing of a designated closure residual built from zeta data.

At local prime level, residuals are imbalance functionals such as \(B_p\). At global completed-zeta level, the residual is \(C(t)=|\Xi(t)|^2\).

### Remark 2.2

The definition introduces notation and workflow, not a new theorem. The reader should track where claims are proved and where language is interpretive.

## 3. Three reflections in the critical strip

Let \(s=\sigma+it\). Define three involutions:
$$
J(s)=\overline{s},\qquad F(s)=1-s,\qquad R(s)=1-\overline{s}=F\circ J=J\circ F.
$$
These maps organize the strip symmetries used later. What to notice is that they isolate the critical line as a fixed set of \(R\), not as a conjectural statement.

$$
R\!\left(\tfrac12+it\right)=\tfrac12+it.
$$
So \(\operatorname{Re}(s)=\tfrac12\) is the fixed-point set of \(R\) in the strip. This geometric fact alone does not prove anything about where all zeros lie.

## 4. Prime routes and the square-root mirror

For prime \(p>1\) and \(s=\sigma+it\),
$$
p^{-s}=p^{-\sigma}e^{-it\log p}.
$$
This decomposes each prime contribution into amplitude and phase. It appears here because the balance claim is an amplitude claim.

On the critical line,
$$
p^{-(1/2+it)}=\frac{1}{\sqrt p}e^{-it\log p},\qquad
p^{-(1/2-it)}=\frac{1}{\sqrt p}e^{+it\log p}.
$$
Both routes share amplitude \(p^{-1/2}\) and reverse phase direction; this is the square-root mirror. It is a local structural symmetry, not a proof that \(\zeta\) vanishes there.

## 5. Local prime imbalance

Define
$$
B_p(\sigma)=\left|p^{-\sigma}-p^{-(1-\sigma)}\right|.
$$
This residual measures mismatch between mirror exponents. The key point is that vanishing means exact amplitude agreement.

Write \(\sigma=\tfrac12+\delta\):
\begin{align*}
B_p\!\left(\tfrac12+\delta\right)
&=\left|p^{-1/2-\delta}-p^{-1/2+\delta}\right|\\
&=2p^{-1/2}\left|\sinh(\delta\log p)\right|.
\end{align*}
Now the question reduces to where \(\sinh\) vanishes. This step does not invoke RH; it is elementary real analysis.

### Proposition 5.1

For every \(p>1\), \(B_p(\sigma)=0\) if and only if \(\sigma=\tfrac12\).

**Proof.** Since \(p^{-1/2}>0\),
$$
B_p\!\left(\tfrac12+\delta\right)=0
\iff \sinh(\delta\log p)=0.
$$
Because \(\log p\neq 0\) for \(p>1\) and \(\sinh x=0\) iff \(x=0\), we obtain \(\delta=0\), i.e. \(\sigma=\tfrac12\). The converse is immediate. \(\square\)

## 6. Finite global imbalance over primes

Let \(p_1<p_2<\cdots<p_N\) be the first \(N\) primes, and define
$$
B_N(\sigma)^2=\sum_{j=1}^{N} B_{p_j}(\sigma)^2.
$$
This aggregates local residuals into one finite measure. It appears to show that finite collections keep the same unique minimizer.

### Proposition 6.1

For every finite prime set \(\{p_1,\dots,p_N\}\) with \(p_j>1\),
$$
B_N(\sigma)=0 \iff \sigma=\tfrac12.
$$

**Proof.** If \(\sigma=\tfrac12\), each term \(B_{p_j}(\sigma)=0\), so \(B_N(\sigma)=0\). Conversely, if \(B_N(\sigma)=0\), each nonnegative term must vanish. Proposition 5.1 then gives \(\sigma=\tfrac12\). \(\square\)

### Remark 6.2

This is a finite-prime theorem. It does not by itself prove a global statement about all nontrivial zeros.

## 7. Prime-power echo field

In the half-plane \(\operatorname{Re}(s)>1\),
$$
\log\zeta(s)=\sum_p\sum_{k\ge 1}\frac{p^{-ks}}{k}.
$$
We label \(k=1\) terms as primitive routes and \(k\ge2\) as echo routes. The reader should notice the domain restriction: this expansion is used only where it converges.

## 8. Completed zeta and global closure residual

Define
$$
\Xi(t)=\xi\!\left(\frac12+it\right),\qquad C(t)=|\Xi(t)|^2.
$$
This is the global residual used across the series. It appears to cleanly separate local-prime arguments from global-completed-zeta language.

A global closure event is
$$
\Xi(t_n)=0.
$$
This introduces the eigenvalue notation \(t_n\) used later. It does not prove that all zeros are on the critical line.

## 9. Proven statements vs interpretations

### Proven in this paper

- The critical line is the unique local prime-route amplitude-balance line (Proposition 5.1).
- For every finite prime set, the finite global imbalance vanishes only at \(\sigma=\tfrac12\) (Proposition 6.1).

### Interpreted/formalized

- Zeta zeros are interpreted as global Perfect Closure events of \(C(t)=|\Xi(t)|^2\).
- This zeta closure residual becomes one face of the later operator framework in Paper 4.

### Not claimed

- No proof of the Riemann Hypothesis.
- No claim that Euler product formulas converge on \(\operatorname{Re}(s)=\tfrac12\).
- No claim that any single prime term cancels \(\zeta\).

## 10. Short bridge to Paper 2

Let
$$
Q=e^{u\phi}=\cos\phi+u\sin\phi,\qquad u^2=-1.
$$
If \(\operatorname{Re}(Q)=\tfrac12\), then \(\phi=\pi/3\), hence
$$
Q^3=-1,\qquad Q^6=1.
$$
Paper 2 studies this six-step gate in quaternionic orientation space.

## References

1. B. Riemann, *Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse* (1859).
2. E. C. Titchmarsh and D. R. Heath-Brown, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford Univ. Press, 1986.
3. H. M. Edwards, *Riemann's Zeta Function*, Dover, 2001.
4. B. Mazur and W. Stein, *Prime Numbers and the Riemann Hypothesis*, Cambridge Univ. Press, 2016.
5. E. Bombieri, “The Riemann Hypothesis,” Clay Mathematics Institute problem description.

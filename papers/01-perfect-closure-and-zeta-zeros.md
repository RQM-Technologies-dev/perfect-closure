# Zeta-Zero Perfect Closure: The Critical Line as a Square-Root Mirror

**John Van Geem / RQM Technologies**  
*Technical Manuscript - April 2026*

## Abstract

We define Perfect Closure in the zeta setting as a two-level structure: local prime-route amplitude balance and global completed-residual vanishing. We show that for each prime route, the critical line \\(\sigma=1/2\\) is the unique amplitude-balance location because the conjugate amplitudes are exactly square-root weighted, \\(p^{-1/2}\\). We then define the completed residual \\(\Xi(t)=\xi(1/2+it)\\), and we treat \\(\Xi(t_n)=0\\) as the global closure condition. This establishes a conservative hierarchy: local balance supports the geometric plausibility of closure, while global vanishing remains an analytic property of the completed function. This paper does not claim a proof of the Riemann Hypothesis.

## Keywords

Riemann zeta function; critical line; perfect closure; square-root mirror; completed zeta function; spectral trace.

## 1. Introduction

This paper sets the technical foundation for the series by clarifying what is local, what is global, and what is only interpretive language. We define **Perfect Closure** as vanishing residual structure in a chosen representation. In the zeta setting, we separate two residuals: a local prime-route imbalance and a global completed residual. This distinction is the key to maintaining mathematical caution.

The central thesis is: on the critical line, each prime route is square-rooted into equal-magnitude conjugate phase routes, and a zeta zero is a completed global closure event where \\(\Xi(t)\\) vanishes. The phrase "complex spectral trace" is retained only as a diagnostic label for the condition \\(\Xi(t_n)=0\\), not as the primary framing.

## 2. Contributions

We make four concrete contributions:

1. We define a local prime-route imbalance \\(B_p(\sigma)\\) and prove that its unique zero occurs at \\(\sigma=1/2\\).
2. We explain why \\(p^{-s}=p^{-\sigma}e^{-it\log p}\\) separates amplitude from phase and why this separation matters structurally.
3. We formalize the global closure condition as \\(\Xi(t_n)=0\\) with \\(\Xi(t)=\xi(1/2+it)\\).
4. We establish a conservative bridge to Paper 2: local square-root balance is necessary structural support but does not imply a proof of RH.

## 3. Mathematical Setup

Let
\\[
s=\sigma+it,\qquad p^{-s}=p^{-\sigma}e^{-it\log p}.
\\]
The factor \\(p^{-\sigma}\\) controls amplitude and the factor \\(e^{-it\log p}\\) controls phase rotation. This decomposition is essential because it separates two mechanisms that are often conflated in informal arguments.

On the critical line \\(\sigma=1/2\\),
\\[
p^{-(1/2\pm it)}=\frac{1}{\sqrt p}e^{\mp it\log p}.
\\]
Thus conjugate routes have equal amplitude \\(1/\sqrt p\\) and opposite phase direction. Off the critical line, \\(p^{-\sigma}\\neq p^{-(1-\sigma)}\\), so the two conjugate routes are not equally weighted. We interpret this as broken local mirror balance.

![Square-root mirror prime routes](../assets/figures/square-root-mirror-prime-routes.svg)

*Figure 1. Prime-route square-root mirror on \\(\sigma=1/2\\). Equal amplitudes and opposite phases visualize local balance; this does not imply termwise cancellation of \\(\zeta\\).* 

## 4. Formal Definitions and Proposition

We define the local imbalance
\\[
B_p(\sigma)=\left|p^{-\sigma}-p^{-(1-\sigma)}\right|.
\\]
Write \\(\sigma=1/2+\delta\\). Then
\\[
\begin{aligned}
B_p(1/2+\delta)
&=\left|p^{-1/2-\delta}-p^{-1/2+\delta}\right|\\
&=p^{-1/2}\left|p^{-\delta}-p^{\delta}\right|\\
&=p^{-1/2}\left|e^{-\delta\log p}-e^{\delta\log p}\right|\\
&=2p^{-1/2}|\sinh(\delta\log p)|.
\end{aligned}
\\]

### Proposition 1
For every prime \\(p>1\\),
\\[
B_p(\sigma)=0 \iff \sigma=1/2.
\\]

**Proof.** Since \\(p^{-1/2}>0\\), we have \\(B_p(1/2+\delta)=0\\iff\sinh(\delta\log p)=0\\). Because \\(\log p\neq0\\) and \\(\sinh x=0\\iff x=0\\), it follows that \\(\delta=0\\), hence \\(\sigma=1/2\\). Converse is immediate. \\(\square\\)

For finite sets of primes, \\(B_N^2(\sigma)=\sum_{j=1}^N B_{p_j}(\sigma)^2\\) has the same unique zero at \\(\sigma=1/2\\). This confirms that aggregating local balances does not move the local mirror line.

![Prime imbalance curve](../assets/figures/prime-imbalance-curve.svg)

*Figure 2. Typical behavior of \\(B_p(1/2+\delta)\\) for several primes, with zero at \\(\delta=0\\).* 

## 5. Interpretation and Discussion

The proposition is intentionally local: it identifies where conjugate amplitudes are matched route-by-route. It does not identify where the completed zeta function must vanish. This distinction matters because local mirror support is a structural input, while zeta zeros are global outcomes of analytic continuation and completion.

Composite and prime-power terms do not invalidate the local result. In the expansion
\\[
\log\zeta(s)=\sum_p\sum_{k\ge1}\frac{p^{-ks}}{k}\qquad (\Re(s)>1),
\\]
we may interpret \\(k=1\\) as primary prime routes and \\(k\ge2\\) as echo terms. Echo terms enrich global structure, but the unique local mirror statement for each prime remains unchanged.

Global closure is therefore defined using the completed residual:
\\[
\Xi(t)=\xi\!\left(\frac12+it\right),\qquad C(t)=|\Xi(t)|^2.
\\]
A closure event is
\\[
\Xi(t_n)=0 \quad\Leftrightarrow\quad C(t_n)=0.
\\]
This establishes the global target carried forward to Papers 2--4.

## 6. Interpretive Boundaries

- We do **not** claim a proof of the Riemann Hypothesis.
- We do **not** claim that local prime balance alone determines zero locations.
- We do **not** claim that an isolated prime route cancels \\(\zeta\\).
- We do **not** claim that "complex spectral trace" is the core thesis; it is a secondary diagnostic phrase for \\(\Xi(t_n)=0\\).

## 7. Conclusion

We defined Perfect Closure in a conservative two-level form: local square-root mirror balance and global completed-residual vanishing. We proved that local prime-route imbalance vanishes uniquely at \\(\sigma=1/2\\), and we set \\(\Xi(t_n)=0\\) as the global closure condition. This establishes the formal handoff to Paper 2, where the same closure variable is lifted from the classical complex line into quaternionic slice geometry.

## References

[1] B. Riemann, *Ueber die Anzahl der Primzahlen unter einer gegebenen Groesse*, 1859.  
[2] E. C. Titchmarsh and D. R. Heath-Brown, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford Univ. Press, 1986.  
[3] H. M. Edwards, *Riemann's Zeta Function*, Dover, 2001.

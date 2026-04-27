# Quaternionic Closure Pressure: Lifting the Critical-Line Pole into $S^3$

## Abstract

This paper develops a local quaternionic lift of the pole geometry of the completed Riemann zeta logarithmic derivative near a **simple** critical-line zero. Let
$$
\xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma\!\left(\frac s2\right)\zeta(s),
$$
and suppose
$$
\rho=\frac12+i\gamma
$$
is a simple zero of $\xi$. Then, in standard complex analysis,
$$
\frac{\xi'(s)}{\xi(s)}=\frac1{s-\rho}+\text{regular terms}
$$
locally near $\rho$. Prior numerical diagnostics in this project examined the radial closure-pressure functional
$$
Q(\delta,t;\gamma)=\delta\,\Re\!\left(\frac{\xi'}{\xi}\right)-(t-\gamma)\,\Im\!\left(\frac{\xi'}{\xi}\right),
$$
with $s=\tfrac12+\delta+it$, and found that near simple critical-line zeros one observes the expected unit residue behavior $Q\approx 1$. The present work lifts the local displacement $\delta+i\tau$ (where $\tau=t-\gamma$) to a quaternionic displacement
$$
\Delta q=\delta+n\tau,\qquad n^2=-1,
$$
and proposes a local quaternionic closure-pressure field
$$
L_q(\Delta q)=(\Delta q)^{-1}+H_q(\Delta q),
$$
with bounded regular remainder $H_q$. The pure pole part satisfies $\Delta q(\Delta q)^{-1}=1$, and motivates a local quaternionic Perfect Closure condition
$$
\Delta q\,L_q(\Delta q)\to 1\qquad (\Delta q\to 0).
$$
No claim is made that this proves the Riemann Hypothesis (RH), that $\xi$ has already been globally extended as a quaternionic entire function, or that noncommutative analytic issues are solved. The contribution is a local geometric lift of known simple-pole behavior into a quaternionic identity-return language.

## 1. Introduction

The prior paper, *The Critical Line as the Mirror-Balance Axis*, framed $\Re(s)=\tfrac12$ as the symmetry-centered axis of the completed zeta functional equation. The associated numerical work introduced local drift and pressure diagnostics including $D(\delta,t)$, $P(\delta,t)$, and a radial detector $Q(\delta,t;\gamma)$ near known critical-line zeros. Empirically, these diagnostics were consistent with the standard residue geometry of simple zeros: a local inverse displacement law controls leading behavior.

The next step is not to globalize prematurely, but to sharpen the local geometry of that residue. Near a simple zero, complex analysis says $\xi'/\xi$ has a first-order pole with residue $1$. In coordinates centered at the zero, the pole has radial form. This makes it natural to ask whether the local inverse law can be re-expressed as a quaternionic inversion structure that preserves the same radial residue while exposing additional orientation data.

This paper provides that local lift. It is deliberately scoped:

1. **Standard analytic facts** are used only in their local complex form (simple pole of $\xi'/\xi$ at a simple zero).
2. **Numerical evidence already generated** is treated as consistency support for residue behavior, not as a proof mechanism.
3. **Quaternionic interpretation** is proposed as a local geometric encoding of inverse displacement.
4. **Open proof obligations** are listed explicitly, especially for any future claim linking closure conditions to global zero location.

The conceptual payoff is a cleaner statement of Perfect Closure at the pole level: not merely vanishing of a scalar observable, but local return to quaternionic identity under singular inversion plus bounded remainder.

## 2. Local Pole Geometry of the Completed Zeta Function

Define
$$
\xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma\!\left(\frac s2\right)\zeta(s).
$$
Let
$$
\rho=\frac12+i\gamma
$$
be a simple zero of $\xi$. Then there is a neighborhood of $\rho$ in which
$$
\frac{\xi'(s)}{\xi(s)}=\frac1{s-\rho}+R(s),
$$
where $R$ is holomorphic (regular) near $\rho$.

Write
$$
s=\frac12+\delta+it,\qquad \tau=t-\gamma,
$$
so
$$
s-\rho=\delta+i\tau.
$$
The leading pole term is
$$
\frac1{\delta+i\tau}=\frac{\delta-i\tau}{\delta^2+\tau^2}.
$$
Hence
$$
\Re\!\left(\frac1{\delta+i\tau}\right)=\frac{\delta}{\delta^2+\tau^2},
\qquad
\Im\!\left(\frac1{\delta+i\tau}\right)=-\frac{\tau}{\delta^2+\tau^2}.
$$
Therefore
$$
\delta\,\Re\!\left(\frac1{\delta+i\tau}\right)-\tau\,\Im\!\left(\frac1{\delta+i\tau}\right)
=\frac{\delta^2+\tau^2}{\delta^2+\tau^2}=1.
$$
This identity is the precise local origin of the unit radial closure-pressure residue.

## 3. The Radial Closure-Pressure Functional

The diagnostic used in the prior numerical work is
$$
Q(\delta,t;\gamma)=\delta\,\Re\!\left(\frac{\xi'(s)}{\xi(s)}\right)-(t-\gamma)\,\Im\!\left(\frac{\xi'(s)}{\xi(s)}\right),
\qquad s=\frac12+\delta+it.
$$
Setting $\tau=t-\gamma$, and inserting
$$
\frac{\xi'}{\xi}=\frac1{\delta+i\tau}+R,
$$
one gets
$$
Q(\delta,t;\gamma)=1+\delta\,\Re R-\tau\,\Im R.
$$
Because $R$ is bounded near $\rho$, the correction term tends to $0$ as $(\delta,\tau)\to(0,0)$, so
$$
Q(\delta,t;\gamma)\to 1
$$
for a simple zero.

Interpretively, this does not produce new location theorems; it re-reads a classical residue statement through a radial detector aligned with displacement coordinates. Numerically seeing $Q\approx1$ near known simple critical-line zeros is exactly what one should expect from the analytic pole law. That is useful confirmation and calibration, but not proof of RH.

## 4. Quaternionic Lift of the Local Displacement

The complex displacement variable
$$
\delta+i\tau
$$
selects one imaginary axis. To encode orientation more generally, introduce a unit imaginary quaternion $n$ with
$$
n^2=-1,\qquad \|n\|=1,
$$
and define
$$
\Delta q=\delta+n\tau.
$$
Quaternionic conjugation gives
$$
\overline{\Delta q}=\delta-n\tau,
$$
and norm
$$
N(\Delta q)=\Delta q\,\overline{\Delta q}=\delta^2+\tau^2.
$$
Hence for $\Delta q\neq0$,
$$
(\Delta q)^{-1}=\frac{\overline{\Delta q}}{N(\Delta q)}
=\frac{\delta-n\tau}{\delta^2+\tau^2}.
$$
This is the direct quaternionic analogue of
$$
\frac1{\delta+i\tau}=\frac{\delta-i\tau}{\delta^2+\tau^2}.
$$

Geometrically, choosing $i$ fixes one complex slice. Allowing $n$ to vary over all unit imaginary quaternions sweeps the 2-sphere of imaginary directions, and the corresponding unit quaternions form $S^3$ under multiplication. The local lift does not require global quaternionic analyticity of $\xi$; it only rewrites the displacement-residue geometry of the local pole.

## 5. Quaternionic Closure-Pressure Field

Define a local quaternionic field model
$$
L_q(\Delta q)=(\Delta q)^{-1}+H_q(\Delta q),
$$
where $H_q$ is assumed bounded and regular near $\Delta q=0$. It plays the role of a nonsingular remainder mirroring the complex regular term $R(s)$.

Define the pure pole part
$$
L_q^{(0)}(\Delta q):=(\Delta q)^{-1}.
$$
Then
$$
\Delta q\,L_q^{(0)}(\Delta q)=\Delta q(\Delta q)^{-1}=1.
$$
This is an exact quaternionic algebra identity (for nonzero $\Delta q$), and it is the core identity-return pattern underlying the lift.

Define the quaternionic closure detector
$$
Q_q(\Delta q):=\Re\!\big[\Delta q\,L_q(\Delta q)\big].
$$
For the pure pole,
$$
Q_q^{(0)}(\Delta q)
=\Re\!\big[\Delta q(\Delta q)^{-1}\big]
=\Re(1)=1.
$$
Thus the scalar detector reproduces the same unit radial residue in quaternionic form.

## 6. Quaternionic Perfect Closure

We define local quaternionic Perfect Closure by
$$
\lim_{\Delta q\to0}\Delta q\,L_q(\Delta q)=1.
$$
Equivalently,
$$
\Re\!\big[\Delta qL_q(\Delta q)\big]\to1,
\qquad
\Im\!\big[\Delta qL_q(\Delta q)\big]\to0.
$$
This has three immediate interpretations:

- the real closure detector tends to $1$;
- tangential/quaternionic imaginary residue tends to $0$;
- the local field resolves to identity (no residual local rotation).

**Perfect Closure is the condition that the singular pressure field resolves to the identity, leaving no residual radial or tangential quaternionic displacement.**

This is a definition and interpretive framework, not a theorem claiming that every local model of $\xi'/\xi$ admits such a quaternionic realization globally.

## 7. Closure Class Associated with a Critical-Line Zero

Given a critical-line zero height $\gamma$, define the associated quaternionic orientation family
$$
\mathcal C_\gamma=\left\{\frac12+n\gamma:\ n^2=-1\right\}.
$$
This should be read carefully:

- it is **not** a claim of newly discovered quaternionic zeros of $\zeta$;
- it is a local geometric class encoding all imaginary orientations compatible with the same scalar height parameter;
- the usual complex zero $\frac12+i\gamma$ is one selected slice (say $n=i$) through this family.

Interpretively, the complex critical-line zero records one oriented view of a closure event. The quaternionic lift encodes the full orientation family of the same local inverse-pressure geometry.

## 8. Relation to the Mirror-Balance Axis

The mirror-balance framework centers real trace at $\Re(s)=\tfrac12$. The quaternionic displacement model preserves this trace by construction through
$$
q=\frac12+\Delta q=\frac12+\delta+n\tau.
$$
The local singularity center corresponds to $\delta=0$, i.e., real part $\tfrac12$ in the complex slice.

A natural future obstruction statement is:
$$
\Delta qL_q(\Delta q)\to1
\quad\Longrightarrow\quad
\Re(q)=\frac12.
$$
This implication is **not proved here**. It is a target for future work: if a rigorous framework showed that unit quaternionic identity-return closure forces mirror-balance trace, that would supply a principled route from local closure to axis localization.

At present, this paper only formulates the lift and target statement; it does not deliver the obstruction theorem.

## 9. Numerical Reproducibility Context

The numerical diagnostic framework reused here is:

- $D(\delta,t)=\Re\!\left(\xi'/\xi\right)$,
- $P(\delta,t)=\delta\,D(\delta,t)$,
- $Q(\delta,t;\gamma)=\delta\Re(\xi'/\xi)-(t-\gamma)\Im(\xi'/\xi)$.

Near simple critical-line zeros, one observes $Q\approx1$ on sufficiently small punctured neighborhoods, in line with residue theory and bounded regular correction. This empirical behavior motivated the quaternionic detector
$$
Q_q(\Delta q)=\Re\!\big[\Delta qL_q(\Delta q)\big].
$$

The reproducibility script added with this paper computes $\xi'/\xi$ via `mpmath`, evaluates $Q$ near the first several known heights, and optionally generates a heatmap for the first zero neighborhood when `matplotlib` is available.

If project figures matching these diagnostics are not already available, the following placeholders may be used:

- **Figure 1:** Pole-normalized pressure near the first zero.
- **Figure 2:** Radial $Q$ heatmap near the first zero.
- **Figure 3:** Deviation $|Q-1|$ near the first zero.

## 10. Open Proof Obligations

The quaternionic lift is intentionally local and leaves major proof tasks open:

1. Develop a rigorous quaternionic analytic extension (or a precise slice-local formalism) tied to the completed zeta setting.
2. Determine whether local quaternionic closure classes can be globalized consistently across zeros and heights.
3. Prove or disprove that unit closure residues force real trace $\Re=\tfrac12$.
4. Relate quaternionic closure constraints to the exact functional equation $\xi(s)=\xi(1-s)$.
5. Separate clearly theorems about residue detection from theorems about zero location.

These are essential before any RH-level inference could be justified.

### 10.1 Why local residue control is necessary but insufficient

The local model
$$
\frac{\xi'(s)}{\xi(s)}=\frac1{s-\rho}+R(s)
$$
is exact and informative near a fixed simple zero, but by itself it cannot determine where *all* zeros must lie. Any meromorphic function with simple zeros has a logarithmic derivative with first-order poles. What is specific to the zeta setting is the global completion symmetry and the way it couples distant regions of the strip. A full RH-level argument would need to combine:

- local residue structure at each candidate zero;
- global constraints from $\xi(s)=\xi(1-s)$;
- quantitative obstruction of off-axis closure.

The present paper addresses only the first item directly while introducing language intended to support the second and third.

### 10.2 Noncommutativity and ordering caveats

Quaternionic multiplication is noncommutative, so products that coincide in $\mathbb C$ can bifurcate in $\mathbb H$. For example,
$$
\Delta q\,L_q(\Delta q)\quad\text{and}\quad L_q(\Delta q)\,\Delta q
$$
need not agree once noncentral remainder terms are included. Here we adopt the left product convention in the Perfect Closure condition
$$
\Delta qL_q(\Delta q)\to 1,
$$
because it aligns with the chosen detector definition $Q_q(\Delta q)=\Re[\Delta qL_q(\Delta q)]$. A future rigorous framework should either justify this convention as canonical or prove left-right equivalence in the relevant local class.

### 10.3 Multiplicity dependence

The unit residue statement is tied to simple zeros. If $\rho$ had multiplicity $m>1$, then locally
$$
\frac{\xi'(s)}{\xi(s)}\sim\frac{m}{s-\rho},
$$
and the radial detector would approach $m$ (up to regular corrections), not $1$. Thus this paper’s “unit radial residue” language always includes the simple-zero assumption. This dependency is intentional and explicit.

## 11. Claims Discipline and Scope Boundaries

To prevent overreach, we separate claim types explicitly:

- **Established local analytic fact:** for simple zero $\rho$, $\xi'/\xi$ has local pole $1/(s-\rho)$.
- **Established algebraic fact:** $\Delta q(\Delta q)^{-1}=1$ for nonzero $\Delta q$.
- **Numerical consistency fact:** $Q\approx1$ near tested simple critical-line zero heights.
- **Proposed geometric lift:** replace $\delta+i\tau$ by $\delta+n\tau$ to encode orientation families.
- **Proposed closure definition:** Perfect Closure as $\Delta qL_q(\Delta q)\to1$.
- **Open conjectural direction:** use closure constraints to force mirror-balance trace globally.

Accordingly, this work does **not** claim:

- a proof of RH;
- a complete quaternionic entire extension of $\xi$;
- a solved noncommutative analytic framework for global zeta dynamics;
- discovery of new quaternionic zeros of $\zeta$.

### 11.1 Separation of evidence channels

Three evidence channels are used, each with different status:

1. **Deductive analytic:** local pole expansion of $\xi'/\xi$ at simple zeros.
2. **Computational:** finite-precision samples of $Q$ near selected known heights.
3. **Interpretive geometric:** quaternionic orientation-family lift of displacement.

To avoid category errors, these channels are never merged into a single proof claim in this manuscript.

### 11.2 What the lift contributes

The quaternionic lift contributes (i) an explicit orientation parameter $n$ over the unit imaginary sphere and (ii) an identity-return product form $\Delta qL_q(\Delta q)$ that sharpens closure language beyond scalar diagnostics. It does not, by itself, generate a new location theorem for zeros.

## 12. Conclusion

The local pole geometry of $\xi'/\xi$ near a simple critical-line zero already contains a precise unit residue law. Prior pressure diagnostics captured this as $Q\approx1$ in complex coordinates. The present paper lifts that same local structure into quaternionic form by replacing $\delta+i\tau$ with $\Delta q=\delta+n\tau$ and interpreting inverse displacement as quaternionic radial inversion.

In this language, a critical-line zero is not only a complex cancellation point but a visible slice of a quaternionic closure center with unit radial residue. The pure pole identity $\Delta q(\Delta q)^{-1}=1$ motivates a stronger local condition,
$$
\Delta qL_q(\Delta q)\to1,
$$
interpreted as identity return with no residual quaternionic tangential component.

This reframing is geometric and local. It sharpens closure language but does not solve RH. The central value of the lift is conceptual precision: a simple zero produces unit radial residue, and in quaternionic notation that residue is encoded as local identity return under inverse-pressure flow.

Viewed this way, the lift acts as a translation dictionary: classical complex residue data are preserved exactly at leading order, while quaternionic notation exposes orientation degrees of freedom that are hidden when one freezes the imaginary axis. The mathematical burden remains to determine which, if any, of those orientation constraints become globally rigid under the completed functional equation.

## 13. Technical Addendum: Local Error Scale of the Detector

Write the local expansion as
$$
\frac{\xi'(s)}{\xi(s)}=\frac1{\delta+i\tau}+R(\delta,\tau),
$$
with bounded remainder on a punctured neighborhood,
$$
|R(\delta,\tau)|\le M.
$$
Then
$$
Q(\delta,t;\gamma)-1
=\delta\,\Re R(\delta,\tau)-\tau\,\Im R(\delta,\tau),
$$
so
$$
|Q-1|
\le |\delta|\,|\Re R|+|\tau|\,|\Im R|
\le (|\delta|+|\tau|)M.
$$
Hence the deviation from unit residue is first-order in local displacement scale when the remainder is bounded.

In quaternionic form, if
$$
L_q(\Delta q)=(\Delta q)^{-1}+H_q(\Delta q),
\qquad \|H_q(\Delta q)\|\le M_q,
$$
then
$$
\Delta qL_q(\Delta q)-1=\Delta qH_q(\Delta q),
$$
and therefore
$$
\|\Delta qL_q(\Delta q)-1\|
\le \|\Delta q\|\,M_q.
$$
So the quaternionic identity-return condition has an analogous first-order stability estimate under bounded regular perturbation. This addendum is local and qualitative; deriving explicit uniform constants in wider regions remains open.

## 14. Methodological Notes for Reproducibility and Interpretation

This section records practical guidance for reading and reproducing the numerical side of the argument without conflating it with theorem-level claims.

### 14.1 Why evaluate on punctured neighborhoods

The detector uses $\xi'/\xi$, which is singular at zeros. Any direct sample exactly at $s=\rho$ is undefined (or numerically unstable as division by near-zero with unresolved cancellation). The diagnostic is therefore evaluated on *punctured* neighborhoods:
$$
(\delta,\tau)\neq(0,0),\qquad |\delta|,|\tau|\ll1.
$$
The local law predicts approach to $1$ as the sample contracts toward the center, not equality at the singular point itself.

### 14.2 Choice of offsets and expected scaling

Small offsets such as $10^{-3}$ or $10^{-4}$ usually balance two competing effects:

- small enough for pole dominance over regular remainder;
- not so small that finite-precision differentiation becomes numerically noisy.

Because $Q-1$ scales at first order under bounded remainder, one expects smaller offsets to reduce deviation until floating-point/precision effects dominate. A good practice is to compare multiple offset scales and verify trend consistency rather than relying on a single grid size.

### 14.3 Numerical differentiation caveat

The script computes $\xi'(s)$ numerically (via `mpmath`) and divides by $\xi(s)$. This is adequate for local diagnostics but introduces error from two sources:

1. derivative approximation at finite precision;
2. division amplification near small $|\xi(s)|$.

Increasing working precision (`mp.mp.dps`) generally improves stability but increases runtime. The current script uses modest precision to keep execution practical in a standard development environment.

### 14.4 Heatmaps as qualitative diagnostics

Heatmaps of $Q$ and $|Q-1|$ near the first zero are intended to show geometry qualitatively:

- an approximately radial region with values clustered near $1$ away from the exact singular center;
- bounded, structured deviation compatible with a nonzero regular remainder.

Such plots are useful sanity checks for the residue interpretation, but they are not substitutes for proofs. Color scaling, interpolation choices, and grid resolution can all alter visual impressions.

### 14.5 Interpreting agreement across zero heights

Testing several known heights serves two purposes:

- confirms behavior is not an isolated artifact of the first zero;
- checks implementation consistency across different imaginary scales.

Agreement with $Q\approx1$ near each tested simple zero is exactly consistent with complex residue theory. It supports the detector’s validity as a local probe, while remaining agnostic about global localization of all zeros.

### 14.6 Relationship to prior mirror-balance diagnostics

In prior notation, one can view
$$
D(\delta,t)=\Re\left(\frac{\xi'}{\xi}\right),
$$
as a real-direction drift observable, and
$$
P(\delta,t)=\delta D(\delta,t)
$$
as a partial pressure component. The full radial detector
$$
Q=\delta\Re\left(\frac{\xi'}{\xi}\right)-\tau\Im\left(\frac{\xi'}{\xi}\right)
$$
combines real and tangential contributions into a residue-normalized scalar. The quaternionic detector
$$
Q_q(\Delta q)=\Re[\Delta qL_q(\Delta q)]
$$
is designed to preserve this normalization logic while opening an orientation-aware extension.

### 14.7 Interpretation discipline for future work

The intended workflow for subsequent papers is:

1. keep analytic statements tied to explicit hypotheses (simple zero, local neighborhood);
2. report computations as finite tests with precision and sampling metadata;
3. separate proposed geometric definitions from theorem claims;
4. state clearly which bridge lemmas are still missing for any RH implication.

This discipline is especially important in speculative extensions (quaternionic, operator-theoretic, or physical analogies), where intuitive geometry can outpace established analytic control.

---

## Appendix A. Key Equations

1. Completed zeta:
$$
\xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma\!\left(\frac s2\right)\zeta(s).
$$

2. Local logarithmic derivative near a simple zero $\rho$:
$$
\frac{\xi'(s)}{\xi(s)}=\frac1{s-\rho}+\text{regular terms}.
$$

3. Local displacement coordinates:
$$
s-\rho=\delta+i\tau,\qquad \tau=t-\gamma.
$$

4. Radial closure-pressure functional:
$$
Q(\delta,t;\gamma)=\delta\Re\!\left(\frac{\xi'}{\xi}\right)-(t-\gamma)\Im\!\left(\frac{\xi'}{\xi}\right).
$$

5. Quaternionic displacement:
$$
\Delta q=\delta+n\tau,\qquad n^2=-1.
$$

6. Quaternionic inverse:
$$
(\Delta q)^{-1}=\frac{\delta-n\tau}{\delta^2+\tau^2}.
$$

7. Quaternionic local field:
$$
L_q(\Delta q)=(\Delta q)^{-1}+H_q(\Delta q).
$$

8. Quaternionic closure detector:
$$
Q_q(\Delta q)=\Re\!\big[\Delta qL_q(\Delta q)\big].
$$

9. Perfect Closure condition:
$$
\Delta qL_q(\Delta q)\to1\quad (\Delta q\to0).
$$

## Appendix B. Claims Classification

| Statement | Status | Notes |
|---|---|---|
| $\xi'/\xi$ has a simple pole at a simple zero | standard analytic fact | local logarithmic derivative |
| $Q\approx1$ near a simple zero | standard residue behavior + numerical confirmation | depends on simple-zero assumption |
| $\delta+i\tau$ can be locally lifted to $\delta+n\tau$ | proposed quaternionic geometric lift | local, not global |
| $\Delta q(\Delta q)^{-1}=1$ | algebraic identity | quaternionic inverse |
| Perfect Closure means $\Delta qL_q\to1$ | proposed definition | needs further development |
| Critical-line zeros are quaternionic closure centers | interpretive framework | not an RH proof |
| Off-axis unit closure is impossible | not proven | future proof target |

# The Zeta-Mass Closure Operator: Perfect Closure as an Eigenvalue Law

**John Van Geem / RQM Technologies**  
*Research Note - April 2026*

## Abstract

This paper gives the main synthesis of the series. The same value \(t_n\) appears in three aligned forms:
$$
\Xi(t_n)=0,
$$
$$
\mathcal A_{\mathbf u}\chi_t=t\chi_t,
$$
$$
P\bar P=\left(\frac{\hbar t_n}{L_\ast}\right)^2.
$$
The first equation is the complex spectral-trace face, the second is the quaternionic operator face, and the third is the physical mass-shell face after scale conversion by \(L_\ast\). This paper states the bridge formally, while keeping non-claim boundaries explicit: it is not a proof of RH and not a derivation of observed particle masses.

## Reader Guide

Paper 4 answers: **how can one eigenvalue have a zeta face and a mass-shell face?**

The strategy is to keep one symbol \(t_n\) fixed while changing the interpretation context:

1. In the complex residual context, \(t_n\) is where \(\Xi\) vanishes.
2. In the operator context, \(t_n\) is an eigenvalue of \(\mathcal A_{\mathbf u}\).
3. In the physical context, \(t_n\) sets invariant norm after conversion by \(L_\ast\).

This paper is therefore a compatibility map across three languages, not a claim that those languages are already experimentally unified.

To help readers track equation roles, the same symbol set is used in each section:

- \(t_n\) always denotes a closure-labeled spectral value.
- \(\mathcal A_{\mathbf u}\) always denotes the slice-oriented dilation operator.
- \(L_\ast\) always denotes the spectral-to-physical conversion length.

When these symbols recur, they should be read as the same structural objects viewed in different equation contexts, not as new definitions each time.

![Main zeta-to-mass-shell pipeline](../assets/figures/zeta-to-mass-shell-pipeline.svg)

*Figure: Main synthesis pipeline from complex spectral trace \(\Xi(t_n)=0\) to quaternionic closure eigenvalue \(\mathcal A_{\mathbf u}\chi_{t_n}=t_n\chi_{t_n}\) to mass-shell norm \(P\bar P=(\hbar t_n/L_\ast)^2\). It summarizes the bridge logic and does not by itself prove RH or derive observed masses.*

## 1. Internal scale operator and eigenmodes

Let \(\rho>0\) and define
$$
\mathcal A_{\mathbf u}=\mathbf u\left(\rho\frac{d}{d\rho}+\frac12\right),\qquad \mathbf u^2=-1.
$$
The operator \(\rho\frac{d}{d\rho}\) is a dilation generator, so \(\mathcal A_{\mathbf u}\) is a quaternionic-oriented dilation operator with the half-shift included.

Equation reading note: the half-shift \(+1/2\) is included so that power modes of the form \(\rho^{-1/2-\mathbf u t}\) return a clean eigenvalue \(t\) after the full operator action. Without this shift, the same mode ansatz would carry an extra constant offset.

Take eigenmodes
$$
\chi_t(\rho)=\rho^{-1/2-\mathbf u t}.
$$
Now compute explicitly:
$$
\frac{d}{d\rho}\rho^{-1/2-\mathbf u t}=\left(-\frac12-\mathbf u t\right)\rho^{-3/2-\mathbf u t},
$$
so
$$
\rho\frac{d}{d\rho}\chi_t=\left(-\frac12-\mathbf u t\right)\chi_t.
$$
Then
$$
\left(\rho\frac{d}{d\rho}+\frac12\right)\chi_t=-\mathbf u t\,\chi_t,
$$
and multiplying by \(\mathbf u\) gives
$$
\mathcal A_{\mathbf u}\chi_t=t\chi_t,
$$
because \(\mathbf u(-\mathbf u)=1\). This is the operator-side origin of the eigenvalue label used in the bridge.

Interpretive summary of Section 1: the operator equation does not yet use zeta zeros. It only establishes that the mode family is naturally indexed by a real parameter \(t\) that behaves as an eigenvalue. This index is what the next section constrains using the complex closure condition \(\Xi(t_n)=0\).

![Closure operator bridge](../assets/figures/closure-operator-bridge.svg)

*Figure: Operator bridge chain \(\rho \rightarrow \chi_t(\rho)=\rho^{-1/2-\mathbf u t} \rightarrow \mathcal A_{\mathbf u} \rightarrow \Xi(\mathcal A_{\mathbf u}) \rightarrow\) kernel mode at \(t_n\rightarrow\) mass-shell lift through \(L_\ast\). This supports the map in Sections 1-3 and is not a standalone proof.*

## 2. Complex zeta-slice condition and selector

Define
$$
\Xi(t)=\xi\!\left(\frac12+it\right).
$$
A complex spectral trace value is any \(t_n\) satisfying
$$
\Xi(t_n)=0.
$$
Now introduce the selector operator
$$
\mathcal Z_{\mathbf u}=\Xi(\mathcal A_{\mathbf u}).
$$
Formally, this means we evaluate the same scalar residual function on the operator spectrum. For an eigenmode \(\chi_t\), functional calculus gives
$$
\Xi(\mathcal A_{\mathbf u})\chi_t=\Xi(t)\chi_t.
$$
Therefore, if \(\Xi(t_n)=0\), then
$$
\Xi(\mathcal A_{\mathbf u})\chi_{t_n}=0.
$$
This is the kernel statement linking complex trace and quaternionic eigenmode. The equation does not say the complex and quaternionic theories are identical in all respects; it says that zero-labeled spectral values are carried consistently by the chosen operator model.

Equation reading note: the implication
\[
\Xi(t_n)=0 \Longrightarrow \Xi(\mathcal A_{\mathbf u})\chi_{t_n}=0
\]
is a spectral transport statement. It moves a scalar zero condition into an operator-kernel condition on a corresponding mode. The map is one-way in this presentation: zero-labeled scalar inputs define selected kernel modes in the operator picture.

## 3. Mass-shell norm realization after scaling

Take the physical invariant norm relation
$$
P\bar P=m^2c^2.
$$
Introduce the closure-conversion scale \(L_\ast\) via
$$
\log\rho=\ell/L_\ast.
$$
This equation converts dimensionless dilation coordinate into physical length coordinate. Matching closure curvature to Compton curvature yields
$$
m_n=\frac{\hbar}{cL_\ast}|t_n|.
$$
The right side has units of mass because \(\hbar/(cL_\ast)\) has units of mass and \(t_n\) is dimensionless.

Dimensional reading:

- \(t_n\): dimensionless spectral coordinate,
- \(L_\ast\): length,
- \(\hbar/c\): momentum-length scale,
- \(\hbar/(cL_\ast)\): mass scale.

So the equation \(m_n=\frac{\hbar}{cL_\ast}|t_n|\) is the minimal linear map that respects unit consistency while preserving the absolute-value symmetry in \(t_n\).

Equivalent forms are
$$
P\bar P=\left(\frac{\hbar t_n}{L_\ast}\right)^2,
$$
and
$$
L_\ast=t_n\frac{\hbar}{mc}=t_n\bar\lambda_C.
$$
The first emphasizes invariant norm realization. The second emphasizes conversion-length interpretation: a chosen pairing \((m,t_n)\) implies a corresponding \(L_\ast\).

Practical reading: if \(L_\ast\) is independently fixed, the equations predict \(m_n\) from \(t_n\). If \(L_\ast\) is allowed to vary freely for every pairing, the same equations become descriptive identities with weaker predictive force. Paper 5 formalizes this distinction.

## 4. Complex Spectral Slices of Quaternionic Mass Shells

The synthesis can now be read as one value with two external faces and one internal role:

- complex face: \(\Xi(t_n)=0\),
- operator role: \(\mathcal A_{\mathbf u}\chi_{t_n}=t_n\chi_{t_n}\),
- physical face: \(P\bar P=(\hbar t_n/L_\ast)^2\).

![Two faces of \(t_n\)](../assets/figures/tn-two-faces-bridge.svg)

*Figure: The same ordinate \(t_n\) read in two sectors: complex spectral face \(\Xi(t_n)=0\) and mass-shell face \(P\bar P=(\hbar t_n/L_\ast)^2\). The figure is interpretive guidance and does not claim that zeta zeros are particles or that RH is proven.*

The zeta zero is therefore not identified with a particle. It is interpreted as a spectral trace value that can be carried, under the stated map, into a mass-shell norm expression.

This is the most important interpretation boundary in the paper: \"trace\" and \"realization\" are different words on purpose. The trace is a complex spectral condition. The realization is a physical norm statement after conversion. Keeping those levels distinct avoids category errors.

## 5. Optional supporting mechanisms

### 5.1 Closure Cadence (optional)

For phase \(e^{-\mathbf u t_n\log\rho}\), define
$$
\Lambda_n=\frac{2\pi}{t_n},\qquad \Delta_n=\frac{\pi}{3t_n}.
$$
\(\Lambda_n\) is a full cycle length in log-scale variable; \(\Delta_n\) is a sixth-cycle step. These are geometric cadence markers. They are optional and not part of the core operator proof chain.

They are included because readers often ask how the six-step closure language can be reflected in a continuous \(\rho\)-based mode model. These cadence quantities provide one intuitive answer, but they do not alter the bridge equations in Sections 1-3.

### 5.2 Completion layer inside \(\Xi\) (optional)

The completed zeta expression is
$$
\xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
$$
This equation reminds us that \(\Xi\) is already a completed residual containing symmetry and regularizing factors. It supports why the series uses \(\Xi\), not bare \(\zeta\), as its closure object.

## 6. Non-claims and bridge to Paper 5

- No proof of RH.
- No claim that zeta zeros are particles.
- No derived universal \(L_\ast\) in this paper.
- No Standard Model mass derivation.

Paper 5 asks the decisive predictive question: can \(L_\ast\) be fixed independently, or at least stabilize across predeclared families strongly enough to generate testable out-of-sample predictions?

## References

1. E. C. Titchmarsh and D. R. Heath-Brown, *The Theory of the Riemann Zeta-Function*, 1986.
2. H. M. Edwards, *Riemann's Zeta Function*, 2001.
3. S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields*, 1995.


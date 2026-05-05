# Quaternionic Standing-Wave Closure

## Core geometric object

Use unit quaternions
\[
q(\phi,\mathbf u)=\cos\phi+\mathbf u\sin\phi,
\]
where \(\mathbf u\) is a unit pure-imaginary quaternion (\(\mathbf u^2=-1\)).

Quaternionic phase evolution is a rotation on \(S^3\). The closure question is whether the phase flow is open (non-returning in rest-frame structure) or self-returning as a standing resonance.

## Closure language

- **Open propagation:** phase flow without stable self-return (free radiation mode).
- **Closed propagation:** phase returns under conjugate composition into a persistent resonance.
- **Mass shell (interpretive):** stable closed quaternionic standing-wave state.

This repo uses closure language as a structural interpretation layered over standard physics, not as a replacement formalism.

## Standing-wave intuition

In a standing-wave closure state, counter-directed phase routes are locked by a global closure condition. The net result is not cancellation to zero field everywhere, but persistence of a bounded resonance pattern with invariant shell properties.

That is why the thesis uses:

\[
\text{mass} \equiv \text{closed light-like phase}.
\]

The phrase means "stable self-closed phase architecture," not "literal trapped photons in a classical cavity model."

## Conjugate quaternionic routes and relativistic closure

To connect quaternionic closure directly to the minimal relativistic bridge, define conjugate phase routes
\[
q_+(\phi)=e^{\mathbf u\phi},
\qquad
q_-(\phi)=e^{-\mathbf u\phi},
\]
with \(\mathbf u^2=-1\). Their product is
\[
q_+q_-=1.
\]

This identity-return condition is the quaternionic encoding of directional closure: conjugate routes close displacement under composition.

The corresponding two-route kinematic model is
\[
p_+^\mu=\left(\frac{E}{c},+\mathbf p\right),
\qquad
p_-^\mu=\left(\frac{E}{c},-\mathbf p\right),
\]
so each route is null (\(E^2-p^2c^2=0\)), while the total is
\[
P^\mu=\left(\frac{2E}{c},0\right),
\]
with invariant mass \(M=2E/c^2\).

Interpretation:

The conjugate phase routes close to identity. Directional displacement cancels, but the enclosed phase energy remains as invariant rest mass.

## Link to shell locking

Quaternionic closure gets operationalized through spectral shells on
\[
M=S^3\times\mathbb R_s.
\]

The shell-number operator
\[
\hat N=\sqrt{-\Delta_{S^3}+1}
\]
and locking condition
\[
\hat N=\frac{s^2}{2}
\]
provide the quantized closure framework used in the hydrogen bridge.

## What is and is not claimed

Claimed:

- quaternionic geometry provides a natural language for phase closure/return;
- closure shells offer a disciplined bridge from thesis language to spectral models.

Not claimed:

- a full microscopic derivation of all interactions;
- a replacement for QED/QM/relativistic field theory;
- an all-constants-from-zero first-principles construction.

---

See also: [Hydrogen closure bridge](hydrogen-closure-bridge.md), [Claim boundaries](claim-boundaries.md)

# Perfect Closure

## The Breakthrough in One Sentence

> **Mass is what light becomes when phase closes.**

Perfect Closure is a proposal about structure, not a replacement for established physics. Free light is non-closing phase propagation: it travels without forming a rest-frame standing structure. Mass appears when light-like phase routes close into a stable standing configuration whose net spatial momentum cancels while energy remains. In this view, matter is not a separate substance from light, but a different regime of phase organization. Hydrogen shell-locking is presented here as the first calibrated bridge from that closure thesis to measured spectral structure.

> **It is all light; light that has closure becomes mass.**

## Why this matters

If this framework continues to hold, it offers a clean geometric language for how stability and invariant mass can emerge from null/lightlike components. It also provides a disciplined bridge from wave-closure ideas to observable spectra, starting with hydrogen and extending through a test program rather than broad first-principles claims.

## What is new here

- The front-facing claim is explicitly the light-to-mass closure thesis.
- The conservative bridge is explicit: individually null routes can sum to a closed configuration with canceled net spatial momentum and nonzero invariant mass.
- Hydrogen is treated as a calibrated shell-locking architecture on \(S^3 \times \mathbb{R}_s\), not as a complete theory of all atoms.
- RH/zeta material is retained as archived analogy, not the central evidence path.

## What this repo is not claiming

For explicit non-claims and falsifiability discipline, see [Claim Boundaries](docs/claim-boundaries.md).

## Start here

1. [docs/perfect-closure.md](docs/perfect-closure.md)
2. [docs/invariant-mass-from-closed-light.md](docs/invariant-mass-from-closed-light.md)
3. [docs/hydrogen-closure-bridge.md](docs/hydrogen-closure-bridge.md)
4. [docs/spectral-core-transition.md](docs/spectral-core-transition.md)
5. [docs/claim-boundaries.md](docs/claim-boundaries.md)

## Core Bridge Equations

### Minimal Mass-from-Closure Bridge

A free lightlike route has null invariant:

$$
p^\mu p_\mu = 0.
$$

A closed lightlike configuration has total four-momentum:

$$
P^\mu_{\mathrm{closed}} = \sum_i p_i^\mu.
$$

If closure cancels net spatial momentum,

$$
\sum_i \mathbf{p}_i = 0,
$$

while energy remains positive, then

$$
M^2 c^4 = \left(\sum_i E_i\right)^2 - c^2 \left|\sum_i \mathbf{p}_i\right|^2
$$

reduces to

$$
Mc^2 = \sum_i E_i.
$$

Thus mass appears as the invariant norm of closed lightlike phase.

### Hydrogen Shell Locking: First Calibrated Architecture

Hydrogen is the first calibrated shell model showing how closed phase can organize into spectral shells.

The hydrogen shell-locking architecture is defined on

$$
M = S^3 \times \mathbb{R}_s.
$$

With

$$
\hat N = \sqrt{-\Delta_{S^3} + 1},
$$

$$
\hat N Y_K = (K+1)Y_K,
$$

$$
-\Delta_{S^3}Y_K = K(K+2)Y_K,
$$

shell-locking is expressed as

$$
\hat N = \frac{s^2}{2}.
$$

Then

$$
n = K+1 = \frac{s^2}{2},
$$

$$
J(s) = \hbar \frac{s^2}{2},
$$

$$
E(s) = -\frac{4\mathrm{Ry}}{s^4},
$$

and at shell lock \(s^2 = 2n\),

$$
E_n = -\frac{\mathrm{Ry}}{n^2}.
$$

Degeneracy is

$$
\dim \mathcal{H}_K(S^3) = (K+1)^2 = n^2.
$$

## Program Structure

- **Ontology:** free light vs closed light
- **Geometry:** quaternionic phase closure and standing-wave return
- **Spectral bridge:** shell-number operator and shell locking on \(S^3 \times \mathbb{R}_s\)
- **Calibration:** hydrogen as first calibrated closure-shell example

## Repository Map

- `docs/` - thesis, geometry, bridge, and boundaries
- `papers/` - current light-to-mass paper sequence
- `archive/zeta-critical-line-program/` - previous RH/critical-line-centered material (historical/analogy)
- `future/` - forward-looking speculative notes
- `assets/figures/` - diagrams and generated visuals

## License

Written materials in this repository are released under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE) license.

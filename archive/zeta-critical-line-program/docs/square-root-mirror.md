# The Square-Root Mirror

## Why Re(s) = 1/2 Is Special

The Riemann zeta function, for Re(s) > 1, is given by the Euler product:

```
zeta(s) = product over primes p of  1 / (1 - p^{-s})
```

Each prime *p* contributes the term `p^{-s}`. For a complex number s = σ + it:

```
p^{-s}  =  p^{-σ} * e^{-it log p}
```

The magnitude is `p^{-σ}` and the phase is `e^{-it log p}`.

---

## The Functional Equation and Conjugate Symmetry

The Riemann zeta function satisfies a functional equation relating ζ(s) to ζ(1-s):

```
xi(s) = xi(1-s)
```

where `xi(s)` is the completed zeta function. This symmetry pairs each complex value s with the reflected value 1 - s̄ across the critical line.

This means the prime contributions at s and at its functional-equation partner `1 - s̄` are structurally linked. The prime *p* contributes:

```
p^{-s}         at s
p^{-(1-s*)}    at the functional-equation partner
```

where `s*` denotes complex conjugate.

---

## On the Critical Line: Equal Magnitude

On the critical line Re(s) = 1/2, write s = 1/2 + it. The two conjugate routes are:

```
p^{-(1/2 + it)}  =  (1/sqrt(p)) * e^{-it log p}

p^{-(1/2 - it)}  =  (1/sqrt(p)) * e^{+it log p}
```

**Both routes carry the same magnitude: `1/sqrt(p)`.**

The phases are equal in magnitude and opposite in sign: one winds clockwise around the unit circle, the other counterclockwise, both at the same angular speed `t log p`.

This is the *square-root mirror*: on the critical line, every prime is split into two equal-magnitude, opposite-phase routes. The factor `1/sqrt(p)` is exactly the square root of the prime — hence the name.

---

## Off the Critical Line: Broken Symmetry

For σ ≠ 1/2, the two conjugate routes have different magnitudes:

```
p^{-(σ + it)}      =  p^{-σ} * e^{-it log p}       (magnitude p^{-σ})

p^{-((1-σ) + it)}  =  p^{-(1-σ)} * e^{-it log p}   (magnitude p^{-(1-σ)})
```

When σ < 1/2: `p^{-σ} > p^{-1/2} > p^{-(1-σ)}`  — the first route dominates.

When σ > 1/2: `p^{-σ} < p^{-1/2} < p^{-(1-σ)}`  — the second route dominates.

In either case, the balance is broken. One route carries more weight than the other. The precondition for Perfect Closure — equal-magnitude conjugate routes — is not satisfied.

---

## Equal Magnitude vs. Actual Cancellation

**Important distinction:** Equal magnitude of the conjugate routes is a *necessary structural condition* for the possibility of Perfect Closure, but it is not *sufficient* to guarantee a zero.

For a zero to occur at s = 1/2 + it, the full prime-generated phase structure — the product over all primes, analytically continued — must combine to give exactly zero. This is a global condition that depends on the detailed phase relationships among all primes simultaneously.

The equal-magnitude condition ensures that the *possibility* of cancellation exists: neither route dominates the other. Whether actual cancellation occurs at a specific value of t is determined by the global analytic structure, not by the local magnitude condition alone.

This is why the critical line is where zeros *can* occur (structurally), and the Riemann Hypothesis asserts that they *do* all occur there — but proving that assertion requires establishing the global cancellation, which is the hard part.

---

## Summary

| Location | Magnitudes | Balance | Closure possibility |
|---|---|---|---|
| Re(s) = 1/2 (critical line) | Both = 1/sqrt(p) | Equal | Perfect Closure possible |
| Re(s) > 1/2 | p^{-σ} < p^{-(1-σ)} | Unequal | Closure not possible |
| Re(s) < 1/2 | p^{-σ} > p^{-(1-σ)} | Unequal | Closure not possible |

The critical line is the unique locus where every prime's conjugate routes are balanced. This is why it is the *square-root mirror*: the place where primes are perfectly halved into equal-magnitude, opposite-phase contributions.

---

*Back to [Home](index.md) | See also: [Perfect Closure](perfect-closure.md) | [Cautions](cautions.md)*

# Lisp Cheney Two-Space Copying GC

## Domain
`memory`

## Overview
Technical documentation and theoretical architecture of **Lisp Cheney Two-Space Copying GC**.

### Theoretical Complexity
- **Time Complexity**: $\mathcal{O}(1)$ amortized state transitions
- **Space Complexity**: $\mathcal{O}(N)$ bounded by configured allocation capacity

### System Invariants
1. Monotonicity of operation counters across all state mutations.
2. Capacity bounding guarantees preventing heap unbounded expansion.
3. Clean state isolation ensuring idempotent resets.

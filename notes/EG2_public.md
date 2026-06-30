# EG2 Public Note (Capture and Restart)

Mature wording: `transport / local-to-global transfer`.

In-paper anchor: `paper/LOCAL_GLOBAL_LANGLANDS_COMPATIBILITY_PREPRINT.md` (`LGC_G2`).

## Goal
Expand the compressed capture/restart language into the local-to-global transport gate for `proving persistence of admissible compatibility correspondences and local-global matching packages through a multi-lane Langlands compatibility super-architecture`.

## Objects

- transport carrier: the admissible evolution, deformation, or routed lattice declared in the preprint.
- capture floor: `sigma_localglobal`.
- restart law: the normalization/re-entry rule that keeps corrective steps inside the admissible class.
- carried losses: defect, restart, and normalization losses that must remain explicit.

## Closure Criterion

`LGC_G2` closes when `sigma_localglobal` survives admissible losses and restart corrections: local-global compatibility defect stays above capture floor across admissible transfer losses.
This is the transport contribution to `M_LGC`.

## Lemma Chain and Proof Payload

### Lemma EG2.1 (transport accounting)
Every transport step used by the lane is charged to the declared defect ledger instead of being absorbed into prose.

Payload: verify that the capture constant `sigma_localglobal` is present in the constants registry and extraction inputs.

### Lemma EG2.2 (restart preservation)
Restart or normalization preserves the declared admissible class and does not create an untracked remainder.

Payload: inspect the repro script and guard output for the gate tied to `sigma_localglobal`.

### Theorem EG2.3 (capture gate closure)
If transport accounting and restart preservation hold, then `LGC_G2` carries local control forward without breaking admissibility.

## Current Instantiation

- gate: `LGC_G2`
- artifact key: `sigma_localglobal`
- mature equivalent: `transport / local-to-global transfer`
- audit surface: `repro/run_repro.sh` and `repro/certificate_runtime.json`

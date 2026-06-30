# Geometric Galois Bridge

Mature wording: `Galois bridge / remainder discipline`.

In-paper anchor: `paper/LOCAL_GLOBAL_LANGLANDS_COMPATIBILITY_PREPRINT.md` (bridge and margin interface).

## Goal
Make the geometric/arithmetic bridge explicit without pretending that the projected admissible lane is the unrestricted problem-side universe.

## Objects

- visible sector: the declared admissible sector controlled by the Canonical Lane package.
- problem-side class: the larger geometric, etale, arithmetic, or Galois-side object family named by the preprint.
- remainder: the complement not closed by the visible sector alone.
- transfer lock: `reciprocity_transfer`.
- coherence remainder: `eps_coh`.

## Closure Criterion

The bridge is valid only when the admissible visible sector is projected, the remainder is named, and the endpoint-transfer lock `reciprocity_transfer` connects the canonical endpoint to the ordinary problem-side formulation.

## Lemma Chain and Proof Payload

### Lemma GG.1 (visible-sector projection)
The Canonical Lane claim is made on the declared admissible visible sector, not on an unstated unrestricted object.

Payload: check the preprint's admissible-class and explicit-remainder language.

### Lemma GG.2 (remainder discipline)
Any stronger external consequence must route through the named remainder rather than bypassing it.

Payload: verify that `eps_coh` and the defect/coherence ledgers remain visible in the runtime artifacts.

### Theorem GG.3 (geometric/arithmetic bridge)
If projection, remainder discipline, and endpoint transfer are all explicit, then the geometric/Galois bridge is a lawful translation layer rather than ornamental terminology.

## Current Instantiation

- transfer artifact key: `reciprocity_transfer`
- coherence artifact key: `eps_coh`
- margin: `M_LGC`
- mature equivalent: `Galois bridge / remainder discipline`
- audit surface: `notes/IDENTIFICATION_BRIDGE.md` and `repro/certificate_runtime.json`

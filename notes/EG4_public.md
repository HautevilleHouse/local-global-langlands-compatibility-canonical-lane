# EG4 Public Note (Rigidity and Endpoint Transfer)

Mature wording: `bad-limit exclusion / endpoint transfer`.

In-paper anchor: `paper/LOCAL_GLOBAL_LANGLANDS_COMPATIBILITY_PREPRINT.md` (`LGC_G4`, `LGC_G5`).

## Goal
Separate the rigidity job from the endpoint-transfer job for `proving persistence of admissible compatibility correspondences and local-global matching packages through a multi-lane Langlands compatibility super-architecture`.
The older wording `rigidity and endpoint-transfer` corresponds to bad-limit exclusion plus the bridge into the intended endpoint object.

## Objects

- bad-limit class: candidates extracted by the compactness gate but incompatible with closure.
- rigidity floor: `rho_rigidity`.
- endpoint-transfer lock: `reciprocity_transfer`.
- coherence interface: `eps_coh` remains available to the bridge and final margin.

## Closure Criterion

`LGC_G4` closes when `rho_rigidity` excludes bad endpoint alternatives: bad nonreciprocal countermodels are excluded.
`LGC_G5` closes when `reciprocity_transfer` transfers the surviving endpoint to the intended target class: rigid limits transfer to the predicted compatibility endpoint class.
Together they feed the strict margin `M_LGC`.

## Lemma Chain and Proof Payload

### Lemma EG4.1 (bad-limit exclusion)
Every extracted bad limit contradicts a declared rigidity constraint or leaves the admissible class.

Payload: verify `rho_rigidity` in the registry and certificate surfaces.

### Lemma EG4.2 (endpoint transfer)
The surviving rigid representative is locked to the standard problem-side endpoint by `reciprocity_transfer`.

Payload: read this note together with `notes/IDENTIFICATION_BRIDGE.md`.

### Theorem EG4.3 (rigidity/transfer gate closure)
If bad limits are excluded and the endpoint lock is active, then `LGC_G4` and `LGC_G5` deliver the boundary object needed by the final margin.

## Current Instantiation

- rigidity gate: `LGC_G4`
- rigidity artifact key: `rho_rigidity`
- transfer gate: `LGC_G5`
- transfer artifact key: `reciprocity_transfer`
- mature equivalent: `bad-limit exclusion / endpoint identification`
- audit surface: `notes/IDENTIFICATION_BRIDGE.md` and `repro/certificate_runtime.json`

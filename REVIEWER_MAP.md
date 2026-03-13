# Reviewer Map

## Claim Scope

- Canonical-lane claim: inside the `manifold_constrained` routed lattice, if the theorem chain in this repository holds and the guard certificate passes, the repository-level super-lane closure claim is satisfied.
- Standard target claim: Across the declared admissible reciprocity lattice, compatible Galois representations and automorphic packets match with the expected local-global compatibility, functional equation behavior, and endpoint identification package.

## Super-Lane Families

1. compatible-system and local parameter matching
2. local-global compatibility for admissible places
3. potential automorphy and descent transport
4. trace and `L`-function reciprocity control
5. global endpoint stitching across the declared compatibility lattice

## Theorem Dependency Chain

1. `EG1`: coercive projected response and active floor.
2. `EG2`: routed-family capture across the declared lattice.
3. `EG3`: compactness and no-collapse spacing for normalized towers.
4. `EG4`: rigidity and endpoint transfer.
5. Identification bridge: strict coherence on the determining class.
6. Scalar closure: `LGC_G1`, `LGC_G2`, `LGC_G3`, `LGC_G4`, `LGC_G5`, `LGC_G6`, `LGC_GM` all `PASS`.

## Falsification Conditions

- `repro/certificate_runtime.json` has any non-`PASS` gate.
- `lane.active_lane != "manifold_constrained"`.
- `all_pass != true`.
- Any manifest hash mismatch under `repro/repro_manifest.json`.
- A verified counterexample to any routed family theorem used by the super-repo.

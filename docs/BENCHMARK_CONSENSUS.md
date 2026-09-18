# AMI-SALT Benchmark Consensus v0.1

**Status:** EXPERIMENT / archaeology-informed design  
**Principle:** Trust instead of Authority

## Goal

Define a small, auditable benchmark and evidence layer for comparing AMI/model/router changes without allowing the tested system to grade itself.

The first version is intentionally conservative:

- compare a **baseline** against a **candidate** under identical conditions;
- keep transport, inference and validation failures separate;
- prefer deterministic checks where possible;
- use multiple independent judge models only as one evidence layer;
- preserve disagreement and `UNKNOWN` instead of forcing consensus;
- write benchmark outcomes as append-only SALT evidence with provenance;
- never let financial support buy SALT trust.

## Historical provenance

The following material is **HISTORICAL evidence**, not current truth:

1. `kajobert/sophia/docs/features/SALT_WHITEPAPER.md`
   - model-agnostic adversarial benchmark;
   - reproducible profiles;
   - granular 0-100 scoring;
   - deep-dive tests;
   - certificate/report hashes.

2. `kajobert/sophia/plugins/salt_auditor/scoring.py`
   - multi-variant aggregation;
   - consistency factor;
   - explicit dimensional scoring;
   - score breakdown suitable for machine-readable evidence.

3. `kajobert/sophia/docs/research/conversation-opus.md`
   - historical proposal for **multi-model consensus** using different model families;
   - higher consensus threshold for deep changes;
   - human approval for deep/core changes.

4. `kajobert/sophia/docs/research/Analýza architektonických základů AI SOPHIA.txt`
   - warning about correlated model bias / collusion;
   - **weighted consensus** based on diversity and confidence calibration;
   - independent verifier outside the voting loop;
   - judge-based topology.

5. Google Drive: `THE SALT MANIFESTO`
   - model-agnostic SALT auditing;
   - adversarial testing;
   - trust as continuously verified rather than assumed;
   - peer auditing between AI systems;
   - historical blockchain/anchoring concept.

These sources are retained as provenance only. Any reused mechanism must be validated against CURRENT AMI architecture.

## Core benchmark object

Each run records:

- `benchmark_id`
- `benchmark_version`
- `case_id`
- `task_type`
- `baseline_config_hash`
- `candidate_config_hash`
- `subject_agent_id`
- `subject_model`
- `router_role`
- `router_policy_version`
- `input_artifact_hash`
- `transport_result`
- `inference_result`
- `validation_result`
- `deterministic_checks`
- `judge_panel_id`
- `judge_results`
- `consensus_result`
- `disagreement_reason`
- `human_review_state`
- `latency_ms`
- `token_usage`
- `cost_if_known`
- `created_at`

A transport failure must never be scored as a model-quality failure.

## Judge panel

A judge panel SHOULD contain models from distinct model/provider families when available, for example:

- OpenAI
- Gemini
- Grok
- Mistral
- another independently trained/open-weights family

The tested model MUST NOT be the sole judge of its own output.

### Judge output

Each judge returns only a bounded structured record:

- rubric version
- criterion scores
- pass / fail / abstain
- confidence
- short evidence-linked rationale
- detected critical violation
- optional uncertainty note

No hidden reasoning is stored.

## Consensus is evidence, not truth

The system must not equate unanimous agreement with correctness.

The primary meta-metric is **calibrated agreement**, not raw vote count.

Track at minimum:

- pairwise agreement;
- variance across judges;
- abstention rate;
- agreement on deterministic/golden cases;
- judge family diversity;
- stability under prompt/order perturbation;
- calibration error where ground truth exists.

A 100% agreement result is stronger only when:

1. judges are sufficiently diverse;
2. deterministic checks do not contradict them;
3. hidden/golden controls pass;
4. the same conclusion is stable across perturbations.

If these conditions are not met, consensus remains lower-confidence evidence.

## Minimal v0.1 aggregation

For each criterion:

1. deterministic verifier, if available;
2. independent judge panel;
3. disagreement classification;
4. optional bounded human review.

Suggested state machine:

- `PASS_VERIFIED`
- `PASS_CONSENSUS`
- `DISAGREEMENT`
- `ABSTAIN`
- `FAIL_VERIFIED`
- `UNKNOWN`

No forced numeric score is required for v0.1.

If a numeric score is emitted for compatibility with historical SALT, it MUST retain the full breakdown and uncertainty metadata.

## Anti-gaming rules

- subject cannot award SALT to itself;
- judge identity/model/provider are recorded;
- duplicate evidence cannot multiply credit;
- hidden/golden benchmark cases are versioned and access-controlled;
- benchmark definitions are frozen for a run;
- baseline and candidate receive identical inputs;
- judge outputs are blinded to which side is baseline/candidate where practical;
- critical deterministic failures override favorable judge consensus;
- disagreement is preserved, not averaged away;
- historical imported evidence cannot count as CURRENT-earned SALT.

## SALT evidence event

A benchmark result may produce a SALT evidence event:

`actor -> contribution/change -> benchmark_run -> verification -> outcome -> context -> time -> event_hash`

Recommended fields:

- `salt_evidence_id`
- `subject_type`
- `subject_id`
- `evidence_type`
- `benchmark_run_id`
- `benchmark_version`
- `provenance_refs`
- `verification_methods`
- `consensus_state`
- `confidence`
- `policy_version`
- `earned_at`
- `event_hash`

The ledger should be append-only and deterministically replayable.

## Relationship to self-improvement

Self-improvement is not prohibited by design.

The safety boundary is:

`proposal -> benchmark -> independent verification -> SALT evidence -> approval policy -> apply -> post-change benchmark -> rollback if regression`

This supports prompt/router/model/fine-tuning experiments while keeping provenance and reversibility.

Deep or identity-affecting changes require stricter evidence and explicit human approval until a later validated policy exists.

## v0.1 acceptance criteria

1. Same benchmark input produces reproducible evidence artifacts.
2. Transport/inference/validation failures are separated.
3. At least one deterministic/golden case is included.
4. At least three judge results can be recorded without forcing consensus.
5. `ABSTAIN`, `DISAGREEMENT` and `UNKNOWN` are first-class states.
6. Duplicate benchmark evidence does not double-accrue SALT.
7. Historical SALT evidence remains marked HISTORICAL.
8. Candidate model/router changes cannot be promoted solely by self-rating.
9. Every SALT accrual points to a benchmark/evidence hash and policy version.
10. Replay of the same event stream yields the same ledger state.

## Next experiments

- Luna baseline vs candidate planner/critic routing;
- adversarial self-modification boundary test;
- multi-model judge agreement on a small golden set;
- judge calibration using deliberately easy, ambiguous and contradictory cases;
- evaluate whether diversity-weighted consensus is more reliable than simple majority.


# Funding Provenance

**Status:** DESIGN / EXPERIMENT

> **Trust instead of Authority.**

AMI-SALT should make financial support traceable through time from contribution to infrastructure consumption and, where evidence exists, to concrete AMI outcomes.

The goal is not merely to publish how much money was received. The goal is to make it possible to answer:

> What did this support actually enable?

## Core trace

A funding trace links:

`support -> funding lot -> resource allocation -> spend/credit consumption -> AMI task/run -> output -> verified outcome`

Examples of outputs may include:

- a GitHub pull request;
- a benchmark run;
- an archaeology extraction;
- inference used for a bounded AMI task;
- database/storage/compute capacity used by a documented AMI service.

## Funding lots

Each verified support event creates a funding lot with a stable identifier, amount, currency, timestamp and supporter attribution policy.

A lot can be public, pseudonymous or anonymous. Private payment details stay outside the public ledger.

When pooled funds are consumed, AMI should record an accounting allocation from one or more funding lots to the spend. The bootstrap implementation uses deterministic FIFO allocation because it is simple, reproducible and auditable. Future policy versions may support explicit earmarking or other allocation rules.

Because money in a pooled account is fungible, this is an **auditable accounting provenance model**, not a claim that a particular physical currency unit can be followed through a bank account.

## Resource spend

A spend record should identify, where available:

- provider/resource category, such as inference, compute, storage or networking;
- amount and currency;
- provider invoice/credit reference hash without exposing secrets;
- allocation policy version;
- funding-lot allocations;
- timestamp and event hash.

If support is converted into prepaid provider credit, the trace may include a separate credit-purchase event and later credit-consumption events.

## Outcome linkage

A spend can reference one or more AMI execution records, and those executions can reference public outcomes.

For GitHub this may produce machine-readable provenance such as:

`funding_trace_ids: [trace-...]`

A PR may then render a human-readable section such as:

**Financial support:** Alice, Bob + anonymous supporters

or

**Supported by:** Alice (62%), Bob (38%)

Only verified allocations may be displayed. Financial attribution is not technical authorship and is not SALT trust authority.

The wording **Trusted by** should be reserved for an actual SALT trust/evidence assertion. A donor must not become trusted merely by paying.

## Partial and shared funding

One support lot may fund many runs. One run may consume multiple lots. One PR may be the result of several runs and other non-financial contributions.

Therefore attribution should preserve amounts/shares instead of pretending there is always one sponsor per result.

## Public supporter view

With supporter opt-in, AMI may expose:

- cumulative support;
- remaining unconsumed funded amount;
- amount already consumed;
- infrastructure categories funded;
- linked public runs/PRs/outcomes;
- estimated runtime enabled under the cost model active at that time.

This creates a time-travelable history: a supporter can inspect what was happening when their funding lot was consumed and which outcomes were linked to it.

## Integrity requirements

- immutable event identifiers;
- canonical serialization and hashes;
- no double-consumption of a funding lot;
- allocation totals must exactly equal the spend they fund;
- policy version on every allocation;
- duplicate/replay protection;
- no fabricated supporter attribution;
- public recognition is opt-in;
- anonymous support remains possible;
- financial support never directly purchases SALT trust, protocol authority or merge rights.

## Next experiment

The first implementation should prove deterministic funding-lot allocation and reproducible trace generation before connecting a real payment provider, OpenRouter billing or automated PR annotations.

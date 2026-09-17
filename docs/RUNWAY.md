# AMI-SALT Support and Runway

**Status:** DESIGN

> **Trust instead of Authority.**

AMI-SALT separates two different things that must never be conflated:

1. **SALT trust/contribution** — earned from verifiable contribution, evidence, successful cooperation and outcomes.
2. **Financial support** — money voluntarily contributed to sustain AMI infrastructure and development.

Financial support does **not** buy SALT trust and does not grant authority over AMI.

## Support evidence

A support event records that resources were contributed to AMI. It may contain:

- opaque supporter ID or public display name;
- amount and currency;
- timestamp;
- payment/provider reference hash or other non-secret receipt reference;
- destination purpose, such as inference, compute, storage, networking or research;
- whether public recognition is explicitly opted in.

Raw payment credentials, addresses and private billing records stay outside the public repository.

## Public supporter leaderboard

AMI may publish an opt-in leaderboard of financial supporters, ranked by verified cumulative support.

This leaderboard is **support recognition**, not a trust ranking. It must never be used as the SALT contribution score or as a source of protocol authority.

Possible public fields:

- display name / pseudonym;
- verified cumulative support;
- funded infrastructure-equivalent estimate;
- first/last support timestamp;
- supporter-selected message or project area, subject to moderation.

Anonymous support remains valid and is counted in aggregate runway without public attribution.

## Infrastructure runway

Support can be converted into a transparent estimate of future operating capacity.

Instead of claiming that one currency unit permanently equals one hour, AMI publishes a versioned cost model. Example cost categories:

- model inference / API tokens;
- CPU/GPU compute;
- database/storage;
- network/egress;
- monitoring/backups;
- domain/service subscriptions;
- bounded development/research execution where appropriate.

The system should expose at least:

- current verified reserve;
- committed/prepaid infrastructure credit where known;
- trailing average burn rate;
- projected runway in hours/days;
- assumptions and cost-model version;
- uncertainty range.

Conceptually:

`projected_runway_hours = usable_reserve / estimated_hourly_burn`

The estimate is informational and changes whenever prices, usage or policy change.

## Contribution-backed growth

A useful supporter-facing metric is not merely money received but **what the support enabled**. Support evidence can later link to outcomes such as:

`support -> funded resource -> AMI task/run -> verified output -> outcome`

This makes the system auditable without pretending that money itself creates trust.

## Financial independence target

AMI can publish a sustainability target such as:

- 24 hours prepaid;
- 7 days prepaid;
- 30 days prepaid;
- 90 days operational reserve.

These are runway milestones, not SALT balances.

## Safety and policy boundaries

- no automatic exchange rate from money to SALT trust;
- no promise of financial return;
- no redemption promise for SALT;
- no hidden donor authority;
- public recognition is opt-in;
- all cost estimates state assumptions and timestamp;
- financial mechanisms that become transferable or investment-like require separate legal and security review.

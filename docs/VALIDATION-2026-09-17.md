# Local validation and CI correction

Status: EXPERIMENT; not a production ledger or hosted-CI certification.

## Verified source snapshot

Base: `89852da9216bda151a7e882653e1c11e49b18ade`.
The five existing Python source/test files were read through the GitHub connector, materialized in an isolated local environment and verified against their Git blob SHA-1 values before execution. No server credentials, payment data or provider calls were used.

## Reproduced failure

The original `.github/workflows/ci.yml` omitted the YAML literal block marker after `run:` for a Python heredoc. PyYAML reproduced `mapping values are not allowed here` on line 30 at `JSON: PASS`. The corrected step uses `run: |`.

A zero-job workflow is not, by itself, proof of a GitHub runner outage. This repository had a concrete workflow defect. The independent AMI runner probe still requires its own diagnosis and check annotations.

## Executed tests

Environment: CPython 3.13.5, PyYAML 6.0.3, Linux/Bash.

- Original seven unit tests: PASS.
- Expanded regression suite against original code/workflow: FAIL (14 failed subtests, 14 errors).
- Expanded suite after these changes: 19 test methods PASS.
- Python compileall: PASS.
- Workflow YAML parsing and `bash -n` syntax checks: PASS.

Reproduce on Linux:

```sh
python -m pip install -r requirements-ci.txt
python -m compileall -q salt tests
python -m unittest discover -s tests -v
```

The hosted workflow targets Python 3.12; the local result above must not be described as a completed GitHub Actions run. The workflow's JSON step checks syntax, not the entire semantic JSON Schema contract.

## Correctness changes

Reject boolean, float, non-finite and nonnumeric monetary input; require nonblank identifiers and supporter attribution; use exact integer division for whole-hour estimates. Tests cover conservation, deterministic allocation and input immutability.

## Remaining boundaries

FIFO allocation is a pure function over a caller-ordered single-currency snapshot. It is not a transactional database, does not deduplicate spend IDs across calls, and does not enforce concurrent no-double-spending. Those require a separately reviewed persistent ledger. No real payments, rewards, provider top-ups, automatic publication, merge or deployment are enabled by this change.

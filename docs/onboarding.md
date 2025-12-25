# Zero-Install Onboarding (for non-developers)

- Clone the repo and open the folder in VS Code.
- When prompted, choose **Allow Automatic Tasks in Folder**.
- The "ALN: First-time Setup" task will run automatically and validate ALN files; no commands required beyond having Python 3 installed.
- The repo uses the public DID in `did-config.json` for CI/ALN validation identity; no private keys are stored in the repository.

ALN Safety Rules:
- **Headers required**: All new `policy`, `plan`, and `datashard` files MUST start with a header like `policy NAME v1`.
- **Schema checks**: Datashards must declare a destination path (e.g., `destination-path` or `destination_path`).
- **Handler termination**: Files with `handler` declarations must include a termination marker (e.g., `end_state`, `finalization`, or `shutdown_step`).

Failing these checks will intentionally fail CI; this is a safety feature, not a bug.

Current Known ALN Safety Failures:
- `raptor-mini/telemetry/NeuroGATT_Defender.aln` — SCHEMA:handler_missing_termination
- `systems/neuromind/Mindsoft_VSG_Core.aln` — SCHEMA:handler_missing_termination
- `vitalnet/chilesupremegalea/ChileSupremeGalea_NeuroRights.aln` — SCHEMA:handler_missing_termination

Note: CI will show failures until these handlers include explicit safe termination steps. The repository owner prefers manual or reviewed fixes for these high-impact modules; auto-fix is disabled by design. Use the Copilot prompts and the per-job JSON reports to propose changes in separate, auditable PRs.

# Copilot Playbook — Common Maintenance Prompts

Use these copy-paste prompts in Copilot Chat (or Raptor-mini) to perform common tasks.

1. "Scan all `*.aln` files under the repo and report any naming or schema inconsistencies."
2. "Add an ALN module named `IncidentArchiver` under `raptor-mini/telemetry/` that includes a datashard and a handler for anchoring incidents to Hyperledger. Follow existing module patterns."
3. "Harden `scripts/aln_lint.py` to also detect unclosed `handler` blocks and missing `datashard` destination paths; propose code changes."
4. "Generate an example policy `policy Example.SafeMode v1` with `goals`, `step` definitions, and a `guarantees` section, saving to `raptor-mini/policy/`."
5. "Create a new integration test in `tests/integration/` that simulates a hypnotic audio sample and asserts the NeuroGATT_Defender would block it (mock the detector)."

Each prompt references specific files and folders in this repo so non-developers can paste them directly into Copilot Chat or Raptor-mini.

ALN Safety Rules (copy to documentation or use in chat):
- All new `policy`/`plan`/`datashard` files must have a proper header like `policy NAME v1`.
- Missing headers, missing datashard `destination-path`, or missing handler termination markers will fail CI intentionally.

Repair prompts (copy-paste into Copilot chat):
- "Scan all `*.aln` files and add correct policy/plan/datashard headers where missing, following existing patterns." 
- "For any datashard missing a destination/path field, propose a safe default (e.g., `destination-path: /registry/<module>`) and update the file." 
- "For any handler module without a shutdown/end_state, add a conservative finalization step (e.g., `finalization: 'safe_shutdown'`)."

Daily Safety Review Loop (copy-paste prompts)
- "List any new ALN lint failures in the latest CI run by reading `aln_lint_report_*.json` artifacts and summarize them." 
- "Draft an ALN safety issue using `.github/ISSUE_TEMPLATE/aln-safety-failure.md` with failures from `aln_lint_report_vitalnet.json`."
- "Show me the suggested termination patterns from `docs/aln-safety-suggestions.md` for `NeuroGATT_Defender.aln` and explain how they address `SCHEMA:handler_missing_termination`."
- "Create a draft PR body using `.github/PULL_REQUEST_TEMPLATE/aln-safety-fix.md` proposing a conservative finalization for `systems/neuromind/Mindsoft_VSG_Core.aln` (do not apply changes)."

These prompts are designed so a non-expert can run a 5–10 minute daily safety review by pasting them into Raptor-mini or Copilot Chat.

Current Known ALN Safety Failures (for triage):
- `raptor-mini/telemetry/NeuroGATT_Defender.aln` — SCHEMA:handler_missing_termination
- `systems/neuromind/Mindsoft_VSG_Core.aln` — SCHEMA:handler_missing_termination
- `vitalnet/chilesupremegalea/ChileSupremeGalea_NeuroRights.aln` — SCHEMA:handler_missing_termination

Guidance: CI will deliberately fail these modules until a reviewed, manual fix introduces safe termination steps. Use the JSON reports uploaded as CI artifacts and the repair prompts above to prepare PRs for human review.
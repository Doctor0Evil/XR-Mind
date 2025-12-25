# ALN Issue Creation Guidance (for maintainers)

Purpose: simple, copy-paste instructions to raise ALN safety issues from CI reports.

Steps to raise an ALN safety issue

1. Download the ALN lint artifact from the failed CI run (artifact name `aln-lint-<folder>`).
2. Extract and open `aln_lint_report_<folder>.json`.
3. For each failing file, copy the path and errors and paste them into a new issue using `.github/ISSUE_TEMPLATE/aln-safety-failure.md`.
   - Check the relevant area: [ ] raptor-mini / [ ] systems / [ ] vitalnet
   - Paste the failing files and error codes in the template fields.
4. Add a short reason for manual review (e.g., "high-impact runtime handler needs legal review before safe shutdown can be added").
5. Assign the issue to the appropriate owner and include the JSON report as an artifact link.

---

Example issue bodies (ready-to-paste)

Example 1 — NeuroGATT_Defender

- Area: raptor-mini
- Failing files:
  - `raptor-mini/telemetry/NeuroGATT_Defender.aln`
- Error codes:
  - `SCHEMA:handler_missing_termination`
- Reason for manual review:
  - Handler logic performs runtime detection; requires human/legal review to add a conservative finalization that avoids exposing raw neural data.

Example 2 — Mindsoft VSG Core

- Area: systems
- Failing files:
  - `systems/neuromind/Mindsoft_VSG_Core.aln`
- Error codes:
  - `SCHEMA:handler_missing_termination`
- Reason for manual review:
  - Core audio handlers must have a reversible end-state to prevent endless muting; legal review recommended.

Example 3 — Chile Supreme Galea

- Area: vitalnet
- Failing files:
  - `vitalnet/chilesupremegalea/ChileSupremeGalea_NeuroRights.aln`
- Error codes:
  - `SCHEMA:handler_missing_termination`
- Reason for manual review:
  - High-impact national compliance module; any termination/quarantine step must be reviewed for privacy and legal safeguards.

Notes:
- These examples are templates; include the CI artifact link and attach the JSON report to the issue for triage.
- Keep the issue concise and focused on safety; avoid speculative implementation details in the issue description.
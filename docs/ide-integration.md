# IDE Integration — Consuming ALN Safety Intel

## Consuming ALN Safety Intel

Tools and IDEs can integrate with the ALN safety workflows by following these simple steps:

1. Read `aln-knowledge-manifest.json` to discover safety artifacts (report globs, suggestion docs, templates).
2. Pull the latest `aln_lint_report_*.json` artifacts (these are uploaded by CI per-folder) and parse the `files` array to find failing files and error codes.
3. Read `docs/aln-safety-suggestions.md` for conservative, review-only fixes and human/legal guidance.
4. Treat these items as read-only inputs: use them to triage, propose PRs, or train evaluation tools — do not auto-apply fixes without a human-reviewed PR.

### Minimum integration for IDEs/AI agents
- **Read the manifest.** Discover safety artifacts via `aln-knowledge-manifest.json`.
- **Ingest ALN files + safety_workflows.** Parse `aln_lint_report_*.json` and `docs/aln-safety-suggestions.md`.
- **Surface failures and suggestions.** Present failing files and suggested fixes to users (read-only) without auto-fixing.
- **Offer assisted fixes on demand.** If a user asks to fix something, open the matching issue/PR templates for review rather than applying changes automatically.

This keeps ALN safety high-signal and auditable across tools and automation.

---
name: ALN Safety Failure
about: Report ALN lint failures and request manual triage.
labels: ["aln-safety","triage"]
assignees: []
---

## ALN Safety Failure - Quick Triage

- [ ] raptor-mini
- [ ] systems
- [ ] vitalnet

**Failing files**
```
(Please paste paths from `aln_lint_report_*.json`)
```

**Error codes**
```
(e.g., SCHEMA:handler_missing_termination)
```

**Reason for manual review**

(Short explanation of why this change needs human/legal review)

**Suggested next steps**
- Create a PR referencing this issue that proposes a conservative, auditable fix.
- Include a re-run of `py scripts/aln_lint.py` in the PR checks.

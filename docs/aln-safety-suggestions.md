# ALN Safety Suggestions (conservative, review-only)

This document lists conservative, minimal suggestions to address current ALN safety failures. **Do not apply these automatically**; each suggestion *needs human and legal review* before implementation.

---

## 1) raptor-mini/telemetry/NeuroGATT_Defender.aln

Issue: `SCHEMA:handler_missing_termination` — file defines `handler` sections but lacks an explicit termination or finalization marker.

Suggestion (conservative): Add a final `handler` that ensures the detector ends safely and records an incident without taking irreversible actions.

Example snippet to add (ALN style):

handler finalization_safe_shutdown()
{
  # Conservative finalization: disable active detection, persist incident summary, and notify human operator
  finalization: "safe_shutdown";
  action: {
    disable_active_detection();
    persist_incident_summary();
    notify_human_review("NeuroGATT detection finalized; review required.");
  }
}

Note: Replace helper calls with existing project semantics; this snippet is a template and must be reviewed by maintainers and legal before merging.

---

## 2) systems/neuromind/Mindsoft_VSG_Core.aln

Issue: `SCHEMA:handler_missing_termination` — contains `handler CoreCycle` which loops over audio frames; add a deterministic termination to avoid persistent blocking or muting without audit.

Suggestion (conservative): Ensure the handler logs a reversible remediation and sets an `end_state` marker to avoid endless hard-block when a condition is met.

Example snippet to add:

handler core_finalization()
{
  end_state: "muted_to_safe_mode";
  action: {
    record_vsg_event("safe_mode_engaged");
    set_voice_channel_state("attenuate");
    require_human_acknowledgement();
  }
}

Note: Human review required to confirm language and regulatory compliance before applying.

---

## 3) vitalnet/chilesupremegalea/ChileSupremeGalea_NeuroRights.aln

Issue: `SCHEMA:handler_missing_termination` — `galea_runtime_guard` handler performs risk escalation. Add an explicit `shutdown_step` or `finalization` clause that quarantines the stream and stashes a redacted evidence package.

Suggestion (conservative): Add a short finalization handler that quarantines stream and anchors a minimal evidence package to the ledger, without exposing raw neural data.

Example snippet to add:

handler quarantine_and_anchor()
{
  shutdown_step: "quarantine_and_anchor";
  action: {
    quarantine_stream();
    anchor_redacted_evidence();
    notify_user_and_legal("BCI stream quarantined for review");
  }
}

Note: The evidence anchoring step must avoid including raw neurodata; ensure redaction steps conform to policy.

---

## General notes
- Each suggestion is intentionally conservative: prefer quarantine, notification, and evidence anchoring over auto-remediation.
- Document any change in the associated PR and cross-reference the ALN lint JSON report to show the issue resolved.
- All changes should be reversible and auditable; do not introduce permanent destructive actions without legal signoff.

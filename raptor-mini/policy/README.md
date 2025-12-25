# Policy: Hands-Free Neural Defense

This folder contains user-facing ALN policy specifications for Hands-Free Neural Defense modes.

Files:
- `RaptorMini_NeuralDefense_HandsFree_Mode.aln` — non-technical policy describing goals, behaviors, and guarantees for always-on protection.

Notes:
- Policies are written in ALN for clarity and to be consumable by the ALN-first toolchain.
- Technical enforcement modules (eBPF, agent hooks) should reference policy IDs when implementing blocks or filters.

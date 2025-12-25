#!/usr/bin/env python3
"""First-time setup: runs quick checks for new contributors.
- Runs the ALN linter
- Runs a fast git sanity check if .git exists
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(__file__)) if os.path.basename(__file__) != 'first_time_setup.py' else os.getcwd()

print('Welcome — running quick first-time setup checks (ALN linter, repo sanity)')
# Try several python launchers to run the linter deterministically
cmds = [['py', '-3', 'scripts/aln_lint.py'], ['python', 'scripts/aln_lint.py'], ['python3', 'scripts/aln_lint.py']]

ok = False
for c in cmds:
    try:
        r = subprocess.run(c, cwd=ROOT)
        if r.returncode == 0:
            ok = True
            break
    except FileNotFoundError:
        continue

if not ok:
    print('\nWARNING: ALN linter could not be executed automatically. Please ensure Python 3 is available and run:')
    print('    python scripts/aln_lint.py')

# Optional fast sanity check
if os.path.isdir(os.path.join(ROOT, '.git')):
    try:
        print('\nRepo status:')
        subprocess.run(['git', 'status', '-sb'], cwd=ROOT)
    except Exception:
        print('Could not run git status; git may not be available on PATH.')

print('\nFirst-time setup complete.')

#!/usr/bin/env python3
"""Minimal ALN linter
Checks: file presence, non-empty, first non-comment token, header/version, section sanity,
brace parity, double-quote parity, and schema-level checks for datashards and handlers.
"""
import os
import sys
import fnmatch
import argparse
import re

ROOT = os.path.dirname(os.path.dirname(__file__)) if os.path.basename(__file__) != 'aln_lint.py' else os.getcwd()
ALLOWED_STARTS = ("policy", "plan", "module", "datashard", "meta")


def find_aln_files(root, prefix=None):
    for dirpath, _, filenames in os.walk(root):
        for f in filenames:
            if f.endswith('.aln'):
                full = os.path.join(dirpath, f)
                if prefix:
                    # Normalize separators and ensure it's under the prefix
                    norm_prefix = os.path.normpath(prefix)
                    if not os.path.commonpath([os.path.abspath(full), os.path.abspath(norm_prefix)]) == os.path.abspath(norm_prefix):
                        continue
                yield full


def first_non_comment_line(lines):
    for line in lines:
        s = line.strip()
        if not s:
            continue
        if s.startswith('#') or s.startswith('//'):
            continue
        return s
    return ''


def check_file(path):
    res = {'path': path, 'ok': True, 'errors': []}
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            text = fh.read()
    except Exception as e:
        res['ok'] = False
        res['errors'].append(f'cannot_read: {e}')
        return res

    if not text.strip():
        res['ok'] = False
        res['errors'].append('empty_file')
        return res

    lines = text.splitlines()
    first = first_non_comment_line(lines)
    if not first:
        res['ok'] = False
        res['errors'].append('no_non_comment_lines')
        return res

    first_tok = first.split()[0]
    # Accept tokens that are allowed or namespace-style meta names that end with '.meta'
    if first_tok not in ALLOWED_STARTS and not first_tok.endswith('.meta'):
        res['ok'] = False
        res['errors'].append(f'first_token_invalid: {first_tok}')

    # Stricter header/version enforcement for certain types
    if first_tok.lower() in ('policy', 'plan', 'datashard'):
        # Expect: <token> <NAME> v<major> (examples: policy Foo v1_0, plan Bar v2)
        header_re = re.compile(r'^(policy|plan|datashard)\s+[A-Za-z0-9_.\-]+\s+[vV]\d+(_\d+)*')
        if not header_re.match(first):
            res['ok'] = False
            res['errors'].append(f'header_format_invalid: "{first.strip()}"')

    # Basic semantic section checks per type
    type_checks = {
        'policy': ['goals', 'step', 'policies', 'guarantees', 'behaviors'],
        'plan': ['step', 'actions', 'priority_order', 'goal-constraints'],
        'datashard': ['schema', 'fields', 'datashardheader', 'header']
    }
    lower_text = text.lower()
    if first_tok.lower() in type_checks:
        required_tokens = type_checks[first_tok.lower()]
        if not any(tok in lower_text for tok in required_tokens):
            res['ok'] = False
            res['errors'].append(f'missing_required_section_for_{first_tok.lower()}')

    # SCHEMA checks: datashard destination/path
    if first_tok.lower() == 'datashard':
        if not any(k in lower_text for k in ('destination-path', 'destination_path', 'target_path')):
            res['ok'] = False
            res['errors'].append('SCHEMA:datashard_missing_destination')

    # SCHEMA checks: handler termination markers
    if re.search(r'\bhandler\b', lower_text):
        if not any(k in lower_text for k in ('end_state', 'finalization', 'shutdown_step')):
            res['ok'] = False
            res['errors'].append('SCHEMA:handler_missing_termination')

    # brace parity
    open_braces = text.count('{')
    close_braces = text.count('}')
    if open_braces != close_braces:
        res['ok'] = False
        res['errors'].append(f'brace_parity: {open_braces} != {close_braces}')

    # double-quote parity
    quote_count = text.count('"')
    if quote_count % 2 != 0:
        res['ok'] = False
        res['errors'].append('double_quote_parity')

    return res


def main():
    parser = argparse.ArgumentParser(description='ALN linter')
    parser.add_argument('--folder', help='Limit checks to a specific folder prefix', default=None)
    parser.add_argument('--report-json', help='Write a JSON report to this path', default=None)
    args = parser.parse_args()

    failures = []
    files = list(find_aln_files('.', prefix=args.folder))
    if not files:
        print('No .aln files found.')
        return 1

    total = 0
    passed = 0
    failed = 0

    print(f'Found {len(files)} .aln files, running checks...')
    for f in sorted(files):
        total += 1
        r = check_file(f)
        if r['ok']:
            print(f'OK  {f}')
            passed += 1
        else:
            print(f'FAIL {f} -> {r["errors"]}')
            failures.append(r)
            failed += 1

    print('\nALN Lint Summary:')
    print(f'  Total scanned: {total}')
    print(f'  Passed:        {passed}')
    print(f'  Failed:        {failed}')

    # If requested, write JSON report
    if args.report_json:
        try:
            import json
            report = {
                'files': [{'path': r['path'], 'errors': r['errors']} for r in failures],
                'summary': {'total': total, 'passed': passed, 'failed': failed}
            }
            with open(args.report_json, 'w', encoding='utf-8') as jf:
                json.dump(report, jf, indent=2)
            print(f"Wrote JSON report to {args.report_json}")
        except Exception as e:
            print(f"Could not write report JSON: {e}")

    if failures:
        print(f"{len(failures)} file(s) failed ALN lint checks")
        return 2

    print('All ALN files passed linter checks')
    return 0


if __name__ == '__main__':
    sys.exit(main())
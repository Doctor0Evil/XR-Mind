#!/usr/bin/env python3
"""Build ALN dataset from session logs (placeholder)"""
import json

def build(in_path: str, out_path: str):
    with open(in_path) as f:
        for line in f:
            # naive copy for now
            obj = json.loads(line)
            with open(out_path, "a") as o:
                o.write(json.dumps(obj) + "\n")

if __name__ == "__main__":
    build("../logs/raptor_sessions.jsonl", "../datasets/aln_neurodefense.jsonl")

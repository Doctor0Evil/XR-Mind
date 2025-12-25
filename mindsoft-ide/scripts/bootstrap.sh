#!/usr/bin/env bash
# bootstrap.sh - create the workspace layout from the layout spec
set -e

echo "Creating Mindsoft Neuro-Safety IDE skeleton..."
mkdir -p ide-core/frontend/src
mkdir -p ide-core/backend/cmd/ide-server
mkdir -p neurosafety-engine/core
mkdir -p kernel-guard-agent/agent
mkdir -p xr-bci-plugins/unity/Editor
mkdir -p mindpattern-registry
mkdir -p compliance-policies
mkdir -p incident-response/schema
mkdir -p smartcity-integration/nodes
mkdir -p docs
mkdir -p examples/safe-xr-game/unity-project
mkdir -p scripts
mkdir -p config

echo "Done."

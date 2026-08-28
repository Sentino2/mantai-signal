#!/usr/bin/env bash
# Trigger a digest run in the cloud immediately (used by /loop or manually).
# Requires: gh authed to a user with access to Sentino2/mantai-signal.
set -euo pipefail
REPO="${REPO:-Sentino2/mantai-signal}"
echo "Dispatching daily-digest on $REPO..."
gh workflow run daily-digest.yml -R "$REPO"
echo "Watching latest run..."
sleep 4
gh run watch -R "$REPO" --exit-status

#!/bin/bash
# Shim: the canonical deploy script lives in iCloud next to the source file
# (documented in the Learning Spanish CLAUDE.md). This forwards to it so the
# two copies can never diverge again.
exec bash "$HOME/Library/Mobile Documents/com~apple~CloudDocs/Personal/Learning Spanish/deploy.sh" "$@"

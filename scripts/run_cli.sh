#!/usr/bin/env bash
set -euo pipefail

python -m app.main --rfp sample_data/sample_rfp.txt --outdir out "$@"

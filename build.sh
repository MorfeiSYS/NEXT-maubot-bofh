#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

if ! command -v mbc >/dev/null 2>&1; then
    echo "mbc not found. Install dev dependencies:" >&2
    echo "  pip install -r requirements-dev.txt" >&2
    exit 1
fi

echo "Building maubot plugin..."
mbc build

mbp="$(ls -t *.mbp 2>/dev/null | head -n 1)"
if [[ -n "${mbp}" ]]; then
    echo "Created: $(pwd)/${mbp}"
fi

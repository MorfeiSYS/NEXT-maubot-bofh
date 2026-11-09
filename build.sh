#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

if ! command -v mbc >/dev/null 2>&1; then
    echo "mbc not found. Install dev dependencies:" >&2
    echo "  pip install -r requirements-dev.txt" >&2
    exit 1
fi

build_dir="$(pwd)/build"
mkdir -p "$build_dir"

if compgen -G "*.mbp" > /dev/null; then
    mv -f *.mbp "$build_dir/"
fi

echo "Building maubot plugin into build/..."
mbc build -o "$build_dir"

mbp="$(ls -t "$build_dir"/*.mbp 2>/dev/null | head -n 1)"
if [[ -n "${mbp}" ]]; then
    echo "Created: ${mbp}"
fi

#!/usr/bin/env bash
# Build the site locally and serve it, board tab included, so you can read
# through the whole thing before anything is pushed.
#
#   ./scripts/preview.sh                      # board passphrase: "local-preview"
#   BOARD_PASSPHRASE='...' ./scripts/preview.sh
#   PORT=9000 PUBLISH_POLICY=approved ./scripts/preview.sh
#
# The passphrase here is only for your local build. The real one lives in the
# repository secret BOARD_PASSPHRASE and is never stored in the repo.
set -euo pipefail
cd "$(dirname "$0")/.."

PORT="${PORT:-8000}"
export BOARD_PASSPHRASE="${BOARD_PASSPHRASE:-local-preview}"

if ! python3 -c "import markdown, yaml, cryptography" 2>/dev/null; then
  echo "Installing build dependencies..."
  python3 -m pip install -q -r scripts/requirements.txt
fi

rm -rf _site
python3 scripts/build_site.py --out _site

cat <<MSG

  Reading site   http://localhost:${PORT}/
  Board tab      http://localhost:${PORT}/board.html
  Passphrase     ${BOARD_PASSPHRASE}

  Ctrl-C to stop.

MSG
cd _site && exec python3 -m http.server "${PORT}"

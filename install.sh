#!/bin/sh
set -e

SKILL_NAME="py-clean-arch"
RAW_BASE="https://raw.githubusercontent.com/CJHwong/py-clean-architecture-examples/main"

case "${1:-claude}" in
  agents) DEST=~/.agents/skills/$SKILL_NAME ;;
  claude) DEST=~/.claude/skills/$SKILL_NAME ;;
  *)
    echo "Usage: bash install.sh [claude|agents]  (default: claude)"
    exit 1
    ;;
esac

mkdir -p "$DEST"
curl -sSL "$RAW_BASE/skills/$SKILL_NAME/SKILL.md" > "$DEST/SKILL.md"
echo "Installed $SKILL_NAME to $DEST"

#!/bin/sh
set -e

SKILL_NAME="py-clean-arch"
RAW_BASE="https://raw.githubusercontent.com/CJHwong/py-clean-architecture-examples/main"
SOURCE_URL="https://github.com/CJHwong/py-clean-architecture-examples/blob/main/install.sh"

usage() {
  echo "Usage: sh install.sh [-y] [claude|agents]  (default: claude)"
  echo "  -y, --yes  skip the risk prompt (for agents and CI)"
}

# A piped install runs whatever the server sends, with your permissions, so ask
# first. The answer comes from /dev/tty because stdin is the script itself.
confirm_install() {
  cat >&2 <<EOF
WARNING: this installer downloads code from the internet and runs it as you.
It can read, change, or delete anything your user account can.
The server can send different code each time, so read the script first:
  $SOURCE_URL
Pass -y to skip this question (for agents and CI).
EOF
  if ! (: </dev/tty) 2>/dev/null; then
    echo "install.sh: no terminal to ask on; re-run with -y to accept the risk" >&2
    exit 1
  fi
  printf 'Proceed? [Y/n] ' >&2
  read -r answer </dev/tty || answer=""
  case "$answer" in
    n|N|no|No|NO) echo "install.sh: aborted" >&2; exit 1 ;;
  esac
}

assume_yes=0
target=claude
for arg in "$@"; do
  case "$arg" in
    -y|--yes) assume_yes=1 ;;
    agents|claude) target=$arg ;;
    *) usage; exit 1 ;;
  esac
done

case "$target" in
  agents) DEST=~/.agents/skills/$SKILL_NAME ;;
  claude) DEST=~/.claude/skills/$SKILL_NAME ;;
esac

[ "$assume_yes" -eq 1 ] || confirm_install

mkdir -p "$DEST"
curl -sSL "$RAW_BASE/skills/$SKILL_NAME/SKILL.md" > "$DEST/SKILL.md"
echo "Installed $SKILL_NAME to $DEST"

#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
: "${GRADLE_BIN:=gradle}"
cd "$ROOT/android"
"$GRADLE_BIN" assembleDebug --no-daemon
printf '\nAPK: %s\n' "$ROOT/android/app/build/outputs/apk/debug/app-debug.apk"

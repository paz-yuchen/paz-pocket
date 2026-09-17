#!/usr/bin/env python3
"""Start a detached distill-session turn after a Codex session ends."""

from __future__ import annotations

import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from typing import Any


RECURSION_GUARD = "PAZ_DISTILL_SESSION_HOOK_ACTIVE"
SKILL_PATH_ENV = "DISTILL_SESSION_SKILL_PATH"
LOG_DIR_ENV = "DISTILL_SESSION_HOOK_LOG_DIR"
DRY_RUN_ENV = "DISTILL_SESSION_HOOK_DRY_RUN"


def _load_event() -> dict[str, Any]:
    event = json.load(sys.stdin)
    if not isinstance(event, dict):
        raise ValueError("hook input must be a JSON object")
    if event.get("hook_event_name") != "SessionEnd":
        raise ValueError("expected a SessionEnd hook event")
    if not isinstance(event.get("session_id"), str) or not event["session_id"]:
        raise ValueError("SessionEnd event is missing session_id")
    return event


def _skill_path() -> Path:
    configured = os.environ.get(SKILL_PATH_ENV)
    candidates = [
        Path(configured).expanduser() if configured else None,
        Path.home() / ".agents/skills/distill-session/SKILL.md",
        Path.home() / ".codex/skills/distill-session/SKILL.md",
        Path(__file__).resolve().parents[1] / "skills/distill-session/SKILL.md",
    ]
    for candidate in candidates:
        if candidate is not None and candidate.is_file():
            return candidate.resolve()
    raise FileNotFoundError(
        "distill-session/SKILL.md was not found; install the skill globally or "
        f"set {SKILL_PATH_ENV}"
    )


def _codex_path() -> str:
    configured = os.environ.get("CODEX_CLI_PATH")
    if configured and Path(configured).is_file():
        return configured
    discovered = shutil.which("codex")
    if discovered:
        return discovered
    raise FileNotFoundError("codex executable was not found on PATH")


def _prompt(skill_path: Path, transcript_path: object) -> str:
    transcript = transcript_path if isinstance(transcript_path, str) else "unavailable"
    return f"""Invoke the $distill-session skill for this completed session.

Read and follow the skill instructions at:
{skill_path}

This is an automated SessionEnd invocation. Treat the resumed conversation as the source material. The hook reported the transcript path as {transcript}; use it only if needed because the transcript format is not a stable interface.

Perform Phase 1 only: produce the complete review manifest and ask the user to approve all items, selected IDs, or revisions. Do not write to Obsidian or apply any proposed knowledge changes without explicit user approval.
"""


def _safe_session_id(session_id: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", session_id)[:160] or "unknown"


def _launch(event: dict[str, Any]) -> None:
    session_id = event["session_id"]
    skill_path = _skill_path()
    codex = _codex_path()
    requested_cwd = event.get("cwd")
    cwd = Path(requested_cwd) if isinstance(requested_cwd, str) else Path.home()
    if not cwd.is_dir():
        cwd = Path.home()

    command = [
        codex,
        "exec",
        "resume",
        "--skip-git-repo-check",
        session_id,
        _prompt(skill_path, event.get("transcript_path")),
    ]
    child_env = os.environ.copy()
    child_env[RECURSION_GUARD] = "1"

    if os.environ.get(DRY_RUN_ENV) == "1":
        print(json.dumps({"command": command, "cwd": str(cwd)}, ensure_ascii=False))
        return

    log_dir = Path(
        os.environ.get(
            LOG_DIR_ENV,
            str(Path.home() / ".codex/log/distill-session-hooks"),
        )
    ).expanduser()
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"{_safe_session_id(session_id)}.log"

    with log_path.open("ab", buffering=0) as log_file:
        subprocess.Popen(
            command,
            cwd=cwd,
            env=child_env,
            stdin=subprocess.DEVNULL,
            stdout=log_file,
            stderr=subprocess.STDOUT,
            start_new_session=True,
            close_fds=True,
        )


def main() -> int:
    if os.environ.get(RECURSION_GUARD) == "1":
        return 0
    try:
        _launch(_load_event())
    except (json.JSONDecodeError, OSError, ValueError) as error:
        print(f"distill-session hook failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

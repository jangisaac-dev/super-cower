#!/usr/bin/env python3
"""Validate the super-cower skill package structure."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    ROOT / "SKILL.md",
    ROOT / "README.md",
    ROOT / ".codex" / "INSTALL.md",
    ROOT / "agents" / "openai.yaml",
    ROOT / "references" / "brainstorming.md",
    ROOT / "references" / "writing-plans.md",
    ROOT / "references" / "subagent-driven-development.md",
    ROOT / "references" / "requesting-code-review.md",
    ROOT / "references" / "test-driven-development.md",
    ROOT / "references" / "systematic-debugging.md",
    ROOT / "references" / "finishing-development.md",
    ROOT / "references" / "codex-tools.md",
    ROOT / "references" / "agents" / "implementer.md",
    ROOT / "references" / "agents" / "spec-reviewer.md",
    ROOT / "references" / "agents" / "code-quality-reviewer.md",
]

IMPLEMENTER_TOKENS = [
    "DONE",
    "DONE_WITH_CONCERNS",
    "NEEDS_CONTEXT",
    "BLOCKED",
    "summary",
    "files_touched",
    "tests_run",
    "concerns",
]

REVIEWER_TOKENS = [
    "APPROVED",
    "CHANGES_REQUIRED",
    "summary",
    "blocking_issues",
    "non_blocking_issues",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def parse_frontmatter(text: str) -> dict[str, str] | None:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return None
    data: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        if not raw_line.strip():
            continue
        if ":" not in raw_line:
            return None
        key, value = raw_line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def validate_required_files(errors: list[str]) -> None:
    for path in REQUIRED_FILES:
        if not path.exists():
            fail(f"Missing required file: {path}", errors)
        elif path.is_file() and not read_text(path).strip():
            fail(f"Required file is empty: {path}", errors)


def validate_skill_md(errors: list[str]) -> None:
    skill_text = read_text(ROOT / "SKILL.md")
    frontmatter = parse_frontmatter(skill_text)
    if frontmatter is None:
        fail("SKILL.md must start with valid YAML frontmatter.", errors)
        return

    if set(frontmatter) != {"name", "description"}:
        fail("SKILL.md frontmatter must contain only 'name' and 'description'.", errors)

    if frontmatter.get("name") != "super-cower":
        fail("SKILL.md frontmatter name must be 'super-cower'.", errors)

    description = frontmatter.get("description", "")
    if "[TODO" in description or len(description) < 120:
        fail("SKILL.md description must be complete and informative.", errors)

    required_phrases = [
        "single public entrypoint",
        "references/brainstorming.md",
        "references/writing-plans.md",
        "references/subagent-driven-development.md",
    ]
    lowered = skill_text.lower()
    for phrase in required_phrases:
        if phrase not in lowered:
            fail(f"SKILL.md is missing required phrase: {phrase}", errors)


def validate_openai_yaml(errors: list[str]) -> None:
    text = read_text(ROOT / "agents" / "openai.yaml")
    required_lines = [
        'display_name: "Super Cower"',
        'default_prompt: "Use $super-cower',
        "policy:",
        "allow_implicit_invocation: true",
    ]
    for line in required_lines:
        if line not in text:
            fail(f"agents/openai.yaml is missing: {line}", errors)


def validate_install_doc(errors: list[str]) -> None:
    text = read_text(ROOT / ".codex" / "INSTALL.md")
    required_phrases = [
        "~/.agents/skills/super-cower",
        "multi_agent = true",
        "AGENTS.md",
        "ln -s",
    ]
    for phrase in required_phrases:
        if phrase not in text:
            fail(f".codex/INSTALL.md is missing: {phrase}", errors)


def validate_codex_tools(errors: list[str]) -> None:
    text = read_text(ROOT / "references" / "codex-tools.md")
    required_phrases = [
        "spawn_agent",
        "send_input",
        "wait_agent",
        "close_agent",
        "fork_context=false",
    ]
    for phrase in required_phrases:
        if phrase not in text:
            fail(f"references/codex-tools.md is missing: {phrase}", errors)


def validate_agent_prompt(path: Path, tokens: list[str], errors: list[str]) -> None:
    text = read_text(path)
    for token in tokens:
        if token not in text:
            fail(f"{path} is missing token: {token}", errors)


def main() -> int:
    errors: list[str] = []

    validate_required_files(errors)
    if errors:
        for error in errors:
            print(f"[FAIL] {error}", file=sys.stderr)
        return 1

    validate_skill_md(errors)
    validate_openai_yaml(errors)
    validate_install_doc(errors)
    validate_codex_tools(errors)
    validate_agent_prompt(ROOT / "references" / "agents" / "implementer.md", IMPLEMENTER_TOKENS, errors)
    validate_agent_prompt(ROOT / "references" / "agents" / "spec-reviewer.md", REVIEWER_TOKENS, errors)
    validate_agent_prompt(
        ROOT / "references" / "agents" / "code-quality-reviewer.md",
        REVIEWER_TOKENS,
        errors,
    )

    if errors:
        for error in errors:
            print(f"[FAIL] {error}", file=sys.stderr)
        return 1

    print("[OK] super-cower skill package is structurally valid.")
    print(f"[OK] Checked {len(REQUIRED_FILES)} required files under {ROOT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

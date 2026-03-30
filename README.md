# Super Cower

`super-cower` is a single-entry Codex skill for software-development work. The user
should be able to say "`super-cower`" once, or not mention it at all, and still get
the full workflow: design clarification, planning, subagent execution, review, and
wrap-up.

## What It Contains

- `SKILL.md`: the only public entrypoint and routing document
- `references/`: internal stage guides and subagent prompt templates
- `scripts/validate_skills.py`: structural validator for the skill package
- `.codex/INSTALL.md`: global installation instructions for `~/.agents/skills`

## Design Goals

- Expose only one public skill name: `super-cower`
- Keep the upstream `superpowers` flow shape, but adapt it to Codex tools
- Hide helper stages behind internal references instead of publishing many skills
- Prefer automatic activation for general software-engineering requests

## Install

Read [`.codex/INSTALL.md`](.codex/INSTALL.md) for the global symlink setup and the
recommended `AGENTS.md` routing line.

## Validate

Run both checks from the repository root:

```bash
python3 scripts/validate_skills.py
# Optional: run the upstream validator if you have the skill-creator tool available.
python3 /path/to/skill-creator/scripts/quick_validate.py .
```

For privacy-safe publishing, prefer a repository-local Git identity that does not
expose a personal email address, and review staged changes before pushing:

```bash
git config user.name "super-cower-release"
git config user.email "super-cower@users.noreply.github.com"
git diff --cached
```

## Repository Layout

```text
.
├── .codex/INSTALL.md
├── agents/openai.yaml
├── references/
│   ├── agents/
│   ├── brainstorming.md
│   ├── codex-tools.md
│   ├── finishing-development.md
│   ├── requesting-code-review.md
│   ├── subagent-driven-development.md
│   ├── systematic-debugging.md
│   ├── test-driven-development.md
│   └── writing-plans.md
├── scripts/validate_skills.py
└── SKILL.md
```

## Upstream Relationship

This repository is a Codex-focused adaptation of the ideas in
[obra/superpowers](https://github.com/obra/superpowers). It keeps the same general
workflow philosophy while collapsing the public surface area down to one Codex skill.

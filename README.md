# Super Cower

`super-cower` is a single-entry Codex skill for software-development work. It is
designed to feel native inside Codex rather than like a thin port from another
assistant: short repo inspection, explicit `update_plan`, selective clarification,
task packets for `spawn_agent`, focused `apply_patch` edits, and verification that
fits the repository.

The goal is that a user can say "`super-cower`" once, or not mention it at all, and
still get the full flow without helper-skill ceremony: design clarification,
planning, subagent execution, review, and wrap-up.

## What It Contains

- `SKILL.md`: the only public entrypoint and routing document
- `docs/super-cower/`: repository-local home for saved specs and plans
- `references/`: internal stage guides and subagent prompt templates
- `scripts/validate_skills.py`: structural validator for the skill package
- `.codex/INSTALL.md`: global installation instructions for `~/.agents/skills`

## What Makes It Codex-Native

- Expose only one public skill name: `super-cower`
- Organize around Codex controller behavior instead of generic assistant abstractions
- Hide helper stages behind internal references instead of publishing many skills
- Prefer automatic activation for general software-engineering requests
- Use `update_plan` for multi-step coordination and `multi_tool_use.parallel` for
  fast read-only inspection
- Use `spawn_agent`, `send_input`, `wait_agent`, and `close_agent` with explicit
  task packets and disjoint file ownership
- Treat dirty worktrees, missing git metadata, and prompt-heavy repositories as
  first-class realities rather than edge cases
- Keep validator coverage tight enough that future edits do not silently drift back
  toward platform-agnostic wording

## Activation And Opt-Out

- `super-cower` should activate for general software-development work without the
  user having to invoke helper stage names.
- The user can opt out by explicitly asking for another workflow, asking not to use
  TDD, or asking not to use subagents.
- If the task is tiny or delegation would only add overhead, the workflow should
  stay inline and finish locally.

## Workflow Shape

1. Inspect the current repository and instructions briefly.
2. Ask one clarifying question only when the task is still decision-ambiguous.
3. Write an explicit plan when the work spans multiple meaningful steps.
4. Split execution into task packets with owned files, verification commands, and
   constraints.
5. Run worker/reviewer subagents when that buys meaningful leverage; otherwise stay
   inline.
6. Verify with focused tests, validators, or characterization checks, then wrap up
   with a concise handoff.

## Install

Read [`.codex/INSTALL.md`](.codex/INSTALL.md) for the global symlink setup and the
recommended `AGENTS.md` routing line.

## Validate

Run the repository validator from the repository root:

```bash
python3 scripts/validate_skills.py
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
├── docs/super-cower/
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
workflow philosophy while collapsing the public surface area down to one Codex
skill and replacing generic multi-stage choreography with Codex-native controller
loops, evidence-driven review, and task-packet contracts.

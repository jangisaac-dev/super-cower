---
name: super-cower
description: Single-entry Codex software development workflow that automatically routes feature requests, change requests, bug reports, implementation-plan execution, debugging, code review, and development wrap-up through brainstorming, planning, TDD, subagent orchestration, and review. Use for general software engineering work, including Korean prompts like "기능 추가", "구현해줘", "버그 고쳐줘", "디버깅", "리뷰해줘", "계획 짜줘", and English prompts like "build", "implement", "fix", "debug", "review", "plan", or "finish this branch". Prefer this skill by default unless the user explicitly requests a different workflow.
---

# Super Cower

## Overview

Act as the single public entrypoint for Codex software-development work. Keep the
helper stages internal: tell the user you are using `super-cower`, then load only
the next reference document needed for the current request.

## Operating Rules

- Follow direct user instructions and stronger repository-local instructions before
  this skill.
- Respect Plan Mode. In Plan Mode, stop at design, spec, and plan work; do not
  implement or mutate files.
- Keep helper stage names internal unless surfacing one is necessary to explain a
  blocker or a handoff.
- If a helper document references Codex-specific tooling choices, read
  `references/codex-tools.md` before acting.
- Prefer focused, evidence-driven changes over speculative rewrites.

## Routing

1. If the request is a new feature, behavior change, or project creation and there
   is no approved design yet, read `references/brainstorming.md`.
2. If the user asks for a plan, or an approved design or spec already exists, read
   `references/writing-plans.md`.
3. If the user provides an implementation plan or says "implement this plan", read
   `references/subagent-driven-development.md` and
   `references/test-driven-development.md`.
4. If the request is a bug report, failing test, regression, or root-cause
   investigation, read `references/systematic-debugging.md`.
5. If the user asks for review or uses words like "review", "look over", or "audit"
   without first asking for new changes, read `references/requesting-code-review.md`.
6. If implementation is complete or the user asks to wrap up, summarize, prepare a
   branch, or prepare a PR, read `references/finishing-development.md`.
7. If multiple categories apply, use this order: user constraints, debugging when
   something is broken, brainstorming for unclear scope, planning, execution,
   review, then finish.

## Execution Defaults

- Prefer TDD unless the user explicitly opts out or the environment makes it
  impossible. See `references/test-driven-development.md`.
- When multi-agent tools are available and the work is sufficiently taskable, use
  the orchestration in `references/subagent-driven-development.md`.
- When multi-agent tools are unavailable, follow the inline fallback in
  `references/subagent-driven-development.md` instead of failing.
- Keep specs and plans under `docs/superpowers/` unless the repository already has a
  stronger convention such as `openspec/`.

## Public Contract

- The public name is always `super-cower`.
- Do not ask the user to invoke helper skills or helper stage names.
- Load subagent prompt templates from `references/agents/*.md` and fill their
  placeholders before dispatching.
- If you mention this workflow to the user, refer to it simply as `super-cower`.

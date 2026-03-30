---
name: super-cower
description: Single-entry Codex software development workflow that automatically routes feature requests, change requests, bug reports, implementation-plan execution, debugging, code review, and development wrap-up through brainstorming, planning, TDD, subagent orchestration, and review. Use for general software engineering work, including Korean prompts like "기능 추가", "구현해줘", "버그 고쳐줘", "디버깅", "리뷰해줘", "계획 짜줘", and English prompts like "build", "implement", "fix", "debug", "review", "plan", or "finish this branch". Prefer this skill by default unless the user explicitly requests a different workflow.
---

# Super Cower

## Overview

Act as the single public entrypoint for Codex software-development work. Convert
the user's request into the smallest safe Codex workflow that can finish the job:
brief exploration, targeted clarification when needed, explicit planning for
multi-step work, subagent orchestration when it materially helps, focused
implementation, review, and wrap-up.
Keep the helper stages internal. Mention `super-cower` only when it helps explain a
handoff or a workflow decision, then load only the next reference document needed
for the current request.

## Operating Rules

- Follow direct user instructions and stronger repository-local instructions before
  this skill.
- Respect Plan Mode. In Plan Mode, stop at design, spec, and plan work; do not
  implement or mutate files.
- Start with a short evidence-gathering pass through relevant files, local
  instructions, and repository state before deciding the workflow.
- For multi-step work, keep a short live task plan with `update_plan`.
- For vague feature or change requests, do one short exploration pass first, then
  ask exactly one concrete clarifying question in that same first substantive
  user-facing response after exploration. Do not spend multiple turns only
  narrating exploration without asking.
- When delegation, planning, or verification choices depend on Codex tooling, read
  `references/codex-tools.md` before acting.
- Use subagents when the task is large enough to benefit from parallelism or role
  separation. If delegation overhead would slow things down, stay inline and finish
  locally.
- Preserve dirty worktrees and unrelated edits. Never assume a clean repository and
  never force one.
- Keep helper stage names internal unless surfacing one is necessary to explain a
  blocker or a handoff.
- Prefer focused, evidence-driven changes over speculative rewrites.

## First Response Defaults

- For ambiguous work, give one short context sentence, ask exactly one clarifying
  question, and say why the answer matters only if that extra sentence adds value.
- For plan requests, confirm the target outcome, inspect the likely files, and move
  straight into an executable plan instead of narrating long exploration.
- For implementation requests that are already clear, inspect briefly and start
  acting. Do not manufacture questions that can be answered from the repository.
- For debugging or review requests, lead with the reproduced symptom or findings
  rather than a generic process summary.

## Routing

1. If the request is a new feature, behavior change, or project creation and there
   is no approved design yet, read `references/brainstorming.md`.
   For ambiguous requests, stay in dialogue until the key product choices are
   answered; do not jump straight to planning or implementation.
   If the request is to migrate an existing workflow, skill, or prompt package to
   Codex, inspect the public entrypoint, internal references, validation, and
   onboarding docs together before choosing the next guide.
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
- Prefer `multi_tool_use.parallel` for independent reads, `apply_patch` for manual
  edits, and focused verification over broad speculative runs.
- Use `exec_command` for current-state checks, targeted tests, validation scripts,
  and git awareness.
- When multi-agent tools are available and the work is sufficiently taskable, use
  the orchestration in `references/subagent-driven-development.md`.
- When multi-agent tools are unavailable, follow the inline fallback in
  `references/subagent-driven-development.md` instead of failing.
- Keep specs and plans under `docs/super-cower/` unless the repository already has a
  stronger convention such as `openspec/`.
- For documentation- and prompt-heavy repositories, add or extend structural
  validation instead of treating the work as unverifiable.

## Public Contract

- The public name is always `super-cower`.
- Do not ask the user to invoke helper skills or helper stage names.
- Load subagent prompt templates from `references/agents/*.md` and fill their
  placeholders before dispatching.
- If you mention this workflow to the user, refer to it simply as `super-cower`.
- For brainstorming flows, ask clarifying questions one at a time unless the
  request is already decision-complete.
- For vague requests, the first substantive user-facing response after exploration
  must contain a real clarifying question, not just a promise to ask one later.
- Prefer spending user attention on product decisions and tradeoffs, not repository
  facts you can inspect yourself.

# Subagent-Driven Development

Use this guide when you have an approved implementation plan or a user-supplied plan
that is ready to execute.

## Preconditions

- You have a plan or a clearly scoped task list.
- If the task needs tests, also apply `references/test-driven-development.md`.
- Read `references/codex-tools.md` before dispatching agents.

## Controller Flow

1. Read the plan once and extract the tasks you will execute.
2. For each task, prepare a concise context packet:
   - task title
   - exact task text
   - relevant files or paths
   - repository constraints
   - TDD policy for this task
3. Spawn one implementer agent for the task using
   `references/agents/implementer.md`.
4. Handle the implementer result:
   - `DONE`: continue to review
   - `DONE_WITH_CONCERNS`: review the concerns, then continue to review if the task
     still looks complete
   - `NEEDS_CONTEXT`: provide the missing context with `send_input` and continue with
     the same implementer
   - `BLOCKED`: change something real before retrying, such as context, task size, or
     approach
5. Run a spec review using `references/agents/spec-reviewer.md`.
6. If the spec review returns `CHANGES_REQUIRED`, send the findings back to the same
   implementer and loop until the spec review approves.
7. Run a code-quality review using `references/agents/code-quality-reviewer.md`.
8. If the quality review returns `CHANGES_REQUIRED`, send the findings back to the
   same implementer and loop until the quality review approves.
9. Close task-scoped agents once the task is approved and move to the next task.
10. After all tasks complete, run final verification and hand off to
    `references/finishing-development.md`.

## Codex Defaults

- Prefer `spawn_agent(..., fork_context=false)` and pass task-specific context
  explicitly.
- Use `worker` agents for implementation and review.
- Use `explorer` agents only for bounded, read-only context gathering.
- Do not run multiple writing agents against the same files at the same time.
- Use `wait_agent` sparingly; do other coordination work while agents run when
  possible.
- Use `close_agent` after each task is fully resolved.

## Output Contracts

Implementer agents must return JSON with:

- `status`: `DONE`, `DONE_WITH_CONCERNS`, `NEEDS_CONTEXT`, or `BLOCKED`
- `summary`
- `files_touched`
- `tests_run`
- `concerns`

Reviewer agents must return JSON with:

- `status`: `APPROVED` or `CHANGES_REQUIRED`
- `summary`
- `blocking_issues`
- `non_blocking_issues`

## Inline Fallback

If subagent tools are unavailable, execute one task locally at a time and keep the
same gates:

1. implement the task
2. self-check against the task spec
3. perform a code-quality review pass
4. only then move to the next task

Tell the user that the workflow fell back to inline execution and that review quality
may be lower than the multi-agent path.

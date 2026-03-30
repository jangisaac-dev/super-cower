# Subagent-Driven Development

Use this guide when you have an approved implementation plan or a user-supplied plan
that is ready to execute.

## Preconditions

- You have a plan or a clearly scoped task list.
- If the task needs tests, also apply `references/test-driven-development.md`.
- Read `references/codex-tools.md` before dispatching agents.

## Controller Flow

1. Probe the environment before dispatch:
   - confirm repository state
   - identify the relevant verification commands
   - confirm whether subagent tools are available
2. Read the plan once and extract the tasks you will execute.
3. Decide which tasks should stay local and which are worth delegating. Delegate
   only when the task is well-bounded and the coordination cost is justified.
4. Use `update_plan` to track the critical path and keep only one in-progress step.
5. For each delegated task, prepare an executable task packet:
   - task id
   - task title
   - exact task text
   - acceptance criteria
   - out-of-scope reminders
   - owned files or write scope
   - relevant read-only files or paths
   - repository constraints
   - verification commands
   - TDD policy for this task
   - reviewer focus when helpful
6. If key context is still missing, gather it locally or spawn one bounded
   read-only explorer before assigning the implementation task.
7. Spawn one implementer agent for the task using
   `references/agents/implementer.md`.
8. Run multiple implementers in parallel only when their write scopes are disjoint.
9. While agents are running, prepare review packets, inspect unrelated context, or
   advance other controller work instead of immediately blocking on `wait_agent`.
10. Handle the implementer result:
   - `DONE`: continue to review
   - `DONE_WITH_CONCERNS`: review the concerns, then continue to review if the task
     still looks complete
   - `NEEDS_CONTEXT`: provide the missing context with `send_input` and continue with
     the same implementer
   - `BLOCKED`: change something real before retrying, such as context, task size, or
     approach
11. Build an evidence-driven review packet with:
    - task id and title
    - acceptance criteria
    - implementation summary
    - files touched
    - verification commands and results
    - changed excerpts or key file references when helpful
    - known concerns from the implementer
12. Run a spec review using `references/agents/spec-reviewer.md`.
13. Run a code-quality review using `references/agents/code-quality-reviewer.md`.
14. If either review returns `CHANGES_REQUIRED`, synthesize the blocking findings and
    send them back to the same implementer. Reuse the same worker unless there is a
    concrete reason to replace it.
15. If the same task fails review twice or reviewers disagree in a contradictory way,
    escalate to a controller decision instead of looping forever.
16. Close task-scoped agents once the task is approved and move to the next task.
17. After all tasks complete, run final verification and hand off to
    `references/finishing-development.md`.

## Codex Defaults

- Use `multi_tool_use.parallel` for local read-only context gathering before or
  between delegation steps.
- Prefer `spawn_agent(..., fork_context=false)` and pass task-specific context
  explicitly.
- Use `worker` agents for implementation and review.
- Use `explorer` agents only for bounded, read-only context gathering.
- Do not run multiple writing agents against the same files at the same time.
- Tell workers they are not alone in the codebase and must preserve unrelated edits.
- Use `wait_agent` sparingly; do other coordination work while agents run when
  possible.
- Use `close_agent` after each task is fully resolved.
- For documentation- or prompt-heavy repositories, treat validators and structural
  checks as the task's test surface.

## Task Packet Checklist

Before spawning a worker, confirm the packet includes all of the following:

- clear task title
- exact requested outcome
- owned files
- supporting references
- repository constraints and non-goals
- verification commands
- TDD or validation expectation
- output contract

## Controller-Owned State

Track, at minimum, the following controller state for each task:

- task id
- current owner: local, explorer, or worker
- retry count
- review status
- final verification status
- unresolved risks or follow-ups

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
3. write down verification evidence
4. perform a code-quality review pass against that evidence
5. only then move to the next task

Tell the user that the workflow fell back to inline execution and that review quality
may be lower than the multi-agent path.

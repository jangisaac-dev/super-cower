# Codex Tool Mapping

Use this reference whenever the workflow needs to translate generic agent workflow
steps into Codex tools.

## Capability Matrix

- Local controller work happens through `exec_command`, `multi_tool_use.parallel`,
  `update_plan`, `apply_patch`, and repository-native verification commands.
- Delegation happens through `spawn_agent`, `send_input`, `wait_agent`, and
  `close_agent` when those tools are available and the task is worth the overhead.
- If delegation tools are unavailable, inline controller execution is the default
  path, not an error condition.

## Controller Defaults

- Start with a short user-facing update, then inspect the repository before choosing
  the next stage.
- Use `multi_tool_use.parallel` for independent read-only inspection work so the
  controller gathers context quickly.
- Use `update_plan` once the task clearly has multiple meaningful steps.
- Use `apply_patch` for manual file edits. Use shell commands for formatters, test
  runs, validators, and other repository-native commands.
- Prefer focused verification evidence over large, slow command runs.

## Core Mapping

- short repo inspection -> `exec_command`, `rg`, `sed`, `ls`
- parallel repo inspection -> `multi_tool_use.parallel`
- plan or task checklist -> `update_plan`
- subagent dispatch -> `spawn_agent`
- send more context to the same subagent -> `send_input`
- wait for a subagent result when blocked -> `wait_agent`
- close finished subagents -> `close_agent`
- manual file edits -> `apply_patch`
- focused verification commands -> `exec_command`
- inspect existing shell state when needed -> `read_thread_terminal`

## Subagent Defaults

- Prefer `fork_context=false` and provide explicit task context.
- Use `worker` for implementers and reviewers.
- Use `explorer` only for narrow read-only discovery tasks.
- Assign explicit ownership: owned files, allowed references, constraints, and
  verification commands.
- Keep write scopes disjoint if more than one agent runs at the same time.
- Do other controller work while agents run. Call `wait_agent` sparingly.
- Close task-scoped agents as soon as their work is approved or no longer needed.

## Task Packet Minimum

Every delegated task should include:

- task id
- task title
- exact task text
- acceptance criteria
- out-of-scope reminders
- owned files or expected write scope
- relevant read-only references
- project or repository context
- local constraints and non-goals
- verification commands
- reviewer focus when helpful
- TDD policy
- expected output contract

## Prompt Loading

When a workflow step calls for an implementer or reviewer:

1. Read the matching template under `references/agents/`.
2. Replace the placeholders with the current task, context, and constraints.
3. Spawn the agent with that filled prompt as the message.
4. Ask for JSON-only output when the template requires it.

## Plan Mode

- In Plan Mode, use the workflow for design and planning only.
- Do not edit files or execute implementation steps while Plan Mode is active.

## Dirty Worktrees

- Check git state before editing when repository hygiene matters.
- Preserve unrelated edits in the worktree.
- Never rely on destructive cleanup commands as part of the normal workflow.

## Git Reality

- Not every Codex workspace is a git checkout.
- Detect git state before assuming branches, commits, or PRs are available.
- If git is unavailable, complete the workflow with verification and a human-readable
  summary instead of forcing branch operations.

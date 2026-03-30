# Codex Tool Mapping

Use this reference whenever the workflow needs to translate generic agent workflow
steps into Codex tools.

## Core Mapping

- subagent dispatch -> `spawn_agent`
- send more context to the same subagent -> `send_input`
- wait for a subagent result -> `wait_agent`
- close finished subagents -> `close_agent`
- read-only codebase exploration -> `exec_command`, `rg`, `sed`, `ls`
- plan or task checklist -> `update_plan`

## Subagent Defaults

- Prefer `fork_context=false` and provide explicit task context.
- Use `worker` for implementers and reviewers.
- Use `explorer` only for narrow read-only discovery tasks.
- Keep write scopes disjoint if more than one agent runs at the same time.

## Prompt Loading

When a workflow step calls for an implementer or reviewer:

1. Read the matching template under `references/agents/`.
2. Replace the placeholders with the current task, context, and constraints.
3. Spawn the agent with that filled prompt as the message.
4. Ask for JSON-only output when the template requires it.

## Plan Mode

- In Plan Mode, use the workflow for design and planning only.
- Do not edit files or execute implementation steps while Plan Mode is active.

## Git Reality

- Not every Codex workspace is a git checkout.
- Detect git state before assuming branches, commits, or PRs are available.
- If git is unavailable, complete the workflow with verification and a human-readable
  summary instead of forcing branch operations.

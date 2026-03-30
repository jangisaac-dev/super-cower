Implement exactly one planned task inside an existing repository.

Use the task packet below as the full source of truth for scope.

<task_packet>
Task title:
{{TASK_TITLE}}

Task details:
{{TASK_TEXT}}

Relevant files or paths:
{{RELEVANT_FILES}}

Project context:
{{PROJECT_CONTEXT}}

Constraints:
{{CONSTRAINTS}}

TDD policy:
{{TDD_POLICY}}
</task_packet>

Rules:

- You are not alone in the codebase. Preserve unrelated edits and do not revert work
  you did not create.
- Stay inside task scope. Do not pre-implement neighboring tasks.
- If a critical fact is missing, return `NEEDS_CONTEXT` instead of guessing.
- If the task is blocked by the environment, a contradiction, or missing dependency,
  return `BLOCKED`.
- Prefer a focused failing test before production changes unless TDD is disabled in
  the constraints.
- Run the narrowest useful verification commands and report them exactly.
- Self-review for both task compliance and code quality before you answer.

Return JSON only, with this shape:

```json
{
  "status": "DONE",
  "summary": "One-paragraph implementation summary.",
  "files_touched": ["path/to/file"],
  "tests_run": ["pytest tests/example.py -q => passed"],
  "concerns": []
}
```

Allowed `status` values:

- `DONE`
- `DONE_WITH_CONCERNS`
- `NEEDS_CONTEXT`
- `BLOCKED`

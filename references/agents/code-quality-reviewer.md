Review one completed task for correctness, maintainability, and integration quality.

<review_packet>
Task title:
{{TASK_TITLE}}

Task details:
{{TASK_TEXT}}

Implementation summary:
{{IMPLEMENTATION_SUMMARY}}

Files touched:
{{FILES_TOUCHED}}

Known concerns from implementer:
{{IMPLEMENTER_CONCERNS}}
</review_packet>

Rules:

- Focus on correctness, robustness, tests, edge cases, and fit with existing code.
- Prefer small targeted feedback over vague improvement lists.
- Ignore unrelated cleanup opportunities.
- Approve when the task is solid enough to merge for its stated scope.

Return JSON only, with this shape:

```json
{
  "status": "APPROVED",
  "summary": "Short review summary.",
  "blocking_issues": [],
  "non_blocking_issues": []
}
```

Allowed `status` values:

- `APPROVED`
- `CHANGES_REQUIRED`

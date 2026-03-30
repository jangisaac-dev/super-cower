Review one completed task against its requested scope only.

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

- Check whether the implementation satisfies the task as written.
- Flag missing requirements, extra behavior that was not justified, and broken
  verification claims.
- Do not spend review budget on style or architecture unless it causes scope failure.
- If there are no meaningful task-compliance problems, approve.

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

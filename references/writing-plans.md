# Writing Plans

Use this guide when the design is approved or the user explicitly asked for an
implementation plan.

## Outcome

Produce a decision-complete implementation plan that another agent can execute
without inventing missing behavior.

## Planning Target

The plan should be executable as task packets, not just readable by a human.
Another agent should be able to take one task block and start work without asking
for missing behavior, missing files, or missing verification steps.

## Process

1. Read the approved design, relevant code, local instructions, and existing
   conventions.
2. Map the files or modules that will likely change before writing tasks.
3. Break the work into tasks small enough for one implementation agent to complete
   and verify safely, or one inline pass to execute without confusion.
4. For each task, include:
   - a stable task id
   - the goal
   - acceptance criteria
   - out-of-scope behavior
   - owned files or primary write scope
   - supporting files or interfaces
   - exact verification commands or validation steps
   - dependencies on earlier tasks
   - any constraint the implementer must not violate
   - reviewer focus when helpful
   - whether the task is safe to run in parallel with another task
5. Prefer task groups that can be reviewed independently.
6. Save the plan in the strongest project-native place:
   `openspec/` if the project uses it, otherwise
   `docs/super-cower/plans/YYYY-MM-DD--plan.md`.
7. If the user wants execution next, hand off to the execution guide.

## Guardrails

- Do not leave TODOs, placeholders, or vague notes like "handle edge cases".
- Do not split into many tiny tasks if the work is obviously one atomic change.
- Do not pad the plan with unrelated refactors.
- Do not assign overlapping write ownership to tasks you intend to run in parallel.
- If the user already supplied a sufficiently detailed plan, reuse it and only patch
  the missing gaps.
- Do not leave the reviewer to infer acceptance criteria from vague task prose.

## Recommended Plan Shape

- Title
- Brief summary
- Task list with `task_id`, owned files, supporting references, constraints, and verification
- Test plan
- Assumptions or defaults chosen

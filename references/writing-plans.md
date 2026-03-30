# Writing Plans

Use this guide when the design is approved or the user explicitly asked for an
implementation plan.

## Outcome

Produce a decision-complete implementation plan that another agent can execute
without inventing missing behavior.

## Process

1. Read the approved design, relevant code, local instructions, and existing
   conventions.
2. Map the files or modules that will likely change before writing tasks.
3. Break the work into tasks small enough for one implementation agent to complete
   and verify safely.
4. For each task, include:
   - the goal
   - affected files or interfaces
   - exact verification steps
   - dependencies on earlier tasks
   - any constraint the implementer must not violate
5. Prefer task groups that can be reviewed independently.
6. Save the plan in the strongest project-native place:
   `openspec/` if the project uses it, otherwise
   `docs/superpowers/plans/YYYY-MM-DD--plan.md`.
7. If the user wants execution next, hand off to the execution guide.

## Guardrails

- Do not leave TODOs, placeholders, or vague notes like "handle edge cases".
- Do not split into many tiny tasks if the work is obviously one atomic change.
- Do not pad the plan with unrelated refactors.
- If the user already supplied a sufficiently detailed plan, reuse it and only patch
  the missing gaps.

## Recommended Plan Shape

- Title
- Brief summary
- Task list with files, constraints, and verification
- Test plan
- Assumptions or defaults chosen

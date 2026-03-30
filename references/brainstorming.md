# Brainstorming

Use this guide when the user wants to build, change, or design something and the
scope is not already nailed down.

## Outcome

Produce an approved design or spec before implementation starts.

## Process

1. Inspect the current project context first.
2. Ask only the questions that materially change the design.
3. For non-trivial work, propose two or three approaches with a recommendation.
4. Present the design in short sections the user can validate quickly.
5. Confirm success criteria, constraints, interfaces, testing expectations, and any
   migration or rollout concerns.
6. Once the design is approved, write it down in the strongest project-native place:
   `openspec/` if that project uses OpenSpec, otherwise
   `docs/superpowers/specs/YYYY-MM-DD--design.md`.
7. Hand off to planning once the design is approved.

## Guardrails

- Do not jump into implementation while the design is still fuzzy.
- Scale the amount of ceremony to the task. Tiny changes can have tiny specs.
- Respect Plan Mode. If Plan Mode is active, stop after the design or spec.
- Keep the helper stage name internal. The user only needs to hear that
  `super-cower` is refining the design.

## Minimum Design Contents

- Goal and success criteria
- In-scope and out-of-scope behavior
- User-facing and developer-facing constraints
- Key interfaces or files likely to change
- Testing and verification expectations
- Assumptions that were chosen instead of left ambiguous

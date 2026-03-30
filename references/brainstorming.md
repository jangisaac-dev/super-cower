# Brainstorming

Use this guide when the user wants to build, change, or design something and the
scope is not already nailed down.

## Outcome

Produce an approved design or spec before implementation starts.
For vague requests, get there through an actual back-and-forth conversation, not
through silent assumption-making.

## Process

1. Inspect the current project context first, but keep the first pass short and
   targeted.
2. If the request is still ambiguous after that pass, ask exactly one concrete
   clarifying question in that same first substantive user-facing response after
   exploration.
3. Wait for the answer before asking the next question, unless the request is
   already decision-complete.
4. Ask only the questions that materially change scope, behavior, constraints, or
   success criteria.
5. For non-trivial work, propose two or three approaches with a recommendation.
6. Present the design in short sections the user can validate quickly.
7. Confirm success criteria, constraints, interfaces, testing expectations, and any
   migration or rollout concerns.
8. Once the design is approved, write it down in the strongest project-native place:
   `openspec/` if that project uses OpenSpec, otherwise
   `docs/super-cower/specs/YYYY-MM-DD--design.md`.
9. Hand off to planning once the design is approved.

## Questioning Protocol

- One question per message.
- Prefer the highest-leverage question first.
- Ask about product choices, not trivia you can learn from the codebase.
- After the short exploration pass, your first substantive response must include
  the actual question. Do not say you will ask later and then keep exploring.
- If the project is tiny and the user's request is already precise, state the
  assumption set and skip unnecessary questions.
- If the request is vague, do not move to planning until at least one real
  clarifying question has been asked and answered.

## Good First Questions

- What is the primary user action or outcome this feature should enable?
- Where should the new behavior be triggered in the UI or API?
- Which output format or persistence behavior should we support first?
- What constraints matter most: speed, simplicity, compatibility, or visual fit?

## Guardrails

- Do not jump into implementation while the design is still fuzzy.
- Scale the amount of ceremony to the task. Tiny changes can have tiny specs.
- Respect Plan Mode. If Plan Mode is active, stop after the design or spec.
- Do not spend repeated turns saying you will inspect more context when you already
  have enough to ask a high-value question.
- Do not end the first substantive brainstorming response with only an inspection
  summary when the request is still ambiguous.
- Do not batch a list of clarifying questions into one message unless the user
  explicitly asks for that style.
- Keep the helper stage name internal. The user only needs to hear that
  `super-cower` is refining the design.

## First Response Shape For Vague Requests

Use this pattern after the short exploration pass:

1. One sentence summarizing the most relevant context you found.
2. One sentence asking exactly one clarifying question.
3. Optional one sentence explaining why that question matters.

Example:

`현재 저장소에는 내보내기 관련 기능이 보이지 않습니다. 우선 CSV 내보내기를 버튼 클릭으로 시작하면 될까요? 이 선택이 UI 위치와 테스트 범위를 결정합니다.`

## Minimum Design Contents

- Goal and success criteria
- In-scope and out-of-scope behavior
- User-facing and developer-facing constraints
- Key interfaces or files likely to change
- Testing and verification expectations
- Assumptions that were chosen instead of left ambiguous

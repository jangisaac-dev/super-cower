# Test-Driven Development

Use this guide during implementation unless the user explicitly opts out or the
environment makes TDD impossible.

## Default Cycle

1. Write or identify a focused failing test for the behavior you are about to change.
2. Run it and confirm it fails for the reason you expect.
3. Implement the smallest change that can make the test pass.
4. Re-run the focused test, then the next wider verification layer.
5. Refactor only after the behavior is protected by passing tests.

## Verification Contract

When the work is being delegated or reviewed, capture the verification trail in a
way another agent can inspect:

- failing command or failing example when available
- expected failure or reproduced symptom
- passing command after the change
- broader verification command
- manual verification notes only when no reasonable automation exists

## Guardrails

- Do not quietly write production code first if a reasonable test can be written.
- Keep test scope tight; avoid whole-suite runs until the local behavior is stable.
- For prompt, documentation, or skill repositories, treat structural validation,
  characterization checks, and focused example-based verification as the equivalent
  safety net.
- If TDD is not practical, say why and choose the smallest safe alternative, such as
  characterization tests or manual reproducible verification.
- If the repository already has a validator, extend or run that validator before
  claiming the work is sufficiently checked.
- User instructions override this guide. If the user says not to use TDD, do not
  force it.

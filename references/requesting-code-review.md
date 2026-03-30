# Requesting Code Review

Use this guide when the user asks for a review, audit, or critique of code or a
patch.

## Review Priorities

Focus on:

- correctness bugs
- regressions
- missing tests
- security or data-loss risks
- scope mismatches against the requested behavior

## Response Shape

1. Findings first
2. Order findings by severity
3. Include file and line references whenever possible
4. Keep the summary brief and put it after the findings
5. If there are no findings, say that explicitly and mention residual risks or test
   gaps

## Guardrails

- Do not lead with praise or a general summary.
- Do not spend review budget on cosmetic nits unless they hide a real risk.
- Do not suggest unrelated refactors.
- If you are unsure whether something is truly a problem, say so and explain the
  uncertainty.

# Systematic Debugging

Use this guide for bugs, regressions, failing tests, and unexpected runtime behavior.

## Process

1. Reproduce the failure and capture the exact symptom.
2. Narrow the scope: identify where expected and actual behavior diverge.
3. Trace the control flow, data flow, logs, or state that explains the divergence.
4. Form one concrete hypothesis at a time and test it with evidence.
5. Implement the smallest fix that addresses the confirmed root cause.
6. Verify the original symptom is gone and that nearby behavior still works.

## Guardrails

- Do not patch blindly based on hunches.
- Do not widen the fix before you understand the root cause.
- If there are multiple independent failures, parallelize only when their write scope
  is disjoint.
- After three failed fix attempts or contradictory evidence, pause and revisit the
  assumptions instead of thrashing.

## Expected Outputs

- the reproduced symptom
- the confirmed root cause
- the minimal fix
- the verification evidence

# Finishing Development

Use this guide when implementation is complete and the work needs a final verification
and handoff.

## Process

1. Run the most relevant focused tests plus any broader checks needed for confidence.
2. Summarize what changed, what was verified, and any checks that could not be run.
3. If the repository is under git and the user wants branch hygiene help, prepare the
   next action:
   - suggested branch name
   - suggested commit message
   - suggested PR summary or change summary
4. If git is unavailable or the environment is detached, do not force git commands.
   Provide the human-readable wrap-up instead.

## Guardrails

- Do not claim completion without verification evidence.
- Do not hide unrun tests or unresolved risks.
- Keep helper stage names internal. Tell the user that `super-cower` verified and
  wrapped up the work.

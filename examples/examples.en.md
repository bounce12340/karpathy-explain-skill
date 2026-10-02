# Karpathy × ELI5: three synthetic examples

> These are **synthetic scenarios** that show the skill's output style. They are not findings about any real project, so there are no files or lines to cite and every conclusion should be read as `[inferred]`. In real use, the skill reads the source first and ties conclusions back to files, lines, and tests.
>
> For a real target whose line references are checked by CI, see [real-walkthrough.md](real-walkthrough.md). Traditional Chinese version: [examples.md](examples.md).

## Example 1: a new engineer inherits an API that returns 403

**Request**: "The user is logged in, so why does `GET /reports/42` return 403? Explain it for a new engineer."

**30 seconds**: Logging in is like badging into an office building; a 403 means you are inside the building, but your badge may not open records room 42. Do not confuse "logged in" with "allowed to read this report."

**Diagram**: `request → authenticate → look up the report's owning account → authorization check → 200 or 403`. Whether a missing report returns 404 instead of 403 depends on the actual API contract; the analogy cannot decide that.

**Deep dive**: First confirm the middleware attaches the identity, and that the resource query is scoped to the tenant or owning account. Then check the status-code rules for rejection. Tests should cover at least: your own report, someone else's report, not logged in, and a report that does not exist. **Never** fix the 403 by letting any logged-in user through.

## Example 2: why a frontend draft may disappear

**Request**: "After a failed submit, the draft sometimes disappears. Draw the data flow and tell me where the risk is."

**30 seconds**: Like pressing send on a letter: if the carrier never received it, you cannot throw away your only draft. Wait for the server to confirm, or confirm that a reliable copy exists, before touching the local draft.

**Diagram**: `edit → local draft → submit → {server confirms → clear draft; submit fails → keep draft and notify}`. If there is an offline queue, you must also prove that the queue **actually wrote** the copy.

**Deep dive**: Find where the draft is cleared, the ordering between the network response and local storage, and races from double-clicking submit. Acceptance: with both the network and offline storage failing, the only draft can still be recovered. "Reliable copy" must be defined by testing, not by a function name.

## Example 3: does a red CI mean the code is broken?

**Request**: "Same commit: Node 22 tests time out, Node 24 passes. Help me understand the risk and the next step."

**30 seconds**: Two examiners grade the same exam; one calls time, the other says pass. That alone does not prove the code is right or wrong. First find out whether there is a timing dependency.

**Diagram**: `same SHA → {Node 22: timeout; Node 24: pass} → compare timings, rerun, isolate the test → classify the cause`.

**Deep dive**: Confirm both jobs really tested the same SHA, whether the failure is only a timeout, and whether the test depends on wall-clock time, external services, or parallel load. A passing rerun only suggests flakiness; it does not replace a root cause and does not make the CI "all green."

---

Example request:

> Use karpathy-explain to explain this source code to an engineer who just took it over. Start with a 30-second summary, draw the success and failure paths, then list what is confirmed and what still needs verification, with file and line references: `<source path>`.

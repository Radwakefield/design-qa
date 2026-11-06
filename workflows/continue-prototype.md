# Workflow: Continue a Prototype

Apply the designer's feedback to an existing prototype, or fork a new version to explore a different option.

## Required Reading

1. `references/prototype-build.md`
2. `references/motion-rules.md` (if the change touches animation)
3. `references/rula-tokens.md` (if the feedback names tokens or type styles)

---

## Step 1: Edit in Place, or Fork a Version?

| The designer says | Do |
| --- | --- |
| "change", "make this", "fix", "update", pasted Agentation notes | Edit the current version in place |
| "an option", "explore", "a v2", "what if", "try" | Fork: copy the current version into a new `vN` folder, then edit the copy |
| "add X from v3 to v2" | Port the named change into that version only; diff afterwards to confirm nothing else moved |

When forking, recreate the copied files (read, delete, write) rather than leaving a plain copy. Retitle the page and the controls panel so the versions are easy to tell apart.

## Step 2: Read the Feedback Carefully

For each Agentation note or instruction:

1. **Exact spec given** (CSS properties, sizes, colors): apply it as written. Map raw hex values to Rula tokens.
2. **Spec conflicts with how the element works** (for example a `gap` that would make a stacked label 94px tall): apply the intent, explain the adjustment in one line.
3. **Ambiguous** (a note that repeats another element's spec, "centered" with two possible axes): apply the most likely reading, say which, and offer the other in the wrap-up.
4. **Consistency follow-ons:** if the change should also apply somewhere matching (the selected time should match the selected day), apply it and say so.

## Step 3: Make the Change

- Keep the controls panel accurate: update its copy when behavior changes.
- When behavior is driven by measured heights, keep spacing in padding.
- After any port between versions, diff the two versions and confirm only the intended lines differ.

## Step 4: Verify

Run the verification loop in `references/prototype-build.md`. Check the exact states the feedback was about, plus one neighboring state (the other format, the shortest and longest content).

If the browser can't open the file, stop retrying, give the designer the `open` command, and ask them to check. Say exactly what to look for.

## Step 5: Report

One short list:

- What changed, with the values used
- Any interpretation you made, and the alternative
- What you verified, and anything you couldn't
- Whether packaged handoffs are now out of date

---

## Success Criteria

- [ ] Correct choice of edit in place vs fork
- [ ] Every note applied, interpreted, or questioned explicitly
- [ ] Controls panel copy matches the new behavior
- [ ] Verified, or the designer told exactly what to check
- [ ] Stale handoff packages flagged

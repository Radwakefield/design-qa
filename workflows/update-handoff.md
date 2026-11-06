# Workflow: Update an Existing Build

Engineering already implemented a version. Send their agent only what changed, and catch drift in the real code first.

## Required Reading

1. `references/repo-setup.md` (drift check)
2. `templates/handoff-update.md`

---

## Step 1: Establish the Baseline

The baseline is what engineering built:

- Coming from `workflows/qa-build.md`: the PR's head commit, and the `qa-pr-<n>` prototype's "As built" state.
- Otherwise: the handoff engineering built from, and its snapshot commit. If it has none, ask the designer which version and roughly when.

## Step 2: Drift Check

1. Run the Repo Check from SKILL.md and get the designer to pull.
2. List commits since the baseline on the component folders the handoff names (command in `references/repo-setup.md`).
3. Summarize each relevant commit in one line: what it changes and whether it affects the update. Flag moved files, changed behavior, and the engineer's own implementation if it has landed.

## Step 3: Diff the Prototype

Compare the baseline with the designer's current version (`diff` the two folders, or the files in the old and new bundles). Every intended difference becomes a numbered change. Unintended differences are bugs; fix them first.

## Step 4: Write the Update Doc

Copy `templates/handoff-update.md`. For each change:

- **Before:** what the existing build does
- **After:** what it should do, with exact values
- **Where:** the real files (from a PR, the files it changed)
- **How:** technique and a short sketch, labelled not run

Add one combined section when the changes interact (for example a height calculation several changes feed into), and an acceptance checklist covering only the changed behavior plus anything it could break.

## Step 5: Rebuild the Shareable HTML

Run `scripts/bundle.py` on the current version, overwriting the old shareable file so the engineer has one source of truth. Verify it opens.

## Step 6: Hand Over

Tell the designer which files to send, which old doc still applies, and the drift findings that might need a conversation with engineering. When the baseline is a PR, offer to post the update as a PR comment, only with their go-ahead (it's visible to the team).

---

## Success Criteria

- [ ] Baseline identified (PR head or handoff snapshot)
- [ ] Drift checked on the component folders; relevant commits summarized
- [ ] Every change has before, after, where and how
- [ ] Shareable HTML rebuilt and opening cleanly
- [ ] Designer told what to send and what still applies

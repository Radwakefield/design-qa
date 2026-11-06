# Workflow: QA a Build

The designer pastes a PR or preview link. Turn what engineering built into an editable prototype that matches it, so the designer can jump in and make changes directly. Then send the changes back as an update.

This is not a review report. Don't grade the build or list everything that's missing; get the designer editing the real thing as fast as possible.

## Required Reading

1. `references/repo-setup.md`
2. `references/prototype-build.md`
3. `references/rula-tokens.md`

---

## Step 1: Read the Link

| Link | Do |
| --- | --- |
| GitHub PR (`github.com/<org>/<repo>/pull/<n>`) | Use the GitHub connector to read the PR: title, head branch, base, changed files, and the preview URL if a bot posted one in the comments |
| Preview link (for example `<repo>-pr-<n>.pre.rula…`) | Parse the repo and PR number from the hostname when it follows that pattern; otherwise ask for the PR link once |

Tell the designer in one line which PR and component this is.

## Step 2: Get the Built Code

1. Run the Repo Check from SKILL.md on the PR's repo.
2. Read the PR's version of each changed file with the GitHub connector at the PR's head branch. That's the built state, without the designer switching branches.
3. If the PR has already merged, the designer's pulled `main` has it; read the files locally.

Record the snapshot as the PR's head commit: "Based on `<repo>` PR #`<n>` @ `<short hash>`".

## Step 3: Find the Starting Prototype

Look for an earlier prototype or handoff for this work (the designer's project folder, a `handoff/` folder naming this PR's ticket or component).

| Found | Do |
| --- | --- |
| A prototype version engineering built from | Copy it into a new `qa-pr-<n>` folder, then change the copy to match what the PR actually built (values, spacing, behavior). The designer edits reality, not the old intent |
| Nothing | Build the prototype from the PR's code, following `workflows/start-prototype.md` Step 5, in a new `qa-pr-<n>` folder |

Keep the controls panel. Its first mode is **"As built (PR #`<n>`)"**, so changes can always be compared against what shipped.

## Step 4: Hand It to the Designer

Verify it opens and matches the build (if the preview link loads, compare a screenshot of each against the other). Then tell the designer, briefly:

- Where the prototype is, and that it matches PR #`<n>` as built
- If you spotted a clear mismatch with the earlier prototype while matching the build, list it in one line each (at most a few). Don't go hunting
- To use Agentation (⌘⇧F) to mark changes, or just describe them, and paste them back

## Step 5: Make the Changes

Follow `workflows/continue-prototype.md` for each round of notes, editing the `qa-pr-<n>` version in place. The controls panel's "As built" mode stays as the comparison.

## Step 6: Send It Back

When the designer is done, follow `workflows/update-handoff.md` with the PR's head commit as the baseline. The update doc's "Before" is the PR as built, so every change is phrased as a fix to that PR, and the rebuilt single-file HTML goes with it.

---

## Success Criteria

- [ ] PR and component identified from the link
- [ ] Built code read at the PR's head (no branch switching for the designer)
- [ ] `qa-pr-<n>` prototype matches the build, with an "As built" mode in the controls panel
- [ ] Designer editing within minutes; no review report produced
- [ ] Changes packaged as an update against the PR

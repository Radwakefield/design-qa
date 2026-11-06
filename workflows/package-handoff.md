# Workflow: Package a Handoff

Turn a prototype version into two files: a shareable HTML for the engineer, and a markdown handoff their coding agent can implement.

## Required Reading

1. `references/repo-setup.md` (snapshot and freshness)
2. `references/rula-tokens.md`
3. `templates/handoff.md`

---

## Step 1: Confirm What's Being Packaged

Ask only if unclear: which version, and whether the engineer already built an earlier version. If they did, switch to `workflows/update-handoff.md`.

Run the Repo Check from SKILL.md. If the repo is stale, get the designer to pull, then re-check that the files you'll name still exist (packages and folders move).

## Step 2: Build the Shareable HTML

Create a `handoff/` folder next to the versions. Run the bundling script:

```bash
python3 -I "${CLAUDE_SKILL_DIR}/scripts/bundle.py" "<version folder>" "<handoff folder>/<name>.html" --title "<readable title>"
```

It inlines the CSS and JS, removes Agentation, and keeps the controls panel. Then:

1. Open the output in the browser: one network request (the file itself), no console errors.
2. Click through the key states once.

## Step 3: Write the Agent Handoff

Copy `templates/handoff.md` and fill every section:

1. **Context:** repo, snapshot commit, Figma links, related tickets, which option this is (if there are several).
2. **File map:** every prototype part → the real file. Use paths you confirmed exist at the snapshot.
3. **Behavior and values:** timings, easing, sizes, colors as tokens, states.
4. **Technique:** the approach in numbered steps, without new dependencies where possible.
5. **Code sketch:** short, labelled "not run; verify against the prototype".
6. **Visual spec:** every value the designer set, grouped by component.
7. **Open questions:** decisions engineering should confirm (touch targets, layout moves, content hidden under a fixed button).
8. **Acceptance checklist:** observable checks, including keyboard, reduced motion, rapid clicking, and existing tests.

When there are several options, add a one-line note at the top of each doc naming the other options and what's shared.

## Step 4: Hand Over

Reveal the folder in Finder. Tell the designer:

- Which two files to send, and that the HTML pairs with their video
- That the controls panel can show before/after in the video
- What the engineer needs to decide (the open questions)
- What wasn't verified

---

## Success Criteria

- [ ] Repo fresh; file paths confirmed at the recorded snapshot
- [ ] Single-file HTML opens on its own with no errors
- [ ] Handoff markdown has every template section filled
- [ ] Code sketches labelled as not run
- [ ] Open questions listed
- [ ] Folder revealed and next steps given

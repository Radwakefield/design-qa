# Workflow: Start a Prototype

Build v1 of a prototype that mirrors a real component, with a controls panel for comparing behaviors.

## Required Reading

1. `references/repo-setup.md`
2. `references/prototype-build.md`
3. `references/motion-rules.md` (if anything animates)
4. `references/rula-tokens.md`

---

## Step 1: Setup Questions

Ask up to three at once, skipping any the designer already answered:

1. **Which repo and component?** A GitHub URL, repo name, or the screen it lives on.
2. **What should change?** The behavior or look they want, in their words.
3. **Is there a Figma frame?** A link to the target design, if one exists.

Also ask where the prototype should live. Default to a new folder inside the designer's current project folder, named after the work (for example `Streamline/experiment four`). Never inside the repo clone.

## Step 2: Repo Check

Run the Repo Check from SKILL.md. Record the snapshot (short commit hash and date).

## Step 3: Read the Real Component

1. Find the component: search by visible text from the screen ("Book session"), component names, or file names.
2. Read it and its direct children and styles. Note:
   - The markup and component library in use (for example react-aria `Tabs`)
   - Behavior to preserve (resetting a selection when the parent changes, keyboard handling)
   - **The actual cause of the problem.** For example, a panel swapping instantly because each tab renders its own panel.
   - Existing patterns worth copying (absolutely positioned icons, data attributes for state)
3. Tell the designer what you found in two or three sentences, including the cause, before building.

If the repo has no installed packages, don't try to install or run it. Read only.

## Step 4: Read Figma (if provided)

1. Export the frame as an image and look at it.
2. Pull exact values only for what you need: node effects, named styles, spacing.
3. Sanity-check values that might not render (see Gotchas in SKILL.md). Prefer named design-system styles.

## Step 5: Build v1

Follow `references/prototype-build.md`:

1. Create `index.html`, `styles.css`, `drawer.js` (or a name that fits the component) in the prototype folder.
2. Mirror the real markup and behavior. Use Rula tokens, not guessed colors.
3. Add the controls panel: "Instant swap (current prod)" vs the new behavior, plus duration, easing and slow motion.
4. Add Agentation.
5. Apply `references/motion-rules.md` to any animation.

Tell the designer the plan for the change in a few lines before writing it (what moves, timing, easing, how interruptions behave).

## Step 6: Verify

Run the verification loop in `references/prototype-build.md`: open it, check the console, step through the states that matter, take screenshots. Fix what's wrong before showing the designer.

## Step 7: Hand Over

Tell the designer:

- Where the prototype is and how to open it
- What changed vs production, and what the controls panel compares
- What you verified, and anything you couldn't
- That they can leave notes with Agentation and paste them back

---

## Success Criteria

- [ ] Repo checked for freshness; snapshot recorded
- [ ] Real component read; root cause stated to the designer
- [ ] Prototype outside the repo, mirroring real markup and tokens
- [ ] Controls panel compares current production with the new behavior
- [ ] Agentation loads
- [ ] Verified in a browser, or the designer told exactly what wasn't verified

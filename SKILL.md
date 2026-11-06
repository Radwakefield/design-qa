---
name: design-qa
description: Prototype a UI or interaction change against a real product repo, hand it off to engineering, and QA what engineering builds by turning a PR or preview link into an editable prototype the designer can change directly. Produces a single-file HTML for the engineer and a markdown handoff their coding agent can implement. Use when a designer wants to prototype or rebuild a component from a codebase (a drawer, picker, form, transition), explore options side by side, hand a prototype off to engineering, QA or make design changes to an engineering build from a PR or preview link, or send engineering an update after they've built a version.
argument-hint: "[PR or preview link] or [start | continue | package | update] [repo or prototype folder]"
---

# Design QA

Turn "I want this component to behave differently" into a working prototype that mirrors the real code, and a handoff an engineer's agent can implement without guessing. When engineering has built it, turn their PR into a prototype the designer can edit directly.

**The core insight:** read the real repo, don't run it. Mirror the production component in a throwaway, zero-dependency HTML prototype. Iterate fast there. Then hand engineering exact specs tied to exact files.

## Core Principles

1. **The designer owns git; Claude only reads.** The designer clones and pulls with GitHub Desktop. Claude reads the code and history. (Claude's sandbox can't use the designer's GitHub login or write a repo's `.git` folder, so git writes fail from inside it.)
2. **Pull before reading.** A stale local copy silently produces a prototype of old code. Check the repo's age first, every time.
3. **Each layer has one source of truth.** Figma for intent, the repo for structure and behavior, Rula tokens for values. When they disagree, say which one won and why.
4. **Prototype outside the repo.** The prototype lives in the designer's own folder, never inside the clone, so pulls never conflict.
5. **Make motion judgeable, not describable.** Every prototype gets a controls panel: today's behavior vs the new one, duration, easing, slow motion.
6. **Verify in a real browser after every change.** If verification becomes impossible, say so plainly and hand checking to the designer. Never claim an unseen result works.
7. **Options are versions, not overwrites.** Keep v1, v2, v3 side by side so the designer can compare and engineering can pick.
8. **Two handoffs, two audiences.** The engineer gets a file they can double-click; their agent gets file paths, exact values, technique, and a checklist.

## Mode Detection

| Signal in `$ARGUMENTS` or the request | Mode | Workflow |
| --- | --- | --- |
| A PR link (`github.com/…/pull/…`) or a preview link, alone or with a note | QA a build | [workflows/qa-build.md](workflows/qa-build.md) |
| `start`, a repo name or repo URL, "prototype", "rebuild", "explore how X could work" | Start a prototype | [workflows/start-prototype.md](workflows/start-prototype.md) |
| `continue`, Agentation feedback, "change", "make this", "an option", "v2", "explore" with an existing prototype | Continue a prototype | [workflows/continue-prototype.md](workflows/continue-prototype.md) |
| `package`, "share", "hand off", "send to eng", "for their agent" | Package a handoff | [workflows/package-handoff.md](workflows/package-handoff.md) |
| `update`, "eng already built", "they implemented", "what changed" (no link) | Update an existing build | [workflows/update-handoff.md](workflows/update-handoff.md) |

If the mode is unclear, ask once:

- **QA a build** — paste a PR or preview link and make changes to what engineering built
- **Start a prototype** — new component or interaction, from a repo
- **Continue a prototype** — feedback, edits, or a new option
- **Package a handoff** — send a version to engineering

Use AskUserQuestion with those four options. Plain-text fallback: "Are we (1) QA-ing a build (paste the PR or preview link), (2) starting a prototype, (3) continuing one, or (4) packaging a handoff?" (Update is reached from QA or Package, or by asking for it directly.)

Shortcuts: a PR or preview link goes straight to QA. Pasted Agentation feedback goes straight to Continue. A named repo and component go straight to Start.

## Repo Check (every mode)

Run before reading any code. Details and commands: [references/repo-setup.md](references/repo-setup.md).

1. **Find the clone.** Look in `~/Documents/GitHub/<repo>` (the GitHub Desktop default), then other folders the designer already uses (for example `~/rula-eng/<repo>`). Ask if not found.
2. **Missing →** walk the designer through cloning with GitHub Desktop. Wait for "done" before continuing.
3. **Present →** check its branch, local changes and age with read-only git commands. If it's more than a day old, or not on `main`, ask the designer to switch to `main` and **Fetch origin → Pull** in GitHub Desktop, and wait.
4. **Record the snapshot** (`git rev-parse --short HEAD` and date). It goes into every handoff.

## Gotchas

These are the specific places this workflow fails. Check your own work against them.

- **Don't run `git clone`, `pull` or `fetch` through Bash.** The sandbox blocks the designer's GitHub credentials and writes to `.git`, so it fails and wastes the designer's time. Route git writes to GitHub Desktop (or a designer-approved Terminal-panel command, see repo-setup).
- **Don't read code before checking the repo's age.** In the source session, a two-week-old clone was missing the exact commit the designer asked to start from.
- **Don't run the drift check on single files.** The commit that mattered changed `slots.module.scss`, not the `slots.tsx` the handoff named. Check the component folders, then use `--follow` only to find moved files.
- **Don't suggest cloning into `Documents` from the macOS Terminal app.** Terminal often lacks `Documents` access and fails with "Operation not permitted" or a misleading "directory not empty". GitHub Desktop and Claude's Terminal panel don't have this problem.
- **Don't copy raw Figma effect values without checking they render.** A shadow with a spread larger than its blur (for example `0 -5px 30px -40px`) is invisible in CSS and in Figma. Prefer the named design-system style on the node, and tell the designer.
- **Don't put spacing in margins inside a region whose height you measure or animate.** Margins collapse out of the container, so the animation lands short. Use padding.
- **Don't animate keyboard-initiated changes.** Arrow-key navigation through days or tabs must swap instantly; only pointer actions animate.
- **Don't strip the controls panel from the shareable HTML.** Engineers and the designer's video use it to compare behaviors. Strip Agentation instead.
- **Don't present code sketches as tested.** The repo usually has no installed packages. Label React code "not run; verify against the prototype".
- **Don't turn QA into a review report.** When a designer pastes a PR or preview link, they want to edit what was built, not read a list of what's wrong. Build the "as built" prototype first; mention only clear mismatches, in a line each.
- **Don't make the designer switch branches to QA a PR.** Read the PR's files at its head branch with the GitHub connector instead.
- **Don't silently resolve ambiguous feedback.** If a note repeats another element's spec, or "centered" could mean two axes, apply the most likely reading, say which, and offer the other.
- **Don't keep trying `file://` URLs after Chrome returns `ERR_ACCESS_DENIED`.** It won't recover in-session. Say so, give the designer the `open` command, and ask what they see.
- **Don't add folders or names the designer has to remember.** Use GitHub Desktop's suggested path and the designer's existing project folder.

## Reference Index

| File | Contents | Load when |
| --- | --- | --- |
| [references/repo-setup.md](references/repo-setup.md) | Finding clones, GitHub Desktop clone/pull steps, freshness and drift commands, Terminal-panel fallback | Every mode (Repo Check) |
| [references/prototype-build.md](references/prototype-build.md) | Prototype file layout, controls panel, height-morph technique, Agentation embed, verification loop, versioning | QA, Start, Continue |
| [references/motion-rules.md](references/motion-rules.md) | Motion and interaction quality checks | Start, Continue (any animation) |
| [references/rula-tokens.md](references/rula-tokens.md) | Rula colors, type styles, effect styles | QA, Start, Continue, Package |

## Workflow Index

| Workflow | Purpose |
| --- | --- |
| [workflows/qa-build.md](workflows/qa-build.md) | PR or preview link → an editable prototype matching the build → designer's changes → update |
| [workflows/start-prototype.md](workflows/start-prototype.md) | Repo + Figma + real components → v1 prototype with a controls panel |
| [workflows/continue-prototype.md](workflows/continue-prototype.md) | Apply feedback, or fork a new version for a new option |
| [workflows/package-handoff.md](workflows/package-handoff.md) | Single-file HTML + agent-ready handoff markdown |
| [workflows/update-handoff.md](workflows/update-handoff.md) | Drift check + a doc covering only what changed since engineering's build |

## Templates and Scripts

| File | Use |
| --- | --- |
| [templates/handoff.md](templates/handoff.md) | Skeleton for a full agent handoff |
| [templates/handoff-update.md](templates/handoff-update.md) | Skeleton for a "what changed" update |
| [scripts/bundle.py](scripts/bundle.py) | Inline a prototype's CSS and JS into one shareable HTML file, without Agentation |

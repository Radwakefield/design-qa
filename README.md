# design-qa

A Claude skill for designers: prototype a UI or interaction change against a real product repo, hand it off to engineering in a form their coding agent can implement, and QA what engineering builds by editing it directly.

## What it does

1. **Start:** reads the real component in the repo (and the Figma frame, if any), finds what causes today's behavior, and builds a standalone HTML prototype that mirrors it, with Rula tokens and a controls panel comparing current production with the new behavior.
2. **Continue:** applies Agentation feedback or other notes, and forks side-by-side versions (v2, v3) when you're exploring options.
3. **Package:** produces a single-file HTML for the engineer (pair it with a video) and a markdown handoff for their agent: file map, exact spec, technique, open questions and an acceptance checklist.
4. **QA:** paste a PR or preview link. Claude turns what engineering built into an editable prototype that matches it, so you can jump in and make changes (with Agentation or by describing them). Your changes go back to engineering as an update doc.
5. **Update:** when engineering has built a version and the design has moved on, checks what changed in the code since and writes a doc covering only what's different.

## Install (once per designer)

This repo is private. Ask Rad for access first, and accept the GitHub invite email.

1. Install **GitHub Desktop** (desktop.github.com) and sign in with GitHub.
2. **File → Clone repository**, and search for `Radwakefield/design-qa`.
3. Set **Local Path** to `~/.claude/skills/design-qa`. In the **Choose…** dialog, press ⌘⇧G and paste `~/.claude/skills`, because the `.claude` folder is hidden by default.
4. Click **Clone**, then restart the Claude app (or start a new session). Type `/design-qa` to check it's there.

Or, in one step from the Claude app's Terminal panel (if you use the GitHub CLI):

```bash
gh repo clone Radwakefield/design-qa ~/.claude/skills/design-qa
```

### Updating

Open `design-qa` in GitHub Desktop and click **Fetch origin → Pull**. New sessions pick up the changes.

## Setup for prototyping (once per designer)

1. Clone the product repos you work on in GitHub Desktop: **File → Clone repository**, search, keep the suggested path, **Clone**.
2. If your Mac syncs Desktop & Documents to iCloud, click **Choose…** and clone into a folder outside Documents instead.

## Using it

```
/design-qa start booking-ui — animate the time picker drawer between days
/design-qa continue        (then paste Agentation notes)
/design-qa package v2
/design-qa <PR or preview link>   (QA engineering's build: get an editable copy and make changes)
/design-qa update          (send changes after engineering built a version)
```

Claude also picks it up automatically when you ask to prototype something from a repo, hand a prototype off to engineering, or QA what engineering built.

## What Claude does and doesn't do

- Claude **reads** the repo; you **clone and pull** it in GitHub Desktop. Claude will ask you to pull when your copy is out of date.
- Prototypes live in your own project folder, never inside the repo.
- Claude checks every change in a browser. When it can't, it says so and tells you what to check.

## Files

| Path | Purpose |
| --- | --- |
| `SKILL.md` | Principles, mode routing, repo check, gotchas |
| `workflows/` | QA, start, continue, package, update |
| `references/` | Repo setup and drift, prototype techniques, motion rules, Rula tokens |
| `templates/` | Handoff and update-handoff skeletons |
| `scripts/bundle.py` | Builds the single-file shareable HTML |

## Origin

Distilled from a session rebuilding the Book session time picker drawer in `booking-ui` (animated day-to-time transitions, fixed-height drawer options, handoffs to engineering).

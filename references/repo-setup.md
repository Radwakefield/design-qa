# Repo Setup, Freshness and Drift

How designers get a repo onto their machine, keep it current, and how to detect when the code has moved since a prototype or handoff.

## Who Does What

| Action | Who | How |
| --- | --- | --- |
| Clone | Designer | GitHub Desktop |
| Pull | Designer | GitHub Desktop: Fetch origin → Pull |
| Read code, log, diff, status | Claude | Read-only Bash `git -C <path> …` |
| Remote lookups without a clone (a PR's files, a commit) | Claude | GitHub connector |

Claude's Bash sandbox can't use the designer's GitHub login and can't write to a repo's `.git` folder. Git writes from Bash always fail; don't attempt them.

## Finding a Clone

Check in this order and use the first that exists:

1. `~/Documents/GitHub/<repo>` (GitHub Desktop's default)
2. Folders the designer already uses, for example `~/rula-eng/<repo>`
3. Ask: "Where did you clone `<repo>`? (In GitHub Desktop: Repository → Show in Finder.)"

Confirm it's a git repo with `git -C <path> rev-parse --show-toplevel`.

## Cloning with GitHub Desktop

Give the designer these steps:

1. Install GitHub Desktop from desktop.github.com if needed, and sign in with GitHub.
2. **File → Clone repository**, and search for the repo name (for example `registration`).
3. Keep the suggested **Local Path** (`~/Documents/GitHub/<repo>`). If they have iCloud "Desktop & Documents Folders" sync turned on, click **Choose…** and pick a folder outside Documents, because iCloud syncing a repo is slow and causes conflicts.
4. Click **Clone**, and say "done" when it finishes.

Shortcut: on any repo's GitHub page, **Code → Open with GitHub Desktop** opens the same dialog.

## Freshness Check

Read-only, safe to run from Bash:

```bash
git -C <path> status -sb
```

```bash
git -C <path> log -1 --format="%h · %cr · %s"
```

| Result | Do |
| --- | --- |
| On `main`, clean, under a day old | Proceed |
| Older than a day | Ask the designer: GitHub Desktop → **Fetch origin → Pull**. Wait. |
| On another branch | Ask them to switch to `main` (**Current branch → main**), then pull |
| Local changes | Ask what they are before doing anything; designers shouldn't edit inside the clone |

After the pull, re-run the log command to confirm the hash moved.

## Snapshot

Record for every handoff:

```bash
git -C <path> log -1 --format="%h · %cs"
```

Write it as: "Based on `<repo>` @ `<hash>`, `<date>`."

## Drift Check

**Always check the component folders first, not individual files.** A change often lands in a sibling file (a fix to `slots.module.scss` when the handoff names `slots.tsx`), and a file-level check misses it.

```bash
git -C <path> log --oneline <snapshot>..HEAD -- <component folder one> <component folder two>
```

Then confirm each file the handoff names still exists, and for any that doesn't, find where it went:

```bash
git -C <path> log --oneline --follow <snapshot>..HEAD -- <file>
```

`--follow` only tracks one file at a time, so use it for moved files, not as the main check. Summarize each relevant commit in one line (`git -C <path> show --stat <hash>` shows what it touched), and flag it before building on old assumptions.

## Terminal-Panel Fallback

If the designer prefers not to use GitHub Desktop, propose the command in Claude's Terminal panel. It runs in their own shell with their login, outside the sandbox, and they approve each one.

```bash
gh repo clone <org>/<repo> ~/Documents/GitHub/<repo>
```

```bash
git -C ~/Documents/GitHub/<repo> pull --ff-only
```

- Add the destination path to a `gh repo clone` copied from GitHub's **Code** button; otherwise it clones into the terminal's current folder.
- If `gh` reports they're not signed in, propose `gh auth login` first.
- If the remote uses SSH and the pull fails with "Bad configuration option: usekeychain", prefix the command with `GIT_SSH_COMMAND=/usr/bin/ssh` (Homebrew's SSH rejects Apple's `UseKeychain` option).
- `--ff-only` guarantees the pull never creates a merge.

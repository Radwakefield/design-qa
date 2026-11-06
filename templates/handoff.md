# Handoff: [what changes] ([repo])

**For:** an engineer or coding agent working in `[org/repo]`
**Prototype:** `[file].html` (sent alongside this file; open it in any browser)
**Design:** [Figma link and node]
**Based on:** `[repo]` @ `[short hash]`, [date]
**Related:** [tickets, PRs]

> [Only if there are several options:] This is **option [N]** of [total]. [One line on how the others differ.] Section 2 is shared by all options.

## Goal

[Two or three sentences: the problem today, and what should happen instead.]

The prototype is plain HTML/CSS/JS that copies the markup and behavior of the real components. **Treat it as the source of truth for look and motion.** Its controls panel compares current behavior with the new one and plays it in slow motion. It's a review aid; don't ship it.

## Where this lives

| Prototype part | Real file |
| --- | --- |
| [part] | `[path]` |

Use the existing design-system variables rather than hex values:

| Token | Hex |
| --- | --- |
| `[token]` | `[hex]` |

## 1. [The behavior change]

### Behavior

- **[Trigger]:** [what happens]
- **Keyboard:** [instant, no animation]
- **Interruptions:** [continue from the current value, never snap]
- **Reduced motion:** [what remains]

### Values

| Property | Value |
| --- | --- |
| [property] | [value] |

### Technique

1. [Step]
2. [Step]

### Code sketch (not run; verify against the prototype)

```tsx
// [file] (sketch)
```

## 2. Visual spec

### [Component] (`[file]`)

- **[Element]:** [exact values]

## Open questions

- [Decision engineering should confirm, and why]

## Acceptance checklist

- [ ] [Observable check]
- [ ] Keyboard navigation works without animation
- [ ] Reduced motion: [expected result]
- [ ] Existing tests in `[paths]` still pass; snapshots and selectors updated where markup changed

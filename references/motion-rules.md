# Motion and Interaction Checks

Apply to every animated change. If the `emil-design-eng` skill is installed, load it for depth; these are the checks that mattered in practice.

## Decide First

| Question | Rule |
| --- | --- |
| Is it triggered by the keyboard? | Don't animate. Swap instantly (arrow keys through tabs, days, lists). |
| Will users see it many times a session? | Keep it short and subtle, or skip it. |
| What's its purpose? | It must prevent a jarring jump, show a state change, or confirm an action. "Looks cool" isn't enough. |

## Values

| Element | Duration | Easing |
| --- | --- | --- |
| Drawer, sheet or region height | 200–300ms (300ms default) | `cubic-bezier(0.32, 0.72, 0, 1)` (drawer curve) |
| Content entering | ~220ms, after a ~60ms delay | `cubic-bezier(0.25, 1, 0.5, 1)` |
| Content exiting | ~120ms (faster than entering) | `ease-out` |
| Stagger between rows or items | 30–80ms (35ms default) | — |
| Press feedback | 160ms | `ease-out` on `transform: scale(0.97)` |
| Hover color | 150ms | `ease` |

Never use `ease-in` for UI. It delays the moment the user is watching most closely.

## Implementation Checks

- [ ] CSS **transitions**, not keyframes, for anything that can be re-triggered quickly (transitions retarget mid-flight; keyframes restart).
- [ ] Interruptions continue from the current rendered value; rapid clicking never snaps.
- [ ] Specific properties in `transition`, never `transition: all`.
- [ ] Entering content starts from `opacity: 0` plus a small offset (6px) or `scale(0.95)`, never `scale(0)`.
- [ ] Crossfades blur the outgoing layer slightly (`filter: blur(2px)`) so they read as one change, not two layers overlapping.
- [ ] Hover styles wrapped in `@media (hover: hover) and (pointer: fine)`.
- [ ] `:active { transform: scale(0.97) }` on pressable elements.
- [ ] `prefers-reduced-motion: reduce`: heights snap, movement removed, a short opacity fade allowed.
- [ ] Outgoing content can't be clicked (`pointer-events: none`) and is removed from the DOM afterwards.
- [ ] Focus rings aren't clipped by `overflow` on animated containers (`overflow-clip-margin` or side padding).

## Review Format

When reviewing an existing implementation, report issues in one table:

| Before | After | Why |
| --- | --- | --- |
| `transition: all 300ms` | `transition: height 300ms var(--ease-drawer)` | Name exact properties |

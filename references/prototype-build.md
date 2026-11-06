# Building the Prototype

How to structure a prototype so it mirrors production, iterates fast, verifies reliably and bundles into one shareable file.

## File Layout

```
<project folder>/<work name>/
├── index.html      # Markup mirroring the real component + controls panel + Agentation
├── styles.css      # Rula tokens as CSS variables, then component styles
├── drawer.js       # Data, rendering, behavior (name it after the component)
├── v2/             # A forked option: same three files
└── handoff/        # Shareable HTML + handoff docs (see package-handoff)
```

- **No build step, no packages.** Plain HTML, CSS and JS, so changes show instantly and the bundle is one file.
- **Mirror the real markup:** same element roles, state attributes and structure as the component (for example `role="tab"` with `aria-selected` for a react-aria `Tab`). Use mock data shaped like the real data, and vary it to hit every layout state (1, 2 and 3 rows of times).
- **Tokens first:** declare Rula tokens as CSS variables at the top of `styles.css` (see `rula-tokens.md`), and animation knobs as variables too, so the controls panel can drive them.

## Controls Panel

A dark panel beside the phone frame. It's a review aid, not part of the design, so label it as one.

| Control | Purpose |
| --- | --- |
| Mode radios: "Instant swap (current prod)" vs the new behavior(s) | Before/after comparison, and the designer's video |
| Duration slider | Tune timing live |
| Easing select (drawer curve, strong ease-out, strong ease-in-out, linear) | Compare curves |
| Slow motion ×4 | Inspect choreography; multiply every duration |
| Option toggles (for example "cap drawer at half the map") | Compare a variant without forking |

Write a two-line description at the top of the panel saying what this version does. Update it whenever behavior changes.

## Height-Morph Technique

The reusable way to animate a region between content of different heights, interruptibly:

```js
function morph(viewport, nextLayer, { crossfade, instant = false }) {
  const animate = !instant && state.mode !== 'instant' && !reducedMotion.matches;
  const from = viewport.getBoundingClientRect().height; // correct even mid-transition

  viewport.querySelectorAll('.layer.is-exiting').forEach((el) => el.remove());
  const current = viewport.querySelector('.layer');
  if (!animate || !current) {
    viewport.replaceChildren(nextLayer);
    viewport.style.height = '';
    return;
  }

  viewport.classList.add('is-locked');            // transition: none
  viewport.style.height = `${from}px`;
  if (crossfade) {
    current.classList.add('is-exiting');           // absolute, fades + blurs out
    setTimeout(() => current.remove(), 200);
    nextLayer.classList.add('is-entering');        // items start at opacity 0, translateY(6px)
    viewport.append(nextLayer);
  } else {
    viewport.replaceChildren(nextLayer);
  }
  const to = nextLayer.getBoundingClientRect().height;
  viewport.getBoundingClientRect();                // reflow
  viewport.classList.remove('is-locked');
  viewport.style.height = `${to}px`;
  if (crossfade) requestAnimationFrame(() => nextLayer.classList.remove('is-entering'));

  const release = () => { if (viewport.style.height === `${to}px`) viewport.style.height = ''; };
  if (Math.abs(to - from) < 0.5) release();        // no transitionend will fire
  else viewport.addEventListener('transitionend', (e) =>
    e.target === viewport && e.propertyName === 'height' && release(), { once: true });
}
```

```css
.height-viewport { position: relative; overflow: clip; overflow-clip-margin: 4px;
  transition: height var(--height-duration) var(--height-ease); }
.height-viewport.is-locked { transition: none; }
.layer { padding: 20px 0 16px; }                    /* padding, never margins */
.layer.is-exiting { position: absolute; inset: 0 0 auto; pointer-events: none;
  opacity: 0; filter: blur(2px); transition: opacity 120ms ease-out, filter 120ms ease-out; }
.layer.is-entering .item { opacity: 0; transform: translateY(6px); transition: none; }
```

Stagger entering items with a per-row delay (`calc(60ms + var(--row) * 35ms)`).

## Fixed-Height Containers

When the designer wants a container (a drawer, a sheet) to hold one height while content changes inside it:

1. Compute the target height from its parts: header + footer + body padding + each body child's outer height. For regions mid-animation, count their *target* height (the incoming layer), not the current animated height.
2. Substitute the fixed allowance for the region that varies (for example "always count the time area as two rows").
3. Don't use `scrollHeight` for the body: once the container is taller than its content, it only reports the visible height.
4. Set the height in px with a CSS height transition. Let the body scroll (`overflow-y: auto`) and keep the CTA in a fixed footer outside it.
5. Show the overflow cue (the `lg(-)` shadow on the footer) only while `scrollTop + clientHeight < scrollHeight - 1`. Re-check on scroll and after transitions settle.

## Agentation

Load it from a CDN so the prototype stays dependency-free. Put this before `</body>`:

```html
<div id="agentation-root"></div>
<script type="module">
  import React from 'https://esm.sh/react@18.3.1';
  import { createRoot } from 'https://esm.sh/react-dom@18.3.1/client';
  import { Agentation } from 'https://esm.sh/agentation?deps=react@18.3.1,react-dom@18.3.1';
  createRoot(document.getElementById('agentation-root')).render(React.createElement(Agentation));
</script>
```

Keep the `<!-- Agentation:` comment marker above it; `scripts/bundle.py` uses it to strip the block from shareable files. Tell the designer: press ⌘⇧F (or click the bottom-right button), click an element, leave a note, copy all notes, and paste them back.

## Verification Loop

After every change, using the Chrome DevTools connector:

1. Open the file in a **new background page with its own isolated context**, so the designer's open tab is never disturbed. Resize to about 900×920.
2. Check console errors.
3. Take an accessibility snapshot to get element IDs; click through the states the change affects (shortest and longest content, each format, keyboard navigation).
4. Screenshot the component node rather than the whole page.
5. Close your test pages when done.

Screenshots are slower than most animations, so they show end states. To test mid-animation behavior, turn on slow motion, act, and snapshot immediately: an exiting layer still present proves it animated; its absence proves an instant swap.

If Chrome returns `ERR_ACCESS_DENIED` for the file, stop. Give the designer:

```bash
open "<absolute path to index.html>"
```

and tell them exactly which states to check.

## Versioning

- Fork by creating a `vN` folder and writing fresh copies of the three files (read, then write), not `cp`.
- Retitle the `<title>` and the controls panel per version.
- When porting a change between versions, `diff` the folders afterwards; only the intended lines and the version labels should differ.

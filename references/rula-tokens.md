# Rula Tokens

Values from `@pathccm/rula-ui` and the Rula Figma libraries. In prototypes, declare them as CSS variables. In handoffs, name the token (`$sky-50`, `--rula-ui-sky-50`), not the hex.

If a designer gives a hex value, map it to the matching token below. If it doesn't match one, ask before inventing a new color.

## Color

```css
:root {
  --rula-ui-white: #ffffff;
  --rula-ui-grey-50: #fafafa;
  --rula-ui-grey-100: #f4f5f6;
  --rula-ui-grey-150: #ebedf0;
  --rula-ui-grey-200: #e0e2e6;
  --rula-ui-grey-300: #c1c5cd;
  --rula-ui-grey-400: #969aa0;
  --rula-ui-grey-500: #6a6c71;
  --rula-ui-grey-600: #56575b;
  --rula-ui-grey-700: #3f4146;
  --rula-ui-grey-800: #26272a;
  --rula-ui-grey-900: #15171a;
  --rula-ui-sky-10: #f0faf9;
  --rula-ui-sky-20: #d9ebe9;
  --rula-ui-sky-30: #b7e2e0;
  --rula-ui-sky-40: #57afb0;
  --rula-ui-sky-50: #296662;
  --rula-ui-sky-60: #123331;
}
```

Figma "primitive" names map directly: `--primitive-grey-800` → `--rula-ui-grey-800`.

## Type

Font: **Scto Grotesk A** (fallback `'Inter', -apple-system, sans-serif`). It's installed on designers' Macs, so prototypes render it locally; engineers without it see Inter.

All product styles below use `font-size: 0.875rem; letter-spacing: -0.0175rem`.

| Figma style | Weight | Line height | Typical use |
| --- | --- | --- | --- |
| Product / Paragraph / Small | 400 | 130% | Helper text (timezone notes) |
| Product / Paragraph / Small – Bold | 500 | 130% | Buttons, addresses, slot labels |
| Product / Label (tabs, chips) | 500 | 140% | Toggle labels, day names and dates |

Check whether a `@pathccm/rula-ui` typography mixin matches (`text.paragraphSmall`, `text.paragraphSmallBold`) before writing raw values in a handoff, and confirm its weight: some existing mixins are heavier than current Figma specs.

## Effects

| Style | CSS | Use |
| --- | --- | --- |
| `lg(-)` "foreground of a background w/ overflow" | `box-shadow: 0 -25px 50px -40px rgba(0, 0, 0, 0.25)` | Fixed footer or CTA bar while content scrolls beneath it |

## Component Patterns

| Pattern | Spec |
| --- | --- |
| Selected chip (day, time) | Background `sky-10`, border `sky-50`, text `sky-60` |
| Chip hover (mouse only) | Border `sky-50`, text `sky-60`, no background change |
| Selected chip on hover or focus | Keep the background; only the text darkens (keeps it readable) |
| Segmented toggle | Group: `grey-150`, `padding: 0.25rem`, `gap: 0.25rem`, 8px radius. Selected: white, 6px radius, small shadow. Icon absolutely positioned left of the label so the text stays centered |
| Primary CTA | `sky-50`, full width, 999px radius, 50% opacity when disabled |

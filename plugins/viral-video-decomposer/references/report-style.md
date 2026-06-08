# Viral Video Report Style

Use this style contract when creating full HTML reports for viral-video decomposition.

For exact CSS, reuse or adapt `viral-video-lab.css`. The prose below explains the intent and the parts that should remain stable.

## Design Goal

Build a dense, editorial analysis surface for reviewing and reusing a viral short-video structure. The report should feel like a working lab notebook, not a marketing landing page.

The default report name in the interface is:

- Brand/title: `Viral Video Lab`
- Navigation labels: `Core`, `Shots`, `Blueprint`, `Prompt`
- Style switch: `A` and `B`

## Layout Contract

Use these major sections in order:

1. Sticky topbar with brand, compact navigation, and A/B style switch.
2. Hero with source facts and compact stats.
3. Summary card.
4. Production storyboard compression table.
5. Key-shot contact sheet.
6. Shot-by-shot cards.
7. AI production blueprint card.
8. Variable-slot cards.
9. Agent prompt template.

Do not turn the report into a landing page. Avoid oversized decorative hero layouts, nested cards, ornamental gradients, and explanatory UI copy.

## Style A: Editorial

Style A is the warm editorial default.

- Background: warm off-white paper.
- Typography: serif display brand/headline, clean sans body, mono labels.
- Cards: light panel, thin warm border, small radius, generous but not loose padding.
- Tables: compact, bordered, readable.
- Shot cards: image on the left and metadata on the right on desktop; stacked on mobile.
- Accent: restrained warm red/brown.

Recommended CSS primitives:

```css
:root{
  --paper:#f8f7f4;
  --ink:#161513;
  --muted:#706d68;
  --line:#e4e0d8;
  --panel:#fffdfa;
  --panel-2:#f1eee8;
  --accent:#a33a32;
}
.card,.shot{
  background:rgba(255,253,250,.88);
  border:1px solid var(--line);
  border-radius:12px;
  padding:24px;
  margin:18px 0;
}
```

## Style B: Swiss

Style B is a clean Swiss/editorial variant.

- Background: near-white.
- Typography: Helvetica-style sans, lighter large headings, mono uppercase labels.
- Color: black text with a restrained blue accent.
- Cards and shots: transparent panels with thin gray borders.
- Tables: same module style, with subtle blue top emphasis only where the table already uses it.

Recommended CSS primitives:

```css
body[data-style="swiss"]{
  --paper:#f7f7f5;
  --ink:#050505;
  --muted:#6d6d6d;
  --line:#d9d9d4;
  --panel:#f7f7f5;
  --panel-2:#efefec;
  --accent:#0038b8;
}
body[data-style="swiss"] .card,
body[data-style="swiss"] .shot{
  background:transparent;
  border-color:#d7d7d2;
}
```

## Locked Decisions From The Accepted Report

Keep these decisions stable unless the user explicitly asks for a redesign:

- Topbar brand remains `Viral Video Lab`, not a Chinese descriptive title.
- A/B versions use the same report structure and differ only through theme CSS.
- The `AI 生产蓝图` module uses the same `.card` style as adjacent modules in both A and B. Do not give it a custom dark panel or special blue outline.
- The key-shot overview uses a tight contact sheet. Avoid large gutters or tall row spacing.
- Mobile topbar should stay compact: hide nav, keep brand and A/B switch in one row, target about `56px` height.
- All screenshots must use relative paths under `visual/` from the report HTML.

## Contact Sheet Guidance

For reports with many keyframes, create a compact contact sheet rather than stacking screenshots.

Recommended defaults:

- 7 columns for about 35-45 shots.
- Gap: 4-8 px.
- Thumbnail width: about 140-155 px.
- Label strip: short shot id and timecode only.
- Keep the image aspect ratio wide enough that the report page does not become excessively long.

## HTML Requirements

- Use a single self-contained HTML file, except frame images under `visual/`.
- Use local relative image paths such as `visual/S001.png` and `visual/contact_sheet.jpg`.
- Include a small script that stores the selected style in `localStorage`.
- Use stable IDs for navigation: `overview`, `shots`, `blueprint`, `prompt`.
- Avoid changing accepted style details during content-only updates.

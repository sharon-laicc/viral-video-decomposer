# Viral Video Report Style

Use this style contract when creating full HTML reports for viral-video decomposition.

This is a locked product style, not an inspiration board. For exact CSS, inline or copy `viral-video-lab.css`. Do not "improve", "modernize", or replace it unless the user explicitly requests a redesign.

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

Do not add extra visible modules after the Agent prompt unless the user explicitly asks. In particular, do not add a visible `JSON Brief（机器可读）` section to the HTML report; the JSON brief is delivered as a separate `.json` file.

## Required DOM Contract

The generated HTML MUST contain these structural pieces:

```html
<body data-style="editorial">
  <nav class="topbar">
    <div class="topbar-inner">
      <div class="brand">Viral Video Lab</div>
      <div class="nav">
        <a href="#overview">Core</a>
        <a href="#shots">Shots</a>
        <a href="#blueprint">Blueprint</a>
        <a href="#prompt">Prompt</a>
      </div>
      <div class="style-switch" aria-label="切换报告样式">
        <button type="button" data-style-option="editorial" aria-pressed="true">A</button>
        <button type="button" data-style-option="swiss" aria-pressed="false">B</button>
      </div>
    </div>
  </nav>
  <main>
    <header class="hero">...</header>
    <section class="card" id="overview">...</section>
    <section class="card">生产分镜压缩表...</section>
    <section class="card" id="shots"><img class="sheet" src=".../contact_sheet.jpg"></section>
    <section class="shot"><img src=".../S001.png">...</section>
    <section class="card" id="blueprint">AI 生产蓝图...</section>
    <section class="card">变量槽...</section>
    <section class="card" id="prompt"><pre>...</pre></section>
  </main>
</body>
```

Class names are part of the visual system. Do not rename `.topbar-inner`, `.brand`, `.nav`, `.style-switch`, `.hero`, `.stats`, `.stat`, `.card`, `.shot`, `.sheet`, `.grid`, `.mini`, or the style-switch attributes.

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
- All screenshots must use local relative paths from the report HTML. The default folder is `<report-slug>-visual/` when the report is placed in the same output directory.

## Evidence Asset Contract

Full HTML reports must display visual evidence. Do not omit images.

Required files:

- `contact_sheet.jpg`: compact overview of sampled frames.
- `S001.png`, `S002.png`, ...: shot-card images used by the shot sections.

Recommended folder shape:

```text
outputs/
  xhs-example_图文拆解报告.html
  xhs-example_拉片拆解.md
  xhs-example_video_generation_brief.json
  xhs-example-visual/
    contact_sheet.jpg
    S001.png
    S002.png
```

The HTML should reference those files like:

```html
<img class="sheet" src="xhs-example-visual/contact_sheet.jpg" alt="关键镜头总览">
<img src="xhs-example-visual/S001.png" alt="S001">
```

Before delivery, check every `img src` path exists relative to the HTML file. If source extraction is blocked and no real frame can be captured, do not ship a final `*_图文拆解报告.html`; ship a draft analysis or ask for the video/screenshots. Placeholder-only shot panels are not valid visual evidence.

## Shot-By-Shot Depth Contract

`Shot-by-Shot` in the HTML report means frame-backed shot cards, not a broad outline.

- Do not merge multiple visible cuts into one card.
- Do not label guessed narrative chunks as final shot-by-shot analysis.
- For slow continuous footage, create a new card at each meaningful action beat or every 3-5 seconds.
- For 20-60s videos, expect roughly 10-25 shot cards unless the footage is truly static.
- For 60-120s videos, expect roughly 18-45 shot cards unless the footage is truly static.
- Every shot card must include a real `<img src=".../S###.png">` image.
- The contact sheet should include the same `S###` sequence shown in the shot cards.

## Contact Sheet Guidance

For reports with many keyframes, create a compact contact sheet rather than stacking screenshots.

Recommended defaults:

- 7 columns for about 35-45 shots.
- Gap: 4-8 px.
- Thumbnail width: about 140-155 px.
- Label strip: short shot id and timecode only.
- Keep the image aspect ratio wide enough that the report page does not become excessively long.

## HTML Requirements

- Use a single self-contained HTML file, except frame images in the sibling `<report-slug>-visual/` directory.
- Use local relative image paths such as `xhs-example-visual/S001.png` and `xhs-example-visual/contact_sheet.jpg`.
- Include a small script that stores the selected style in `localStorage`.
- Use stable IDs for navigation: `overview`, `shots`, `blueprint`, `prompt`.
- Avoid changing accepted style details during content-only updates.

## Anti-Drift Rules

These outputs are considered incorrect:

- A report whose CSS resembles a generic card dashboard instead of `viral-video-lab.css`.
- A topbar with Chinese-only product names such as `爆款视频拆解台` instead of `Viral Video Lab`.
- Missing A/B switch, missing Swiss B theme, or changing the switch to tabs that navigate away.
- Missing contact sheet or missing shot images when frames are available.
- Placeholder-only shot panels such as `.shot-placeholder` instead of real frame images.
- A visible `JSON Brief（机器可读）` module inside the HTML report.
- A long video compressed into a few broad narrative chunks while calling the section `Shot-by-Shot`.
- `AI 生产蓝图` styled differently from neighboring `.card` modules.
- Big screenshot gutters that make the `关键镜头总览` section excessively tall.
- Mobile topbar wrapping into multiple rows or becoming visually taller than about 56px.

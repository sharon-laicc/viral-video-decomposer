---
name: video-structure-analyzer
description: 拆解爆款短视频、Vlog、小红书/抖音/B站视频、广告素材或竞品视频时使用。用于把视频链接、截图、录屏、字幕、逐字稿或参考视频拆成镜头级拉片表、爆款机制、可复用结构、批量选题变量、脚本/分镜/prompt，以及给后续视频生成 agent 使用的 JSON brief。也适用于用户说“分析爆款视频”“拆视频”“拉片”“拆解短视频”“复刻这种视频结构但不要抄”“根据爆款批量产出视频方案”等场景。
metadata:
  short-description: 拆解爆款视频并生成生产 brief
---

# Video Structure Analyzer

Use this skill as the pre-production researcher for video-generation agents. The goal is not only to explain why a video works, but to produce reusable, original, machine-readable production specs.

## Core Rule

Analyze methods, structure, rhythm, and production logic. Do not copy protected expression. Avoid reproducing exact scripts, distinctive shot sequences, watermarks, creator identity, brand identity, or proprietary assets unless the user owns them or explicitly asks for analysis-only commentary.

## Non-Negotiable Report Fidelity

When the user asks for an HTML report, the report is not a free-design task. You MUST reproduce the accepted `Viral Video Lab` report system exactly enough that a user can recognize it as the same product:

- Load `references/report-style.md` before writing HTML.
- Inline or copy the exact CSS from `references/viral-video-lab.css`; do not replace it with a new visual system.
- Keep the interface name `Viral Video Lab`.
- Keep the same A/B switch behavior, labels, navigation, module order, spacing scale, card treatment, table treatment, shot-card grid, mobile topbar behavior, and `AI 生产蓝图` module styling.
- Do not invent a new hero, color palette, card style, Chinese title bar, marketing landing page, decorative gradients, special blueprint panel, or unrelated template.
- Content may change per video; layout and visual system should remain stable.

## Input Modes

**Primary mode: Video URL only** - Users should only need to provide a video link. The skill automatically handles video download and processing.

Accepted video sources:

- **Xiaohongshu (小红书)**: Direct link or video ID
- **Douyin (抖音)**: Direct link or video ID
- **Bilibili**: Direct link or video ID
- **YouTube**: Direct link or video ID
- **TikTok**: Direct link or video ID
- **Kuaishou (快手)**: Direct link or video ID
- **Instagram**: Direct link or video ID
- **Ad libraries**: Direct link

Alternative inputs (when video link is unavailable):

- Local video file upload (for testing or when link is blocked)
- Screenshots or screen recordings
- Transcript, SRT/VTT subtitles, or OCR text
- Existing analysis notes

**Important**: Users should NOT need to manually download or upload videos. The skill should automatically:
1. Accept the video URL
2. Download the video using appropriate tools (yt-dlp, ffmpeg, browser automation, etc.)
3. Extract frames and metadata
4. Generate the analysis report

If a platform blocks direct download, the skill should:
- Attempt multiple download methods
- Fall back to browser automation if needed
- Use screenshots or metadata as alternatives
- Clearly state any limitations in the output

## Workflow

1. Capture source facts:
   Title, creator/account, platform, URL, duration, visible engagement metrics, publish date if available, product/category, and any extraction limitations.

2. Extract usable evidence:
   **Automatic video download**: Use `yt-dlp`, `ffmpeg`, or browser automation to automatically download the video from the provided URL. Do not ask the user to upload the video file.
   
   Extraction priority:
   1. Attempt automatic download using `yt-dlp` (supports most platforms)
   2. If blocked, try `ffmpeg` with URL directly
   3. If still blocked, use browser automation to capture video
   4. Extract frames using `ffmpeg` or `ffprobe`
   5. Extract subtitles/transcripts if available
   6. For blocked web video, sample screenshots at meaningful timestamps
   
   Always record the extraction method used in the source facts.

   For full HTML reports, evidence images are required. Create a sibling visual directory for every report, named with the same slug plus `-visual`, for example:

   - `xhs-smelly-cat_图文拆解报告.html`
   - `xhs-smelly-cat-visual/contact_sheet.jpg`
   - `xhs-smelly-cat-visual/S001.png`
   - `xhs-smelly-cat-visual/S002.png`

   The HTML must reference those local relative files. A final `*_图文拆解报告.html` must use real frame images, not decorative placeholders. If frames cannot be extracted, do not pretend the report is complete: create a clearly labeled draft analysis or ask the user for the video file/screenshots, and state that a final HTML report requires visual evidence. Do not silently omit the screenshot/contact-sheet modules.

3. Build the shot-level table:
   The table is the main output. Include timecode, duration, visual, shot size, action, subtitle/dialogue summary, sound, camera angle, camera movement, transition, emotional function, narrative function, and generation prompt.

   For full reports, `Shot-by-Shot` means actual shots/cuts, not broad narrative chunks. Do not compress a long video into 6-8 generic sections unless the user explicitly asks for a compressed outline. When real frames are available:

   - Create one `S###` row/card per visible cut or meaningful continuous action beat.
   - For slow continuous footage, sample at least every 3-5 seconds.
   - For 20-60s videos, expect roughly 10-25 shots unless the video is truly static.
   - For 60-120s videos, expect roughly 18-45 shots unless the video is truly static.
   - Every shot card in the HTML should have a matching real image file.
   - If exact frames are unavailable, do not invent precise timecodes; label the section as a reconstructed outline instead of final shot-by-shot.

4. Segment the narrative:
   Group shots into sections such as Hook, setup, proof, reveal, contrast, routine block, escalation, payoff, summary, CTA. Name the section by its job, not by vague labels.

5. Explain the viral mechanism:
   Identify hook type, curiosity gap, emotional driver, information density, rhythm, visual density, trust signals, audience fantasy/pain, repeatable meme or comment trigger, and conversion move.

6. Convert analysis into production assets:
   Produce reusable templates, variables, batch variants, script options, shot prompts, caption rules, BGM/SFX guidance, platform adaptations, and a `video_generation_brief.json`-style object.

7. Add originality guardrails:
   List what can be reused at the pattern level and what must be changed to avoid copying.

## Required Outputs

For quick requests, answer inline with these sections:

- Source facts
- One-paragraph thesis
- Shot-level table or compressed shot table
- Viral mechanism
- Reusable production template
- Batch variants or next-video ideas
- JSON brief

For substantial requests, create files in the working project:

- `*_拆解报告.html` or `*_拆解报告.md`
- `*_拉片拆解.md`
- `*_video_generation_brief.json`
- Required for HTML reports: a `*-visual/` directory containing `contact_sheet.jpg` plus sampled frame images named `S001.png`, `S002.png`, etc. Use `visual/contact_sheet.jpg` paths only when the HTML itself lives inside the same parent directory and the folder is actually named `visual`.

When producing HTML reports, read `references/report-style.md` and follow that style contract as a hard requirement. Prefer a dense professional analysis surface, not a marketing landing page. The accepted default is a `Viral Video Lab` report with source facts, stats, contact sheet, shot cards, production table, AI blueprint, variable slots, prompt template, and an A/B visual style toggle.

Do not include a visible `JSON Brief（机器可读）` module inside the HTML report unless the user explicitly asks to display raw JSON in the web page. The JSON brief belongs in the separate `*_video_generation_brief.json` file. The HTML should include `Agent Prompt Template`, not raw machine JSON.

The `AI 生产蓝图` module should use the same module/card styling as adjacent sections in both A and B themes unless the user explicitly asks for a special treatment.

For key-shot overviews, generate a compact contact sheet with tight gutters. Do not use large screenshot row gaps that make the report excessively long.

## Shot Table Schema

Use this table unless the user asks for another format:

| 排序 | 镜号 | 时间码 | 时长秒 | 画面 | 景别 | 内容/动作 | 台词/字幕 | 声音 | 摄像机角度 | 镜头运动 | 转场 | 情绪功能 | 叙事功能 | 生成提示词 |
|---|---|---|---:|---|---|---|---|---|---|---|---|---|---|---|

For fast analysis, compress to:

| 镜号 | 时间码 | 画面/动作 | 台词/字幕摘要 | 情绪功能 | 叙事功能 | 可复用生成提示 |
|---|---|---|---|---|---|---|

## JSON Brief

For the complete JSON contract and detailed heuristics, read `references/output-contract.md` when generating machine-readable assets.

Minimum JSON object:

```json
{
  "source": {},
  "analysis_summary": "",
  "viral_pattern": {},
  "shots": [],
  "production_template": {},
  "batch_variants": [],
  "originality_guardrails": []
}
```

## User Experience

**Minimal user input required**: Users should only provide:
1. Video URL (or video ID)
2. (Optional) Specific analysis focus or output format

**Automatic handling**:
- Video download
- Frame extraction
- Subtitle/transcript retrieval
- Metadata collection
- Report generation

**No file upload needed** unless:
- The video URL is blocked and user provides local file as fallback
- User wants to analyze multiple videos at once

## Quality Bar

- Be concrete: prefer "0-3s close-up of messy desk, abrupt zoom, anxiety hook" over "strong opening".
- Preserve timing: timecodes and durations matter because later agents need executable pacing.
- Treat empty shots as meaningful: B-roll, pauses, object close-ups, and transition shots often carry rhythm and emotion.
- Separate human-readable insight from machine-readable production specs.
- If evidence is incomplete, mark confidence and avoid pretending exact frame timing is known.
- **Automatic video handling**: Always attempt to download video from URL automatically. Only ask for file upload if automatic download fails after all retry methods.
- Before delivering an HTML report, verify that the HTML contains: `.topbar-inner`, `.brand` with `Viral Video Lab`, `.style-switch`, `body[data-style="swiss"]`, `#overview`, `#shots`, `#blueprint`, `#prompt`, a contact-sheet `<img>`, and at least one shot card image when frames are available.
- Before delivering an HTML report, verify that every local `<img src="...">` path resolves relative to the HTML file. Broken image references are a failed output.
- Before delivering an HTML report, verify that it does not contain placeholder-only shot panels, a visible `JSON Brief（机器可读）` section, or compressed narrative beats mislabeled as final shot-by-shot analysis.
- If possible, run `references/validate_report.py <report.html>` before final delivery. If it fails, fix the report instead of presenting it as complete.

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

## Input Modes

Accept any available source:

- Video URL from Xiaohongshu, Douyin, Bilibili, YouTube, Kuaishou, TikTok, Instagram, or an ad library.
- Local video, screen recording, screenshots, contact sheet, transcript, SRT/VTT, OCR text, or existing notes.
- Multiple videos when the user wants a pattern library or batch production template.

If a platform blocks direct download, use browser inspection, screenshots, transcript/OCR, page metadata, or manually sampled keyframes. State the limitation in the output.

## Workflow

1. Capture source facts:
   Title, creator/account, platform, URL, duration, visible engagement metrics, publish date if available, product/category, and any extraction limitations.

2. Extract usable evidence:
   Prefer direct transcript/subtitles and frame sampling. If available, use `ffmpeg`/`ffprobe` for duration and keyframes. For blocked web video, sample screenshots at meaningful timestamps and record the method.

3. Build the shot-level table:
   The table is the main output. Include timecode, duration, visual, shot size, action, subtitle/dialogue summary, sound, camera angle, camera movement, transition, emotional function, narrative function, and generation prompt.

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
- Optional `contact_sheet.jpg` and sampled frame images

When producing HTML reports, read `references/report-style.md` and follow that style contract. Prefer a dense professional analysis surface, not a marketing landing page. The accepted default is a `Viral Video Lab` report with source facts, stats, contact sheet, shot cards, production table, AI blueprint, variable slots, prompt template, and an A/B visual style toggle.

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

## Quality Bar

- Be concrete: prefer "0-3s close-up of messy desk, abrupt zoom, anxiety hook" over "strong opening".
- Preserve timing: timecodes and durations matter because later agents need executable pacing.
- Treat empty shots as meaningful: B-roll, pauses, object close-ups, and transition shots often carry rhythm and emotion.
- Separate human-readable insight from machine-readable production specs.
- If evidence is incomplete, mark confidence and avoid pretending exact frame timing is known.

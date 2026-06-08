# Output Contract

Load this reference when producing a full report, JSON brief, or batch production plan.

## Evidence Notes

Always record:

- `extraction_method`: direct video, downloaded file, browser screenshots, transcript only, screenshots only, mixed.
- `confidence`: high, medium, or low.
- `limitations`: blocked playback, missing audio, no exact timestamps, OCR uncertain, sampled keyframes only.

## Viral Pattern Fields

Use these fields when relevant:

```json
{
  "hook_type": "反常识 | 痛点反问 | 结果先行 | 冲突悬念 | 情绪共鸣 | 视觉奇观 | 身份代入",
  "emotion_driver": "焦虑/好奇/爽感/陪伴/羡慕/信任/松弛",
  "audience_promise": "观众看完会获得什么",
  "curiosity_gap": "开头埋下但暂不解释的信息差",
  "rhythm": "快切/三段式/日常流/递进证明/反转",
  "visual_density": "低/中/高，以及原因",
  "trust_signals": ["真实截图", "过程展示", "前后对比", "身份背书"],
  "comment_trigger": "会促使评论区讨论的问题或立场",
  "conversion_move": "关注/收藏/私信/评论领取/购买/品牌记忆"
}
```

## Shot Object

```json
{
  "shot_id": "S001",
  "timecode": "00:00-00:03",
  "duration_sec": 3,
  "visual": "",
  "shot_size": "特写 | 近景 | 中景 | 全景 | 屏录 | 空镜",
  "action": "",
  "dialogue_or_caption": "",
  "sound": {
    "voice": "",
    "music": "",
    "sfx": "",
    "silence_or_pause": ""
  },
  "camera": {
    "angle": "",
    "movement": ""
  },
  "transition": "",
  "emotional_function": "",
  "narrative_function": "",
  "generation_prompt": "",
  "confidence": "high"
}
```

## Production Template

```json
{
  "duration_target": "30-45s",
  "structure": [
    {
      "section": "Hook",
      "time_range": "0-3s",
      "job": "制造信息差",
      "required_shots": 2,
      "rules": ["结果先行", "字幕不超过14字", "第一秒必须有视觉变化"]
    }
  ],
  "caption_rules": [],
  "voiceover_rules": [],
  "visual_rules": [],
  "sound_rules": [],
  "platform_adaptations": {
    "xiaohongshu": "",
    "douyin": "",
    "bilibili": ""
  }
}
```

## Batch Variants

Each variant should be original at the topic and expression level:

```json
{
  "topic": "",
  "target_audience": "",
  "angle": "",
  "hook": "",
  "script_outline": [],
  "shot_plan": [],
  "risk_notes": ""
}
```

## Originality Guardrails

Separate reusable patterns from non-reusable expression:

- Reuse: structure, pacing, emotional job, content category, shot role, variable slots.
- Change: exact wording, distinctive jokes, creator persona, unique life details, brand marks, original footage, exact shot order when it is highly distinctive.
- Transform: replace topic, setting, examples, visual assets, phrasing, CTA, and proof materials.

## Report Shape

When generating an HTML report, also load `report-style.md` and preserve the accepted `Viral Video Lab` A/B report style.

Recommended full report content:

1. 视频基础信息
2. 提取方式与置信度
3. 一句话核心判断
4. 完整逐字稿或字幕摘要
5. 镜头级拉片表
6. 段落结构拆解
7. 台词与画面关系
8. 情绪曲线
9. 爆款机制归纳
10. 可复用脚本模板
11. 批量生成变量表
12. 给视频生成 agent 的 JSON brief

Recommended HTML module order:

1. Hero/source facts and compact stats
2. 总结
3. 生产分镜压缩表
4. 关键镜头总览
5. 镜头级拆解卡片
6. AI 生产蓝图
7. 变量槽
8. Agent Prompt Template

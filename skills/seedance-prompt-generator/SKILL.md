---
name: seedance-prompt-generator
description: Convert Chinese storyboard scripts, shot lists, advert scripts, MV scripts, product demos, video extension notes, or multimodal reference plans into Seedance 2.0-ready video prompts. Use when the user provides a分镜表/拉片表/镜头脚本 with fields like 时间戳、时长、分镜内容、人物主体、环境道具、景别、镜头角度、运镜、色调光线、声音、对白字幕、转场、脚本功能, or asks to write/optimize 即梦 Seedance 2.0 prompts using @图片/@视频/@音频 references.
---

# Seedance Prompt Generator

## Workflow

1. Read the user's storyboard, shot list, reference assets, and desired generation length.
2. If the user provides a table-like storyboard, preserve shot order and merge rows into one coherent prompt unless they explicitly ask for per-shot prompts.
3. Map each shot's fields into Seedance 2.0 prompt clauses:
   - `时间戳/时长` -> time-coded segments such as `0-3秒：...`.
   - `分镜内容/脚本功能` -> core visual event and narrative/product purpose.
   - `人物/主体` -> exact subject identity and consistency requirement.
   - `环境/道具` -> scene, prop, product, material, brand text, and placement.
   - `景别/镜头角度/运镜/转场` -> camera grammar and continuity.
   - `色调/光线` -> visual style, lighting, texture, mood.
   - `背景音/音效/音乐/对白/字幕` -> audio, dialogue, voice tone, captions.
4. Use explicit `@图片1`, `@图1`, `@视频1`, `@音频1` references when assets are supplied or implied. Say what each asset controls:首帧、尾帧、主体形象、材质、场景、运镜、动作、表情、音色、BGM、转场节奏.
5. Keep the prompt in natural Chinese, direct and production-oriented. Avoid abstract intent without visual instructions.
6. Include practical Seedance constraints only when useful: generated duration should be 4-15s; multimodal work should normally use 全能参考; only首帧图+prompt can use 首尾帧入口; uploaded files are addressed with `@素材名`; do not rely on写实真人脸素材 because the platform may reject it.

## Output Format

Return:

```markdown
推荐生成时长：X秒
入口建议：全能参考 / 首尾帧
素材引用：
- @图片1：...
- @视频1：...

Seedance 2.0 提示词：
...

可选负向/约束：
...
```

If the user only needs the prompt, return only the final prompt.

## Prompting Rules

- Prefer time-coded segments for scripts longer than one beat: `0-3秒`, `3-6秒`, `6-10秒`.
- For one-shot or continuous camera work, say `全程不要切镜头，一镜到底` and describe the camera path.
- For reference videos, specify which attributes to copy: `参考@视频1的运镜、画面切换节奏、动作、表情、转场、音效/BGM`.
- For product videos, name product identity, hero shots, material proof points, scale, use scenario, logo/text placement, and final tagline.
- For edits or extensions, name the source video and whether to extend forward/backward or change a specific subject/action while preserving the rest.
- For dialogue, write the exact spoken lines and speaker names; for voice, specify accent, emotion, tempo, or `音色参考@视频1`.
- For subtitle or brand text, quote the exact on-screen text and describe when/how it appears.
- Remove table bookkeeping that Seedance does not need, but keep useful intent from `脚本功能` as visual emphasis.

## Reference

For detailed patterns, templates, and representative examples distilled from the Seedance 2.0 manual, read `references/seedance-2-prompt-guide.md`.

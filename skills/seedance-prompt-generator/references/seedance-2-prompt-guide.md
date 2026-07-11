# Seedance 2.0 Prompt Guide

This reference distills the local manual "即梦 Seedance 2.0 使用手册" into reusable prompt patterns.

## Platform Facts

- Inputs: text plus image/video/audio references.
- Image input: up to 9 files; video input: up to 3 files, total 2-15s; audio input: up to 3 files, total <=15s.
- Generated duration: 4-15s.
- Mixed input total: up to 12 files.
- Use `@素材名` to bind assets to roles: `@图片1作为首帧`, `@视频1参考运镜`, `@音频1用于配乐`.
- Use 全能参考 for multimodal prompts. Use 首尾帧 when only first/last frame style input is needed.
- Uploaded写实真人脸素材 may be blocked. Prefer illustrated, CG, product, animal, object, or non-identifiable references when possible.

## Core Formula

Write prompts in this order:

1. Task type: generate, edit, extend, replace, reference, one-shot, music beat, product demo.
2. Asset role mapping: what each `@图片/@视频/@音频` controls.
3. Time structure: exact beats or continuous camera path.
4. Subject and action: who/what changes, exact movement, expression, physical interaction.
5. Scene and props: environment, product, material, text, logo, spatial layout.
6. Camera language: shot size, angle, movement, lens/effect, transition, continuity.
7. Visual style: color, lighting, texture, mood, realism/animation style.
8. Audio: BGM, sound effects, voice tone, dialogue, captions.
9. Constraints: no cut, keep character/product consistent, do not change source content except specified part, keep text exact.

## Storyboard Table Mapping

For a table like:

`序号 / 时间戳 / 时长 / 分镜内容 / 人物主体 / 环境道具 / 景别 / 镜头角度 / 运镜 / 色调光线 / 背景音音效音乐 / 对白旁白字幕 / 转场镜头衔接 / 脚本功能`

Convert each row into:

`{时间段}：{景别+角度+运镜}，{主体在环境/道具中的具体动作}，{光线色调}，{声音/对白/字幕}，{转场}`。

Then add a final sentence that binds the whole video:

`整体保持{风格/产品一致性/节奏}，每个镜头衔接自然，重点突出{脚本功能合并后的卖点/情绪/剧情目标}。`

## Common Templates

### Simple First-Frame Generation

`@图片1作为首帧，{主体}在{场景}中{连续动作}。镜头{运镜}，{景别/角度}，{光线/风格}。背景音为{音效/BGM}，画面出现字幕“{文字}”。`

### Multimodal Reference

`@图片1参考主体形象，@图片2参考场景，@视频1参考运镜和动作节奏，@音频1参考BGM。{时间段脚本}。保持主体外观一致，动作连贯自然。`

### Reference Video Recreation

`参考@视频1的所有运镜、画面切换节奏和转场，用@图片1中的{主体}进行复刻。{主体}在{场景}中{动作/剧情}，画面风格为{风格}，音效为{音效}。`

### One-Shot / Continuous Camera

`全程不要切镜头，一镜到底。@图片1作为首帧，镜头从{起点}开始，{推/拉/摇/移/环绕/跟随}到{路径节点1}，再过渡到{节点2}，最终停在{终点/产品/角色表情}。`

### Video Extension

`将@视频1延长{X}秒。{0-X秒分段脚本}。延长部分要承接原视频的构图、光线、人物/产品状态和运动方向，衔接自然。`

### Targeted Video Edit

`在@视频1基础上，仅将{对象/动作/剧情}改为{新内容}，其余场景、镜头节奏和画面风格保持一致。{具体时间段或动作描述}。`

### Product Advertisement

`@图片1作为产品主体，@图片2参考材质/侧面/使用场景，生成{时长}秒商业广告。{时间段脚本}。重点展示{卖点1、卖点2、卖点3}，最后画面出现品牌/广告语“{文案}”。`

### Dialogue / Audio

`{角色A}用{情绪/口音/语速}说：“{台词}”。{角色B}回应：“{台词}”。背景音乐为{风格}，关键动作加入{音效}。如有参考音色，写“音色参考@视频1”。`

### Music Beat / MV

`@图片1-@图片N根据@视频1中的画面关键帧和音乐节奏进行卡点，镜头在每个强拍切换/推进/闪切。整体{风格}，画面张力强，可根据音乐补充景别和光影变化。`

## Representative Prompt Patterns From The Manual

- `参考@视频1的所有转场和运镜，一镜到底，画面以棋局为起始...无缝渐变转场...镜头拉远...一镜到底。`
- `对@图片2的包包进行商业化的摄像展示，包包的侧面参考@图片1，表面材质参考@图片3，要求将包包细节均有所展示，背景音恢宏大气。`
- `把@图片1作为画面的首帧图，第一人称视角，参考@视频1的运镜效果，上方/左边/右边场景分别参考@图片2/@图片3/@图片4。`
- `参考@图1的男人形象，他在@图2的场景中，完全参考@视频1的所有运镜效果和主角面部表情...`
- `参考视频1的人物动作，参考视频2的环绕运镜镜头语言，生成角色1和角色2的打斗场面...`
- `将@视频1的人物换成@图片1，@图片1为首帧，参考@视频1的运镜...从第三人称视角变成人物主观视角...`
- `由@图片1的天花板开始，参考@视频1的拼图破碎效果进行转场，“BELIEVE”字体替换成“Seedance”，参考@图2的字体。`
- `参考@图片1的专题片分镜头脚本，参考分镜、景别、运镜、画面和文案，创作一段15s的...片头。`
- `将@视频1延长15秒。1-5秒：... 6-10秒：... 11-15秒：...`
- `固定镜头...参考@视频1的鱼眼镜头，让@视频2中的主体看向鱼眼镜头，参考@视频1中的说话动作，背景BGM参考@视频3中的音效。`
- `@图片1@图片2@图片3@图片4@图片5，一镜到底的追踪镜头，从...最终...`
- `颠覆@视频1的整个剧情。0-3秒：... 3-6秒：... 6-9秒：...`
- `@图片1-@图片7中的图片根据@视频中的画面关键帧的位置和整体节奏进行卡点...可根据音乐及画面需求自行改变景别并补充光影变化。`

## Quality Checklist

- Every referenced asset has a role.
- Each time segment contains a visible action, camera instruction, and audio/text instruction when needed.
- Product/character consistency is explicit.
- Desired transition type is explicit: hard cut, match cut, no cut, seamless morph, fade, black screen, beat cut.
- Text to appear on screen is quoted exactly.
- Dialogue is assigned to speakers.
- The prompt does not contradict Seedance duration/input limits.

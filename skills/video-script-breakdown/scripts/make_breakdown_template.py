#!/usr/bin/env python3
"""生成视频脚本拆解或拉片分析的 Markdown 模板。"""

from __future__ import annotations

import argparse
from pathlib import Path


COLUMNS = [
    "时间码",
    "镜头",
    "人物",
    "环境/道具",
    "动作",
    "景别/构图",
    "运镜",
    "转场/剪辑",
    "字幕/包装",
    "音频/BGM",
    "色调/光线",
    "节奏功能",
    "复刻建议",
]


def build_table(shots: int) -> str:
    header = "| " + " | ".join(COLUMNS) + " |"
    separator = "| " + " | ".join(["---"] * len(COLUMNS)) + " |"
    rows = []
    for index in range(1, shots + 1):
        row = [""] * len(COLUMNS)
        row[1] = f"{index:02d}"
        rows.append("| " + " | ".join(row) + " |")
    return "\n".join([header, separator, *rows])


def build_document(title: str, shots: int, mode: str) -> str:
    sections = [
        f"# {title}",
        "",
        "## 项目概览",
        "",
        "- 输入类型:",
        "- 平台/比例:",
        "- 目标受众:",
        "- 核心情绪:",
        "- 参考风格:",
        "",
        "## 结构拆解",
        "",
        "- 开头钩子:",
        "- 信息铺垫:",
        "- 冲突/转折:",
        "- 高潮/记忆点:",
        "- 收束/CTA:",
        "",
        "## 分镜拉片表",
        "",
        build_table(shots),
        "",
        "## 结构规律",
        "",
        "- 重复模式:",
        "- 节奏变化:",
        "- 视听语言:",
        "- 爆点机制:",
        "",
    ]

    if mode in {"remake", "full"}:
        sections.extend(
            [
                "## 复刻方案",
                "",
                "- 可直接复用:",
                "- 需要本土化/品牌化:",
                "- 不建议照搬:",
                "- 素材清单:",
                "- 剪辑配方:",
                "",
                "## AI 视频提示词",
                "",
                "| 镜头 | 图像/视频提示词 | 负面约束 | 连贯性锚点 |",
                "|---|---|---|---|",
                *[f"| {index:02d} |  |  |  |" for index in range(1, shots + 1)],
                "",
            ]
        )

    sections.extend(
        [
            "## 制作风险",
            "",
            "- 难拍/难生成镜头:",
            "- 连贯性风险:",
            "- 字幕与画面冲突:",
            "- 音频版权/风格风险:",
            "- 需要补充确认:",
            "",
        ]
    )
    return "\n".join(sections)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--shots", type=int, default=12, help="要生成的镜头行数。")
    parser.add_argument("--mode", choices=["script", "lapian", "remake", "full"], default="full")
    parser.add_argument("--title", default="视频脚本拆解与拉片分析")
    parser.add_argument("--output", help="输出 Markdown 文件路径；不传时打印到终端。")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.shots < 1:
        raise SystemExit("--shots 必须大于等于 1")
    document = build_document(args.title, args.shots, args.mode)
    if args.output:
        Path(args.output).write_text(document, encoding="utf-8")
    else:
        print(document)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

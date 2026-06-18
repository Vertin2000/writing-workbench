"""init_workbench.py — 把 6 层空骨架拷贝到目标目录。

只做两件事：
1. 验证 / 创建目标目录
2. 把 ../assets/meta-skeleton/ 整树拷过去

不接受 blueprint / components 参数。所有项目专属内容由 AI 在 Skill 工作流中
现场生成，不走脚本。
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


SKELETON_DIR = Path(__file__).resolve().parent.parent / "assets" / "meta-skeleton"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Initialize a writing workbench (6-layer meta-skeleton).",
    )
    p.add_argument(
        "--target",
        required=True,
        help="Target directory to scaffold (will be created if missing).",
    )
    p.add_argument(
        "--force",
        action="store_true",
        help="Allow scaffolding into a non-empty directory (overwrites conflicts).",
    )
    return p.parse_args()


def ensure_target(target: Path, force: bool) -> None:
    if target.exists():
        if not target.is_dir():
            sys.exit(f"[ERROR] Target exists but is not a directory: {target}")
        has_content = any(target.iterdir())
        if has_content and not force:
            sys.exit(
                f"[ERROR] Target directory is not empty: {target}\n"
                f"        Pass --force to scaffold anyway (will overwrite "
                f"conflicting files)."
            )
    else:
        target.mkdir(parents=True, exist_ok=True)


def copy_skeleton(target: Path) -> list[Path]:
    if not SKELETON_DIR.is_dir():
        sys.exit(f"[ERROR] Skeleton source missing: {SKELETON_DIR}")

    written: list[Path] = []
    for src in SKELETON_DIR.rglob("*"):
        rel = src.relative_to(SKELETON_DIR)
        dst = target / rel
        if src.is_dir():
            dst.mkdir(parents=True, exist_ok=True)
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            written.append(dst)
    return written


def main() -> None:
    args = parse_args()
    target = Path(args.target).resolve()

    ensure_target(target, args.force)
    written = copy_skeleton(target)

    print(f"[OK] Scaffolded writing workbench at: {target}")
    print(f"     Layers: 00_Context / 01_Workflow / 02_Modules / "
          f"03_DataRoom / 04_Drafts / 05_Checklists")
    print(f"     Files written: {len(written)}")
    print()
    print("Next: AI runs Step 4-5 (Context / 结构策略 / Modules 切分) and fills in")
    print("project-specific content per writing-workbench skill workflow.")


if __name__ == "__main__":
    main()

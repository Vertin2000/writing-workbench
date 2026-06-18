# Writing Workbench

Writing Workbench is an agent skill for long-form writing projects that need to survive large context, many source materials, multiple draft modules, and multi-session iteration.

It does not teach an agent what to write. It gives the agent and the writer a project workspace that keeps context, source material, module briefs, drafts, and checklists separate and traceable.

## What It Creates

The skill scaffolds a six-layer writing workspace:

```text
00_Context/      Small, stable context loaded before every module
01_Workflow/     Writing order, dependencies, and module call template
02_Modules/      One task brief per writing module
03_DataRoom/     Large source material loaded only when named
04_Drafts/       Versioned module drafts
05_Checklists/   Module checks and whole-document consistency checks
```

The core workflow is:

1. Capture intent.
2. Inventory all context, files, rules, and missing material.
3. Partition every inventory item into Context, Modules, or DataRoom.
4. Split project context and writing modules.
5. Scaffold the workspace.
6. Fill briefs and write drafts module by module.
7. Verify drafts against module and whole-document checklists.

The important part is traceability: every source item has a place, every module has a brief, and every draft can be checked against explicit acceptance criteria.

## When To Use It

Use this skill for writing projects that meet at least two of these conditions:

- substantial input material, such as notes, reports, data, rules, worldbuilding, or source documents
- substantial output, such as chapters, sections, scenes, reports, proposals, or multi-part deliverables
- multi-turn iteration, especially when work will continue across sessions

Do not use it for one-off emails, short copy, simple edits, or quick Q&A.

## Quick Start

Install or copy the `writing-workbench/` folder into your agent's skills directory. Then ask your agent to use the skill for a long-form writing project.

To initialize a workspace manually:

```powershell
python writing-workbench/scripts/init_workbench.py --target ./my-writing-project
```

The script only copies the empty six-layer skeleton. Project-specific files are created by the agent during the skill workflow, after intent, inventory, partition, and module splitting are clear.

## Example

See [`examples/mini-report-workbench`](examples/mini-report-workbench/) for a small, synthetic example of how Inventory, Partition, and Checklists work together.

## 中文说明

Writing Workbench 是一个面向长上下文写作项目的 Agent Skill。它的目标不是替你规定内容模板，而是把素材、上下文、模块任务书、草稿和验收清单分层管理，让长文项目在多轮会话里不散架。

它特别适合论文、报告、标书、长篇创作、技术文档、法律/政策分析等多素材、多章节、多轮迭代的写作任务。

## License

Apache-2.0

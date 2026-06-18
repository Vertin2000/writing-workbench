# Writing Workbench

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3-3776AB.svg)](https://www.python.org/)

Stop losing context across long writing projects. Writing Workbench turns a long-form task into a traceable six-layer workspace.

Writing Workbench is an agent skill for projects that need to survive many source materials, modular drafts, and multi-session iteration.

It does not tell an agent what to write. It gives the agent and the writer a project workspace that keeps context, source material, structure choices, module briefs, drafts, and checklists separate and traceable.

## What It Creates

The skill scaffolds a six-layer writing workspace:

```text
00_Context/      Source-backed compressed context loaded before every module
01_Workflow/     Structure strategy, writing order, dependencies, and module call template
02_Modules/      One task brief per writing module
03_DataRoom/     Large source material loaded only when named
04_Drafts/       Versioned module drafts
05_Checklists/   Module checks and whole-document consistency checks
```

The core workflow is:

1. Capture intent.
2. Inventory all context, files, rules, and missing material.
3. Partition every inventory item into Context, Modules, or DataRoom.
4. Split project context into source-backed Context files.
5. Compare structure strategies, then choose the reader-facing structure and production order.
6. Scaffold the workspace.
7. Fill briefs and write drafts module by module.
8. Verify drafts against module and whole-document checklists.

The important part is explicit traceability: every compressed context item points back to a source, every structure choice is written down, every module has a brief, and every draft can be checked against acceptance criteria.

## When To Use It

Use this skill for writing projects that meet at least two of these conditions:

- substantial input material, such as notes, reports, data, rules, worldbuilding, or source documents
- substantial output, such as chapters, sections, scenes, reports, proposals, or multi-part deliverables
- multi-turn iteration, especially when work will continue across sessions

Do not use it for one-off emails, short copy, simple edits, or quick Q&A.

## Quick Start

Install or copy the `writing-workbench/` folder into your agent's skills directory. Then ask your agent to use the skill for a long-form writing project.

With the `skills` CLI:

```bash
npx skills add https://github.com/Vertin2000/writing-workbench/tree/main/writing-workbench
```

To initialize a workspace manually:

```powershell
python writing-workbench/scripts/init_workbench.py --target ./my-writing-project
```

The script only copies the empty six-layer skeleton. Project-specific files are created by the agent during the skill workflow, after intent, inventory, partition, structure strategy, and module splitting are clear.

## Example

The examples illustrate the workflow mechanics, not default report structures.

- [`examples/mini-report-workbench`](examples/mini-report-workbench/) is a bilingual concept example of structure strategy, Inventory, Partition, and Checklist iteration.
- [`examples/full-report-workbench-zh`](examples/full-report-workbench-zh/) is a full synthetic Chinese workbench with source-backed Context, Workflow, Modules, DataRoom, Drafts, and Checklists.
- [`examples/full-report-workbench-en`](examples/full-report-workbench-en/) is an English guide to the full Chinese example.

Start with [`examples/full-report-workbench-zh`](examples/full-report-workbench-zh/) for a complete Chinese-language report workbench. It shows how Context, Workflow, Modules, DataRoom, Drafts, and Checklists work together across a full project.

## Community

GitHub Discussions are open for questions, example workbenches, and notes on what you used the framework to write.

## 中文说明

Writing Workbench 是一个面向长上下文写作项目的 Agent Skill。它不替你规定内容模板；它把素材、上下文、模块任务书、草稿和验收清单分层管理，让长文项目在多轮会话里不散架。

它特别适合论文、报告、标书、长篇创作、技术文档、法律/政策分析等多素材、多章节、多轮迭代的写作任务。

## License

Apache-2.0

# Full Report Workbench Guide

This guide explains the Chinese full example in [`../full-report-workbench-zh`](../full-report-workbench-zh/). The example is synthetic, but it is shaped like a real long-form report project.

## Scenario

Team Alpha needs to write a management review report after eight simulated operating stages. The report must explain:

- what changed in the numbers
- how decisions changed across stages
- how the team moved from ad hoc judgment to a reusable checklist
- what the next iteration should preserve or improve

The Chinese example keeps the full six-layer Writing Workbench structure. It does not include source project files, real names, real data, slides, documents, images, or tool scripts.

## Reading Order

Start here:

1. `../full-report-workbench-zh/README.md`
2. `../full-report-workbench-zh/00_Context/00_项目简报.md`
3. `../full-report-workbench-zh/00_Context/03_素材归类与对账.md`
4. `../full-report-workbench-zh/01_Workflow/章节写作看板.md`
5. `../full-report-workbench-zh/04_Drafts/模拟经营复盘报告_v1.md`
6. `../full-report-workbench-zh/05_Checklists/全篇一致性.md`

## What This Example Shows

`00_Context/` keeps stable facts small and loaded before every module. The example separates project purpose, data rules, style rules, and inventory reconciliation.

`01_Workflow/` defines the writing order and the standard module call pattern.

`02_Modules/` gives each report section a brief: position, required material, minimum deliverable, boundaries, and checklist path.

`03_DataRoom/` stores source-like material by index. The example uses a tiny synthetic metrics table, available as both CSV and Markdown.

`04_Drafts/` contains a compact sample draft that demonstrates how a report can cite the workbench without repeating the same facts mechanically. It also shows the placeholder conventions used by the skill: `[SOURCE]`, `[DATA GAP]`, and `[DEFER]`.

`05_Checklists/` turns review into an explicit acceptance step. The whole-document checklist includes a rule for key numbers and fact restatement: the same fact may appear in multiple places, but each appearance should serve a different narrative purpose. The foundation checklist checks whether the workbench itself is still healthy.

## Why The Example Is Mostly Chinese

The original workflow was designed for Chinese long-form writing. Keeping the full example in Chinese preserves the native shape of the task: file names, module briefs, style constraints, and acceptance checklists. This English guide gives non-Chinese readers enough context to inspect the structure without maintaining two full translations.

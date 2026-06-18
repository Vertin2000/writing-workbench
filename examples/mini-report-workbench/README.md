# Mini Report Workbench Example

This example uses synthetic material to show how Writing Workbench keeps a small report project traceable. It is not a full generated workspace; it shows the decisions an agent should make before scaffolding.

这个迷你示例使用合成材料，说明 Writing Workbench 在脚手架生成前怎样做结构判断、素材归类和验收清单迭代。它不是完整工作台，只保留最小概念样本。

## Intent

Write a short internal review report about a six-week pilot program.

- Audience: project owner and team leads
- Output: executive summary, stage review, risks, next actions
- Source material: weekly notes, final metrics table, team feedback
- Iteration: draft first, revise after stakeholder comments

中文对应：

- 目标读者：项目负责人和团队负责人
- 产出形态：执行摘要、阶段复盘、风险、下一步行动
- 素材来源：周记录、最终指标表、团队反馈
- 迭代方式：先写初稿，再根据利益相关方反馈修订

## Structure Strategy / 结构策略

Before splitting modules, the agent should compare a few plausible structures instead of assuming the first outline is right.

| Option | Reader-facing structure | Production order | Trade-off |
| --- | --- | --- | --- |
| Result-first memo | Summary → stage review → risks → next actions | stage review → summary → risks → next actions | Fast for busy owners; summary should wait until facts are stable. |
| Timeline review | week-by-week review → metrics → risks → next actions | stage review → metrics → risks → summary | Good for diagnosis; slower for readers who need the answer first. |
| Action-led note | next actions → evidence → risks | risks → stage review → next actions | Useful for urgent decisions; may hide the learning process. |

Recommended choice: result-first memo, with production starting from the stage review. The final reading order and the actual writing order are intentionally different.

中文对应：切模块前，AI 应先比较几种可能结构，而不是默认作者的第一版提纲就是最佳答案。本例推荐“结果先行”的成稿结构，但实际写作从阶段复盘开始，因为事实稳定后再写摘要更稳。

## Inventory

1. Pilot goal and success definition
2. Target audience and tone
3. Weekly notes
4. Final metrics table
5. Team feedback
6. Required sections
7. Terms to use consistently
8. Known missing data: support workload by week

Inventory item total: 8

中文对应：Inventory 只列素材和规则，不急着整理。这里共有 8 项，包括试点目标、读者与语气、周记录、指标表、团队反馈、必写章节、术语和缺失数据。

## Partition

### 00_Context

- Pilot goal and success definition
- Target audience and tone
- Required sections
- Terms to use consistently

### 02_Modules

- Executive summary: depends on final metrics table and stage review findings
- Stage review: depends on weekly notes and final metrics table
- Risks and next actions: depends on team feedback and missing support workload data

### 03_DataRoom

- Weekly notes
- Final metrics table
- Team feedback
- Known missing data: support workload by week

Inventory item total: 8
Classified items: 8
Unclassified items: 0

中文对应：Partition 把每一项 Inventory 显式归到 `00_Context`、`02_Modules` 或 `03_DataRoom`。最后必须对账：总数 8，已归类 8，未归类 0。

## Checklist Iteration

After the first draft, the team notices that the same final metric appears in the executive summary and stage review with nearly identical wording. This is not a factual error, but it makes the report feel repetitive.

Add this whole-document consistency check:

> Key numbers and fact restatement: the same number or fact may appear in the summary, body, and review sections, but each appearance should serve a different narrative purpose. Avoid repeating the same number with the same sentence pattern across sections. Rewrite, merge, cross-reference, or add a new comparison angle when needed.

This is the value of `05_Checklists`: each real project can discover a new acceptance dimension and preserve it for the next writing pass.

中文对应：第一版草稿后，团队发现同一个关键数字在摘要和阶段复盘里用几乎相同句式重复出现。这不是事实错误，但会让报告显得机械。把这个发现固化进 `05_Checklists`，工作台下一轮就会更好用。

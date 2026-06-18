# Mini Report Workbench Example

This example uses synthetic material to show how Writing Workbench keeps a small report project traceable. It is not a full generated workspace; it shows the decisions an agent should make before scaffolding.

## Intent

Write a short internal review report about a six-week pilot program.

- Audience: project owner and team leads
- Output: executive summary, stage review, risks, next actions
- Source material: weekly notes, final metrics table, team feedback
- Iteration: draft first, revise after stakeholder comments

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

## Checklist Iteration

After the first draft, the team notices that the same final metric appears in the executive summary and stage review with nearly identical wording. This is not a factual error, but it makes the report feel repetitive.

Add this whole-document consistency check:

> Key numbers and fact restatement: the same number or fact may appear in the summary, body, and review sections, but each appearance should serve a different narrative purpose. Avoid repeating the same number with the same sentence pattern across sections. Rewrite, merge, cross-reference, or add a new comparison angle when needed.

This is the value of `05_Checklists`: each real project can discover a new acceptance dimension and preserve it for the next writing pass.

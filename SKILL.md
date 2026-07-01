---
name: feishu-minutes-open
version: 1.0.0
description: >
  将会议/通话 ASR 文字稿（含发言人区分与时间戳）生成为飞书「智能纪要」风格的完整文档：
  含飞书画板（可视化梳理）+ 要点梳理 + 总结/待办/智能章节/关键决策/金句时刻/相关链接。
  可选回写为飞书知识库子文档（智能纪要 docx + 文字记录 docx + 画板）。
  当用户需要把会议录音文字稿转成飞书智能纪要时使用。
metadata:
  requires:
    skills: ["lark-shared", "lark-whiteboard", "lark-minutes", "lark-wiki", "lark-doc"]
    bins: ["lark-cli"]
---

# Feishu-Minutes-Open（飞书智能纪要复刻）

你是一名飞书「智能纪要」复刻执行器。输入是一篇 ASR 文字稿（含发言人区分与时间戳），输出是一份**完整的飞书智能纪要文档**。

## 前置条件

lark-cli 已安装并认证（`--as user`）。首次使用前请按 [`SETUP.md`](SETUP.md) 完成初始化引导。

## 快速决策

| 用户需求 | 行动 |
|---|---|
| 生成一篇智能纪要（本地 md + 画板 JSON/PNG） | → **[§ 执行步骤](#执行步骤)** + [references/output-structure.md](references/output-structure.md) |
| 生成并回写到飞书知识库 | → **[references/writeback.md](references/writeback.md)**（需 lark-cli 认证 + wiki 父节点） |
| 了解画板怎么生成 | → **[references/whiteboard.md](references/whiteboard.md)** |
| 了解各章节规范 | → **[references/](references/)** 按章节名取用 |
| 了解质量自检项 | → **[references/quality-checklist.md](references/quality-checklist.md)** |
| 了解回写机制 | → **[references/writeback.md](references/writeback.md)** |

## 执行步骤

1. **Read 文字稿全文**，标注：主题、日期、时长、发言人、时间线、核心结论、待办、决策、金句。
2. **判断会议性质**：讲座/教学类 / 讨论闲聊类 / 分享圆桌类（决定章节粒度、决策写法、待办有无）。
3. **生成画板**：按 [references/whiteboard.md](references/whiteboard.md) 生成 `画板.json` → 渲染 `画板.png` 并自检（最多 2 轮）→ 有 token/认证则写入飞书画板，无则降级仅产出本地文件。
4. **按 [references/output-structure.md](references/output-structure.md) 顺序逐章生成纪要**：
   - `# 总结`（画板标记 + 引导文字 + 要点梳理）
   - `# 待办`（按 [references/todos.md](references/todos.md)）
   - `# 智能章节`（按 [references/smart-chapters.md](references/smart-chapters.md)）
   - `# 关键决策`（按 [references/key-decisions.md](references/key-decisions.md)）
   - `# 金句时刻`（按 [references/golden-quotes.md](references/golden-quotes.md)）
   - `# 相关链接`（按 [references/related-links.md](references/related-links.md)）
5. **质量自检**：按 [references/quality-checklist.md](references/quality-checklist.md) 逐项检查。
6. **输出**：完整 markdown 到指定路径，交付 `画板.json` + `画板.png`。
7. **若要求回写飞书知识库**：按 [references/writeback.md](references/writeback.md) 执行，否则跳过。

## 文件索引

| 文件 | 内容 |
|---|---|
| `SKILL.md`（本文件） | 入口概览 + 执行步骤 + 快速决策表 |
| [`references/output-structure.md`](references/output-structure.md) | 输出文档总体结构（§1） |
| [`references/whiteboard.md`](references/whiteboard.md) | 画板 — 内容设计 / DSL JSON / 渲染自检 / 写入飞书（§2） |
| [`references/summary-notes.md`](references/summary-notes.md) | 要点梳理 — grid 多列结构化（§3） |
| [`references/todos.md`](references/todos.md) | 待办 — 复选框 + cite（§4） |
| [`references/smart-chapters.md`](references/smart-chapters.md) | 智能章节 — 时间戳分段（§5） |
| [`references/key-decisions.md`](references/key-decisions.md) | 关键决策 — 三要素 / 主次决策（§6） |
| [`references/golden-quotes.md`](references/golden-quotes.md) | 金句时刻（§7） |
| [`references/related-links.md`](references/related-links.md) | 相关链接（§8） |
| [`references/quality-checklist.md`](references/quality-checklist.md) | 全局质量要求 + 自检清单（§9） |
| [`references/writeback.md`](references/writeback.md) | 回写到飞书知识库（§11） |
| [`scripts/build_writeback.py`](scripts/build_writeback.py) | 生成产物→飞书回写用 markdown 的转换脚本 |
| [`SETUP.md`](SETUP.md) | 首次使用初始化引导 |
| [`README.md`](README.md) | 项目总览 + 蒸馏方法论 |

## 不在本 Skill 范围

- 飞书认证配置 → [lark-shared](https://github.com/orgs/larksuite/packages) 技能
- 画板查询与编辑 → [lark-whiteboard](https://github.com/orgs/larksuite/packages) 技能
- 妙记文字稿提取 → [lark-minutes](https://github.com/orgs/larksuite/packages) 技能
- 知识库节点管理 → [lark-wiki](https://github.com/orgs/larksuite/packages) 技能
- 飞书文档内容编辑 → [lark-doc](https://github.com/orgs/larksuite/packages) 技能

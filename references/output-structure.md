# 输出文档总体结构

## 输入文字稿格式

- 第 1 行：`<开始时间> | <时长>`，例如 `2026-06-18 08:00:44 CST|1h 21min 31s`。从中提取**日期**与**起止时间**用于纪要头部。
- `Keywords:` 行：ASR 提取的关键词，作为把握主题的线索（不必原样输出）。
- 正文分段：`Speaker X HH:MM:SS.mmm ` 后跟该发言人该时段转写文本，发言人之间空行分隔。
  - 发言人编号是 ASR 区分的，不一定是真实姓名。纪要里引用"说话人 1""说话人 2"即可，**不要**臆造姓名。
  - 时间戳是生成"智能章节"分段与链接的依据。

## 输出章节顺序

严格按以下顺序输出。每个大章节用 `# ` 一级标题。章节之间空两行。整篇文档以 `<title>` 开头。

**格式硬规则**：
- 第 1 行**必须**是 `<title>智能纪要：{主题} {日期}</title>`（用标签包裹，不是纯文本标题）。
- **每个一级章节**（`# 总结`、`# 待办`、`# 智能章节`、`# 关键决策`、`# 金句时刻`、`# 相关链接`）的正文结束后、下一个章节前，**必须**放一个空行加 `<readonly-block type="isv"></readonly-block>`（这是飞书纪要的渲染分隔标记）。

```
<title>智能纪要：{主题} {日期}</title>

<引用块：录音主题 / 录音时间>

> 智能纪要由 AI 生成，可能不准确，请谨慎甄别后使用
```

**头部格式硬规则**：
- **录音时间格式**统一为：`{YYYY年M月D日}（{周X}）{开始HH:MM} - {结束HH:MM}（GMT+08）`（如"2026年5月1日（周五）13:48 - 14:39（GMT+08）"）。开始时间从文字稿第 1 行取，结束时间=开始时间+时长。**禁止**用"YYYY-MM-DD HH:MM:SS CST｜时长 Xmin"等其它格式。
- **`<title>` 主题措辞**：从文字稿内容归纳，≤20字，名词性短语，优先采用文字稿本身出现的主题表述（如标题/开场白点题），不要自加副标题（如"XX分享+现场问答"）。

```
# 总结
<whiteboard 画板（见 references/whiteboard.md）>
<一段引导文字>
<grid 多列要点梳理（见 references/summary-notes.md）>

<readonly-block type="isv"></readonly-block>



# 待办
（见 references/todos.md）

<readonly-block type="isv"></readonly-block>



# 智能章节
（见 references/smart-chapters.md）

<readonly-block type="isv"></readonly-block>



# 关键决策
（见 references/key-decisions.md，若无真正决策则输出"无关键决策"说明）

<readonly-block type="isv"></readonly-block>



# 金句时刻
（见 references/golden-quotes.md，若无金句可省略整章，则该章及其 readonly-block 都不出现）

<readonly-block type="isv"></readonly-block>



# 相关链接
（见 references/related-links.md）
```

> 章节取舍：待办/智能章节/相关链接几乎必有；金句时刻仅当文字稿中确有合适金句时才输出（含其 readonly-block），没有就整章省略。关键决策的处理见 references/key-decisions.md——分享/圆桌类会议也要保留该章节但标注"无关键决策"。

<div align="center">

<!-- ════════════════════════════════════════════════════════════ -->
<!--  Banner Hero 区域                                            -->
<!-- ════════════════════════════════════════════════════════════ -->

<img src="banner.png" alt="Smart-Minutes-Open Banner" width="100%">

<br/>

**无需飞书 AI 会员，把会议文字稿变成飞书「智能纪要」级专业文档。**

<!-- 多语言链接 -->
[📖 English](./README.md) · [📖 中文](./README.zh.md) · [🚀 Quick Start](./SETUP.md)

<!-- Shields 多行布局 -->
<p>
  <a href="https://github.com/YunfanGoForIt/Smart-Minutes-Open/stargazers">
    <img src="https://img.shields.io/github/stars/YunfanGoForIt/Smart-Minutes-Open?style=flat-square&logo=github&color=FFD700&label=Stars" alt="stars">
  </a>
  <a href="https://github.com/YunfanGoForIt/Smart-Minutes-Open/network/members">
    <img src="https://img.shields.io/github/forks/YunfanGoForIt/Smart-Minutes-Open?style=flat-square&logo=github&color=00B96B&label=Forks" alt="forks">
  </a>
  <a href="https://github.com/YunfanGoForIt/Smart-Minutes-Open/issues">
    <img src="https://img.shields.io/github/issues/YunfanGoForIt/Smart-Minutes-Open?style=flat-square&logo=github&color=FF6B6B&label=Issues" alt="issues">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-00B96B?style=flat-square&logo=open-source-initiative&logoColor=white" alt="license">
  </a>
</p>
<p>
  <img src="https://img.shields.io/badge/Claude%20Code-Skill-8A2BE2?style=flat-square&logo=anthropic&logoColor=white" alt="claude-code">
  <img src="https://img.shields.io/badge/飞书-lark--cli-3370FF?style=flat-square&logo=lark&logoColor=white" alt="lark">
  <img src="https://img.shields.io/badge/status-active-00B96B?style=flat-square" alt="status">
  <img src="https://img.shields.io/badge/PRs-welcome-00B96B?style=flat-square" alt="prs">
</p>

<p>
  <em>"飞书 AI 会员太贵额度太少，我蒸馏了一个平替。"</em><br/>
  <em>"Feishu's AI plan is pricey and quota-tight — so I distilled an open replacement."</em>
</p>

</div>

---

## 🌟 一句话介绍

> **Smart-Minutes-Open** 是一个 Claude Code Skill，将会议/通话 ASR 文字稿生成为与飞书「智能纪要」同等风格的完整文档：
> **画板速览 + 要点梳理 + 待办/智能章节/关键决策/金句时刻/相关链接**，可选回写为飞书知识库子文档。
>
> **无需飞书 AI 会员。只需一篇文字稿。**

---

## 🚀 快速开始

```bash
# 1. 安装飞书 CLI
npm install -g @larksuite/cli
lark-cli config init

# 2. 安装本 skill
# 把本目录放到 Claude Code 的 ~/.claude/skills/smart-minutes-open/ 下

# 3. 提取文字稿
lark-cli minutes +detail --minute-tokens <token> --transcript

# 4. 触发生成
# 在 Claude Code 中把文字稿路径发过去，说"生成智能纪要"即可
```

📖 详细初始化步骤见 [`SETUP.md`](SETUP.md)

---

## 🎙️ 如何获取 ASR 文字稿

这个 Skill 的输入是一篇**带发言人区分 + 时间戳的 ASR 文字稿**。如果你还没有文字稿，下面两条路径任选其一。

### 方案 A：用飞书妙记（推荐，已在飞书生态内的用户）

飞书妙记自带**录音转文字**能力，无需任何额外工具：

- **免费用户**：每月 **300 分钟**免费转写额度（含会议录制、录音、本地文件上传、云文件导入四个场景），每月 1 号自动恢复。
- **飞书 AI 会员用户**：即使「智能纪要」额度用完了，**录音转文字的 300 分钟额度仍可继续使用**——这恰好是这个 Skill 存在的意义：用飞书录音转写拿到文字稿，再由本 Skill 生成智能纪要，**绕开智能纪要的额度限制**。

操作：在飞书桌面端或移动端进入「妙记」→ 点 **录音** 或 **上传音视频文件** → 转写完成后，用 `lark-cli` 提取文字稿：

```bash
lark-cli minutes +detail --minute-tokens <妙记token> --transcript
# → 默认输出到 ./minutes/<token>/transcript.txt，含发言人区分与时间戳
```

> 飞书妙记的转写结果格式与本 Skill 期望的输入格式天然对齐（`发言人 时间戳\n正文`），无需任何加工。

### 方案 B：用通义听悟（额度更大，不在飞书生态内的用户）

如果飞书的 300 分钟额度不够用，或者你根本不在飞书生态内，推荐用阿里云的**通义听悟**（tingwu.aliyun.com）：

- **免费额度非常大**：每日登录签到即可领取 **10 小时**转写时长，绑定阿里云盘还能再解锁更多。
- **支持说话人区分**：转写时自动区分不同发言人，可手动编辑发言人名称。
- **单文件最长 6 小时**，支持音频（MP3/WAV/M4A/AAC 等）和视频（MP4/MOV 等）。
- **可导出多种格式**：Word / PDF / SRT 字幕，导出时可勾选"包含发言人"和"包含时间戳"。

操作：访问 [tingwu.aliyun.com](https://tingwu.aliyun.com) → 登录后点 **上传音视频** 或 **开启实时记录** → 转写完成 → 点 **导出**，选 **Word 格式 + 勾选发言人**，保存到本地。

> 通义听悟导出的 Word 文件里已经是"发言人 + 时间戳 + 正文"结构，把它另存为 `.txt` 即可作为本 Skill 的输入。若导出格式与示例文字稿略有差异，可在 Claude Code 里直接让它"按这个文字稿生成智能纪要"，模型会自适应。

### 输入格式参考

无论哪条路径，最终喂给 Skill 的文字稿大致长这样（第一行是日期+时长，之后是 `发言人 时间戳 + 正文`分段）：

```
2026-06-18 08:00:44 CST|1h 21min 31s

Keywords:
考试、范围、题型、复习

Speaker 1 00:00:16.480
我们今天来讲一下期末考试的范围和题型……

Speaker 2 00:00:42.120
老师，请问开卷还是闭卷？
```

拿到这样的文字稿后，回到 [🚀 快速开始](#-快速开始) 第 4 步，把路径发给 Claude 即可。

---

## 📦 输入 / 输出

| 输入 | 输出 |
|------|------|
| 一篇 ASR 文字稿（`transcript.txt`，含发言人区分与时间戳） | `智能纪要.md` — 完整纪要文档 |
| 可选：妙记 token + minutes 子域名 | `画板.json` + `画板.png` — 开头可视化画板 |
| 可选：回写配置（知识库父节点） | 飞书知识库子文档（需回写模式） |

---

## 📂 项目结构

```
Smart-Minutes-Open/
├─ SKILL.md                          ← 入口：快速决策 + 执行步骤
├─ SETUP.md                          ← 首次初始化引导
├─ README.md                         ← 本文件（项目总览 + 蒸馏方法论）
├─ references/                       ← 详细规范（按需读取，渐进式加载）
│  ├─ output-structure.md            ← 输出文档总体结构
│  ├─ whiteboard.md                  ← 画板 — DSL JSON / 渲染 / 写入
│  ├─ summary-notes.md               ← 要点梳理 — grid 多列结构化
│  ├─ todos.md                       ← 待办 — 复选框 + cite
│  ├─ smart-chapters.md              ← 智能章节 — 时间戳分段
│  ├─ key-decisions.md               ← 关键决策 — 三要素 / 主次
│  ├─ golden-quotes.md               ← 金句时刻
│  ├─ related-links.md               ← 相关链接
│  ├─ quality-checklist.md           ← 全局质量要求 + 自检清单
│  └─ writeback.md                   ← 回写到飞书知识库
└─ scripts/
   └─ build_writeback.py             ← 生成产物 → 飞书回写 markdown 转换
```

> 💡 **渐进式加载**（Progressive Disclosure）：`SKILL.md` 保持精简（~75 行），各章节规范拆分到 10 份独立文档。模型生成某章节时只需读对应 reference，不必一次加载全部规范——既省上下文，又便于单独维护。

---

## 🛠️ 依赖

本 skill 依赖 [lark-cli](https://github.com/orgs/larksuite/packages) 及以下官方技能：

| 技能 | 用途 |
|------|------|
| `lark-shared` | 认证与权限 |
| `lark-whiteboard` | 画板查询与编辑 |
| `lark-minutes` | 妙记文字稿提取 |
| `lark-wiki` | 知识库节点管理 |
| `lark-doc` | 飞书文档编辑 |

不做内联复制，避免与官方技能内容重复、维护脱钩。

---

## 🏆 这个 Skill 是怎么炼成的：用"机器学习训练"的思路写 Skill

> [!IMPORTANT]
> 这个 Skill 不是手写出来的，而是**蒸馏**出来的——用一套类似 ML 训练流程的方法，让模型自己 Loop 迭代优化，直到生成质量逼近飞书原版。

我们用 **13 轮迭代 + 双 Agent 隔离打分** 的方法论，把飞书原版纪要作为"标准答案"，像训练模型一样把规则逐步优化。分数不会说谎：

### 📊 评分演进

| 指标 | 分数 | 可视化 |
|------|------|--------|
| 初始版本 | 74 | ███████████████░░░░░ |
| 第 3 轮 | 78 | ████████████████░░░░ |
| 第 6 轮 | 86 | █████████████████░░░ |
| 第 8 轮 | 88 | █████████████████▌░░ |
| **训练集最终** | **86-88** | **█████████████████▌░░** |
| **测试集（未参与改进）** | **~85.8** | **█████████████████▍░░** |
| **验证集（盲测）** | **81** | **████████████████░░░░** |

> 🎯 **测试集 85.8 + 验证集 81** — 证明没有过拟合，真实场景可用。

---

## 🧠 核心方法论：双 Agent 隔离 + 分数驱动

```mermaid
graph TD
    A["🧠 主线程 / 调度者<br/>维护 skill 版本 · 决定迭代保留"] --> B["📝 纪要生成 Agent"]
    A --> C["🔍 质量把关 Agent"]
    B --> D["文字稿 + 当前 skill<br/>→ 生成纪要<br/>❌ 不知道答案<br/>❌ 不知道分数<br/>❌ 不知道改进建议"]
    C --> E["原版纪要 + 生成版 + 文字稿<br/>→ 8维度打分<br/>→ 提出 skill 改哪条规则"]
    E --> A
    A --> F["整合建议 → 修改 skill<br/>→ 产出新版本候选"]
    F --> G{"🎯 验证分数是否上升"}
    G -->|✅ 是| H["保留为新版本"]
    G -->|❌ 否| I["放弃，回退上一版"]
```

> [!TIP]
> **为什么要隔离？** 防止"对着答案做题"。如果生成 Agent 能看到飞书原版纪要或上一轮的改进建议，它就会直接抄答案、迎合评分，而不是真正内化规则。隔离后，分数上升才真实反映 skill 在变好。

### 类机器学习的数据划分

| 集合 | 数量 | 用途 | 类比 |
|------|------|------|------|
| **训练集** | 11 篇 | 每轮选 1 篇做"改进样本" | 训练集 |
| **测试集** | 4 篇 | 每 ~3 轮全量打分，防止过拟合 | 测试集 |
| **验证集** | 2 篇 | 无原版，最终盲测，模拟真实场景 | 验证集 |

### 关键突破（分数驱动下被逼出来的）

1. **会议性质先分流** — 讲座类细切（每 3-5 分钟一章）、讨论类按大主题合并、圆桌类按嘉宾成章
2. **画板从文字 grid 升级为 DSL JSON + 渲染自检** — 真正可渲染的飞书画板
3. **占位符规范化 + 防幻觉** — 飞书链接子域名用占位符禁造假域名、术语不确定时保留音译
4. **关键决策分主次 + 分享类建议性决策** — 1 条主决策完整三要素 + N 条其他简列

> [!NOTE]
> 这套方法论本身（双 Agent 隔离 + 类 ML 数据划分 + 分数驱动迭代）是**可复用**的——换一个领域，只要能拿到"原版答案 + 输入样本"，就能用同样的流程蒸馏出对应的 skill。

---

## 📐 8 维度评分体系

| 维度 | 权重 | 说明 |
|------|------|------|
| 画板 | 20% | 可视化结构图质量 |
| 要点梳理 | 20% | 多列结构化速览 |
| 智能章节 | 15% | 分段逻辑与粒度 |
| 关键决策 | 15% | 主次决策、三要素完整性 |
| 待办 | 10% | 复选框 + cite 准确度 |
| 格式还原度 | 10% | 与飞书原版风格一致性 |
| 忠实度与幻觉 | 5% | 无虚构域名、无过度演绎 |
| 金句时刻 | 5% | 关键语录捕获 |

---

## 🤝 贡献

欢迎 Issue / PR！如果你有真实会议文字稿 + 飞书原版纪要，可以帮我们扩展数据集，进一步提升泛化能力。

## 📄 许可

MIT © 作者（详见 [LICENSE](LICENSE)）

---

<div align="center">

**觉得有用？点个 ⭐ 支持一下！**

<a href="https://github.com/YunfanGoForIt/Smart-Minutes-Open">
  <img src="https://img.shields.io/github/stars/YunfanGoForIt/Smart-Minutes-Open?style=social" alt="star">
</a>

</div>

<!-- Star History -->

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=YunfanGoForIt/Smart-Minutes-Open&type=Date)](https://star-history.com/#YunfanGoForIt/Smart-Minutes-Open&Date)

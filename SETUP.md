# 初始化引导（首次使用必读）

本 skill 把智能纪要回写到飞书知识库时，需要一个**根目录**作为容器：每次生成的智能纪要作为根目录的子文档，原始文字稿再作为该智能纪要的子文档。脱敏后的开源版不知道你的飞书库里哪个文档当根目录，所以首次使用需先建一个并记录下来。

```
你的飞书知识库
└─ 📋 会议纪要（根目录，本步骤创建）        ← 记录到本地配置
   └─ 智能纪要：XX 2026-07-01              ← 每次生成时自动创建
      └─ 文字记录：XX 2026-07-01           ← 原始文字稿
```

## 前置：安装并认证 lark-cli

```bash
# 1. 安装 lark-cli（任选一种）
npm install -g @larksuite/cli        # npm
brew install lark-cli                 # macOS Homebrew（若有 formula）

# 2. 初始化应用配置 + 用户身份授权（按 lark-shared 技能的引导走）
lark-cli config init                 # 扫码完成应用配置
lark-cli auth login --domain minutes,note,drive,docs,wiki --no-wait --json
# → 拿到 verification_url，浏览器打开完成授权
lark-cli auth login --device-code <上一步返回的 device_code>
lark-cli auth status                 # user: ready 即可
```

> 详细认证步骤见 `lark-shared` 技能。妙记属于用户个人数据，必须用 `--as user` 身份。

## 步骤 1：在飞书知识库新建根目录文档

在飞书客户端或网页版打开你的知识库，新建一个文档作为智能纪要根目录，建议命名 `📋 会议纪要`（或你习惯的名字）。打开它，从浏览器地址栏复制它的 URL，形如：

```
https://{你的租户}.feishu.cn/wiki/{node_token}
```

末尾的字符串就是 `node_token`。

## 步骤 2：把根目录 token 写入本地配置

在你能稳定运行本 skill 的目录下，创建配置文件 `.feishu-minutes-config.json`：

```json
{
  "wiki_parent_node_token": "<上一步的 node_token>",
  "minutes_domain": "<你的飞书租户子域名>",
  "root_title": "📋 会议纪要"
}
```

字段说明：
- `wiki_parent_node_token`：根目录文档的 node_token（必填）。
- `minutes_domain`：你的飞书租户子域名，用于拼接妙记/纪要链接（如 `https://{minutes_domain}.feishu.cn/...`）。不知道就先留空字符串，回写时链接用占位符。
- `root_title`：根目录标题，仅用于日志展示，可省略。

> 配置文件不要提交到 git（已含 `.gitignore`）。多人/多租户时可建多份配置，运行时指定。

## 步骤 3：验证

```bash
# 确认父节点可访问、能解析出 space_id
lark-cli wiki spaces get_node --params '{"token":"<wiki_parent_node_token>"}' --as user
```

能正常返回节点信息即初始化完成。之后每次生成 + 回写，skill 会自动读这份配置。

## 没有飞书知识库怎么办？

不回写也能用：本 skill 可只生成本地 `智能纪要.md` + `画板.json` + `画板.png`，跳过回写步骤。SETUP 仅在需要回写时才必要。

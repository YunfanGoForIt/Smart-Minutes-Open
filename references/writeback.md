# 回写到飞书知识库（可选，调用方要求时执行）

把生成的智能纪要回写为飞书知识库子文档，结构与原版一致：**目标 wiki 父节点下新建「智能纪要：{主题} {日期}」docx，其下再建「文字记录：{主题} {日期}」docx 存放文字稿**；智能纪要顶部画板写入 `画板.json`。

```
{wiki 父节点（智能纪要根目录）}
└─ 智能纪要：{主题} {日期}          ← 智能纪要 docx（含画板 + 要点 + 各章节）
   └─ 文字记录：{主题} {日期}        ← 文字记录 docx（原始文字稿）
```

> **目标 wiki 父节点**：由 `SETUP.md` 初始化时建立并记录到本地配置（`.feishu-minutes-config.json`）。调用方指定其它父节点时以其为准（用 `lark-cli wiki spaces get_node --params '{"token":"<wiki_token>"}' --as user` 解析 space_id）。

## 前置条件

- lark-cli 已认证（先 Read `lark-shared` 技能），身份 `--as user`。
- 已按 `SETUP.md` 完成初始化，配置文件中记录了 wiki 父节点 node_token 与 space_id。
- 调用方提供**妙记 token**（`MINUTE_TOKEN`）与**妙记子域名**（`MINUTES_DOMAIN`），用于智能章节与相关链接的 minutes URL。未提供则用占位符，链接不可点击但结构完整。
- 已按画板规范生成 `画板.json` + `画板.png` 并通过 `--check`。

## 步骤 1：说话人映射（纪要与文字记录统一）

从文字稿建立说话人映射：按**首次出现顺序**把文字稿的说话人标签（无论是真实姓名还是 `Speaker X`）映射为 `说话人 1`、`说话人 2`、`说话人 3`……。智能纪要正文与文字记录 doc 必须使用**同一套映射**，确保两文档对得上。

## 步骤 2：创建两个 wiki 子节点（先建空壳，拿 obj_token）

```bash
# 读取配置拿到父节点 token
SMART_PARENT=$(jq -r .wiki_parent_node_token .feishu-minutes-config.json)

# 1) 智能纪要 docx（作为根目录的子节点）
lark-cli wiki +node-create \
  --parent-node-token "$SMART_PARENT" \
  --title "智能纪要：{主题} {日期}" --as user
# → 记下 SMART_NODE_TOKEN（node_token）与 SMART_OBJ_TOKEN（obj_token）

# 2) 文字记录 docx（作为智能纪要节点的子节点）
lark-cli wiki +node-create \
  --parent-node-token <SMART_NODE_TOKEN> \
  --title "文字记录：{主题} {日期}" --as user
# → 记下 TR_NODE_TOKEN 与 TR_OBJ_TOKEN
```

## 步骤 3：生成两份待写入的 markdown

可用 [`scripts/build_writeback.py`](../scripts/build_writeback.py) 自动生成，或手动构造。写入用 markdown 与本地预览版有两处差异：**不含 `<title>` 行**（标题由 `wiki +node-create --title` 设定，从 `> 录音主题：` 开始）；画板与文字记录链接用真实 token。

**`./_智能纪要.md`**：按各章节规范生成，但：
- `# 总结` 顶部画板标记用 `<whiteboard type="blank"></whiteboard>`（**不是** `token=...`）——导入时飞书创建空白画板并在响应里回传 token（步骤 4），再在步骤 5 写入 `画板.json`。
- `# 相关链接` 文字记录用真实 token：`- [文字记录]\n\n  - [{主题} {日期}](https://{MINUTES_DOMAIN}.feishu.cn/docx/{TR_OBJ_TOKEN})`。
- 妙记链接用调用方提供的 token/子域名，未提供则 `MINUTE_TOKEN`/`MINUTES_DOMAIN` 占位。

**`./_文字记录.md`**：与原版飞书「文字记录」doc 格式一致：
- 不含标题行，直接从引用块开始：
  ```
  > 录音主题：{主题}  
  > 录音时间：{YYYY年M月D日}（{周X}）{开始HH:MM} - {结束HH:MM}（GMT+08）  
  > 智能纪要：[{主题} {日期}](https://{MINUTES_DOMAIN}.feishu.cn/docx/{SMART_OBJ_TOKEN})
  ```
  （每行末尾两个空格做软换行）
- 正文：把文字稿每个说话段落转为 `说话人 X HH:MM:SS  \n{转写文本}\n\n`（**去掉毫秒**，说话人按步骤 1 映射；段落间空行）。

## 步骤 4：写入两个 doc

```bash
# 文字记录
lark-cli docs +update --api-version v2 --doc <TR_OBJ_TOKEN> \
  --command append --doc-format markdown --content '@_文字记录.md' --as user

# 智能纪要（响应里含新建画板的 block_token）
lark-cli docs +update --api-version v2 --doc <SMART_OBJ_TOKEN> \
  --command append --doc-format markdown --content '@_智能纪要.md' --as user
# → 从响应 document.new_blocks[] 中找 block_type=="whiteboard" 的那条，记下 block_token = WB_TOKEN
```

> `--content '@file'` 只接受 cwd 下相对路径（绝对路径会报 `unsafe file path`）；用完清理 `./_*.md`。也可用 `--content -` 从 stdin 传。飞书 block 标签（`<whiteboard>`/`<grid>`/`<column>`/`<readonly-block>`/`<cite>` 等）在 `--doc-format markdown` 下会被解析为真实 block。

## 步骤 5：写入画板

```bash
npx -y @larksuite/whiteboard-cli@^0.2.11 -i 画板.json --to openapi --format json \
  | lark-cli whiteboard +update --whiteboard-token <WB_TOKEN> \
    --source - --input_format raw \
    --idempotent-token <10+字符唯一串> --as user --overwrite
```

## 步骤 6：交付与降级

向调用方返回：
- 智能纪要 URL：`https://{MINUTES_DOMAIN}.feishu.cn/wiki/<SMART_NODE_TOKEN>`
- 文字记录 URL：`https://{MINUTES_DOMAIN}.feishu.cn/wiki/<TR_NODE_TOKEN>`
- 画板已写入智能纪要顶部。

**降级**：若任一步因权限/认证失败，保留已生成的 `智能纪要.md`/`画板.json`/`画板.png` 本地产物，报告失败步骤；已建的空壳 wiki 节点需告知调用方以便清理（不要留半成品 doc）。若仅缺妙记 token，仍可完成写入，只是 minutes 链接为占位符。

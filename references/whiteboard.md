# 画板（开头可视化梳理）— 位于 # 总结 顶部

画板要"清晰、简要地梳理整个录音内容"。飞书原版画板的视觉风格是：**主标题 + 💡核心结论通栏 + 2~4 个分区（每分区 2 张柔和配色卡片）+ 可选徽章 + 右下"内容由 AI 生成"水印，全程无连线，靠分组与配色表达结构**。

**本 skill 生成真正的画板 DSL JSON 文件，渲染 PNG 自检，并写入飞书画板**，使纪要开头的 `<whiteboard>` 渲染出与原版一致的画板速览。原版 `<whiteboard>` 之后直接接引导文字 + 要点梳理，**没有额外的"画板内容"文字 grid**——画板本身就是速览。

## 一、画板内容设计规则（JSON 内容的来源）

- **主标题**：≤20 字名词性短语，从文字稿归纳（与 `<title>` 主题一致），前可加 1 个点题 emoji（如 🦄/🚀/📊，视会议调性选，不确定可省略）。
- **💡 核心结论**：2-3 条，每条≤30 字，必须是"结论"而非"话题"，关键词加粗。这是全篇最重要的 takeaway。
- **分区**：2-4 个，按会议自然主题切分，不要过细。每分区 2 张并排卡片；步骤型会议（"第一步/第二步…"）可为序列卡片，仍按卡片处理。
- **每张卡片**：emoji+标题（≤12 字）+ 一句话副标题（点题）+ 2-5 条要点（每条关键词加粗）。可在右上角加一枚徽章（状态/分工标签，如"正常推进""明确分工"，无则省略）。
- **底部水印**：右下"内容由 AI 生成"。
- **无连线**：靠分组、对齐、配色表达结构，不要画箭头/连线。
- **简要优先**：整张画板信息密度高但不堆砌，分区与卡片数与会议实际主题数对齐。

## 二、画板 DSL JSON 结构规范

按以下骨架生成 `画板.json`（DSL 语法，`version: 2`，顶层 `nodes` 数组）。布局基于 Flex（Yoga 引擎，语义同 CSS Flexbox）。配色取自飞书画板经典色板（参考 lark-whiteboard 技能）。

```json
{
  "version": 2,
  "nodes": [
    {
      "type": "frame", "id": "root",
      "layout": "vertical", "gap": 20, "padding": 32,
      "width": 1200, "height": "fit-content",
      "fillColor": "#FFFFFF",
      "children": [
        { "type": "text", "id": "title",
          "width": "fill-container", "height": "fit-content",
          "text": "{🦄} {一句话会议主题}", "fontSize": 26, "textColor": "#1F2329", "textAlign": "left" },

        { "type": "frame", "id": "conclusion",
          "layout": "horizontal", "gap": 12, "padding": 16,
          "width": "fill-container", "height": "fit-content",
          "fillColor": "#F0F4FC", "borderColor": "#5178C6", "borderWidth": 2, "borderRadius": 8,
          "alignItems": "start",
          "children": [
            { "type": "text", "width": "fit-content", "height": "fit-content",
              "text": "💡 核心结论：", "fontSize": 16, "textColor": "#1F2329", "textAlign": "left" },
            { "type": "text", "width": "fill-container", "height": "fit-content",
              "text": [
                { "content": "• {结论1关键词加粗}，{展开}\n", "fontSize": 15, "color": "#1F2329" },
                { "content": "• {结论2}\n", "fontSize": 15, "color": "#1F2329" },
                { "content": "• {结论3}", "fontSize": 15, "color": "#1F2329" }
              ], "textAlign": "left" }
          ] },

        {
          "type": "frame", "id": "section-1",
          "layout": "vertical", "gap": 12, "padding": 0,
          "width": "fill-container", "height": "fit-content",
          "children": [
            { "type": "text", "width": "fit-content", "height": "fit-content",
              "text": "{分区标题1}", "fontSize": 20, "textColor": "#1F2329", "textAlign": "left" },
            {
              "type": "frame", "id": "section-1-row",
              "layout": "horizontal", "gap": 16, "padding": 0,
              "width": "fill-container", "height": "fit-content",
              "alignItems": "stretch",
              "children": [
                {
                  "type": "frame", "id": "card-1a",
                  "layout": "vertical", "gap": 10, "padding": 16,
                  "width": "fill-container", "height": "fit-content",
                  "fillColor": "#EAE2FE", "borderColor": "#8569CB", "borderWidth": 2, "borderRadius": 8,
                  "children": [
                    { "type": "frame", "layout": "horizontal", "gap": 8, "padding": 0,
                      "width": "fill-container", "height": "fit-content",
                      "justifyContent": "space-between", "alignItems": "center",
                      "children": [
                        { "type": "text", "width": "fit-content", "height": "fit-content",
                          "text": "📅 {卡片标题A}", "fontSize": 16, "textColor": "#1F2329", "textAlign": "left" },
                        { "type": "rect", "width": "fit-content", "height": "fit-content",
                          "text": "正常推进", "fontSize": 12, "textColor": "#509863",
                          "fillColor": "#FFFFFF", "borderColor": "#509863", "borderWidth": 2, "borderRadius": 12 }
                      ] },
                    { "type": "text", "width": "fill-container", "height": "fit-content",
                      "text": "{副标题A一句话点题}", "fontSize": 14, "textColor": "#1F2329", "textAlign": "left" },
                    { "type": "text", "width": "fill-container", "height": "fit-content",
                      "text": [
                        { "content": "• ", "fontSize": 14, "color": "#1F2329" },
                        { "content": "{关键词}", "bold": true, "fontSize": 14, "color": "#1F2329" },
                        { "content": "{展开}\n", "fontSize": 14, "color": "#1F2329" },
                        { "content": "• {要点2}\n", "fontSize": 14, "color": "#1F2329" },
                        { "content": "• {要点3}", "fontSize": 14, "color": "#1F2329" }
                      ], "textAlign": "left" }
                  ] },
                { "type": "frame", "id": "card-1b",
                  "layout": "vertical", "gap": 10, "padding": 16,
                  "width": "fill-container", "height": "fit-content",
                  "fillColor": "#F0F4FC", "borderColor": "#5178C6", "borderWidth": 2, "borderRadius": 8,
                  "children": [ "…同结构…" ]
                }
              ]
            }
          ] },

        { "type": "text", "id": "watermark",
          "width": "fill-container", "height": "fit-content",
          "text": "内容由 AI 生成", "fontSize": 12, "textColor": "#646A73", "textAlign": "right" }
      ]
    }
  ]
}
```

**结构要点**：
- 顶层 `frame(vertical, width 1200 固定, height fit-content, fillColor #FFFFFF)`，子节点顺序：主标题 → 核心结论通栏 → 各分区 → 水印。
- 核心结论通栏：`horizontal` frame，浅蓝底 `#F0F4FC`/`#5178C6`；左侧 `💡 核心结论：` label（`fit-content`），右侧富文本要点列（`fill-container`，每条以 `• ` 开头、`\n` 换行）。
- 每分区：`vertical` frame，内含分区标题 text（fontSize 20, `#1F2329`, 左对齐，**深色纯文字不加色**）+ 卡片行 `horizontal` frame（`alignItems: stretch` 保证两卡等高）。
- 每张卡片：`vertical` frame，`fillColor`=该卡浅色、`borderColor`=该卡深色（同色系），`borderWidth 2, borderRadius 8`。children 三段：
  1. 顶部行 `horizontal` frame（`justifyContent: space-between, alignItems: center`）：`emoji 卡片标题` text（左）+ 可选徽章 rect（右，白底/同色边/`borderRadius 12`）。无徽章则整行只放标题 text。
  2. 副标题 text（fontSize 14, 左对齐）。
  3. 要点 text（富文本 `WBTextRun[]`，每条 `• ` + 关键词 `bold:true` + 展开，`\n` 换行，fontSize 14, 左对齐, `width fill-container, height fit-content`）。
- 配色：从经典色板为每张卡片选不同色——4 卡常用 浅紫 `#EAE2FE`/`#8569CB`、浅蓝 `#F0F4FC`/`#5178C6`、浅绿 `#DFF5E5`/`#509863`、浅黄 `#FEF1CE`/`#D4B45B`；同分区两卡用不同色区分。**不得使用色板外的自创色值**。分区标题与正文文字统一 `#1F2329`，辅助/水印用 `#646A73`。
- emoji 直接写进 text 字符串（如 `"text": "📅 卡片标题A"`），不依赖图标库。

**硬约束（防渲染崩）**：
1. **含文字节点 `height` 必须用 `fit-content`**——写死数值会截断文字。
2. **每个 frame 必须显式写 `layout`/`gap`/`padding`**——不写 layout 子节点全堆左上角，不写 gap/padding 会粘连/贴边。
3. **`fill-container` 仅在 Flex 父容器且祖先链有固定宽度时生效**——顶层 frame `width: 1200` 已提供固定宽度，卡片内 `fill-container` 文本节点可正常撑开。
4. **`alignItems` 默认 `start`**——卡片行需等高时必须显式写 `alignItems: "stretch"`。
5. **不用 `layout: "dagre"`**（本场景无拓扑连线），不要给容器套 dagre。
6. **不用 SVG `<text>`**——本场景全部用 DSL `text` 节点承载文字。
7. **`text`/`content` 中双引号写 `\"`，换行用 `\n`**（不要双重转义为 `\\n`）。
8. **connector 不出现**——画板无连线，顶层 `nodes` 只有一个 root frame。

## 三、产物文件

在纪要输出目录（与 `智能纪要.md` 同级）产出两个文件：
- `画板.json`：DSL 源文件（§2 骨架填实）。
- `画板.png`：渲染预览（§4 自检用）。

## 四、渲染自检

```bash
# 渲染 PNG 预览
npx -y @larksuite/whiteboard-cli@^0.2.11 -i 画板.json -o 画板.png
# 检测 text-overflow / node-overlap
npx -y @larksuite/whiteboard-cli@^0.2.11 -i 画板.json --check
```

看 PNG：信息完整？布局合理？配色协调？文字无截断？卡片无重叠？`--check` 报错就修，最多 2 轮。症状→修复：
- 文字截断 → 该节点 `height` 改 `fit-content`。
- 文字溢出右侧 → 缩短文案或加大父容器 `width`。
- 卡片重叠粘连 → 增大 `gap`。
- 布局偏左/偏右 → 检查 `alignItems`/`justifyContent`。
2 轮后仍严重错乱 → 走 Mermaid 兜底（思维导图/流程图语法），但本场景一般不需要。

## 五、写入飞书画板（让纪要开头出现真正可渲染的画板）

1. **认证**：先用 Read 读 `lark-shared` 技能，按其说明完成 lark-cli 认证与权限处理。身份默认 `--as user`。
2. **取画板 token**：
   - **调用方提供了 whiteboard token** → 直接用。
   - **有纪要 doc_id 但无 token** → 在文档中 append 一个空白画板块，从响应取 `block_token`：
     ```bash
     lark-cli docs +update --api-version v2 --doc <doc_id> --command append \
       --content '<whiteboard type="blank"></whiteboard>' --as user
     ```
     从返回的 `data.new_blocks[0].block_token`（`block_type == "whiteboard"` 的那条）取得 token。
3. **写入画板**（DSL → OpenAPI 原生 → 飞书）：
   ```bash
   npx -y @larksuite/whiteboard-cli@^0.2.11 -i 画板.json --to openapi --format json \
     | lark-cli whiteboard +update --whiteboard-token <token> \
       --source - --input_format raw \
       --idempotent-token <10+字符唯一串，如时间戳+标识> \
       --as user --overwrite
   ```
   `--overwrite` 覆盖式写入（不带则增量更新，可能与已有内容重叠）。`--idempotent-token` 至少 10 字符，避免重试导致重复写入。
4. **降级**：若无 lark-cli 认证 / 无 doc_id / 调用方未给 token，则**只交付 `画板.json` + `画板.png` 产物**，markdown 里 `<whiteboard token="WHITEBOARD_TOKEN">` 保留占位，并在执行自检里标注"画板未写入飞书（缺 token/认证），仅产出本地 JSON+PNG"。

## 六、markdown 中的画板标记

`# 总结` 顶部放画板标记，**不要**再附加"🖼画板内容"文字 grid（画板本身即速览，与原版对齐）：

```
<whiteboard token="{真实token 或 WHITEBOARD_TOKEN}"></whiteboard>
```

- 写入成功 → 用真实 token。
- 降级未写入 → 用 `WHITEBOARD_TOKEN` 占位（不要用空字符串，也不要用会议/妙记 token 替代）。
- **回写飞书知识库时**（见 references/writeback.md） → 改用 `<whiteboard type="blank"></whiteboard>`（不带 token）：导入时飞书自动创建空白画板并在响应回传 token，再由回写流程写入 `画板.json`。

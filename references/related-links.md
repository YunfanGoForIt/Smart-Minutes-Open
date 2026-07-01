# 相关链接（# 相关链接）

```
- 妙记：[{主题}](https://{MINUTES_DOMAIN}.feishu.cn/minutes/{token}?from=ai_minutes)
- 文字记录

  - [{主题} {日期}](https://{MINUTES_DOMAIN}.feishu.cn/docx/DOC_TOKEN_PLACEHOLDER)
```

- `{token}` 用调用方提供的妙记 token（生成 Agent 会从调用方 prompt 得到）；若未提供则用占位 `MINUTE_TOKEN`。
- **所有飞书链接的子域名一律用占位符 `MINUTES_DOMAIN`**（妙记链接、文字记录 docx 链接），形如 `https://MINUTES_DOMAIN.feishu.cn/...`，**禁止编造**任何形似真实的子域名（如某产品线子域）。文字记录的 docx token 用 `DOC_TOKEN_PLACEHOLDER`。
- 会中若明确提到了共享文档/链接，可在此列出；否则只列妙记与文字记录两项。

> 回写飞书知识库时（见 references/writeback.md），文字记录链接改用真实 token。

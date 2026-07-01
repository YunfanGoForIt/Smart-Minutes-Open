#!/usr/bin/env python3
"""把生成产物转成飞书回写用的两份 markdown。

用法:
  python build_writeback.py <minute_id> <smart_node> <smart_obj> <tr_node> <tr_obj>

产生:
  _min_{minute_id}.md   — 智能纪要（去 title, 画板改 blank, 链接改真实 token）
  _tr_{minute_id}.md    — 文字记录（引用块 + 说话人段落）
"""
import sys, re, os


def parse_args():
    """argv: id smart_node smart_obj tr_node tr_obj"""
    id_, smart_node, smart_obj, tr_node, tr_obj = sys.argv[1:6]
    return id_, smart_node, smart_obj, tr_node, tr_obj


def main():
    id_, smart_node, smart_obj, tr_node, tr_obj = parse_args()
    base = os.getcwd()

    # ---------- 读入原始文件 ----------
    smart_md = ""
    transcript = ""

    # 尝试 out/ 目录（合并导出）或当前目录
    for prefix in ["out", "."]:
        sp = os.path.join(prefix, id_, "智能纪要.md")
        tp = os.path.join(prefix, id_, "transcript.txt")
        if os.path.isfile(sp):
            with open(sp, encoding="utf-8") as f:
                smart_md = f.read()
        if os.path.isfile(tp):
            with open(tp, encoding="utf-8") as f:
                transcript = f.read()
        if smart_md and transcript:
            break

    if not smart_md:
        sys.exit(f"找不到 智能纪要.md（out/{id_}/ 或 ./{id_}/）")
    if not transcript:
        sys.exit(f"找不到 transcript.txt（out/{id_}/ 或 ./{id_}/）")

    # ---------- 读取配置中的 minutes_domain ----------
    minutes_domain = ""
    config_path = os.path.join(base, ".feishu-minutes-config.json")
    if os.path.isfile(config_path):
        try:
            with open(config_path, encoding="utf-8") as f:
                minutes_domain = json.loads(f.read()).get("minutes_domain", "")
        except Exception:
            pass  # 解析失败不致命

    # ---------- 智能纪要 md 转换 ----------

    # 1) 剥 <title> 行及其后空行
    m = re.search(r'^<title>.*?</title>\s*\n\s*', smart_md, re.S)
    min_md = smart_md[m.end():] if m else smart_md

    # 2) 画板占位 -> blank（回写时飞书自动创建画板）
    min_md = min_md.replace(
        '<whiteboard token="WHITEBOARD_TOKEN"></whiteboard>',
        '<whiteboard type="blank"></whiteboard>'
    )

    # 3) 剥 IMAGE_PLACEHOLDER 图片行（回写时不需要占位图）
    min_md = '\n'.join(
        line for line in min_md.split('\n')
        if not re.match(r'^\s*!\[.*\]\(IMAGE_PLACEHOLDER\)\s*$', line)
    ) + '\n'

    # 4) 文字记录链接 -> 真实 wiki URL
    placeholder_url = f'https://{minutes_domain or "MINUTES_DOMAIN"}.feishu.cn/docx/DOC_TOKEN_PLACEHOLDER'
    real_url = f'https://{minutes_domain or "MINUTES_DOMAIN"}.feishu.cn/wiki/{tr_node}'
    min_md = min_md.replace(placeholder_url, real_url)

    # ---------- 文字记录 md ----------

    # 提取 header 字段
    topic = ""
    record_time = ""
    for ln in smart_md.split('\n'):
        m2 = re.match(r'^>\s*录音主题：(.*)$', ln)
        if m2:
            topic = m2.group(1).strip()
        m3 = re.match(r'^>\s*录音时间：(.*)$', ln)
        if m3:
            record_time = m3.group(1).strip()
    tm = re.search(r'<title>智能纪要：(.*?)</title>', smart_md)
    title_td = tm.group(1).strip() if tm else ""

    lines = []
    # 引用块头部（每行末尾两个空格做软换行）
    lines.append(f'> 录音主题：{topic}  ')
    lines.append(f'> 录音时间：{record_time}  ')
    smart_link = f'https://{minutes_domain or "MINUTES_DOMAIN"}.feishu.cn/wiki/{smart_node}'
    lines.append(f'> 智能纪要：[{title_td}]({smart_link})')
    lines.append('')
    lines.append('')

    # 解析 transcript 说话块
    blocks = re.split(r'\n\s*\n', transcript)
    spk_re = re.compile(r'^(Speaker \d+|说话人 \d+)\s+(\d{2}:\d{2}:\d{2})(?:\.\d+)?\s*$')
    for blk in blocks:
        blk = blk.strip()
        if not blk:
            continue
        # 跳过首行日期 / Keywords 块
        if blk.startswith('20') and '|' in blk.split('\n')[0]:
            continue
        if blk.startswith('Keywords'):
            continue
        first_nl = blk.find('\n')
        if first_nl == -1:
            continue
        head = blk[:first_nl].strip()
        body = blk[first_nl + 1:].strip()
        m4 = spk_re.match(head)
        if not m4:
            continue
        spk = m4.group(1)
        ts = m4.group(2)
        # Speaker N -> 说话人 N（统一映射）
        ms = re.match(r'Speaker (\d+)', spk)
        if ms:
            spk = f'说话人 {ms.group(1)}'
        # body 内多余空行压缩
        body = re.sub(r'\n{3,}', '\n\n', body)
        lines.append(f'{spk} {ts}  ')
        lines.append(body)
        lines.append('')
        lines.append('')

    tr_md = '\n'.join(lines).rstrip() + '\n'

    # ---------- 写出 ----------
    min_file = f'_min_{id_}.md'
    tr_file = f'_tr_{id_}.md'
    with open(min_file, 'w', encoding='utf-8') as f:
        f.write(min_md)
    with open(tr_file, 'w', encoding='utf-8') as f:
        f.write(tr_md)
    print(f'wrote {min_file} ({len(min_md)} chars), {tr_file} ({len(tr_md)} chars)')


if __name__ == '__main__':
    main()

# 工具说明

## 聊天记录解析器

以下解析器可以直接从 ex-skill 项目复用，功能完全兼容：

- `wechat_parser.py` — 从 ex-skill/tools/wechat_parser.py 复制
- `imessage_parser.py` — 从 ex-skill/tools/imessage_parser.py 复制
- `sms_parser.py` — 从 ex-skill/tools/sms_parser.py 复制

复制方法：

```bash
# 假设你已经 clone 了 ex-skill
cp /path/to/ex-skill/tools/wechat_parser.py ./tools/
cp /path/to/ex-skill/tools/imessage_parser.py ./tools/
cp /path/to/ex-skill/tools/sms_parser.py ./tools/
```

这些解析器只做一件事：把各种格式的聊天记录转成纯文本。
已读不需要照片分析、社交媒体解析、persona 生成等模块。

## 已读独有工具

- `report_writer.py` — 确诊报告文件管理（已包含）

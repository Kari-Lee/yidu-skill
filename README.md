# 已读 · Yidu

> 心理咨询：600块一小时，帮你分析原生家庭
> 你闺蜜：免费，但她也在等她那个人回消息    
> 你妈：免费，但她会说"分了吧"  
>已读：免费，不评判，不说分了吧。  
只告诉你ta发"好"的时候在想什么  

ta不是不爱你。  
ta只是把爱藏在了你看不见的地方  
——才怪

ta就是回避型    
已读帮你省掉找的过程

确诊你们各自得了什么病    
免费。不痛。但可能有点残忍。  
把聊天记录丢进来。三十秒确诊。

---

## 这是什么

已读是一个 Claude Code / OpenClaw Skill。

把ta的聊天记录丢进来，AI 帮你：

1. **确诊** ta的依恋类型（回避型 / 焦虑型 / 安全型 / 混乱型）
2. **翻译** ta每句"嗯""哦""随便"背后的真实意思
3. **开方** 针对ta的类型给你具体的回消息策略

不是前任模拟器。不复刻任何人。不教你挽回。不教你套话术。

只帮你看清楚你们之间到底在发生什么。

---

## 和前任 Skill 有什么区别

前任 Skill 帮你留住过去。已读帮你看懂现在。

| | 前任 Skill | 已读 |
|---|---|---|
| 做什么 | 复刻一个人的说话方式 | 分析一段关系的互动模式 |
| 输出 | "像她一样说话"的 AI | 确诊报告 + 回消息策略 |
| 情绪 | 悼念 | 行动 |
| 用完之后 | 继续聊 | 去回ta消息 |

---

## 安装

### Claude Code

```bash
# 安装到当前项目
mkdir -p .claude/skills
git clone https://github.com/yourname/yidu-skill .claude/skills/yidu

# 或安装到全局
git clone https://github.com/yourname/yidu-skill ~/.claude/skills/yidu
```

### OpenClaw

```bash
git clone https://github.com/yourname/yidu-skill ~/.openclaw/workspace/skills/yidu
```

---

## 使用

启动：

```
/yidu
```

按提示输入关系背景，然后粘贴聊天记录。

### 后续命令

| 命令 | 功能 |
|------|------|
| `/yidu-translate {ta的消息}` | 翻译ta发的任何一句话 |
| `/yidu-reply {ta的消息}` | 针对ta的消息给你回复建议 |
| `/yidu-send {你想发的话}` | 检测这条消息会不会触发ta的防御机制 |
| `/yidu-predict` | 如果继续这样，三周后会怎样 |
| `/yidu-temperature` | ta最近消息的情绪温度变化 |

---

## 示例

```
用户 > /yidu

已读 > ta是你的什么人？
用户 > 正在折磨我的人

已读 > 简单说一下背景？
用户 > 暧昧三个月 同事 ta总是已读不回

已读 > 把聊天记录丢进来吧。

用户 > [粘贴聊天记录]

已读 >
确诊：回避型
置信度：87%（剩下13%是我给你留的希望）

核心模式：爱你的方式是没有消失

ta出卖自己的三句话：
1. ta说「到时候再说」— 没有"到时候"
2. ta说「我最近有点忙」— 忙着回避你
3. ta说「嗯」— 收到了但不想展开
```

```
用户 > /yidu-translate 到时候再说

已读 >
ta说：「到时候再说」

翻译：
可能性 A（60%）：不会有到时候，这是ta的终结话术
可能性 B（30%）：ta确实在犹豫，但犹豫本身就是答案
可能性 C（10%）：ta真的在等一个合适的时机

最可能的是：A
因为：回避型说"到时候再说"的时候，"到时候"约等于永远
```

```
用户 > /yidu-send 你是不是不喜欢我了

已读 >
你想发：「你是不是不喜欢我了」

判定：别发

这条消息会触发ta的：核心逃跑机制
ta收到之后大概率会：沉默更久，或者回一个"你想多了"

替代版本：「今天看到一个好笑的东西想发给你」
→ 改了什么：把质问换成分享，降低ta的防御成本，让ta觉得回你不累
```

---

## 数据来源

| 来源 | 格式 | 说明 |
|------|------|------|
| 微信聊天记录 | WeChatMsg / 留痕 / PyWxDump 导出 | 推荐，信息最丰富 |
| iMessage | Mac 直接读取或导出 | macOS 用户推荐 |
| 短信 | txt 导出 | 基础但够用 |
| 直接粘贴 | 复制粘贴到对话框 | 最快，零门槛 |
| 截图 | 聊天截图 | AI 自动识别文字 |

所有数据本地处理，不发送到任何外部服务。

---

## 项目结构

```
yidu-skill/
├── SKILL.md                    # Skill 入口
├── prompts/
│   ├── intake.md               # 信息录入
│   ├── attachment_analyzer.md  # 依恋类型分析
│   ├── deep_reader.md          # 深度解读
│   ├── reply_strategist.md     # 回消息策略
│   ├── report_builder.md       # 确诊报告
│   ├── translator.md           # 翻译器
│   ├── send_checker.md         # 发还是不发
│   ├── predictor.md            # 三周后预测
│   └── temperature.md          # 语气温度计
├── tools/
│   ├── wechat_parser.py        # 微信解析
│   ├── imessage_parser.py      # iMessage 解析
│   ├── sms_parser.py           # 短信解析
│   └── report_writer.py        # 报告管理
├── reports/                    # 确诊报告（gitignored）
├── requirements.txt
└── LICENSE
```

---

## 免责声明

已读不对你们的感情结果负责，只负责让你看清楚在发生什么。

不治病，就确诊，其ta的你自己决定。

---

**创始人：被回避型折磨成疯子的人**
**研发动力：早ta知道就好了**

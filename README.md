# 🧙 修仙漫剧 AI 生成系统

使用 Hermes Agent + DeepSeek V4 AI 模型自动生成修仙题材的漫剧脚本。

## ✨ 功能特性

- 🤖 **AI 驱动**：基于 DeepSeek V4 大语言模型
- 🎬 **自动编剧**：生成完整的修仙故事线和漫剧脚本
- 🧑‍💼 **Agent 协调**：使用 Hermes Agent 智能调度生成流程
- 📖 **结构化输出**：JSON/Markdown 格式的漫剧脚本
- 🔄 **可扩展**：支持自定义设定和参数调整

## 🎯 核心功能流程

```
用户输入（修仙题材设定）
    ↓
Hermes Agent 分析需求
    ↓
DeepSeek V4 生成内容
    ├─ 世界观设定
    ├─ 故事大纲（多话框架）
    └─ 详细漫剧脚本
    ↓
输出结构化漫剧内容
```

## 📋 项目结构

```
xianxia-manga-ai/
├── README.md
├── requirements.txt
├── config/
│   └── settings.py              # 配置文件
├── src/
│   ├── __init__.py
│   ├── deepseek_client.py       # DeepSeek API 客户端
│   ├── hermes_agent.py          # Hermes Agent 核心
│   ├── manga_generator.py       # 漫剧生成引擎
│   ├── prompts.py               # AI Prompt 模板库
│   └── utils.py                 # 工具函数
├── examples/
│   └── generate_example.py      # 使用示例
└── output/
    └── (生成的漫剧脚本)
```

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置 API

编辑 `config/settings.py`，设置 DeepSeek API：

```python
DEEPSEEK_API_KEY = "sk-a77c6ab5a9b841b6bf9c5d0c22e4f111"
DEEPSEEK_API_URL = "https://api.deepseek.com"
```

### 3. 生成修仙漫剧

```bash
python examples/generate_example.py
```

## 📖 使用示例

```python
from src.hermes_agent import HermesAgent
from src.manga_generator import MangaGenerator

# 初始化
agent = HermesAgent()
generator = MangaGenerator()

# 生成修仙漫剧
result = generator.generate(
    theme="修仙成神之路",
    episodes=5,
    style="热血冒险"
)

# 获取结果
print(result)
```

## 🎨 修仙元素系统

系统包含完整的修仙设定：

- **修为等级**：炼气、筑基、金丹、元婴、渡劫、成仙
- **功法体系**：道法、剑法、丹道、阵法
- **宗门设定**：正道宗门、魔道势力、隐世组织
- **妖兽等级**：妖兽、古兽、神兽
- **世界观**：灵气复苏、秘境、上界

## 🔧 高级配置

### 自定义生成参数

```python
config = {
    "world_setting": "东方奇幻世界",
    "protagonist_type": "平凡少年",
    "conflict_type": "宗门争斗",
    "magic_system": "五行法术",
    "tone": "热血励志"
}

result = generator.generate_with_config(config)
```

### Prompt 自定义

编辑 `src/prompts.py` 中的 Prompt 模板，自定义生成风格。

## 📝 输出格式

生成的漫剧脚本包含：

```json
{
  "title": "漫剧标题",
  "world_setting": "世界观设定",
  "episodes": [
    {
      "episode_no": 1,
      "title": "第一话标题",
      "scenes": [
        {
          "scene_no": 1,
          "location": "场景地点",
          "description": "场景描写",
          "characters": ["人物1", "人物2"],
          "dialogues": [
            {
              "character": "人物1",
              "speech": "台词",
              "action": "动作描写"
            }
          ]
        }
      ]
    }
  ]
}
```

## 🛠️ 开发指南

### 添加新的 Prompt 模板

在 `src/prompts.py` 中添加：

```python
CUSTOM_PROMPT = """
你是一个修仙漫剧编剧...
"""
```

### 扩展 Agent 功能

编辑 `src/hermes_agent.py`，添加新的工具函数。

### 自定义生成逻辑

在 `src/manga_generator.py` 中修改生成流程。

## 📚 API 文档

详见 [API.md](./docs/API.md)（建设中）

## ⚙️ 系统要求

- Python 3.8+
- 有效的 DeepSeek API Key
- 网络连接

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📞 支持

有问题？请提交 Issue 或联系开发者。

---

**让我们一起创造精彩的修仙漫剧吧！** 🧙✨

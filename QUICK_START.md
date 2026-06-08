# 🎬 立即开始：生成你的100岁老人修仙视频

## ⚡ 3 分钟快速开始

### 步骤 1：克隆/下载项目
```bash
cd xianxia-manga-ai
```

### 步骤 2：安装依赖
```bash
pip install -r requirements.txt
```

### 步骤 3：设置 API Key

#### 方式 A：编辑 .env 文件（最简单）
```bash
# 项目根目录创建或编辑 .env 文件
DEEPSEEK_API_KEY=sk-a77c6ab5a9b841b6bf9c5d0c22e4f111
STABLE_DIFFUSION_API_KEY=your_sd_key_here
ELEVENLABS_API_KEY=your_elevenlabs_key_here
```

#### 方式 B：设置环境变量
```bash
export DEEPSEEK_API_KEY="sk-a77c6ab5a9b841b6bf9c5d0c22e4f111"
export STABLE_DIFFUSION_API_KEY="your_sd_key_here"
export ELEVENLABS_API_KEY="your_elevenlabs_key_here"
```

### 步骤 4：运行生成脚本
```bash
python examples/generate_video_now.py
```

### 步骤 5：选择选项
```
请选择视频参数：

【视频长度】
1. 短版 (1-2分钟，2话)
2. 中版 (3-5分钟��5话) - 推荐
3. 长版 (10+分钟，10话)

选择视频长度 (1-3): 2  # 输入你的选择
```

### 步骤 6：等待完成 ☕
- 漫剧脚本生成：1-2 分钟
- 图像生成：3-5 分钟
- 语音生成：2-3 分钟
- 视频合成：1-2 分钟
- **总耗时：7-13 分钟**

### 步骤 7：查看结果
```bash
# 打开输出目录
cd output
ls -lh

# 播放视频
ffplay 百岁仙途_final.mp4
```

---

## 🔑 获取免费 API Key

### 1️⃣ Stable Diffusion（图像生成）

**官网**：https://platform.stability.ai

1. 注册账户
2. 登录后进入 Dashboard
3. 点击 "API Keys"
4. 复制你的 API Key
5. **免费额度**：100张图/月

```
获取链接：https://platform.stability.ai/account/keys
```

### 2️⃣ ElevenLabs（语音生成）

**官网**：https://elevenlabs.io

1. 注册账户
2. 登录后进入 Profile
3. 点击 "API Key"
4. 复制你的 API Key
5. **免费额度**：10,000字符/月（足够！）

```
获取链接：https://elevenlabs.io/app/profile/api-keys
```

### 3️⃣ DeepSeek（漫剧生成）

✅ **已有**：sk-a77c6ab5a9b841b6bf9c5d0c22e4f111

---

## 📊 成本计算

对于一部 **2-5 话的修仙漫剧**：

| 服务 | 用量 | 免费额度 | 成本 |
|------|------|--------|------|
| DeepSeek | 生成脚本 | 充足 | ✅ 免费 |
| Stable Diffusion | 6 张图 | 100/月 | ✅ 免费 |
| ElevenLabs | ~2000 字 | 10000/月 | ✅ 免费 |
| FFmpeg | 视频合成 | 本地软件 | ✅ 免费 |
| **总成本** | | | **✨ 完全免费** |

---

## 📁 生成后的文件结构

```
output/
├── 百岁仙途_script.json          ← 漫剧脚本（剧本）
│
├── episode_01_scene_1.png        ← 第1话场景1
├── episode_01_scene_2.png        ← 第1话场景2
├── episode_01_scene_3.png        ← 第1话场景3
│
├── episode_02_scene_1.png        ← 第2话场景1
├── episode_02_scene_2.png        ← 第2话场景2
├── episode_02_scene_3.png        ← 第2话场景3
│
├── voice_00_老教师.wav           ← 老教师的台词
├── voice_01_年轻弟子.wav         ← 年轻弟子的台词
├── voice_02_女修士.wav           ← 女修士的台词
├── voice_03_宗主.wav             ← 宗主的台词
│
├── background_music.mp3          ← 背景音乐
│
└── 百岁仙途_final.mp4            ✨ ← 最终视频！
```

---

## 🎬 视频信息

- **格式**：MP4
- **分辨率**：1280×720（HD）
- **帧率**：24 fps
- **音频**：立体声
- **时长**：2-5 分钟（取决于话数）
- **字幕**：自动生成
- **用途**：YouTube、抖音、快手、哔哩哔哩等平台

---

## 💻 系统要求

### 最低配置：
- **操作系统**：Windows/macOS/Linux
- **Python**：3.8+
- **内存**：4GB+
- **网络**：稳定的互联网连接

### 推荐配置：
- **操作系统**：macOS/Linux
- **Python**：3.9+
- **内存**：8GB+
- **GPU**：可选（加快图像生成）

### 软件要求：
- **FFmpeg**：用于视频合成

#### 安装 FFmpeg

**macOS**：
```bash
brew install ffmpeg
```

**Ubuntu/Debian**：
```bash
sudo apt-get install ffmpeg
```

**Windows**：
- 下载：https://ffmpeg.org/download.html
- 或使用 Chocolatey：`choco install ffmpeg`

---

## 🚀 完整命令一键启动

```bash
# 一次性完整设置
git clone https://github.com/huhuugt/xianxia-manga-ai.git
cd xianxia-manga-ai
pip install -r requirements.txt

# 创建 .env 文件
cat > .env << EOF
DEEPSEEK_API_KEY=sk-a77c6ab5a9b841b6bf9c5d0c22e4f111
STABLE_DIFFUSION_API_KEY=your_key_here
ELEVENLABS_API_KEY=your_key_here
EOF

# 运行生成
python examples/generate_video_now.py
```

---

## ❓ 常见问题

### Q：不想配置 API，可以吗？

**A：** 可以！我可以帮你设置本地模型：
- Stable Diffusion：使用 `diffusers` 库（需要显卡）
- TTS：使用开源模型（如 Tacotron2）
- 性能会慢一些，但完全免费且可以离线运行

### Q：生成的视频可以用于商业用途吗？

**A：** 取决于你选择的 API：
- Stable Diffusion：✅ 可以（需要 Pro 计划）
- ElevenLabs：✅ 可以
- 建议查看各服务的使用条款

### Q：可以自定义故事内容吗？

**A：** 完全可以！编辑这个文件：
```python
# examples/generate_video_now.py
config = {
    "title": "你的标题",
    "episodes": 5,  # 改变话数
    # 修改漫剧生成参数
}
```

### Q：生成失败了怎么办？

**A：** 查看日志：
```bash
cat output/video_generation.log
```

常见问题：
1. **API Key 无效**：检查 .env 文件
2. **网络错误**：检查网络连接
3. **配额不足**：等待月度重置或升级账户

### Q：支持其他语言吗？

**A：** 支持！ElevenLabs 支持 29+ 种语言。修改漫剧生成参数即可。

---

## 📱 分享你的视频

生成完成后，可以：

### YouTube
- 直接上传 MP4 文件
- 标题：「AI 生成」100岁老人修仙漫剧
- 描述：使用 DeepSeek、Stable Diffusion、ElevenLabs 等 AI 工具生成

### 抖音/快手
- 转换为竖屏格式
- 添加热门音乐和话题标签
- 视频时长：15-60 秒

### 哔哩哔哩
- 直接上传 MP4
- 分类：番剧、动画、创意视频
- 获得平台认可和推荐

### Instagram/TikTok
- 竖屏格式
- 添加字幕效果
- 使用热门音乐和话题

---

## 🎯 下一步行动

- [ ] 注册获取 API Key（Stable Diffusion + ElevenLabs）
- [ ] 安装 FFmpeg
- [ ] 克隆项目并安装依赖
- [ ] 配置 .env 文件
- [ ] 运行 `python examples/generate_video_now.py`
- [ ] 等待视频生成完成
- [ ] 播放和检查视频
- [ ] 分享到社交媒体
- [ ] 享受点赞和评论！

---

## 💬 需要帮助？

- **GitHub Issues**：https://github.com/huhuugt/xianxia-manga-ai/issues
- **文档**：查看 `README.md` 和 `VIDEO_GENERATION_GUIDE.md`
- **日志**：`output/video_generation.log`

---

## 🎉 准备好了吗？

现在你已经拥有了生成 AI 修仙漫剧视频的所有工具！

**立即开始**：

```bash
python examples/generate_video_now.py
```

**祝你的视频获得百万级播放！** 🚀✨🧙

---

*最后更新：2026-06-08*

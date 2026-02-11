# Quality Resources Hub - 高质量资源导航

精选开发者必备的高质量网站和工具

🌐 **在线访问：** https://tigg2025.github.io/quality-resources-hub/

## 🎯 设计理念

### 双重友好
1. **人类友好** - 精美界面，方便浏览和搜索
2. **机器友好** - 结构化数据，方便程序读取和维护

## 📁 项目结构

```
quality-resources-hub/
├── index.html          # 网页界面（人类查看）
├── resources.json      # 结构化数据（机器读取）
├── maintain.py         # 维护脚本（自动检查）
└── README.md          # 项目说明
```

## 🤖 机器友好特性

### 1. 结构化数据 (resources.json)
```json
{
  "meta": {
    "title": "高质量资源导航",
    "lastUpdate": "2026-02-11",
    "version": "1.0.0"
  },
  "categories": [
    {
      "id": "ai-tools",
      "name": "AI 开发工具",
      "resources": [
        {
          "name": "ClawHub",
          "url": "https://clawhub.ai",
          "description": "...",
          "tags": ["OpenClaw", "Skills"],
          "status": "active",
          "addedDate": "2026-02-11",
          "lastChecked": "2026-02-11"
        }
      ]
    }
  ]
}
```

### 2. 维护脚本 (maintain.py)

**检查所有资源可用性：**
```bash
python maintain.py check
```

**列出所有活跃资源：**
```bash
python maintain.py list
```

**按标签搜索：**
```bash
python maintain.py tag OpenClaw
```

### 3. 程序化访问

**Python示例：**
```python
import json
import requests

# 读取资源数据
response = requests.get('https://tigg2025.github.io/quality-resources-hub/resources.json')
data = response.json()

# 获取所有AI工具
for category in data['categories']:
    if category['id'] == 'ai-tools':
        for resource in category['resources']:
            print(f"{resource['name']}: {resource['url']}")
```

**JavaScript示例：**
```javascript
// 在网页中使用
fetch('resources.json')
  .then(res => res.json())
  .then(data => {
    // 处理数据
    console.log(data.categories);
  });
```

## 👥 人类友好特性

### 1. 精美界面
- 渐变色设计
- 卡片悬停效果
- 响应式布局

### 2. 实时搜索
- 支持标题搜索
- 支持描述搜索
- 支持标签搜索

### 3. 统计信息
- 总资源数
- 分类数
- 最后更新时间

### 4. 状态标识
- ✅ 正常资源
- ❌ 失效资源（灰色显示）

## 🔄 维护流程

### 定期检查（建议每周）
```bash
# 1. 检查所有资源
python maintain.py check

# 2. 查看结果，处理失效资源

# 3. 提交更新
git add resources.json
git commit -m "Update: 检查资源可用性"
git push
```

### 添加新资源
1. 编辑 `resources.json`
2. 添加到对应分类的 `resources` 数组
3. 提交并推送

### 删除失效资源
1. 从 `resources.json` 中删除
2. 提交并推送

## 📊 资源分类

### 🤖 AI 开发工具
- ClawHub, YouSkill, Vercel Skills
- Hugging Face, Papers with Code

### 👥 开发者社区
- GitHub, Stack Overflow, Dev.to

### 📚 技术文档
- MDN Web Docs, DevDocs

### 🛠️ 工具和框架
- npm, PyPI

### 🎨 设计和UI资源
- Dribbble, Figma Community

### 📰 新闻和趋势
- Hacker News, Product Hunt

### ☁️ 云服务和部署
- 百度智能云, Vercel, Railway

### 🔌 API和数据
- RapidAPI, Public APIs

## 🚀 本地开发

```bash
# 克隆仓库
git clone https://github.com/tigg2025/quality-resources-hub.git
cd quality-resources-hub

# 直接打开 index.html 查看
open index.html

# 或使用本地服务器
python -m http.server 8000
# 访问 http://localhost:8000
```

## 📝 贡献指南

欢迎提交 Pull Request 添加更多高质量资源！

**提交要求：**
- 资源必须是高质量的
- 必须可以正常访问
- 提供清晰的描述
- 添加合适的标签

## 📄 许可

MIT License

---

💡 持续更新中 | 由 OpenClaw 驱动

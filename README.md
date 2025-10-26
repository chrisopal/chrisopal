# 词海日程（ChrisOpal Vocabulary Planner）

一个前后端分离的多终端背单词解决方案，满足多考试难度、每日词量自定义、自动复习、收藏、发音示例与 AI 学情分析等需求。前端采用 React（CDN+Babel 模式）构建自适应界面，可运行在移动端浏览器和微信小程序 WebView；后端使用 Python FastAPI 提供单词数据、复习计划、收藏与统计接口。

## 功能概览

- 📚 **多难度词库**：支持初中、高中、大学 CET4/CET6、雅思、托福六大词表，含发音、释义、场景、例句与配图。
- ⚙️ **每日词量自定义**：默认 10 词，可在 5-30 之间调节，自动计算每日词单并循环覆盖词库。
- 🔁 **智能复习**：自动记录错词，次日加入“回顾复习”区块强化记忆。
- 🗣️ **即时发音**：调用浏览器 SpeechSynthesis 朗读单词。
- 📝 **多题型测验**：每日生成选择题、完形填空、阅读理解等巩固题；测验弹窗可随时关闭再进入。
- ⭐ **收藏夹**：手动收藏或自动加入错题，便于反复巩固。
- 📊 **AI 学情分析**：后端根据答题表现输出错词统计与复习建议。
- 📱 **多端自适应**：流式布局兼容 iOS/Android 浏览器与微信小程序 WebView。

## 目录结构

```text
├── backend/              # FastAPI 服务
│   ├── data/word_sets.py # 词库数据
│   ├── main.py           # API 入口
│   └── state.json        # 简易持久化（配置、历史、收藏）
├── public/
│   ├── index.html        # React 挂载入口
│   ├── app.jsx           # 前端逻辑（Babel 运行时）
│   └── styles.css        # 界面样式
└── README.md
```

## 本地运行

### 1. 启动后端（FastAPI）

```bash
python -m venv .venv
source .venv/bin/activate  # Windows 使用 .venv\Scripts\activate
pip install -r requirements.txt
uvicorn backend.main:app --reload --port 8000
```

### 2. 启动前端静态站点

在另一个终端窗口运行：

```bash
python3 -m http.server 5173 --directory public
```

随后访问 [http://localhost:5173](http://localhost:5173) 即可使用应用（前端默认向 `http://localhost:8000` 发起 API 请求）。

> 若部署到其他环境，确保前端可访问后端 API；可根据部署域名配置反向代理或 CORS。

## API 概览

- `GET /api/config`：获取当前难度、每日词量、收藏等配置。
- `POST /api/config`：更新难度或每日词量，参数示例 `{ "difficulty": "ielts", "words_per_day": 15 }`。
- `GET /api/words?date=YYYY-MM-DD`：获取目标日期的新词、复习词与测验题。
- `POST /api/progress`：提交测验结果，自动生成复习名单与学情分析。
- `POST /api/favorite`：收藏/取消收藏某个单词。
- `GET /api/stats?date=YYYY-MM-DD`：查询每日统计与 AI 分析。

## 开发提示

- 词库数据位于 `backend/data/word_sets.py`，可按需扩展或接入数据库。
- `backend/state.json` 仅用于示例级持久化，生产环境请改用数据库或缓存。
- 前端若需集成到打包框架（Vite、CRA 等），可将 `app.jsx` 拆分为模块化 React 组件。

欢迎根据自身需求进一步拓展题型、复习算法或账号体系。祝学习顺利！

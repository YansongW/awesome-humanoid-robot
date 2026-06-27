# 人形机器人知识图谱 Web 前端

一个基于 FastAPI + Jinja2 的维基百科风格浏览器，支持：

- 浏览知识图谱中所有条目（设计、制造、算法、量产等）
- 关键词搜索
- 查看单个条目的摘要、正文、领域、层级、关系
- 自然语言提问，由 AI 基于检索到的图谱内容作答

## 运行

在项目根目录的虚拟环境中执行：

```bash
source .venv/bin/activate
uvicorn web.app:app --reload --host 0.0.0.0 --port 8000
```

然后打开 http://localhost:8000。

## 配置 LLM

问答功能依赖 `scripts/ai4sci_lib/llm_client.py`，需要设置环境变量：

```bash
export OPENAI_API_KEY="sk-..."
# 或
export AI4SCI_API_KEY="sk-..."
```

如果使用 Kimi CLI 作为后端，可设置：

```bash
export AI4SCI_USE_KIMI_CLI=1
```

## 数据

应用启动时会自动加载：

- `research/**/*.md` —— 实体/条目
- `data/relationships/*.md` —— 关系

新增或修改这些 Markdown 文件后，重启服务即可生效。

## API

- `GET /api/search?q=<关键词>&top_k=10` —— 搜索条目
- `GET /api/entry/<entry_id>` —— 获取单个条目 JSON
- `POST /api/ask` (form: `question`) —— 自然语言问答

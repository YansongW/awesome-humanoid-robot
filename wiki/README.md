# 人形机器人：从矿山到市场

> 基于 [Awesome Humanoid Robot](https://github.com/YansongW/awesome-humanoid-robot) 知识图谱的 Wiki 项目。

## 项目简介

本项目将 Awesome Humanoid Robot 知识图谱整理为公开可读的 Wiki，采用 MkDocs + Material 主题构建，作为 KG 网站的内容子项目。

## 本地预览

### 环境要求

- Python 3.9+
- pip

### 安装依赖

```bash
pip install mkdocs-material mkdocs-minify-plugin mkdocs-mermaid2-plugin
```

### 启动本地服务器

```bash
mkdocs serve
```

然后访问 http://127.0.0.1:8000。

### 构建站点

```bash
mkdocs build
```

构建产物位于 `site/` 目录。

## 部署到 GitHub Pages

```bash
mkdocs gh-deploy
```

Wiki 内容已通过主仓库 KG 网站（https://kg.rounds-tech.com/wiki/）呈现。

## 目录结构

```
wiki/
├── docs/                      # 文档源文件
│   ├── index.md              # 首页
│   ├── table-of-contents.md  # 全书目录
│   ├── chapters/             # 正文章节
│   │   ├── chapter-01.md
│   │   ├── chapter-02.md
│   │   └── ...
│   ├── appendices/           # 附录
│   │   └── ...
│   └── assets/               # 静态资源
│       ├── stylesheets/
│       └── images/
├── mkdocs.yml                # MkDocs 配置
├── overrides/                # 主题覆盖
└── README.md                 # 本文件
```

## 写作规范

详见 `../AGENTS.md`。

## 许可

本书内容采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 许可协议。

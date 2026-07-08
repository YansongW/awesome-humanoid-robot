# Rounds Tech KG 静态站点

这是 `awesome-humanoid-robot` 知识图谱的产品级静态前端，部署在 GitHub Pages，通过 `rounds-tech.com` 访问。

## 本地开发

```bash
# 1. 进入项目根目录并激活虚拟环境
cd /Users/yansong/Desktop/awesome-humanoid-robot
source .venv/bin/activate

# 2. 安装依赖
pip install -r website/requirements.txt

# 3. 构建静态站点
python -m website.builder.build

# 4. 本地预览
python -m http.server 8080 --directory website/dist
```

然后打开 http://localhost:8080。

## 目录结构

```
website/
├── builder/           # 静态站点构建脚本
│   ├── loader.py      # 加载 research/ 和 data/relationships/
│   ├── search_index.py# 生成搜索索引和关系图数据
│   ├── renderer.py    # 渲染 HTML
│   └── build.py       # 构建入口
├── templates/         # Jinja2 HTML 模板
├── src/               # 前端静态资源（CSS/JS）
│   ├── css/main.css
│   └── js/{app,search,graph}.js
└── dist/              # 构建输出（GitHub Pages 源）
```

## 自动部署

每次推送到 `main` 分支时，`.github/workflows/deploy.yml` 会自动：

1. 安装 Python 依赖
2. 运行 `python -m website.builder.build`
3. 将 `website/dist/` 部署到 GitHub Pages

## 域名配置

`CNAME` 文件已放置在仓库根目录，内容为 `rounds-tech.com`。请在域名注册商处将 `rounds-tech.com` 的 A 记录指向 GitHub Pages IP：

- 185.199.108.153
- 185.199.109.153
- 185.199.110.153
- 185.199.111.153

然后在仓库 Settings → Pages 中确认源为 "GitHub Actions"。

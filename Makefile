# 人形机器人知识图谱 — 常用任务入口
# 用法：make <target>（先 source .venv/bin/activate 或确保 python 指向 .venv）

PYTHON ?= python
VENV := .venv
PY := $(if $(wildcard $(VENV)/bin/python),$(VENV)/bin/python,$(PYTHON))

.PHONY: help site audit kg roadmap-check ingest gui serve clean

help: ## 显示全部可用命令
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  make %-14s %s\n", $$1, $$2}'

site: ## 构建静态站（zh + en + ko → website/dist）
	$(PY) -m website.builder.build

audit: ## 运行知识图谱质量审计（JSON 报告 → .staging/quality_reports/）
	$(PY) scripts/audit_entry_quality.py --json-only

kg: audit ## 审计并打印连通性摘要（边数/零度/悬空）
	@$(PY) -c "import json,glob;r=json.load(open(sorted(glob.glob('.staging/quality_reports/quality_report_*.json'))[-1]));rel=r['relationships'];c=rel['connectivity'];print(f\"entries={r['total_entries']} edges={rel['total']} dangling={len(rel['dangling'])} dup={len(rel['duplicates'])} zero={c['zero_degree_count']} ({c['zero_degree_ratio']:.1%}) avg_degree={c['avg_degree']}\")"

roadmap-check: ## 重新生成路线图↔卡片绑定并校验链接有效性
	$(PY) scripts/build_roadmap_mapping.py

ingest: ## 列出可用的摄取/挖掘脚本（按需单独运行）
	@echo "关系挖掘:    $(PY) scripts/build_latent_relationships.py [--write]"
	@echo "零度挂接:    $(PY) scripts/link_zero_degree_entities.py [--write] [--llm --write]"
	@echo "LLM 分型:    $(PY) scripts/llm_classify_relations.py [--write]"
	@echo "暂存提升:    $(PY) scripts/auto_promote_staging.py"

gui: ## 启动本地 Web GUI（http://127.0.0.1:8000）
	$(PY) -m uvicorn web.app:app --host 127.0.0.1 --port 8000

serve: site ## 构建并在本地预览静态站（http://127.0.0.1:8080）
	cd website/dist && $(PY) -m http.server 8080

clean: ## 清理构建产物（website/dist）
	rm -rf website/dist

---
id: ent_company_biren
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 壁仞科技
  en: 壁仞科技
status: active
sources:
- id: src_biren_official
  type: website
  url: https://www.birentech.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 壁仞科技 / 壁仞科技

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 壁仞科技 |
| **英文名** | Biren Technology |
| **总部** | 中国上海市 |
| **成立时间** | 2019 年 |
| **官网** | [https://www.birentech.com](https://www.birentech.com) |
| **供应链环节** | 通用 GPU、AI 训练/推理芯片、智算中心、国产算力 |
| **企业属性** | 独角兽、国产 GPU 独角兽 |
| **母公司/所属集团** | 无（独立主体） |
| **数据来源** | 壁仞官网、产品发布会、公开新闻稿、行业研报 |

## 公司简介

壁仞科技专注于通用 GPU 研发，提供高性能 AI 训练与推理芯片，致力于打造国产自主可控的算力底座。

壁仞科技是中国通用 GPU 领域的代表企业之一，核心产品 BR100 系列基于自研 Biren 架构，面向大模型训练、推理与高性能计算。公司强调软硬件协同，提供 BIRENSUPA 软件栈，并积极参与国产智算中心建设。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 通用 GPU 芯片 | AI 训练/推理与 HPC | BR100 / BR104 | 大模型、AIGC、科学计算 |
| 加速卡与服务器 | 数据中心 AI 加速 | BR100 加速卡 / OAM 模组 | 智算中心、云计算 |
| 软件栈 | 编译器与开发工具 | BIRENSUPA | AI 框架适配、模型迁移 |

## 代表产品

### 壁仞 BR100 系列 GPU

> 壁仞 BR100 系列 GPU：请访问 [官方资料](https://www.birentech.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 架构 | Biren 自研通用 GPU 架构 | 壁仞公开资料 |
| 制程 | 7 nm | 公开报道 |
| 晶体管数 | 约 770 亿 | 壁仞发布会 |
| 算力 | FP32 约 1000 TFLOPS；BF16/FP16 约 2000 TFLOPS | 壁仞公开资料 |
| 显存 | 64 GB HBM2e / HBM3 | 公开报道 |
| 互联 | BLink 片间互联 | 壁仞公开资料 |
| 功耗 | 约 550 W | 公开报道 |
| 价格 | 未公开 | - |

**技术亮点**：国产高性能通用 GPU、大算力与高带宽显存、BLink 高速互联、支持大模型训练推理。

**应用场景**：大模型训练、AIGC、科学计算、智算中心。

### 壁仞 BIRENSUPA 软件平台

> 壁仞 BIRENSUPA 软件平台：请访问 [官方资料](https://www.birentech.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 组成 | 驱动、编译器、运行时、算子库 | 壁仞公开资料 |
| 框架支持 | PyTorch、TensorFlow、PaddlePaddle 等 | 壁仞公开资料 |
| 模型库 | 大模型、CV、NLP 示例 | 壁仞公开资料 |
| 迁移工具 | 模型迁移与性能调优工具 | 壁仞公开资料 |
| 部署方式 | 本地 / 集群 / 云 | 未公开 |
| 开发语言 | Python / C++ | 壁仞公开资料 |
| 许可 | 未公开 | - |
| 价格 | 随硬件提供 | 未公开 |

**技术亮点**：国产 GPU 软件栈、主流 AI 框架适配、降低模型迁移成本。

**应用场景**：AI 模型训练与推理、国产算力适配、智算中心运营。

## 供应链位置

- **上游关键零部件/材料**：晶圆代工（台积电/国产代工厂）、HBM 存储、封测、EDA 工具、IP 核。
- **下游客户/应用场景**：互联网大厂、智算中心、科研院所、AI 初创企业、云计算厂商。
- **主要竞争对手/对标**：NVIDIA A100/H100、AMD MI 系列、华为昇腾、海光信息、寒武纪。

## 知识图谱节点与关系

- 公司实体：`ent_company_biren`
- 产品实体：`ent_product_biren_br100`、`ent_product_biren_supa`
- 关键关系：
  - `ent_company_biren` -- `manufactures` --> `ent_product_biren_br100`
  - `ent_company_biren` -- `manufactures` --> `ent_product_biren_supa`
  - `ent_product_biren_br100` -- `uses` --> `ent_component_hbm_memory`
  - `ent_product_biren_br100` -- `runs_with` --> `ent_product_biren_supa`

## 参考资料

1. [官网](https://www.birentech.com)
2. [壁仞科技官网](https://www.birentech.com)
3. 壁仞 BR100 产品发布会资料
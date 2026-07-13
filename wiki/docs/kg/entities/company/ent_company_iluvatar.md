---
id: ent_company_iluvatar
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 天数智芯
  en: Iluvatar CoreX
status: active
sources:
- id: src_iluvatar_official
  type: website
  url: https://www.iluvatar.com.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 天数智芯 / Iluvatar CoreX

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 天数智芯 |
| **英文名** | Iluvatar CoreX |
| **总部** | 中国上海市浦东新区 |
| **成立时间** | 2015 年 |
| **官网** | [https://www.iluvatar.com.cn](https://www.iluvatar.com.cn) |
| **供应链环节** | 通用 GPU、AI 训练/推理芯片、国产算力 |
| **企业属性** | 独角兽、国产 GPU 企业 |
| **母公司/所属集团** | 无（独立主体） |
| **数据来源** | 天数智芯官网、产品发布会、公开新闻稿、行业研报 |

## 公司简介

天数智芯是中国专注于通用 GPU 与高性能计算芯片设计的企业，致力于打造自主可控的云端 AI 训练与推理算力。

天数智芯推出“天垓”系列通用 GPU 加速卡与“智铠”系列推理加速卡，采用自研通用 GPU 架构，兼容主流 CUDA 生态，支持大模型训练、推理及科学计算。其产品定位国产替代，为智算中心、互联网、金融及科研提供高性能算力。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 天垓系列 | 通用 GPU 训练加速卡 | 天垓 100 / 200 | 大模型训练、HPC |
| 智铠系列 | AI 推理加速卡 | 智铠 100 / 200 | 大模型推理、CV、推荐 |
| 软件栈 | 芯片使能与开发工具 | 天数智芯软件栈 | 全系列加速卡 |

## 代表产品

### 天数智芯天垓 200（BI-V200）

> 天数智芯天垓 200：请访问 [官方资料](https://www.iluvatar.com.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 架构 | 自研通用 GPU 架构 | 天数智芯公开资料 |
| 制程 | 7 nm（公开报道） | 公开报道 |
| 算力 | FP16 / BF16 / FP32 数百 TFLOPS 级 | 天数智芯公开资料 |
| 显存 | 32 GB HBM2e（部分型号） | 公开报道 |
| 互联 | 支持多卡互联 | 天数智芯公开资料 |
| 接口 | PCIe Gen4 / OAM | 公开报道 |
| 功耗 | 约 300–350 W | 公开报道 |
| 价格 | 未公开 | - |

**技术亮点**：通用 GPU 架构、CUDA 兼容、支持大规模并行计算、配套完整软件栈。

**应用场景**：大模型训练、AIGC、科学计算、智算中心、机器人仿真与训练。

### 天数智芯智铠 100（MR-V100）

> 天数智芯智铠 100：请访问 [官方资料](https://www.iluvatar.com.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 定位 | 云端 AI 推理 | 天数智芯公开资料 |
| 算力 | INT8 / FP16 高吞吐 | 天数智芯公开资料 |
| 显存 | 未公开 | - |
| 接口 | PCIe Gen4 | 公开报道 |
| 能效 | 未公开 | - |
| 软件栈 | 天数智芯推理软件栈 | 天数智芯公开资料 |
| 功耗 | 约 150 W | 公开报道 |
| 价格 | 未公开 | - |

**技术亮点**：高推理吞吐、低延迟、与训练卡统一架构与软件生态。

**应用场景**：大模型推理、推荐系统、视频分析、智能客服、具身智能云端推理。

## 供应链位置

- **上游关键零部件/材料**：晶圆代工、HBM 存储、封测、EDA/IP、服务器、高速互连。
- **下游客户/应用场景**：互联网大厂、云计算厂商、智算中心、AI 企业、科研院所、机器人公司。
- **主要竞争对手/对标**：NVIDIA A100/H100、AMD MI 系列、华为昇腾、壁仞科技、沐曦。

## 知识图谱节点与关系

- 公司实体：`ent_company_iluvatar`
- 产品实体：`ent_product_iluvatar_biv200`
- 零部件实体：`ent_component_iluvatar_biv200_gpu`
- 关键关系：
  - `ent_company_iluvatar` -- `manufactures` --> `ent_product_iluvatar_biv200`
  - `ent_company_iluvatar` -- `manufactures` --> `ent_component_iluvatar_biv200_gpu`
  - `ent_product_iluvatar_biv200` -- `uses` --> `ent_component_iluvatar_biv200_gpu`

## 参考资料

1. [天数智芯官网](https://www.iluvatar.com.cn)
2. [天数智芯产品页](https://www.iluvatar.com.cn/product/)
3. 天数智芯产品发布会资料
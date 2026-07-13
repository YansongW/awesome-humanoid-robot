# 登临科技 / Denglai Technology

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 登临科技 |
| **英文名** | Denglai Technology |
| **总部** | 中国上海市浦东新区 |
| **成立时间** | 2017 年 |
| **官网** | [https://www.denglai.com.cn](https://www.denglai.com.cn) |
| **供应链环节** | 通用 GPU、AI 推理/训练芯片、国产算力 |
| **企业属性** | 独角兽、国产 GPU 企业 |
| **母公司/所属集团** | 无（独立主体） |
| **数据来源** | 登临科技官网、产品发布会、公开新闻稿、行业研报 |

## 公司简介

登临科技是中国专注于通用 GPU 与人工智能加速器设计的企业，以“GPU+”创新架构为核心，提供高效能 AI 计算产品。

登临科技提出 GPU+（GPGPU 加 AI 加速）架构，兼顾图形/通用计算与深度学习加速，推出 Goldwasser 系列加速卡。其产品强调高算力利用率、低功耗与 CUDA 兼容，广泛应用于云端推理、边缘计算、智算中心及大模型部署。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| Goldwasser 系列 | 云端 AI 训练/推理加速卡 | Goldwasser X / L / S 系列 | 大模型推理、CV、NLP |
| 边缘/行业方案 | 边缘 AI 与行业一体机 | 行业定制方案 | 智能制造、智慧城市 |
| 软件栈 | 芯片使能与开发工具 | Denglai 软件栈 | 全系列加速卡 |

## 代表产品

### 登临科技 Goldwasser X（髙 Goldwasser-XL）

> 登临科技 Goldwasser X：请访问 [官方资料](https://www.denglai.com.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 架构 | GPU+ 创新架构（GPGPU + AI 加速） | 登临科技公开资料 |
| 制程 | 7 nm（公开报道） | 公开报道 |
| 算力 | INT8 / FP16 高吞吐（数百 TOPS 级） | 登临科技公开资料 |
| 显存 | 32 GB HBM2e（部分型号） | 公开报道 |
| 互联 | 支持多卡互联 | 登临科技公开资料 |
| 接口 | PCIe Gen4 | 公开报道 |
| 功耗 | 约 150–300 W（视型号） | 公开报道 |
| 价格 | 未公开 | - |

**技术亮点**：GPU+ 架构兼顾通用计算与 AI 加速、高算力利用率、CUDA 兼容、支持多精度推理。

**应用场景**：大模型推理、AIGC、推荐系统、视频分析、智算中心。

### 登临科技 Goldwasser-L（边缘推理）

> 登临科技 Goldwasser L：请访问 [官方资料](https://www.denglai.com.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 定位 | 边缘/轻量推理 | 登临科技公开资料 |
| 算力 | INT8 数十至百 TOPS 级 | 登临科技公开资料 |
| 显存 | 未公开 | - |
| 接口 | PCIe / M.2 | 公开报道 |
| 功耗 | 约 25–75 W | 公开报道 |
| 软件栈 | 登临科技 SDK | 登临科技公开资料 |
| 应用场景 | 边缘计算、机器人端侧推理 | 登临科技公开资料 |
| 价格 | 未公开 | - |

**技术亮点**：低功耗边缘推理、紧凑形态、与云端卡统一软件栈。

**应用场景**：边缘盒子、机器人感知、工业质检、智慧城市。

## 供应链位置

- **上游关键零部件/材料**：晶圆代工、HBM 存储、封测、EDA/IP、PCB、散热。
- **下游客户/应用场景**：互联网大厂、云计算厂商、智算中心、AI 企业、机器人公司、科研院所。
- **主要竞争对手/对标**：NVIDIA T4/L4、寒武纪、燧原科技、天数智芯、沐曦。

## 知识图谱节点与关系

- 公司实体：`ent_company_denglai`
- 产品实体：`ent_product_denglai_goldwasser_x`
- 零部件实体：`ent_component_denglai_goldwasser_x_accelerator`
- 关键关系：
  - `ent_company_denglai` -- `manufactures` --> `ent_product_denglai_goldwasser_x`
  - `ent_company_denglai` -- `manufactures` --> `ent_component_denglai_goldwasser_x_accelerator`
  - `ent_product_denglai_goldwasser_x` -- `uses` --> `ent_component_denglai_goldwasser_x_accelerator`

## 参考资料

1. [登临科技官网](https://www.denglai.com.cn)
2. [登临科技产品页](https://www.denglai.com.cn/product/)
3. 登临科技产品发布会资料
---
id: ent_company_enflame
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 燧原科技
  en: 燧原科技
status: active
sources:
- id: src_enflame_official
  type: website
  url: https://www.enflame-tech.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 燧原科技 / 燧原科技

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 燧原科技 |
| **英文名** | Enflame Technology |
| **总部** | 中国上海市 |
| **成立时间** | 2018 年 |
| **官网** | [https://www.enflame-tech.com](https://www.enflame-tech.com) |
| **供应链环节** | AI 训练/推理芯片、云端 AI 加速、智算中心、国产算力 |
| **企业属性** | 独角兽、国产 AI 芯片企业 |
| **母公司/所属集团** | 无（独立主体） |
| **数据来源** | 燧原官网、产品发布会、公开新闻稿、行业研报 |

## 公司简介

燧原科技专注人工智能云端算力产品，提供 AI 训练与推理加速卡及系统，助力国产智算中心建设。

燧原科技是中国云端 AI 芯片代表企业，自研 GCU 架构，推出云燧 T 系列训练芯片/加速卡与云燧 i 系列推理芯片/加速卡。产品强调高算力、高能效比与大规模集群互联，配套 GCU-LARE 互联技术与驭算软件栈。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 训练加速卡 | 云端大模型训练 | 云燧 T20 / T21 | 大模型训练、AIGC |
| 推理加速卡 | 云端 AI 推理 | 云燧 i20 / i10 | 大模型推理、推荐、CV |
| 集群与软件 | 大规模 AI 集群与工具链 | 云燧智算集群 / 驭算 | 智算中心、超算 |

## 代表产品

### 燧原云燧 T20 / T21 训练加速卡

> 燧原云燧 T20 / T21 训练加速卡：请访问 [官方资料](https://www.enflame-tech.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 架构 | 自研 GCU 架构 | 燧原公开资料 |
| 制程 | 未公开 | - |
| 算力 | FP32/BF16/FP16 数百 TFLOPS 级 | 燧原公开资料 |
| 显存 | HBM2e | 公开报道 |
| 互联 | GCU-LARE 片间互联 | 燧原公开资料 |
| 功耗 | 约 300–350 W | 公开报道 |
| 形态 | 双宽全高 PCIe 加速卡 / OAM | 燧原公开资料 |
| 价格 | 未公开 | - |

**技术亮点**：国产云端训练芯片、GCU-LARE 高速互联、高能效比、配套大规模智算集群方案。

**应用场景**：大模型训练、AIGC、科学计算、智算中心。

### 燧原云燧 i20 推理加速卡

> 燧原云燧 i20 推理加速卡：请访问 [官方资料](https://www.enflame-tech.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 定位 | 云端 AI 推理 | 燧原公开资料 |
| 算力 | INT8/FP16 高吞吐 | 燧原公开资料 |
| 显存 | 未公开 | - |
| 接口 | PCIe Gen4 | 公开报道 |
| 能效 | 未公开 | - |
| 支持模型 | CV、NLP、大模型推理 | 燧原公开资料 |
| 软件栈 | 驭算 | 燧原公开资料 |
| 价格 | 未公开 | - |

**技术亮点**：高推理吞吐、低延迟、与训练卡统一软件栈、适配国产智算中心。

**应用场景**：大模型推理、推荐系统、视频分析、智能客服。

## 供应链位置

- **上游关键零部件/材料**：晶圆代工、HBM 存储、封测、EDA、服务器、高速互连 IP。
- **下游客户/应用场景**：互联网大厂、云计算厂商、智算中心、AI 企业、科研院所。
- **主要竞争对手/对标**：NVIDIA A100/H100、华为昇腾、寒武纪、壁仞科技、沐曦。

## 知识图谱节点与关系

- 公司实体：`ent_company_enflame`
- 产品实体：`ent_product_enflame_yunsui_t20`、`ent_product_enflame_yunsui_i20`
- 关键关系：
  - `ent_company_enflame` -- `manufactures` --> `ent_product_enflame_yunsui_t20`
  - `ent_company_enflame` -- `manufactures` --> `ent_product_enflame_yunsui_i20`
  - `ent_product_enflame_yunsui_t20` -- `uses` --> `ent_component_hbm_memory`
  - `ent_product_enflame_yunsui_i20` -- `uses` --> `ent_component_pcie_interface`

## 参考资料

1. [官网](https://www.enflame-tech.com)
2. [燧原科技官网](https://www.enflame-tech.com)
3. 燧原产品发布会资料
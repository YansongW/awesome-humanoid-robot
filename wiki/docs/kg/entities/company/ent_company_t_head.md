---
id: ent_company_t_head
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 平头哥半导体
  en: T-Head Semiconductor
status: active
sources:
- id: src_t_head_official
  type: website
  url: https://www.t-head.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 平头哥半导体 / T-Head Semiconductor

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 平头哥半导体 |
| **英文名** | T-Head Semiconductor |
| **总部** | 中国浙江省杭州市 |
| **成立时间** | 2018 年 |
| **官网** | [https://www.t-head.cn](https://www.t-head.cn) |
| **供应链环节** | RISC-V/ARM 处理器 IP、AI 芯片、云计算芯片、嵌入式计算 |
| **企业属性** | 阿里巴巴集团全资子公司 |
| **母公司/所属集团** | 阿里巴巴集团 |
| **数据来源** | 平头哥官网、阿里云栖大会资料、产品手册、公开新闻稿 |

## 公司简介

平头哥半导体是阿里巴巴旗下的芯片公司，聚焦 RISC-V 与 ARM 架构处理器 IP、AI 加速芯片及云计算芯片研发。

平头哥以“玄铁”RISC-V 处理器 IP、“含光”AI 推理芯片及“倚天”ARM 服务器 CPU 为核心产品线，构建端-边-云全栈算力。其 RISC-V 生态与 AI 加速能力为机器人、物联网及边缘智能提供高灵活性与高能效比的计算方案。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 玄铁 RISC-V | RISC-V 处理器 IP | 玄铁 C906 / C910 / C920 / R908 | MCU、边缘 AI、机器人控制 |
| 含光 AI 芯片 | 云端/边缘 AI 推理 | 含光 800 | 数据中心、云计算 AI 推理 |
| 倚天 CPU | 云原生服务器 CPU | 倚天 710 | 云计算、服务器 |
| 无剑平台 | SoC 设计平台 | 无剑 100 / 600 | 芯片定制 |

## 代表产品

### 平头哥玄铁 C920

> 平头哥玄铁 C920：请访问 [官方资料](https://www.t-head.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 架构 | RISC-V RV64GC + Vector 1.0 | 平头哥公开资料 |
| 流水线 | 12 级乱序超标量 | 平头哥公开资料 |
| 主频 | 最高 3 GHz（公开报道） | 公开报道 |
| 算力 | 未公开 | - |
| 缓存 | 支持多级缓存 | 平头哥公开资料 |
| 接口 | AXI / ACE 等标准总线 | 平头哥公开资料 |
| 功耗 | 视实现场景而定 | 平头哥公开资料 |
| 价格 | IP 授权，未公开 | - |

**技术亮点**：高性能 RISC-V 内核、支持 Vector 向量扩展、可集成 AI 加速器、开源软件生态丰富。

**应用场景**：边缘 AI 计算、机器人主控 MCU/MPU、工业控制、AIoT。

### 平头哥含光 800

> 平头哥含光 800：请访问 [官方资料](https://www.t-head.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 架构 | 自研深度神经网络推理架构 | 平头哥公开资料 |
| 制程 | 12 nm（公开报道） | 公开报道 |
| 算力 | INT8 最高约 80,000 TOPS（峰值） | 平头哥公开资料 |
| 内存 | HBM2 | 公开报道 |
| 接口 | PCIe Gen3 x16 | 公开报道 |
| 功耗 | 未公开 | - |
| 应用场景 | 数据中心 AI 推理、视觉识别 | 平头哥公开资料 |
| 价格 | 未公开 | - |

**技术亮点**：高推理吞吐、低延迟、针对电商/视觉/搜索场景优化、与阿里云业务深度融合。

**应用场景**：云端图像识别、视频分析、推荐系统、大模型推理加速。

## 供应链位置

- **上游关键零部件/材料**：晶圆代工、封测、HBM/存储、EDA/IP、PCB、散热。
- **下游客户/应用场景**：阿里云、物联网设备商、芯片设计公司、机器人整机厂、工业自动化企业。
- **主要竞争对手/对标**：ARM Cortex、SiFive、Andes、华为昇腾、寒武纪、NVIDIA T4。

## 知识图谱节点与关系

- 公司实体：`ent_company_t_head`
- 产品实体：`ent_product_t_head_xuantie_c920`
- 零部件实体：`ent_component_t_head_xuantie_c920_ip`
- 关键关系：
  - `ent_company_t_head` -- `manufactures` --> `ent_product_t_head_xuantie_c920`
  - `ent_company_t_head` -- `manufactures` --> `ent_component_t_head_xuantie_c920_ip`
  - `ent_product_t_head_xuantie_c920` -- `uses` --> `ent_component_t_head_xuantie_c920_ip`

## 参考资料

1. [平头哥官网](https://www.t-head.cn)
2. [平头哥玄铁系列](https://www.t-head.cn/product/)
3. 阿里云栖大会公开资料
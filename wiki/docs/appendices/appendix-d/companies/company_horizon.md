# 地平线 / Horizon Robotics

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 地平线 |
| **英文名** | Horizon Robotics |
| **总部** | 中国北京市 |
| **成立时间** | 2015 年 |
| **官网** | [https://www.horizon.ai](https://www.horizon.ai) |
| **供应链环节** | 边缘 AI 芯片、智能驾驶、机器人计算、BPU 架构 |
| **企业属性** | 上市公司（HKEX: 9660）、国内自动驾驶芯片独角兽 |
| **母公司/所属集团** | 无（独立上市主体） |
| **数据来源** | 地平线官网、招股书、公开新闻稿、行业研报 |

## 公司简介

地平线是中国领先的边缘 AI 芯片公司，以自研 BPU 架构为核心，为智能驾驶与机器人提供高性能、低功耗的计算平台。

地平线专注于边缘人工智能芯片及解决方案，自主研发 BPU（Brain Processing Unit）神经网络处理架构，产品覆盖 Journey 系列智能驾驶芯片与 Horizon Mono/ Pilot/ SuperDrive 解决方案。Journey 6 系列面向下一代高阶智驾与具身智能计算，强调算法与芯片协同优化。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| Journey 智能驾驶芯片 | ADAS 与高阶智驾 SoC | Journey 2/3/5/6 系列 | 乘用车、商用车智驾 |
| 机器人/具身智能计算 | 机器人感知与决策计算平台 | Journey 6 / 衍生机器人方案 | 人形机器人、AMR、无人车 |
| 算法与工具链 | 感知/规划算法与开发平台 | Horizon SuperDrive / OpenExplorer | 智能驾驶、机器人开发 |

## 代表产品

### 地平线 Journey 6

> 地平线 Journey 6：请访问 [官方资料](https://www.horizon.ai) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| AI 算力 | Journey 6E：128 TOPS；Journey 6P：560 TOPS | 地平线公开资料 |
| BPU 架构 | BPU 纳什（纳什架构） | 地平线公开资料 |
| 制程 | 未公开 | - |
| CPU | 多核 ARM Cortex-A78AE / 自研安全核 | 公开报道 |
| ISP | 支持多路高分辨率摄像头输入 | 地平线公开资料 |
| 功能安全 | ASIL-D / ASIL-B 等级支持 | 地平线公开资料 |
| 接口 | PCIe、Ethernet、MIPI CSI-2、CAN-FD | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：高算力 BPU、算法-芯片协同设计、面向高阶智驾与具身智能的感知决策一体、支持多传感器融合。

**应用场景**：高阶智能驾驶、人形机器人/AMR 感知与决策、多模态边缘 AI。

### 地平线 Journey 5

> 地平线 Journey 5：请访问 [官方资料](https://www.horizon.ai) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| AI 算力 | 128 TOPS | 地平线官网 |
| BPU 架构 | BPU 贝叶斯 | 地平线官网 |
| CPU | 8 核 ARM Cortex-A55 / 双核 A76 | 公开报道 |
| ISP | 支持 16 路摄像头输入 | 地平线公开资料 |
| 功耗 | 约 30 W | 公开报道 |
| 功能安全 | ASIL-B(D) 目标 | 地平线公开资料 |
| 量产状态 | 已量产上车 | 地平线公开资料 |
| 价格 | 未公开 | - |

**技术亮点**：已大规模量产的高算力智驾芯片、开放工具链、支持行泊一体与高速/城区 NOA。

**应用场景**：乘用车 ADAS/AD、机器人感知、智能交通。

## 供应链位置

- **上游关键零部件/材料**：晶圆代工（台积电/中芯国际等）、封测、存储器、ISP IP、车规认证服务。
- **下游客户/应用场景**：大众、比亚迪、理想、长安等车企；机器人/无人车方案商与开发者。
- **主要竞争对手/对标**：NVIDIA Drive、Mobileye、Qualcomm Snapdragon Ride、黑芝麻智能、华为昇腾。

## 知识图谱节点与关系

- 公司实体：`ent_company_horizon`
- 产品实体：`ent_product_horizon_journey6`、`ent_product_horizon_journey5`
- 关键关系：
  - `ent_company_horizon` -- `manufactures` --> `ent_product_horizon_journey6`
  - `ent_company_horizon` -- `manufactures` --> `ent_product_horizon_journey5`
  - `ent_product_horizon_journey6` -- `uses` --> `ent_component_bpu_nash`
  - `ent_product_horizon_journey5` -- `uses` --> `ent_component_bpu_bayes`

## 参考资料

1. [官网](https://www.horizon.ai)
2. [地平线官网](https://www.horizon.ai)
3. 地平线机器人招股书（HKEX: 9660）
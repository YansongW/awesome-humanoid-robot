---
id: ent_company_qualcomm
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 高通
  en: 高通
status: active
sources:
- id: src_qualcomm_official
  type: website
  url: https://www.qualcomm.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 高通 / 高通

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 高通 |
| **英文名** | Qualcomm |
| **总部** | 美国加利福尼亚州圣迭戈 |
| **成立时间** | 1985 年 |
| **官网** | [https://www.qualcomm.com](https://www.qualcomm.com) |
| **供应链环节** | 移动 SoC、AI 计算、机器人平台、RB5/RB3、无线通信 |
| **企业属性** | 上市公司（NASDAQ: QCOM）、全球无线通信与移动计算龙头 |
| **母公司/所属集团** | 无（Qualcomm Incorporated 为上市主体） |
| **数据来源** | 高通官网、Qualcomm Robotics 官方资料、公开新闻稿 |

## 公司简介

高通通过集成 AI、5G、视觉与连接能力的机器人平台，为 AMR、无人机、服务机器人与人形机器人提供边缘计算与连接底座。

高通是全球领先的无线科技创新者，Snapdragon 平台覆盖智能手机、汽车、XR、PC 与机器人。Qualcomm Robotics 平台（RB3、RB5、RB6、RB1/RB2）集成了高性能 CPU/GPU/NPU、ISP、AI 引擎与 5G/Wi-Fi 连接，支持 ROS 2、AI 推理与多摄像头融合，是机器人开发的主流平台之一。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 机器人平台 | 机器人开发平台与参考设计 | RB5 / RB3 / RB6 / RB1 / RB2 | AMR、无人机、服务机器人、人形机器人 |
| Snapdragon 移动/计算平台 | 移动与边缘 AI 计算 | Snapdragon 8 / X / 7 系列 | 智能终端、XR、机器人 |
| 汽车平台 | 舱驾一体与车联网 | Snapdragon Ride / Cockpit | 智能座舱、自动驾驶 |

## 代表产品

### 高通 RB5 / 机器人开发平台

> 高通 RB5 / 机器人开发平台：请访问 [官方资料](https://www.qualcomm.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| SoC | Qualcomm QRB5165 | 高通官网 |
| AI 算力 | 第 5 代 AI 引擎，15 TOPS | 高通公开资料 |
| CPU | Kryo 585 八核（最高 2.84 GHz） | 高通官网 |
| GPU | Adreno 650 | 高通官网 |
| ISP | 支持 7 个摄像头并发 | 高通官网 |
| 连接 | 5G、Wi-Fi 6、蓝牙 5.1、GPS | 高通官网 |
| 接口 | USB 3.1、PCIe、MIPI CSI、GPIO | 开发套件资料 |
| 价格 | 开发套件约 449 USD（参考价） | 高通/经销商 |

**技术亮点**：5G + AI 一体化机器人平台、异构计算、支持 ROS 2 与机器学习、参考设计丰富。

**应用场景**：AMR、配送机器人、无人机、服务机器人、人形机器人原型开发。

### 高通 RB1 / RB2 机器人平台

> 高通 RB1 / RB2 机器人平台：请访问 [官方资料](https://www.qualcomm.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| SoC | QRB2210（RB1）/ QRB4210（RB2） | 高通官网 |
| AI 算力 | RB2：约 5–7 TOPS | 高通公开资料 |
| CPU | 四核/八核 ARM Cortex | 高通官网 |
| 摄像头 | 支持多路摄像头 | 高通官网 |
| 连接 | Wi-Fi、蓝牙、可选 4G/5G | 高通官网 |
| 尺寸 | 开发板形态 | 开发套件资料 |
| 功耗 | 低功耗设计 | 高通公开资料 |
| 价格 | 未公开 | - |

**技术亮点**：面向中低端机器人的高性价比平台、集成连接与 AI、降低开发门槛。

**应用场景**：小型服务机器人、教育机器人、清洁机器人、IoT 网关。

## 供应链位置

- **上游关键零部件/材料**：台积电/三星代工、ARM IP、存储器、射频前端、基带 IP、传感器合作伙伴。
- **下游客户/应用场景**：机器人 OEM/ODM、AMR 厂商、无人机厂商、车企、手机/PC 厂商。
- **主要竞争对手/对标**：NVIDIA Jetson、Intel Movidius、地平线 Journey、华为昇腾、MediaTek。

## 知识图谱节点与关系

- 公司实体：`ent_company_qualcomm`
- 产品实体：`ent_product_qualcomm_rb5`、`ent_product_qualcomm_rb1_rb2`
- 关键关系：
  - `ent_company_qualcomm` -- `manufactures` --> `ent_product_qualcomm_rb5`
  - `ent_company_qualcomm` -- `manufactures` --> `ent_product_qualcomm_rb1_rb2`
  - `ent_product_qualcomm_rb5` -- `uses` --> `ent_component_qrb5165_soc`
  - `ent_product_qualcomm_rb1_rb2` -- `uses` --> `ent_component_qrb4210_soc`

## 参考资料

1. [官网](https://www.qualcomm.com)
2. [高通官网](https://www.qualcomm.com)
3. [Qualcomm Robotics RB5 页面](https://www.qualcomm.com/products/internet-of-things/industrial/robotics/qualcomm-robotics-rb5-platform)
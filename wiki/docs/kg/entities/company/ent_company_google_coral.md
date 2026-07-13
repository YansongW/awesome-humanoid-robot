---
id: ent_company_google_coral
schema_version: 1
type: company
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Google Coral
  en: Google Coral
status: active
sources:
- id: src_google_coral_official
  type: website
  url: https://coral.ai
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# Google Coral / Google Coral

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | Google Coral |
| **英文名** | Google Coral |
| **总部** | 美国加利福尼亚州山景城 |
| **成立时间** | 2019 年（Coral 产品线发布） |
| **官网** | [https://coral.ai](https://coral.ai) |
| **供应链环节** | Edge TPU、端侧 AI 加速器、AIoT/机器人视觉 |
| **企业属性** | Google / Alphabet 旗下（上市公司 NASDAQ: GOOGL） |
| **母公司/所属集团** | Alphabet / Google |
| **数据来源** | Coral 官网、Google 官方文档、公开产品资料 |

## 公司简介

Google Coral 是 Google 推出的边缘 AI 平台，核心为自研 Edge TPU，可在极低功耗下完成神经网络推理。Coral 提供 Dev Board、USB Accelerator、PCIe/M.2 加速器及 SoM 等多种形态，面向智能相机、机器人、工业检测与 AIoT 设备。其软件栈基于 TensorFlow Lite，支持 Edge TPU Compiler 将量化模型高效部署到端侧。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| Dev Board / SoM | 集成 SoM 的开发板 | Coral Dev Board | AIoT 原型、机器人感知、边缘 AI 开发 |
| USB / PCIe / M.2 加速器 | 外接式 Edge TPU 加速器 | Coral USB Accelerator | 现有嵌入式平台 AI 升级、工业视觉、智能相机 |

## 代表产品

### Coral Dev Board

> Coral Dev Board：请访问 [官方资料](https://coral.ai) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| SoC | NXP i.MX 8M（四核 Cortex-A53 + Cortex-M4F） | Coral 公开资料 |
| AI 加速器 | Google Edge TPU | Coral 公开资料 |
| AI 算力 | 最高 4 TOPS INT8 | Coral 公开资料 |
| 能效 | 约 2 TOPS/W | Coral 公开资料 |
| 内存 | 1 GB / 4 GB LPDDR4（依版本） | Coral 公开资料 |
| 存储 | 8 GB / 16 GB / 64 GB eMMC + MicroSD | Coral 公开资料 |
| 制程 | Edge TPU 未公开；i.MX 8M 14 nm | Coral 公开资料 |
| 接口 | USB 3.0、GbE、HDMI 2.0、MIPI CSI/DSI、40-pin GPIO、PCIe（SoM） | Coral 公开资料 |
| 功耗 | 约 5 W 典型（整板） | Coral 公开资料 |
| 尺寸 | 约 88 mm × 60 mm（含散热器） | Coral 公开资料 |
| 价格 | Dev Board 约 150 USD（参考价） | Coral 公开资料 |

**技术亮点**：可拆卸 Coral SoM、Edge TPU 与 i.MX 8M 异构集成、Mendel Linux、TensorFlow Lite 生态、可快速从原型迁移到定制载板。

**应用场景**：**机器人端侧感知**：实时目标检测、语义分割与导航辅助，降低云端依赖；**智能相机原型**：本地事件检测与人脸识别，提升隐私与响应速度；**工业视觉检测**：缺陷分类、条码/二维码识别与产线质检

### Coral USB Accelerator

> Coral USB Accelerator：请访问 [官方资料](https://coral.ai) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| AI 加速器 | Google Edge TPU | Coral 公开资料 |
| AI 算力 | 最高 4 TOPS INT8 | Coral 公开资料 |
| 接口 | USB 3.0 Type-C | Coral 公开资料 |
| 功耗 | 约 2 W | Coral 公开资料 |
| 尺寸 | 约 65 mm × 30 mm | Coral 公开资料 |
| 价格 | 约 75 USD（参考价） | Coral 公开资料 |

**技术亮点**：即插即用、USB 供电、无需额外散热、快速为现有设备增加 AI 推理能力。

**应用场景**：PC/边缘盒子 AI 扩展、工业视觉、智能相机、开发验证。

## 供应链位置

- **上游关键零部件/材料**：台积电晶圆代工、NXP i.MX 8M SoC、LPDDR4/eMMC、封测、PCB/模组
- **下游客户/应用场景**：AIoT 设备商、机器人整机厂、智能相机厂商、工业视觉方案商、开发者
- **主要竞争对手/对标**：Intel Movidius、Hailo、NVIDIA Jetson Nano、Qualcomm QCS、地平线征程

## 知识图谱节点与关系

- 公司实体：`ent_company_google_coral`
- 产品实体：`ent_product_google_coral_dev_board`、`ent_product_google_coral_usb_accelerator`
- 零部件实体：`ent_component_google_coral_edge_tpu`、`ent_component_google_coral_edge_tpu_2`
- 关键关系：
  - `ent_company_google_coral` -- `manufactures` --> `ent_product_google_coral_dev_board`
  - `ent_company_google_coral` -- `manufactures` --> `ent_product_google_coral_usb_accelerator`
  - `ent_company_google_coral` -- `manufactures` --> `ent_component_google_coral_edge_tpu`
  - `ent_company_google_coral` -- `manufactures` --> `ent_component_google_coral_edge_tpu_2`
  - `ent_product_google_coral_dev_board` -- `uses` --> `ent_component_google_coral_edge_tpu`
  - `ent_product_google_coral_usb_accelerator` -- `uses` --> `ent_component_google_coral_edge_tpu_2`

## 参考资料

1. [Coral 官网](https://coral.ai)
2. [Coral Dev Board 产品页](https://coral.ai/products/dev-board/)
3. [Coral 官方文档](https://coral.ai/docs/)
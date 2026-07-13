---
id: ent_component_syntouch_biotac_transducer
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: component
names:
  zh: SynTouch BioTac 触觉换能器核心
  en: SynTouch BioTac Tactile Transducer Core
status: active
sources:
- id: src_syntouch_biotac
  type: website
  url: https://www.syntouchllc.com/Products/BioTac/
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# SynTouch BioTac 触觉换能器核心 / SynTouch BioTac Tactile Transducer Core

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [SynTouch](../../../appendices/appendix-d/companies/company_syntouch.md) |
| **产品类别** | 仿生多模态触觉传感器 |
| **发布时间** | 2008 年起持续迭代 |
| **状态** | 量产/商用 |
| **官网/来源** | [SynTouch 官网](https://www.syntouchllc.com) |

## 产品概述

SynTouch BioTac 是全球首款、也是学术界与工业界应用最广泛的仿生指尖触觉传感器之一。其设计模仿人类指尖的机械结构与感知能力：刚性骨状核心外覆可更换的弹性皮肤，皮肤与核心之间填充导电液体。当传感器接触物体时，皮肤与液体层的形变会改变核心表面电极阵列的阻抗，同时压力传感器检测液体振动，热敏元件感知温度与热流。

BioTac 可同步输出力、振动与温度三类触觉信息，支持滑移检测、接触位置定位、纹理识别、硬度估计、边缘/棱角识别等功能。其电子器件全部封装在刚性核心内部，柔性皮肤可更换，具有极高的鲁棒性与可维护性。

## 产品图片

![SynTouch BioTac](https://www.syntouchllc.com/Products/BioTac/_media/BioTac_485.jpg)


## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 传感原理 | 流体压力 + 电极阻抗 + 热传导 | 官网公开资料 |
| 感知维度 | 力、振动、温度、热流 | 官网公开资料 |
| 电极数量 | 19 个感应电极 + 4 个激励电极 | 学术论文 |
| 尺寸 | 类人指尖尺寸 | 官网公开资料 |
| 重量 | 未公开 | - |
| 力量程 | 0 – 50 N | BioTac 手册 |
| 力分辨率 | 10 mN | BioTac 手册 |
| 压力量程 | 0 – 100 kPa | BioTac 手册 |
| 压力分辨率 | 37 Pa | BioTac 手册 |
| 振动量程 | ±760 Pa | BioTac 手册 |
| 振动分辨率 | 0.4 Pa | BioTac 手册 |
| 温度量程 | 0 – 75 ℃ | BioTac 手册 |
| 温度分辨率 | 0.1 ℃ | BioTac 手册 |
| 热流量程 | ±1 ℃/s | BioTac 手册 |
| 热流分辨率 | 0.001 ℃/s | BioTac 手册 |
| 电极阻抗采样率 | 100 Hz | 学术论文 |
| 振动采样率 | 2200 Hz | 学术论文 |
| 通信接口 | 集成电子模块 + 主机通信 | 官网公开资料 |
| 集成方案 | Shadow Hand / Allegro Hand / PR2 等 | 官网公开资料 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[SynTouch](../../../appendices/appendix-d/companies/company_syntouch.md)
- **核心零部件/技术来源**：自研柔性皮肤、导电液体、电极阵列、压力传感器、热敏元件；信号处理电路集成于核心内部。
- **下游应用/客户**：机器人灵巧手、假肢、科研院校、材料表征、医疗康复。

## 知识图谱节点与关系

- 产品实体：`ent_product_syntouch_biotac`
- 制造商实体：`ent_company_syntouch`
- 零部件实体：`ent_component_syntouch_biotac_transducer`
- 关键关系：
  - `rel_ent_company_syntouch_manufactures_ent_product_syntouch_biotac`（`ent_company_syntouch` → `manufactures` --> `ent_product_syntouch_biotac`）
  - `rel_ent_company_syntouch_manufactures_ent_component_syntouch_biotac_transducer`（`ent_company_syntouch` → `manufactures` --> `ent_component_syntouch_biotac_transducer`）
  - `rel_ent_product_syntouch_biotac_uses_ent_component_syntouch_biotac_transducer`（`ent_product_syntouch_biotac` → `uses` --> `ent_component_syntouch_biotac_transducer`）

## 应用场景

- **机器人灵巧操作**：抓取、拧转、按压、滑移检测与材质识别。
- **假肢触觉反馈**：为上肢假肢提供接近人类皮肤的力/温度感知。
- **材料触觉表征**：量化材料粗糙度、摩擦、柔顺性、热属性等触觉维度。
- **科研与教学**：触觉感知算法、仿生机器人、人机交互研究的标准传感器。

## 竞争对比

| 对比项 | SynTouch BioTac | 帕西尼 PX-6AX | XELA uSkin |
|--------|-----------------|---------------|------------|
| 传感原理 | 流体/电极/热传导 | 6D 霍尔阵列 | 磁阻式 3 轴 |
| 感知模态 | 力 + 振动 + 温度 | 15 种触觉信息 | 3 轴力 |
| 形态 | 仿生指尖 | 传感单元/灵巧手 | 柔性皮肤贴片 |
| 核心优势 | 仿生、鲁棒、可换皮肤 | 高密度、国产化 | 柔软、易集成 |

## 选购与部署建议

- 需根据目标灵巧手选择对应的集成套件（Shadow、Allegro、PR2 等）。
- 柔性皮肤为耗材，建议根据使用频率备件更换。
- 振动与温度数据对表面处理算法要求较高，建议配套 SynTouch 软件或自研标定流程。

## 参考资料

1. [SynTouch 官网](https://www.syntouchllc.com)
2. [SynTouch BioTac 产品页](https://www.syntouchllc.com/Products/BioTac/)
3. [BioTac Brochure](https://www.syntouchllc.com/Products/BioTac/_media/BioTac_Brochure.pdf)
4. [Interpreting and Predicting Tactile Signals for the SynTouch BioTac（arXiv）](https://arxiv.org/pdf/2101.05452.pdf)
5. [附录 D 企业目录](../../../appendices/appendix-d/index-companies.md)
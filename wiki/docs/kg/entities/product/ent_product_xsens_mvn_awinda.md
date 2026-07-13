---
id: ent_product_xsens_mvn_awinda
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Xsens MVN Awinda 无线惯性动作捕捉系统
  en: Xsens MVN Awinda Wireless Motion Capture System
status: active
sources:
- id: src_ent_product_xsens_mvn_awinda_website
  type: website
  url: https://xsens.com
- id: src_ent_product_xsens_mvn_awinda_shop
  type: website
  url: https://shop.movella.com/us/product-lines/motion-capture/products/xsens-mvn-awinda-starter
- id: src_ent_product_xsens_mvn_awinda_manual
  type: document
  url: https://www.xsens.com/hubfs/Downloads/Manuals/MTw_Awinda_User_Manual.pdf
- id: src_ent_product_xsens_mvn_awinda_wiki
  type: website
  url: docs/appendices/appendix-d/companies/company_xsens.md
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# Xsens MVN Awinda 无线惯性动作捕捉系统 / Xsens MVN Awinda Wireless Motion Capture System

## 概述

Xsens MVN Awinda 是荷兰 Xsens Technologies（现为 Movella Holdings 旗下品牌）推出的无线全身惯性动作捕捉系统。该系统通过 17 颗无线惯性测量单元（IMU）与可调节绑带固定于人体，配合 Awinda 无线接收站及 MVN Analyze/Animate 软件，实现无需动捕棚、可穿于衣物外的实时动作捕捉。其磁干扰免疫、快速穿戴和低延迟特性，使其在影视动画、体育科学、康复医学及机器人运动参考采集等场景得到广泛应用。

## 工作原理与技术架构

每颗 MTw Awinda 无线传感器集成三轴陀螺仪、三轴加速度计和三轴磁力计，通过 sensor fusion 算法估计传感器相对于地理坐标系的姿态。17 颗 IMU 分布于全身主要肢体段，结合 23 段、22 关节的生物力学模型，解算全身关节角度、质心、节段速度与加速度。

姿态更新采用捷联惯性导航与磁力计辅助的航姿参考系统（AHRS）方法，更新率为 60 Hz。系统端到端延迟约为：

$$
\tau_{\text{latency}} \approx 30\ \text{ms}
$$

无线通信采用 Awinda 专有协议，工作于 2.4 GHz 频段。Starter 版本无线覆盖范围约为 25 m，完整版本可达 50 m；MTw 传感器尺寸为 47 mm × 30 mm × 13 mm，重量约 16 g，续航约 6–12 小时。

静态姿态精度典型值为：

- Roll/Pitch：0.5° RMS
- Heading：1.0° RMS

动态姿态精度典型值为：

- Roll/Pitch：0.75° RMS
- Heading：1.5° RMS

## 关键参数表

| 参数项 | 数值/范围 | 备注 |
|--------|-----------|------|
| 传感器数量 | 17 颗无线 IMU + 1 道具传感器 | — |
| 无线通信 | Awinda 协议，2.4 GHz | — |
| 更新率 | 最高 60 Hz | — |
| 延迟 | 约 30 ms | 系统端到端 |
| 无线范围 | 25 m（Starter）/ 50 m（完整版） | 室外/室内有差异 |
| 续航 | 6–12 小时 | 依型号与使用模式 |
| 传感器尺寸 | 47 mm × 30 mm × 13 mm | MTw |
| 传感器重量 | 16 g | 单颗 |
| 穿戴方式 | 可调节绑带，可穿于衣物外 | — |
| 静态精度（Roll/Pitch） | 0.5° RMS | — |
| 静态精度（Heading） | 1.0° RMS | — |
| 动态精度（Roll/Pitch） | 0.75° RMS | — |
| 动态精度（Heading） | 1.5° RMS | — |
| 生物力学模型 | 23 段 / 22 关节 | — |
| 机身缓冲 | 30 s | 短时断链保护 |
| 手指追踪 | 兼容 Xsens Metagloves by Manus | — |
| 工作温度 | 0 ℃ ~ 50 ℃（指定性能） | MTw -10 ℃ ~ 60 ℃ |
| 价格 | 未公开 | 官方询价 |

## 应用场景

- **影视与游戏动画**：角色动作捕捉、虚拟制作、实时预演。
- **体育生物力学**：动作技术分析、伤病预防、康复评估。
- **医学与康复**：步态分析、神经康复、假肢/外骨骼评估。
- **机器人运动参考**：为人形机器人采集自然人体运动数据，验证控制算法与运动规划。

## 供应链关系

- **制造商**：Xsens Technologies B.V. / Movella Holdings Inc.。
- **上游关键物料**：MEMS IMU 芯片（陀螺仪/加速度计/磁力计）、无线射频模块、Lycra/弹性面料、电池、传感器融合算法 IP。
- **下游客户**：影视工作室、体育科研机构、医院/康复中心、机器人公司与高校实验室。
- **知识图谱关系**：
  - `ent_company_xsens_movella` — `manufactures` → `ent_product_xsens_mvn_awinda`
  - `ent_product_xsens_mvn_awinda` — `provides_data_to` → 人形机器人运动控制/数字人节点

## 来源与验证

- Xsens 官网与 Movella 在线商城给出 MVN Awinda Starter 的 17 颗无线传感器、60 Hz 更新率、30 ms 延迟、25 m 无线范围、6–12 小时续航、Metagloves 兼容等参数。
- MTw Awinda 用户手册披露了传感器尺寸 47×30×13 mm、重量 16 g、无线范围（室内/室外）、同步精度 <10 μs、静态/动态精度、工作温度等技术指标。
- 附录 D Wiki《Xsens / Movella Xsens》词条摘录了 MVN Awinda 的核心参数与应用场景。
---
id: ent_component_deep_robotics_j_series_joint
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 云深处 J 系列机器人关节
  en: DEEP Robotics J-Series Joint
status: active
sources:
- id: src_deep_robotics_j60
  type: website
  url: https://www.deeprobotics.cn/en/wap/j60.html
- id: src_deep_robotics_j80j100
  type: website
  url: https://www.deeprobotics.cn/en/wap/j80j100.html
- id: src_deep_robotics_x30
  type: website
  url: https://www.deeprobotics.cn/robot/index/x30.html
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 云深处 J 系列机器人关节 / DEEP Robotics J-Series Joint

## 概述

云深处科技（DEEP Robotics）J 系列机器人关节是面向足式与人形机器人开发的集成化旋转执行器，覆盖轻量化到中高扭矩的多场景需求。该系列主要包括 J60 轻量化关节，以及 J80/J100 大扭矩工业级关节。J60 主要面向教育科研、中小型四足机器人和人形机器人上肢；J80/J100 则已批量应用于云深处 X30 行业级四足机器人，并作为 DR01/DR02 等人形机器人的核心动力单元。

## 工作原理 / 技术架构

J 系列关节采用“无框力矩电机 + 精密减速器 + 伺服驱动器 + 绝对值编码器”的一体化设计，将机械传动、电机、电控与传感高度集成。

- **电机与传动**：采用无框永磁同步力矩电机，配合谐波或行星减速机构，将电机高速低扭矩输出转换为关节低速高扭矩输出。输出扭矩与电流的关系可表示为
  \[
  \tau = K_t \, I
  \]
  其中 \(\tau\) 为输出扭矩（N·m），\(K_t\) 为关节扭矩常数（N·m/A），\(I\) 为相电流有效值（A）。
- **扭矩密度**：关节的扭矩密度定义为
  \[
  \rho_\tau = \frac{\tau_{\text{peak}}}{m}
  \]
  其中 \(m\) 为关节质量（kg）。J80-27P 峰值扭矩密度达到 \(84\,\text{N·m} / 1.48\,\text{kg} \approx 56.8\,\text{N·m/kg}\)；J100-116P 峰值扭矩密度可达 \(107.5\,\text{N·m/kg}\)。
- **感知与控制**：J80/J100 配备无电池多圈绝对值编码器（单圈 17 bit、多圈 16 bit），J60 采用 14 bit 绝对值编码器；支持电流环、速度环与位置环闭环控制。J80/J100 采用 EtherCAT 总线，可同步多达 30 个关节；J60 采用 CAN 总线，通信波特率 1 Mbps，控制频率 1 kHz。
- **电气与防护**：J80/J100 额定电压 DC 72 V，工作电压范围 DC 28–95 V；整机达到 IP67 防护等级，可在 −20 °C 至 55 °C 环境下运行。

## 关键参数表

| 参数项 | J60（典型值） | J80-27P（典型值） | J100-116P（典型值） |
|---|---|---|---|
| 外形尺寸 | 76.5 mm × 63 mm | 105 mm × 85.5 mm | 未公开 |
| 质量 | 0.48 kg | 1.48 kg | 未公开 |
| 工作电压 | DC 18–36 V | DC 28–95 V | DC 28–95 V |
| 额定电压 | DC 24 V | DC 72 V | DC 72 V |
| 峰值扭矩 | 19.94 N·m | 84 N·m | 315 N·m |
| 额定扭矩 | 未公开 | 28 N·m | 未公开 |
| 峰值转速 | 24.18 rad/s | 17 rad/s | 未公开 |
| 扭矩常数 | 0.898 N·m/A | 2 N·m/Arms | 未公开 |
| 峰值扭矩密度 | 41.54 N·m/kg | 56.8 N·m/kg | 107.5 N·m/kg |
| 编码器分辨率 | 14 bit 绝对值 | 单圈 17 bit / 多圈 16 bit | 单圈 17 bit / 多圈 16 bit |
| 通信接口 | CAN（1 Mbps） | EtherCAT | EtherCAT |
| 防护等级 | 未公开 | IP67 | IP67 |

## 应用场景

- **人形机器人**：DR01 采用 J60 轻量关节与 J100 高扭矩关节组合，实现行走、越障与复杂全身运动。
- **四足机器人**：J80/J100 为 X30 四足机器人提供腿部高动态驱动，支撑 IP67 级户外巡检、应急救援。
- **科研教育**：J60 体积小巧、接口开放，适用于 SLAM、强化学习与运动控制算法验证。

## 供应链关系

- **上游**：稀土永磁体、无氧铜绕组、精密轴承、谐波/行星减速器齿坯、编码器芯片、功率半导体、接插件与外壳铝材。
- **制造商**：云深处科技（DEEP Robotics）自主设计并量产 J 系列关节。
- **下游整机**：用于云深处自研的 X30、DR01、DR02、Lynx M20 等机器人；亦可外供给人形机器人、协作机械臂与特种移动平台厂商。
- **图谱位置**：在公司–产品–零部件网络中，`ent_company_deep_robotics` → `manufactures` → `ent_component_deep_robotics_j_series_joint`，并通过 `uses` 关系嵌入 `ent_product_deep_robotics_x30` 等产品实体。

## 来源与验证

- 参数来源于云深处科技官网 J60、J80/J100 产品页（2026-07 可访问）。
- J100-116P 峰值扭矩与扭矩密度引自 J80/J100 官方介绍页。
- X30 应用关系来自云深处 X30 产品页及附录 D 企业 Wiki。
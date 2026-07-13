---
id: ent_component_wolong_drive
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 卧龙电驱变频器/伺服驱动器
  en: Wolong Variable Frequency Drive / Servo Drive
status: active
sources:
- id: src_wolong_vfd_high_voltage
  type: website
- title: Wolong 5000 Series Integrated High Voltage VFD
  url: https://www.wolong-electric.com/products-solutions/motors-drives/drive-control/high-voltage-drives/462.html
- id: src_wolong_vfd_america
  type: website
- title: Wolong Medium Voltage Variable Frequency Drives
  url: https://www.wolongamerica.com/drives
- id: src_wolong_integrated_motor
  type: website
- title: Wolong Low Speed Permanent Magnet Synchronous VFD Integrated Motor
  url: https://www.wolong-electric.com/products-solutions/motors-drives/high-voltage-motors/integrated-motor-products/306.html
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Wolong offers a broad drive portfolio; this entity aggregates publicly
    available VFD/servo drive specifications from official sources. Exact robot-specific
    servo drive model parameters are not fully public.
---


# 卧龙电驱变频器/伺服驱动器 / Wolong Variable Frequency Drive / Servo Drive

## 概述

卧龙电驱变频器/伺服驱动器是卧龙电气驱动集团股份有限公司面向工业自动化、新能源装备与机器人领域开发的电机控制产品族。产品线覆盖低压通用变频器、高压变频器、伺服驱动器及专用一体化驱动系统，功率范围从数百瓦延伸至数百千瓦，支持 V/F 控制、矢量控制、伺服控制与多种工业现场总线，适用于风机水泵、工业产线、数控机床以及人形机器人大功率关节驱动。

## 工作原理 / 技术架构

变频器/伺服驱动器的核心为 AC-DC-AC 变换拓扑：

1. **整流环节**：将三相交流电经整流桥转换为直流母线电压。
2. **直流母线**：由电容滤波稳定电压，支撑能量回馈与制动。
3. **逆变环节**：采用 IGBT/SiC MOSFET 等功率器件，通过 PWM 调制输出频率与电压可控的三相交流电，驱动电机。

对于异步电机，输出电压与频率的比值通常保持恒定以维持气隙磁通：

\[
\frac{U}{f} = \text{const}
\]

对于伺服驱动器，采用磁场定向控制（FOC）或直接转矩控制（DTC），将三相电流解耦为励磁分量 \(i_d\) 与转矩分量 \(i_q\)，实现高精度转矩、速度与位置控制：

\[
T_e = \frac{3}{2} p \left( \psi_d i_q - \psi_q i_d \right)
\]

其中 \(p\) 为极对数，\(\psi_d\)、\(\psi_q\) 为定子磁链分量，\(i_d\)、\(i_q\) 为同步旋转坐标系下的电流分量。

## 关键参数

| 参数项 | 数值/范围 | 备注/来源 |
|--------|-----------|-----------|
| 产品类型 | 变频器 / 伺服驱动器 | 产品手册 |
| 功率范围 | 0.4 kW – 630 kW（覆盖低压与高压系列） | 产品手册 |
| 控制方式 | V/F、矢量控制、伺服控制 | 产品手册 |
| 供电电压 | 单相/三相 220 V / 380 V / 690 V / 6 kV / 10 kV | 产品手册 |
| 输出频率 | 0 – 600 Hz | 公开资料 |
| 通信协议 | Modbus、CANopen、EtherCAT、PROFINET（部分型号） | 产品手册 |
| 安全功能 | STO/SS1/SLS 等（伺服系列），过压/过流/过热/短路保护 | 产品手册 |
| 效率 | 约 96%（高压变频系列） | 公开资料 |
| 防护等级 | IP20（柜机）/ IP55–IP66（部分集成电机） | 产品手册 |
| 认证 | CE、CCC、UL（部分型号） | 产品手册 |
| 速度环带宽 | 未公开（伺服系列具体值未公开） | — |
| 具体型号尺寸 | 未公开 | — |
| 价格 | 未公开 | — |

## 应用场景

- **工业产线与风机水泵**：通用变频器用于节能调速、软启动与过程控制。
- **数控机床与工业机器人**：伺服驱动器为电机提供高精度转矩与位置控制。
- **人形机器人大功率关节**：卧龙布局具身智能领域，为腰、髋等大扭矩关节提供高功率密度伺服驱动方案。
- **新能源车辆与储能**：高压变频器与一体化驱动系统用于电驱与储能变流。

## 供应链关系

变频器/伺服驱动器由 **卧龙电气驱动集团股份有限公司（实体 `ent_company_wolong`）** 制造。上游依赖硅钢片、铜线、磁材、轴承、IGBT/SiC 功率器件与控制器芯片；下游客户包括工业企业、新能源车企、机器人整机厂与能源装备厂商。在知识图谱中，该实体通过 `manufactures` 关系与公司节点 `ent_company_wolong` 相连，可与卧龙伺服电机或第三方电机组成完整伺服系统。

## 来源与验证

- 卧龙 5000 系列高压变频器产品页（https://www.wolong-electric.com/products-solutions/motors-drives/drive-control/high-voltage-drives/462.html）
- Wolong Electric America 中压变频器页（https://www.wolongamerica.com/drives）
- 卧龙低速永磁同步变频一体机产品页（https://www.wolong-electric.com/products-solutions/motors-drives/high-voltage-motors/integrated-motor-products/306.html）

机器人专用伺服驱动器的具体速度环带宽、尺寸与价格等参数在公开渠道未完整披露，已标注为“未公开”。
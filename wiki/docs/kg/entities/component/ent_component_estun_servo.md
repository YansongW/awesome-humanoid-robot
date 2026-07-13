---
id: ent_component_estun_servo
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 埃斯顿伺服系统
  en: Estun Servo System
status: active
sources:
- id: src_ent_component_estun_servo_official
  type: website
  url: https://www.estun.com
- id: src_ent_component_estun_servo_gongkong
  type: website
  url: http://www.gongkong.com/product/201412/77788.html
- id: src_ent_component_estun_servo_wiki
  type: website
  url: docs/appendices/appendix-d/companies/company_estun.md
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 埃斯顿伺服系统 / Estun Servo System

## 概述

埃斯顿伺服系统（Estun Servo System）是南京埃斯顿自动化股份有限公司（Estun Automation，SZ: 002747）自主研发的交流伺服驱动与电机成套产品，涵盖 PRONET、ED3L、EM3A 等多个系列。该系统以永磁同步伺服电机（PMSM）为核心执行元件，配套自研伺服驱动器，面向工业机器人、数控机床、电子制造、锂电设备及人形机器人关节等场景，提供位置、速度、转矩及总线控制功能，是国产高端伺服系统的代表性产品之一。

## 工作原理与技术架构

系统采用磁场定向矢量控制（FOC）架构，驱动器内部包含电流环、速度环和位置环三级闭环。控制器通过解析编码器反馈的转子位置，将三相电流解耦为励磁分量 $i_d$ 与转矩分量 $i_q$；对于表贴式永磁同步电机通常采用 $i_d=0$ 控制，此时电磁转矩近似为：

$$
T_e \approx \frac{3}{2} p \psi_f i_q
$$

其中 $p$ 为极对数，$\psi_f$ 为永磁体磁链，$i_q$ 为交轴电流。

机械功率与转矩、角速度的关系为：

$$
P = T \cdot \omega = \frac{T \cdot 2\pi n}{60}
$$

其中 $n$ 为转速（r/min）。驱动器支持在线惯量辨识、自动调谐、低频/中频振动抑制以及电子齿轮比动态切换，可通过 EtherCAT、CANopen、Modbus 等总线与上位控制器协同。

## 关键参数表

| 参数项 | 数值/范围 | 备注 |
|--------|-----------|------|
| 产品形态 | 伺服驱动器 + 伺服电机 | 成套系统 |
| 代表系列 | PRONET / ED3L / EM3A | — |
| 功率范围 | 0.05–75 kW | 系列覆盖 |
| 输入电压 | 单相/三相 100 VAC、200 VAC、400 VAC | 依型号 |
| 控制模式 | 位置 / 速度 / 转矩 / 总线 | CSP/CSV/CST 等 |
| 通信接口 | EtherCAT、Modbus、CANopen、POWERLINK、PROFIBUS | 视型号配置 |
| 编码器支持 | 17/23 位绝对值编码器、2500 P/R 增量编码器、旋转变压器 | — |
| 速度环带宽 | 1.6 kHz（PRONET 参考值） | 公开资料 |
| 电机防护等级 | IP65（部分电机） | — |
| 驱动器防护等级 | IP20（典型） | — |
| 控制精度 | ±1 脉冲（位置模式） | 公开规格 |
| 认证 | CE、UL（部分型号） | — |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **工业机器人**：六轴机器人、SCARA、Delta 机器人的关节伺服驱动。
- **人形机器人**：腿部、手臂关节的位置、速度与力矩控制，以及无框力矩电机配套。
- **数控机床**：进给轴、主轴的高精度定位与轮廓控制。
- **新能源与 3C**：锂电卷绕、光伏划片、3C 装配等高动态产线。

## 供应链关系

- **制造商**：`ent_company_estun`（南京埃斯顿自动化股份有限公司）自研并量产该伺服系统。
- **上游关键物料**：稀土永磁材料、IGBT/MOSFET 功率器件、DSP/ARM 控制芯片、编码器芯片、轴承、磁材、铸件。
- **下游集成**：埃斯顿自产工业机器人直接使用；同时外供机床、锂电、光伏、人形机器人整机厂。
- **知识图谱关系**：
  - `ent_company_estun` — `manufactures` → `ent_component_estun_servo`
  - `ent_product_estun_robot` — `uses` → `ent_component_estun_servo`

## 来源与验证

- 埃斯顿自动化官网对产品线的总体描述：埃斯顿自动化官网。
- 中国工控网 ProNet 系列页面列出功率范围、控制模式、通信接口、编码器类型及认证信息。
- 附录 D Wiki《埃斯顿自动化 / Estun Automation》词条摘录了 PRONET 系列功率 0.05–75 kW、编码器 17/23 位绝对值、通信接口 EtherCAT/Modbus/CANopen 等参数。
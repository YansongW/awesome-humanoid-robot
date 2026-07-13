---
id: ent_component_huazhong_hsj
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 华中数控 HSJ 系列伺服驱动器
  en: Huazhong HSJ Series Servo Drive
status: active
sources:
- id: src_ent_component_huazhong_hsj_official
  type: website
  url: https://www.huazhongcnc.com
- id: src_ent_component_huazhong_hsj_wiki
  type: website
  url: docs/appendices/appendix-d/companies/company_huazhong_cnc.md
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 华中数控 HSJ 系列伺服驱动器 / Huazhong HSJ Series Servo Drive

## 概述

华中数控 HSJ 系列伺服驱动器是武汉华中数控股份有限公司（Huazhong CNC，300161.SZ）推出的全数字交流伺服驱动单元，主要用于配套 HNC-818D/HNC-848D 等华中数控系统。该系列采用 DSP、FPGA 与智能功率模块（IPM）架构，支持永磁同步伺服电机的高速高精控制，广泛应用于数控机床、工业机器人及人形机器人关节驱动领域。

## 工作原理与技术架构

HSJ 系列伺服驱动器采用磁场定向矢量控制（FOC）与三环闭环结构：

- **电流环**：基于电流传感器与 PWM 调制，实现 $i_d/i_q$ 解耦控制。
- **速度环**：通过编码器速度反馈抑制负载扰动。
- **位置环**：接收上位机脉冲指令或总线指令，实现高精度定位。

对于表贴式永磁同步电机，在 $i_d=0$ 控制策略下，电磁转矩为：

$$
T_e = \frac{3}{2} p \psi_f i_q
$$

其中 $p$ 为极对数，$\psi_f$ 为永磁磁链，$i_q$ 为交轴电流。输出功率与转矩、转速关系为：

$$
P = \frac{2\pi n T}{60}
$$

驱动器支持 Modbus、CANopen 等通信协议，可适配 17/23 位绝对值编码器，实现全闭环位置控制。

## 关键参数表

| 参数项 | 数值/范围 | 备注 |
|--------|-----------|------|
| 产品形态 | 全数字交流伺服驱动器 | 单轴/多轴模块 |
| 功率范围 | 100 W – 7.5 kW | 系列范围 |
| 输入电压 | 单相/三相 220 VAC / 380 VAC | 依型号 |
| 控制模式 | 位置 / 速度 / 转矩 | — |
| 通信协议 | Modbus、CANopen | 公开规格 |
| 编码器支持 | 17/23 位绝对值编码器 | — |
| 速度环带宽 | 未公开 | 产品手册 |
| 电流环采样 | 未公开 | 典型数字伺服水平 |
| 防护等级 | IP20（典型） | — |
| 工作温度 | 0 ℃ ~ 45 ℃（典型） | — |
| 安全功能 | 未公开 | 部分型号支持 STO |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **数控机床**：高速高精进给轴、主轴驱动，配套 HNC 数控系统。
- **工业机器人**：六轴机器人、SCARA 机器人关节伺服。
- **人形机器人**：下肢、上肢关节的力矩/位置控制。
- **专用设备**：包装机械、纺织机械、印刷机械的伺服定位系统。

## 供应链关系

- **制造商**：`ent_company_huazhong_cnc`（武汉华中数控股份有限公司）。
- **上游关键物料**：DSP/FPGA 控制芯片、IGBT/IPM 功率模块、电流传感器、编码器、磁材、散热器。
- **下游集成**：机床厂、工业机器人厂商、人形机器人整机厂，以及航空航天/汽车零部件加工用户。
- **知识图谱关系**：
  - `ent_company_huazhong_cnc` — `manufactures` → `ent_component_huazhong_hsj`
  - `ent_component_huazhong_hnc_818d` — `controls` → `ent_component_huazhong_hsj`

## 来源与验证

- 华中数控官网提供伺服驱动产品手册下载入口。
- 附录 D Wiki《华中数控 / Huazhong CNC》词条明确列出 HSJ 系列功率范围 100 W–7.5 kW、控制模式位置/速度/转矩、通信协议 Modbus/CANopen、编码器 17/23 位绝对值等参数。
- 速度环带宽、电流环采样频率、部分安全功能等细节未在公开资料披露，表中标注为“未公开”。
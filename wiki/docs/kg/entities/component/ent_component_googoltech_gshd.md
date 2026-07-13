---
id: ent_component_googoltech_gshd
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 固高科技 GSHD 系列高性能伺服驱动器
  en: Googol Technology GSHD Series High-Performance Servo Drive
status: active
sources:
- id: src_ent_component_googoltech_gshd_1
  type: website
  url: https://www.googoltech.com.hk/Uploads/202411/67484b7c26c04.pdf
- id: src_ent_component_googoltech_gshd_2
  type: website
  url: https://www.googoltech.com.hk/Servo_drive/show/6.html
- id: src_ent_component_googoltech_gshd_3
  type: website
  url: http://www.googoltech.com/show-539.html
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 固高科技 GSHD 系列高性能伺服驱动器 / Googol Technology GSHD Series High-Performance Servo Drive

## 概述

固高科技 GSHD 系列是一款面向工业机器人、协作机器人与人形机器人关节的高性能交流伺服驱动器，功率覆盖 100 W 至 7.5 kW。该系列采用创新的硬件与软件设计，支持位置、速度、转矩三种控制模式，可驱动交流旋转伺服电机、直线电机、直流无刷电机及直驱（DD）电机。GSHD 支持 EtherCAT、gLink-II（固高千兆工业以太网）、RS485、模拟量及脉冲指令等多种接口，并配备 DriverStudio 调试软件，广泛应用于激光加工、半导体、数控机床、工业机器人与人形机器人领域。

## 工作原理 / 技术架构

GSHD 采用三相全桥逆变器与磁场定向矢量控制（FOC）。在 DQ 旋转坐标系下，电机定子电流被分解为励磁分量 $I_d$ 与转矩分量 $I_q$，输出电磁转矩近似为

$$
T_e = \frac{3}{2} p \psi_f I_q
$$

其中 $p$ 为极对数，$\psi_f$ 为永磁体磁链。驱动器电流环刷新周期为 31.25 μs（32 kHz），速度环与位置环刷新周期为 125 μs（8 kHz），电流环带宽可达 5 kHz。GSHD 支持增量式/绝对式编码器、霍尔、旋转变压器、正余弦编码器，并可通过第二编码器实现全闭环控制，位置精度可达 ±1 脉冲。

## 关键参数表

| 参数项 | 典型值/范围 | 备注/来源 |
|--------|-------------|-----------|
| 产品形态 | 单轴交流伺服驱动器 | 固高科技 |
| 适配电机 | 交流旋转伺服电机、直线电机、DC 电机、DD 电机 | 产品手册 |
| 功率范围 | 100 W – 7.5 kW（中压型 200 W–7.3 kW；高压型至 7.5 kW） | 产品手册 |
| 输入电压 | 单相/三相 220 VAC；三相 380 VAC（视型号） | 产品手册 / 附录 D |
| 额定输出电流 | 1.5 A – 24 A（视具体型号） | 产品手册 |
| 控制模式 | 位置 / 速度 / 转矩（可切换） | 产品手册 |
| 电流环刷新周期 | 31.25 μs（32 kHz） | 产品手册 |
| 速度/位置环刷新周期 | 125 μs（8 kHz） | 产品手册 |
| 电流环带宽 | ≤ 5 kHz | 产品手册 |
| 编码器支持 | 增量式、绝对式、霍尔、旋转变压器、正余弦 | 产品手册 |
| 正余弦细分 | 4096 倍，分辨率可达 32 bit | 产品手册 |
| 通信协议 | EtherCAT、gLink-II、RS485、模拟量±10 V、脉冲 | 产品手册 |
| 安全功能 | STO / 动态制动 / 全时动态刹车 | 产品手册 |
| 位置精度 | ±1 脉冲 | 应用案例 |
| 尺寸/重量 | 未公开（视型号） | 官方未披露 |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **工业机器人**：六轴、SCARA、协作机器人关节驱动，支持高动态力控与复杂轨迹规划。
- **人形机器人**：全身关节高动态响应、力控驱动与多轴同步。
- **半导体设备**：精密运动平台、晶圆传输设备的高速定位。
- **激光加工与数控机床**：高动态跟随、轨迹控制与振动抑制。

## 供应链关系

- **制造商**：固高科技 / Googol Technology（`ent_company_googoltech`）。
- **上游关键零部件/材料**：DSP/ARM 控制芯片、FPGA、IGBT/MOSFET、PCB、电容、电流传感器、编码器接口芯片、散热器件。
- **下游客户/应用场景**：工业机器人厂商、人形机器人整机厂、半导体设备商、激光设备商、数控机床制造商。
- **竞争/对标**：汇川 SV680、雷赛 L8、安川 Σ-7、松下 MINAS A6、三菱 MR-J5。
- **知识图谱关系**：`ent_company_googoltech` — `manufactures` → `ent_component_googoltech_gshd`；GSHD 伺服驱动器与 `ent_component_googoltech_gt400` 运动控制卡可形成控制器-驱动器-电机闭环。

## 来源与验证

1. [GSHD 系列高性能伺服驱动器 Datasheet（PDF）](https://www.googoltech.com.hk/Uploads/202411/67484b7c26c04.pdf)
2. [固高科技 GSHD 伺服驱动器产品页](https://www.googoltech.com.hk/Servo_drive/show/6.html)
3. [固高科技 GSHD 应用案例](http://www.googoltech.com/show-539.html)
4. [附录 D 重点产品 Wiki：固高科技 GSHD](../../../appendices/appendix-d/products/product_googol_gshd.md)
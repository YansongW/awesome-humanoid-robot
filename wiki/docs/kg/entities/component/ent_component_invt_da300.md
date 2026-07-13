---
id: ent_component_invt_da300
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 英威腾 DA300 系列伺服驱动器
  en: INVT DA300 Series Servo Drive
status: active
sources:
- id: src_ent_component_invt_da300_official
  type: website
  url: https://www.invt.com.cn
- id: src_ent_component_invt_da300_gkzhan
  type: website
  url: https://www.gkzhan.com/chanpin/13470457.html
- id: src_ent_component_invt_da300_kerntech
  type: website
  url: http://kerntech.com.cn/index.php?c=product&id=6693
- id: src_ent_component_invt_da300_wiki
  type: website
  url: docs/appendices/appendix-d/companies/company_invt.md
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 英威腾 DA300 系列伺服驱动器 / INVT DA300 Series Servo Drive

## 概述

英威腾 DA300 系列伺服驱动器是深圳市英威腾电气股份有限公司（INVT Electric，002334.SZ）推出的高性能交流伺服驱动产品，覆盖 100 W 至 2 kW 功率段（更高功率版本按型号扩展）。该系列采用一体化结构设计，体积相比 DA200 可缩小约 45%，支持脉冲、RS485、CANopen、EtherCAT 等多种控制方式，具备电子凸轮、龙门同步、振动抑制、惯量辨识等功能，适用于工业机器人、数控机床、包装机械及人形机器人关节等高动态应用场景。

## 工作原理与技术架构

DA300 采用全数字矢量控制架构，内部实现电流环、速度环、位置环三环闭环。驱动器通过 SVPWM 调制输出三相电压，控制永磁同步电机转子磁场与定子电流矢量的夹角，实现高效转矩输出。

在 $i_d=0$ 控制下，电磁转矩为：

$$
T_e = \frac{3}{2} p \psi_f i_q
$$

其中 $p$ 为极对数，$\psi_f$ 为永磁磁链，$i_q$ 为交轴电流。转速与角速度关系为：

$$
\omega = \frac{2\pi n}{60}
$$

机械输出功率为：

$$
P = T_e \cdot \omega
$$

DA300 支持在线惯量辨识、自动/手动陷波滤波器、速度观测器、扰动抑制及摩擦转矩补偿，可有效抑制 5–200 Hz 频段的前端振动与整机振动。EtherCAT 总线型支持 CSP/CSV/CST 等 CiA402 模式，并可选配 STO（Safe Torque Off）安全端子。

## 关键参数表

| 参数项 | 数值/范围 | 备注 |
|--------|-----------|------|
| 产品形态 | 单轴交流伺服驱动器 | 一体化结构 |
| 功率范围 | 100 W – 2 kW（公开列表） | 更高功率按型号扩展 |
| 输入电压 | 单相/三相 AC 220 V ±15% | 47–63 Hz |
| 控制模式 | 位置 / 速度 / 转矩 / 全闭环 / CANopen / EtherCAT | — |
| 脉冲输入 | 差分 4 Mpps，集电极开路 200 kpps | 脉冲+方向/CW+CCW/正交 |
| 模拟量输入 | 2 路（1 路 12 bit + 1 路 16 bit，标准型） | — |
| 模拟量输出 | 2 路监视输出 | — |
| 通信接口 | USB、RS485、CANopen、EtherCAT | 后两者选配 |
| 编码器支持 | 23 位绝对值（典型），亦支持增量/光栅尺 | — |
| 电子齿轮比 | 1/10000 – 1000 | — |
| 振动抑制 | 5–200 Hz | 前端/整机振动 |
| 安全端子 | STO（选配） | 符合欧洲安全标准 |
| 内部位置规划 | 128 点 | — |
| 防护等级 | IP20 | — |
| 工作温度 | 0 ℃ ~ 45 ℃ | — |
| 储存温度 | -20 ℃ ~ 80 ℃ | 不冻结 |
| 湿度 | ≤90% RH（无凝露） | — |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **工业机器人**：六轴机器人、SCARA、Delta 机器人的关节驱动。
- **人形机器人**：四肢关节的位置、速度与力矩控制。
- **数控机床**：进给轴、主轴高精度定位与轮廓控制。
- **包装与印刷**：飞剪、追剪、定长切割、套色控制。

## 供应链关系

- **制造商**：`ent_company_invt`（深圳市英威腾电气股份有限公司）。
- **上游关键物料**：IGBT/MOSFET 功率器件、DSP/ARM 控制芯片、电解电容、PCB、编码器芯片、磁材、散热器、风扇。
- **下游集成**：工业机器人厂商、机床厂、锂电/光伏设备商、人形机器人整机厂。
- **知识图谱关系**：
  - `ent_company_invt` — `manufactures` → `ent_component_invt_da300`
  - `ent_component_invt_da300` — `drives` → 伺服电机/关节模组节点

## 来源与验证

- 智能制造网 DA300 产品页公开了电源、控制模式、脉冲/模拟量接口、通信、编码器、电子齿轮、振动抑制、STO、环境条件等完整技术参数。
- KERNTECH 产品页补充了一体化结构、体积缩小 45%、电子凸轮/龙门同步/惯量辨识等性能特点。
- 英威腾官网作为品牌来源，附录 D Wiki 确认了 DA300 作为英威腾伺服产品线的定位。
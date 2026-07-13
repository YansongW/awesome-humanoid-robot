# 台达 ASDA-B3 系列伺服驱动器 / Delta ASDA-B3 Servo Drive

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [台达电子 / Delta Electronics](../companies/company_delta_electronics.md) |
| **产品类别** | 伺服驱动器 / 运动控制核心部件 |
| **发布时间** | 2020 年代持续迭代 |
| **状态** | 量产/商用 |
| **官网/来源** | [https://www.deltaww.com](https://www.deltaww.com) |

## 产品概述

台达 ASDA-B3 系列是面向工业自动化与机器人应用的高性能交流伺服驱动器，功率覆盖 100 W 至 15 kW。

产品支持脉冲、CANopen、EtherCAT 与台达 DMCNET 等多种控制接口，内置高级运动控制算法与抑振功能，搭配 ECMA 系列伺服电机，可满足工业机器人、协作机器人与人形机器人关节对高响应、高精度的需求。

## 产品图片

> Delta ASDA-B3：请访问 [官方资料](https://www.deltaww.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 单轴交流伺服驱动器 | 台达官网 |
| 功率范围 | 100 W – 15 kW | 产品手册 |
| 输入电压 | 单相/三相 220 VAC / 380 VAC | 产品手册 |
| 控制模式 | 位置 / 速度 / 转矩 | 产品手册 |
| 通信协议 | Pulse / CANopen / EtherCAT / DMCNET | 产品手册 |
| 速度环带宽 | 3.1 kHz（参考） | 产品手册 |
| 编码器支持 | 17/20/23 位绝对值 | 产品手册 |
| 安全功能 | STO（部分型号） | 产品手册 |
| 防护等级 | IP20（典型） | 产品手册 |
| 价格 | 未公开 | 需询价 |

## 供应链位置

- **制造商**：[台达电子 / Delta Electronics](../companies/company_delta_electronics.md)
- **核心零部件/技术来源**：自研功率模块、控制板与伺服算法；IGBT/SiC 功率器件、电容、编码器芯片外购。
- **下游应用/客户**：工业机器人、人形机器人关节、半导体设备、3C 电子、机床、物流自动化。

## 知识图谱节点与关系

- 零部件实体：`ent_component_delta_asda_b3`
- 制造商实体：`ent_company_delta_electronics`
- 关键关系：
  - `rel_ent_company_delta_electronics_manufactures_ent_component_delta_asda_b3`（`ent_company_delta_electronics` → `manufactures` → `ent_component_delta_asda_b3`）

## 应用场景

- **工业机器人**：六轴机器人、SCARA、Delta 机器人关节的伺服驱动。
- **人形机器人**：腿部、手臂关节电机的位置、速度与力矩控制。
- **半导体设备**：精密运动平台、贴片机、晶圆传输设备。
- **电子制造**：PCB 加工、搬运机械、3C 自动化产线。

## 竞争对比

| 对比项 | 台达 ASDA-B3 | 汇川 SV660 | Yaskawa Σ-7 |
|--------|--------------|------------|-------------|
| 功率范围 | 100 W – 15 kW | 50 W – 7.5 kW | 30 W – 55 kW |
| 通信接口 | EtherCAT / DMCNET / CANopen | EtherCAT / 脉冲 | EtherCAT / MECHATROLINK |
| 编码器 | 最高 23 位绝对值 | 23 位绝对值 | 24 位绝对值 |
| 核心优势 | 多总线、宽功率、节能设计 | 本土化服务、性价比 | 高端精度与可靠性 |

## 选购与部署建议

- 根据电机功率、电压等级与总线协议选择对应型号。
- 人形机器人应用需确认驱动器是否支持高动态力控与低温漂。
- 建议通过台达官方渠道获取最新固件与调试软件。

## 相关词条

- [制造商：台达电子 / Delta Electronics](../companies/company_delta_electronics.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考资料

1. [台达官网](https://www.deltaww.com)
2. 台达 ASDA-B3 系列产品手册
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
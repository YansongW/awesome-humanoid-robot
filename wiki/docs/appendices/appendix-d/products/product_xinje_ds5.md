# 信捷 DS5 系列伺服驱动器 / Xinje DS5 Servo Drive

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [信捷电气 / Xinje Electric](../companies/company_xinje.md) |
| **产品类别** | 伺服驱动器 / 运动控制核心部件 |
| **发布时间** | 2010 年代持续迭代 |
| **状态** | 量产/商用 |
| **官网/来源** | [https://www.xinje.com](https://www.xinje.com) |

## 产品概述

信捷 DS5 系列是面向中小型自动化设备与机器人应用的交流伺服驱动器，功率覆盖 100 W 至 7.5 kW。

产品支持脉冲、Modbus、CANopen 与 EtherCAT 等多种控制接口，具备自动调谐、惯量辨识与抑振功能，与信捷 XD/XL 系列 PLC、MS6 系列伺服电机形成完整自动化解决方案，广泛应用于 3C、包装、纺织、机床与人形机器人关节驱动。

## 产品图片

> Xinje DS5：请访问 [官方资料](https://www.xinje.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 单轴交流伺服驱动器 | 信捷官网 |
| 功率范围 | 100 W – 7.5 kW | 产品手册 |
| 输入电压 | 单相/三相 220 VAC / 380 VAC | 产品手册 |
| 控制模式 | 位置 / 速度 / 转矩 | 产品手册 |
| 通信协议 | Pulse / Modbus / CANopen / EtherCAT | 产品手册 |
| 速度环带宽 | 2.5 kHz（参考） | 产品手册 |
| 编码器支持 | 17/23 位绝对值 | 产品手册 |
| 安全功能 | STO（部分型号） | 产品手册 |
| 防护等级 | IP20（典型） | 产品手册 |
| 价格 | 未公开 | 需询价 |

## 供应链位置

- **制造商**：[信捷电气 / Xinje Electric](../companies/company_xinje.md)
- **核心零部件/技术来源**：自研功率模块、控制板与伺服算法；IGBT/MOS 功率器件、电容、编码器芯片外购。
- **下游应用/客户**：自动化设备厂商、工业机器人厂商、人形机器人整机厂、3C 电子、包装纺织。

## 知识图谱节点与关系

- 零部件实体：`ent_component_xinje_ds5`
- 制造商实体：`ent_company_xinje`
- 关键关系：
  - `rel_ent_company_xinje_manufactures_ent_component_xinje_ds5`（`ent_company_xinje` → `manufactures` → `ent_component_xinje_ds5`）
  - `ent_component_xinje_ds5` -- `uses` --> `ent_component_xinje_ms6`

## 应用场景

- **工业机器人**：六轴机器人、SCARA、Delta 机器人关节的伺服驱动。
- **人形机器人**：手臂、腿部关节的位置、速度与力矩控制。
- **包装机械**：飞剪、追剪、定长输送等运动控制。
- **纺织机械**：横机、圆机、梭织机的高精度传动。

## 竞争对比

| 对比项 | 信捷 DS5 | 汇川 SV660 | 英威腾 DA200 |
|--------|----------|------------|--------------|
| 功率范围 | 100 W – 7.5 kW | 50 W – 7.5 kW | 100 W – 7.5 kW |
| 通信接口 | EtherCAT / CANopen / 脉冲 | EtherCAT / 脉冲 | EtherCAT / CANopen / 脉冲 |
| 编码器 | 最高 23 位绝对值 | 23 位绝对值 | 最高 23 位绝对值 |
| 核心优势 | PLC 生态集成、性价比高 | 本土化服务、响应快 | 行业方案丰富 |

## 选购与部署建议

- 建议与信捷 PLC/HMI 配套使用以发挥生态集成优势。
- 根据负载惯量、刚性要求与总线协议选择对应子型号。
- 建议通过信捷官方渠道获取最新固件与调试软件。

## 相关词条

- [制造商：信捷电气 / Xinje Electric](../companies/company_xinje.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考资料

1. [信捷官网](https://www.xinje.com)
2. 信捷 DS5 系列产品手册
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
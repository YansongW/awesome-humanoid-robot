# 固高科技 GSHD 系列伺服驱动器 / Googol GSHD Servo Drive

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [固高科技 / Googol Technology](../companies/company_googoltech.md) |
| **产品类别** | 伺服驱动器 / 运动控制核心部件 |
| **发布时间** | 2020 年代持续迭代 |
| **状态** | 量产/商用 |
| **官网/来源** | [https://www.googoltech.com](https://www.googoltech.com) |

## 产品概述

固高科技 GSHD 系列是面向工业机器人、协作机器人与人形机器人关节的高性能伺服驱动器，功率覆盖 100 W 至 7.5 kW。

产品依托固高在运动控制算法与控制器平台方面的积累，支持 EtherCAT、CANopen 等工业总线，具备高响应带宽、多轴协同与功能安全设计，是国产高端伺服驱动与人形机器人核心零部件替代的重要方案。

## 产品图片

> Googol GSHD：请访问 [官方资料](https://www.googoltech.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 单轴/多轴交流伺服驱动器 | 固高科技官网 |
| 功率范围 | 100 W – 7.5 kW | 产品手册 |
| 输入电压 | 单相/三相 220 VAC / 380 VAC | 产品手册 |
| 控制模式 | 位置 / 速度 / 转矩 | 产品手册 |
| 通信协议 | EtherCAT / CANopen | 产品手册 |
| 速度环带宽 | 未公开 | - |
| 电流环频率 | 未公开 | - |
| 编码器支持 | 17/23 位绝对值、BiSS-C | 产品手册 |
| 安全功能 | STO / SS1 等（部分型号） | 产品手册 |
| 价格 | 未公开 | 需询价 |

## 供应链位置

- **制造商**：[固高科技 / Googol Technology](../companies/company_googoltech.md)
- **核心零部件/技术来源**：自研控制算法与功率板；IGBT/MOS 管、PCB、电容、电流传感器、编码器接口芯片、DSP/ARM 控制芯片外购。
- **下游应用/客户**：工业机器人厂商、人形机器人整机厂、半导体设备、激光设备、数控机床。

## 知识图谱节点与关系

- 零部件实体：`ent_component_googoltech_gshd`
- 制造商实体：`ent_company_googoltech`
- 关键关系：
  - `rel_ent_company_googoltech_manufactures_ent_component_googoltech_gshd`（`ent_company_googoltech` → `manufactures` → `ent_component_googoltech_gshd`）

## 应用场景

- **工业机器人**：六轴、SCARA、协作机器人关节驱动。
- **人形机器人**：全身关节高动态响应与力控驱动。
- **半导体设备**：精密运动平台、晶圆传输设备。
- **激光加工**：高动态跟随与轨迹控制。

## 竞争对比

| 对比项 | 固高 GSHD | 汇川 SV680 | 雷赛 L8 |
|--------|-----------|------------|---------|
| 定位 | 高端机器人伺服驱动 | 通用高性能伺服 | 国产高性价比伺服 |
| 通信接口 | EtherCAT / CANopen | EtherCAT / CANopen | EtherCAT / CANopen |
| 核心优势 | 运动控制算法、多轴协同 | 本土化服务、全功率段 | 性价比高、调试便捷 |
| 价格 | 未公开 | 未公开 | 未公开 |

## 选购与部署建议

- 根据功率、轴数、编码器类型与总线协议选择对应型号。
- 人形机器人应用建议评估多轴驱动的散热、同步性能与故障安全机制。
- 建议通过固高科技官方渠道获取最新固件、调试软件与认证信息。

## 相关词条

- [制造商：固高科技 / Googol Technology](../companies/company_googoltech.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考资料

1. [固高科技官网](https://www.googoltech.com)
2. 固高科技 GSHD 系列产品手册
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
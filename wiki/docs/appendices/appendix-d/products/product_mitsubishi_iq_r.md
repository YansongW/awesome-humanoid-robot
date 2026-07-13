# Mitsubishi Electric MELSEC iQ-R R04CPU / MELSEC iQ-R

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [三菱电机 / Mitsubishi Electric](../companies/company_mitsubishi_electric.md) |
| **产品类别** | 可编程逻辑控制器（PLC） |
| **发布时间** | 2014 年（现役系列持续更新） |
| **状态** | 量产/商用 |
| **官网/来源** | [三菱电机 官网](https://www.mitsubishielectric.com) |

## 产品概述

MELSEC iQ-R 系列是三菱电机推出的新一代模块化 PLC，以高速运算、大容量程序内存和内置高速网络为特点。

R04CPU 作为 iQ-R 系列的代表性 CPU 模块，支持纳秒级逻辑运算、CC-Link IE 现场网络及 GX Works3 统一编程环境，适用于大规模、高节拍的生产线控制。

## 产品图片

> Mitsubishi Electric MELSEC iQ-R R04CPU：请访问 [官方资料](https://www.mitsubishielectric.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品类型 | 模块化 PLC CPU | 官方资料 |
| 程序容量 | 40 k 步 | 官方资料（R04CPU） |
| 基本指令处理速度 | 0.98 ns | 官方资料 |
| 最大 I/O 点数 | 4,096 点 | 官方资料 |
| 通信接口 | CC-Link IE Field、Ethernet、RS-232 | 官方资料 |
| 编程软件 | GX Works3 | 官方资料 |
| 供电电压 | 100–240 VAC / 24 VDC | 官方资料 |
| 价格 | 未公开 | 未公开 |

## 供应链位置

- **制造商**：[三菱电机 / Mitsubishi Electric](../companies/company_mitsubishi_electric.md)
- **核心零部件/技术来源**：自研 CPU 与 FA 网络芯片；功率器件、存储、连接器及结构件外购。
- **下游应用/客户**：汽车、半导体设备、机床、机器人集成、人形机器人运动控制平台。

## 知识图谱节点与关系

- 产品实体：`ent_product_mitsubishi_iq_r`
- 制造商实体：`ent_company_mitsubishi_electric`
- 关键关系：
  - `ent_company_mitsubishi_electric` → `manufactures` → `ent_product_mitsubishi_iq_r`（关系文件：`rel_ent_company_mitsubishi_electric_manufactures_ent_product_mitsubishi_iq_r.md`）

## 应用场景

- **汽车产线**：车身、动力总成装配控制。
- **半导体设备**：晶圆搬运、曝光机控制。
- **数控机床**：高精度插补与轴控制。
- **机器人系统**：为人形机器人装配与测试提供高速控制。

## 竞争对比

| 对比项 | Mitsubishi Electric MELSEC iQ-R R04CPU | Siemens S7-1500 | OMRON NJ501 |
|--------|---------------|--------|--------|
| 程序容量 | 40 k 步（R04CPU） | 未公开 | 未公开 |
| 基本指令速度 | 0.98 ns | 未公开 | 未公开 |
| 主要现场网络 | CC-Link IE | PROFINET | EtherCAT |
| 价格 | 未公开 | 未公开 | 未公开 |

## 选购与部署建议

在日系设备生态或已使用 CC-Link IE 网络的产线中，iQ-R 系列可提供无缝升级；选型时需匹配 I/O 模块与网络拓扑。

## 参考资料

1. [三菱电机 官网](https://www.mitsubishielectric.com)
2. [Mitsubishi Electric MELSEC iQ-R R04CPU 产品页](https://www.mitsubishielectric.com/fa/products/cnt/plc/r/r04cpu.html)
3. Mitsubishi Electric FA Global Website / MELSEC iQ-R Catalog
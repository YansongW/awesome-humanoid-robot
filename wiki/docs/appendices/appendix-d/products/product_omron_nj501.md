# OMRON NJ501 Sysmac 控制器 / NJ501

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [欧姆龙 / OMRON](../companies/company_omron.md) |
| **产品类别** | 机器自动化控制器（MAC） |
| **发布时间** | 2011 年起（现役主力型号） |
| **状态** | 量产/商用 |
| **官网/来源** | [欧姆龙 官网](https://www.omron.com) |

## 产品概述

NJ501 系列是欧姆龙 Sysmac 平台的机器自动化控制器，将传统 PLC 的逻辑控制与多轴运动控制集成在同一硬件与软件环境中。

通过 EtherCAT 总线，NJ501 可同步控制伺服、变频器、I/O 及视觉设备，并支持 IEC 61131-3 编程与 PLCopen 运动控制功能块，适用于需要逻辑+运动一体化的高端设备。

## 产品图片

> OMRON NJ501 Sysmac 控制器：请访问 [官方资料](https://www.omron.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品类型 | 机器自动化控制器（MAC） | 官方资料 |
| 最大控制轴数 | 64 轴（EtherCAT） | 官方资料 |
| 最大 I/O 点数 | 2,560 点 | 官方资料（依型号） |
| 程序容量 | 未公开 | 未公开 |
| 通信接口 | EtherCAT、EtherNet/IP、USB、OPC UA | 官方资料 |
| 编程标准 | IEC 61131-3 / PLCopen 运动控制功能块 | 官方资料 |
| 供电电压 | 24 VDC | 官方资料 |
| 价格 | 未公开 | 未公开 |

## 供应链位置

- **制造商**：[欧姆龙 / OMRON](../companies/company_omron.md)
- **核心零部件/技术来源**：自研控制器硬件与 Sysmac Studio 软件；处理器、通信芯片、功率器件、存储外购。
- **下游应用/客户**：3C 制造、汽车部件、包装机械、机器人系统集成、人形机器人原型控制。

## 知识图谱节点与关系

- 产品实体：`ent_product_omron_nj501`
- 制造商实体：`ent_company_omron`
- 关键关系：
  - `ent_company_omron` → `manufactures` → `ent_product_omron_nj501`（关系文件：`rel_ent_company_omron_manufactures_ent_product_omron_nj501.md`）

## 应用场景

- **3C 电子**：贴片、组装、检测设备的运动控制。
- **包装机械**：多轴同步与飞剪、追剪控制。
- **机器人集成**：工业机器人与人形机器人关节控制。
- **汽车部件**：发动机、变速器装配线。

## 竞争对比

| 对比项 | OMRON NJ501 Sysmac 控制器 | Mitsubishi iQ-R | Schneider M580 |
|--------|---------------|--------|--------|
| 控制轴数 | 最多 64 轴 | 未公开 | 未公开 |
| 编程环境 | Sysmac Studio | GX Works3 | EcoStruxure |
| 主要通信 | EtherCAT / EtherNet/IP | CC-Link IE / Ethernet | 以太网 / Modbus TCP |
| 价格 | 未公开 | 未公开 | 未公开 |

## 选购与部署建议

对于需要逻辑与运动深度融合、轴数在数十轴以内的设备，可优先考虑 NJ501；选型时确认 I/O 规模与 EtherCAT 从站兼容性。

## 参考资料

1. [欧姆龙 官网](https://www.omron.com)
2. [OMRON NJ501 Sysmac 控制器 产品页](https://www.omron.com.cn/products/family/3194/)
3. OMRON FA product catalog / Sysmac Studio documentation
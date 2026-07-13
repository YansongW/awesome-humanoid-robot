# 三菱电机 / Mitsubishi Electric Corporation

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 三菱电机 |
| **英文名** | Mitsubishi Electric Corporation |
| **总部** | 日本东京 |
| **成立时间** | 1921 年 |
| **官网** | [https://www.mitsubishielectric.com](https://www.mitsubishielectric.com) |
| **供应链环节** | 工厂自动化（FA）、PLC、伺服系统、CNC、工业机器人 |
| **企业属性** | 上市公司（TYO：6503） |
| **母公司/所属集团** | 三菱集团（无单一控股母公司，独立上市） |
| **数据来源** | 三菱电机官网、FA 产品样本、公开财报 |

## 公司简介

三菱电机是全球领先的工厂自动化（FA）与机电产品综合制造商。

三菱电机的 FA 业务涵盖 MELSEC 可编程控制器、MELSERVO 伺服、CNC 数控系统、工业机器人（MELFA）及可视化软件。其 iQ 平台以高速、高可靠性和网络一体化著称，在汽车、半导体、机床、电梯等领域拥有深厚基础。三菱电机的伺服与运动控制技术可为人形机器人关节驱动与精密定位提供核心零部件。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| PLC / 控制器 | 高速模块化控制器 | MELSEC iQ-R / iQ-F | 汽车、半导体、机床 |
| 伺服系统 | 高精度运动控制 | MELSERVO-J5 / J4 | 电子、机器人、包装 |
| 工业机器人 | 垂直多关节 / SCARA | MELFA RV / RH / F 系列 | 装配、搬运、焊接 |

## 代表产品

### Mitsubishi Electric MELSEC iQ-R R04CPU

> Mitsubishi Electric MELSEC iQ-R R04CPU：请访问 [官方资料](https://www.mitsubishielectric.com) 查看。

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

**技术亮点**：纳秒级指令处理、内置 CC-Link IE 现场网络、统一工程软件 GX Works3、模块化高扩展性。

**应用场景**：汽车产线控制、半导体设备、数控机床、电梯控制、人形机器人装配与测试设备。

## 与人形机器人的关联

人形机器人关节伺服对高速响应与定位精度要求严苛，三菱电机的 MELSERVO 与 iQ-R 控制器可为关节模组开发与整机运动控制提供高可靠性平台。

## 供应链位置

- **上游关键零部件/材料**：半导体、功率模块、编码器、磁性材料、结构件、PCB
- **下游客户/应用场景**：汽车制造、半导体设备、机床、电梯、能源基础设施
- **主要竞争对手/对标**：Siemens, OMRON, Schneider Electric, Fanuc

## 知识图谱节点与关系

- 公司实体：`ent_company_mitsubishi_electric`
- 产品实体：`ent_product_mitsubishi_iq_r`
- 关键关系：
  - `ent_company_mitsubishi_electric` -- `manufactures` --> `ent_product_mitsubishi_iq_r`

## 参考资料

1. [三菱电机 官网](https://www.mitsubishielectric.com)
2. [Mitsubishi Electric MELSEC iQ-R R04CPU 产品页](https://www.mitsubishielectric.com/fa/products/cnt/plc/r/r04cpu.html)
3. Mitsubishi Electric FA Global Website / MELSEC iQ-R Catalog
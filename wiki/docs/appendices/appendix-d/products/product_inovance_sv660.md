# 汇川 SV660 伺服驱动 / Inovance SV660 Servo Drive

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [汇川技术 / Inovance](../companies/company_inovance.md) |
| **产品类别** | 伺服驱动器 |
| **发布时间** | SV660 系列为现役主力型号 |
| **状态** | 量产/商用 |
| **官网/来源** | [汇川技术官网](https://www.inovance.com) |

## 产品概述

汇川 SV660 系列是汇川技术推出的一款高性能中小功率交流伺服驱动器，功率范围覆盖 0.05 kW 至 7.5 kW，支持脉冲、EtherCAT（SV660N）等多种控制接口，广泛应用于半导体设备、贴片机、印刷电路板加工、搬运机械、机床与传送机械等自动化设备。

SV660 系列内置刚性表设置、在线惯量辨识、自动调谐与振动抑制功能，配合 MS1 系列 23 位单圈/多圈绝对值编码器伺服电机，可实现快速精确的位置、速度与转矩控制。其紧凑的体积与分体式编码器设计有助于减少电机尺寸与重量，适配移动机构与紧凑安装空间。

## 产品图片

> Inovance SV660：请访问 [官方资料](https://www.inovance.com) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 功率范围 | 0.05 kW – 7.5 kW | 官方手册 |
| 控制接口 | 脉冲（SV660P）/ EtherCAT（SV660N） | 官方手册 |
| 编码器支持 | 23 位单圈/多圈绝对值编码器 | 官方手册 |
| 控制模式 | 位置 / 速度 / 转矩 / 混合模式 | 官方手册 |
| 通信协议 | EtherCAT / CANopen / Modbus | 官方手册 |
| 防护等级 | IP20（典型） | 官方手册 |
| 供电电压 | 单相/三相 220 VAC 或 380 VAC（依型号） | 官方手册 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[汇川技术 / Inovance](../companies/company_inovance.md)
- **核心零部件/技术来源**：自研功率模块、控制板与伺服算法；IGBT/SiC 功率器件、电容、编码器芯片外购。
- **下游应用/客户**：工业机器人、人形机器人关节、半导体设备、3C 电子、机床、物流自动化。

## 知识图谱节点与关系

- 零部件实体：`ent_component_inovance_sv660`
- 制造商实体：`ent_company_inovance`
- 关键关系：
  - `rel_ent_company_inovance_manufactures_ent_component_inovance_sv660`（`ent_company_inovance` → `manufactures` → `ent_component_inovance_sv660`）

## 应用场景

- **工业机器人**：六轴机器人、SCARA、Delta 机器人关节的伺服驱动。
- **人形机器人**：腿部、手臂关节电机的位置、速度与力矩控制。
- **数控机床**：进给轴、主轴的高精度定位与轮廓控制。
- **电子制造**：贴片机、PCB 钻孔机、搬运机械的精密运动控制。

## 竞争对比

| 对比项 | 汇川 SV660 | Yaskawa Σ-7 | Panasonic A6 |
|--------|------------|-------------|--------------|
| 功率范围 | 0.05–7.5 kW | 0.03–55 kW | 0.05–5 kW |
| 通信接口 | EtherCAT / 脉冲 | EtherCAT / MECHATROLINK | EtherCAT / Pulse |
| 编码器 | 23 位绝对值 | 24 位绝对值 | 23 位绝对值 |
| 核心优势 | 本土化服务、性价比、快速调试 | 高端精度与可靠性 | 高速响应 |

## 选购与部署建议

- 选型时应根据负载惯量、刚性要求与总线协议选择 SV660P（脉冲）或 SV660N（EtherCAT）。
- 调试建议先进行在线惯量辨识与振动抑制，再接入整机进行轨迹优化。

## 参考资料

1. [汇川技术官网](https://www.inovance.com)
2. [汇川 SV660N 系列伺服手册](https://idea-tech.in/wp-content/uploads/2020/04/INOVANCE-SV660-SERVO-ETHERCAT-MANUAL-CHINESE-20-4-20.pdf)
3. [CSDN – 汇川 SV660N 调试手册](https://blog.csdn.net/crown6465/article/details/145727125)
4. [原创力文档 – 汇川 SV660N 系列伺服调试手册](https://max.book118.com/html/2024/0807/8125023046006117.shtm)
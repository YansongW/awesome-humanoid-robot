# 飞腾腾云 S5000C / Phytium S5000C

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [飞腾 / Phytium](../companies/company_phytium.md) |
| **产品类别** | 国产高性能服务器/计算 CPU |
| **发布时间** | 2023 年发布腾云 S5000C |
| **状态** | 量产/商用 |
| **官网/来源** | 飞腾官网、产品手册 |

## 产品概述

飞腾腾云 S5000C 是飞腾面向服务器与高性能计算推出的新一代 ARM 架构 CPU，基于自研 FTC862 核心，具备高核心数、高内存带宽与多路互联能力。

S5000C 兼容 ARMv8 指令集，支持国产操作系统与中间件生态，适用于云计算、数据库、大数据分析、智算中心及机器人后台训练与仿真平台。其高可靠性与安全扩展特性，使其成为政企关键业务与国产化替代的重要选择。

## 产品图片

> 飞腾腾云 S5000C：请访问 [官方资料](https://www.phytium.com.cn) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| CPU | 飞腾腾云 S5000C | 飞腾官网 |
| 架构 | ARMv8，自研 FTC862 核心 | 飞腾公开资料 |
| 核心数 | 最高 64 核 | 飞腾公开资料 |
| 制程 | 7 nm | 公开报道 |
| 主频 | 最高 2.1 GHz | 飞腾公开资料 |
| 内存 | 支持 DDR4 / DDR5 | 飞腾公开资料 |
| 内存通道 | 8 通道（视型号） | 飞腾公开资料 |
| 互联 | 支持多路互连 | 飞腾公开资料 |
| 接口 | PCIe Gen4 / CXL（视型号） | 公开报道 |
| 功耗 | 约 150–250 W | 公开报道 |
| 价格 | 未公开 | - |

## 供应链位置

- **制造商**：[飞腾 / Phytium](../companies/company_phytium.md)
- **核心零部件/技术来源**：自研 FTC 核心、晶圆代工、DDR 内存、主板/PCB、BIOS/固件。
- **下游应用/客户**：政府、金融、电信、能源、轨交、工业自动化、智算中心、科研院所。

## 知识图谱节点与关系

- 产品实体：`ent_product_phytium_s5000c`
- 零部件实体：`ent_component_phytium_s5000c_cpu`
- 制造商实体：`ent_company_phytium`
- 关键关系：
  - `rel_ent_company_phytium_manufactures_ent_product_phytium_s5000c`（`ent_company_phytium` → `manufactures` → `ent_product_phytium_s5000c`）
  - `rel_ent_company_phytium_manufactures_ent_component_phytium_s5000c_cpu`（`ent_company_phytium` → `manufactures` → `ent_component_phytium_s5000c_cpu`）
  - `ent_product_phytium_s5000c` -- `uses` --> `ent_component_phytium_s5000c_cpu`

## 应用场景

- **国产服务器与云计算**：作为数据中心通用算力节点，替代 x86 平台。
- **智算中心训练/仿真平台**：支撑机器人模型训练、仿真调度与数据管理。
- **工业控制与边缘网关**：为智能制造、轨交、能源等场景提供高可靠主控。

## 竞争对比

| 对比项 | 飞腾 S5000C | 华为鲲鹏 920 | 海光 C86 |
|--------|------|------|------|
| 架构 | ARMv8 | ARMv8 | x86 |
| 核心数 | 最高 64 核 | 最高 64 核 | 最高 32 核 |
| 生态 | 国产 OS/中间件 | 鲲鹏生态 | x86 兼容 |
| 国产化 | 自主核心 | 自主核心 | x86 授权 |

## 选购与部署建议

- 部署前确认操作系统、数据库及中间件对 ARM 架构的适配与性能优化。
- 评估多路互联、内存容量与 I/O 扩展是否满足目标负载需求。
- 建议通过飞腾官方渠道或授权集成商获取兼容性列表与技术支持。

## 相关词条

- [制造商：飞腾 / Phytium](../companies/company_phytium.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考资料

1. [飞腾官网](https://www.phytium.com.cn)
2. [飞腾产品页](https://www.phytium.com.cn/product/)
3. 飞腾公开产品手册
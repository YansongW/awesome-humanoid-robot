# 平头哥玄铁 C920 / T-Head Xuantie C920

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [平头哥半导体 / T-Head](../companies/company_t_head.md) |
| **产品类别** | RISC-V 高性能处理器 IP |
| **发布时间** | 玄铁 C920 为新一代高性能 RISC-V 处理器 |
| **状态** | 商用授权 |
| **官网/来源** | 平头哥官网、阿里云栖大会资料 |

## 产品概述

平头哥玄铁 C920 是平头哥半导体推出的高性能 RISC-V 应用处理器 IP，面向边缘 AI、工业控制、机器人及 AIoT 等场景。

玄铁 C920 基于 RV64GC 指令集并支持 RISC-V Vector 1.0 扩展，采用 12 级乱序超标量流水线，具备高主频、高算力与良好能效比。其开放的 RISC-V 生态与可定制特性，使芯片客户能够针对机器人控制、视觉处理与 AI 推理等任务进行深度优化。

## 产品图片

> 平头哥玄铁 C920：请访问 [官方资料](https://www.t-head.cn) 查看。

## 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 处理器 IP | 玄铁 C920 | 平头哥官网 |
| 指令集 | RISC-V RV64GC + Vector 1.0 | 平头哥公开资料 |
| 微架构 | 12 级乱序超标量 | 平头哥公开资料 |
| 主频 | 最高 3 GHz（公开报道） | 公开报道 |
| 算力 | 未公开 | - |
| 缓存 | 支持多级缓存 | 平头哥公开资料 |
| 总线接口 | AXI / ACE | 平头哥公开资料 |
| 扩展支持 | 可集成 AI 加速器、安全扩展 | 平头哥公开资料 |
| 功耗 | 视具体实现而定 | 平头哥公开资料 |
| 价格 | IP 授权，未公开 | - |

## 供应链位置

- **制造商**：[平头哥半导体 / T-Head](../companies/company_t_head.md)
- **核心零部件/技术来源**：自研 RISC-V 内核、EDA 工具、授权客户晶圆代工/封测。
- **下游应用/客户**：芯片设计公司、AIoT 厂商、汽车电子、工业控制、机器人芯片厂商。

## 知识图谱节点与关系

- 产品实体：`ent_product_t_head_xuantie_c920`
- 零部件实体：`ent_component_t_head_xuantie_c920_ip`
- 制造商实体：`ent_company_t_head`
- 关键关系：
  - `rel_ent_company_t_head_manufactures_ent_product_t_head_xuantie_c920`（`ent_company_t_head` → `manufactures` → `ent_product_t_head_xuantie_c920`）
  - `rel_ent_company_t_head_manufactures_ent_component_t_head_xuantie_c920_ip`（`ent_company_t_head` → `manufactures` --> `ent_component_t_head_xuantie_c920_ip`）
  - `ent_product_t_head_xuantie_c920` -- `uses` --> `ent_component_t_head_xuantie_c920_ip`

## 应用场景

- **机器人主控 MCU/MPU**：作为机器人运动控制、通信与任务调度的核心处理器。
- **边缘 AI 计算**：集成 NPU 后用于端侧图像识别、语音处理与传感器融合。
- **工业控制与 AIoT**：为智能制造、智能家居、可穿戴设备提供高能效计算。

## 竞争对比

| 对比项 | 玄铁 C920 | ARM Cortex-A78 | SiFive P550 |
|--------|------|------|------|
| 指令集 | RISC-V | ARM | RISC-V |
| 生态 | 平头哥/开源 RISC-V | ARM 成熟生态 | SiFive 生态 |
| 定制化 | 高 | 中 | 高 |
| 授权模式 | IP 授权 | IP 授权 | IP 授权 |

## 选购与部署建议

- 评估目标软件栈对 RISC-V Vector 与特权架构的支持情况。
- 根据性能、功耗与面积目标选择 C920 配置，并预留 AI 加速器集成空间。
- 建议通过平头哥官方渠道获取 IP 包、参考设计与技术支持。

## 相关词条

- [制造商：平头哥半导体 / T-Head](../companies/company_t_head.md)
- [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考资料

1. [平头哥官网](https://www.t-head.cn)
2. [平头哥玄铁系列](https://www.t-head.cn/product/)
3. 阿里云栖大会公开资料
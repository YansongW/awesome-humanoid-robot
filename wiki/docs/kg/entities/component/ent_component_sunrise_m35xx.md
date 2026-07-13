---
id: ent_component_sunrise_m35xx
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Sunrise M35XX 系列六维力/力矩传感器
  en: Sunrise Instruments M35XX Series 6-Axis Force/Torque Sensor
status: active
sources:
- id: src_sunrise_selection_guide
  type: website
  url: https://www.srisensor.com/selection-guide/
- id: src_sunrise_catalog_2025
  type: website
  url: https://www.srisensor.com/uploads/2025-Force-Sensor-Product-catalog_English2.pdf
- id: src_sunrise_app_note
  type: website
  url: https://www.srisensor.com/uploads/13d2fa2c.pdf
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# Sunrise M35XX 系列六维力/力矩传感器

## 概述

Sunrise Instruments（SRI，中文常称“ Sunrise Instruments”或“SRI传感器”）M35XX 系列是一款超薄型六维力/力矩（6-axis Force/Torque，6-DOF F/T）传感器，专为安装空间受限的机器人末端执行器、协作机器人腕部、医疗假肢及精密装配场景设计。该系列采用应变电测原理与矩阵解耦算法，可同时测量三维力 $(F_x, F_y, F_z)$ 与三维力矩 $(M_x, M_y, M_z)$。根据厂商公开选型资料，M35XX 系列厚度仅约 $9.2\,\text{mm}$，外径覆盖 $\phi 30\,\text{mm}$ 至 $\phi 90\,\text{mm}$，额定力范围 $150\,\text{N}$ 至 $2000\,\text{N}$，额定力矩范围 $2.2\,\text{Nm}$ 至 $40\,\text{Nm}$，典型过载能力为满量程的 $300\%$，防护等级为 IP60。

## 工作原理 / 技术架构

M35XX 系列基于金属弹性体上的应变片全桥网络。当外力/力矩作用于传感器负载端时，弹性体产生微小形变，粘贴在弹性梁上的应变片电阻发生变化，惠斯通电桥输出与载荷成比例的毫伏级电压信号。设电桥激励电压为 $V_{\text{exc}}$，应变片阻值变化率为 $\Delta R/R$，则理想输出电压可表示为

$$
V_{\text{out}} = V_{\text{exc}} \cdot \frac{\Delta R}{4R}.
$$

由于六维力传感器的各通道输出存在机械与电气耦合，M35XX 采用矩阵解耦方式。厂商在校准过程中施加标准力/力矩，建立 $6 \times 6$ 灵敏度矩阵 $\mathbf{C}$，实际力/力矩向量 $\mathbf{F}$ 由原始输出电压向量 $\mathbf{V}$ 经解耦矩阵求得：

$$
\mathbf{F} = \mathbf{C}^{-1} \cdot \mathbf{V}.
$$

M35XX 系列提供低电压模拟输出（mV/V），可配合 SRI M830X 放大器或 M812X 数据采集接口盒实现 RS-232、CAN、Ethernet、EtherCAT 等数字输出。其超薄结构通过将应变梁沿径向平面布置实现，能够在保持较高刚度的同时降低轴向高度，适用于机器人腕部等轴向尺寸受限的位置。

## 关键参数表

| 参数 | 规格 |
|---|---|
| 测量维度 | $F_x, F_y, F_z, M_x, M_y, M_z$（六维） |
| 系列外径 | $\phi 30\,\text{mm}$ – $\phi 90\,\text{mm}$ |
| 典型厚度 | $9.2\,\text{mm}$ |
| 额定力范围 | $150\,\text{N}$ – $2000\,\text{N}$（依型号） |
| 额定力矩范围 | $2.2\,\text{Nm}$ – $40\,\text{Nm}$（依型号） |
| 非线性/迟滞 | $\leq 1\% \, \text{F.S.}$ |
| 串扰 | $\leq 3\% \, \text{F.S.}$ |
| 过载能力 | $300\% \, \text{F.S.}$ |
| 防护等级 | IP60 |
| 解耦方式 | 矩阵解耦 |
| 输出形式 | 低电压模拟 / 配接放大器或数采盒后数字输出 |

## 应用场景

M35XX 系列主要部署于空间受限且需要力控反馈的机器人任务：

- **协作机器人腕部力控**：在装配、抛光、打磨等任务中提供末端力/力矩反馈，实现柔顺控制与碰撞检测。
- **精密装配与插拔**：通过实时监测 $F_z$ 与 $M_x, M_y$ 判断轴孔对准状态，降低过盈装配损伤风险。
- **医疗康复与假肢**：超薄结构便于嵌入假肢接受腔或外骨骼关节，测量人机交互力矩。
- **自动化打磨/抛光**：与浮动磨头或机器人力控软件配合，维持恒定的接触力。

## 供应链关系

在机器人产业链中，Sunrise Instruments 作为六维力/力矩传感器核心零部件供应商，向上游采购应变片、弹性体金属坯料、放大器芯片与接插件，向下游服务于机器人本体制造商、系统集成商与自动化终端用户。M35XX 系列通常被集成到协作机器人腕部或末端执行器中，是连接“机器人本体—末端工具—被操作对象”的关键感知节点。典型下游客户包括 ABB、KUKA、YASKAWA 等工业机器人厂商以及高校与研究机构。

## 来源与验证

- Sunrise Instruments 官网选型指南（https://www.srisensor.com/selection-guide/）列明 M35XX 系列外径、厚度、量程与过载能力。
- Sunrise Instruments 2025 产品型录（PDF）确认 M35XX 系列 $9.2\,\text{mm}$ 厚度、矩阵解耦、非线性/迟滞 $\leq 1\%$ F.S.、串扰 $\leq 3\%$ F.S.、IP60 防护等级等参数。
- SRI 应用笔记 SRI-AN01 详细说明应变电桥、矩阵解耦方法及低电压/数字输出配置。
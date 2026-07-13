---
id: ent_component_probe_sensor
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 接触式测头/探针传感器
  en: Touch Probe Sensor
status: active
sources:
- id: src_hexagon_romer_manual
  type: white_paper
  url: https://static.machinetools.com/uploads/2703507/Romer_Absolute_Arm_Manual_V2.3.1-En.pdf
- id: src_hexagon_arm_brochure
  type: white_paper
  url: https://www.exactmachineservice.com/assets/pdfs/hexagon-romer-absolute-arm-brochure.pdf
- id: src_hexagon_absolute_arm
  type: website
  url: https://hexagon.com/products/absolute-arm
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 接触式测头/探针传感器

## 概述

接触式测头（Touch Probe）是坐标测量机（CMM）、便携式测量臂及机器人标定系统中使用的关键传感部件。测头前端装有红宝石或硬质合金测球，当测球与被测表面接触时触发信号，测量系统记录此刻测球中心的三维坐标，从而获取工件几何尺寸与形位公差。在知识图谱中，该零部件与 Hexagon ROMER Absolute Arm 存在 `uses` 关系，是其执行触觉测量的末端传感单元。

## 工作原理 / 技术架构

接触式触发测头内部通常采用运动学支座（kinematic seat）与应变敏感机构。未触发时，测针由三个支撑点精确定位；测球接触工件后产生微小位移，使内部电路状态翻转并发出触发脉冲。测量软件将该触发时刻的关节编码器读数转换为测球中心坐标：

$$
P_{\text{tip}} = P_{\text{probe}} + r \cdot \mathbf{n}
$$

其中 $P_{\text{probe}}$ 为测头安装中心坐标，$r$ 为测球半径，$\mathbf{n}$ 为测球接触点法向矢量。对于便携式测量臂，最终测点坐标由臂的正向运动学计算：

$$
P_{\text{tip}} = f(\theta_1, \theta_2, \ldots, \theta_n) + r \cdot \mathbf{n}
$$

$\theta_i$ 为各关节绝对编码器角度。Hexagon ROMER Absolute Arm 配备 TKJ 快速更换测头接口与自动测头识别功能，测头更换后无需现场重新校准。

## 关键参数表

| 参数项 | 数值 / 说明 |
|--------|-------------|
| 类型 | 接触式触发测头 / 探针传感器 |
| 典型测球材料 | 红宝石（Ruby）/ 硬质合金 |
| 典型测球直径 | 3 mm、6 mm（依配置） |
| 触发方式 | 运动学支座触发 / 应变触发 |
| 测头接口 | TKJ 快速更换接口（Hexagon ROMER 臂） |
| 单点重复精度（搭配 ROMER 臂） | 0.010–0.027 mm（视臂型号与臂长） |
| 体积精度（搭配 ROMER 臂） | $\pm 0.020$–$\pm 0.069$ mm（视型号） |
| 触发力 | 未公开 |
| 工作温度 | 0 °C – 45 °C（依赖整机规格） |
| 价格 | 未公开 |

## 应用场景

- **便携式测量臂 tactile 测量**：配合 Hexagon ROMER Absolute Arm 完成车间现场尺寸检测。
- **三坐标测量机**：在桥式/龙门式 CMM 上执行精密几何量测。
- **机器人标定**：标定机器人 DH 参数、连杆长度与法兰偏差。
- **逆向工程**：逐点数字化复杂曲面与工装夹具。

## 供应链关系

在公司—产品—零部件网络中，接触式测头属于**精密测量传感零部件层**：

- **上游**：红宝石/硬质合金测球、精密轴承、触发机构、电子电路、测杆材料。
- **自身位置**：`ent_product_hexagon_romer_arm -- uses --> ent_component_probe_sensor`。
- **下游**：便携式测量臂、三坐标测量机、机器人标定系统及工业计量服务商。

## 来源与验证

- ROMER Absolute Arm User Manual：https://static.machinetools.com/uploads/2703507/Romer_Absolute_Arm_Manual_V2.3.1-En.pdf
- Hexagon ROMER Absolute Arm Brochure：https://www.exactmachineservice.com/assets/pdfs/hexagon-romer-absolute-arm-brochure.pdf
- Hexagon Absolute Arm 产品页：https://hexagon.com/products/absolute-arm

测头接口、自动识别与快速更换机制来自 Hexagon 官方手册；单点重复精度与体积精度为 ROMER Absolute Arm 整机公开指标，具体测头触发力与价格未公开。
---
id: ent_product_hexagon_romer_arm
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 海克斯康 ROMER Absolute Arm 便携式测量臂
  en: Hexagon ROMER Absolute Arm Portable Measuring Arm
status: active
sources:
- id: src_hexagon_absolute_arm
  type: website
  url: https://hexagon.com/products/absolute-arm
- id: src_hexagon_romer_brochure
  type: white_paper
  url: https://www.exactmachineservice.com/assets/pdfs/hexagon-romer-absolute-arm-brochure.pdf
- id: src_hexagon_romer_manual
  type: white_paper
  url: https://static.machinetools.com/uploads/2703507/Romer_Absolute_Arm_Manual_V2.3.1-En.pdf
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 海克斯康 ROMER Absolute Arm 便携式测量臂

## 概述

ROMER Absolute Arm 是海克斯康（Hexagon AB）制造的高精度便携式关节臂三坐标测量机（Portable CMM）。该设备采用碳纤维结构与各关节绝对式编码器，开机无需回零或预热，可直接用于车间现场的触觉测量或激光扫描。设备提供 6 轴（专注触觉测量）与 7 轴（集成/外接激光扫描）配置，臂长覆盖 1.2 m 至 4.5 m，广泛应用于汽车、航空航天、模具、机器人标定与逆向工程。

## 工作原理 / 技术架构

ROMER Absolute Arm 由肩、肘、腕多段关节组成，每段关节内置高精度绝对式编码器，实时测量关节转角 $\theta_i$。通过正向运动学将关节角度转换为测头尖端三维坐标：

$$
P_{\text{tip}} = T_1(\theta_1) T_2(\theta_2) \cdots T_n(\theta_n) \cdot P_{\text{probe}}
$$

其中 $T_i$ 为第 $i$ 个关节的 Denavit-Hartenberg（DH）变换矩阵，$P_{\text{probe}}$ 为测头在腕部坐标系中的偏移。6 轴臂包含 6 个旋转轴（A/B/C/D/E/F），7 轴臂额外增加扫描头旋转自由度。

接触测量时，系统记录触发时刻的测球中心坐标，并补偿测球半径 $r$：

$$
P_{\text{surface}} = P_{\text{tip}} - r \cdot \mathbf{n}
$$

$\mathbf{n}$ 为测点表面法向。绝对编码器消除了传统增量编码器的回零需求，使设备具备“开机即测”能力。

## 关键参数表

| 参数项 | 数值 / 说明 |
|--------|-------------|
| 制造商 | 海克斯康 / Hexagon AB |
| 类型 | 便携式关节臂三坐标测量机 |
| 轴数 | 6 轴 / 7 轴 |
| 测量范围 | 1.2 m – 4.5 m（多种臂长） |
| 单点重复精度 | 0.010 – 0.027 mm（视型号与臂长） |
| 体积精度（MPEe） | ±0.020 – ±0.069 mm（视型号） |
| 测头类型 | 接触式测头 / 触发测头 / 激光扫描测头 |
| 编码器 | 各关节绝对式编码器 |
| 接口 | USB / Wi-Fi |
| 工作温度 | 0 °C – 45 °C（部分型号 5 °C – 45 °C） |
| 防护等级 | IP54 |
| 裸机重量 | 约 7.9 – 10.8 kg（视型号，不含测头） |
| 软件 | PC-DMIS Portable / RDS |
| 价格 | 未公开 |

## 应用场景

- **车间现场检测**：钣金件、铸件、塑料件、碳纤维件的尺寸与形位公差测量。
- **机器人标定**：标定机器人连杆参数、DH 参数与法兰安装偏差。
- **逆向工程**：配合激光扫描头获取复杂曲面点云，生成 CAD 模型。
- **工装夹具验证**：焊接夹具、装配治具的现场精度校验。

## 供应链关系

在公司—产品—零部件网络中，ROMER Absolute Arm 处于**精密测量设备产品层**：

- **上游**：高精度光栅尺/绝对编码器、碳纤维管材、轴承、测头传感器、花岗石/磁性底座、工业软件 IP。
- **自身位置**：`ent_company_hexagon -- manufactures --> ent_product_hexagon_romer_arm`；`ent_product_hexagon_romer_arm -- uses --> ent_component_probe_sensor`。
- **下游**：汽车、航空航天、电子、医疗器械、机器人零部件与整机制造商。

## 来源与验证

- Hexagon Absolute Arm 产品页：https://hexagon.com/products/absolute-arm
- ROMER Absolute Arm Brochure：https://www.exactmachineservice.com/assets/pdfs/hexagon-romer-absolute-arm-brochure.pdf
- ROMER Absolute Arm User Manual：https://static.machinetools.com/uploads/2703507/Romer_Absolute_Arm_Manual_V2.3.1-En.pdf

轴数、臂长范围、单点重复精度、体积精度与防护等级均来自 Hexagon 官方资料；具体型号报价需联系海克斯康或其授权代理商。
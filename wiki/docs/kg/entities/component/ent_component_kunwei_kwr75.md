---
id: ent_component_kunwei_kwr75
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 坤维 KWR75 六维力/力矩传感器
  en: Kunwei KWR75 6-Axis Force/Torque Sensor
status: active
sources:
- id: src_kunwei_kwr75_product
  type: website
  url: https://www.czkunweitech.com/products/kwr75-six-axis-forcetorque-sensor-for-robot-arm/
- id: src_kunwei_kwr75b_guide
  type: website
  url: https://www.lowdigit.com/images/Datasheets/Dobot/Low_Digit_Dobot_KWR75B%20Sensor%20User%20Guide.pdf
- id: src_kunwei_madeinchina
  type: website
  url: https://m.made-in-china.com/product/Kunwei-Strain-Gauge-Six-Axis-Force-Sensor-for-Industrial-Welding-Robot-2084396995.html
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 坤维 KWR75 六维力/力矩传感器

## 概述

坤维（Kunwei）KWR75 系列是一款面向协作机器人（Cobot）与轻型工业机械臂的六维力/力矩传感器，采用硅应变片与应变电测原理，将负载转换为电压信号，并结合六轴联合校准技术抑制通道间串扰。该系列外径为 $75\,\text{mm}$，提供多种量程型号（如 KWR75A/B/C/D/E/F），可覆盖 $30\,\text{N}$ 至 $500\,\text{N}$ 的力测量范围以及 $1.5\,\text{Nm}$ 至 $18\,\text{Nm}$ 的力矩测量范围。KWR75 系列默认采用数字串口输出，并可选配 RS-422/RS-485、Modbus、CAN、工业以太网或 USB 接口，便于直接接入机器人控制器。

## 工作原理 / 技术架构

KWR75 系列基于应变电测技术：弹性体在受力后产生应变，粘贴在弹性体上的硅应变片阻值变化，经惠斯通电桥转换为差分电压。设传感器标定灵敏度为 $S$（单位 $\text{mV}/\text{V}$ 每单位载荷），激励电压为 $V_{\text{exc}}$，则输出电压 $V_{\text{out}}$ 与载荷 $F$ 近似满足

$$
V_{\text{out}} = S \cdot V_{\text{exc}} \cdot F.
$$

由于六维传感器的各输出通道存在机械耦合，坤维采用六轴联合校准算法，在标定过程中对 $F_x/F_y/F_z$ 与 $M_x/M_y/M_z$ 六个通道同步施加标准载荷，建立解耦矩阵并对每个传感器单独生成校准参数，从而降低串扰误差。传感器内置高精度信号调理与 A/D 转换电路，采样频率可达 $1\,\text{kHz}$，并通过数字接口输出已解耦的力/力矩数据。

## 关键参数表

| 参数 | KWR75B（典型型号） | 系列范围 |
|---|---|---|
| 测量维度 | $F_x, F_y, F_z, M_x, M_y, M_z$ | 六维 |
| $F_x, F_y$ 额定量程 | $200\,\text{N}$ | $30\,\text{N}$ – $400\,\text{N}$ |
| $F_z$ 额定量程 | $200\,\text{N}$ | $30\,\text{N}$ – $700\,\text{N}$ |
| $M_x, M_y$ 额定量程 | $8\,\text{Nm}$ | $1.5\,\text{Nm}$ – $18\,\text{Nm}$ |
| $M_z$ 额定量程 | $8\,\text{Nm}$ | $1.5\,\text{Nm}$ – $18\,\text{Nm}$ |
| 外径 | $75\,\text{mm}$ | $75\,\text{mm}$ |
| 高度 | $31.5\,\text{mm}$ | $31.5\,\text{mm}$ – $33.5\,\text{mm}$ |
| 重量 | $0.28\,\text{kg}$ | $0.26\,\text{kg}$ – $0.36\,\text{kg}$ |
| 过载能力 | $300\% \, \text{F.S.}$ | $300\% \, \text{F.S.}$ |
| 分辨率 | $0.03\% \, \text{F.S.}$ | $0.03\% \, \text{F.S.}$ |
| 重复性 | $0.1\% \, \text{F.S.}$ | $0.1\% \, \text{F.S.}$ |
| 精度 | $0.5\% \, \text{F.S.}$ | $0.5\% \, \text{F.S.}$ |
| 采样频率 | $1\,\text{kHz}$ | $1\,\text{kHz}$ |
| 供电电压 | $9\text{–}24\,\text{VDC}$ | $9\text{–}24\,\text{VDC}$（部分型号 $12\text{–}48\,\text{VDC}$） |
| 通信接口 | RS-422/RS-485/Modbus/CAN/Ethernet/USB | 依型号可选 |
| 防护等级 | IP64 | IP64 |

## 应用场景

KWR75 系列主要应用于需要力/力矩反馈的轻型机器人系统：

- **协作机器人拖动示教**：通过实时读取腕部力矩，操作人员可直接牵引机械臂完成轨迹示教。
- **3C 产品装配与测试**：在手机、笔记本等精密部件装配中实现轴孔插入力监测与微小力控制。
- **医疗康复设备**：用于外骨骼或康复机器人关节，测量人机交互力矩并保障安全性。
- **汽车与电子检测**：在零部件压装、按键手感测试、线束插拔等场景中进行力特征采集。

## 供应链关系

坤维科技作为六维力传感器核心零部件厂商，位于机器人供应链上游，其客户包括协作机器人整机厂商、自动化集成商与科研院所。KWR75 系列常被集成在机械臂腕部或末端法兰处，是机器人由“位置控制”向“力位混合控制”升级的关键传感器。越疆（Dobot）等协作机器人厂商的用户指南中已将 KWR75B 列为可选末端力控配件，说明其在国产协作机器人生态中已被广泛采用。

## 来源与验证

- 坤维官网产品页（https://www.czkunweitech.com/products/kwr75-six-axis-forcetorque-sensor-for-robot-arm/）列明 KWR75 系列采用硅应变片、六轴联合校准、适用协作机器人腕部等核心信息。
- Low Digit Dobot KWR75B Sensor User Guide 提供 KWR75B 的精确量程、尺寸、重量、电气接口与采样频率参数。
- Made-in-China 平台坤维产品页给出 KWR75A–F 全系列量程对照表，确认 $F_x/F_y$、$F_z$、$M_x/M_y$、$M_z$ 的型号覆盖范围。
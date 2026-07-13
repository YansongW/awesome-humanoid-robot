---
id: ent_component_cooldrive_r
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 清能德创 CoolDrive R 系列伺服驱动器
  en: CoolDrive R Series Servo Drive
sources:
- id: src_cooldrive_official
  type: website
- title: '"清能德创官网"'
  url: https://www.cooldrive.com.cn
- id: src_cooldrive_chuandong
  type: website
- title: '"CoolDrive R 系列产品介绍"'
  url: https://www.chuandong.com/product/product208600.html
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official datasheets, product manuals and verified
    distributors; missing values marked as 未公开.
---


# 清能德创 CoolDrive R 系列伺服驱动器 / CoolDrive R Series Servo Drive

## 概述

CoolDrive R 系列是清能德创电气技术（北京）有限公司面向工业机器人推出的多轴一体化网络伺服驱动器。该系列将 6/4/3 个伺服轴集成于单一机身，内置振动抑制、速度/加速度前馈、惯量前馈与功能安全，可显著节省控制柜空间并提升机器人动态性能。

## 工作原理 / 技术架构

驱动器采用共直流母线多轴架构，通过 EtherCAT 工业以太网与机器人控制器通信，支持位置、速度与转矩三环控制。电机电流环控制转矩：

$$\tau = K_t \cdot I_q$$

其中 $K_t$ 为电机转矩常数，$I_q$ 为交轴电流。CoolDrive R 内置速度/加速度前馈、定位抖动消除与弱磁控制算法，可在轻载下实现高速运行；同时支持 STO/SS1/SLS 等功能安全。

## 关键参数表

| 参数 | 数值 | 备注 |
|---|---|---|
| 产品形态 | 多轴一体化网络伺服驱动器 | 清能德创资料 |
| 轴数 | R6/R4/R3 等，6/4/3 轴 | 清能德创资料 |
| 功率范围 | 未公开 | 需按型号确认 |
| 通信协议 | EtherCAT / CANopen | 清能德创资料 |
| 控制模式 | 位置 / 速度 / 转矩 | 清能德创资料 |
| 编码器支持 | 增量式 / 绝对值 | 清能德创资料 |
| 安全功能 | STO、SS1、SLS 等 | 清能德创资料 |
| 安装空间节省 | 相比通用方案最高约 50% | 清能德创资料 |
| 速度环带宽 | 未公开 | - |
| 价格 | 未公开 | 需询价 |

## 应用场景

六关节工业机器人、协作机器人、Delta/SCARA 机器人、人形机器人关节驱动、数控机床、激光加工设备。

## 供应链关系

清能德创（`ent_company_cooldrive`）设计制造 CoolDrive R 系列，上游包括 IGBT/MOS、DSP/ARM 控制芯片、电流传感器与 PCB；下游客户为工业机器人、人形机器人与高端装备厂商，与汇川技术、雷赛智能、安川、三菱等竞争。

## 来源与验证

- 清能德创官网：https://www.cooldrive.com.cn
- CoolDrive R 系列介绍：https://www.chuandong.com/product/product208600.html
---
id: ent_component_ati_nano25
type: component
schema_version: 1
domain: 02_components
status: active
names:
  zh: ATI Nano25 六维力/力矩传感器
  en: ATI Nano25 Six-Axis Force/Torque Sensor
sources:
- id: src_ati_nano25_datasheet
  type: website
- title: ATI Nano25 Transducer Section Datasheet
  url: https://www.ati-ia.com/zh-CN/app_content/documents/9620-05-Transducer%20Section.pdf
- id: src_ati_nano25_manual
  type: website
- title: ATI F/T Sensor System Installation and Operation Manual
  url: https://www.ati-ia.com/zh-CN/app_content/documents/9610-05-1017-10.pdf
- id: src_ati_official
  type: website
- title: ATI Industrial Automation 官网
  url: https://www.ati-ia.com
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from official ATI datasheets and installation manuals;
    values correspond to SI-250-6 calibration unless noted.
---


# ATI Nano25 六维力/力矩传感器 / ATI Nano25 Six-Axis Force/Torque Sensor

## 概述

ATI Nano25 是 ATI Industrial Automation 推出的微型六维力/力矩（F/T）传感器，专为空间受限但对测量精度要求较高的应用设计。该传感器可同时测量三个正交方向的力（Fx、Fy、Fz）与三个正交方向的力矩（Tx、Ty、Tz），广泛应用于协作机器人、医疗手术机器人、人形机器人手腕/脚踝力控、机器人精密装配与手指力研究。

## 工作原理 / 技术架构

Nano25 基于硅应变计（silicon strain gauge）测力原理：

1. **弹性体结构**：传感器本体由高强度不锈钢经 EDM 线切割加工而成，内部形成多根弹性梁。外力/力矩作用于传感器时，弹性梁产生微小变形。
2. **硅应变计**：在弹性梁表面贴附高灵敏度硅应变计，其电阻变化与应变成正比，输出信号强度约为传统箔式应变计的 75 倍。
3. **信号调理与解耦**：传感器内部或外部采集系统对应变信号进行放大、温度补偿与矩阵解耦，输出六维力/力矩值。
4. **高过载保护**：单轴过载能力为额定量程的 5.7–12.3 倍，避免意外冲击导致传感器损坏。

六维力传感器的串扰（cross-talk）是衡量各通道独立性的关键指标。ATI 通过出厂标定提供解耦矩阵 $\mathbf{C}$，将原始应变信号向量 $\mathbf{s}$ 转换为力/力矩向量 $\mathbf{F}$：

$$
\mathbf{F} = \mathbf{C} \cdot \mathbf{s}
$$

其中 $\mathbf{F} = [F_x, F_y, F_z, T_x, T_y, T_z]^T$，解耦矩阵可显著降低通道间串扰。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制造商 | ATI Industrial Automation（Novanta 子公司） | 官网 |
| 传感器类型 | 六维力/力矩传感器（6-DOF F/T） | 官方 datasheet |
| 直径 | 25 mm | 官方 datasheet |
| 高度 | 21.6 mm | 官方 datasheet |
| 重量 | 63.4 g（含标准安装板） | 官方 datasheet |
| 力测量范围（Fx/Fy） | ±250 N | SI-250-6 标定 |
| 力测量范围（Fz） | ±1,000 N | SI-250-6 标定 |
| 力矩测量范围（Tx/Ty） | ±6 Nm | SI-250-6 标定 |
| 力矩测量范围（Tz） | ±3.4 Nm | SI-250-6 标定 |
| 单轴过载能力 | 额定量程的 7.1–15.1 倍 | 经销商 datasheet |
| 共振频率 | Fx/Fy/Tz: 3,600 Hz；Fz/Tx/Ty: 3,800 Hz | 官方 datasheet |
| 刚度（X/Y 向力） | 53 × 10⁶ N/m | 官方 datasheet |
| 刚度（Z 向力） | 110 × 10⁶ N/m | 官方 datasheet |
| 防护等级 | 可选 IP65 / IP68 | 官方 datasheet |
| 输出接口 | 模拟 / DAQ / EtherCAT / Net / TWE / WNet / Controller | 官方 datasheet |
| 供电电压 | 由采集系统提供 | - |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **人形机器人手腕/脚踝力控**：为全身平衡、足式行走与双臂操作提供六维接触力反馈。
- **协作机器人拖拽示教与安全碰撞检测**：实时监测末端接触力，实现人机协作中的安全停机和柔顺拖动。
- **医疗手术机器人**：用于微创手术器械的末端力反馈，提升医生操作临场感。
- **机器人精密装配与打磨**：监测插销、螺纹装配、抛光打磨过程中的接触力，实现恒力控制。
- **手指力研究与遥操作**：作为小型化力觉传感器，部署于灵巧手指端或主手控制器。

## 供应链关系

ATI Industrial Automation（`ent_company_ati`）是全球六维力/力矩传感器与机器人末端执行器龙头，2021 年被 Novanta Inc. 收购。Nano25（`ent_component_ati_nano25`）属于 Nano 系列微型 F/T 传感器产品线。ATI 的上游包括高强度不锈钢、硅应变计、信号调理电路与精密机械加工；下游客户覆盖工业机器人、协作机器人、医疗手术机器人、人形机器人与 FANUC 等机器人 OEM。ATI 与 OnRobot、Robotiq、宇立仪器、坤维科技、海伯森等形成竞争。在知识图谱中，ATI 同时为 FANUC CRX 协作机器人提供末端执行器套件。

## 来源与验证

- ATI 官方 Transducer Section Datasheet 提供了 Nano25 的尺寸、量程、刚度、共振频率等核心参数。
- ATI F/T 传感器系统安装与操作手册提供了 SI/US 标定、分辨率、过载能力等详细规格。
- ATI 官网与 Novanta 收购公告确认了公司背景与产品线定位。
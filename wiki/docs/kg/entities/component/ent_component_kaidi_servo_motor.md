---
id: ent_component_kaidi_servo_motor
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 凯迪伺服电机
  en: Kaidi Servo Motor
status: active
sources:
- id: src_kaidi_official
  type: website
- title: 凯迪股份官网
  url: https://www.kaidi-electric.com
- id: src_kaidi_annual_report
  type: report
- title: 凯迪股份年度报告与投资者关系
  url: http://www.sse.com.cn
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: 参数引自凯迪股份官网与年报；核心机电参数未公开，已标注。
---


# 凯迪伺服电机 / Kaidi Servo Motor

## 概述

凯迪伺服电机是常州市凯迪电器股份有限公司（Kaidi Electrical，SH.605828）生产的伺服电机产品。凯迪股份主营线性驱动系统、电动推杆与伺服电机，近年来积极布局人形机器人线性关节模组，开发高推力密度电动缸与微型丝杠执行器。其伺服电机产品线与线性驱动器深度集成，支持位置、力矩与速度闭环控制。

## 工作原理 / 技术架构

伺服电机通过编码器反馈实现位置/速度/转矩闭环控制。永磁同步伺服电机的电磁转矩可表示为

$$
T = \frac{3}{2} p \psi_f I_q
$$

其中 $p$ 为极对数，$\psi_f$ 为永磁体磁链，$I_q$ 为 q 轴电流。配合伺服驱动器，电机可在宽调速范围内实现精确控制，满足机器人关节对动态响应与定位精度的要求。

## 关键参数表

| 参数 | 典型值 / 范围 | 备注 |
|------|--------------|------|
| 电机类型 | 永磁直流 / 无刷直流 | 产品手册 |
| 额定功率 | 未公开 | - |
| 额定转速 | 未公开 | - |
| 额定扭矩 | 未公开 | - |
| 电压 | 12–48 V DC | 产品手册 |
| 控制方式 | 位置 / 力矩 / 速度闭环 | 产品手册 |
| 法兰尺寸 | 未公开 | - |
| 防护等级 | IP42 / IP54（线性驱动器可选） | 产品手册 |
| 重量 | 未公开 | - |
| 价格 | 未公开 | - |

## 应用场景

- 智能家居驱动（升降桌、沙发、医疗床）
- 医疗康复设备
- 自动化执行机构
- 人形机器人线性关节
- 汽车与工业自动化

## 供应链关系

制造商为常州市凯迪电器股份有限公司（`ent_company_kaidi`）。上游关键原材料包括永磁材料、硅钢片、铝合金、轴承与控制器芯片；下游客户包括家具厂商、医疗器械企业、汽车 OEM 与人形机器人公司。知识图谱中的关键关系为：`ent_company_kaidi` -- `manufactures` --> `ent_component_kaidi_servo_motor`。

## 来源与验证

本卡片参数引自凯迪股份官网与年报公开资料。伺服电机具体型号、额定功率、额定转速、额定扭矩、重量等核心参数未公开。
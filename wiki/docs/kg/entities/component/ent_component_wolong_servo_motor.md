---
id: ent_component_wolong_servo_motor
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 卧龙伺服电机
  en: Wolong Servo Motor
status: active
sources:
- id: src_wolong_official
  type: website
- title: 卧龙电驱官网
  url: https://www.wolong.com
- id: src_wolong_servo_motor_page
  type: website
- title: Wolong Servo Motors Product Page
  url: https://www.wolong-electric.com/products-solutions/automation-solutions/motion-control/servo-motor
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: 参数引自卧龙电驱官网与产品页；具体 WM 型号细分参数未公开。
---


# 卧龙伺服电机 / Wolong Servo Motor

## 概述

卧龙伺服电机是卧龙电驱（Wolong Electric Drive，SH.600580）生产的伺服电机产品，WM 系列覆盖 100 W–7.5 kW 功率范围，法兰尺寸 40–180 mm。卧龙电驱是国内工业电机与驱动系统龙头，近年布局人形机器人高功率密度伺服电机与关节驱动方案。

## 工作原理 / 技术架构

伺服电机通过转子位置反馈实现磁场定向控制（FOC）。永磁同步电机的电磁转矩公式为

$$
T = \frac{3}{2} p \left[ \psi_f I_q + (L_d - L_q) I_d I_q \right]
$$

其中 $p$ 为极对数，$\psi_f$ 为永磁磁链，$I_d$、$I_q$ 为 d-q 轴电流，$L_d$、$L_q$ 为 d-q 轴电感。WM 系列采用分芯绕组设计，具有高功率密度与小槽口转矩脉动，适配多种编码器配置与高/中/低惯量应用。

## 关键参数表

| 参数 | 典型值 / 范围 | 备注 |
|------|--------------|------|
| 系列 | WM 系列 | 产品手册 |
| 法兰尺寸 | 40 / 60 / 80 / 100 / 130 / 180 mm | 产品手册 |
| 额定功率 | 100 W – 7.5 kW | 产品手册 |
| 额定扭矩 | 0.32 – 48 N·m | 产品手册 |
| 额定转速 | 3000 rpm | 产品手册 |
| 最高转速 | 6000 rpm | 产品手册 |
| 防护等级 | IP65（部分型号） | 产品手册 |
| 重量 | 0.5–10 kg | 产品手册 |
| 效率等级 | IE5 / GB 1 级（WERMA5 系列） | 产品手册 |
| 价格 | 未公开 | - |

## 应用场景

- 工业机器人关节驱动
- 人形机器人大功率关节
- 数控机床进给与主轴
- 包装机械与物流自动化
- 新能源产线与电力装备

## 供应链关系

制造商为卧龙电驱（`ent_company_wolong`），隶属卧龙控股集团有限公司。上游关键原材料包括硅钢片、铜线、磁材、轴承、功率器件（IGBT/SiC）与控制器芯片；下游客户包括工业企业、新能源车企、机器人整机厂与能源装备制造商。知识图谱中的关键关系为：`ent_company_wolong` -- `manufactures` --> `ent_component_wolong_servo_motor`。

## 来源与验证

本卡片参数引自卧龙电驱官网伺服电机产品页与公开产品手册。具体 WM 型号细分参数、价格未公开。
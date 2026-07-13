---
id: ent_company_step
schema_version: 1
type: company
'title:': Step Automation / Kinco
domain: 02_components
theoretical_depth: system
names:
  zh: 步科股份
  en: Step Automation / Kinco
status: active
sources:
- id: src_step_official
  type: website
  url: https://www.kinco.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---





# 步科股份 / Step Automation / Kinco

> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

## 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 步科股份 |
| **英文名** | Step Automation / Kinco |
| **总部** | 中国深圳 |
| **成立时间** | 1996 |
| **官网** | [https://www.kinco.cn](https://www.kinco.cn) |
| **供应链环节** | 伺服驱动 / 低压伺服 / HMI |
| **企业属性** | 上市公司（SH.688160）、国内品牌 |
| **母公司/所属集团** | 深圳市步科电气有限公司 / Kinco |
| **数据来源** | 官网、年报、产品手册、WAIC 2026 报道 |

## 公司简介

国内领先的机器自动化与数字化解决方案供应商，低压伺服系统在移动机器人领域市占率领先。

步科股份主营工业自动化设备控制核心部件，包括 HMI、PLC、伺服系统、低压伺服电机与驱动器。公司低压伺服产品广泛用于 AGV/AMR、协作机器人、医疗康复设备与人形机器人关节，具备高集成度、低能耗与快速响应特点。

## 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 低压伺服系统 | 移动机器人专用 | FD 系列、SMC 系列 | AGV/AMR、服务机器人 |
| 伺服驱动器 | 通用与专用伺服 | JD 系列、OD 系列 | 工业机器人、机床 |
| 人机界面 | 工业 HMI | GL100、GT100 系列 | 产线监控、设备控制 |

## 代表产品

### 低压伺服系统 / Step Low-Voltage Servo System

> 低压伺服系统：请访问 [官方资料](https://www.kinco.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 驱动器约 70×120×40 mm（参考） | 产品手册 |
| 重量 | 未公开 | 产品手册 |
| 供电电压 | DC 24–72 V | 产品手册 |
| 额定功率 | 50 W – 1 kW | 产品手册 |
| 额定转速 | 3,000 rpm | 产品手册 |
| 编码器 | 17/23 位多圈绝对值 | 产品手册 |
| 通信接口 | CANopen / EtherCAT / RS485 | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：低压直流供电、高功率密度、支持多种总线，适配移动机器人和电池供电设备。

**应用场景**：AGV/AMR 轮毂驱动、协作机器人关节、人形机器人下肢、外骨骼。

### 伺服电机 / Step Servo Motor

> 伺服电机：请访问 [官方资料](https://www.kinco.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 40/60/80 法兰（系列范围） | 产品手册 |
| 重量 | 0.3–3 kg | 产品手册 |
| 额定功率 | 100 W – 1.5 kW | 产品手册 |
| 额定扭矩 | 0.32–4.77 N·m | 产品手册 |
| 额定转速 | 3,000 rpm | 产品手册 |
| 防护等级 | IP65（部分型号） | 产品手册 |
| 编码器 | 23 位绝对值 | 产品手册 |
| 价格 | 未公开 | - |

**技术亮点**：高精度编码器、低齿槽转矩、紧凑结构，适合关节模组一体化集成。

**应用场景**：协作机器人、SCARA、Delta、人形机器人关节。

## 供应链位置

- **上游关键零部件/材料**：IGBT/SiC 功率器件、MCU/FPGA 控制芯片、磁性材料、编码器芯片、电容电阻
- **下游客户/应用场景**：AGV/AMR 厂商、协作机器人公司、人形机器人 OEM、医疗设备、物流自动化
- **主要竞争对手/对标**：汇川技术、禾川科技、雷赛智能、鸣志电器、Inovance

## 知识图谱节点与关系

- 公司实体：`ent_company_step`
- 产品/零部件实体：`ent_component_step_low_voltage_servo`, `ent_component_step_servo_motor`
- 关键关系：
  - `ent_company_step` -- `manufactures` --> `ent_component_step_low_voltage_servo`
  - `ent_company_step` -- `manufactures` --> `ent_component_step_servo_motor`

## 参考资料

1. [官网](https://www.kinco.cn)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.inovance.com)（请按实际产品型号核对）
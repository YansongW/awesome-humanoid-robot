---
id: ent_component_hcfa_x3e_motor
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 禾川 X3E 系列伺服电机
  en: HCFA X3E Series Servo Motor
sources:
- id: src_hcfa_x3e_catalog
  type: website
- title: HCFA 禾川科技官网产品页
  url: https://www.hcfa.cn
- id: src_hcfa_annual_report
  type: report
- title: HCFA 2024 年度报告
  url: https://www.hcfa.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Specifications from HCFA product catalog, annual report and public
    distributor listings; missing values marked as 未公开.
---


# 禾川 X3E 系列伺服电机 / HCFA X3E Series Servo Motor

## 概述

禾川 X3E 系列伺服电机是禾川科技（HCFA）推出的经济型通用伺服电机，与 SV-X3E 伺服驱动器配套构成 X3E 伺服系统。该系列电机覆盖 50 W 至 2 kW 功率范围，额定转速 3000 rpm，采用 17 位绝对值磁编码器或增量式编码器反馈，支持 EtherCAT、PROFINET、CANopen、Modbus 等工业总线，广泛应用于机器人、3C 电子、光伏、锂电及包装自动化等领域。

## 工作原理与技术架构

X3E 伺服电机为永磁同步伺服电机（PMSM），在矢量控制框架下运行。电磁转矩可表示为：

$$
T_e = \frac{3}{2} p \psi_f i_q
$$

其中 $p$ 为极对数，$\psi_f$ 为永磁体磁链，$i_q$ 为交轴电流。禾川 X3E 系统采用磁场定向控制（FOC），通过 SVPWM 调制实现电流环、速度环、位置环三环闭环控制。

主要技术特点包括：

- **编码器反馈**：标配 17 位绝对值磁编码器（部分型号可选 23 位多摩川绝对值编码器），提供单圈/多圈位置信息，无需电池备份。
- **总线通信**：与 SV-X3E 驱动器配合，支持 EtherCAT、PROFINET、CANopen、Modbus 等协议，便于多轴协同控制。
- **防护设计**：电机防护等级可达 IP65，适配一般工业环境。
- **电压等级**：AC 200 – 230 V（部分型号支持 380 V）。

## 关键参数

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 功率范围 | 50 W – 2 kW | HCFA X3E 手册 |
| 额定转速 | 3000 rpm | HCFA X3E 手册 |
| 最高转速 | 未公开（视型号）| - |
| 额定扭矩 | 未公开（系列范围）| - |
| 电压等级 | AC 200 – 230 V | HCFA X3E 手册 |
| 编码器 | 17 位绝对值磁编 / 增量式（可选 23 位）| HCFA X3E 手册 / 公开报道 |
| 防护等级 | IP65 | HCFA 企业公告 |
| 过载能力 | 未公开 | - |
| 绝缘等级 | 未公开 | - |
| 通信协议 | EtherCAT / PROFINET / CANopen / Modbus | HCFA 2024 年报 |
| 价格 | 未公开 | - |

注：具体型号的额定扭矩、最高转速、过载倍数及绝缘等级需以禾川官方产品手册为准。

## 应用场景

- **3C 自动化**：贴装、锁附、检测、搬运等高节拍定位应用。
- **包装机械**：枕式包装、立式包装、灌装产线的伺服定位。
- **光伏与锂电设备**：电池片传输、电芯叠片、注液等工序。
- **机器人**：SCARA、协作机器人及人形机器人关节的旋转驱动。
- **AGV/AMR**：与禾川低压伺服系统配合，用于移动机器人行走轮驱动。

## 供应链关系

- **上游**：稀土磁材、硅钢片、漆包线、轴承、编码器芯片、IGBT/SiC 功率器件（驱动器侧）、PCB。
- **制造商**：禾川科技（HCFA）通过关系 `ent_company_hcfa -- manufactures --> ent_component_hcfa_x3e_motor` 记录于知识图谱。
- **下游**：工业机器人、人形机器人、光伏、锂电、物流设备厂商。常与 `ent_component_hcfa_x5e_drive` 伺服驱动器形成配套。主要竞争对手包括汇川技术、雷赛智能、安川、松下等。

## 来源与验证

核心参数来自禾川科技官网产品页、2024 年度报告及 1688/Taobao 等分销商页面的公开信息。额定扭矩、最高转速、过载能力及绝缘等级未在公开资料中完整披露，已标注为未公开。
---
id: ent_component_shanghai_electromechanical_traction_machine
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 上海机电永磁同步曳引机
  en: Shanghai Electromechanical PM Traction Machine
status: active
sources:
- id: src_ent_component_shanghai_electromechanical_traction_machine_official
  type: website
  url: https://www.shanghai-electric.com
- id: src_ent_component_shanghai_electromechanical_traction_machine_wiki
  type: website
  url: docs/appendices/appendix-d/companies/company_shanghai_electromechanical.md
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 上海机电永磁同步曳引机 / Shanghai Electromechanical PM Traction Machine

## 概述

上海机电永磁同步曳引机（Shanghai Electromechanical Permanent Magnet Synchronous Traction Machine）是上海机电股份有限公司（Shanghai Electromechanical Co., Ltd.，SH.600835）面向电梯、自动扶梯及大负载垂直提升设备推出的无齿轮永磁同步曳引机系列。该系列以稀土永磁转子为核心，配合变频矢量控制驱动器，直接驱动曳引轮，省去了传统蜗轮蜗杆减速箱，具有高功率因数、高效率、低噪声和低维护量的特点，是电梯主机的主流技术路线之一。

## 工作原理与技术架构

曳引机由永磁同步电动机（PMSM）、曳引轮、制动器及编码器组成。变频器依据编码器反馈的转子位置，输出三相变频变压电源，产生与转子永磁磁场同步的旋转磁场，直接驱动曳引轮旋转，通过钢丝绳与曳引轮之间的摩擦力实现轿厢升降。

关键物理关系如下：

- 同步转速：
  $$
  n_s = \frac{60 f}{p}
  $$
  其中 $f$ 为定子供电频率，$p$ 为电机极对数。

- 额定输出转矩与功率：
  $$
  T_N = \frac{P_N \times 60}{2\pi n_N}
  $$
  其中 $P_N$ 为额定功率，$n_N$ 为额定转速。

- 对于典型 2:1 悬挂比（rope ratio $r=2$）的电梯系统，曳引轮侧 traction force 为：
  $$
  F_t = \frac{2 T}{D}
  $$
  其中 $D$ 为曳引轮直径。

- 整机效率：
  $$
  \eta = \frac{P_{\text{out}}}{P_{\text{in}}} \times 100\% \geq 90\%
  $$

制动器通常采用盘式电磁制动，额定制动力矩按 GB/T 24478 等标准一般不低于额定转矩的 2.5 倍；绝缘等级为 F 级，允许绕组温升较高，适应断续周期工作制。

## 关键参数表

| 参数项 | 数值/范围 | 备注 |
|--------|-----------|------|
| 产品形态 | 无齿轮永磁同步曳引机 | 系列化产品 |
| 额定功率 | 2.2–50 kW | 依型号 |
| 额定转速 | 100–250 rpm | 低速大转矩 |
| 额定转矩 | 200–5,000 N·m | 系列范围 |
| 供电电压 | 380 VAC | 三相 |
| 悬挂比 | 2:1（典型） | 亦可根据设计定制 |
| 效率 | ≥90% | 额定工况 |
| 功率因数 | ≈0.95 | 永磁同步特性 |
| 制动方式 | 盘式电磁制动器 | DC110V 典型 |
| 绝缘等级 | F 级 | — |
| 防护等级 | IP41–IP54 | 视型号 |
| 工作制 | 60% ED（典型） | 断续周期 |
| 编码器 | 2048/8192 P/R（可选） | 闭环矢量控制 |
| 噪声 | ≤60 dB | 电机噪声 |
| 工作温度 | -10 ℃ ~ +40 ℃ | — |
| 适用海拔 | ≤1000 m | — |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **电梯主机**：商用/住宅客梯、货梯、医用电梯的永磁同步无齿轮驱动主机。
- **自动扶梯与自动人行道**：大扭矩低速直驱方案。
- **垂直升降设备**：立体车库、舞台升降台、大负载提升机构。
- **重载机器人线性驱动**：在超大负载人形机器人或升降平台中作为直线运动的动力源。

## 供应链关系

在公司–产品–零部件网络中，该实体的位置为：

- **制造商**：`ent_company_shanghai_electromechanical`（上海机电股份有限公司）通过子公司生产该曳引机。
- **上游关键物料**：稀土永磁体（钕铁硼）、硅钢片、铜线、轴承钢、制动器摩擦片、编码器。
- **下游集成**：电梯整机厂、自动扶梯厂商、重载提升设备制造商，以及部分人形机器人/具身智能平台的升降关节模组。
- **知识图谱关系**：
  - `ent_company_shanghai_electromechanical` — `manufactures` → `ent_component_shanghai_electromechanical_traction_machine`
  - `ent_component_shanghai_electromechanical_traction_machine` — `used_in` → 电梯/垂直提升系统产品节点

## 来源与验证

- 上海机电官网公开的公司及产品方向信息：上海机电股份有限公司官网。
- 附录 D Wiki 中《上海机电 / Shanghai Electromechanical》词条摘录了永磁同步曳引机的系列功率、转速、转矩、电压、效率、防护等级等参数，并标注数据来自产品手册与 WAIC 2026 报道。
- 具体型号的精确参数未在公开网络完全披露，表格中系列范围以附录 D Wiki 及行业样本为准；若需单机选型，应以制造商最新产品手册或询价单为准。
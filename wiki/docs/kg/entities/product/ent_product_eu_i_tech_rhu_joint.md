---
id: ent_product_eu_i_tech_rhu_joint
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: component
names:
  zh: 意优 RHU 人形专用谐波一体化关节模组
  en: EYouBot RHU Humanoid Harmonic Drive Joint
status: active
sources:
- id: src_eyoubot_rhu_series
  type: website
  url: https://eyoubot.com/humanoid-harmonic-drive-robot-actuator
- title: 意优 RHU 人形专用谐波一体化关节模组
- id: src_eyoubot_rhu32h120
  type: website
  url: https://eyoubot.com/products/rhu32h-120
- title: RHU32H-120 产品参数
- id: src_eyoubot_donews_2026
  type: article
  url: https://www.donews.com/news/detail/4/6391898.html
- title: 意优科技发布 PHU、RHU、RP 三大量产关节方案
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 意优 RHU 人形专用谐波关节 / EYouBot RHU Humanoid Harmonic Joint

## 概述

意优 RHU 系列是意优科技（EYouBot）面向人形机器人仿生关节开发的谐波一体化关节模组。该系列在同等扭矩输出下将体积与重量较常规产品降低约 30%，支持大中空走线、双绝对值编码器、EtherCAT/CANopen 双通信协议以及安全扭矩关闭（STO）功能，可覆盖人形机器人上肢、腰部与下肢的旋转关节需求。

## 工作原理 / 技术架构

RHU 关节采用谐波减速器（strain-wave gear）作为核心传动单元，由波发生器、柔性薄壁齿轮（柔轮）和刚性外齿圈（刚轮）组成。波发生器每转一圈，柔轮与刚轮的齿数差使得输出端实现高减速比

$$
i=\frac{N_{\text{刚轮}}}{N_{\text{刚轮}}-N_{\text{柔轮}}},
$$

典型单级减速比为 50:1–160:1。关节内部集成无框力矩电机、驱动器、双绝对值编码器与可选电磁制动器，形成驱控一体结构。

输出扭矩与电机扭矩的关系为

$$
\tau_{\text{out}}=i\,\eta\,\tau_{\text{motor}},
$$

其中 $\eta$ 为传动效率。RHU 系列通过 FPGA 全硬件 FOC 算法实现高精度电流环与力矩环控制。

## 关键参数表

### 系列通用规格

| 参数 | 数值 / 说明 |
|---|---|
| 产品类型 | 人形专用谐波一体化关节模组 |
| 工作电压 | 24–48 V |
| 编码器 | 双绝对值，19 bit |
| 通信协议 | EtherCAT / CANopen |
| 工作噪音 | ＜60 dB |
| 工作温度 | -20–60 °C |
| 使用寿命 | ＞10,000 h |
| 安全功能 | STO 安全扭矩关闭 + 电磁制动（可选） |
| 大中空直径 | 最大 22 mm |

### RHU32H-120 示例参数

| 参数 | 数值 |
|---|---|
| 外形尺寸 | φ120 × 126 mm |
| 重量 | 4080 g（无制动）/ 4360 g（带制动） |
| 减速比 | 120 / 160 |
| 额定输出功率 | 216 W / 221 W |
| 2000 rpm 额定扭矩 | 124 N·m / 169 N·m |
| 输出端平均扭矩 | 197 N·m / 267 N·m |
| 输出端启停峰值扭矩 | 270 N·m / 459 N·m |
| 瞬时允许最大扭矩 | 848 N·m |

## 应用场景

- **人形机器人**：肩部、肘部、腕部、腰部、髋部、膝部、踝部旋转关节。
- **协作机械臂**：需要零背隙、高精度的关节模组。
- **高端移动平台**：轮足、外骨骼等需要高扭矩密度的场景。
- **服务机器人**：对噪音与体积敏感的关节应用。

## 供应链关系

- **上游**：谐波减速器（如绿的谐波等合作伙伴）、稀土永磁电机、磁性编码器/光学编码器、功率器件、铝合金壳体供应商。
- **同层**：意优科技作为一体化关节模组供应商，为多家头部人形机器人企业提供量产级关节，并提供端子式/甩线式标准接口。
- **下游**：人形机器人整机厂、协作机器人厂商、外骨骼与仿生机器人开发商。

## 来源与验证

- 意优 RHU 系列页：https://eyoubot.com/humanoid-harmonic-drive-robot-actuator
- RHU32H-120 参数页：https://eyoubot.com/products/rhu32h-120
- DoNews 报道：https://www.donews.com/news/detail/4/6391898.html
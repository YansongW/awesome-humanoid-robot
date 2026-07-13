---
id: ent_product_humanoid_robot_skin
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 人形机器人电子皮肤
  en: Humanoid Robot Electronic Skin
status: active
sources:
- id: src_ent_product_humanoid_robot_skin_1
  type: website
  url: https://www.hanwei.cn/product/cp101rxcgq/
- id: src_ent_product_humanoid_robot_skin_2
  type: website
  url: https://www.iit.it/documents/175012/591433/maggiali.pdf/7974b85f-5177-e162-97ed-8d9de658e273
- id: src_ent_product_humanoid_robot_skin_3
  type: website
  url: https://arxiv.org/html/2503.13048v1
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 人形机器人电子皮肤 / Humanoid Robot Electronic Skin

## 概述

人形机器人电子皮肤是一种覆盖机器人身体表面的大面积柔性触觉感知系统，能够测量压力、形状、温度、剪切力甚至形变，从而赋予机器人类似人类皮肤的接触感知能力。电子皮肤通常由分布式传感单元（taxels）、柔性基材、局部信号处理电路与通信网络组成，是人形机器人实现安全人机交互、精细抓取与全身力控的关键部件。当前商用与科研电子皮肤主要基于压阻、电容、压电、摩擦电、电阻抗断层成像（EIT）及神经形态等传感原理。

## 工作原理 / 技术架构

电子皮肤的核心是柔性力-电换能层。以压阻式为例，当外界压力 $F$ 作用于有效接触面积 $A$ 时，柔性导电复合材料产生形变，电阻 $R$ 发生变化：

$$
\frac{\Delta R}{R_0} = GF \cdot \varepsilon
$$

其中 $GF$ 为应变因子，$\varepsilon$ 为应变。通过测量电流或电压变化，可反演接触压力 $p = F/A$。电容式电子皮肤则利用极板间距 $d$ 随压力变化导致电容 $C \propto 1/d$ 变化的原理。EIT 电子皮肤通过在柔性介质边界注入电流并测量边界电压，重建内部电导率分布，从而同时感知接触力与弯曲形变。

分布式电子皮肤需在局部嵌入微控制器进行模数转换与预处理，再通过总线或无线方式将数据汇聚至中央控制器，以降低布线复杂度并提升可扩展性。

## 关键参数表

| 参数项 | 典型值/范围（以商用/科研代表产品为例） | 备注/来源 |
|--------|----------------------------------------|-----------|
| 传感原理 | 压阻式 / 电容式 / 压电式 / EIT / 神经形态 | 因方案而异 |
| 厚度 | ＜ 0.3 mm（汉威 CP101 柔性微压力传感器） | 汉威官网 |
| 传感点密度 | 约 100 个传感点/cm² | 汉威公开研报 |
| 压力测量范围 | 5 mN – 10 N（汉威 CP101） | 汉威官网 |
| 响应时间 | ＜ 100 ms（汉威 CP101）；科研方案可达 ＜ 1 ms | 汉威官网 / 研报 |
| 灵敏度 | 约 0.1 kPa（汉威柔性触觉传感器） | 公开研报 |
| 弯折寿命 | ＞ 100 万次 | 公开研报 |
| 工作温度 | 16 – 55 °C（汉威 CP101） | 汉威官网 |
| 工作湿度 | ＜ 80% RH | 汉威官网 |
| 单传感单元功耗 | 约 3 mW / 12 个传感单元（IIT 研究样机） | IIT 论文 |
| 传感单元尺寸 | 4 mm 直径（IIT 样机） | IIT 论文 |
| 空间分辨率 | 1.8 mm（部分科研压阻阵列） | 公开论文 |
| 价格 | 未公开 | 因方案与面积差异大 |

## 应用场景

- **人形机器人全身触觉**：覆盖手臂、躯干、手掌、指尖，检测意外碰撞并触发保护性反射。
- **灵巧手抓取控制**：实时感知接触力分布，实现鸡蛋、玻璃器皿等易碎物品的力控抓取。
- **人机协作安全**：识别人体接触位置与力度，降低协作机器人与人形机器人在共融环境中的碰撞风险。
- **医疗康复与假肢**：为假肢提供触觉反馈，或为康复机器人监测患者接触压力。
- **智能可穿戴**：健康监测、步态分析、压力分布评估。

## 供应链关系

- **核心传感单元/上游**：柔性压力传感器（如 `ent_component_hanwei_cp101`）、柔性基材（PI/PET/PDMS）、纳米导电材料、MEMS/ASIC 读出电路、封装材料、数据采集与通信模块。
- **系统集成商**：人形机器人整机厂、机器人灵巧手厂商、电子皮肤专业供应商。
- **下游客户/应用场景**：人形机器人、协作机器人、假肢与康复设备、智能可穿戴设备。
- **竞争/对标**：汉威科技、Tekscan、SynTouch、基于 IIT/iCub 电子皮肤的科研方案、国内外高校与初创企业。
- **知识图谱关系**：`ent_component_hanwei_cp101` — `used_in` → `ent_product_humanoid_robot_skin`；电子皮肤作为 `ent_product_humanoid_joint` 等人形机器人产品的外部感知层，常与力控关节协同工作。

## 来源与验证

1. [汉威科技 CP101 柔性微压力传感器官方产品页](https://www.hanwei.cn/product/cp101rxcgq/)
2. [IIT 博士论文：Large Area Tactile Sensor for Humanoid Robots（PDF）](https://www.iit.it/documents/175012/591433/maggiali.pdf/7974b85f-5177-e162-97ed-8d9de658e273)
3. [arXiv：Robot Skin with Touch and Bend Sensing using EIT](https://arxiv.org/html/2503.13048v1)
4. [附录 D 企业 Wiki：汉威科技](../../../appendices/appendix-d/companies/company_hanwei.md)

注：本实体为人形机器人电子皮肤的通用产品类别，表中参数综合了商用柔性压力传感器与科研样机的公开数据，具体电子皮肤系统参数应以集成商方案为准。
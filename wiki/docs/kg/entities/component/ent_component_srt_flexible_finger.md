---
id: ent_component_srt_flexible_finger
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: component
status: active
names:
  zh: SRT 柔性夹爪软体手指模块
  en: SRT Soft Gripper Finger Module
sources:
- id: src_srt_official
  type: website
- title: SRT 软体机器人官网
  url: https://www.softrobottech.com
- id: src_srt_sunya_tech
  type: website
- title: 舜若科技 SRT 软体机器人产品介绍
  url: https://www.sunya.biz/srtgripper.html
- id: src_srt_waibao_pdf
  type: website
- title: 软体机器人科技股份有限公司参展资料
  url: https://www.worldrobotconference.com/uploads/exfile/video/kjka9u.pdf
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Specifications from official product manuals, distributor pages and
    exhibition materials; missing values marked as 未公开.
---


# SRT 柔性夹爪软体手指模块 / SRT Soft Gripper Finger Module

## 概述

SRT 柔性夹爪软体手指模块（SRT Soft Gripper Finger Module）是北京软体机器人科技股份有限公司（SRT）开发的柔性末端执行器核心部件，采用食品级硅胶等柔性材料通过气动驱动实现自适应包覆抓取。与传统刚性夹爪不同，SRT 软体手指无需根据工件尺寸预先调整，即可抓取异形、易碎、柔软、不规则物体，广泛应用于食品生鲜、3C 电子、汽车零部件、医疗日化、物流仓储等领域。

## 工作原理 / 技术架构

SRT 软体手指基于仿生软体结构，核心机理为气动驱动的弹性变形：

1. **柔性气囊结构**：手指内部包含多个相互连通的气囊腔室，腔室壁厚呈非对称分布。
2. **正压抓取**：向气囊注入正压气体时，薄壁侧变形量大于厚壁侧，手指整体向目标物体弯曲并包覆其外表面，形成多点接触的自适应抓取。
3. **负压释放**：抽负压时手指张开，释放物体；在特定结构中亦可利用负压实现内撑抓取。
4. **材料非线性**：硅胶材料呈现超弹性，其应力-应变关系可用 Neo-Hookean 或 Mooney-Rivlin 本构模型近似描述，满足大变形、低刚度的柔顺接触需求。

抓取力 $F$ 与气压 $P$、接触面积 $A$ 及材料刚度 $k$ 的关系可近似表示为

$$
F \approx P \cdot A - k \cdot \delta
$$

其中 $\delta$ 为接触压缩量。通过调节气压可在较大范围内控制抓取力，避免损伤易碎工件。

## 关键参数表

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 制造商 | 软体机器人科技 / SRT | 官网 |
| 驱动方式 | 气动（正压抓取 / 负压释放） | 官网/经销商资料 |
| 手指材料 | 食品级硅胶 | 官网/经销商资料 |
| 工作温度 | -40 °C – 150 °C | 产品手册 |
| 工作压力 | -100 – 100 kPa | 产品手册 |
| 使用寿命 | >300 万次循环 | 产品手册 |
| 重复定位精度 | 0.08 mm | 产品手册 |
| 工作频率 | ≤110 CPM（约 300 次/分钟） | 产品手册 |
| 负载范围 | 100 g – 7 kg（因型号而异） | DirectIndustry |
| 夹爪重量 | 38 g – 1,090 g（因型号而异） | DirectIndustry |
| 适用工件 | 异形、易碎、柔软、不规则物体 | 官网公开资料 |
| 认证 | CE、RoHS、FDA、LFGB、JFSL370 等 | 官网公开资料 |
| 通信接口 | 气动控制器 + 机器人 I/O | 产品手册 |
| 价格 | 未公开 | - |

## 应用场景

- **食品生鲜分拣**：肉类、果蔬、烘焙食品的柔性抓取与包装码盘，满足食品接触材料认证。
- **3C 电子装配**：手机屏幕、边框、电路板等易损件的拾取与装配。
- **汽车零部件**：汽车软包电池、线束、塑料件的上下料。
- **医疗日化**：医疗耗材、化妆品瓶、化学器皿的安全搬运。
- **物流仓储**：异形包裹、 mixed-SKU 场景下的柔性抓取。

## 供应链关系

SRT（`ent_company_srt`）是全球领先的软体机器人技术与柔性末端执行器供应商，SRT 柔性夹爪软体手指模块（`ent_component_srt_flexible_finger`）作为其 SFG 系列柔性夹爪的核心零部件，通过 `uses` 关系装配于产品实体 SRT 柔性夹爪（`ent_product_srt_soft_gripper`）。SRT 的上游原材料包括食品级硅胶、气动元件、气动控制器、3D 视觉模组与工业机器人本体；下游客户覆盖食品生鲜、3C 电子、汽车零配件、医疗日化、物流仓储与协作机器人 OEM。SRT 与 OnRobot、Soft Robotics Inc.（美国）、Schmalz、Robotiq 等厂商形成竞争。

## 来源与验证

- SRT 官网与产品手册提供了工作压力、温度、寿命、重复精度等核心参数。
- 舜若科技等经销商页面转载了 SFG-FMA 系列的技术参数。
- 世界机器人大会参展资料详细介绍了 SRT 软体机器人的专利布局、产品系列与行业解决方案。
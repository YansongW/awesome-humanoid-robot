---
id: ent_component_xusheng_ev_motor_housing
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 旭升集团新能源汽车驱动电机壳体
  en: Xusheng EV Traction Motor Housing
status: active
sources:
- id: src_xusheng_official
  type: website
- title: 旭升集团官网
  url: https://www.xusheng.com
- id: src_xusheng_company_wiki
  type: document
- title: 附录 D 企业 Wiki - 旭升集团
  url: docs/appendices/appendix-d/companies/company_xusheng.md
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
  review_notes: Specifications extracted from company Wiki and public product literature;
    model-specific dimensions and price marked as 未公开.
---


# 旭升集团新能源汽车驱动电机壳体 / Xusheng EV Traction Motor Housing

## 概述

新能源汽车驱动电机壳体是旭升集团（Ningbo Xusheng Group）面向新能源动力总成开发的核心铝合金压铸结构件。它用于包覆和保护驱动电机定子、转子及冷却系统，同时提供散热通道、安装接口与密封界面。该产品采用高压压铸（HPDC）结合 CNC 精密加工制造，具有高导热、高气密性与尺寸稳定性，近年来也向人形机器人关节壳体等新兴领域延伸。

## 工作原理 / 技术架构

电机壳体既是结构件也是热管理部件。其内部通常集成水冷通道，冷却液在壳体流道内循环，带走定子绕组产生的热量。稳态热传导可近似用一维傅里叶定律描述：

\[
Q = \frac{k \cdot A \cdot \Delta T}{d}
\]

其中 \(Q\) 为热流量（W），\(k\) 为铝合金导热系数（约 150–200 W/(m·K)），\(A\) 为散热面积（m²），\(\Delta T\) 为壳体与冷却液温差（K），\(d\) 为等效壁厚（m）。

为满足气密性要求，压铸件需控制孔隙率并通过氦质谱或压降法检测，典型泄漏率指标为 ≤ 5 sccm（部分型号）。

## 关键参数

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 材质 | 铝合金 A380 / AlSi10MnMg | 产品手册 |
| 制造工艺 | 高压压铸 + CNC 精加工 + 热处理 | 产品手册 |
| 尺寸范围 | 依客户型号定制 | 产品手册 |
| 重量 | 5–40 kg（典型范围） | 产品手册 |
| 尺寸精度 | CT4–CT6 | 产品手册 |
| 气密性 | ≤ 5 sccm（部分型号） | 产品手册 |
| 抗拉强度 | 270–320 MPa（T7 热处理状态，参考同集团结构件） | 产品手册 |
| 表面处理 | 涂装 / 阳极氧化 / 钝化 | 产品手册 |
| 冷却方式 | 集成水冷通道 | 产品手册 |
| 典型应用电压 | 适配 400 V / 800 V 电驱平台 | 公开资料 |
| 具体型号尺寸 | 未公开 | — |
| 价格 | 未公开 | — |

## 应用场景

- **新能源汽车驱动电机**：为乘用车、商用车电驱系统提供电机定子安装、冷却与防护壳体。
- **混合动力变速箱**：用于 PHEV/HEV 混动专用变速箱的电机集成壳体。
- **人形机器人关节壳体**：依托铝合金压铸能力，向机器人关节、谐波减速器壳体等轻量化结构件延伸。

## 供应链关系

该电机壳体由 **旭升集团（实体 `ent_company_xusheng`）** 制造。上游依赖铝合金锭、镁合金锭、模具钢、压铸机、CNC 设备与热处理炉；下游客户包括特斯拉、蔚来、小鹏、理想、宁德时代及机器人整机厂。在知识图谱中，该实体通过 `manufactures` 关系与公司节点 `ent_company_xusheng` 相连，是旭升集团“三电系统壳体”产品线的代表零部件之一。

## 来源与验证

- 旭升集团官网（https://www.xusheng.com）
- 附录 D 企业 Wiki《旭升集团》（docs/appendices/appendix-d/companies/company_xusheng.md）

具体型号尺寸、单件价格与部分热性能参数在公开渠道未完整披露，已标注为“未公开”。
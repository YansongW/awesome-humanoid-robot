---
id: ent_product_zeiss_oinspect
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 蔡司 O-INSPECT 多传感器三坐标测量机
  en: ZEISS O-INSPECT Multisensor CMM
status: active
sources:
- id: src_zeiss_oinspect
  type: website
  url: https://www.zeiss.com/metrology/products/systems/optical-measurement/o-inspect.html
- id: src_zeiss_specs_pdf
  type: document
  url: https://www.tqscorp.com/wp-content/uploads/2026/01/O-Inspect-Machines-2025.pdf
- id: src_zeiss_iqs_portfolio
  type: document
  url: https://asset-downloads.zeiss.com/catalogs/download/iqs2/e2cd5220-0ac9-49da-b33f-3575b78e2e15/EN_60_025_ZEISS_IQS_PORTFOLIO_2026_web.pdf
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 蔡司 O-INSPECT 多传感器三坐标测量机 / ZEISS O-INSPECT Multisensor CMM

## 概述

ZEISS O-INSPECT 是卡尔·蔡司工业测量技术公司推出的多传感器坐标测量机，将接触式扫描、光学成像与白光共焦三种测量方式集成于同一平台。设备可在一次装夹中完成复杂几何体的三维尺寸、形位公差与表面形貌检测，型号包括 O-INSPECT 322、543 与 863。

## 工作原理 / 技术架构

O-INSPECT 采用花岗岩基座与空气轴承导向，三轴 CNC 运动由伺服电机驱动。接触式测量使用 ZEISS VAST XXT 扫描测头连续采集测点；光学测量采用 ZEISS Discovery.V12 变焦镜头，具有四倍于常规镜头的视野；敏感/反光表面可选用 ZEISS DotScan 白光共焦传感器进行非接触 topography 采集。所有数据由 ZEISS CALYPSO 软件统一处理，支持 CAD 模型比对与 PiWeb 报告输出。

长度测量精度通常以
\[
E_0 = a + \frac{L}{K}
\]
形式给出，其中 \(a\) 为固定误差项，\(L\) 为测量长度（mm），\(K\) 为与长度成比例的误差系数。O-INSPECT 543 的典型 3D 精度为 \(1.9 + L/250\) µm。

## 关键参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 型号 | O-INSPECT 322 / 543 / 863 | ZEISS |
| 测量范围 | 300×200×200 / 500×400×300 / 800×600×300 mm | ZEISS / OptiPro |
| 结构形式 | 柱式（322）/ 固定桥式（543/863） | ZEISS 规格书 |
| 传感器 | VAST XXT（接触）+ Discovery.V12（光学）+ DotScan（白光） | ZEISS |
| 3D 长度测量精度 | 1.9 + L/250 µm（典型） | Revelation Machinery / ZEISS |
| 软件 | ZEISS CALYPSO | ZEISS |
| 轴最大速度 | 300 mm/s（X/Y/Z） | ZEISS 规格书 |
| 轴加速度 | 500 mm/s² | ZEISS 规格书 |
| 最大工件重量 | 约 20 kg（依型号） | ZEISS |
| 工作温度 | 18–30 °C | ZEISS |
| 转台（选配） | 可编程旋转轴 | ZEISS |

## 应用场景

- 机器人零部件几何量检测与公差分析
- 医疗植入物（人工关节、牙科）精密测量
- 航空发动机叶片形貌检测
- 3C 结构件与注塑件全尺寸检测

## 供应链关系

卡尔·蔡司（`ent_company_zeiss`）为 O-INSPECT 的制造商。上游包括花岗岩、精密气浮导轨、光学镜头、测头传感器及测量软件；下游客户为汽车、航空航天、医疗与机器人行业的质量检测实验室。在知识图谱中，`ent_company_zeiss` 通过 `manufactures` 关系指向 `ent_product_zeiss_oinspect`。

## 来源与验证

- [ZEISS O-INSPECT Multisensor CMM](https://www.zeiss.com/metrology/products/systems/optical-measurement/o-inspect.html)
- [ZEISS O-INSPECT Specifications 2025](https://www.tqscorp.com/wp-content/uploads/2026/01/O-Inspect-Machines-2025.pdf)
- [ZEISS IQS Portfolio 2026](https://asset-downloads.zeiss.com/catalogs/download/iqs2/e2cd5220-0ac9-49da-b33f-3575b78e2e15/EN_60_025_ZEISS_IQS_PORTFOLIO_2026_web.pdf)
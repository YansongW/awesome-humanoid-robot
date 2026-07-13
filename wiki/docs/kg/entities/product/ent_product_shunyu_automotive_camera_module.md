---
id: ent_product_shunyu_automotive_camera_module
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 舜宇光学车载/机器人摄像头模组
  en: Sunny Optical Automotive / Robot Camera Module
status: active
sources:
- id: src_sunnyoptical_automotive
  type: website
  url: https://www.sunnyoptical.com/en/pro/009017006/index.html
- title: Automotive Imaging - Sunny Optical
- id: src_sunnyoptical_report
  type: report
  url: https://pdf.dfcfw.com/pdf/H3_AP202403111626210620_1.pdf
- title: 舜宇光学科技（02382.HK）深度报告 - 东方财富
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 舜宇光学车载/机器人摄像头模组 / Sunny Optical Automotive / Robot Camera Module

## 概述

舜宇光学科技（Sunny Optical Technology）是全球领先的光学成像与感知产品供应商，车载镜头全球市占率连续多年排名第一。公司车载/机器人摄像头模组覆盖前视、后视、环视、电子后视镜（CMS）及舱内监测（DMS/OMS）等应用，分辨率从 1.7 MP 到 8 MP 乃至 17 MP，适配 Mobileye、英伟达、高通、地平线等主流自动驾驶平台。

## 工作原理 / 技术架构

车载摄像头模组由光学镜头、图像传感器（CIS）、ISP、串行器与结构件组成。舜宇光学在镜头端采用玻塑混合非球面镜片与模芯镀膜技术，提升高温稳定性与成像清晰度；在模组端通过 AA（Active Alignment）主动对准、气密性封装与高低温可靠性测试，满足 AEC-Q100/Q102 等车规要求。

摄像头视场角（FOV）与焦距 $f$、传感器尺寸相关：

$$
\text{FOV} = 2 \arctan\left(\frac{d}{2f}\right)
$$

其中 $d$ 为传感器有效成像宽度。高像素模组（8 MP）相比 1.2 MP 模组可将车辆/行人/障碍物有效识别距离提升约 2 倍。

## 关键参数表

| 参数 | 典型范围/数值 |
|------|--------------|
| 应用领域 | 前视 ADAS、环视、后视、CMS、DMS/OMS、机器人视觉 |
| 分辨率 | 1.7 MP / 2 MP / 3 MP / 5 MP / 8 MP / 17 MP |
| 视场角 | 15°–120°（依镜头与用途） |
| 镜头类型 | 玻塑混合非球面、全玻璃 |
| 适用平台 | Mobileye、NVIDIA、Qualcomm、Horizon 等 |
| 最高自动驾驶等级 | L4（17 MP 前视镜头） |
| 车规认证 | AEC-Q 系列、IATF 16949 |
| 特色技术 | 模芯镀膜、主动除霜除雾、低温漂设计 |
| 全球车载镜头市占率 | 连续多年第一（公开报道） |

## 应用场景

- 乘用车与商用车 ADAS/自动驾驶感知
- 智能机器人视觉导航与避障
- 智能座舱驾驶员/乘客监测
- 电子后视镜与 360° 环视系统
- 工业检测与安防监控

## 供应链关系

舜宇光学位于车载/机器人视觉产业链中游偏上，上游采购光学玻璃、塑料粒子、CIS、ISP、SerDes 芯片与结构件；中游为镜头设计、模组组装与测试；下游面向 Tier-1 供应商、整车厂、机器人本体企业与安防厂商。舜宇与索尼、Valens 等企业在 MIPI A-PHY 等下一代接口技术上展开合作。

## 来源与验证

参数来源于舜宇光学官网车载成像页面（https://www.sunnyoptical.com/en/pro/009017006/index.html）及东方财富研报（https://pdf.dfcfw.com/pdf/H3_AP202403111626210620_1.pdf）。具体模组型号的光学参数以舜宇官方产品规格书为准，部分细节未公开。
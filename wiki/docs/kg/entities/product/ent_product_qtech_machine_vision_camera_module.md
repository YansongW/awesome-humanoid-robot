---
id: ent_product_qtech_machine_vision_camera_module
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 丘钛科技机器视觉/车载摄像头模组
  en: Q Technology Machine Vision & Automotive Camera Module
status: active
sources:
- id: src_qtech_2024_earnings
  type: website
  url: https://www.qtechsmartvision.com/ueditor/php/upload/file/20250325/1742864750138768.pdf
- title: 丘钛科技 2024 年度业绩投资者交流会议资料
- id: src_qtech_brand_maigoo
  type: website
  url: https://www.maigoo.com/brand/126034.html
- title: 丘钛科技 Q Tech 品牌介绍 - 买购网
- id: src_qtech_xueqiu
  type: website
  url: https://xueqiu.com/3077407437/371167883
- title: 丘钛科技摄像头模组和激光雷达在无人驾驶、机器人中的应用 - 雪球
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 丘钛科技机器视觉/车载摄像头模组 / Q Technology Machine Vision & Automotive Camera Module

## 概述

丘钛科技（集团）有限公司（Q Technology，港股代码：01478）是全球主要的摄像头模组封装测试企业之一，产品覆盖智能手机、车载、物联网与机器人四大场景。其机器视觉/车载摄像头模组面向自动驾驶、扫地机器人、人形机器人、AGV/AMR 与无人机，提供 2D 导航、3D ToF/dToF、双目融合、RGB-D 与车规级 ADAS 感知方案。

## 工作原理 / 技术架构

摄像头模组（CCM）由图像传感器、镜头、音圈马达（VCM）、ISP 芯片与柔性/印刷电路板组成，通过 COB（板上芯片）、COF、MOB、MOC 等封装工艺实现高像素、小型化与高可靠性。对于机器人视觉应用，丘钛提供全局曝光、宽视场角（FOV）与低畸变镜头，以满足 SLAM 与避障需求。

空间分辨率可用地面采样距离（GSD）近似：

\[
\text{GSD} = \frac{H \cdot p}{f}
\]

其中 \(H\) 为工作高度，\(p\) 为像素尺寸，\(f\) 为镜头焦距。ToF/dToF 方案则通过测量光脉冲飞行时间获取深度：

\[
d = \frac{c \cdot \Delta t}{2}
\]

其中 \(c\) 为光速，\(\Delta t\) 为发射与接收光脉冲的时间差。

## 关键参数表

| 参数 | 代表值/范围 |
|------|-------------|
| 像素覆盖 | 200 万–2 亿像素（全产品线） |
| 机器视觉导航模组 | 140° FOV，全量程 ≤1% 误差，低畸变 |
| 3D 感知方案 | 3D ToF / dToF / 双目融合 / RGB-D |
| 车载摄像头模组 | 800 万像素+，AEC-Q100，宽动态 |
| 封装技术 | COB、COF、MOB、MOC |
| 主要应用终端 | 智能手机、ADAS、扫地机器人、人形机器人、AGV/AMR、无人机 |

## 应用场景

- 自动驾驶前视/环视/舱内监控
- 人形机器人环境感知、目标识别与导航
- 扫地机器人/AMR 避障与路径规划
- 无人机航拍、避障与测绘
- 工业检测与机器视觉引导

## 供应链关系

丘钛科技模组整合上游镜头（投资新钜、poLight 等）、马达、图像传感器、ISP、驱动 IC 与线路板；中游为丘钛自有的 COB/COF/MOB/MOC 封装与光学设计能力；下游面向华为、小米、OPPO、vivo、三星、比亚迪、小鹏、蔚来、大疆、科沃斯、石头科技、追觅及人形机器人本体厂商。2024 年公司非手机摄像头模组出货量高速增长，车载与物联网成为新的增长曲线。

## 来源与验证

参数与业务描述来自丘钛科技 2024 年度业绩投资者交流资料、品牌介绍及雪球分析文章。具体模组型号的光学参数、接口定义与datasheet未在公开资料中披露，标注为“未公开”。
---
id: ent_component_percipio_fs820
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 图漾科技 FS820 工业 3D 相机
  en: Percipio FS820 Industrial 3D Camera
status: active
sources:
- id: src_percipio_fs820_official
  type: website
- title: Percipio F Series Product Page
  url: https://en.percipio.xyz/product-f-series/
- id: src_percipio_fs820_seeed
  type: website
- title: Percipio 3D Camera FS820 - Seeed Studio
  url: https://www.seeedstudio.com/Percipio-3D-Camera-FS820-p-4820.html
- id: src_percipio_fs820_rbtx
  type: website
- title: Percipio FS820 3D Camera - RBTX
  url: https://rbtx.tr/en-GB/components/vision-sensors/percipio-industrial-3d-camera-fm855-e1
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications compiled from Percipio product pages, Seeed Studio
    and RBTX distributor listings; missing values marked as 未公开.
---


# 图漾科技 FS820 工业 3D 相机 / Percipio FS820 Industrial 3D Camera

## 概述

Percipio FS820 是图漾科技（Percipio.XYZ）面向短距离、眼在手上（eye-in-hand）协作机器人场景开发的紧凑型工业 3D 相机。它基于主动双目结构光（active stereo structured-light）原理，集成红外结构光投射与双目深度感知，可在 0.3 m–1.3 m 工作范围内输出毫米级精度的深度图、RGB 图与点云。其机身小巧、功耗低，支持千兆以太网供电与硬触发，适用于抓取、装配、检测等柔性制造任务。

## 工作原理 / 技术架构

FS820 采用主动双目结构光深度感知架构。红外激光投射器向场景投射经过编码的结构光图案，两个红外相机从不同基线位置采集被物体表面调制的图像；通过立体匹配计算视差，并结合三角测量恢复每个像素的三维坐标。

在理想平行光轴双目模型中，深度 \(Z\) 与视差 \(d\) 的关系为：

\[
Z = \frac{f \cdot B}{d}
\]

其中 \(f\) 为相机焦距（像素单位），\(B\) 为双目基线长度，\(d\) 为同一空间点在两幅图像中的水平视差。基线越长，远距离精度越高，但近距离盲区越大；FS820 针对 0.3–1.3 m 的近距离场景优化了基线与焦距配置，以在紧凑体积内实现较高深度分辨率。

## 关键参数

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 深度技术 | 主动双目结构光 | Percipio 官方资料 |
| 工作距离 | 0.3 m – 1.3 m | Seeed Studio / RBTX |
| 深度分辨率 | 最高 1280 × 960 | 经销商 datasheet |
| RGB 分辨率 | 2 MP（约 1920 × 1080 或等效） | Seeed Studio |
| 帧率 | 5 fps @ 全深度分辨率 | Seeed Studio / RBTX |
| Z 向精度 | 约 ±2 mm @ 0.5 m | 第三方经销商（条件依赖） |
| FOV（H/V） | 未公开 | — |
| 基线 | 未公开 | — |
| 数据接口 | Gigabit Ethernet | 官方 datasheet |
| 供电 | PoE / DC（具体电压未公开） | — |
| 典型功耗 | 约 4 W | 机器视觉网经销商页 |
| 防护等级 | 最高 IP65 | 经销商资料 |
| 尺寸 | 约 125 mm × 85 mm × 30 mm（同系列 FM851 参考） | 未公开（FS820 单独尺寸） |
| 重量 | 约 228 g | RBTX 产品页 |
| 工作温度 | 0 °C – +45 °C（典型） | 经销商资料 |
| 价格 | 约 USD 749 | Seeed Studio |

## 应用场景

- **协作机器人眼在手上抓取**：利用小体积与轻重量直接安装于机械臂末端，实现近距离物体定位与抓取路径规划。
- **精密装配与检测**：在 0.3–1.3 m 范围内获取亚厘米级深度信息，用于间隙测量、缺陷检测与位姿估计。
- **医疗与服务机器人**：低功耗、小尺寸特性适合对载荷与空间敏感的医疗辅助机器人。

## 供应链关系

FS820 由 **图漾科技（Percipio.XYZ，实体 `ent_company_percipio`）** 设计与制造。上游依赖 CMOS 图像传感器、红外激光投射器、光学镜头、工业以太网芯片与结构光算法；下游面向协作机器人整机厂、工业自动化集成商与 3D 视觉解决方案商。在知识图谱中，该实体通过 `manufactures` 关系与公司节点 `ent_company_percipio` 相连，是 Percipio FS 系列短距 3D 相机的代表型号之一。

## 来源与验证

- Percipio 官方 F 系列产品页（https://en.percipio.xyz/product-f-series/）
- Seeed Studio FS820 商品页（https://www.seeedstudio.com/Percipio-3D-Camera-FS820-p-4820.html）
- RBTX 经销商产品页（https://rbtx.tr/en-GB/components/vision-sensors/percipio-industrial-3d-camera-fm855-e1）

部分参数（如精确 FOV、基线、单独尺寸、供电细节）在公开渠道未完整披露，已标注为“未公开”。
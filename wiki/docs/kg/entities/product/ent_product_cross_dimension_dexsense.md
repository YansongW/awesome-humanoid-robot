---
id: ent_product_cross_dimension_dexsense
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 跨维智能 DexSense 纯视觉空间智能传感器
  en: Cross-Dimension DexSense Vision Sensor
status: active
sources:
- id: src_dexforce_official
  type: website
  url: https://www.dexforce.com/
- title: 跨维智能官网
- id: src_dexforce_about
  type: website
  url: https://dexforce.com/about.html
- title: 跨维智能公司介绍
- id: src_dexforce_w1_pro_donews
  type: article
  url: https://www.donews.com/news/detail/1/5761824.html
- title: 跨维智能发布第二代人形机器人 DexForce W1 Pro
- id: src_dexforce_w1_ithome
  type: article
  url: https://www.ithome.com/0/826/024.htm
- title: 跨维科技发布 DexForce W1 具身机器人
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 跨维智能 DexSense / Cross-Dimension DexSense

## 概述

DexSense 是跨维（深圳）智能数字科技有限公司自研的纯视觉空间与具身智能传感器，属于跨维“EmbodiChain”具身智能产品矩阵中的核心感知部件。该传感器采用多图像传感器模块化设计，搭载跨维自研成像与感知算法，可在强光直射、阴影、低光照等复杂光照条件下实时输出稠密点云与深度图，为 DexForce W1 / W1 Pro 人形机器人提供仿人双眼级别的三维感知能力。

## 工作原理 / 技术架构

DexSense 基于双目立体视觉与深度学习三维重建：

1. **多相机模组**：头部主传感器为仿人双目纯视觉模组，腕部配备近距离操作相机，底盘集成前后深度相机，形成全域感知网络。
2. **立体匹配**：通过标定后的双相机图像计算视差 $d$，结合基线 $b$ 与焦距 $f$ 估计深度

$$
   Z=\frac{b\,f}{d}.
   $$

3. **通用感知大模型**：利用 3D VLA（3D Vision-Language-Action）大模型对场景进行语义与几何联合理解。
4. **Sim2Real 数据闭环**：在跨维 DexVerse™ 引擎中生成合成数据，提升模型在真实复杂光照下的泛化能力。

W1 Pro 头部双目传感器的视场覆盖可用近似公式估算：

$$
W=2Z\tan\frac{\alpha_h}{2},\quad H=2Z\tan\frac{\alpha_v}{2},
$$

其中 $\alpha_h=90^\circ$、$\alpha_v=60^\circ$ 分别为水平与垂直视场角，$Z$ 为观测距离。

## 关键参数表

| 参数 | 数值 / 说明 |
|---|---|
| 传感器类型 | 纯视觉双目空间智能传感器 |
| 头部主视场角 | 90°（H）× 60°（V） |
| 帧率 | 60 Hz |
| 双目标定误差 | ≤ ±0.05 像素 |
| 立体匹配精度 | ≤ 0.1 像素（亚像素级） |
| 三维轮廓还原误差 | ≤ 1 mm |
| 双目拍照同步 | ≤ 20 μs |
| 功耗 | 约为初代 1/3 |
| 腕部操作相机 FOV / 工作距离 | 87°×58° / 7–50 cm |
| 底盘深度相机量程 | 0.2–2.5 m |
| 算法能力 | 强光、阴影、低光照自适应 |

## 应用场景

- **人形机器人头部感知**：为 DexForce W1/W1 Pro 提供环境三维重建与语义理解。
- **腕部精细操作视觉**：近距离抓取、插孔、装配等亚毫米级任务。
- **底盘导航避障**：前后深度相机支撑 SLAM 与动态障碍物检测。
- **工业与家庭服务**：智能制造、家庭助理、科研教育中的通用视觉前端。

## 供应链关系

- **上游**：图像传感器、光学镜头、ISP/计算芯片、结构件供应商。
- **同层**：DexSense 作为跨维智能自研感知模块，集成于 DexForce W1/W1 Pro 整机，并通过 EmbodiChain 平台向开发者开放。
- **下游**：人形机器人整机厂商、具身智能算法开发者、工业/服务场景集成商。

## 来源与验证

- 跨维智能官网：https://www.dexforce.com/
- 跨维智能公司介绍：https://dexforce.com/about.html
- DoNews DexForce W1 Pro 报道：https://www.donews.com/news/detail/1/5761824.html
- IT之家 DexForce W1 报道：https://www.ithome.com/0/826/024.htm
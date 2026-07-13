---
id: ent_product_ofilm_tof_3d_module
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 欧菲光 3D ToF 深度相机模组
  en: OFILM 3D ToF Depth Camera Module
status: active
sources:
- id: src_ofilm_head_perception_news
  type: article
  url: http://www.ofilm.com/news1_inner_273.html
- title: 欧菲光推出人形机器人视觉感知产品架构组合方案
- id: src_ofilm_product_page
  type: website
  url: http://www.ofilm.com/en/products_inner1_39.html
- title: OFILM Product Page
- id: src_3disf_jd400_tof
  type: article
  url: http://mp.weixin.qq.com/s?__biz=MzI2Nzg4NjA5OQ==&mid=2247566803&idx=2&sn=07e27c3b81c258c332df668406b7e84b
- title: JD-400 iToF 3D 相机产品介绍
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 欧菲光 3D ToF 深度相机模组 / OFILM 3D ToF Depth Camera Module

## 概述

欧菲光 3D ToF 深度相机模组是欧菲光面向人形机器人、智能终端与工业视觉推出的三维感知模组。该模组基于间接/脉冲 Time-of-Flight（iToF/pToF）技术，通过调制红外光相位测距，可实时输出高分辨率深度图与点云。欧菲光将其集成到“头部视觉感知系统”与“腕部视觉感知系统”中，用于实现人形机器人全方位环境感知与近距离高精度抓取测距。

## 工作原理 / 技术架构

ToF 深度测量的物理基础为光飞行时间。对于间接 ToF，发射端向场景投射调制频率为 $f_m$ 的近红外光，接收端测量反射光相对于发射光的相位延迟 $\phi$，则目标距离

$$
d=\frac{c\,\phi}{4\pi f_m},
$$

其中 $c$ 为光速。多频调制可扩展非模糊距离并抑制多径干扰。欧菲光方案将 ToF 深度相机与 RGB 相机、IMU 融合，形成 RGB-D 感知流；在腕部方案中通过 AI 补全算法将原生 640×480 深度图超分至 1280×960，以提升微小物体轮廓的捕捉能力。

## 关键参数表

| 参数 | 数值 / 说明 |
|---|---|
| 技术路线 | 3D ToF（间接/脉冲） |
| 典型波长 | 940 nm |
| ToF 原生分辨率 | 640×480 |
| AI 超分输出 | 1280×960 |
| 腕部量程 | 0.07–1 m |
| 腕部测距精度 | 0.07–0.5 m：＜3 mm；0.5–1 m：＜1% |
| 帧率 | 30 fps |
| 腕部模组尺寸 | 45×28×30.5 mm |
| 接口 | USB / GMSL |
| 头部系统 | 集成 5 颗 RGB + 1 颗 ToF + IMU + AI 补全 |
| 曝光模式 | RGB 全局曝光（避免运动畸变） |

## 应用场景

- **人形机器人头部**：全方位环视、障碍物检测、SLAM 定位与场景理解。
- **腕部精细操作**：抓取前物体位姿估计、插孔/装配距离测量。
- **工业检测**：非接触式尺寸测量、缺陷检测、栈板识别。
- **消费电子与康养**：手势识别、跌倒检测、人机交互。

## 供应链关系

- **上游**：VCSEL/红外光源、ToF 图像传感器、光学镜头、滤光片、ISP 芯片、PCB 与结构件供应商。
- **同层**：欧菲光作为模组集成商，将 ToF 深度相机与 RGB、IMU、AI 算法打包为头部/腕部感知子系统。
- **下游**：人形机器人整机厂、智能手机/AR 设备厂商、工业视觉集成商。

## 来源与验证

- 欧菲光人形机器人视觉感知方案新闻：http://www.ofilm.com/news1_inner_273.html
- 欧菲光产品页：http://www.ofilm.com/en/products_inner1_39.html
- iToF 相机技术参考：http://mp.weixin.qq.com/s?__biz=MzI2Nzg4NjA5OQ==&mid=2247566803&idx=2&sn=07e27c3b81c258c332df668406b7e84b
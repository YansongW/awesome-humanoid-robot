---
id: ent_product_aubo_amr
schema_version: 1
type: product
domain: 04_assembly_integration_testing
theoretical_depth: system
names:
  zh: 遨博 AUBO-AMR300 海纳复合机器人
  en: AUBO-AMR300 Haina Mobile Manipulator
status: active
sources:
- id: src_aubo_amr300_wrc
  type: website
  url: https://www.worldrobotconference.com/news/latestnews/1876.html
- title: 【WRC展商推介】遨博（北京）智能科技股份有限公司
- id: src_aubo_haina_official
  type: website
  url: https://www.aubo-robotics.cn/products/th
- title: 海纳系列移动式协作机器人 - 遨博智能官网
- id: src_aubo_i5_specs
  type: website
  url: https://www.zjaubo.com/products/7.html
- title: AUBO-i5 协作机器人 - 浙江遨博机器人有限公司
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-13
---


# 遨博 AUBO-AMR300 海纳复合机器人 / AUBO-AMR300 Haina Mobile Manipulator

## 概述

遨博 AUBO-AMR300 是遨博智能基于“海纳”复合机器人操作平台推出的移动式协作机器人，将协作机械臂、自主移动机器人（AMR）、2D/3D 视觉与末端夹爪集成于一体，实现“手、眼、脚”协同作业。该产品面向工业、农业、建筑、港口、电力、航空航天及生物医药等领域，提供一站式移动操作解决方案。

## 工作原理 / 技术架构

AUBO-AMR300 由移动底盘、协作机械臂、视觉系统与末端执行器组成，所有子系统通过遨博海纳多合一控制系统统一调度。底盘采用双轮差速驱动，运动学模型为

\[
v = \frac{v_R + v_L}{2}, \quad \omega = \frac{v_R - v_L}{L}
\]

其中 \(v_R\)、\(v_L\) 为左右轮线速度，\(L\) 为轮距，\(v\) 与 \(\omega\) 分别为底盘线速度与角速度。导航采用高精度 SLAM 激光雷达实现地图构建与自主定位；机械臂末端通过 2D/3D 视觉引导完成目标识别与抓取，视觉重复定位精度达 \(\pm 1\,\text{mm}\)。

## 关键参数表

| 参数 | 数值 |
|------|------|
| 外形尺寸（长×宽×高，不含机械臂） | \(1000 \times 700 \times 600\,\text{mm}\) |
| 自重（不含机械臂） | 250 kg |
| 负载表面尺寸 | \(650 \times 620\,\text{mm}\) |
| 最大载重（含机械臂与载具） | 300 kg |
| 移动定位精度 | \(\pm 10\,\text{mm}\) |
| 3D 视觉重复定位精度 | \(\pm 1\,\text{mm}\) |
| 续航时间 | 6–8 h |
| 驱动方式 | 双轮差速 |
| 标配协作臂 | AUBO-i5（6 轴，负载 5 kg，工作半径 886.5 mm） |
| 控制架构 | 遨博海纳多合一控制系统 |

## 应用场景

- 工厂物料搬运与产线上下料
- 仓储物流中的移动拣选与托盘搬运
- 3C、汽车零部件装配与检测
- 电力/航空航天领域的巡检与维护
- 生物医药洁净室内的样本转运

## 供应链关系

AUBO-AMR300 由遨博（北京）智能科技股份有限公司研发制造。上游包括伺服电机、减速器、激光雷达、视觉相机、电池及结构件；中游为遨博自研的协作机器人、控制器与海纳操作系统；下游通过系统集成商交付给制造、物流与特种行业用户。遨博同时提供 i 系列协作机器人与视觉、夹爪等生态配件。

## 来源与验证

参数主要来自世界机器人大会展商推介页面及遨博官网。底盘最大行驶速度、电池容量、充电时间、机械臂最大末端速度等细节未在公开资料中披露，标注为“未公开”。
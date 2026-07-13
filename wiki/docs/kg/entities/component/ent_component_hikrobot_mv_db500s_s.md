---
id: ent_component_hikrobot_mv_db500s_s
schema_version: 1
type: component
domain: 02_components
theoretical_depth: system
names:
  zh: 海康机器人 MV-DB500S-S RGB-D 智能立体相机
  en: Hikrobot MV-DB500S-S RGB-D Smart Stereo Camera
status: active
sources:
- id: src_hikrobot_mv_db500s_s_spec
  type: website
- title: HIKROBOT MV-DB500S-S RGBD智能立体相机
  url: http://ljopt.com/product/6503.html
- id: src_hikrobot_logistics_vision
  type: document
- title: Hikrobot Logistic Vision Solutions Catalog
  url: https://www.maxxvision.com/downloads/Kataloge/Hikrobot/Hikrobot_Logistic_Vision_Solutions.pdf
- id: src_hikrobot_ztec
  type: website
- title: Hikrobot MV-DB500S – RGB-D smart camera
  url: https://www.ztec.dk/shop/hikrobot-mv-db500s-mv-db500s-42197
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications compiled from Hikrobot distributor listings and product
    catalog; exact sensor model and optical parameters are not fully public.
---


# 海康机器人 MV-DB500S-S RGB-D 智能立体相机 / Hikrobot MV-DB500S-S RGB-D Smart Stereo Camera

## 概述

MV-DB500S-S 是海康机器人（Hikrobot）推出的 RGB-D 智能立体相机，定位于物流单件分离（singulation）场景。它采用单 DOE 散斑结构光立体视觉方案，集成彩色相机与深度感知模块，可在 500 mm 净距离、1500 mm 测量范围内输出深度图、RGB 图与物体位姿信息。相机内置深度学习实例分割算法，支持千兆以太网供电与多相机标定，防护等级 IP65，适用于快递分拣、包裹抓取与自动化上下料。

## 工作原理 / 技术架构

MV-DB500S-S 基于主动结构光双目立体视觉。红外激光模块通过 DOE（Diffractive Optical Element）投射高密度散斑图案，左右红外相机采集被测物体表面的散斑图像；通过立体匹配计算视差图，再依据三角测量恢复三维坐标。RGB 相机同步采集彩色图像，实现深度与彩色的像素级对齐输出。

深度计算遵循双目三角测量公式：

\[
Z = \frac{f \cdot B}{d}
\]

其中 \(f\) 为相机焦距（像素单位），\(B\) 为双目基线，\(d\) 为匹配视差。在 1 m 距离处，该型号标称深度检测精度为 XY/Z 方向 5 mm；在 2 m 距离处约为 10 mm。精度随距离增大而下降，符合 \(\Delta Z \propto Z^2\) 的近似规律。

内置 AI 加速模块运行实例分割网络，对包裹进行像素级分割并输出抓取点或位姿，降低上位机计算负担。

## 关键参数

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 深度技术 | 单 DOE 散斑结构光立体视觉 | 产品目录 |
| 近视场 | 580 mm × 470 mm | 产品目录 / 经销商 |
| 远视场 | 2,500 mm × 1,800 mm | 经销商（S 型号） |
| 净距离（CD） | 500 mm | 产品目录 |
| 测量范围（MR） | 1,500 mm | 产品目录 |
| 物体检测范围 | 50 mm × 50 mm × 10 mm – 1,000 mm × 1,000 mm × 1,000 mm | 经销商 |
| 深度图检测精度 | X,Y: 5 mm @ 1 m；10 mm @ 2 m；Z: 4 mm @ 1 m；8 mm @ 2 m（部分经销商） | 产品目录 / 经销商 |
| 彩色图检测精度 | X,Y: 2.6 mm @ 1 m；5.5 mm @ 2 m | 产品目录 |
| 扫描帧率 | 25 fps @ 单件分离模式（部分资料称 30 fps） | 经销商 |
| 分辨率 | Depth: 1,408 × 1,024；RGB: 1,536 × 1,280（典型） | 经销商 |
| 数据类型 | 原始图（黑白+彩色）、深度图、物体位姿信息 | 经销商 |
| 激光安全等级 | Class 1 | 产品目录 |
| 数据接口 | Gigabit Ethernet（1,000 Mbit/s） | 产品目录 |
| 数字 I/O | 12-pin M12，3 路光耦隔离输入 / 3 路光耦隔离输出 | 产品目录 |
| 供电 | 12–24 VDC | 产品目录 |
| 典型功耗 | 5.5 W @ 24 VDC（S 型号）；标准型号 < 9 W | 经销商 |
| 尺寸 | 200 mm × 47 mm × 100 mm（标准）；184 mm × 55 mm × 53 mm（部分 S 型号） | 产品目录 / 经销商 |
| 重量 | 约 1 kg（标准）；约 700 g（部分 S 型号） | 经销商 |
| 防护等级 | IP65 | 产品目录 |
| 工作温度 | 0 °C – +45 °C | 产品目录 |
| 存储温度 | −30 °C – +80 °C | 产品目录 |
| 配套软件 | 海康单件分离控制系统 / HiViewer | 经销商 |
| 认证 | CE, RoHS, KC | 产品目录 |

## 应用场景

- **快递单件分离**：在物流分拣线上识别并分离堆叠包裹，为后续扫码、称重与分拣提供位姿。
- **机器人包裹抓取**：输出物体位姿与抓取点，引导机械臂完成自动化上下料。
- **体积测量与仓储管理**：结合深度图与实例分割，实现包裹体积估算与库存盘点。

## 供应链关系

MV-DB500S-S 由 **海康机器人（Hikrobot，实体 `ent_company_hikrobot`）** 设计与制造，母公司为海康威视。上游依赖 CMOS 图像传感器、ISP 芯片、DOE 激光器、光学镜头、主控 SoC 与电机驱动；下游客户包括 3C/半导体制造、汽车、锂电、物流仓储、AMR/AGV 与人形机器人感知模组厂商。在知识图谱中，该实体通过 `manufactures` 关系与公司节点 `ent_company_hikrobot` 相连，是海康机器人 MV-DB 系列 RGB-D 相机的单件分离专用型号。

## 来源与验证

- HIKROBOT MV-DB500S-S 经销商规格页（http://ljopt.com/product/6503.html）
- Hikrobot Logistic Vision Solutions 产品目录（https://www.maxxvision.com/downloads/Kataloge/Hikrobot/Hikrobot_Logistic_Vision_Solutions.pdf）
- ZTEC 经销商产品页（https://www.ztec.dk/shop/hikrobot-mv-db500s-mv-db500s-42197）

部分参数（如精确传感器型号、基线长度、深度传感器分辨率细节）在公开渠道未完整披露，不同经销商对 S 型号的帧率与功耗描述存在差异，已在备注中说明。
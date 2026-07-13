---
id: ent_product_slamtec_mapper
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 思岚科技 SLAMTEC Mapper 激光建图雷达
  en: SLAMTEC Mapper Laser Mapping Radar
status: active
sources:
- id: src_ent_product_slamtec_mapper_website
  type: website
  url: https://www.slamtec.com/cn/lidar/mapper
- id: src_ent_product_slamtec_mapper_datasheet
  type: document
  url: https://img.iceasy.com/product/product/files/202210/8a8a8a1a8362bd080183eb9b955c3a8d.pdf
- id: src_ent_product_slamtec_mapper_wiki
  type: website
  url: docs/appendices/appendix-d/companies/company_slamtec.md
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 思岚科技 SLAMTEC Mapper 激光建图雷达 / SLAMTEC Mapper Laser Mapping Radar

## 概述

SLAMTEC Mapper 是上海思岚科技（SLAMTEC）推出的集成式激光建图与定位传感器。该产品将 360° 二维激光雷达与第三代高性能 SLAM 图优化引擎（SharpEdge™ 精细化建图技术）融合于一体，内置 9 自由度惯性导航系统，只需 5 V DC 供电即可独立工作，无需外部里程计或额外计算单元，可直接输出实时激光扫描数据、地图数据以及机器人位姿（x, y, θ），广泛应用于机器人导航定位、环境测绘、建筑工程及手持测量。

## 工作原理与技术架构

SLAMTEC Mapper 的测距核心通过调制红外激光进行三角测距或 TOF 测距，并以固定频率 360° 旋转扫描。传感器每秒进行多次测距采样，将扫描数据送入内置处理单元运行 SLAM 算法：

- **前端里程计**：通过连续两帧激光扫描的配准估计局部运动。
- **后端图优化**：构建位姿图并检测闭环，修正累积误差。
- **IMU 融合**：内置 9-DOF IMU 提供倾斜补偿与运动速度约束，支持手持建图模式。

建图分辨率（地图栅格尺寸）为：

$$
\Delta s = 0.05\ \text{m}
$$

即每个像素代表 0.05 m × 0.05 m 的区域。在理想实验室环境下，重复定位精度为：

$$
\epsilon_{\text{repeat}} < 0.02\ \text{m}
$$

输出数据刷新频率为 10 Hz，可通过 SLAMWARE SDK 或 ROS Node 获取。

## 关键参数表

| 参数项 | 数值/范围 | 备注 |
|--------|-----------|------|
| 产品形态 | 集成激光雷达 + SLAM 处理单元 | 上电即用 |
| 扫描方式 | 360° 二维激光扫描 | — |
| 测距范围 | 40 m（92% 反射率） | M2M2 型号 |
| 采样频率 | 9200 Hz | M2M2 |
| 扫描频率 | 10 Hz | — |
| 数据刷新频率 | 10 Hz | — |
| 建图分辨率 | 0.05 m | — |
| 最大建图面积 | 300 m × 300 m | M2M2 |
| 重复定位精度 | <0.02 m | 理想实验室环境 |
| 最大移动速度 | 2 m/s | — |
| 最大倾斜角度 | ±3° | 建议保持水平 |
| 激光波长 | 895–915 nm | 红外 |
| 激光峰值功率 | 28 W | 脉冲 |
| 脉冲宽度 | 10 ns | — |
| 脉冲占空比 | 0.0092% | — |
| 激光安全等级 | IEC-60825 Class 1 | 人眼安全 |
| 供电 | 5 V DC | USB 或 DC 插座 |
| 通信接口 | WiFi / 100 M 以太网 | 内置 AP/Station |
| 惯性导航 | 9-DOF IMU | 内置 |
| 尺寸/重量 | 未公开 | 官方未披露 |
| 价格 | 未公开 | 需询价 |

## 应用场景

- **机器人导航定位**：服务机器人、AMR、无人车的 SLAM 与定位。
- **环境测绘与建筑**：手持或车载建图、室内平面图生成。
- **巡检机器人**：长走廊、复杂室内场景的地图构建与位姿跟踪。
- **人形机器人**：为双足机器人提供 2D 激光 SLAM 输入，支持自主行走与避障。

## 供应链关系

- **制造商**：`ent_company_slamtec`（上海思岚科技有限公司）。
- **上游关键物料**：激光发射器、光电探测器、无刷电机、光学透镜、FPGA/SoC、9-DOF IMU、结构件。
- **下游客户**：服务机器人厂商、AMR/OEM、测绘设备商、高校与研究机构。
- **知识图谱关系**：
  - `ent_company_slamtec` — `manufactures` → `ent_product_slamtec_mapper`
  - `ent_product_slamtec_mapper` — `provides` → 机器人 SLAM/导航子系统节点

## 来源与验证

- 思岚科技官方 SLAMTEC Mapper 页面说明了集成 SLAM 引擎、SharpEdge 建图、9-DOF IMU、5 V 供电、WiFi/以太网、2 m/s 移动速度、室内外可用等核心特性。
- SLAMTEC Mapper 数据表（型号 M2M2）公开了 40 m 测距、9200 Hz 采样、10 Hz 扫描/刷新、0.05 m 建图分辨率、300×300 m 最大建图面积、<0.02 m 重复定位精度、激光波长/功率/安全等级、通信接口等完整参数。
- 附录 D Wiki《思岚科技 / SLAMTEC》词条确认了 SLAMTEC Mapper 的产品定位与应用场景。
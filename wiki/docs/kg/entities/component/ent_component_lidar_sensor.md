---
id: ent_component_lidar_sensor
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 激光雷达传感器
  en: LiDAR Sensor
status: active
sources:
- id: src_ent_component_lidar_sensor_1
  type: website
  url: https://www.hesaitech.com/wp-content/uploads/2025/04/XT32M2X_User_Manual_X03-en-250310.pdf
- id: src_ent_component_lidar_sensor_2
  type: website
  url: https://visimind.com/products/hesai/
- id: src_ent_component_lidar_sensor_3
  type: website
  url: https://www.indiamart.com/proddetail/hesai-pandar-128-lidar-sensor-2858282556512.html
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 激光雷达传感器 / LiDAR Sensor

## 概述

激光雷达（LiDAR，Light Detection and Ranging）传感器是一种主动式光学测距传感器，通过发射激光束并接收回波来测量目标距离，进而构建三维点云。按测距原理可分为飞行时间（Time-of-Flight, ToF）与三角测距两类；按扫描方式可分为机械旋转式、半固态（MEMS/转镜）和固态（Flash/OPA）。本实体为机器人产业链中的通用零部件类别，典型代表包括禾赛 XT 系列、Pandar 系列及思岚 RPLIDAR 系列等。

## 工作原理 / 技术架构

ToF 激光雷达通过测量激光脉冲往返时间 $\Delta t$ 计算目标距离：

$$
d = \frac{c \Delta t}{2}
$$

其中 $c$ 为光速。对于多线机械旋转雷达，水平角分辨率 $\theta_H$、垂直角分辨率 $\theta_V$、线数 $N$ 与帧率 $f$ 共同决定点云密度。单帧点云数可近似为

$$
N_{\text{points}} \approx \frac{360°}{\theta_H} \cdot N
$$

而点频 $P$ 为 $N_{\text{points}} \cdot f$。三角测距雷达则通过基线长度 $b$ 与反射光斑成像位置的几何关系解算距离，适用于中短距、低成本场景。

## 关键参数表

| 参数项 | 典型值/范围（以市场主流机器旋转/半固态产品为例） | 备注/来源 |
|--------|--------------------------------------------------|-----------|
| 测距原理 | 飞行时间（ToF）/ 三角测距 | 因型号而异 |
| 测距范围 | 0.05 – 300 m（型号相关） | Hesai XT32M2X |
| 测距精度 | ±1 cm（典型值） | Hesai XT 系列 |
| 测距分辨率 | 0.5 cm（1σ，典型） | Hesai XT32M2X |
| 水平视场角 | 360°（机械旋转）/ 120°（前向固态） | 因型号而异 |
| 垂直视场角 | 31° – 40.3°（多线旋转）/ 25°（前向固态） | 因型号而异 |
| 水平角分辨率 | 0.09° – 0.36°（5–20 Hz 可调） | Hesai XT32M2X |
| 垂直角分辨率 | 1.3° – 2°（多线产品） | Hesai XT 系列 |
| 扫描频率 | 5 – 20 Hz | Hesai XT 系列 |
| 点频 | 最高 6,912,000 pts/s（双回波） | Hesai Pandar 128 |
| 激光波长 | 905 nm / 1550 nm（视型号） | Hesai XT 系列为 905 nm |
| 激光安全等级 | Class 1（人眼安全） | Hesai XT 系列 |
| 功耗 | 9 – 29 W（视型号） | Hesai XT/OT 系列 |
| 重量 | 190 g – 2.3 kg（视型号） | 公开 datasheet |
| 通信接口 | Ethernet / UDP / TCP / TTL UART（视型号） | 公开 datasheet |
| 价格 | 未公开 | 因型号与批量差异大 |

## 应用场景

- **人形机器人环境感知**：建图、定位与避障，辅助行走与操作。
- **服务机器人导航**：SLAM、路径规划、动态障碍物检测。
- **自动驾驶与无人车**：高精度三维环境感知、车道线检测、小目标识别。
- **测绘与数字孪生**：移动测量、无人机航测、工业设施三维重建。

## 供应链关系

- **核心零部件/技术来源**：激光发射器（VCSEL/EEL/光纤激光器）、光电探测器（APD/SPAD/SiPM）、扫描机构（电机/MEMS/转镜）、光学透镜、FPGA/ASIC 信号处理芯片、PCB、结构件。
- **主要制造商/品牌**：禾赛科技、速腾聚创、华为、大疆 Livox、思岚科技、Velodyne、Ouster、Luminar。
- **下游客户/应用场景**：机器人整机厂、自动驾驶方案商、测绘公司、工业巡检、安防监控。
- **知识图谱关系**：本实体为通用零部件类别；`ent_component_slamtec_rplidar_a3` 是其具体产品实例之一；`ent_product_megvii_logistics_robot` 等物流机器人可能 `uses` → `ent_component_lidar_sensor`。

## 来源与验证

1. [Hesai XT32M2X User Manual（官方 PDF）](https://www.hesaitech.com/wp-content/uploads/2025/04/XT32M2X_User_Manual_X03-en-250310.pdf)
2. [Visimind：Hesai XT16 / XT32 / XT32M 规格汇总](https://visimind.com/products/hesai/)
3. [IndiaMART：Hesai Pandar 128 产品信息](https://www.indiamart.com/proddetail/hesai-pandar-128-lidar-sensor-2858282556512.html)

注：本实体为通用零部件节点，表中参数为市场主流产品的代表性范围，具体型号参数应以对应制造商 datasheet 为准。
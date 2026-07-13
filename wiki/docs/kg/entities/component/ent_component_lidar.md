---
id: ent_component_lidar
schema_version: 1
type: component
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: 激光雷达
  en: LiDAR
status: active
sources:
- id: src_hesai_xt32m2x_manual
  type: website
  url: https://www.hesaitech.com/wp-content/uploads/2025/04/XT32M2X_User_Manual_X03-en-250310.pdf
- id: src_velodyne_vlp16_datasheet
  type: website
  url: https://navysbir.com/n23_2/N232-080-VLP16.pdf
- id: src_geoweeknews_navvis_vlx3
  type: website
  url: https://www.geoweeknews.com/articles/navvis-partners-with-hesai-for-its-new-vlx3-system/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# 激光雷达 / LiDAR

## 概述

激光雷达（Light Detection and Ranging，LiDAR）是一种通过发射激光脉冲并接收回波来测量目标距离、方位与反射强度的主动式光学传感器。按扫描方式可分为机械旋转式、混合固态（MEMS）与纯固态（OPA/Flash）三大类。作为通用技术类别节点，以下关键参数以主流机械旋转式产品 Hesai XT32M2X 与 Velodyne VLP-16 为代表值进行说明。

## 工作原理 / 技术架构

机械旋转式 LiDAR 利用电机带动激光发射/接收模块绕垂直轴旋转，形成 360° 水平视场；多个激光器按不同俯仰角排布，构成垂直视场。测距基于脉冲飞行时间（Time of Flight, ToF）：

$$
d = \frac{c \, \Delta t}{2}
$$

其中 $c \approx 3.00 \times 10^8\ \text{m/s}$ 为光速，$\Delta t$ 为激光发射与回波接收的时间差。点云密度取决于激光通道数、旋转频率与脉冲重复频率，单帧点数为：

$$
N_{\text{frame}} = n_{\text{channels}} \cdot f_{\text{rotation}} \cdot \frac{360^\circ}{\Delta \theta_{\text{azimuth}}}
$$

典型 16 线产品在 10 Hz 转速、0.2° 水平角分辨率下每秒可输出约 30 万点；32 线产品单回波可达 64 万点/秒。

## 关键参数表

| 参数 | Hesai XT32M2X（代表值） | Velodyne VLP-16（代表值） |
|------|------------------------|--------------------------|
| 扫描方式 | 机械旋转 | 机械旋转 |
| 通道数 | 32 | 16 |
| 水平视场角 | 360° | 360° |
| 垂直视场角 | 40.3°（-20.8° ~ +19.5°） | 30°（±15°） |
| 垂直角分辨率 | 1.3° | 2° |
| 量程 | 0.5 ~ 300 m（80 m @ 10% 反射率） | 100 m |
| 测距精度 | ±1 cm（典型） | ±3 cm（典型） |
| 测距重复精度 | 0.5 cm（1σ，典型） | — |
| 点频（单回波） | 640,000 pts/s | 300,000 pts/s |
| 回波模式 | 单/双/三回波 | 双回波 |
| 波长 | 905 nm | 903 nm |
| 激光等级 | Class 1 人眼安全 | Class 1 人眼安全 |
| 功耗 | 10 W | 8 W |
| 重量 | 490 g | 830 g |
| 防护等级 | IP6K7 | IP67 |
| 工作温度 | -20 °C ~ 60 °C | -10 °C ~ 60 °C |

## 应用场景

- 自动驾驶与机器人导航：构建实时三维点云地图，实现 SLAM 与障碍物检测；
- 移动测绘：车载、机载与背包式三维激光扫描；
- 工业自动化：AGV/AMR 避障、料位检测与尺寸测量；
- 数字孪生与 BIM：高精度点云采集与逆向建模。

## 供应链关系

`ent_component_lidar` 是传感器类别节点，向上依赖激光发射器、光电探测器、光学镜片、电机/扫描机构、信号处理 FPGA/ASIC 与高精度时钟等零部件；向下为整机平台提供环境感知输入，例如 `ent_product_unitree_h1` 等机器人产品集成 LiDAR 实现 360° 感知。在图谱中，制造商节点如 `ent_company_hesai` 生产具体产品型号，并通过 `ent_component_hesai_at128`、`ent_component_hesai_et25` 等实例与该类别节点关联。

## 来源与验证

- Hesai XT32M2X 官方用户手册提供了通道数、视场角、量程、精度、点频、功耗、环境适应性等完整参数。
- Velodyne VLP-16 官方规格书提供了 16 通道机械旋转 LiDAR 的典型参数。
- Geo Week News 报道了 NavVis VLX3 系统采用 XT32M2X 的实测规格。
- 本表对未公开项未作推断，机械旋转式 LiDAR 的代表性参数以两款公开 datasheet 为准。
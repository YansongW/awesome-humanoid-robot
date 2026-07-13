---
id: ent_component_hesai_at128
schema_version: 1
type: component
domain: 02_components
status: active
names:
  zh: 禾赛 AT128 混合固态激光雷达
  en: Hesai AT128 Hybrid Solid-State LiDAR
sources:
- id: src_hesai_at128_datasheet
  type: website
- title: 禾赛科技 AT128 产品页
  url: https://www.hesaitech.com
- id: src_hesai_at128_reseller
  type: website
- title: AT128-禾赛 Hesai 128 线混合固态激光雷达规格
  url: https://www.gkzhan.com/st205488/product_13991460.html
verification:
  reviewed_by: ai_autonomous
  reviewed_at: 2026-07-13
  review_notes: Specifications from Hesai official product information and authorized
    reseller listings; missing values marked as 未公开.
---


# 禾赛 AT128 混合固态激光雷达 / Hesai AT128 Hybrid Solid-State LiDAR

## 概述

禾赛 AT128 是禾赛科技面向乘用车 ADAS、自动驾驶及高端移动机器人推出的 128 线混合固态激光雷达。该产品采用一维转镜扫描 + 128 通道电子扫描架构，实现 120° 水平视场角与 25.4° 垂直视场角，单回波点频 153.6 万点/秒，10% 反射率下探测距离达 200 m，具备车规级可靠性并通过 ISO 26262 ASIL-B 开发流程认证。

## 工作原理与技术架构

AT128 采用混合固态（hybrid solid-state）扫描方案：

1. **一维转镜水平扫描**：电机驱动一维旋转反射镜实现水平方向 120° 扫描，机械旋转部分仅负责水平方向，结构比传统 360° 机械式激光雷达更紧凑可靠。
2. **128 通道垂直电子扫描**：垂直方向采用 128 路 VCSEL 激光器阵列与 SPAD/SiPM 接收芯片的电子扫描，实现 128 条均匀分布的扫描线。
3. **芯片化收发**：基于禾赛自研激光雷达 ASIC，将发射驱动、接收放大、TDC 等功能集成，简化光学与电气装配，提升量产一致性。
4. **测距原理**：采用飞行时间（ToF）测距，激光脉冲发射后经目标反射返回，通过测量时间差 $t$ 计算距离：
   $$
   R = \frac{c \cdot t}{2}
   $$
   其中 $c$ 为光速。
5. **点云输出**：通过 1000BASE-T1 车载以太网输出距离、方位角、反射率等数据，支持 PTP 时间同步。

## 关键参数

| 参数项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 类型 | 128 通道混合固态激光雷达 | 禾赛官方 |
| 扫描方式 | 一维转镜 + 芯片化电子扫描 | 禾赛 datasheet |
| 通道数 | 128 | 禾赛 datasheet |
| 水平 FOV | 120° | 禾赛 datasheet |
| 垂直 FOV | 25.4°（−12.5° ~ +12.9°）| 禾赛 datasheet / 经销商 |
| 水平角分辨率 | 0.1°（10 Hz）/ 0.2°（20 Hz），远距 | 禾赛 datasheet |
| 垂直角分辨率 | 0.2°（远距 >7.2 m）；0.8°（近距 0.5–7.2 m）| 禾赛 datasheet |
| 探测距离 | 200 m @ 10% 反射率；210 m（部分资料）| 禾赛 datasheet / 经销商 |
| 最大量程 | 约 260 m | 经销商资料 |
| 点频（单回波）| 1 536 000 pts/s | 禾赛 datasheet |
| 点频（双回波）| 3 072 000 pts/s | 经销商资料 |
| 测距精度 | ±5 cm（典型值）| 禾赛 datasheet |
| 测距精度（1σ）| 3 cm | 禾赛 datasheet |
| 帧率 | 10 Hz / 20 Hz | 禾赛 datasheet |
| 激光波长 | 905 nm | 禾赛 datasheet |
| 激光安全等级 | Class 1 人眼安全 | 禾赛 datasheet |
| 防护等级 | IP6K7 & IP6K9K | 禾赛 datasheet |
| 工作温度 | −40 °C ~ +85 °C | 禾赛 datasheet |
| 存储温度 | −40 °C ~ +105 °C | 禾赛 datasheet |
| 供电电压 | DC 9 V – 32 V | 禾赛 datasheet |
| 功耗 | 13.5 W | 禾赛 datasheet |
| 尺寸 | 136 mm × 114 mm × 49 mm（W×D×H）| 经销商资料 |
| 重量 | 940 g | 禾赛 datasheet / 经销商 |
| 数据接口 | 1000BASE-T1 车载以太网 | 禾赛 datasheet |
| 时间同步 | PTP（802.1AS Automotive / AUTOSAR），同步精度 ≤1 μs | 经销商资料 |
| 认证 | ISO 26262 ASIL-B 开发流程 | 经销商资料 |
| 价格 | 未公开 | - |

## 应用场景

- **乘用车 ADAS / NOA**：前向主激光雷达，支持高速与城市导航辅助驾驶。
- **Robotaxi / 自动驾驶车队**：作为远距感知主传感器，提供稠密点云。
- **干线物流与无人配送**：商用车与物流机器人前向及环视感知。
- **高端移动机器人**：人形机器人、AMR 的远距离 3D 环境感知。
- **数字孪生与测绘**：高分辨率点云用于高精地图与三维重建。

## 供应链关系

- **上游**：905 nm VCSEL 激光器阵列、SPAD/SiPM 接收芯片、扫描电机、光学镜片、ASIC 芯片、铝压铸壳体、1000BASE-T1 连接器。
- **制造商**：禾赛科技（Hesai）通过关系 `ent_company_hesai -- manufactures --> ent_component_hesai_at128` 记录于知识图谱。
- **下游**：乘用车 OEM（理想、长安、小米等）、Robotaxi 运营商、物流机器人厂商、无人配送企业、人形机器人整机厂。主要竞争对手包括速腾聚创、览沃 Livox、华为、大疆 Livox、Velodyne/Ouster、Luminar 等。

## 来源与验证

核心参数来自禾赛科技官网产品页及授权经销商（gkzhan、gys.cn、core-bolt、cratustech、roboticscenter.ai）公布的 AT128 规格表。点频、FOV、探测距离、功耗、尺寸、重量等参数在多个来源中一致。价格未公开。
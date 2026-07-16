---
$id: ent_component_livox_mid_360_lidar_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: Livox Mid-360 LiDAR
  zh: Livox Mid-360 激光雷达
  ko: Livox Mid-360 LiDAR
summary:
  en: Compact 360-degree LiDAR commonly mounted on the head or torso of humanoid robots.
  zh: Livox Mid-360 激光雷达是人形机器人领域的重要component。以下内容整理自项目 Wiki，供深入查阅。
  ko: 휨로봇 머리나 몸통에 장착되는 컴팩트한 360도 LiDAR.
domains:
- 02_components
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- '360'
- component
- lidar
- livox
- sensor
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/companies/company_livox.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Livox Mid-360 LiDAR
  url: https://www.livoxtech.com/
  date: '2024'
  accessed_at: '2026-07-02'
---


## 概述
Livox Mid-360 激光雷达是人形机器人领域的重要零部件。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## 览沃 / Livox Technology

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 览沃 |
| **英文名** | Livox Technology |
| **总部** | 中国深圳 |
| **成立时间** | 2016 |
| **官网** | [https://www.livoxtech.com](https://www.livoxtech.com) |
| **供应链环节** | 激光雷达、混合固态 LiDAR、机器人 3D 感知 |
| **企业属性** | 私有公司、DJI 内部孵化独立公司 |
| **母公司/所属集团** | DJI 大疆创新内部孵化 / 独立运营 |
| **数据来源** | 官网、DJI/Livox 公开资料、产品 datasheet |

### 公司简介

览沃科技是 DJI 内部孵化的激光雷达公司，以高性价比混合固态激光雷达切入机器人与自动驾驶市场。

Livox 致力于提供高性能、低成本的激光雷达传感器，产品采用独特的旋镜式混合固态扫描技术。Mid-360 凭借 360° 环视、小体积与轻量化，成为机器人 SLAM 与导航的热门选择，并已应用于四足机器人、清洁机器人与 AMR。

### 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| Mid 系列 | 机器人 360° 激光雷达 | Mid-360 / Mid-360S / Mid-70 | AMR、四足机器人、清洁机器人、SLAM |
| HAP / Horizon | 车规级激光雷达 | HAP / Horizon / Tele-15 | 自动驾驶、乘用车 |
| Avia | 测绘级激光雷达 | Avia | 无人机测绘、三维建模 |

### 代表产品

#### 览沃 Mid-360

> 览沃 Mid-360：请访问 [官方资料](https://www.livoxtech.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 65 mm × 65 mm × 60 mm | 官方 datasheet |
| 重量 | 265 g | 官方 datasheet |
| 激光波长 | 905 nm | 官方 datasheet |
| 激光安全等级 | Class 1（IEC60825-1:2014） | 官方 datasheet |
| FOV | 水平 360°；竖直 -7° ~ 52° | 官方 datasheet |
| 探测距离 | 40 m @ 10% 反射率；70 m @ 80% 反射率 | 官方 datasheet |
| 点频 | 200,000 点/秒（首回波） | 官方 datasheet |
| 帧率 | 10 Hz（典型） | 官方 datasheet |
| 测距精度 | ≤2 cm @ 10 m；≤3 cm @ 0.2 m | 官方 datasheet |
| IMU | 内置 ICM40609 | 官方 datasheet |
| 接口 | 100 BASE-TX Ethernet | 官方 datasheet |
| 功耗 | 6.5 W（典型） | 官方 datasheet |
| 价格 | 约 CNY 3,999 | 官方商城 |

**技术亮点**：360° 环视、超小体积、内置 IMU、IP67 防护，是机器人 SLAM 与导航的主流选择。

**应用场景**：AMR/AGV 导航、四足机器人、清洁机器人、割草机器人、三维测绘。

#### 览沃 HAP

> 览沃 HAP：请访问 [官方资料](https://www.livoxtech.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| FOV | 120°(H) × 30°(V) | 官方 datasheet |
| 探测距离 | 150 m @ 10% 反射率 | 官方 datasheet |
| 点频 | 240,000 点/秒 | 官方 datasheet |
| 角分辨率 | 0.18°(H) × 0.23°(V) | 官方 datasheet |
| 扫描方式 | 混合固态（旋镜式） | 官方 datasheet |
| 防护等级 | IP67 | 官方 datasheet |
| 价格 | 未公开 | 未公开 |

**技术亮点**：车规级混合固态激光雷达，已在多款乘用车前装量产，兼顾远距探测与可靠性。

**应用场景**：乘用车 ADAS、Robotaxi、高端移动机器人。

### 供应链位置

- **上游关键零部件/材料**：905 nm 激光器、SPAD/APD、扫描电机、光学镜片、主控 SoC、IMU
- **下游客户/应用场景**：AMR/AGV、四足机器人（如云深处绝影 X30）、清洁机器人、割草机器人、自动驾驶
- **主要竞争对手/对标**：禾赛科技、速腾聚创、Ouster、Velodyne、RoboSense

### 知识图谱节点与关系

- 公司实体：`ent_company_livox`
- 产品实体：`ent_component_livox_mid_360`
- 产品实体：`ent_component_livox_hap`
- 关键关系：
  - `ent_company_livox` -- `manufactures` --> `ent_component_livox_mid_360`
  - `ent_company_livox` -- `manufactures` --> `ent_component_livox_hap`
  - `ent_company_livox` -- `supplies` --> `ent_company_deep_robotics` (云深处绝影 X30 四足机器人搭载 Livox Mid-360)

### 参考资料

1. [官网](https://www.livoxtech.com)
2. [产品资料与公开报道](https://www.livoxtech.com)
3. [附录 D 产品目录](../index-products.md)

## 参考
- [Livox Mid-360 LiDAR](https://www.livoxtech.com/)
- 项目 Wiki：appendix-d/companies/company_livox.md

## Overview
The Livox Mid-360 LiDAR is an important component in the field of humanoid robotics. The following content is compiled from the project Wiki for in-depth reference.

## Content
## Livox Technology

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

### Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 览沃 |
| **English Name** | Livox Technology |
| **Headquarters** | Shenzhen, China |
| **Founded** | 2016 |
| **Website** | [https://www.livoxtech.com](https://www.livoxtech.com) |
| **Supply Chain Role** | LiDAR, Hybrid Solid-State LiDAR, Robot 3D Perception |
| **Company Type** | Private Company, Independent Company Incubated by DJI |
| **Parent Company/Group** | Incubated by DJI / Operates Independently |
| **Data Source** | Official Website, DJI/Livox Public Materials, Product Datasheets |

### Company Profile

Livox Technology is a LiDAR company incubated by DJI, entering the robot and autonomous driving market with cost-effective hybrid solid-state LiDAR.

Livox is dedicated to providing high-performance, low-cost LiDAR sensors, employing a unique rotating mirror hybrid solid-state scanning technology. The Mid-360, with its 360° surround view, compact size, and lightweight design, has become a popular choice for robot SLAM and navigation, and has been applied in quadruped robots, cleaning robots, and AMRs.

### Product Line

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Mid Series | Robot 360° LiDAR | Mid-360 / Mid-360S / Mid-70 | AMR, Quadruped Robots, Cleaning Robots, SLAM |
| HAP / Horizon | Automotive-Grade LiDAR | HAP / Horizon / Tele-15 | Autonomous Driving, Passenger Vehicles |
| Avia | Surveying-Grade LiDAR | Avia | Drone Surveying, 3D Modeling |

### Representative Products

#### Livox Mid-360

> Livox Mid-360: Please visit [Official Materials](https://www.livoxtech.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Dimensions | 65 mm × 65 mm × 60 mm | Official Datasheet |
| Weight | 265 g | Official Datasheet |
| Laser Wavelength | 905 nm | Official Datasheet |
| Laser Safety Class | Class 1 (IEC60825-1:2014) | Official Datasheet |
| FOV | Horizontal 360°; Vertical -7° ~ 52° | Official Datasheet |
| Detection Range | 40 m @ 10% Reflectivity; 70 m @ 80% Reflectivity | Official Datasheet |
| Point Rate | 200,000 points/sec (First Return) | Official Datasheet |
| Frame Rate | 10 Hz (Typical) | Official Datasheet |
| Ranging Accuracy | ≤2 cm @ 10 m; ≤3 cm @ 0.2 m | Official Datasheet |
| IMU | Built-in ICM40609 | Official Datasheet |
| Interface | 100 BASE-TX Ethernet | Official Datasheet |
| Power Consumption | 6.5 W (Typical) | Official Datasheet |
| Price | Approx. CNY 3,999 | Official Store |

**Technical Highlights**: 360° surround view, ultra-compact size, built-in IMU, IP67 protection, a mainstream choice for robot SLAM and navigation.

**Application Scenarios**: AMR/AGV Navigation, Quadruped Robots, Cleaning Robots, Lawn Mowing Robots, 3D Surveying.

#### Livox HAP

> Livox HAP: Please visit [Official Materials](https://www.livoxtech.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| FOV | 120°(H) × 30°(V) | Official Datasheet |
| Detection Range | 150 m @ 10% Reflectivity | Official Datasheet |
| Point Rate | 240,000 points/sec | Official Datasheet |
| Angular Resolution | 0.18°(H) × 0.23°(V) | Official Datasheet |
| Scanning Method | Hybrid Solid-State (Rotating Mirror) | Official Datasheet |
| Protection Rating | IP67 | Official Datasheet |
| Price | Not Disclosed | Not Disclosed |

**Technical Highlights**: Automotive-grade hybrid solid-state LiDAR, already mass-produced in several passenger vehicles, balancing long-range detection and reliability.

**Application Scenarios**: Passenger Car ADAS, Robotaxi, High-End Mobile Robots.

### Supply Chain Position

- **Upstream Key Components/Materials**: 905 nm Laser, SPAD/APD, Scanning Motor, Optical Lenses, Main Control SoC, IMU
- **Downstream Customers/Applications**: AMR/AGV, Quadruped Robots (e.g., Deep Robotics Jueying X30), Cleaning Robots, Lawn Mowing Robots, Autonomous Driving
- **Main Competitors/Peers**: Hesai Technology, RoboSense, Ouster, Velodyne, RoboSense

### Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_livox`
- Product Entity: `ent_component_livox_mid_360`
- Product Entity: `ent_component_livox_hap`
- Key Relationships:
  - `ent_company_livox` -- `manufactures` --> `ent_component_livox_mid_360`
  - `ent_company_livox` -- `manufactures` --> `ent_component_livox_hap`
  - `ent_company_livox` -- `supplies` --> `ent_company_deep_robotics` (Deep Robotics Jueying X30 quadruped robot equipped with Livox Mid-360)

### References

1. [Official Website](https://www.livoxtech.com)
2. [Product Materials and Public Reports](https://www.livoxtech.com)
3. [Appendix D Product Catalog](../index-products.md)

## 개요
Livox Mid-360 라이다는 휴머노이드 로봇 분야의 중요한 부품입니다. 아래 내용은 프로젝트 Wiki에서 정리한 것으로, 심층 참고용으로 제공됩니다.

## 핵심 내용
## 란보 / Livox Technology

> 본 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

### 기업 정보 카드

| 항목 | 내용 |
|------|------|
| **중문명** | 란보 |
| **영문명** | Livox Technology |
| **본사** | 중국 선전 |
| **설립 연도** | 2016 |
| **공식 웹사이트** | [https://www.livoxtech.com](https://www.livoxtech.com) |
| **공급망 단계** | 라이다, 하이브리드 솔리드 스테이트 LiDAR, 로봇 3D 인식 |
| **기업 속성** | 사기업, DJI 내부 인큐베이팅 독립 기업 |
| **모회사/소속 그룹** | DJI 대장 혁신 내부 인큐베이팅 / 독립 운영 |
| **데이터 출처** | 공식 웹사이트, DJI/Livox 공개 자료, 제품 데이터시트 |

### 기업 소개

란보 테크놀로지는 DJI 내부에서 인큐베이팅된 라이다 기업으로, 높은 가성비의 하이브리드 솔리드 스테이트 라이다로 로봇 및 자율주행 시장에 진출했습니다.

Livox는 고성능, 저비용의 라이다 센서를 제공하는 데 주력하며, 독특한 회전 미러 방식의 하이브리드 솔리드 스테이트 스캐닝 기술을 채택하고 있습니다. Mid-360은 360° 전방위 시야, 소형 크기, 경량화로 로봇 SLAM 및 내비게이션의 인기 제품이 되었으며, 사족 보행 로봇, 청소 로봇, AMR에 적용되었습니다.

### 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 응용 분야 |
|--------|------|----------|----------|
| Mid 시리즈 | 로봇 360° 라이다 | Mid-360 / Mid-360S / Mid-70 | AMR, 사족 보행 로봇, 청소 로봇, SLAM |
| HAP / Horizon | 차량용 라이다 | HAP / Horizon / Tele-15 | 자율주행, 승용차 |
| Avia | 측량용 라이다 | Avia | 드론 측량, 3D 모델링 |

### 대표 제품

#### 란보 Mid-360

> 란보 Mid-360: [공식 자료](https://www.livoxtech.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 65 mm × 65 mm × 60 mm | 공식 데이터시트 |
| 무게 | 265 g | 공식 데이터시트 |
| 레이저 파장 | 905 nm | 공식 데이터시트 |
| 레이저 안전 등급 | Class 1 (IEC60825-1:2014) | 공식 데이터시트 |
| FOV | 수평 360°; 수직 -7° ~ 52° | 공식 데이터시트 |
| 탐지 거리 | 40 m @ 10% 반사율; 70 m @ 80% 반사율 | 공식 데이터시트 |
| 포인트 주파수 | 200,000 포인트/초 (첫 번째 에코) | 공식 데이터시트 |
| 프레임 속도 | 10 Hz (일반) | 공식 데이터시트 |
| 거리 측정 정밀도 | ≤2 cm @ 10 m; ≤3 cm @ 0.2 m | 공식 데이터시트 |
| IMU | 내장 ICM40609 | 공식 데이터시트 |
| 인터페이스 | 100 BASE-TX Ethernet | 공식 데이터시트 |
| 소비 전력 | 6.5 W (일반) | 공식 데이터시트 |
| 가격 | 약 CNY 3,999 | 공식 쇼핑몰 |

**기술 하이라이트**: 360° 전방위 시야, 초소형 크기, 내장 IMU, IP67 보호 등급으로 로봇 SLAM 및 내비게이션의 주류 선택입니다.

**응용 시나리오**: AMR/AGV 내비게이션, 사족 보행 로봇, 청소 로봇, 잔디 깎기 로봇, 3D 측량.

#### 란보 HAP

> 란보 HAP: [공식 자료](https://www.livoxtech.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| FOV | 120°(H) × 30°(V) | 공식 데이터시트 |
| 탐지 거리 | 150 m @ 10% 반사율 | 공식 데이터시트 |
| 포인트 주파수 | 240,000 포인트/초 | 공식 데이터시트 |
| 각도 분해능 | 0.18°(H) × 0.23°(V) | 공식 데이터시트 |
| 스캔 방식 | 하이브리드 솔리드 스테이트 (회전 미러 방식) | 공식 데이터시트 |
| 보호 등급 | IP67 | 공식 데이터시트 |
| 가격 | 미공개 | 미공개 |

**기술 하이라이트**: 차량용 하이브리드 솔리드 스테이트 라이다로, 여러 승용차에 양산 적용되었으며 원거리 탐지와 신뢰성을 겸비했습니다.

**응용 시나리오**: 승용차 ADAS, Robotaxi, 고급 이동 로봇.

### 공급망 위치

- **상류 핵심 부품/재료**: 905 nm 레이저, SPAD/APD, 스캔 모터, 광학 렌즈, 메인 컨트롤 SoC, IMU
- **하류 고객/응용 시나리오**: AMR/AGV, 사족 보행 로봇 (예: DeepRobotics Jueying X30), 청소 로봇, 잔디 깎기 로봇, 자율주행
- **주요 경쟁사/대응**: Hesai Technology, RoboSense, Ouster, Velodyne, RoboSense

### 지식 그래프 노드 및 관계

- 기업 엔터티: `ent_company_livox`
- 제품 엔터티: `ent_component_livox_mid_360`
- 제품 엔터티: `ent_component_livox_hap`
- 주요 관계:
  - `ent_company_livox` -- `manufactures` --> `ent_component_livox_mid_360`
  - `ent_company_livox` -- `manufactures` --> `ent_component_livox_hap`
  - `ent_company_livox` -- `supplies` --> `ent_company_deep_robotics` (DeepRobotics Jueying X30 사족 보행 로봇에 Livox Mid-360 탑재)

### 참고 자료

1. [공식 웹사이트](https://www.livoxtech.com)
2. [제품 자료 및 공개 보도](https://www.livoxtech.com)
3. [부록 D 제품 목록](../index-products.md)

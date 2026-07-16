---
$id: ent_robot_unitree_h1_humanoid_robot_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: Unitree H1 Humanoid Robot
  zh: 宇树 H1 人形机器人
  ko: Unitree H1 휨로봇
summary:
  en: Full-size electric humanoid with 25-27 DoF, proprietary high-torque joints, peak leg-joint torque up to 360 N·m and
    torque density ~189 N·m/kg.
  zh: 概述 宇树 H1 人形机器人是人形机器人领域的重要robot_system。以下内容整理自项目 Wiki，供深入查阅。
  ko: 25-27자유도를 가진 전기식 휨로봇, 최대 360 N·m 다리 관절 토크 및 약 189 N·m/kg 토크 밀도.
domains:
- 06_design_engineering
- 02_components
layers:
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- high_torque_joint
- humanoid
- quasi_direct_drive
- robot_system
- unitree
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/products/product_unitree_h1.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Unitree H1 Humanoid Robot
  url: https://www.unitree.com/products/h1
  date: '2024'
  accessed_at: '2026-07-01'
---

## 概述
宇树 H1 人形机器人是人形机器人领域的重要机器人系统。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## 宇树 H1 / Unitree H1

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [宇树科技 / Unitree Robotics](../companies/company_unitree.md) |
| **产品类别** | 全尺寸高动态人形机器人 |
| **发布时间** | 2023 年 |
| **状态** | 量产/商用 |
| **官网/来源** | [Unitree 官网](https://www.unitree.com) |

### 产品概述

宇树 H1 是 Unitree Robotics 推出的全尺寸高动态人形机器人，定位为科研、具身智能研究与高动态运动验证平台。H1 采用宇树自研 M107 永磁同步电机，膝关节峰值扭矩达 360 N·m，峰值扭矩密度约 189 N·m/kg，曾创造全尺寸人形机器人 3.3 m/s 奔跑速度纪录。

H1 的基础版手臂为 4 DOF，可选配 H1-2 升级方案将手臂提升至 7 DOF 并增强整机负载能力。整机支持 ROS2 与 Unitree SDK，具备 Wi-Fi、蓝牙与热插拔电池，适用于高校实验室、AI 研究机构与工业原型验证。

### 产品图片

> Unitree H1：请访问 [官方资料](https://www.unitree.com) 查看。

### 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 180 cm（高） | 公开规格 |
| 重量 | 约 47 kg（H1 基础版） | 公开规格 |
| 自由度（整机） | 26–27 DOF | 基础版 26 DOF；H1-2 为 27 DOF |
| 关键性能指标 | 膝关节峰值扭矩 360 N·m；扭矩密度 189 N·m/kg | 公开规格 |
| 行走速度 | 约 1.5 m/s；奔跑速度 3.3 m/s | 公开规格 |
| 续航 | 约 1.5–2 小时（864 Wh 电池） | 公开规格 |
| 计算平台 | 可选 Intel Core / NVIDIA Jetson Orin NX | 公开规格 |
| 价格 | 约 90,000 USD / 国内约 65 万元 | 经销商与媒体报道 |

### 供应链位置

- **制造商**：[宇树科技 / Unitree Robotics](../companies/company_unitree.md)
- **核心零部件/技术来源**：自研 M107 电机与驱动器、Intel RealSense / LIVOX 传感器、减速器与轴承外购。
- **下游应用/客户**：高校、科研院所、具身智能研究团队、工业原型客户。

### 知识图谱节点与关系

- 产品实体：`ent_product_unitree_h1`
- 制造商实体：`ent_company_unitree`
- 关键关系：
  - `rel_ent_company_unitree_manufactures_ent_product_unitree_h1`（`ent_company_unitree` → `manufactures` → `ent_product_unitree_h1`）

### 应用场景

- **双足运动研究**：高校与科研机构开展步态规划、强化学习与动态平衡算法验证。
- **具身智能平台**：作为大模型与机器人控制结合的硬件载体，用于 VLA/VLM 部署测试。
- **工业原型验证**：物流与制造企业用于高动态搬运、越障与复杂地形通过性测试。

### 竞争对比

| 对比项 | Unitree H1 | Unitree G1 | Tesla Optimus Gen 3 |
|--------|------------|------------|---------------------|
| 定位 | 全尺寸高动态研究平台 | 紧凑型开发平台 | 通用/工业人形 |
| 身高 | 180 cm | 127 cm | 173 cm |
| 价格 | 约 90,000 USD | 约 16,000 USD | 目标 20,000–30,000 USD |
| 核心优势 | 高动态运动、扭矩密度、ROS2 生态 | 低成本、可及性、灵巧手 | 制造规模目标、灵巧手 |

### 选购与部署建议

- 高动态运动研究团队建议选配 H1-2 升级方案以提升手臂自由度与整机负载。
- 由于 H1 基础版手臂自由度有限，需要灵巧操作的项目应额外配置末端执行器。

### 参考资料

1. [Unitree 官网](https://www.unitree.com)
2. [Robozaps – Unitree H1 Review](https://blog.robozaps.com/b/unitree-h1-review)
3. [OpenELAB – Unitree H1-2](https://openelab.com/products/unitree-h1-2-humanoid-robot)
4. [附录 D.4 重点产品 Wiki](../index-products.md)

## 参考
- [Unitree H1 Humanoid Robot](https://www.unitree.com/products/h1)
- 项目 Wiki：appendix-d/products/product_unitree_h1.md

## Overview
The Unitree H1 humanoid robot is a significant robotic system in the field of humanoid robotics. The following content is compiled from the project Wiki for in-depth reference.

## Content
## Unitree H1

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

### Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Unitree Robotics](../companies/company_unitree.md) |
| **Product Category** | Full-size high-dynamic humanoid robot |
| **Release Date** | 2023 |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [Unitree Official Website](https://www.unitree.com) |

### Product Overview

The Unitree H1 is a full-size high-dynamic humanoid robot launched by Unitree Robotics, positioned as a platform for scientific research, embodied intelligence research, and high-dynamic motion validation. The H1 uses Unitree's self-developed M107 permanent magnet synchronous motor, with a peak torque of 360 N·m at the knee joint and a peak torque density of approximately 189 N·m/kg. It once set a running speed record of 3.3 m/s for a full-size humanoid robot.

The basic version of the H1 has 4 DOF arms, with an optional H1-2 upgrade that enhances the arms to 7 DOF and increases the overall load capacity. The robot supports ROS2 and the Unitree SDK, features Wi-Fi, Bluetooth, and a hot-swappable battery, making it suitable for university laboratories, AI research institutions, and industrial prototype validation.

### Product Images

> Unitree H1: Please visit the [official website](https://www.unitree.com) for images.

### Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Approx. 180 cm (height) | Public specification |
| Weight | Approx. 47 kg (H1 basic version) | Public specification |
| Degrees of Freedom (Total) | 26–27 DOF | Basic version: 26 DOF; H1-2: 27 DOF |
| Key Performance Indicators | Knee peak torque: 360 N·m; Torque density: 189 N·m/kg | Public specification |
| Walking Speed | Approx. 1.5 m/s; Running speed: 3.3 m/s | Public specification |
| Battery Life | Approx. 1.5–2 hours (864 Wh battery) | Public specification |
| Computing Platform | Optional: Intel Core / NVIDIA Jetson Orin NX | Public specification |
| Price | Approx. 90,000 USD / Domestic: approx. 650,000 RMB | Dealer and media reports |

### Supply Chain Position

- **Manufacturer**: [Unitree Robotics](../companies/company_unitree.md)
- **Core Components/Technology Source**: Self-developed M107 motors and drivers, Intel RealSense / LIVOX sensors, externally sourced reducers and bearings.
- **Downstream Applications/Customers**: Universities, research institutes, embodied intelligence research teams, industrial prototype clients.

### Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_unitree_h1`
- Manufacturer Entity: `ent_company_unitree`
- Key Relationships:
  - `rel_ent_company_unitree_manufactures_ent_product_unitree_h1` (`ent_company_unitree` → `manufactures` → `ent_product_unitree_h1`)

### Application Scenarios

- **Bipedal Locomotion Research**: Universities and research institutions conduct gait planning, reinforcement learning, and dynamic balance algorithm validation.
- **Embodied Intelligence Platform**: Serves as the hardware carrier for combining large models with robot control, used for VLA/VLM deployment testing.
- **Industrial Prototype Validation**: Logistics and manufacturing enterprises use it for high-dynamic handling, obstacle crossing, and complex terrain traversability testing.

### Competitive Comparison

| Comparison Item | Unitree H1 | Unitree G1 | Tesla Optimus Gen 3 |
|-----------------|------------|------------|---------------------|
| Positioning | Full-size high-dynamic research platform | Compact development platform | General/Industrial humanoid |
| Height | 180 cm | 127 cm | 173 cm |
| Price | Approx. 90,000 USD | Approx. 16,000 USD | Target: 20,000–30,000 USD |
| Core Advantage | High-dynamic motion, torque density, ROS2 ecosystem | Low cost, accessibility, dexterous hand | Manufacturing scale target, dexterous hand |

### Purchase and Deployment Recommendations

- High-dynamic motion research teams are advised to opt for the H1-2 upgrade to enhance arm DOF and overall load capacity.
- Due to the limited arm DOF of the basic H1 version, projects requiring dexterous manipulation should configure additional end effectors.

### References

1. [Unitree Official Website](https://www.unitree.com)
2. [Robozaps – Unitree H1 Review](https://blog.robozaps.com/b/unitree-h1-review)
3. [OpenELAB – Unitree H1-2](https://openelab.com/products/unitree-h1-2-humanoid-robot)
4. [Appendix D.4 Key Product Wiki](../index-products.md)

## 개요
우슈 H1 휴머노이드 로봇은 휴머노이드 로봇 분야의 중요한 로봇 시스템입니다. 다음 내용은 프로젝트 Wiki에서 정리한 것으로, 심층 참고용으로 제공됩니다.

## 핵심 내용
## 우슈 H1 / Unitree H1

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

### 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [우슈 테크놀로지 / Unitree Robotics](../companies/company_unitree.md) |
| **제품 카테고리** | 풀사이즈 고동적 휴머노이드 로봇 |
| **출시일** | 2023년 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [Unitree 공식 홈페이지](https://www.unitree.com) |

### 제품 개요

우슈 H1은 Unitree Robotics가 출시한 풀사이즈 고동적 휴머노이드 로봇으로, 연구, 체현 지능 연구 및 고동적 운동 검증 플랫폼으로 자리매김하고 있습니다. H1은 우슈 자체 개발 M107 영구자석 동기 모터를 채택하여 무릎 관절 최대 토크 360 N·m, 최대 토크 밀도 약 189 N·m/kg을 달성했으며, 풀사이즈 휴머노이드 로봇 3.3 m/s 달리기 속도 기록을 세웠습니다.

H1 기본 버전의 팔은 4 DOF이며, H1-2 업그레이드 옵션을 통해 팔을 7 DOF로 향상시키고 전체 기계의 하중 용량을 강화할 수 있습니다. 전체 기계는 ROS2 및 Unitree SDK를 지원하며, Wi-Fi, 블루투스 및 핫스왑 배터리를 갖추고 있어 대학 연구실, AI 연구 기관 및 산업 프로토타입 검증에 적합합니다.

### 제품 이미지

> Unitree H1: [공식 자료](https://www.unitree.com)를 방문하여 확인하세요.

### 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 약 180 cm (높이) | 공개 사양 |
| 무게 | 약 47 kg (H1 기본 버전) | 공개 사양 |
| 자유도 (전체 기계) | 26–27 DOF | 기본 버전 26 DOF; H1-2는 27 DOF |
| 주요 성능 지표 | 무릎 관절 최대 토크 360 N·m; 토크 밀도 189 N·m/kg | 공개 사양 |
| 보행 속도 | 약 1.5 m/s; 달리기 속도 3.3 m/s | 공개 사양 |
| 배터리 지속 시간 | 약 1.5–2시간 (864 Wh 배터리) | 공개 사양 |
| 컴퓨팅 플랫폼 | 옵션 Intel Core / NVIDIA Jetson Orin NX | 공개 사양 |
| 가격 | 약 90,000 USD / 국내 약 65만 위안 | 딜러 및 미디어 보도 |

### 공급망 위치

- **제조사**: [우슈 테크놀로지 / Unitree Robotics](../companies/company_unitree.md)
- **핵심 부품/기술 출처**: 자체 개발 M107 모터 및 드라이버, Intel RealSense / LIVOX 센서, 감속기 및 베어링 외부 구매.
- **하류 응용/고객**: 대학, 연구 기관, 체현 지능 연구팀, 산업 프로토타입 고객.

### 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_unitree_h1`
- 제조사 엔터티: `ent_company_unitree`
- 주요 관계:
  - `rel_ent_company_unitree_manufactures_ent_product_unitree_h1` (`ent_company_unitree` → `manufactures` → `ent_product_unitree_h1`)

### 응용 시나리오

- **이족 보행 운동 연구**: 대학 및 연구 기관에서 보행 계획, 강화 학습 및 동적 균형 알고리즘 검증 수행.
- **체현 지능 플랫폼**: 대규모 모델과 로봇 제어를 결합한 하드웨어 플랫폼으로 VLA/VLM 배포 테스트에 사용.
- **산업 프로토타입 검증**: 물류 및 제조 기업에서 고동적 운반, 장애물 극복 및 복잡 지형 통과성 테스트 수행.

### 경쟁 비교

| 비교 항목 | Unitree H1 | Unitree G1 | Tesla Optimus Gen 3 |
|--------|------------|------------|---------------------|
| 포지셔닝 | 풀사이즈 고동적 연구 플랫폼 | 컴팩트형 개발 플랫폼 | 범용/산업 휴머노이드 |
| 키 | 180 cm | 127 cm | 173 cm |
| 가격 | 약 90,000 USD | 약 16,000 USD | 목표 20,000–30,000 USD |
| 핵심 장점 | 고동적 운동, 토크 밀도, ROS2 생태계 | 저비용, 접근성, 정교한 손 | 제조 규모 목표, 정교한 손 |

### 구매 및 배포 권장 사항

- 고동적 운동 연구팀은 H1-2 업그레이드 옵션을 선택하여 팔 자유도와 전체 기계 하중 용량을 향상시키는 것을 권장합니다.
- H1 기본 버전의 팔 자유도가 제한적이므로, 정교한 조작이 필요한 프로젝트는 추가로 엔드 이펙터를 구성해야 합니다.

### 참고 자료

1. [Unitree 공식 홈페이지](https://www.unitree.com)
2. [Robozaps – Unitree H1 Review](https://blog.robozaps.com/b/unitree-h1-review)
3. [OpenELAB – Unitree H1-2](https://openelab.com/products/unitree-h1-2-humanoid-robot)
4. [부록 D.4 주요 제품 Wiki](../index-products.md)

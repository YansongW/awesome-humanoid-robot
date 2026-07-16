---
$id: ent_robot_system_unitree_g1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: Unitree G1 Humanoid Robot
  zh: Unitree G1 人形机器人
  ko: Unitree G1 휴머노이드 로봇
summary:
  en: A compact, mass-produced humanoid robot developed by Unitree Robotics, featuring 23–43 degrees of freedom, a 35 kg body,
    2 m/s walking speed, and options for dexterous hands, designed for research, education, and light industrial tasks.
  zh: Unitree G1 人形机器人是人形机器人领域的重要robot_system。以下内容整理自项目 Wiki，供深入查阅。
  ko: Unitree Robotics가 개발한 컴팩트한 양산형 휴머노이드 로봇으로, 23~43자유도, 35kg 몸체, 2m/s 보행 속도를 갖추며 연구, 교육 및 경량 산업 작업을 위해 설계됨.
domains:
- 02_components
- 06_design_engineering
- 05_mass_production
- 11_applications_markets
layers:
- upstream
- midstream
- validation_markets
functional_roles:
- system
- knowledge
tags:
- unitree
- humanoid_robot
- g1
- low_cost_humanoid
- research_platform
- dexterous_hand
- mass_production
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/products/product_unitree_g1.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Unitree G1 Developer Specifications
  url: https://support.unitree.com/home/en/G1_developer
  date: '2026'
  accessed_at: '2026-06-22'
- id: src_002
  type: paper
  title: Identification of a Physics-Based Electrical Power Consumption Model for the Unitree G1 Humanoid Arm
  url: https://arxiv.org/abs/2606.15915
  date: '2026'
  accessed_at: '2026-06-22'
theoretical_depth:
- system
---


## 概述
Unitree G1 人形机器人是人形机器人领域的重要机器人系统。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## 宇树 G1 / Unitree G1

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [宇树科技 / Unitree Robotics](../companies/company_unitree.md) |
| **产品类别** | 紧凑型人形机器人 |
| **发布时间** | 2024 年 |
| **状态** | 量产/商用 |
| **官网/来源** | [Unitree G1 产品页](https://www.unitree.com/g1) |

### 产品概述

宇树 G1 是 Unitree 面向教育、科研与开发者推出的紧凑型人形机器人，以激进定价和高可及性著称。G1 身高约 127 cm，体重约 35 kg，基础版拥有 23 个自由度，EDU 版可扩展至 43 DOF 并配备 Dex3-1 五指灵巧手与 NVIDIA Jetson Orin 计算模块。

G1 采用 3D LiDAR、深度相机与 8 核 CPU（EDU 版增加 Jetson Orin），支持 ROS2、Python/C++ SDK 与 OTA 升级。其可折叠设计便于运输与部署，成为全球出货量领先的人形开发平台之一。

### 产品图片

> Unitree G1：请访问 [官方资料](https://www.unitree.com/g1) 查看。

### 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 127 cm（高） | 公开规格 |
| 重量 | 约 35 kg | 公开规格 |
| 自由度（整机） | 23–43 DOF | 基础版/EDU 版配置差异 |
| 关键性能指标 | 关节峰值扭矩 90–120 N·m；负载约 2 kg | 公开规格 |
| 行走速度 | 约 2 m/s | 公开规格 |
| 续航 | 约 1.5–2 小时（9,000 mAh 快拆电池） | 公开规格 |
| 计算平台 | 8 核 CPU；EDU 版可选 NVIDIA Jetson Orin | 公开规格 |
| 价格 | 约 16,000 USD / 国内 9.9 万元起 | 媒体报道 |

### 供应链位置

- **制造商**：[宇树科技 / Unitree Robotics](../companies/company_unitree.md)
- **核心零部件/技术来源**：自研关节电机与驱动器、3D LiDAR、Intel RealSense 深度相机、NVIDIA Jetson Orin（EDU 版）。
- **下游应用/客户**：高校、教育机构、开发者、AI 研究与商用展示。

### 知识图谱节点与关系

- 产品实体：`ent_product_unitree_g1`
- 制造商实体：`ent_company_unitree`
- 关键关系：
  - `rel_ent_company_unitree_manufactures_ent_product_unitree_g1`（`ent_company_unitree` → `manufactures` → `ent_product_unitree_g1`）

### 应用场景

- **教育演示**：高校、中小学与科技馆用于机器人课程、展览与竞赛。
- **AI 与机器人研究**：开发者社区进行模仿学习、强化学习与多模态交互实验。
- **轻量商业**：零售展示、导览迎宾与小批量物流试点。

### 竞争对比

| 对比项 | Unitree G1 | Unitree H1 | Unitree R1 |
|--------|------------|------------|------------|
| 定位 | 紧凑型开发平台 | 全尺寸高动态平台 | 入门级开发平台 |
| 身高 | 127 cm | 180 cm | 121 cm |
| 价格 | 约 16,000 USD | 约 90,000 USD | 约 5,900 USD |
| 核心优势 | 性价比高、EDU 版功能全 | 高动态运动、负载大 | 超低门槛、开发者友好 |

### 选购与部署建议

- 教育/研究机构建议优先选择 G1 EDU 版以获得 SDK、ROS2 与 Jetson Orin 计算支持。
- 部署时需确保场地有足够安全空间，并配置急停装置与防护围栏。

### 参考资料

1. [Unitree G1 产品页](https://www.unitree.com/g1)
2. [Robozaps – Unitree G1 Review](https://blog.robozaps.com/b/unitree-g1-review)
3. [Humanoid.Guide – Unitree G1](https://humanoid.guide/product/g1/)
4. [Humanoid Index – G1](https://humanoidindex.org/robots/g1)

## 参考
- [Unitree G1 Developer Specifications](https://support.unitree.com/home/en/G1_developer)
- [Identification of a Physics-Based Electrical Power Consumption Model for the Unitree G1 Humanoid Arm](https://arxiv.org/abs/2606.15915)
- 项目 Wiki：appendix-d/products/product_unitree_g1.md

## Overview
The Unitree G1 humanoid robot is a significant robotic system in the field of humanoid robotics. The following content is compiled from the project Wiki for in-depth reference.

## Content
## Unitree G1

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

### Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Unitree Robotics](../companies/company_unitree.md) |
| **Product Category** | Compact Humanoid Robot |
| **Release Date** | 2024 |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [Unitree G1 Product Page](https://www.unitree.com/g1) |

### Product Overview

The Unitree G1 is a compact humanoid robot launched by Unitree for education, research, and developers, known for its aggressive pricing and high accessibility. The G1 stands approximately 127 cm tall and weighs about 35 kg. The base version has 23 degrees of freedom (DOF), while the EDU version can be expanded to 43 DOF and is equipped with the Dex3-1 five-finger dexterous hand and the NVIDIA Jetson Orin computing module.

The G1 features 3D LiDAR, depth cameras, and an 8-core CPU (the EDU version adds Jetson Orin), supporting ROS2, Python/C++ SDK, and OTA upgrades. Its foldable design facilitates transportation and deployment, making it one of the leading humanoid development platforms in terms of global shipments.

### Product Images

> Unitree G1: Please visit the [official page](https://www.unitree.com/g1) for images.

### Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Approx. 127 cm (height) | Public specification |
| Weight | Approx. 35 kg | Public specification |
| Degrees of Freedom (Full Body) | 23–43 DOF | Configuration difference between base/EDU versions |
| Key Performance Indicators | Joint peak torque 90–120 N·m; payload approx. 2 kg | Public specification |
| Walking Speed | Approx. 2 m/s | Public specification |
| Battery Life | Approx. 1.5–2 hours (9,000 mAh quick-release battery) | Public specification |
| Computing Platform | 8-core CPU; EDU version optional NVIDIA Jetson Orin | Public specification |
| Price | Approx. 16,000 USD / Starting at 99,000 RMB domestically | Media reports |

### Supply Chain Position

- **Manufacturer**: [Unitree Robotics](../companies/company_unitree.md)
- **Core Components/Technology Sources**: Self-developed joint motors and drivers, 3D LiDAR, Intel RealSense depth cameras, NVIDIA Jetson Orin (EDU version).
- **Downstream Applications/Customers**: Universities, educational institutions, developers, AI research, and commercial exhibitions.

### Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_unitree_g1`
- Manufacturer Entity: `ent_company_unitree`
- Key Relationship:
  - `rel_ent_company_unitree_manufactures_ent_product_unitree_g1` (`ent_company_unitree` → `manufactures` → `ent_product_unitree_g1`)

### Application Scenarios

- **Educational Demonstrations**: Used by universities, primary/secondary schools, and science museums for robotics courses, exhibitions, and competitions.
- **AI and Robotics Research**: Developer communities conduct experiments in imitation learning, reinforcement learning, and multimodal interaction.
- **Light Commercial Use**: Retail displays, guided tours, and small-scale logistics pilots.

### Competitive Comparison

| Comparison Item | Unitree G1 | Unitree H1 | Unitree R1 |
|-----------------|------------|------------|------------|
| Positioning | Compact development platform | Full-size high-dynamic platform | Entry-level development platform |
| Height | 127 cm | 180 cm | 121 cm |
| Price | Approx. 16,000 USD | Approx. 90,000 USD | Approx. 5,900 USD |
| Core Advantage | High cost-effectiveness, full features in EDU version | High-dynamic motion, large payload | Ultra-low barrier, developer-friendly |

### Purchase and Deployment Recommendations

- Educational/research institutions are advised to prioritize the G1 EDU version for SDK, ROS2, and Jetson Orin computing support.
- During deployment, ensure sufficient safe space in the venue and configure emergency stop devices and protective barriers.

### References

1. [Unitree G1 Product Page](https://www.unitree.com/g1)
2. [Robozaps – Unitree G1 Review](https://blog.robozaps.com/b/unitree-g1-review)
3. [Humanoid.Guide – Unitree G1](https://humanoid.guide/product/g1/)
4. [Humanoid Index – G1](https://humanoidindex.org/robots/g1)

## 개요
Unitree G1 휴머노이드 로봇은 휴머노이드 로봇 분야에서 중요한 로봇 시스템입니다. 다음 내용은 프로젝트 Wiki에서 정리한 것으로, 심층 참고용으로 제공됩니다.

## 핵심 내용
## 宇树 G1 / Unitree G1

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료 기준이며, 누락된 항목은 "미공개"로 표시됩니다.

---

### 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [宇树科技 / Unitree Robotics](../companies/company_unitree.md) |
| **제품 카테고리** | 컴팩트형 휴머노이드 로봇 |
| **출시일** | 2024년 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [Unitree G1 제품 페이지](https://www.unitree.com/g1) |

### 제품 개요

宇树 G1은 Unitree가 교육, 연구 및 개발자를 대상으로 출시한 컴팩트형 휴머노이드 로봇으로, 공격적인 가격 정책과 높은 접근성으로 유명합니다. G1의 키는 약 127cm, 무게는 약 35kg이며, 기본 버전은 23 자유도를 가지며, EDU 버전은 43 DOF로 확장 가능하고 Dex3-1 5손가락 정교한 손과 NVIDIA Jetson Orin 컴퓨팅 모듈을 탑재합니다.

G1은 3D LiDAR, 깊이 카메라 및 8코어 CPU(EDU 버전은 Jetson Orin 추가)를 사용하며, ROS2, Python/C++ SDK 및 OTA 업그레이드를 지원합니다. 접이식 디자인으로 운송 및 배치가 용이하여, 전 세계 출하량 선두를 달리는 휴머노이드 개발 플랫폼 중 하나입니다.

### 제품 이미지

> Unitree G1: [공식 자료](https://www.unitree.com/g1)를 방문하여 확인하세요.

### 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|-----------|------|-----------|
| 크기 | 약 127cm(높이) | 공개 사양 |
| 무게 | 약 35kg | 공개 사양 |
| 자유도(전체) | 23–43 DOF | 기본 버전/EDU 버전 구성 차이 |
| 주요 성능 지표 | 관절 최대 토크 90–120 N·m; 탑재 하중 약 2kg | 공개 사양 |
| 보행 속도 | 약 2m/s | 공개 사양 |
| 배터리 지속 시간 | 약 1.5–2시간(9,000mAh 퀵 릴리스 배터리) | 공개 사양 |
| 컴퓨팅 플랫폼 | 8코어 CPU; EDU 버전은 NVIDIA Jetson Orin 선택 가능 | 공개 사양 |
| 가격 | 약 16,000 USD / 국내 9.9만 위안부터 | 미디어 보도 |

### 공급망 위치

- **제조사**: [宇树科技 / Unitree Robotics](../companies/company_unitree.md)
- **핵심 부품/기술 출처**: 자체 개발 관절 모터 및 드라이버, 3D LiDAR, Intel RealSense 깊이 카메라, NVIDIA Jetson Orin(EDU 버전).
- **하류 응용/고객**: 대학, 교육 기관, 개발자, AI 연구 및 상업 전시.

### 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_unitree_g1`
- 제조사 엔터티: `ent_company_unitree`
- 주요 관계:
  - `rel_ent_company_unitree_manufactures_ent_product_unitree_g1`(`ent_company_unitree` → `manufactures` → `ent_product_unitree_g1`)

### 응용 시나리오

- **교육 시연**: 대학, 초중등학교 및 과학관에서 로봇 강의, 전시 및 경진대회에 사용.
- **AI 및 로봇 연구**: 개발자 커뮤니티에서 모방 학습, 강화 학습 및 다중 모드 상호작용 실험 수행.
- **경량 상업**: 소매 전시, 안내 접객 및 소규모 물류 시범 운영.

### 경쟁 비교

| 비교 항목 | Unitree G1 | Unitree H1 | Unitree R1 |
|-----------|------------|------------|------------|
| 포지셔닝 | 컴팩트형 개발 플랫폼 | 풀사이즈 고다이나믹 플랫폼 | 입문형 개발 플랫폼 |
| 키 | 127cm | 180cm | 121cm |
| 가격 | 약 16,000 USD | 약 90,000 USD | 약 5,900 USD |
| 핵심 장점 | 가성비 우수, EDU 버전 기능 완전 | 고다이나믹 운동, 큰 탑재 하중 | 초저가, 개발자 친화적 |

### 구매 및 배치 권장 사항

- 교육/연구 기관은 SDK, ROS2 및 Jetson Orin 컴퓨팅 지원을 위해 G1 EDU 버전을 우선 선택하는 것을 권장합니다.
- 배치 시 현장에 충분한 안전 공간을 확보하고, 비상 정지 장치 및 보호 펜스를 구성해야 합니다.

### 참고 자료

1. [Unitree G1 제품 페이지](https://www.unitree.com/g1)
2. [Robozaps – Unitree G1 Review](https://blog.robozaps.com/b/unitree-g1-review)
3. [Humanoid.Guide – Unitree G1](https://humanoid.guide/product/g1/)
4. [Humanoid Index – G1](https://humanoidindex.org/robots/g1)

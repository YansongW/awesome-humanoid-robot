---
$id: ent_robot_ubtech_walker_s_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: UBTECH Walker S
  zh: 优必选 Walker S
  ko: UBTECH Walker S
summary:
  en: Industrial humanoid robot for factory operations, featuring all-electric modular joints.
  zh: 概述 优必选 Walker S是人形机器人领域的重要robot_system。以下内容整理自项目 Wiki，供深入查阅。
  ko: 공장 작업용 산업용 휨로봇, 전기식 모듈형 관절 특징.
domains:
- 06_design_engineering
- 11_applications_markets
layers:
- midstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- industrial
- modular_joint
- robot_system
- ubtech
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/products/product_walker_s2.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: UBTECH Walker S
  url: https://www.ubtrobot.com/
  date: '2024'
  accessed_at: '2026-07-01'
---

## 概述
优必选 Walker S是人形机器人领域的重要机器人系统。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## 优必选 Walker S2 / UBTECH Walker S2

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [优必选 / UBTECH](../companies/company_ubtech.md) |
| **产品类别** | 工业级人形机器人 |
| **发布时间** | 2024–2025 年 |
| **状态** | 量产/企业交付 |
| **官网/来源** | [UBTECH 商用官网](https://www.commercial.ubtrobot.com/) |

### 产品概述

优必选 Walker S2 是 Walker 工业人形机器人系列的第二代产品，专为汽车制造、3C 电子与物流仓储场景设计。整机拥有 52 个自由度，双臂最大负载 15 kg，并配备第四代五指灵巧手与 ±162° 腰部旋转，能够完成拆箱、上料、质检、喷涂等复杂工业动作。

Walker S2 的核心亮点是自主电池热插拔系统，可在 3 分钟内完成电池更换，实现接近 24 小时连续作业。其感知系统包括双目立体视觉、深度 LiDAR、六轴力传感器与 IMU，搭载 ROSA 2.0 操作系统与多模态大模型，支持多机协同与 MES 系统对接。Walker S2 已在蔚来、比亚迪、空客等客户的产线或试点项目中部署验证。

### 产品图片

> UBTECH Walker S2：请访问 [官方资料](https://www.commercial.ubtrobot.com/) 查看。

### 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 176 cm（高） | 公开规格 |
| 重量 | 约 70–75 kg | 不同配置来源 |
| 自由度（整机） | 52 DOF | 公开规格 |
| 关键性能指标 | 双臂最大负载 15 kg；腰部旋转 ±162° | 公开规格 |
| 行走速度 | 约 2 m/s（7.2 km/h） | 公开规格 |
| 续航 | 约 2 小时；支持热插拔电池 | 公开规格 |
| 计算平台 | X86 + NVIDIA Jetson Orin | RBTX 产品页 |
| 价格 | 未公开（行业估计 68,000–120,000 USD） | 第三方估计 |

### 供应链位置

- **制造商**：[优必选 / UBTECH](../companies/company_ubtech.md)
- **核心零部件/技术来源**：自研一体化关节、NVIDIA Jetson Orin 计算平台、双目立体视觉、深度 LiDAR、灵巧手；部分减速器、电机外购。
- **下游应用/客户**：蔚来汽车、比亚迪、空客、沙特/新加坡/日本试点项目。

### 知识图谱节点与关系

- 产品实体：`ent_product_ubtech_walker_s2`
- 制造商实体：`ent_company_ubtech`
- 关键关系：
  - `rel_ent_company_ubtech_manufactures_ent_product_ubtech_walker_s2`（`ent_company_ubtech` → `manufactures` → `ent_product_ubtech_walker_s2`）

### 应用场景

- **汽车制造**：蔚来、比亚迪等工厂执行外观质检、内饰装配、安全带检测与物料搬运。
- **3C 电子**：精密装配、螺丝拧紧、元器件插装与 AOI 复检辅助。
- **商用展示**：展厅讲解、商超导览与品牌活动互动展示。

### 竞争对比

| 对比项 | 优必选 Walker S2 | Tesla Optimus Gen 3 | Figure 02 |
|--------|------------------|---------------------|-----------|
| 定位 | 工业人形 | 通用/工业人形 | 工业制造人形 |
| 整机 DOF | 52 | 28+ 躯干 + 22×2 手 | 28 |
| 双臂负载 | 15 kg | 约 20 kg | 25 kg |
| 核心优势 | 工厂部署案例、热插拔电池、灵巧手 | 成本目标、AI 数据 | Helix VLA、宝马部署 |

### 选购与部署建议

- 汽车/3C 制造企业应重点评估 Walker S2 与现有 MES/AGV 系统的对接能力。
- 建议规划电池热插拔站点与多机协同调度方案，以发挥 24 小时连续作业优势。

### 参考资料

1. [UBTECH 商用官网](https://www.commercial.ubtrobot.com/)
2. [Robozaps – UBTECH Walker S Review](https://blog.robozaps.com/b/ubtech-walker-s-review)
3. [Humanoid.Guide – Walker S2](https://humanoid.guide/product/walker-s2/)
4. [RBTX – UBTECH Walker S2 产品页](https://rbtx.com/en-US/components/humanoid/ubtech-humanoid-walker-s2)

## 参考
- [UBTECH Walker S](https://www.ubtrobot.com/)
- 项目 Wiki：appendix-d/products/product_walker_s2.md

## Overview
UBTECH Walker S is an important robotic system in the humanoid robot field. The following content is compiled from the project Wiki for in-depth reference.

## Content
## UBTECH Walker S2

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

### Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [UBTECH](../companies/company_ubtech.md) |
| **Product Category** | Industrial-grade humanoid robot |
| **Release Date** | 2024–2025 |
| **Status** | Mass production/Enterprise delivery |
| **Official Website/Source** | [UBTECH Commercial Official Website](https://www.commercial.ubtrobot.com/) |

### Product Overview

The UBTECH Walker S2 is the second-generation product of the Walker industrial humanoid robot series, designed for automotive manufacturing, 3C electronics, and logistics warehousing scenarios. The entire machine features 52 degrees of freedom, a maximum dual-arm payload of 15 kg, and is equipped with a fourth-generation five-finger dexterous hand and ±162° waist rotation, enabling complex industrial tasks such as unpacking, material loading, quality inspection, and spraying.

The core highlight of the Walker S2 is its autonomous battery hot-swap system, which can complete battery replacement within 3 minutes, enabling nearly 24-hour continuous operation. Its perception system includes binocular stereo vision, depth LiDAR, six-axis force sensors, and IMU, powered by the ROSA 2.0 operating system and multimodal large models, supporting multi-robot collaboration and MES system integration. The Walker S2 has been deployed and validated on production lines or in pilot projects at clients such as NIO, BYD, and Airbus.

### Product Image

> UBTECH Walker S2: Please visit the [official website](https://www.commercial.ubtrobot.com/) for details.

### Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Approx. 176 cm (height) | Public specification |
| Weight | Approx. 70–75 kg | Varies by configuration source |
| Degrees of Freedom (Total) | 52 DOF | Public specification |
| Key Performance Indicators | Max dual-arm payload 15 kg; waist rotation ±162° | Public specification |
| Walking Speed | Approx. 2 m/s (7.2 km/h) | Public specification |
| Battery Life | Approx. 2 hours; supports hot-swappable battery | Public specification |
| Computing Platform | X86 + NVIDIA Jetson Orin | RBTX product page |
| Price | Not disclosed (industry estimate 68,000–120,000 USD) | Third-party estimate |

### Supply Chain Position

- **Manufacturer**: [UBTECH](../companies/company_ubtech.md)
- **Core Components/Technology Sources**: Self-developed integrated joints, NVIDIA Jetson Orin computing platform, binocular stereo vision, depth LiDAR, dexterous hand; some reducers and motors are externally sourced.
- **Downstream Applications/Clients**: NIO, BYD, Airbus, pilot projects in Saudi Arabia, Singapore, and Japan.

### Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_ubtech_walker_s2`
- Manufacturer Entity: `ent_company_ubtech`
- Key Relationship:
  - `rel_ent_company_ubtech_manufactures_ent_product_ubtech_walker_s2` (`ent_company_ubtech` → `manufactures` → `ent_product_ubtech_walker_s2`)

### Application Scenarios

- **Automotive Manufacturing**: Performs appearance inspection, interior assembly, seatbelt detection, and material handling at factories like NIO and BYD.
- **3C Electronics**: Precision assembly, screw tightening, component insertion, and AOI re-inspection assistance.
- **Commercial Display**: Exhibition hall explanations, shopping mall tours, and brand event interactive displays.

### Competitive Comparison

| Comparison Item | UBTECH Walker S2 | Tesla Optimus Gen 3 | Figure 02 |
|-----------------|------------------|---------------------|-----------|
| Positioning | Industrial humanoid | General/Industrial humanoid | Industrial manufacturing humanoid |
| Total DOF | 52 | 28+ torso + 22×2 hands | 28 |
| Dual-arm Payload | 15 kg | Approx. 20 kg | 25 kg |
| Core Advantage | Factory deployment cases, hot-swappable battery, dexterous hand | Cost target, AI data | Helix VLA, BMW deployment |

### Selection and Deployment Recommendations

- Automotive/3C manufacturing companies should focus on evaluating the Walker S2's integration capabilities with existing MES/AGV systems.
- It is recommended to plan battery hot-swap stations and multi-robot collaborative scheduling solutions to leverage the advantage of 24-hour continuous operation.

### References

1. [UBTECH Commercial Official Website](https://www.commercial.ubtrobot.com/)
2. [Robozaps – UBTECH Walker S Review](https://blog.robozaps.com/b/ubtech-walker-s-review)
3. [Humanoid.Guide – Walker S2](https://humanoid.guide/product/walker-s2/)
4. [RBTX – UBTECH Walker S2 Product Page](https://rbtx.com/en-US/components/humanoid/ubtech-humanoid-walker-s2)

## 개요
UBTECH Walker S는 휴머노이드 로봇 분야의 중요한 로봇 시스템입니다. 다음 내용은 프로젝트 Wiki에서 정리한 것으로, 심층 참고용으로 제공됩니다.

## 핵심 내용
## UBTECH Walker S2

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료 기준이며, 누락된 항목은 "미공개"로 표시합니다.

---

### 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [UBTECH](../companies/company_ubtech.md) |
| **제품 카테고리** | 산업용 휴머노이드 로봇 |
| **출시 시기** | 2024–2025년 |
| **상태** | 양산/기업 납품 |
| **공식 홈페이지/출처** | [UBTECH 상업용 공식 사이트](https://www.commercial.ubtrobot.com/) |

### 제품 개요

UBTECH Walker S2는 Walker 산업용 휴머노이드 로봇 시리즈의 2세대 제품으로, 자동차 제조, 3C 전자제품 및 물류 창고 시나리오에 특화 설계되었습니다. 본체는 52개의 자유도를 가지며, 양팔 최대 하중 15kg, 4세대 5지 다용도 핸드와 ±162° 허리 회전 기능을 갖추어, 박스 개봉, 자재 투입, 품질 검사, 도장 등 복잡한 산업 작업을 수행할 수 있습니다.

Walker S2의 핵심 장점은 자체 배터리 핫스왑 시스템으로, 3분 이내에 배터리 교체가 가능하여 거의 24시간 연속 작업이 가능합니다. 감지 시스템에는 양안 입체 시각, 심층 LiDAR, 6축 힘 센서 및 IMU가 포함되며, ROSA 2.0 운영 체제와 멀티모달 대형 모델을 탑재하여 다중 로봇 협업 및 MES 시스템 연동을 지원합니다. Walker S2는 NIO, BYD, Airbus 등 고객사의 생산 라인 또는 시범 프로젝트에 배치되어 검증되었습니다.

### 제품 이미지

> UBTECH Walker S2: [공식 자료](https://www.commercial.ubtrobot.com/)를 방문하여 확인하세요.

### 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 약 176 cm (높이) | 공개 사양 |
| 무게 | 약 70–75 kg | 구성에 따라 상이 |
| 자유도 (본체) | 52 DOF | 공개 사양 |
| 주요 성능 지표 | 양팔 최대 하중 15kg; 허리 회전 ±162° | 공개 사양 |
| 보행 속도 | 약 2 m/s (7.2 km/h) | 공개 사양 |
| 배터리 지속 시간 | 약 2시간; 핫스왑 배터리 지원 | 공개 사양 |
| 컴퓨팅 플랫폼 | X86 + NVIDIA Jetson Orin | RBTX 제품 페이지 |
| 가격 | 미공개 (업계 추정 68,000–120,000 USD) | 제3자 추정 |

### 공급망 위치

- **제조사**: [UBTECH](../companies/company_ubtech.md)
- **핵심 부품/기술 출처**: 자체 개발 일체형 관절, NVIDIA Jetson Orin 컴퓨팅 플랫폼, 양안 입체 시각, 심층 LiDAR, 다용도 핸드; 일부 감속기, 모터는 외부 조달.
- **하류 응용/고객**: NIO, BYD, Airbus, 사우디아라비아/싱가포르/일본 시범 프로젝트.

### 지식 그래프 노드 및 관계

- 제품 엔티티: `ent_product_ubtech_walker_s2`
- 제조사 엔티티: `ent_company_ubtech`
- 주요 관계:
  - `rel_ent_company_ubtech_manufactures_ent_product_ubtech_walker_s2` (`ent_company_ubtech` → `manufactures` → `ent_product_ubtech_walker_s2`)

### 응용 시나리오

- **자동차 제조**: NIO, BYD 등 공장에서 외관 품질 검사, 내장 조립, 안전벨트 검사 및 자재 운반 수행.
- **3C 전자제품**: 정밀 조립, 나사 체결, 부품 삽입 및 AOI 재검사 보조.
- **상업용 전시**: 전시장 설명, 쇼핑몰 안내 및 브랜드 활동 인터랙티브 전시.

### 경쟁 비교

| 비교 항목 | UBTECH Walker S2 | Tesla Optimus Gen 3 | Figure 02 |
|--------|------------------|---------------------|-----------|
| 포지셔닝 | 산업용 휴머노이드 | 범용/산업용 휴머노이드 | 산업 제조 휴머노이드 |
| 본체 DOF | 52 | 28+ 몸통 + 22×2 손 | 28 |
| 양팔 하중 | 15 kg | 약 20 kg | 25 kg |
| 핵심 장점 | 공장 배치 사례, 핫스왑 배터리, 다용도 핸드 | 비용 목표, AI 데이터 | Helix VLA, BMW 배치 |

### 구매 및 배치 권장 사항

- 자동차/3C 제조 기업은 Walker S2와 기존 MES/AGV 시스템의 연동 능력을 중점 평가해야 합니다.
- 배터리 핫스왑 스테이션 및 다중 로봇 협업 스케줄링 방안을 계획하여 24시간 연속 작업 이점을 활용하는 것이 좋습니다.

### 참고 자료

1. [UBTECH 상업용 공식 사이트](https://www.commercial.ubtrobot.com/)
2. [Robozaps – UBTECH Walker S 리뷰](https://blog.robozaps.com/b/ubtech-walker-s-review)
3. [Humanoid.Guide – Walker S2](https://humanoid.guide/product/walker-s2/)
4. [RBTX – UBTECH Walker S2 제품 페이지](https://rbtx.com/en-US/components/humanoid/ubtech-humanoid-walker-s2)

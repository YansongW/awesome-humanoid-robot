---
$id: ent_robot_system_tesla_optimus
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: Tesla Optimus
  zh: Tesla Optimus
  ko: 테슬라 옵티머스
summary:
  en: Tesla's general-purpose humanoid robot program, with stated goals of factory deployment and high-volume manufacturing.
  zh: 概述 Tesla Optimus是人形机器人领域的重要robot_system。以下内容整理自项目 Wiki，供深入查阅。
  ko: 테슬라의 범용 휴인oid 로봇 프로그램으로, 공장 배치와 대량 생산을 목표로 합니다.
domains:
- 05_mass_production
- 06_design_engineering
- 11_applications_markets
layers:
- midstream
- validation_markets
functional_roles:
- system
- knowledge
tags:
- tesla
- optimus
- humanoid
- robot_system
- factory
- manufacturing
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/products/product_optimus_gen3.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Tesla Optimus Official Page
  url: https://www.tesla.com/optimus
  date: '2026'
  accessed_at: '2026-06-24'
- id: src_002
  type: report
  title: Interact Analysis — Humanoid Robots and Lithium-Ion Batteries
  url: https://interactanalysis.com/insight/humanoid-robots-and-lithium-ion-batteries/
  date: '2026'
  accessed_at: '2026-06-24'
theoretical_depth:
- system
---

## 概述
Tesla Optimus是人形机器人领域的重要机器人系统。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## Tesla Optimus Gen 3 / 特斯拉 Optimus Gen 3

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [特斯拉 / Tesla](../companies/company_tesla.md) |
| **产品类别** | 通用人形机器人 |
| **发布时间** | Gen 3 手部于 2024 年底公开；2026 年推进整机体量产 |
| **状态** | 内部量产/工厂部署 |
| **官网/来源** | [Tesla 官网](https://www.tesla.com) |

### 产品概述

Tesla Optimus Gen 3 是特斯拉人形机器人平台的最新迭代，重点升级了手部自由度与整机电驱集成度。Gen 3 在 Gen 2 的 173 cm 躯干基础上，将单手自由度从 11 DOF 提升至 22 DOF，单只手搭载 25 个执行器，双手共 50 个执行器，显著增强了精细抓取与工具操作能力。

Optimus Gen 3 依托特斯拉自研的 FSD 视觉神经网络、车载级电池包与执行器技术，目标场景覆盖特斯拉工厂内部的电池分拣、物料搬运，并长期面向消费级市场。马斯克在公开表态中提出目标零售价 20,000–30,000 美元，但截至 2026 年该价格仍属于目标规划，未正式对外销售。

### 产品图片

> Tesla Optimus Gen 3：请访问 [官方资料](https://www.tesla.com) 查看。

### 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 尺寸 | 约 173 cm（高） | Tesla AI Day 公开资料 |
| 重量 | 约 57 kg（Gen 2 躯干基准） | 公开资料；Gen 3 完整体重未公开 |
| 自由度（整机） | 躯干 28+；手部 22×2 | Gen 3 手部升级 |
| 关键性能指标 | 双手搬运约 20 kg；手部 50 执行器 | 公开演示/媒体汇编 |
| 行走速度 | 约 8 km/h（目标） | 第三方评测 |
| 续航 | 约 2–4 小时（视任务） | 未官方确认 |
| 功耗 | 未公开 | - |
| 价格 | 目标零售价 20,000–30,000 USD | Musk 公开表态 |

### 供应链位置

- **制造商**：[特斯拉 / Tesla](../companies/company_tesla.md)
- **核心零部件/技术来源**：自研线性/旋转执行器、FSD 视觉感知、电池包与电源管理、车载级计算平台；部分结构件外协。
- **下游应用/客户**：特斯拉自有工厂（电池分拣、物料搬运），未来面向企业级与消费级市场。

### 知识图谱节点与关系

- 产品实体：`ent_product_tesla_optimus_gen3`
- 制造商实体：`ent_company_tesla`
- 关键关系：
  - `rel_ent_company_tesla_manufactures_ent_product_tesla_optimus_gen3`（`ent_company_tesla` → `manufactures` → `ent_product_tesla_optimus_gen3`）

### 应用场景

- **汽车制造**：在特斯拉工厂执行电池单元分拣、物料搬运、箱体码垛与产线巡检。
- **通用工业**：替代重复性、高强度或存在安全隐患的人工作业，如搬运、装配辅助。
- **未来消费/服务**：家庭清洁、个人助理与照护服务（仍处于长期规划阶段）。

### 竞争对比

| 对比项 | Tesla Optimus Gen 3 | Figure 02 | Boston Dynamics Atlas |
|--------|---------------------|-----------|-----------------------|
| 定位 | 通用/工业人形 | 工业制造人形 | 重载工业人形 |
| 手部 DOF | 22×2 | 16（双手） | 未公开 |
| 价格方向 | 目标 20,000–30,000 USD | 未公开 | 未公开（预估高端） |
| 核心优势 | 规模化制造目标、FSD 视觉、自研执行器 | Helix VLA 模型、宝马部署 | 56 DOF、50 kg 负载、运动能力 |

### 选购与部署建议

- 目前 Optimus Gen 3 仅面向特斯拉内部及特定企业试点，消费级销售尚未开放。
- 企业客户若关注人形机器人替代方案，建议同步评估 Figure 02、Digit 等已部署平台。

### 参考资料

1. [Tesla 官网](https://www.tesla.com)
2. [Tesla AI Day 公开演示](https://www.tesla.com/AI)
3. [Robozaps – Tesla Optimus Gen 3 Specs](https://blog.robozaps.com/b/tesla-optimus-gen-3)
4. [Optimusk – Tesla Optimus Capabilities 2025-2026](https://optimusk.blog/blog/tesla-optimus-capabilities/)

## 参考
- [Tesla Optimus Official Page](https://www.tesla.com/optimus)
- [Interact Analysis — Humanoid Robots and Lithium-Ion Batteries](https://interactanalysis.com/insight/humanoid-robots-and-lithium-ion-batteries/)
- 项目 Wiki：appendix-d/products/product_optimus_gen3.md

## Overview
Tesla Optimus is a significant robotic system in the field of humanoid robotics. The following content is compiled from the project Wiki for in-depth reference.

## Content
## Tesla Optimus Gen 3

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

### Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Tesla](../companies/company_tesla.md) |
| **Product Category** | General-purpose humanoid robot |
| **Release Date** | Gen 3 hand disclosed in late 2024; mass production of the full robot advanced in 2026 |
| **Status** | In-house mass production / factory deployment |
| **Official Website/Source** | [Tesla Official Website](https://www.tesla.com) |

### Product Overview

Tesla Optimus Gen 3 is the latest iteration of Tesla's humanoid robot platform, with key upgrades in hand degrees of freedom and overall electromechanical integration. Building on the Gen 2 torso height of 173 cm, Gen 3 increases single-hand degrees of freedom from 11 DOF to 22 DOF, with 25 actuators per hand and 50 actuators for both hands combined, significantly enhancing fine grasping and tool manipulation capabilities.

Optimus Gen 3 leverages Tesla's self-developed FSD visual neural network, automotive-grade battery pack, and actuator technology. Target scenarios cover battery sorting and material handling within Tesla's factories, with a long-term vision for the consumer market. Elon Musk has publicly stated a target retail price of $20,000–$30,000, but as of 2026, this remains a goal and the robot has not been officially sold externally.

### Product Image

> Tesla Optimus Gen 3: Please visit [Official Information](https://www.tesla.com) for details.

### Specification Table

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Approx. 173 cm (height) | Tesla AI Day public data |
| Weight | Approx. 57 kg (Gen 2 torso baseline) | Public data; Gen 3 full weight not disclosed |
| Degrees of Freedom (Full Body) | Torso 28+; Hands 22×2 | Gen 3 hand upgrade |
| Key Performance Indicators | Dual-hand carrying approx. 20 kg; 50 hand actuators | Public demo / media compilation |
| Walking Speed | Approx. 8 km/h (target) | Third-party evaluation |
| Battery Life | Approx. 2–4 hours (task-dependent) | Not officially confirmed |
| Power Consumption | Not disclosed | - |
| Price | Target retail price $20,000–$30,000 USD | Musk's public statement |

### Supply Chain Position

- **Manufacturer**: [Tesla](../companies/company_tesla.md)
- **Core Components/Technology Sources**: Self-developed linear/rotary actuators, FSD visual perception, battery pack and power management, automotive-grade computing platform; some structural components outsourced.
- **Downstream Applications/Customers**: Tesla's own factories (battery sorting, material handling); future enterprise and consumer markets.

### Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_tesla_optimus_gen3`
- Manufacturer Entity: `ent_company_tesla`
- Key Relationship:
  - `rel_ent_company_tesla_manufactures_ent_product_tesla_optimus_gen3` (`ent_company_tesla` → `manufactures` → `ent_product_tesla_optimus_gen3`)

### Application Scenarios

- **Automotive Manufacturing**: Performs battery cell sorting, material handling, box palletizing, and production line inspection in Tesla factories.
- **General Industry**: Replaces repetitive, high-intensity, or hazardous manual tasks such as handling and assembly assistance.
- **Future Consumer/Service**: Home cleaning, personal assistant, and care services (still in long-term planning stage).

### Competitive Comparison

| Comparison Item | Tesla Optimus Gen 3 | Figure 02 | Boston Dynamics Atlas |
|-----------------|---------------------|-----------|-----------------------|
| Positioning | General-purpose/industrial humanoid | Industrial manufacturing humanoid | Heavy-duty industrial humanoid |
| Hand DOF | 22×2 | 16 (both hands) | Not disclosed |
| Price Direction | Target $20,000–$30,000 USD | Not disclosed | Not disclosed (estimated high-end) |
| Core Advantages | Mass production target, FSD vision, self-developed actuators | Helix VLA model, BMW deployment | 56 DOF, 50 kg payload, locomotion capability |

### Selection and Deployment Recommendations

- Currently, Optimus Gen 3 is only available for internal Tesla use and select enterprise pilots; consumer sales are not yet open.
- Enterprise customers interested in humanoid robot alternatives should also evaluate deployed platforms such as Figure 02 and Digit.

### References

1. [Tesla Official Website](https://www.tesla.com)
2. [Tesla AI Day Public Demo](https://www.tesla.com/AI)
3. [Robozaps – Tesla Optimus Gen 3 Specs](https://blog.robozaps.com/b/tesla-optimus-gen-3)
4. [Optimusk – Tesla Optimus Capabilities 2025-2026](https://optimusk.blog/blog/tesla-optimus-capabilities/)

## 개요
Tesla Optimus는 휴머노이드 로봇 분야의 중요한 로봇 시스템입니다. 아래 내용은 프로젝트 Wiki에서 정리한 것으로, 심층 참고용으로 제공됩니다.

## 핵심 내용
## Tesla Optimus Gen 3 / 테슬라 옵티머스 Gen 3

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시점: 2026-07-01. 모든 파라미터는 공식 공개 자료 기준이며, 누락된 항목은 "미공개"로 표기합니다.

---

### 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [테슬라 / Tesla](../companies/company_tesla.md) |
| **제품 카테고리** | 범용 휴머노이드 로봇 |
| **출시 시점** | Gen 3 손은 2024년 말 공개; 2026년 본체 양산 추진 |
| **상태** | 내부 양산/공장 배치 |
| **공식 사이트/출처** | [Tesla 공식 사이트](https://www.tesla.com) |

### 제품 개요

Tesla Optimus Gen 3는 테슬라 휴머노이드 로봇 플랫폼의 최신 버전으로, 손의 자유도와 본체 전기 구동 통합도를 중점적으로 업그레이드했습니다. Gen 3는 Gen 2의 173cm 본체를 기반으로, 한 손의 자유도를 11 DOF에서 22 DOF로 향상시켰으며, 한 손에 25개의 액추에이터를 탑재하여 양손 합계 50개의 액추에이터를 갖추어 정밀한 파지와 도구 조작 능력을 크게 강화했습니다.

Optimus Gen 3는 테슬라 자체 개발 FSD 시각 신경망, 차량 탑재형 배터리 팩 및 액추에이터 기술을 기반으로 하며, 목표 시나리오는 테슬라 공장 내 배터리 분류, 자재 운반을 포함하며, 장기적으로는 소비자 시장을 지향합니다. 머스크는 공개 발언에서 목표 소매 가격을 20,000~30,000달러로 제시했지만, 2026년 현재 이 가격은 여전히 목표 계획에 불과하며 공식적으로 판매되지는 않았습니다.

### 제품 이미지

> Tesla Optimus Gen 3: [공식 자료](https://www.tesla.com)를 방문하여 확인하세요.

### 사양 파라미터 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 약 173cm (높이) | Tesla AI Day 공개 자료 |
| 무게 | 약 57kg (Gen 2 본체 기준) | 공개 자료; Gen 3 완전체 무게는 미공개 |
| 자유도 (전체) | 본체 28+; 손 22×2 | Gen 3 손 업그레이드 |
| 주요 성능 지표 | 양손 운반 약 20kg; 손 50 액추에이터 | 공개 시연/미디어 종합 |
| 보행 속도 | 약 8km/h (목표) | 서드파티 평가 |
| 배터리 지속 시간 | 약 2~4시간 (작업에 따라 다름) | 공식 확인되지 않음 |
| 소비 전력 | 미공개 | - |
| 가격 | 목표 소매가 20,000~30,000 USD | 머스크 공개 발언 |

### 공급망 위치

- **제조사**: [테슬라 / Tesla](../companies/company_tesla.md)
- **핵심 부품/기술 출처**: 자체 개발 선형/회전 액추에이터, FSD 시각 인식, 배터리 팩 및 전원 관리, 차량 탑재형 컴퓨팅 플랫폼; 일부 구조 부품은 외주.
- **하류 응용/고객**: 테슬라 자체 공장 (배터리 분류, 자재 운반), 향후 기업 및 소비자 시장 대상.

### 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_tesla_optimus_gen3`
- 제조사 엔터티: `ent_company_tesla`
- 주요 관계:
  - `rel_ent_company_tesla_manufactures_ent_product_tesla_optimus_gen3` (`ent_company_tesla` → `manufactures` → `ent_product_tesla_optimus_gen3`)

### 응용 시나리오

- **자동차 제조**: 테슬라 공장에서 배터리 셀 분류, 자재 운반, 상자 팔레타이징 및 생산 라인 순찰 수행.
- **범용 산업**: 반복적, 고강도 또는 안전 위험이 있는 수작업 대체 (예: 운반, 조립 보조).
- **미래 소비자/서비스**: 가사 청소, 개인 비서 및 돌봄 서비스 (아직 장기 계획 단계).

### 경쟁 비교

| 비교 항목 | Tesla Optimus Gen 3 | Figure 02 | Boston Dynamics Atlas |
|--------|---------------------|-----------|-----------------------|
| 포지셔닝 | 범용/산업 휴머노이드 | 산업 제조 휴머노이드 | 중하중 산업 휴머노이드 |
| 손 DOF | 22×2 | 16 (양손) | 미공개 |
| 가격 방향 | 목표 20,000~30,000 USD | 미공개 | 미공개 (고가 추정) |
| 핵심 강점 | 대량 생산 목표, FSD 시각, 자체 액추에이터 | Helix VLA 모델, BMW 배치 | 56 DOF, 50kg 부하, 운동 능력 |

### 구매 및 배치 권장 사항

- 현재 Optimus Gen 3는 테슬라 내부 및 특정 기업 시범 운영에만 제공되며, 소비자 판매는 아직 개방되지 않았습니다.
- 기업 고객이 휴머노이드 로봇 대체 솔루션을 고려한다면, Figure 02, Digit 등 이미 배치된 플랫폼도 함께 평가하는 것이 좋습니다.

### 참고 자료

1. [Tesla 공식 사이트](https://www.tesla.com)
2. [Tesla AI Day 공개 시연](https://www.tesla.com/AI)
3. [Robozaps – Tesla Optimus Gen 3 Specs](https://blog.robozaps.com/b/tesla-optimus-gen-3)
4. [Optimusk – Tesla Optimus Capabilities 2025-2026](https://optimusk.blog/blog/tesla-optimus-capabilities/)

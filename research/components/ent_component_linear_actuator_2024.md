---
$id: ent_component_linear_actuator_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: Linear Actuator
  zh: 线性执行器
  ko: Linear Actuator
summary:
  en: Actuator producing linear motion, typically composed of frameless torque motor, planetary roller screw, encoder and
    force sensor.
  zh: 滚珠/梯形丝杠线性执行器 / Dingzhi Lead Screw / Ball Screw Actuator
  ko: 선형 운 동을 생성하는 액추에이터, 일반적으로 프레임리스 토크 모터, 행성 롤러 스크류, 인코더 및 힘 센서로 구성.
domains:
- 02_components
layers:
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- component
- linear_actuator
- linear_motion
- planetary_roller_screw
- torque_motor
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/products/product_dingzhi_lead_screw.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Linear Actuator
  url: https://en.wikipedia.org/wiki/Linear_actuator
  date: '2024'
  accessed_at: '2026-07-01'
---

## 概述
线性执行器是人形机器人领域的重要零部件。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## 滚珠/梯形丝杠线性执行器 / Dingzhi Lead Screw / Ball Screw Actuator

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [鼎智科技 / Dingzhi Technology](../companies/company_dingzhi.md) |
| **产品类别** | 步进电机 |
| **发布时间** | 现役主力型号 |
| **状态** | 量产/商用 |
| **官网/来源** | [鼎智科技官网](https://www.dingzhimotion.com) |

### 产品概述

一体化步进/伺服电机+丝杠，结构紧凑、自锁性好，适合机器人线性关节与精密推杆。该系列产品由鼎智科技推出，主要面向步进电机 / 线性执行器 / 丝杠 / 关节模组市场，具有10–300 mm（依定制）等核心参数，适用于机器人、自动化设备及精密传动场景。

作为鼎智科技的代表产品之一，滚珠/梯形丝杠线性执行器在医疗、3D 打印、机器人等领域具有广泛应用。产品采用成熟制造工艺，可根据客户需求提供定制化接口、出线方式与控制协议。

### 产品图片

> 滚珠/梯形丝杠线性执行器：请访问 [官方资料](https://www.dingzhimotion.com) 查看。

### 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 丝杠直径 | Ø3–Ø12 mm | 产品手册 |
| 导程 | 1–20 mm | 产品手册 |
| 行程 | 10–300 mm（依定制） | 产品手册 |
| 最大负载 | 500 N | 产品手册 |
| 定位精度 | ±0.02 mm | 产品手册 |
| 重复定位精度 | ±0.01 mm | 产品手册 |
| 传动方式 | 梯形丝杠 / 滚珠丝杠 | 产品手册 |
| 价格 | 未公开 | - |

### 供应链位置

- **制造商**：[鼎智科技 / Dingzhi Technology](../companies/company_dingzhi.md)
- **核心零部件/技术来源**：硅钢片、铜线、磁材、轴承、丝杠钢材、塑料粒子、电子元器件。
- **下游应用/客户**：医疗器械、3D 打印、人形机器人、工业自动化、汽车电子。

### 知识图谱节点与关系

- 零部件实体：`ent_component_dingzhi_lead_screw`
- 制造商实体：`ent_company_dingzhi`
- 关键关系：
  - `rel_ent_company_dingzhi_manufactures_ent_component_dingzhi_lead_screw`（`ent_company_dingzhi` --> `manufactures` --> `ent_component_dingzhi_lead_screw`）

### 应用场景

- **机器人**：人形机器人线性关节、灵巧手驱动、医疗床/注射泵、3D 打印机、光学平台。
- **工业自动化**：精密定位、传动与控制执行机构。
- **医疗与消费电子**：便携式设备、医疗器械驱动单元。
- **新能源与汽车**：电动执行器、热管理与智能座舱部件。

### 竞争对比

| 对比项 | 本产品 | 国际品牌 | 国内对标 |
|--------|--------|----------|----------|
| 核心优势 | 本土化供应、性价比、定制化 | 高端精度与可靠性 | 同区间性能竞争 |
| 交付周期 | 较短 | 较长 | 较短 |
| 服务响应 | 快速 | 中等 | 快速 |
| 价格水平 | 中低端至中高端 | 高端 | 中低端 |

### 选购与部署建议

- 选型时应根据负载、行程、速度与精度要求匹配合适型号，必要时联系厂商获取定制方案。
- 部署前建议进行负载惯量辨识、刚性匹配与振动抑制调试，确保与整机系统兼容。

### 参考资料

1. [鼎智科技官网](https://www.dingzhimotion.com)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.inovance.com)（请按实际产品型号核对）

## 参考
- [Linear Actuator](https://en.wikipedia.org/wiki/Linear_actuator)
- 项目 Wiki：appendix-d/products/product_dingzhi_lead_screw.md

## Overview
Linear actuators are critical components in the humanoid robotics field. The following content is compiled from the project Wiki for in-depth reference.

## Content
## Ball/Trapezoidal Lead Screw Linear Actuator / Dingzhi Lead Screw / Ball Screw Actuator

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

### Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Dingzhi Technology](../companies/company_dingzhi.md) |
| **Product Category** | Stepper Motor |
| **Release Date** | Current Main Model |
| **Status** | Mass Production / Commercial |
| **Official Website/Source** | [Dingzhi Technology Official Website](https://www.dingzhimotion.com) |

### Product Overview

Integrated stepper/servo motor with lead screw, compact structure, good self-locking capability, suitable for robotic linear joints and precision push rods. This series is launched by Dingzhi Technology, targeting the stepper motor / linear actuator / lead screw / joint module market, with core parameters such as 10–300 mm (customizable), applicable to robotics, automation equipment, and precision transmission scenarios.

As one of Dingzhi Technology's representative products, the ball/trapezoidal lead screw linear actuator is widely used in medical, 3D printing, and robotics fields. The product adopts mature manufacturing processes and offers customizable interfaces, wiring methods, and control protocols based on customer requirements.

### Product Image

> Ball/Trapezoidal Lead Screw Linear Actuator: Please visit [Official Materials](https://www.dingzhimotion.com) for details.

### Specification Table

| Specification Item | Value | Remarks/Source |
|--------------------|-------|----------------|
| Screw Diameter | Ø3–Ø12 mm | Product Manual |
| Lead | 1–20 mm | Product Manual |
| Stroke | 10–300 mm (customizable) | Product Manual |
| Maximum Load | 500 N | Product Manual |
| Positioning Accuracy | ±0.02 mm | Product Manual |
| Repeat Positioning Accuracy | ±0.01 mm | Product Manual |
| Transmission Method | Trapezoidal Lead Screw / Ball Screw | Product Manual |
| Price | Not disclosed | - |

### Supply Chain Position

- **Manufacturer**: [Dingzhi Technology](../companies/company_dingzhi.md)
- **Core Components/Technology Sources**: Silicon steel sheets, copper wire, magnetic materials, bearings, screw steel, plastic particles, electronic components.
- **Downstream Applications/Customers**: Medical devices, 3D printing, humanoid robots, industrial automation, automotive electronics.

### Knowledge Graph Nodes and Relationships

- Component Entity: `ent_component_dingzhi_lead_screw`
- Manufacturer Entity: `ent_company_dingzhi`
- Key Relationships:
  - `rel_ent_company_dingzhi_manufactures_ent_component_dingzhi_lead_screw` (`ent_company_dingzhi` --> `manufactures` --> `ent_component_dingzhi_lead_screw`)

### Application Scenarios

- **Robotics**: Humanoid robot linear joints, dexterous hand actuation, medical beds/infusion pumps, 3D printers, optical platforms.
- **Industrial Automation**: Precision positioning, transmission, and control actuators.
- **Medical and Consumer Electronics**: Portable devices, medical device drive units.
- **New Energy and Automotive**: Electric actuators, thermal management, and smart cockpit components.

### Competitive Comparison

| Comparison Item | This Product | International Brands | Domestic Counterparts |
|-----------------|--------------|----------------------|------------------------|
| Core Advantage | Local supply, cost-effectiveness, customization | High-end precision and reliability | Performance competition in the same range |
| Delivery Cycle | Shorter | Longer | Shorter |
| Service Response | Fast | Medium | Fast |
| Price Level | Low-end to Mid-high-end | High-end | Low-end |

### Selection and Deployment Recommendations

- When selecting, match the appropriate model based on load, stroke, speed, and accuracy requirements; contact the manufacturer for customized solutions if necessary.
- Before deployment, perform load inertia identification, stiffness matching, and vibration suppression debugging to ensure compatibility with the overall system.

### References

1. [Dingzhi Technology Official Website](https://www.dingzhimotion.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.inovance.com) (Please verify against actual product models)

## 개요
리니어 액추에이터는 휴머노이드 로봇 분야의 중요한 부품입니다. 다음 내용은 프로젝트 Wiki에서 정리한 것으로, 심층적인 참고를 위해 제공됩니다.

## 핵심 내용
## 볼/사다리꼴 리드 스크류 리니어 액추에이터 / Dingzhi Lead Screw / Ball Screw Actuator

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

### 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [鼎智科技 / Dingzhi Technology](../companies/company_dingzhi.md) |
| **제품 카테고리** | 스테핑 모터 |
| **출시 시기** | 현역 주력 모델 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [鼎智科技 공식 홈페이지](https://www.dingzhimotion.com) |

### 제품 개요

일체형 스테핑/서보 모터 + 리드 스크류로, 구조가 콤팩트하고 자체 잠금 성능이 우수하여 로봇의 선형 관절 및 정밀 푸시 로드에 적합합니다. 이 시리즈 제품은 鼎智科技에서 출시했으며, 주로 스테핑 모터 / 리니어 액추에이터 / 리드 스크류 / 관절 모듈 시장을 대상으로 합니다. 10–300 mm (주문 제작 가능) 등의 핵심 매개변수를 갖추고 있으며, 로봇, 자동화 장비 및 정밀 동력 전달 시나리오에 적용됩니다.

鼎智科技의 대표 제품 중 하나인 볼/사다리꼴 리드 스크류 리니어 액추에이터는 의료, 3D 프린팅, 로봇 등 다양한 분야에서 널리 사용됩니다. 제품은 성숙한 제조 공정을 채택하고 있으며, 고객 요구에 따라 맞춤형 인터페이스, 케이블 출력 방식 및 제어 프로토콜을 제공할 수 있습니다.

### 제품 이미지

> 볼/사다리꼴 리드 스크류 리니어 액추에이터: [공식 자료](https://www.dingzhimotion.com)를 방문하여 확인하세요.

### 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 리드 스크류 직경 | Ø3–Ø12 mm | 제품 매뉴얼 |
| 리드 | 1–20 mm | 제품 매뉴얼 |
| 스트로크 | 10–300 mm (주문 제작 가능) | 제품 매뉴얼 |
| 최대 하중 | 500 N | 제품 매뉴얼 |
| 위치 정밀도 | ±0.02 mm | 제품 매뉴얼 |
| 반복 위치 정밀도 | ±0.01 mm | 제품 매뉴얼 |
| 동력 전달 방식 | 사다리꼴 리드 스크류 / 볼 리드 스크류 | 제품 매뉴얼 |
| 가격 | 미공개 | - |

### 공급망 위치

- **제조사**: [鼎智科技 / Dingzhi Technology](../companies/company_dingzhi.md)
- **핵심 부품/기술 출처**: 규소강판, 구리선, 자성 재료, 베어링, 리드 스크류 강재, 플라스틱 입자, 전자 부품.
- **하류 응용/고객**: 의료 기기, 3D 프린팅, 휴머노이드 로봇, 산업 자동화, 자동차 전자.

### 지식 그래프 노드 및 관계

- 부품 엔터티: `ent_component_dingzhi_lead_screw`
- 제조사 엔터티: `ent_company_dingzhi`
- 주요 관계:
  - `rel_ent_company_dingzhi_manufactures_ent_component_dingzhi_lead_screw` (`ent_company_dingzhi` --> `manufactures` --> `ent_component_dingzhi_lead_screw`)

### 응용 시나리오

- **로봇**: 휴머노이드 로봇 선형 관절, 정교한 손 구동, 의료용 침대/주입 펌프, 3D 프린터, 광학 플랫폼.
- **산업 자동화**: 정밀 위치 결정, 동력 전달 및 제어 액추에이터.
- **의료 및 소비자 전자**: 휴대용 장치, 의료 기기 구동 유닛.
- **신에너지 및 자동차**: 전동 액추에이터, 열 관리 및 스마트 캐빈 부품.

### 경쟁 비교

| 비교 항목 | 본 제품 | 국제 브랜드 | 국내 대응 제품 |
|--------|--------|----------|----------|
| 핵심 장점 | 현지화 공급, 가성비, 맞춤화 | 고급 정밀도 및 신뢰성 | 동일 구간 성능 경쟁 |
| 납기 | 짧음 | 김 | 짧음 |
| 서비스 응답 | 빠름 | 보통 | 빠름 |
| 가격 수준 | 중저가 ~ 중고가 | 고가 | 중저가 |

### 선정 및 배치 권장 사항

- 선정 시 하중, 스트로크, 속도 및 정밀도 요구 사항에 따라 적합한 모델을 매칭해야 하며, 필요 시 제조사에 문의하여 맞춤형 솔루션을 받으십시오.
- 배치 전 부하 관성 식별, 강성 매칭 및 진동 억제 튜닝을 수행하여 전체 시스템과의 호환성을 보장하는 것이 좋습니다.

### 참고 자료

1. [鼎智科技 공식 홈페이지](https://www.dingzhimotion.com)
2. [WAIC 2026 전시 보도](https://www.worldrobotconference.com)
3. [공개 제품 매뉴얼 및 연구 보고서](https://www.inovance.com) (실제 제품 모델에 따라 확인하세요)

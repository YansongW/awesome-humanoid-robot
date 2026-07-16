---
$id: ent_company_wittenstein_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component_manufacturer
names:
  en: Wittenstein
  zh: Wittenstein
  ko: Wittenstein
summary:
  en: German manufacturer of precision gearboxes and servo actuators for robotics and automation.
  zh: Wittenstein是人形机器人领域的重要component_manufacturer。以下内容整理自项目 Wiki，供深入查阅。
  ko: 로보틱스 및 자동화용 정밀 기어박스 및 서보 액추에이터 독일 제조업체.
domains:
- 02_components
- 03_manufacturing_processes
layers:
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- component_manufactur
- component_manufacturer
- gearbox
- germany
- servo_actuator
- wittenstein
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/products/product_wittenstein_sp_plus.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Wittenstein
  url: https://www.wittenstein.de/
  date: '2024'
  accessed_at: '2026-07-01'
---


## 概述
Wittenstein是人形机器人领域的重要零部件_manufacturer。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## WITTENSTEIN alpha SP+ 行星减速器 / WITTENSTEIN alpha SP+ Planetary Gearbox

> 本词条属于 [附录 D 重点产品 Wiki](../../appendix-d.md)。
> 返回：[附录 D.4 重点产品 Wiki 目录](../index-products.md)
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 产品信息卡

| 项目 | 内容 |
|------|------|
| **制造商** | [威腾斯坦 / WITTENSTEIN alpha](../companies/company_wittenstein.md) |
| **产品类别** | 行星减速器 / 伺服减速器 |
| **发布时间** | 现役主力型号 |
| **状态** | 量产/商用 |
| **官网/来源** | [威腾斯坦 官网](https://www.wittenstein.de) |

### 产品概述

SP+ 是 WITTENSTEIN alpha 经典的低背隙行星减速器系列，专为高定位精度与循环动态应用设计。采用螺旋行星齿轮、预紧圆锥滚子轴承和模块化电机接口，可提供从 48 N·m 到 5,700 N·m 的加速扭矩范围。

该系列提供标准（MF）版本，减速比 3–100，7 种尺寸，可选降低背隙版本。SP+ HIGH SPEED 与 MC-L 低摩擦版本进一步覆盖连续运行与高速场景，是机床、机器人与自动化产线的核心传动部件。

### 产品图片

> WITTENSTEIN alpha SP+ 行星减速器 / WITTENSTEIN alpha SP+ Planetary Gearbox：请访问 [官方资料](https://www.wittenstein.de) 查看。

### 规格参数表

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 减速比 | 3:1 – 100:1 | 产品手册 |
| 框号/尺寸 | 7 种尺寸（MF） | 产品手册 |
| 最大输出扭矩 | 48 – 5,700 N·m | 产品手册 |
| 最大输入转速 | 最高 8,500 rpm | 产品手册 |
| 背隙 | 标准 ≤3 arcmin / 降低 ≤1 arcmin | 产品手册 |
| 扭转刚度 | 550 N·m/arcmin | 产品手册 |
| 最大倾覆力矩 | 5,000 N·m | 产品手册 |
| 价格 | 未公开 | - |

### 供应链位置

- **制造商**：[威腾斯坦 / WITTENSTEIN alpha](../companies/company_wittenstein.md)
- **核心零部件/技术来源**：高强度合金钢齿轮、精密轴承、密封件、润滑脂、电机适配法兰
- **下游应用/客户**：工业机器人、人形机器人关节、数控机床、包装与医疗设备制造商

### 知识图谱节点与关系

- 零部件实体：`ent_component_wittenstein_sp_plus`
- 制造商实体：`ent_company_wittenstein`
- 关键关系：
  - `rel_ent_company_wittenstein_manufactures_ent_component_wittenstein_sp_plus`（`ent_company_wittenstein` --> `manufactures` --> `ent_component_wittenstein_sp_plus`）

### 应用场景

- **工业机器人**：六轴机器人腕部、肩部关节的高精度减速
- **人形机器人**：手臂、腿部旋转关节传动
- **数控机床**：机床进给轴、刀库、转台定位
- **其他自动化**：包装机械、印刷设备、医疗定位平台

### 竞争对比

| 对比项 | SP+ 行星减速器 | Neugart PLN | STOBER P |
|--------|------------------------|---------------|---------------|
| 核心优势 | 德国高端螺旋齿、恒定低背隙 | 高精度直齿、PLN 标准 | 模块化 helical 行星 |
| 背隙/精度 | ≤1–3 arcmin | ≤1–3 arcmin | 1–4 arcmin |
| 价格水平 | 高端 | 高端 | 中高端 |
| 交付周期 | 中等 | 中等 | 中等 |

### 选购与部署建议

根据循环次数、峰值扭矩与安装空间选择尺寸；高动态机器人关节建议选用降低背隙版本，并配合 alpha 选型软件 cymex® 校核寿命。

### 参考资料

1. [威腾斯坦 官网](https://www.wittenstein.de)
2. [WITTENSTEIN alpha SP+ Planetary Gearbox](https://www.wittenstein.de/en-en/products/servo-gearboxes/low-backlash-planetary-gearboxes/sp-planetary-gearbox/)
3. [WAIC 2026 参展报道](https://www.worldrobotconference.com)

## 参考
- [Wittenstein](https://www.wittenstein.de/)
- 项目 Wiki：appendix-d/products/product_wittenstein_sp_plus.md

## Overview
Wittenstein is an important component manufacturer in the humanoid robot field. The following content is compiled from the project Wiki for in-depth reference.

## Content
## WITTENSTEIN alpha SP+ Planetary Gearbox

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Index](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

### Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [WITTENSTEIN alpha](../companies/company_wittenstein.md) |
| **Product Category** | Planetary Gearbox / Servo Gearbox |
| **Release Date** | Current main model |
| **Status** | Mass production / Commercial |
| **Official Website/Source** | [WITTENSTEIN Official Website](https://www.wittenstein.de) |

### Product Overview

The SP+ is a classic low-backlash planetary gearbox series from WITTENSTEIN alpha, designed for high positioning accuracy and dynamic cyclic applications. It features helical planetary gears, preloaded tapered roller bearings, and modular motor interfaces, offering an acceleration torque range from 48 N·m to 5,700 N·m.

This series is available in a standard (MF) version with reduction ratios of 3–100 and 7 sizes, with an optional reduced backlash version. The SP+ HIGH SPEED and MC-L low-friction versions further cover continuous operation and high-speed scenarios, making it a core transmission component for machine tools, robots, and automated production lines.

### Product Image

> WITTENSTEIN alpha SP+ Planetary Gearbox: Please visit the [official website](https://www.wittenstein.de) for details.

### Specification Table

| Specification Item | Value | Notes/Source |
|-------------------|-------|--------------|
| Reduction Ratio | 3:1 – 100:1 | Product manual |
| Frame Size | 7 sizes (MF) | Product manual |
| Maximum Output Torque | 48 – 5,700 N·m | Product manual |
| Maximum Input Speed | Up to 8,500 rpm | Product manual |
| Backlash | Standard ≤3 arcmin / Reduced ≤1 arcmin | Product manual |
| Torsional Stiffness | 550 N·m/arcmin | Product manual |
| Maximum Tilting Moment | 5,000 N·m | Product manual |
| Price | Not disclosed | - |

### Supply Chain Position

- **Manufacturer**: [WITTENSTEIN alpha](../companies/company_wittenstein.md)
- **Core Components/Technology Sources**: High-strength alloy steel gears, precision bearings, seals, grease, motor adapter flanges
- **Downstream Applications/Customers**: Industrial robots, humanoid robot joints, CNC machine tools, packaging and medical equipment manufacturers

### Knowledge Graph Nodes and Relationships

- Component entity: `ent_component_wittenstein_sp_plus`
- Manufacturer entity: `ent_company_wittenstein`
- Key relationship:
  - `rel_ent_company_wittenstein_manufactures_ent_component_wittenstein_sp_plus` (`ent_company_wittenstein` --> `manufactures` --> `ent_component_wittenstein_sp_plus`)

### Application Scenarios

- **Industrial Robots**: High-precision reduction in six-axis robot wrist and shoulder joints
- **Humanoid Robots**: Transmission in arm and leg rotational joints
- **CNC Machine Tools**: Feed axes, tool magazines, and turntable positioning
- **Other Automation**: Packaging machinery, printing equipment, medical positioning platforms

### Competitive Comparison

| Comparison Item | SP+ Planetary Gearbox | Neugart PLN | STOBER P |
|----------------|------------------------|---------------|---------------|
| Core Advantage | German high-end helical gears, constant low backlash | High-precision spur gears, PLN standard | Modular helical planetary |
| Backlash/Precision | ≤1–3 arcmin | ≤1–3 arcmin | 1–4 arcmin |
| Price Level | High-end | High-end | Mid-to-high end |
| Delivery Time | Medium | Medium | Medium |

### Selection and Deployment Recommendations

Select the size based on cycle count, peak torque, and installation space; for high-dynamic robot joints, it is recommended to choose the reduced backlash version and use the alpha selection software cymex® to verify service life.

### References

1. [WITTENSTEIN Official Website](https://www.wittenstein.de)
2. [WITTENSTEIN alpha SP+ Planetary Gearbox](https://www.wittenstein.de/en-en/products/servo-gearboxes/low-backlash-planetary-gearboxes/sp-planetary-gearbox/)
3. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)

## 개요
Wittenstein은 휴머노이드 로봇 분야의 핵심 부품 제조업체입니다. 아래 내용은 프로젝트 Wiki에서 정리한 것으로, 심층 참고용으로 제공됩니다.

## 핵심 내용
## WITTENSTEIN alpha SP+ 유성 감속기 / WITTENSTEIN alpha SP+ Planetary Gearbox

> 본 용어는 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

### 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [威腾斯坦 / WITTENSTEIN alpha](../companies/company_wittenstein.md) |
| **제품 카테고리** | 유성 감속기 / 서보 감속기 |
| **출시 시기** | 현역 주력 모델 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [威腾斯坦 공식 사이트](https://www.wittenstein.de) |

### 제품 개요

SP+는 WITTENSTEIN alpha의 고전적인 저백래시 유성 감속기 시리즈로, 높은 위치 정밀도와 순환 동적 애플리케이션을 위해 설계되었습니다. 헬리컬 유성 기어, 프리로드 테이퍼 롤러 베어링 및 모듈식 모터 인터페이스를 채택하여 48 N·m에서 5,700 N·m까지의 가속 토크 범위를 제공합니다.

이 시리즈는 표준(MF) 버전을 제공하며, 감속비 3–100, 7가지 크기, 백래시 감소 버전을 선택할 수 있습니다. SP+ HIGH SPEED 및 MC-L 저마찰 버전은 연속 운전 및 고속 시나리오를 더욱 포괄하여 공작 기계, 로봇 및 자동화 생산 라인의 핵심 동력 전달 부품입니다.

### 제품 이미지

> WITTENSTEIN alpha SP+ 유성 감속기 / WITTENSTEIN alpha SP+ Planetary Gearbox: [공식 자료](https://www.wittenstein.de)를 방문하여 확인하십시오.

### 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 감속비 | 3:1 – 100:1 | 제품 매뉴얼 |
| 프레임 번호/크기 | 7가지 크기 (MF) | 제품 매뉴얼 |
| 최대 출력 토크 | 48 – 5,700 N·m | 제품 매뉴얼 |
| 최대 입력 회전 속도 | 최대 8,500 rpm | 제품 매뉴얼 |
| 백래시 | 표준 ≤3 arcmin / 감소 ≤1 arcmin | 제품 매뉴얼 |
| 비틀림 강성 | 550 N·m/arcmin | 제품 매뉴얼 |
| 최대 전복 모멘트 | 5,000 N·m | 제품 매뉴얼 |
| 가격 | 미공개 | - |

### 공급망 위치

- **제조사**: [威腾斯坦 / WITTENSTEIN alpha](../companies/company_wittenstein.md)
- **핵심 부품/기술 출처**: 고강도 합금강 기어, 정밀 베어링, 씰, 그리스, 모터 어댑터 플랜지
- **하류 응용/고객**: 산업용 로봇, 휴머노이드 로봇 관절, CNC 공작 기계, 포장 및 의료 장비 제조사

### 지식 그래프 노드 및 관계

- 부품 엔터티: `ent_component_wittenstein_sp_plus`
- 제조사 엔터티: `ent_company_wittenstein`
- 주요 관계:
  - `rel_ent_company_wittenstein_manufactures_ent_component_wittenstein_sp_plus` (`ent_company_wittenstein` --> `manufactures` --> `ent_component_wittenstein_sp_plus`)

### 응용 시나리오

- **산업용 로봇**: 6축 로봇 손목, 어깨 관절의 고정밀 감속
- **휴머노이드 로봇**: 팔, 다리 회전 관절 동력 전달
- **CNC 공작 기계**: 공작 기계 이송축, 공구 매거진, 턴테이블 위치 결정
- **기타 자동화**: 포장 기계, 인쇄 장비, 의료 위치 결정 플랫폼

### 경쟁 비교

| 비교 항목 | SP+ 유성 감속기 | Neugart PLN | STOBER P |
|--------|------------------------|---------------|---------------|
| 핵심 장점 | 독일 고급 헬리컬 기어, 일정한 저백래시 | 고정밀 직선 기어, PLN 표준 | 모듈식 헬리컬 유성 |
| 백래시/정밀도 | ≤1–3 arcmin | ≤1–3 arcmin | 1–4 arcmin |
| 가격 수준 | 고급 | 고급 | 중고급 |
| 납기 | 중간 | 중간 | 중간 |

### 구매 및 배치 권장 사항

사이클 횟수, 피크 토크 및 설치 공간에 따라 크기를 선택하십시오. 고동적 로봇 관절에는 백래시 감소 버전을 선택하고 alpha 선정 소프트웨어 cymex®와 함께 수명을 검증하는 것이 좋습니다.

### 참고 자료

1. [威腾斯坦 공식 사이트](https://www.wittenstein.de)
2. [WITTENSTEIN alpha SP+ Planetary Gearbox](https://www.wittenstein.de/en-en/products/servo-gearboxes/low-backlash-planetary-gearboxes/sp-planetary-gearbox/)
3. [WAIC 2026 참가 보도](https://www.worldrobotconference.com)

---
$id: ent_tier1_supplier_sanhua_intelligent_controls
$schema: ../../../../../data/schema/v1/entry_schema.json
$version: 1
type: tier1_supplier
names:
  en: Sanhua Intelligent Controls
  zh: 三花智控
  ko: 산화 인텔리전트 컨트롤스
summary:
  en: Chinese Tier-1 supplier of thermal management and electromechanical actuators, reportedly a key actuator assembly partner
    for Tesla Optimus.
  zh: '> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。 > 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。'
  ko: 중국의 Tier-1 열관리 및 전기기계 액추에이터 공급업체로, 테슬라 옵티머스의 액추에이터 어셈블리 핵심 파트너로 알려짐.
domains:
- 02_components
- 05_mass_production
layers:
- upstream
- midstream
functional_roles:
- organization
tags:
- sanhua
- tier1_supplier
- actuator
- thermal_management
- tesla
- optimus
- china
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/companies/company_sanhua.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001_sanhua_36kr
  type: report
  title: Elon Musk Places $685M Order with Sanhua
  url: https://eu.36kr.com/en/p/3510288514980998
  date: '2025-10-15'
  accessed_at: '2026-06-25'
- id: src_002_sanhua_optimusk
  type: report
  title: 'Tesla Optimus Supply Chain: Who Makes the Parts?'
  url: https://optimusk.blog/blog/tesla-optimus-suppliers/
  date: '2026-06-01'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_robot_system_tesla_optimus
  relationship: supplies
  description:
    en: Sanhua is reported to supply linear and rotary actuator assemblies for Tesla Optimus.
    zh: 据报道，三花智控为特斯拉 Optimus 供应线性与旋转执行器总成。
    ko: 산화는 테슬라 옵티머스용 선형 및 회전 액추에이터 어셈블리를 공급하는 것으로 볏도됨.
- id: ent_component_harmonic_drive_reducer
  relationship: integrates
  description:
    en: Sanhua's actuator assemblies are understood to integrate precision reducers such as harmonic drives sourced from specialized
      reducer suppliers.
    zh: 三花的执行器总成据信集成了来自专业减速器供应商的谐波减速器等精密减速装置。
    ko: 산화의 액추에이터 어셈블리는 전문 감속기 공급업체로부터 조달한 하모닉 드라이브 등의 정밀 감속기를 통합하는 것으로 파악됨.
theoretical_depth:
- system
---

## 概述
三花智控是人形机器人领域的重要Tier 1 供应商。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## 三花智控 / Sanhua Intelligent Controls

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | 三花智控 |
| **英文名** | Sanhua Intelligent Controls |
| **总部** | 中国浙江省绍兴市 |
| **成立时间** | 1994 年 |
| **官网** | [https://www.sanhuaglobal.com](https://www.sanhuaglobal.com) |
| **供应链环节** | 热管理、微通道换热器、电子膨胀阀、机器人机电执行器 |
| **企业属性** | 上市公司（SZ: 002050）、全球制冷与热管理控制部件龙头 |
| **母公司/所属集团** | 三花控股集团有限公司 |
| **数据来源** | 三花智控官网、年报、投资者关系公告、公开研报 |

### 公司简介

三花智控是全球制冷空调控制元器件与新能源汽车热管理龙头，凭借精密阀件、泵与执行器技术向机器人热管理与机电执行器延伸。

公司核心产品包括电子膨胀阀、四通阀、电磁阀、微通道换热器、电子水泵、油冷器及新能源汽车热管理集成组件。三花在流体控制、精密电磁驱动与热管理方面积累深厚，正积极布局人形机器人旋转/线性执行器、伺服电机及热管理组件，与多家头部机器人企业建立合作。

### 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| 制冷空调控制元器件 | 阀件与换热器 | 电子膨胀阀、四通阀、微通道换热器 | 家用/商用空调、冷链 |
| 新能源汽车热管理 | 整车热管理集成 | 电子水泵、Chiller、集成模块 | 新能源汽车 |
| 机器人执行器与热管理 | 人形机器人机电执行器、关节热管理 | 旋转/线性执行器、热管理阀件 | 人形机器人、工业机器人 |

### 代表产品

#### 三花热管理部件 / 电子膨胀阀

> 三花热管理部件 / 电子膨胀阀：请访问 [官方资料](https://www.sanhuaglobal.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 电子膨胀阀、电磁阀、电子水泵、Chiller、换热器 | 三花官网 |
| 控制精度 | 高精度流量/压力调节 | 三花公开资料 |
| 工作压力 | 视型号 0–4.5 MPa 不等 | 产品手册 |
| 介质 | R134a、R1234yf、冷却液等 | 三花资料 |
| 尺寸 | 阀体直径约 20–60 mm（视型号） | 公开规格 |
| 重量 | 数十克至数百克 | 公开规格 |
| 寿命 | >10 万次（典型型号） | 三花公开资料 |
| 价格 | 未公开 | - |

**技术亮点**：全球市占率领先的电子膨胀阀、精密流体控制能力、可扩展至机器人热管理与执行器冷却。

**应用场景**：新能源汽车热管理、储能温控、数据中心液冷、机器人关节热管理。

#### 三花机器人机电执行器

> 三花机器人机电执行器：请访问 [官方资料](https://www.sanhuaglobal.com) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 产品形态 | 旋转执行器、线性执行器（丝杠/推杆） | 投资者关系公告 |
| 驱动方式 | 伺服电机 + 减速器/丝杠 | 行业分析 |
| 扭矩/推力 | 视方案 10–200 N·m / 数百至数千 N | 未公开 |
| 控制方式 | 无刷电机 + 编码器 + 驱动器 | 未公开 |
| 冷却方式 | 可选液冷/风冷 | 未公开 |
| 尺寸 | 因客户方案定制 | 未公开 |
| 重量 | 因规格而异 | 未公开 |
| 价格 | 未公开 | - |

**技术亮点**：依托电磁驱动、流体控制与精密制造能力，开发高集成度机器人执行器；与多家头部人形机器人企业合作。

**应用场景**：人形机器人关节、工业机器人、协作机器人。

### 供应链位置

- **上游关键零部件/材料**：铜材、铝材、稀土永磁体、电子元器件、精密加工设备、密封材料。
- **下游客户/应用场景**：特斯拉、比亚迪、美的、格力等车企与家电企业；人形机器人整机厂。
- **主要竞争对手/对标**：盾安环境、银轮股份；机器人执行器领域对标拓普集团、绿的谐波。

### 知识图谱节点与关系

- 公司实体：`ent_company_sanhua`
- 产品实体：`ent_product_sanhua_thermal`、`ent_product_sanhua_actuator`
- 关键关系：
  - `ent_company_sanhua` -- `manufactures` --> `ent_product_sanhua_thermal`
  - `ent_company_sanhua` -- `manufactures` --> `ent_product_sanhua_actuator`
  - `ent_product_sanhua_thermal` -- `uses` --> `ent_component_electronic_expansion_valve`
  - `ent_product_sanhua_actuator` -- `uses` --> `ent_component_servo_motor`

### 参考资料

1. [官网](https://www.sanhuaglobal.com)
2. [三花智控官网](https://www.sanhuaglobal.com)
3. 三花智控 2024 年度报告与投资者交流纪要

## 参考
- [Elon Musk Places $685M Order with Sanhua](https://eu.36kr.com/en/p/3510288514980998)
- [Tesla Optimus Supply Chain: Who Makes the Parts?](https://optimusk.blog/blog/tesla-optimus-suppliers/)
- 项目 Wiki：appendix-d/companies/company_sanhua.md

## Overview
Sanhua Intelligent Controls is a key Tier 1 supplier in the humanoid robotics sector. The following content is compiled from the project Wiki for in-depth reference.

## Content
## Sanhua Intelligent Controls

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

### Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 三花智控 |
| **English Name** | Sanhua Intelligent Controls |
| **Headquarters** | Shaoxing, Zhejiang Province, China |
| **Founded** | 1994 |
| **Website** | [https://www.sanhuaglobal.com](https://www.sanhuaglobal.com) |
| **Supply Chain Role** | Thermal management, microchannel heat exchangers, electronic expansion valves, robotic electromechanical actuators |
| **Company Type** | Listed company (SZ: 002050), global leader in refrigeration and thermal management control components |
| **Parent/Group** | Sanhua Holding Group Co., Ltd. |
| **Data Sources** | Sanhua Intelligent Controls official website, annual reports, investor relations announcements, public research reports |

### Company Profile

Sanhua Intelligent Controls is a global leader in refrigeration and air conditioning control components and new energy vehicle thermal management. Leveraging its precision valve, pump, and actuator technologies, it extends into robotic thermal management and electromechanical actuators.

The company's core products include electronic expansion valves, four-way valves, solenoid valves, microchannel heat exchangers, electronic water pumps, oil coolers, and integrated thermal management modules for new energy vehicles. With deep expertise in fluid control, precision electromagnetic drives, and thermal management, Sanhua is actively developing rotary/linear actuators, servo motors, and thermal management components for humanoid robots, collaborating with several leading robotics companies.

### Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|-------------------------|-------------------|
| Refrigeration & AC Control Components | Valves and heat exchangers | Electronic expansion valves, four-way valves, microchannel heat exchangers | Residential/commercial AC, cold chain |
| New Energy Vehicle Thermal Management | Integrated vehicle thermal management | Electronic water pumps, Chiller, integrated modules | New energy vehicles |
| Robotic Actuators & Thermal Management | Humanoid robot electromechanical actuators, joint thermal management | Rotary/linear actuators, thermal management valves | Humanoid robots, industrial robots |

### Representative Products

#### Sanhua Thermal Management Components / Electronic Expansion Valves

> Sanhua Thermal Management Components / Electronic Expansion Valves: Please visit [official website](https://www.sanhuaglobal.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Product Form | Electronic expansion valves, solenoid valves, electronic water pumps, Chiller, heat exchangers | Sanhua official website |
| Control Accuracy | High-precision flow/pressure regulation | Sanhua public data |
| Operating Pressure | 0–4.5 MPa depending on model | Product manual |
| Medium | R134a, R1234yf, coolant, etc. | Sanhua data |
| Dimensions | Valve body diameter approx. 20–60 mm (depending on model) | Public specifications |
| Weight | Tens to hundreds of grams | Public specifications |
| Lifespan | >100,000 cycles (typical models) | Sanhua public data |
| Price | Not disclosed | - |

**Technical Highlights**: Global market share leader in electronic expansion valves, precision fluid control capability, expandable to robotic thermal management and actuator cooling.

**Application Scenarios**: New energy vehicle thermal management, energy storage temperature control, data center liquid cooling, robotic joint thermal management.

#### Sanhua Robotic Electromechanical Actuators

> Sanhua Robotic Electromechanical Actuators: Please visit [official website](https://www.sanhuaglobal.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Product Form | Rotary actuators, linear actuators (ball screw/push rod) | Investor relations announcements |
| Drive Method | Servo motor + reducer/ball screw | Industry analysis |
| Torque/Thrust | 10–200 N·m / hundreds to thousands of N depending on solution | Not disclosed |
| Control Method | Brushless motor + encoder + driver | Not disclosed |
| Cooling Method | Optional liquid/air cooling | Not disclosed |
| Dimensions | Customized per customer solution | Not disclosed |
| Weight | Varies by specification | Not disclosed |
| Price | Not disclosed | - |

**Technical Highlights**: Leveraging electromagnetic drive, fluid control, and precision manufacturing capabilities to develop highly integrated robotic actuators; collaborating with multiple leading humanoid robot companies.

**Application Scenarios**: Humanoid robot joints, industrial robots, collaborative robots.

### Supply Chain Position

- **Upstream Key Components/Materials**: Copper, aluminum, rare earth permanent magnets, electronic components, precision machining equipment, sealing materials.
- **Downstream Customers/Applications**: Tesla, BYD, Midea, Gree, and other automotive and home appliance companies; humanoid robot OEMs.
- **Main Competitors/Peers**: Dun'an Environment, Yinlun Co.; in robotic actuators, peers include Tuopu Group, Leaderdrive.

### Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_sanhua`
- Product Entities: `ent_product_sanhua_thermal`, `ent_product_sanhua_actuator`
- Key Relationships:
  - `ent_company_sanhua` -- `manufactures` --> `ent_product_sanhua_thermal`
  - `ent_company_sanhua` -- `manufactures` --> `ent_product_sanhua_actuator`
  - `ent_product_sanhua_thermal` -- `uses` --> `ent_component_electronic_expansion_valve`
  - `ent_product_sanhua_actuator` -- `uses` --> `ent_component_servo_motor`

### References

1. [Official Website](https://www.sanhuaglobal.com)
2. [Sanhua Intelligent Controls Official Website](https://www.sanhuaglobal.com)
3. Sanhua Intelligent Controls 2024 Annual Report and Investor Communication Minutes

## 개요
삼화지공은 휴머노이드 로봇 분야의 중요한 Tier 1 공급업체입니다. 아래 내용은 프로젝트 Wiki에서 정리한 내용으로, 심층 참고용으로 제공됩니다.

## 핵심 내용
## 삼화지공 / Sanhua Intelligent Controls

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

### 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **중문명** | 삼화지공 |
| **영문명** | Sanhua Intelligent Controls |
| **본사** | 중국 저장성 사오싱시 |
| **설립일** | 1994년 |
| **공식 사이트** | [https://www.sanhuaglobal.com](https://www.sanhuaglobal.com) |
| **공급망 단계** | 열관리, 마이크로채널 열교환기, 전자식 팽창밸브, 로봇 전기기계식 액추에이터 |
| **기업 속성** | 상장사 (SZ: 002050), 글로벌 냉동 및 열관리 제어 부품 선두 기업 |
| **모회사/소속 그룹** | 삼화홀딩그룹유한공사 |
| **데이터 출처** | 삼화지공 공식 사이트, 연례 보고서, 투자자 관계 공시, 공개 연구 보고서 |

### 회사 소개

삼화지공은 글로벌 냉동 공조 제어 부품 및 신에너지 차량 열관리 선두 기업으로, 정밀 밸브 부품, 펌프 및 액추에이터 기술을 바탕으로 로봇 열관리 및 전기기계식 액추에이터 분야로 확장하고 있습니다.

회사의 핵심 제품으로는 전자식 팽창밸브, 사방밸브, 전자기밸브, 마이크로채널 열교환기, 전자식 워터 펌프, 오일 쿨러 및 신에너지 차량 열관리 통합 모듈이 있습니다. 삼화는 유체 제어, 정밀 전자기 구동 및 열관리 분야에서 깊은 기술력을 축적하고 있으며, 휴머노이드 로봇의 회전/직선 액추에이터, 서보 모터 및 열관리 부품을 적극적으로 개발하여 여러 선두 로봇 기업과 협력 관계를 구축하고 있습니다.

### 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 응용 분야 |
|--------|------|----------|----------|
| 냉동 공조 제어 부품 | 밸브 부품 및 열교환기 | 전자식 팽창밸브, 사방밸브, 마이크로채널 열교환기 | 가정용/상업용 에어컨, 콜드체인 |
| 신에너지 차량 열관리 | 차량 열관리 통합 | 전자식 워터 펌프, 칠러, 통합 모듈 | 신에너지 차량 |
| 로봇 액추에이터 및 열관리 | 휴머노이드 로봇 전기기계식 액추에이터, 관절 열관리 | 회전/직선 액추에이터, 열관리 밸브 부품 | 휴머노이드 로봇, 산업용 로봇 |

### 대표 제품

#### 삼화 열관리 부품 / 전자식 팽창밸브

> 삼화 열관리 부품 / 전자식 팽창밸브: [공식 자료](https://www.sanhuaglobal.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 제품 형태 | 전자식 팽창밸브, 전자기밸브, 전자식 워터 펌프, 칠러, 열교환기 | 삼화 공식 사이트 |
| 제어 정밀도 | 고정밀 유량/압력 조절 | 삼화 공개 자료 |
| 작동 압력 | 모델에 따라 0–4.5 MPa | 제품 매뉴얼 |
| 매체 | R134a, R1234yf, 냉각수 등 | 삼화 자료 |
| 크기 | 밸브 본체 직경 약 20–60 mm (모델에 따라 다름) | 공개 사양 |
| 무게 | 수십 그램에서 수백 그램 | 공개 사양 |
| 수명 | >10만 회 (대표 모델) | 삼화 공개 자료 |
| 가격 | 미공개 | - |

**기술적 특징**: 글로벌 시장 점유율 선두의 전자식 팽창밸브, 정밀 유체 제어 능력, 로봇 열관리 및 액추에이터 냉각으로 확장 가능.

**응용 분야**: 신에너지 차량 열관리, 에너지 저장 온도 제어, 데이터 센터 액체 냉각, 로봇 관절 열관리.

#### 삼화 로봇 전기기계식 액추에이터

> 삼화 로봇 전기기계식 액추에이터: [공식 자료](https://www.sanhuaglobal.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 제품 형태 | 회전 액추에이터, 직선 액추에이터 (볼스크류/푸시로드) | 투자자 관계 공시 |
| 구동 방식 | 서보 모터 + 감속기/볼스크류 | 업계 분석 |
| 토크/추력 | 구성에 따라 10–200 N·m / 수백에서 수천 N | 미공개 |
| 제어 방식 | 브러시리스 모터 + 엔코더 + 드라이버 | 미공개 |
| 냉각 방식 | 액체 냉각/공랭식 선택 가능 | 미공개 |
| 크기 | 고객 구성에 따라 맞춤 제작 | 미공개 |
| 무게 | 사양에 따라 다름 | 미공개 |
| 가격 | 미공개 | - |

**기술적 특징**: 전자기 구동, 유체 제어 및 정밀 제조 능력을 기반으로 고집적 로봇 액추에이터 개발; 여러 선두 휴머노이드 로봇 기업과 협력.

**응용 분야**: 휴머노이드 로봇 관절, 산업용 로봇, 협동 로봇.

### 공급망 위치

- **상류 핵심 부품/소재**: 구리, 알루미늄, 희토류 영구자석, 전자 부품, 정밀 가공 장비, 밀봉 재료.
- **하류 고객/응용 분야**: 테슬라, BYD, 미디어, 그리 등 자동차 및 가전 기업; 휴머노이드 로봇 완성체 제조사.
- **주요 경쟁사/벤치마크**: 둔안환징, 인룬주펀; 로봇 액추에이터 분야에서 톄푸지퇀, 뤼더셰보와 경쟁.

### 지식 그래프 노드 및 관계

- 회사 엔티티: `ent_company_sanhua`
- 제품 엔티티: `ent_product_sanhua_thermal`, `ent_product_sanhua_actuator`
- 주요 관계:
  - `ent_company_sanhua` -- `manufactures` --> `ent_product_sanhua_thermal`
  - `ent_company_sanhua` -- `manufactures` --> `ent_product_sanhua_actuator`
  - `ent_product_sanhua_thermal` -- `uses` --> `ent_component_electronic_expansion_valve`
  - `ent_product_sanhua_actuator` -- `uses` --> `ent_component_servo_motor`

### 참고 자료

1. [공식 사이트](https://www.sanhuaglobal.com)
2. [삼화지공 공식 사이트](https://www.sanhuaglobal.com)
3. 삼화지공 2024년 연례 보고서 및 투자자 소통 회의록

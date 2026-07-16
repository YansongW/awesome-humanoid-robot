---
$id: ent_company_nabtesco_corporation_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component_manufacturer
names:
  en: Nabtesco Corporation
  zh: 纳博特斯克
  ko: Nabtesco Corporation
summary:
  en: Japanese manufacturer of RV and cycloidal reducers used in high-load robot joints.
  zh: 纳博特斯克是人形机器人领域的重要component_manufacturer。以下内容整理自项目 Wiki，供深入查阅。
  ko: 고하중 로봇 관절에 사용되는 RV 및 사이클로이드 감속기 제조업체.
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
- cycloidal
- japan
- nabtesco
- reducer
- rv_reducer
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from appendix-d/companies/company_nabtesco.md by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Nabtesco Corporation
  url: https://www.nabtesco.co.jp/
  date: '2024'
  accessed_at: '2026-07-01'
---


## 概述
纳博特斯克是人形机器人领域的重要零部件_manufacturer。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
## Nabtesco（纳博特斯克） / Nabtesco

> 本词条属于 [附录 D 企业/产品 Wiki](../../appendix-d.md)。
> 数据更新时间：2026-07-01。所有参数以官方公开资料为准，缺失项标注为“未公开”。

---

### 公司信息卡

| 项目 | 内容 |
|------|------|
| **中文名** | Nabtesco（纳博特斯克） |
| **英文名** | Nabtesco |
| **总部** | 日本东京 |
| **成立时间** | 2003 |
| **官网** | [https://www.nabtesco-motion.cn](https://www.nabtesco-motion.cn) |
| **供应链环节** | RV 减速器 / 精密减速器 / 执行器 |
| **企业属性** | 外资品牌、Nabtesco Corporation 子公司 |
| **母公司/所属集团** | Nabtesco Corporation |
| **数据来源** | 官网、产品手册、公开研报、WAIC 2026 报道 |

### 公司简介

全球 RV 减速器龙头，累计出货超过 700 万台，主导工业机器人重载关节市场。

Nabtesco 的 RV-E、RV-C、RV-N 系列 RV 减速器以高刚性、高扭矩、低背隙和长寿命著称，广泛用于工业机器人基座、大臂、肩部等重载关节。

### 产品线

| 产品线 | 定位 | 代表产品 | 应用领域 |
|--------|------|----------|----------|
| RV-E 系列 | 标准 RV 减速器 | RV-20E / RV-40E / RV-80E | 工业机器人重载关节 |
| RV-N 系列 | 紧凑型高扭矩 RV 减速器 | RV-25N / RV-42N | 协作/人形机器人 |

### 代表产品

#### RV-40E-105 RV 减速器 / RV-40E-105 Precision Reducer

> RV-40E-105 RV 减速器：请访问 [官方资料](https://www.nabtesco-motion.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 外径 | 约 105 mm | Nabtesco RV-E 手册 |
| 重量 | 9.3 kg | 行业研报 / Nabtesco 参数表 |
| 减速比 | 105:1 | Nabtesco 产品页 |
| 额定扭矩 | 412 N·m | Nabtesco 产品页 |
| 启动停止容许扭矩 | 1029 N·m | Nabtesco 产品页 |
| 瞬时最大扭矩 | 2058 N·m | Nabtesco 产品页 |
| 容许输出转速 | 70 rpm（100% 占空比） | Nabtesco 产品页 |
| 背隙 | < 1 arc-min | Nabtesco 产品页 |
| 额定寿命 | 6000 h | Nabtesco 产品页 |

**技术亮点**：主轴承内置、高刚性、抗冲击，是工业机器人肩/腰关节的标准选择。

**应用场景**：六轴工业机器人 J1–J3 关节、人形机器人腰/髋部、重载变位机。

#### RV-20E-81 RV 减速器 / RV-20E-81 Precision Reducer

> RV-20E-81 RV 减速器：请访问 [官方资料](https://www.nabtesco-motion.cn) 查看。

| 规格项 | 数值 | 备注/来源 |
|--------|------|-----------|
| 外径 | 约 65 mm | Nabtesco RV-E 手册 |
| 重量 | 约 4.7 kg | Nabtesco 参数表 |
| 减速比 | 81:1 | Nabtesco 产品页 |
| 额定扭矩 | 167 N·m | Nabtesco 产品页 |
| 启动停止容许扭矩 | 412 N·m | Nabtesco 产品页 |
| 瞬时最大扭矩 | 833 N·m | Nabtesco 产品页 |
| 容许输出转速 | 75 rpm（100% 占空比） | Nabtesco 产品页 |
| 背隙 | < 1 arc-min | Nabtesco 产品页 |
| 额定寿命 | 6000 h | Nabtesco 产品页 |

**技术亮点**：中小型 RV 减速器，适合中等负载机器人关节和精密转台。

**应用场景**：SCARA、小型六轴机器人、人形机器人腿部关节、CNC 转台。

### 供应链位置

- **上游关键零部件/材料**：合金钢、摆线轮、针齿壳、轴承、润滑脂
- **下游客户/应用场景**：工业机器人四大家族、国产机器人、人形机器人 OEM
- **主要竞争对手/对标**：双环传动、中大力德、住友重机械

### 知识图谱节点与关系

- 公司实体：`ent_company_nabtesco`
- 产品实体：`ent_component_nabtesco_rv_40e_105`、`ent_component_nabtesco_rv_20e_81`
- 关键关系：
  - `ent_company_nabtesco` -- `manufactures` --> `ent_component_nabtesco_rv_40e_105`
  - `ent_company_nabtesco` -- `manufactures` --> `ent_component_nabtesco_rv_20e_81`

### 参考资料

1. [官网](https://www.nabtesco-motion.cn)
2. [WAIC 2026 参展报道](https://www.worldrobotconference.com)
3. [公开产品手册与研报](https://www.inovance.com)（请按实际产品型号核对）

## 参考
- [Nabtesco Corporation](https://www.nabtesco.co.jp/)
- 项目 Wiki：appendix-d/companies/company_nabtesco.md

## Overview
Nabtesco is a key component manufacturer in the humanoid robotics sector. The following content is compiled from the project Wiki for in-depth reference.

## Content
## Nabtesco / Nabtesco

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

### Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Nabtesco (纳博特斯克) |
| **English Name** | Nabtesco |
| **Headquarters** | Tokyo, Japan |
| **Founded** | 2003 |
| **Website** | [https://www.nabtesco-motion.cn](https://www.nabtesco-motion.cn) |
| **Supply Chain Role** | RV Reducer / Precision Reducer / Actuator |
| **Enterprise Attribute** | Foreign Brand, Subsidiary of Nabtesco Corporation |
| **Parent Company/Group** | Nabtesco Corporation |
| **Data Source** | Official website, product manuals, public research reports, WAIC 2026 coverage |

### Company Profile

Global leader in RV reducers, with cumulative shipments exceeding 7 million units, dominating the heavy-duty joint market for industrial robots.

Nabtesco's RV-E, RV-C, and RV-N series RV reducers are renowned for high rigidity, high torque, low backlash, and long lifespan, widely used in heavy-duty joints such as robot bases, upper arms, and shoulders.

### Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|-------------------------|-------------------|
| RV-E Series | Standard RV Reducer | RV-20E / RV-40E / RV-80E | Heavy-duty joints for industrial robots |
| RV-N Series | Compact High-Torque RV Reducer | RV-25N / RV-42N | Collaborative/humanoid robots |

### Representative Products

#### RV-40E-105 RV Reducer / RV-40E-105 Precision Reducer

> RV-40E-105 RV Reducer: Please visit [official materials](https://www.nabtesco-motion.cn) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Outer Diameter | Approx. 105 mm | Nabtesco RV-E Manual |
| Weight | 9.3 kg | Industry research report / Nabtesco parameter table |
| Reduction Ratio | 105:1 | Nabtesco product page |
| Rated Torque | 412 N·m | Nabtesco product page |
| Allowable Torque at Start/Stop | 1029 N·m | Nabtesco product page |
| Instantaneous Maximum Torque | 2058 N·m | Nabtesco product page |
| Allowable Output Speed | 70 rpm (100% duty cycle) | Nabtesco product page |
| Backlash | < 1 arc-min | Nabtesco product page |
| Rated Life | 6000 h | Nabtesco product page |

**Technical Highlights**: Built-in main bearing, high rigidity, impact resistance, standard choice for shoulder/waist joints of industrial robots.

**Application Scenarios**: J1–J3 joints of six-axis industrial robots, waist/hip joints of humanoid robots, heavy-duty positioners.

#### RV-20E-81 RV Reducer / RV-20E-81 Precision Reducer

> RV-20E-81 RV Reducer: Please visit [official materials](https://www.nabtesco-motion.cn) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Outer Diameter | Approx. 65 mm | Nabtesco RV-E Manual |
| Weight | Approx. 4.7 kg | Nabtesco parameter table |
| Reduction Ratio | 81:1 | Nabtesco product page |
| Rated Torque | 167 N·m | Nabtesco product page |
| Allowable Torque at Start/Stop | 412 N·m | Nabtesco product page |
| Instantaneous Maximum Torque | 833 N·m | Nabtesco product page |
| Allowable Output Speed | 75 rpm (100% duty cycle) | Nabtesco product page |
| Backlash | < 1 arc-min | Nabtesco product page |
| Rated Life | 6000 h | Nabtesco product page |

**Technical Highlights**: Medium-small RV reducer, suitable for medium-load robot joints and precision rotary tables.

**Application Scenarios**: SCARA, small six-axis robots, leg joints of humanoid robots, CNC rotary tables.

### Supply Chain Position

- **Upstream Key Components/Materials**: Alloy steel, cycloidal gears, pinwheel housings, bearings, lubricating grease
- **Downstream Customers/Application Scenarios**: Big Four industrial robot manufacturers, domestic robots, humanoid robot OEMs
- **Main Competitors/Comparables**: Shuanghuan Transmission, Zhongda Leader, Sumitomo Heavy Industries

### Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_nabtesco`
- Product Entities: `ent_component_nabtesco_rv_40e_105`, `ent_component_nabtesco_rv_20e_81`
- Key Relationships:
  - `ent_company_nabtesco` -- `manufactures` --> `ent_component_nabtesco_rv_40e_105`
  - `ent_company_nabtesco` -- `manufactures` --> `ent_component_nabtesco_rv_20e_81`

### References

1. [Official Website](https://www.nabtesco-motion.cn)
2. [WAIC 2026 Exhibition Coverage](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://www.inovance.com) (Please verify against actual product models)

## 개요
나보테스크(Nabtesco)는 휴머노이드 로봇 분야의 핵심 부품 제조사입니다. 아래 내용은 프로젝트 Wiki에서 정리한 것으로, 심층적인 참고를 위해 제공됩니다.

## 핵심 내용
## Nabtesco（나보테스크） / Nabtesco

> 본 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 시점: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

### 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한국어명** | Nabtesco（나보테스크） |
| **영문명** | Nabtesco |
| **본사** | 일본 도쿄 |
| **설립 연도** | 2003 |
| **공식 사이트** | [https://www.nabtesco-motion.cn](https://www.nabtesco-motion.cn) |
| **공급망 단계** | RV 감속기 / 정밀 감속기 / 액추에이터 |
| **기업 속성** | 외자 브랜드, Nabtesco Corporation 자회사 |
| **모회사/소속 그룹** | Nabtesco Corporation |
| **데이터 출처** | 공식 사이트, 제품 매뉴얼, 공개 보고서, WAIC 2026 보도 |

### 회사 소개

글로벌 RV 감속기 선두 기업으로, 누적 출하량 700만 대를 돌파하며 산업용 로봇의 중하중 관절 시장을 주도합니다.

Nabtesco의 RV-E, RV-C, RV-N 시리즈 RV 감속기는 높은 강성, 높은 토크, 낮은 백래시 및 긴 수명으로 유명하며, 산업용 로봇의 베이스, 상완, 어깨 등 중하중 관절에 널리 사용됩니다.

### 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| RV-E 시리즈 | 표준 RV 감속기 | RV-20E / RV-40E / RV-80E | 산업용 로봇 중하중 관절 |
| RV-N 시리즈 | 컴팩트형 고토크 RV 감속기 | RV-25N / RV-42N | 협동/휴머노이드 로봇 |

### 대표 제품

#### RV-40E-105 RV 감속기 / RV-40E-105 Precision Reducer

> RV-40E-105 RV 감속기: [공식 자료](https://www.nabtesco-motion.cn)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 외경 | 약 105 mm | Nabtesco RV-E 매뉴얼 |
| 중량 | 9.3 kg | 업계 보고서 / Nabtesco 파라미터표 |
| 감속비 | 105:1 | Nabtesco 제품 페이지 |
| 정격 토크 | 412 N·m | Nabtesco 제품 페이지 |
| 기동 정지 허용 토크 | 1029 N·m | Nabtesco 제품 페이지 |
| 순간 최대 토크 | 2058 N·m | Nabtesco 제품 페이지 |
| 허용 출력 회전수 | 70 rpm（100% 듀티 사이클） | Nabtesco 제품 페이지 |
| 백래시 | < 1 arc-min | Nabtesco 제품 페이지 |
| 정격 수명 | 6000 h | Nabtesco 제품 페이지 |

**기술 하이라이트**: 메인 베어링 내장, 높은 강성, 내충격성으로 산업용 로봇 어깨/허리 관절의 표준 선택입니다.

**적용 시나리오**: 6축 산업용 로봇 J1–J3 관절, 휴머노이드 로봇 허리/엉덩이, 중하중 포지셔너.

#### RV-20E-81 RV 감속기 / RV-20E-81 Precision Reducer

> RV-20E-81 RV 감속기: [공식 자료](https://www.nabtesco-motion.cn)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 외경 | 약 65 mm | Nabtesco RV-E 매뉴얼 |
| 중량 | 약 4.7 kg | Nabtesco 파라미터표 |
| 감속비 | 81:1 | Nabtesco 제품 페이지 |
| 정격 토크 | 167 N·m | Nabtesco 제품 페이지 |
| 기동 정지 허용 토크 | 412 N·m | Nabtesco 제품 페이지 |
| 순간 최대 토크 | 833 N·m | Nabtesco 제품 페이지 |
| 허용 출력 회전수 | 75 rpm（100% 듀티 사이클） | Nabtesco 제품 페이지 |
| 백래시 | < 1 arc-min | Nabtesco 제품 페이지 |
| 정격 수명 | 6000 h | Nabtesco 제품 페이지 |

**기술 하이라이트**: 중소형 RV 감속기로, 중간 부하 로봇 관절 및 정밀 턴테이블에 적합합니다.

**적용 시나리오**: SCARA, 소형 6축 로봇, 휴머노이드 로봇 다리 관절, CNC 턴테이블.

### 공급망 위치

- **상류 핵심 부품/소재**: 합금강, 사이클로이드 기어, 핀 케이싱, 베어링, 그리스
- **하류 고객/적용 시나리오**: 산업용 로봇 4대 기업, 국산 로봇, 휴머노이드 로봇 OEM
- **주요 경쟁사/대비 대상**: 쌍환전동, 중대력덕, 스미토모 중기계

### 지식 그래프 노드 및 관계

- 회사 엔티티: `ent_company_nabtesco`
- 제품 엔티티: `ent_component_nabtesco_rv_40e_105`, `ent_component_nabtesco_rv_20e_81`
- 주요 관계:
  - `ent_company_nabtesco` -- `manufactures` --> `ent_component_nabtesco_rv_40e_105`
  - `ent_company_nabtesco` -- `manufactures` --> `ent_component_nabtesco_rv_20e_81`

### 참고 자료

1. [공식 사이트](https://www.nabtesco-motion.cn)
2. [WAIC 2026 참가 보도](https://www.worldrobotconference.com)
3. [공개 제품 매뉴얼 및 보고서](https://www.inovance.com)（실제 제품 모델에 따라 확인 필요）

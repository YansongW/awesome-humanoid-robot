---
$id: ent_component_manufacturer_nidec_drive_technology
$schema: ../../../../../data/schema/v1/entry_schema.json
$version: 1
type: component_manufacturer
names:
  en: Nidec Drive Technology
  zh: 尼得科传动技术
  ko: 니덱 드라이브 테크놀로지
summary:
  en: Japanese precision drive subsidiary of Nidec Corporation, manufacturer of FLEXWAVE strain-wave gear reducers and motion
    products targeted at humanoid robots.
  zh: 日本电产株式会社旗下精密传动子公司，生产面向人形机器人的 FLEXWAVE 应变波齿轮减速器及运动控制产品。
  ko: Nidec Corporation의 일본 정밀 드라이브 자회사로, 휴이노이드 로봇용 FLEXWAVE 스트레인 웨이브 기어 감속기 및 모션 제품을 생산함.
domains:
- 02_components
layers:
- upstream
functional_roles:
- organization
- component
tags:
- nidec
- flexwave
- harmonic_reducer
- strain_wave_gear
- component_manufacturer
- japan
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: AI-extracted from Nidec's official humanoid-robot product page and industry market reports; specific customer names
    and design-win status are not confirmed. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_001_nidec_official
  type: website
  title: Nidec — Highly Developed Humanoid Robots
  url: https://www.nidec-dtc.com/humanoid-robots/
  date: '2026'
  accessed_at: '2026-06-25'
- id: src_002_nidec_market_report
  type: report
  title: Humanoid Robot Market Key Player Ecosystem — Actuators & Actuator Parts
  url: https://www.maximizemarketresearch.com/market-report/global-humanoid-robot-market/10567/
  date: '2026-05-07'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_component_harmonic_drive_reducer
  relationship: produces
  description:
    en: Nidec Drive Technology produces FLEXWAVE strain-wave gear reducers, a form of harmonic reducer used in humanoid robot
      joints.
    zh: 尼得科传动技术生产 FLEXWAVE 应变波齿轮减速器，这是一种用于人形机器人关节的谐波减速器。
    ko: 니덱 드라이브 테크놀로지는 휴이노이드 로봇 관절에 사용되는 하모닉 감속기의 일종인 FLEXWAVE 스트레인 웨이브 기어 감속기를 생산함.
- id: ent_component_bldc_motor
  relationship: produces
  description:
    en: Nidec's broader motor portfolio includes brushless DC and precision servo motors used in robotic actuators.
    zh: 尼得科更广泛的电机产品组合包括用于机器人执行器的无刷直流电机和精密伺服电机。
    ko: 니덱의 폭넓은 모터 포트폴리오에는 로봇 액추에이터에 사용되는 브러시리스 DC 모터 및 정밀 서보 모터가 포함됨.
theoretical_depth:
- system
---
## 概述
日本电产株式会社旗下精密传动子公司，生产面向人形机器人的 FLEXWAVE 应变波齿轮减速器及运动控制产品。

## 核心内容
### 尼得科传动技术的定义与定位
尼得科传动技术属于 **component_manufacturer** 类型。 所属领域包括：02_components。 价值链层级：upstream。 日本电产株式会社旗下精密传动子公司，生产面向人形机器人的 FLEXWAVE 应变波齿轮减速器及运动控制产品。 英文名称为 *Nidec Drive Technology*。 韩文名称为 *니덱 드라이브 테크놀로지*。

### 尼得科传动技术的核心业务与产品
尼得科传动技术在人形机器人产业链中占据特定位置，其产品或技术能力与下游整机厂商形成供应或合作关系。
评估该实体时，应关注其技术壁垒、产能规模、客户结构与财务健康状况。

### 与人形机器人产业的关联
随着人形机器人产业化加速，尼得科传动技术的相关布局、技术路线与市场策略将持续影响行业生态。
其在核心零部件、系统集成或垂直场景中的角色，将直接影响整机成本、性能与交付能力。

### 竞争格局与发展前景
该领域竞争激烈，技术迭代快速。尼得科传动技术能否保持竞争优势，取决于其持续创新能力、供应链韧性与客户拓展能力。

### 相关标签
- nidec
- flexwave
- harmonic_reducer
- strain_wave_gear
- component_manufacturer
- japan

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键component_manufacturer之一，尼得科传动技术在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [Nidec — Highly Developed Humanoid Robots](https://www.nidec-dtc.com/humanoid-robots/)
- [Humanoid Robot Market Key Player Ecosystem — Actuators & Actuator Parts](https://www.maximizemarketresearch.com/market-report/global-humanoid-robot-market/10567/)


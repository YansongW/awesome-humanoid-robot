---
$id: ent_paper_liberman_pincu_designing_robots_with_the_cont_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Designing robots with the context in mind: One design does not fit all'
  zh: 情境驱动下的机器人设计：一种设计并不适用于所有情境
  ko: '상황을 고려한 로봇 설계: 하나의 디자인이 모든 곳에 맞지 않는다'
summary:
  en: This paper proposes a four-layer contextual framework (domain, physical environment, users, role) for socially assistive
    robot design, and reports an online questionnaire study (N=228) showing that users' desired robot characteristics and
    visual qualities differ significantly across four SAR use cases.
  zh: 本文提出一个四层情境框架（领域、物理环境、用户、角色）用于社交辅助机器人设计，并通过在线问卷研究（N=228）证明用户对机器人期望特征和视觉品质的需求在不同SAR使用场景中存在显著差异。核心贡献在于揭示“一种设计无法适应所有情境”的设计原则。
  ko: 본 논문은 사회적 보조 로봇 설계를 위한 네 가지 상황적 층(도메인, 물리적 환경, 사용자, 역할)을 제안하고, 228명의 성인을 대상으로 한 온라인 설문조사를 통해 네 가지 사용 사례에서 사용자가 원하는 로봇
    특성과 시각적 품질이 유의미하게 다름을 보였다.
domains:
- 06_design_engineering
- 11_applications_markets
- 05_mass_production
layers:
- midstream
- validation_markets
functional_roles:
- knowledge
tags:
- context_driven_design
- socially_assistive_robot
- visual_quality
- human_robot_interaction
- user_acceptance
- questionnaire
- mass_customization
- participatory_design
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2211.04163v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (806 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Designing robots with the context in mind- One design does not fit all
  url: https://arxiv.org/abs/2211.04163
  date: '2022'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
该研究指出当前社交辅助机器人（SAR）制造商常将同一外观设计应用于不同场景，忽视了使用情境对用户体验的关键影响。作者构建了包含领域、物理环境、用户和角色四个维度的情境框架，并通过针对四种典型SAR（养老院服务机器人、医院医疗助手、COVID-19巡检机器人、家用个人助手）的在线问卷调研，收集了228名潜在用户对机器人期望特征和视觉品质的反馈。结果表明，用户对机器人外观和功能特性的需求会随使用场景发生显著变化。

## 核心内容
### 研究背景与问题
- 机器人视觉品质（VQs）直接影响用户对其特性的感知及行为态度
- 当前SAR制造商常将同一外观设计部署于不同场景，缺乏科学化设计方法
- 需建立考虑情境差异的SAR视觉设计框架

### 四层情境框架
1. **领域（Domain）**：SAR存在的应用领域（如医疗、养老）
2. **物理环境（Physical Environment）**：部署空间特征（如医院走廊、家庭客厅）
3. **用户（Users）**：目标用户群体特征（如老年人、医护人员）
4. **角色（Role）**：机器人承担的功能角色（如服务、医疗辅助）

### 实验设计
- 方法：在线问卷调研（N=228）
- 测试场景：四种SAR用例
  - 养老院/退休社区服务机器人
  - 医院环境医疗助手机器人
  - COVID-19巡检机器人
  - 家用个人助手机器人
- 测量指标：用户对机器人期望特性（desired characteristics）和视觉品质（visual qualities）的评分

### 关键发现
- 用户对机器人期望特性在不同场景间存在显著差异（p<0.05）
- 视觉品质偏好随使用情境变化：例如医疗场景更强调专业感，家用场景更注重亲和力
- 结论验证了“一种设计无法适应所有情境”的核心假设，为SAR情境化设计提供了实证依据

## Overview
Robots' visual qualities (VQs) impact people's perception of their characteristics and affect users' behaviors and attitudes toward the robot. Recent years point toward a growing need for Socially Assistive Robots (SARs) in various contexts and functions, interacting with various users. Since SAR types have functional differences, the user experience must vary by the context of use, functionality, user characteristics, and environmental conditions. Still, SAR manufacturers often design and deploy the same robotic embodiment for diverse contexts. We argue that the visual design of SARs requires a more scientific approach considering their multiple evolving roles in future society. In this work, we define four contextual layers: the domain in which the SAR exists, the physical environment, its intended users, and the robot's role. Via an online questionnaire, we collected potential users' expectations regarding the desired characteristics and visual qualities of four different SARs: a service robot for an assisted living/retirement residence facility, a medical assistant robot for a hospital environment, a COVID-19 officer robot, and a personal assistant robot for domestic use. Results indicated that users' expectations differ regarding the robot's desired characteristics and the anticipated visual qualities for each context and use case.

## 参考
- http://arxiv.org/abs/2211.04163v1

## 개요
이 연구는 현재 사회적 보조 로봇(SAR) 제조업체들이 동일한 외관 디자인을 다양한 상황에 적용하면서, 사용 맥락이 사용자 경험에 미치는 핵심적 영향을 간과하고 있음을 지적한다. 저자는 도메인, 물리적 환경, 사용자, 역할의 네 가지 차원을 포함하는 상황 프레임워크를 구축하고, 네 가지 대표적인 SAR(요양원 서비스 로봇, 병원 의료 보조 로봇, COVID-19 순찰 로봇, 가정용 개인 비서 로봇)을 대상으로 한 온라인 설문 조사를 통해 228명의 잠재 사용자로부터 로봇의 기대 특성과 시각적 품질에 대한 피드백을 수집했다. 결과는 사용자의 로봇 외관 및 기능 특성에 대한 요구가 사용 상황에 따라 유의미하게 변화함을 보여준다.

## 핵심 내용
### 연구 배경 및 문제
- 로봇의 시각적 품질(VQs)은 사용자가 그 특성을 인식하고 행동 태도를 형성하는 데 직접적인 영향을 미친다
- 현재 SAR 제조업체들은 동일한 외관 디자인을 다양한 상황에 배치하는 경우가 많아 과학적 설계 방법이 부족하다
- 상황 차이를 고려한 SAR 시각 설계 프레임워크 구축이 필요하다

### 4계층 상황 프레임워크
1. **도메인(Domain)**: SAR이 존재하는 응용 분야(예: 의료, 요양)
2. **물리적 환경(Physical Environment)**: 배치 공간의 특성(예: 병원 복도, 가정 거실)
3. **사용자(Users)**: 목표 사용자 집단의 특성(예: 노인, 의료진)
4. **역할(Role)**: 로봇이 수행하는 기능적 역할(예: 서비스, 의료 보조)

### 실험 설계
- 방법: 온라인 설문 조사(N=228)
- 테스트 시나리오: 네 가지 SAR 사용 사례
  - 요양원/은퇴 커뮤니티 서비스 로봇
  - 병원 환경 의료 보조 로봇
  - COVID-19 순찰 로봇
  - 가정용 개인 비서 로봇
- 측정 지표: 사용자가 로봇에 기대하는 특성(desired characteristics) 및 시각적 품질(visual qualities)에 대한 평가

### 핵심 발견
- 사용자가 기대하는 로봇 특성은 상황 간에 유의미한 차이를 보였다(p<0.05)
- 시각적 품질 선호도는 사용 맥락에 따라 변화한다: 예를 들어 의료 상황에서는 전문성이 더 강조되고, 가정 상황에서는 친근감이 더 중시된다
- 결론은 "하나의 디자인이 모든 상황에 적합할 수 없다"는 핵심 가설을 검증하며, SAR 상황 기반 설계를 위한 실증적 근거를 제공한다

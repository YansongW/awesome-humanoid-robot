---
$id: ent_paper_li_usability_of_a_robots_realisti_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Usability of a Robot's Realistic Facial Expressions and Peripherals in Autistic Children's Therapy
  zh: 机器人真实面部表情及外设在自闭症儿童治疗中的可用性研究
  ko: 자폐 아동 치료에서 로봇의 사실적 표정 및 주변 장치의 사용성
summary:
  en: This paper reports usability tests in which 19 autistic children interacted with a Zeno humanoid robot and a therapist
    during emotion-learning activities, comparing realistic corpus-based and live-mirrored facial expressions with exaggerated
    expressions and evaluating tablet and tangible squishy peripherals for child-led control.
  zh: 本文报告了19名自闭症儿童在情绪学习活动中与Zeno人形机器人及治疗师互动的可用性测试。研究对比了基于语料库的真实面部表情与实时镜像表情相对于夸张表情的效果，并评估了平板电脑与触觉软玩具两种外围设备在儿童主导控制中的作用。核心发现是真实表情效果不如夸张表情，且触觉软玩具更具吸引力。
  ko: 본 논문은 19명의 자폐 아동이 치료사와 함께 Zeno 휴머노이드 로봇을 이용한 감정 학습 활동에 참여한 사용성 테스트를 보고하며, 코퍼스 기반 사실적 표정과 실시간 거울 표정을 과장된 표정과 비교하고 아동
    주도형 제어를 위한 태블릿과 촉각 스퀴시 주변 장치를 평가한다.
domains:
- 11_applications_markets
- 06_design_engineering
- 02_components
layers:
- midstream
- upstream
- validation_markets
functional_roles:
- knowledge
- system
tags:
- autism_therapy
- robot_assisted_therapy
- facial_expressions
- zeno_robot
- child_robot_interaction
- tangible_interface
- tablet_interface
- emotion_learning
- assistive_robotics
- live_mirroring
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2007.12236v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (862 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Usability of a Robot's Realistic Facial Expressions and Peripherals in Autistic Children's Therapy
  url: https://arxiv.org/abs/2007.12236
  date: '2020'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
该研究针对机器人辅助自闭症治疗中表情设计这一挑战，通过可用性测试评估了机器人面部表情的真实性及外围设备对儿童主导情绪学习活动的影响。19名自闭症儿童与小型人形机器人及成人治疗师参与了多项情绪学习任务，机器人表情分为基于现有数据库的真实表情和实时镜像表情两种类型，同时使用了平板电脑或触觉软玩具作为儿童控制活动的工具。结果显示，两种真实表情均不如夸张表情有效，其中镜像表情对儿童而言不够直观；平板电脑虽可用但需改进反馈与延迟，而触觉软玩具则成为有效的互动辅助工具。

## 核心内容
### 研究背景与目标
- 机器人辅助治疗是自闭症儿童的新兴疗法，但设计有效的机器人行为仍是挑战。
- 本研究旨在评估机器人面部表情的真实性（基于语料库 vs. 实时镜像）及外围设备（平板电脑 vs. 触觉软玩具）对儿童主导情绪学习活动的影响。

### 实验设置
- **参与者**：19名自闭症儿童，与Zeno人形机器人及一名成人治疗师互动。
- **表情条件**：
  - 基于语料库的真实表情：从预存数据库生成。
  - 实时镜像表情：通过摄像头实时映射儿童面部表情。
  - 夸张表情：作为对比基准。
- **外围设备**：
  - 平板电脑：用于儿童选择情绪或控制活动。
  - 触觉软玩具（squishies）：可挤压的实体玩具，用于触发机器人反应。

### 关键发现
- **表情效果**：
  - 两种真实表情（语料库与镜像）均不如夸张表情有效，儿童对夸张表情反应更积极。
  - 实时镜像表情对儿童而言不够直观，可能导致困惑或参与度下降。
- **外围设备**：
  - 平板电脑可用，但需增加反馈（如视觉或听觉提示）并降低延迟以提升体验。
  - 触觉软玩具作为实体互动工具，能有效吸引儿童注意力并促进参与。

### 结论
- 在自闭症儿童治疗中，机器人使用夸张表情比真实表情更有效，而触觉外围设备比平板电脑更具互动优势。
- 未来设计应优先考虑表情的夸张化与实体交互的直观性，以优化机器人辅助治疗效果。

## Overview
Robot-assisted therapy is an emerging form of therapy for autistic children, although designing effective robot behaviors is a challenge for effective implementation of such therapy. A series of usability tests assessed trends in the effectiveness of modelling a robot's facial expressions on realistic facial expressions and of adding peripherals enabling child-led control of emotion learning activities with autistic children. Nineteen autistic children interacted with a small humanoid robot and an adult therapist in several emotion-learning activities that featured realistic facial expressions modelled on either a pre-existing database or live facial mirroring, and that used peripherals (tablets or tangible 'squishies') to enable child-led activities. Both types of realistic facial expressions by the robot were less effective than exaggerated expressions, with the mirroring being unintuitive for children. The tablet was usable but required more feedback and lower latency, while the tactile tangibles were engaging aids.

## 参考
- http://arxiv.org/abs/2007.12236v1

## 개요
이 연구는 로봇 보조 자폐증 치료에서 표정 설계라는 도전 과제를 대상으로, 사용성 테스트를 통해 로봇 얼굴 표정의 실제성과 주변 기기가 아동 주도 감정 학습 활동에 미치는 영향을 평가했습니다. 19명의 자폐 아동이 소형 휴머노이드 로봇 및 성인 치료사와 여러 감정 학습 과제에 참여했으며, 로봇 표정은 기존 데이터베이스 기반 실제 표정과 실시간 미러링 표정의 두 유형으로 나뉘었고, 동시에 태블릿 PC 또는 촉각 소프트 토이가 아동의 활동 제어 도구로 사용되었습니다. 결과에 따르면 두 실제 표정 모두 과장된 표정보다 효과적이지 않았으며, 미러링 표정은 아동에게 직관적이지 않았습니다. 태블릿 PC는 사용 가능했지만 피드백과 지연 시간 개선이 필요했고, 촉각 소프트 토이는 효과적인 상호작용 보조 도구로 확인되었습니다.

## 핵심 내용
### 연구 배경 및 목표
- 로봇 보조 치료는 자폐 아동을 위한 새로운 치료법이지만, 효과적인 로봇 행동 설계는 여전히 도전 과제입니다.
- 본 연구는 로봇 얼굴 표정의 실제성(코퍼스 기반 vs. 실시간 미러링) 및 주변 기기(태블릿 PC vs. 촉각 소프트 토이)가 아동 주도 감정 학습 활동에 미치는 영향을 평가하는 것을 목표로 합니다.

### 실험 설정
- **참가자**: 19명의 자폐 아동, Zeno 휴머노이드 로봇 및 성인 치료사와 상호작용.
- **표정 조건**:
  - 코퍼스 기반 실제 표정: 사전 저장된 데이터베이스에서 생성.
  - 실시간 미러링 표정: 카메라를 통해 아동의 얼굴 표정을 실시간 매핑.
  - 과장된 표정: 비교 기준으로 사용.
- **주변 기기**:
  - 태블릿 PC: 아동이 감정을 선택하거나 활동을 제어하는 데 사용.
  - 촉각 소프트 토이(squishies): 압축 가능한 실물 장난감으로, 로봇 반응을 유발하는 데 사용.

### 주요 발견
- **표정 효과**:
  - 두 실제 표정(코퍼스 기반 및 미러링) 모두 과장된 표정보다 효과적이지 않았으며, 아동은 과장된 표정에 더 긍정적으로 반응했습니다.
  - 실시간 미러링 표정은 아동에게 직관적이지 않아 혼란 또는 참여도 저하를 초래할 수 있습니다.
- **주변 기기**:
  - 태블릿 PC는 사용 가능하지만, 피드백(예: 시각적 또는 청각적 신호)을 추가하고 지연 시간을 줄여 경험을 개선해야 합니다.
  - 촉각 소프트 토이는 실물 상호작용 도구로서 아동의 주의를 효과적으로 끌고 참여를 촉진합니다.

### 결론
- 자폐 아동 치료에서 로봇은 실제 표정보다 과장된 표정이 더 효과적이며, 촉각 주변 기기가 태블릿 PC보다 상호작용 측면에서 더 유리합니다.
- 향후 설계는 표정의 과장화와 실물 상호작용의 직관성을 우선시하여 로봇 보조 치료 효과를 최적화해야 합니다.

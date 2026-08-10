---
$id: ent_paper_behavior_robot_suite_streamlin_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BEHAVIOR Robot Suite: Streamlining Real-World Whole-Body Manipulation for Everyday Household Activities'
  zh: 'BEHAVIOR Robot Suite: Streamlining Real-World Whole-Body Manipulation for Everyday Household Activities'
  ko: 'BEHAVIOR Robot Suite: Streamlining Real-World Whole-Body Manipulation for Everyday Household Activities'
summary:
  en: 'BEHAVIOR Robot Suite: Streamlining Real-World Whole-Body Manipulation for Everyday Household Activities is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
  zh: BEHAVIOR Robot Suite (BRS) 是一个面向日常家务活动的全身操控框架，由研究团队于2025年提出。其核心贡献在于：基于双臂轮式机器人（配备4自由度躯干），集成了低成本全身遥操作数据采集接口与全身视觉运动策略学习算法，并在五项复杂家务任务中验证了有效性。
  ko: 'BEHAVIOR Robot Suite: Streamlining Real-World Whole-Body Manipulation for Everyday Household Activities is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- behavior_robot_suite
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.05652v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (825 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'BEHAVIOR Robot Suite: Streamlining Real-World Whole-Body Manipulation for Everyday Household Activities (arXiv)'
  url: https://arxiv.org/abs/2503.05652
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'BEHAVIOR Robot Suite: Streamlining Real-World Whole-Body Manipulation for Everyday Household Activities project
    page'
  url: https://behavior-robot-suite.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现实世界的家务任务对移动操作机器人提出严峻挑战。现有基准分析表明，任务成功依赖于三项全身控制能力：双臂协调、稳定精准导航以及末端执行器的大范围可达性。这些能力需要精心的硬件设计，但由此带来的系统复杂性又进一步增加了视觉运动策略学习的难度。为此，BRS 框架应运而生，它采用双臂轮式机器人平台，通过4自由度躯干增强灵活性，并配套开发了经济高效的全身遥操作接口用于数据采集，以及全新的全身视觉运动策略学习算法。该框架在五项强调核心能力并引入额外复杂性的家务任务中进行了评估，涵盖长距离导航、与铰接/可变形物体交互以及狭小空间操作。

## 核心内容
### 核心挑战与设计动机
- 现实家务任务对移动操作机器人提出三大核心要求：**双臂协调**、**稳定精准导航**、**末端执行器大范围可达性**。
- 现有机器人基准分析表明，满足这些要求需精心设计硬件，但系统复杂性会显著增加**视觉运动策略学习**的难度。

### BEHAVIOR Robot Suite (BRS) 框架
- **机器人平台**：采用**双臂轮式机器人**，配备**4自由度躯干**，以增强全身灵活性。
- **数据采集**：集成**低成本全身遥操作接口**，用于高效收集真实世界操作数据。
- **策略学习**：提出**全身视觉运动策略学习算法**，直接利用遥操作数据训练策略。

### 实验评估
- **任务设置**：在**五项挑战性家务任务**上评估，这些任务不仅强调三大核心能力，还引入额外复杂性：
  - 长距离导航
  - 与铰接物体和可变形物体交互
  - 在狭小空间内操作
- **关键结论**：BRS 的集成式机器人本体、数据采集接口和学习框架，为在真实世界日常家务任务中实现全身操控迈出了重要一步。

### 开源信息
- BRS 已开源，代码与文档可在 https://behavior-robot-suite.github.io/ 获取。

## Overview
Real-world household tasks present significant challenges for mobile manipulation robots. An analysis of existing robotics benchmarks reveals that successful task performance hinges on three key whole-body control capabilities: bimanual coordination, stable and precise navigation, and extensive end-effector reachability. Achieving these capabilities requires careful hardware design, but the resulting system complexity further complicates visuomotor policy learning. To address these challenges, we introduce the BEHAVIOR Robot Suite (BRS), a comprehensive framework for whole-body manipulation in diverse household tasks. Built on a bimanual, wheeled robot with a 4-DoF torso, BRS integrates a cost-effective whole-body teleoperation interface for data collection and a novel algorithm for learning whole-body visuomotor policies. We evaluate BRS on five challenging household tasks that not only emphasize the three core capabilities but also introduce additional complexities, such as long-range navigation, interaction with articulated and deformable objects, and manipulation in confined spaces. We believe that BRS's integrated robotic embodiment, data collection interface, and learning framework mark a significant step toward enabling real-world whole-body manipulation for everyday household tasks. BRS is open-sourced at https://behavior-robot-suite.github.io/

## 参考
- http://arxiv.org/abs/2503.05652v2

## 개요
현실 세계의 가사 작업은 이동 조작 로봇에게 심각한 도전 과제를 제기한다. 기존 벤치마크 분석에 따르면, 작업 성공은 세 가지 전신 제어 능력에 의존한다: **양팔 협조**, **안정적이고 정밀한 내비게이션**, 그리고 **엔드 이펙터의 광범위한 도달성**. 이러한 능력은 세심한 하드웨어 설계를 요구하지만, 그로 인한 시스템 복잡성은 시각 운동 정책 학습을 더욱 어렵게 만든다. 이를 위해 BRS 프레임워크가 등장했으며, 이는 양팔 바퀴형 로봇 플랫폼을 채택하고, 4자유도 몸통으로 유연성을 강화하며, 데이터 수집을 위한 경제적인 전신 텔레오퍼레이션 인터페이스와 새로운 전신 시각 운동 정책 학습 알고리즘을 함께 개발했다. 이 프레임워크는 핵심 능력을 강조하고 추가적인 복잡성을 도입하는 다섯 가지 가사 작업에서 평가되었으며, 장거리 내비게이션, 관절형/변형 가능한 물체와의 상호작용, 그리고 좁은 공간에서의 조작을 포함한다.

## 핵심 내용
### 핵심 도전 과제와 설계 동기
- 현실 가사 작업은 이동 조작 로봇에게 세 가지 핵심 요구 사항을 제기한다: **양팔 협조**, **안정적이고 정밀한 내비게이션**, **엔드 이펙터의 광범위한 도달성**.
- 기존 로봇 벤치마크 분석에 따르면, 이러한 요구 사항을 충족하려면 세심한 하드웨어 설계가 필요하지만, 시스템 복잡성은 **시각 운동 정책 학습**의 어려움을 크게 증가시킨다.

### BEHAVIOR Robot Suite (BRS) 프레임워크
- **로봇 플랫폼**: **양팔 바퀴형 로봇**을 채택하고, **4자유도 몸통**을 장착하여 전신 유연성을 강화한다.
- **데이터 수집**: **저비용 전신 텔레오퍼레이션 인터페이스**를 통합하여 실제 세계 조작 데이터를 효율적으로 수집한다.
- **정책 학습**: **전신 시각 운동 정책 학습 알고리즘**을 제안하여 텔레오퍼레이션 데이터를 직접 활용해 정책을 훈련한다.

### 실험 평가
- **작업 설정**: **다섯 가지 도전적인 가사 작업**에서 평가하며, 이 작업들은 세 가지 핵심 능력을 강조할 뿐만 아니라 추가적인 복잡성을 도입한다:
  - 장거리 내비게이션
  - 관절형 물체 및 변형 가능한 물체와의 상호작용
  - 좁은 공간에서의 조작
- **핵심 결론**: BRS의 통합된 로봇 본체, 데이터 수집 인터페이스, 학습 프레임워크는 실제 세계 일상 가사 작업에서 전신 조작을 실현하는 중요한 진전을 이루었다.

### 오픈소스 정보
- BRS는 오픈소스로 공개되었으며, 코드와 문서는 https://behavior-robot-suite.github.io/ 에서 확인할 수 있다.

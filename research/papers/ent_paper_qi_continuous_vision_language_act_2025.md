---
$id: ent_paper_qi_continuous_vision_language_act_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Continuous Vision-Language-Action Co-Learning with Semantic-Physical Alignment for Behavioral Cloning
  zh: CCoL
  ko: Continuous Vision-Language-Action Co-Learning with Semantic-Physical Alignment for Behavioral Cloning
summary:
  en: Continuous Vision-Language-Action Co-Learning with Semantic-Physical Alignment for Behavioral Cloning (CCoL), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Nankai University, The Hong Kong Polytechnic
    University, The Education University of Hong Kong, City University of Hong Kong.
  zh: CCoL 是南开大学、香港理工大学、香港教育大学及香港城市大学于 2025 年联合提出的大型视觉-语言-动作模型，用于机器人操作中的行为克隆。其核心贡献在于通过语义-物理对齐的连续共学习，解决了现有方法中动作执行的物理不连续性与语义-物理错位问题，实现了更平滑、更精准的动作轨迹生成。
  ko: Continuous Vision-Language-Action Co-Learning with Semantic-Physical Alignment for Behavioral Cloning (CCoL), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Nankai University, The Hong Kong Polytechnic
    University, The Education University of Hong Kong, City University of Hong Kong.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ccol
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.14396v5. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (674 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Continuous Vision-Language-Action Co-Learning with Semantic-Physical Alignment for Behavioral Cloning (arXiv)
  url: https://arxiv.org/abs/2511.14396
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: CCoL source
  url: https://doi.org/10.48550/arXiv.2511.14396
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
语言条件操作通过行为克隆从人类演示中学习控制策略，是具身智能的基础。然而，现有方法常因物理不连续性和语义-物理错位导致动作克隆不准确与执行中断。CCoL 框架通过视觉、语言与本体感知输入的连续共学习，生成鲁棒且平滑的执行轨迹。它利用双向交叉注意力机制将语言语义锚定到视觉运动表征中，从而学习上下文信息以生成动作，成功克服了语义-物理错位问题。实验表明，CCoL 在三个仿真套件上平均相对提升 8.0%，在人类演示的双臂插入任务中最高提升 19.2%，并在真实世界的 7 自由度机器人上验证了其在未见及噪声物体状态下的泛化能力。

## 核心内容
### 方法架构
CCoL 是一个基于行为克隆的连续共学习框架，其核心设计包括：
- **连续共学习**：同时处理视觉、语言和本体感知（如机器人内部状态）输入，确保时间上一致的动作执行。
- **语义-物理对齐**：通过双向交叉注意力机制，将语言语义锚定到视觉运动表征中，学习上下文信息以指导动作生成，从而消除语义与物理动作之间的错位。

### 实验设置与结果
- **仿真实验**：在三个仿真套件上进行评估，CCoL 平均相对提升 8.0%。在人类演示的双臂插入任务中，相对增益高达 19.2%。
- **真实世界测试**：在 7 自由度机器人上部署，CCoL 在未见及噪声物体状态下展现出良好的泛化能力，验证了其在实际场景中的鲁棒性。

### 结论
CCoL 通过连续共学习与语义-物理对齐，有效缓解了行为克隆中的累积误差与执行中断问题，为机器人操作提供了更稳定、更精准的解决方案。

## Overview
Language-conditioned manipulation facilitates human-robot interaction via behavioral cloning (BC), which learns control policies from human demonstrations and serves as a cornerstone of embodied AI. Overcoming compounding errors in sequential action decisions remains a central challenge to improving BC performance. Existing approaches mitigate compounding errors through data augmentation, expressive representation, or temporal abstraction. However, they suffer from physical discontinuities and semantic-physical misalignment, leading to inaccurate action cloning and intermittent execution. In this paper, we present Continuous vision-language-action Co-Learning with Semantic-Physical Alignment (CCoL), a novel BC framework that ensures temporally consistent execution and fine-grained semantic grounding. It generates robust and smooth action execution trajectories through continuous co-learning across vision, language, and proprioceptive inputs (e.g., robot internal states). Meanwhile, we anchor language semantics to visuomotor representations by a bidirectional cross-attention to learn contextual information for action generation, successfully overcoming the problem of semantic-physical misalignment. Extensive experiments show that CCoL achieves an average 8.0% relative improvement across three simulation suites, with up to 19.2% relative gain in human-demonstrated bimanual insertion tasks. Real-world tests on a 7-DoF robot further confirm CCoL's generalization under unseen and noisy object states.

## 参考
- http://arxiv.org/abs/2511.14396v5

## 개요
언어 조건 조작은 인간 시연으로부터 행동 클로닝을 통해 제어 정책을 학습하는 것으로, 구현 지능의 기초입니다. 그러나 기존 방법들은 종종 물리적 불연속성과 의미-물리적 불일치로 인해 동작 클로닝의 부정확성과 실행 중단을 초래합니다. CCoL 프레임워크는 시각, 언어 및 고유 감각 입력의 연속 공동 학습을 통해 견고하고 매끄러운 실행 궤적을 생성합니다. 이는 양방향 교차 주의 메커니즘을 활용하여 언어 의미를 시각적 운동 표현에 고정함으로써 문맥 정보를 학습하여 동작을 생성하며, 의미-물리적 불일치 문제를 성공적으로 극복합니다. 실험 결과, CCoL은 세 가지 시뮬레이션 스위트에서 평균 상대적 향상 8.0%, 인간 시연의 이중 팔 삽입 작업에서 최대 19.2% 향상을 보였으며, 실제 7자유도 로봇에서 보지 못한 객체 상태 및 노이즈가 있는 객체 상태에서의 일반화 능력을 검증했습니다.

## 핵심 내용
### 방법 아키텍처
CCoL은 행동 클로닝 기반의 연속 공동 학습 프레임워크로, 핵심 설계는 다음과 같습니다:
- **연속 공동 학습**: 시각, 언어 및 고유 감각(예: 로봇 내부 상태) 입력을 동시에 처리하여 시간적으로 일관된 동작 실행을 보장합니다.
- **의미-물리적 정렬**: 양방향 교차 주의 메커니즘을 통해 언어 의미를 시각적 운동 표현에 고정하고, 문맥 정보를 학습하여 동작 생성을 지도함으로써 의미와 물리적 동작 간의 불일치를 제거합니다.

### 실험 설정 및 결과
- **시뮬레이션 실험**: 세 가지 시뮬레이션 스위트에서 평가되었으며, CCoL은 평균 상대적 향상 8.0%를 달성했습니다. 인간 시연의 이중 팔 삽입 작업에서는 상대적 이득이 최대 19.2%에 달했습니다.
- **실제 세계 테스트**: 7자유도 로봇에 배포되어, CCoL은 보지 못한 객체 상태 및 노이즈가 있는 객체 상태에서 우수한 일반화 능력을 보여주며 실제 시나리오에서의 견고성을 검증했습니다.

### 결론
CCoL은 연속 공동 학습과 의미-물리적 정렬을 통해 행동 클로닝의 누적 오류 및 실행 중단 문제를 효과적으로 완화하며, 로봇 조작에 더 안정적이고 정밀한 솔루션을 제공합니다.

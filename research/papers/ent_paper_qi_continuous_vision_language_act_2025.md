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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.14396v5. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
언어 조건부 조작은 인간 시연으로부터 제어 정책을 학습하고 구현형 AI의 초석이 되는 행동 복제(BC)를 통해 인간-로봇 상호작용을 촉진합니다. 순차적 행동 결정에서 누적 오류를 극복하는 것은 BC 성능 향상의 핵심 과제로 남아 있습니다. 기존 접근법은 데이터 증강, 표현적 표현, 또는 시간적 추상화를 통해 누적 오류를 완화합니다. 그러나 이들은 물리적 불연속성과 의미-물리적 불일치로 인해 부정확한 행동 복제와 간헐적 실행을 초래합니다. 본 논문에서는 시간적으로 일관된 실행과 세분화된 의미 기반을 보장하는 새로운 BC 프레임워크인 연속적 시각-언어-행동 공동 학습 및 의미-물리적 정렬(CCoL)을 제시합니다. 이는 시각, 언어, 고유수용성 입력(예: 로봇 내부 상태)에 걸친 연속적 공동 학습을 통해 강건하고 부드러운 행동 실행 궤적을 생성합니다. 동시에, 양방향 교차 주의를 통해 언어 의미를 시각운동 표현에 고정시켜 행동 생성을 위한 맥락 정보를 학습함으로써 의미-물리적 불일치 문제를 성공적으로 극복합니다. 광범위한 실험을 통해 CCoL은 세 가지 시뮬레이션 제품군에서 평균 8.0%의 상대적 개선을 달성했으며, 인간이 시연한 양손 삽입 작업에서는 최대 19.2%의 상대적 이득을 보였습니다. 7자유도 로봇을 사용한 실제 환경 테스트는 또한 보이지 않고 잡음이 있는 객체 상태에서 CCoL의 일반화 능력을 추가로 확인했습니다.

## 핵심 내용
언어 조건부 조작은 인간 시연으로부터 제어 정책을 학습하고 구현형 AI의 초석이 되는 행동 복제(BC)를 통해 인간-로봇 상호작용을 촉진합니다. 순차적 행동 결정에서 누적 오류를 극복하는 것은 BC 성능 향상의 핵심 과제로 남아 있습니다. 기존 접근법은 데이터 증강, 표현적 표현, 또는 시간적 추상화를 통해 누적 오류를 완화합니다. 그러나 이들은 물리적 불연속성과 의미-물리적 불일치로 인해 부정확한 행동 복제와 간헐적 실행을 초래합니다. 본 논문에서는 시간적으로 일관된 실행과 세분화된 의미 기반을 보장하는 새로운 BC 프레임워크인 연속적 시각-언어-행동 공동 학습 및 의미-물리적 정렬(CCoL)을 제시합니다. 이는 시각, 언어, 고유수용성 입력(예: 로봇 내부 상태)에 걸친 연속적 공동 학습을 통해 강건하고 부드러운 행동 실행 궤적을 생성합니다. 동시에, 양방향 교차 주의를 통해 언어 의미를 시각운동 표현에 고정시켜 행동 생성을 위한 맥락 정보를 학습함으로써 의미-물리적 불일치 문제를 성공적으로 극복합니다. 광범위한 실험을 통해 CCoL은 세 가지 시뮬레이션 제품군에서 평균 8.0%의 상대적 개선을 달성했으며, 인간이 시연한 양손 삽입 작업에서는 최대 19.2%의 상대적 이득을 보였습니다. 7자유도 로봇을 사용한 실제 환경 테스트는 또한 보이지 않고 잡음이 있는 객체 상태에서 CCoL의 일반화 능력을 추가로 확인했습니다.

## 参考
- http://arxiv.org/abs/2511.14396v5

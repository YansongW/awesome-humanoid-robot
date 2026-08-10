---
$id: ent_paper_li_urbanvla_a_vision_language_act_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'UrbanVLA: A Vision-Language-Action Model for Urban Micromobility'
  zh: UrbanVLA
  ko: 'UrbanVLA: A Vision-Language-Action Model for Urban Micromobility'
summary:
  en: 'UrbanVLA: A Vision-Language-Action Model for Urban Micromobility (UrbanVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Galbot, USTC, BAAI.'
  zh: UrbanVLA 是由北京大学、Galbot、中国科学技术大学和 BAAI 于 2025 年提出的大规模视觉-语言-动作模型，专为城市微型移动机器人设计。其核心贡献在于提出一种路径条件化的 VLA 框架，通过两阶段训练（监督微调与强化微调）实现从低层导航（如避障）到高层规划（如路径-视觉对齐）的协同优化，并在
    MetaUrban 的 SocialNav 任务中超越强基线 55% 以上。
  ko: 'UrbanVLA: A Vision-Language-Action Model for Urban Micromobility (UrbanVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Galbot, USTC, BAAI.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- urbanvla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.23576v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (835 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'UrbanVLA: A Vision-Language-Action Model for Urban Micromobility (arXiv)'
  url: https://arxiv.org/abs/2510.23576
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: UrbanVLA source
  url: https://doi.org/10.48550/arXiv.2510.23576
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
UrbanVLA 针对城市环境中配送机器人等应用面临的挑战——需在动态非结构化场景下遵循长时程路径指令——提出了一种路径条件化的视觉-语言-动作框架。该方法在运行时显式对齐噪声路径路点与视觉观测，并据此规划机器人轨迹。通过两阶段训练流程：首先利用模拟环境和网络视频解析的轨迹进行监督微调，随后结合模拟与真实数据执行强化微调，显著提升了模型在真实场景中的安全性与适应性。实验表明，UrbanVLA 在 MetaUrban 的 SocialNav 任务中性能优于现有方法 55% 以上，并成功实现了可靠的真实世界导航。

## 核心内容
### 方法概述
UrbanVLA 的核心是路径条件化的 VLA 框架，其关键创新在于：
- **路径-视觉对齐**：在机器人执行过程中，显式地将带有噪声的路径路点与实时视觉观测进行匹配，确保高层路径指令与低层感知的一致性。
- **轨迹规划**：基于对齐后的信息，生成连续、安全的机器人运动轨迹，兼顾点目标到达与障碍物规避。

### 两阶段训练流程
1. **监督微调**：利用模拟环境（如 MetaUrban）生成的合成数据，以及从网络视频中解析出的真实轨迹，对模型进行初步训练，使其掌握基础导航技能。
2. **强化微调**：结合模拟与真实世界数据，通过强化学习进一步优化模型。该阶段重点提升机器人在动态城市环境中的安全决策能力与适应性，例如应对突发行人或交通变化。

### 实验设置与结果
- **基准测试**：在 MetaUrban 的 SocialNav 任务中评估，该任务要求机器人在密集社交场景下完成长距离导航。
- **性能对比**：UrbanVLA 在成功率、路径效率和安全指标上均显著优于现有强基线方法，整体性能提升超过 55%。
- **真实世界验证**：在真实城市环境中部署时，模型展现出对大规模场景的扩展性（如跨街区导航）和对不确定性（如光照变化、动态障碍物）的鲁棒性，验证了其实际应用潜力。

## Overview
Urban micromobility applications, such as delivery robots, demand reliable navigation across large-scale urban environments while following long-horizon route instructions. This task is particularly challenging due to the dynamic and unstructured nature of real-world city areas, yet most existing navigation methods remain tailored to short-scale and controllable scenarios. Effective urban micromobility requires two complementary levels of navigation skills: low-level capabilities such as point-goal reaching and obstacle avoidance, and high-level capabilities, such as route-visual alignment. To this end, we propose UrbanVLA, a route-conditioned Vision-Language-Action (VLA) framework designed for scalable urban navigation. Our method explicitly aligns noisy route waypoints with visual observations during execution, and subsequently plans trajectories to drive the robot. To enable UrbanVLA to master both levels of navigation, we employ a two-stage training pipeline. The process begins with Supervised Fine-Tuning (SFT) using simulated environments and trajectories parsed from web videos. This is followed by Reinforcement Fine-Tuning (RFT) on a mixture of simulation and real-world data, which enhances the model's safety and adaptability in real-world settings. Experiments demonstrate that UrbanVLA surpasses strong baselines by more than 55% in the SocialNav task on MetaUrban. Furthermore, UrbanVLA achieves reliable real-world navigation, showcasing both scalability to large-scale urban environments and robustness against real-world uncertainties.

## 参考
- http://arxiv.org/abs/2510.23576v1

## 개요
UrbanVLA는 도시 환경에서 배달 로봇과 같은 애플리케이션이 직면한 과제——동적 비구조적 상황에서 장기 경로 명령을 따르는 것——에 대응하기 위해 경로 조건화된 비전-언어-동작 프레임워크를 제안합니다. 이 방법은 실행 중에 노이즈가 있는 경로 웨이포인트와 시각적 관측을 명시적으로 정렬하고, 이를 기반으로 로봇 궤적을 계획합니다. 두 단계 훈련 프로세스를 통해——먼저 시뮬레이션 환경과 웹 비디오에서 해석된 궤적을 사용한 지도 미세 조정, 이후 시뮬레이션 및 실제 데이터를 결합한 강화 미세 조정——실제 환경에서 모델의 안전성과 적응성을 크게 향상시킵니다. 실험 결과, UrbanVLA는 MetaUrban의 SocialNav 작업에서 기존 방법보다 55% 이상 우수한 성능을 보였으며, 신뢰할 수 있는 실제 세계 내비게이션을 성공적으로 구현했습니다.

## 핵심 내용
### 방법 개요
UrbanVLA의 핵심은 경로 조건화된 VLA 프레임워크이며, 주요 혁신은 다음과 같습니다:
- **경로-시각 정렬**: 로봇 실행 중에 노이즈가 있는 경로 웨이포인트와 실시간 시각적 관측을 명시적으로 매칭하여, 고수준 경로 명령과 저수준 인식의 일관성을 보장합니다.
- **궤적 계획**: 정렬된 정보를 기반으로 연속적이고 안전한 로봇 운동 궤적을 생성하며, 목표 지점 도달과 장애물 회피를 동시에 고려합니다.

### 두 단계 훈련 프로세스
1. **지도 미세 조정**: 시뮬레이션 환경(예: MetaUrban)에서 생성된 합성 데이터와 웹 비디오에서 해석된 실제 궤적을 활용하여 모델을 초기 훈련시키고, 기본 내비게이션 기술을 습득하게 합니다.
2. **강화 미세 조정**: 시뮬레이션 및 실제 세계 데이터를 결합하여 강화 학습을 통해 모델을 추가로 최적화합니다. 이 단계는 동적 도시 환경에서 로봇의 안전 의사 결정 능력과 적응성(예: 갑작스러운 보행자나 교통 변화 대응)을 향상시키는 데 중점을 둡니다.

### 실험 설정 및 결과
- **벤치마크 테스트**: MetaUrban의 SocialNav 작업에서 평가되며, 이 작업은 밀집된 사회적 상황에서 로봇이 장거리 내비게이션을 완료해야 합니다.
- **성능 비교**: UrbanVLA는 성공률, 경로 효율성 및 안전 지표에서 기존 강력한 기준 방법보다 현저히 우수하며, 전체 성능이 55% 이상 향상되었습니다.
- **실제 세계 검증**: 실제 도시 환경에 배포할 때, 모델은 대규모 시나리오(예: 블록 간 내비게이션)에 대한 확장성과 불확실성(예: 조명 변화, 동적 장애물)에 대한 견고성을 보여주며, 실제 적용 가능성을 검증했습니다.

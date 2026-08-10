---
$id: ent_paper_wu_dejavu_towards_experience_feed_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Dejavu: Towards Experience Feedback Learning for Embodied Intelligence'
  zh: Dejavu
  ko: 'Dejavu: Towards Experience Feedback Learning for Embodied Intelligence'
summary:
  en: 'Dejavu: Towards Experience Feedback Learning for Embodied Intelligence (Dejavu), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University.'
  zh: Dejavu 是上海交通大学于 2025 年提出的一种面向机器人操作的大型视觉-语言-动作模型。其核心贡献在于提出了一种部署后学习框架，通过经验反馈网络（EFN）让冻结的 VLA 策略能够利用检索到的历史执行记忆来提升任务表现。
  ko: 'Dejavu: Towards Experience Feedback Learning for Embodied Intelligence (Dejavu), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dejavu
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.10181v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (753 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Dejavu: Towards Experience Feedback Learning for Embodied Intelligence (arXiv)'
  url: https://arxiv.org/abs/2510.10181
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Dejavu 旨在解决具身智能体在真实环境中部署后难以获取新知识以改进性能的根本限制。该框架通过一个经验反馈网络（EFN）来增强冻结的视觉-语言-动作（VLA）策略，EFN 能够检索与当前上下文相关的过往动作经验，并基于这些检索到的指导来调节动作预测。EFN 通过强化学习和语义相似度奖励进行训练，鼓励预测动作与当前观测下的历史行为对齐。在部署过程中，EFN 会持续用新轨迹扩充其记忆库，使智能体能够展现“从经验中学习”的能力。

## 核心内容
### 方法概述
Dejavu 提出了一种通用的部署后学习框架，其核心组件是经验反馈网络（EFN）。该网络在冻结的 VLA 策略基础上工作，通过检索与当前观测上下文相关的历史执行记忆来辅助动作预测。

### 架构细节
- **经验反馈网络（EFN）**：负责从记忆库中检索与当前观测语义相似的历史动作经验，并将这些检索到的指导信息作为条件输入到动作预测过程中。
- **训练机制**：EFN 采用强化学习进行训练，奖励函数基于语义相似度。该机制鼓励模型预测的动作与当前观测下过去成功的行为模式保持一致。
- **记忆扩展**：在部署阶段，EFN 会持续将新执行的任务轨迹添加到记忆库中，实现记忆的动态扩充，从而让智能体能够不断“从经验中学习”。

### 实验设置与结果
- **任务范围**：实验覆盖了多种具身操作任务，用于评估框架的适应性、鲁棒性和成功率。
- **关键发现**：与冻结的基线模型相比，EFN 在各项指标上均表现出显著提升。具体而言，EFN 增强了模型对未知环境的适应性，提高了面对干扰时的鲁棒性，并取得了更高的任务成功率。
- **项目页面**：更多细节可访问 https://dejavu2025.github.io/。

## Overview
Embodied agents face a fundamental limitation: once deployed in real-world environments, they cannot easily acquire new knowledge to improve task performance. In this paper, we propose Dejavu, a general post-deployment learning framework that augments a frozen Vision-Language-Action (VLA) policy with retrieved execution memories through an Experience Feedback Network (EFN). EFN identifies contextually relevant prior action experiences and conditions action prediction on the retrieved guidance. We train EFN with reinforcement learning and semantic similarity rewards, encouraging the predicted actions to align with past behaviors under the current observation. During deployment, EFN continually expands its memory with new trajectories, enabling the agent to exhibit ``learning from experience.'' Experiments across diverse embodied tasks show that EFN improves adaptability, robustness, and success rates over frozen baselines. Our Project Page is https://dejavu2025.github.io/.

## 参考
- http://arxiv.org/abs/2510.10181v3

## 개요
Dejavu는 실제 환경에 배포된 후 새로운 지식을 획득하여 성능을 개선하기 어려운 내재적 한계를 해결하기 위해 설계된 프레임워크입니다. 이 프레임워크는 경험 피드백 네트워크(EFN)를 통해 고정된 시각-언어-행동(VLA) 정책을 강화하며, EFN은 현재 맥락과 관련된 과거 행동 경험을 검색하고, 검색된 지침을 기반으로 행동 예측을 조정합니다. EFN은 강화 학습과 의미 유사도 보상을 통해 훈련되며, 예측된 행동이 현재 관측 하의 과거 행동과 정렬되도록 장려합니다. 배포 과정에서 EFN은 지속적으로 새로운 궤적으로 메모리 저장소를 확장하여, 에이전트가 "경험으로부터 학습하는" 능력을 보여줄 수 있게 합니다.

## 핵심 내용
### 방법 개요
Dejavu는 일반적인 배포 후 학습 프레임워크를 제안하며, 핵심 구성 요소는 경험 피드백 네트워크(EFN)입니다. 이 네트워크는 고정된 VLA 정책 위에서 작동하며, 현재 관측 맥락과 관련된 과거 실행 메모리를 검색하여 행동 예측을 보조합니다.

### 아키텍처 세부 사항
- **경험 피드백 네트워크(EFN)**: 메모리 저장소에서 현재 관측과 의미적으로 유사한 과거 행동 경험을 검색하고, 검색된 지침 정보를 행동 예측 과정의 조건 입력으로 사용합니다.
- **훈련 메커니즘**: EFN은 강화 학습을 통해 훈련되며, 보상 함수는 의미 유사도에 기반합니다. 이 메커니즘은 모델이 예측한 행동이 현재 관측 하의 과거 성공적인 행동 패턴과 일관성을 유지하도록 장려합니다.
- **메모리 확장**: 배포 단계에서 EFN은 지속적으로 새로 실행된 작업 궤적을 메모리 저장소에 추가하여 메모리의 동적 확장을 구현하며, 이를 통해 에이전트가 끊임없이 "경험으로부터 학습"할 수 있게 합니다.

### 실험 설정 및 결과
- **작업 범위**: 실험은 다양한 로봇 조작 작업을 포함하며, 프레임워크의 적응성, 견고성 및 성공률을 평가합니다.
- **주요 발견**: 고정된 기준 모델과 비교하여 EFN은 모든 지표에서 현저한 개선을 보였습니다. 구체적으로, EFN은 알 수 없는 환경에 대한 적응성을 강화하고, 간섭에 대한 견고성을 향상시키며, 더 높은 작업 성공률을 달성했습니다.
- **프로젝트 페이지**: 더 많은 세부 사항은 https://dejavu2025.github.io/ 에서 확인할 수 있습니다.

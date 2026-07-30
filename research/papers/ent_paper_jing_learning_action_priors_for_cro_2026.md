---
$id: ent_paper_jing_learning_action_priors_for_cro_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Action Priors for Cross-embodiment Robot Manipulation
  zh: 跨实体机器人操作的动作先验学习
  ko: 교차 구현 로봇 조작을 위한 행동 사전 학습
summary:
  en: This paper proposes a two-stage training framework that learns action priors from unconditioned trajectories via flow
    matching, then transfers them to VLA models for faster convergence and higher success rates in cross-embodiment manipulation,
    including humanoid robots.
  zh: 本文提出一种两阶段训练框架，通过流匹配从无条件轨迹中学习动作先验，再将其迁移至VLA模型，从而在跨实体操作（包括人形机器人）中实现更快的收敛速度和更高的成功率。该工作由研究团队提出，核心贡献在于为动作模块预训练运动先验，解决了VLA模型缺乏显式运动先验的问题。
  ko: 본 논문은 흐름 매칭을 통해 무조건적 궤적으로부터 행동 사전을 학습한 후, 이를 VLA 모델에 전이하여 교차 구현 조작(인간형 로봇 포함)에서 더 빠른 수렴과 높은 성공률을 달성하는 2단계 훈련 프레임워크를
    제안한다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- vla
- action_prior
- flow_matching
- cross_embodiment
- humanoid_manipulation
- transfer_learning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.26095v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Learning Action Priors for Cross-embodiment Robot Manipulation
  url: https://arxiv.org/abs/2606.26095
  date: '2026'
  accessed_at: '2026-06-25'
related_entities: []
theoretical_depth:
- system
---
## 概述
现有VLA模型通常基于VLM骨干网络附加动作模块并联合优化，但动作模块几乎从零学习物理运动，缺乏显式运动先验，导致早期优化需同时发现时间动作动态和跨模态对齐，在跨实体场景中挑战更大。本文提出两阶段训练框架：第一阶段通过流匹配的轻量级编码器-解码器动作模块，仅从无条件动作轨迹中高效学习时间运动结构；第二阶段通过解码器复用和早期潜在蒸馏，将学到的先验迁移至VLA训练，同时允许端到端策略微调。此外，训练好的编码器可作为紧凑历史压缩器，以极低成本生成时间上下文令牌。在13项跨实体任务（模拟和真实世界）上的实验表明，该方法相比无动作先验的VLA训练，收敛更快、成功率更高，尤其在数据稀缺的真实任务中表现突出。

## 核心内容
### 方法架构
- **两阶段训练框架**：第一阶段使用流匹配（flow matching）的轻量级编码器-解码器动作模块，仅从无条件动作轨迹中学习时间运动结构，不处理视觉或语言令牌。第二阶段通过解码器复用和早期潜在蒸馏，将学到的先验迁移至VLA训练，同时允许端到端策略微调。
- **历史压缩器**：训练好的编码器作为紧凑历史压缩器，将状态-动作历史总结为单个时间上下文令牌，实现历史感知建模，且成本极低。

### 实验设置
- **任务与平台**：在13项跨实体任务上验证，涵盖模拟和真实世界平台，包括人形机器人操作。
- **对比基线**：与无动作先验的VLA训练对比，评估收敛速度、成功率和数据效率。

### 关键数字与结果
- **收敛速度**：相比无动作先验的VLA训练，模型收敛更快。
- **成功率**：在跨实体操作任务中，成功率显著提升。
- **数据稀缺场景**：在真实世界数据稀缺任务中，性能大幅增强。
- **可扩展性**：第一阶段动作数据规模扩大，可生成更泛化的动作先验，直接提升下游VLA性能。

### 结论
本文提出的两阶段训练框架通过为动作模块预训练运动先验，有效解决了VLA模型缺乏显式运动先验的问题，在跨实体操作中实现了更快的收敛、更高的成功率和更强的数据效率。

## Overview
Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in cross-embodiment settings. In this work, we propose to pretrain the action module with motion priors before cross-modal VLA alignment. Specifically, we introduce a two-stage training framework that equips the action module with cross-embodiment temporal motion structure before VLA training begins. In Stage~1, a lightweight flow-matching-based encoder-decoder action module efficiently learns temporal motion structure solely from unconditioned action trajectories, without processing visual or language tokens. In Stage~2, this learned prior is transferred to VLA training through decoder reuse and early-stage latent distillation, aligning visual-language features with the action embedding space while still allowing end-to-end policy refinement. In addition, the trained encoder serves as a compact history compressor, summarizing state-action histories into a single temporal context token for history-aware modeling at negligible cost. Extensive experiments across 13 diverse cross-embodiment tasks on both simulated and real-world platforms validate the effectiveness of our approach. Compared with VLA training without action priors, our model achieves faster convergence, higher success rates, and substantially stronger performance on data-scarce real-world tasks. Moreover, scaling up the action data in Stage~1 yields a more generalizable action prior that directly improves downstream VLA performance.

## 개요
대부분의 Vision-Language-Action (VLA) 모델은 Vision-Language Model (VLM) 백본에 액션 모듈을 부착하고 전체 정책을 공동으로 최적화하는 방식으로 구축됩니다. 이 설계는 VLM으로부터 강력한 시각 및 언어 사전 지식을 상속받지만, 액션 모듈은 물리적 움직임을 거의 처음부터 학습해야 합니다. 그 결과, 정책은 명시적인 움직임 사전 지식이 부족하여 초기 최적화가 시간적 액션 동역학과 교차 모달 정렬을 동시에 발견해야 하며, 이는 교차 체화 환경에서 더욱 심화됩니다. 본 연구에서는 교차 모달 VLA 정렬 이전에 액션 모듈을 움직임 사전 지식으로 사전 학습하는 방법을 제안합니다. 구체적으로, VLA 훈련이 시작되기 전에 액션 모듈에 교차 체화 시간적 움직임 구조를 부여하는 2단계 훈련 프레임워크를 도입합니다. 1단계에서는 경량의 흐름 매칭 기반 인코더-디코더 액션 모듈이 시각 또는 언어 토큰을 처리하지 않고 조건 없는 액션 궤적만으로 시간적 움직임 구조를 효율적으로 학습합니다. 2단계에서는 이렇게 학습된 사전 지식이 디코더 재사용 및 초기 단계 잠재 증류를 통해 VLA 훈련으로 전이되어, 시각-언어 특징을 액션 임베딩 공간과 정렬하면서도 종단 간 정책 개선을 가능하게 합니다. 또한, 훈련된 인코더는 간결한 히스토리 압축기 역할을 하여 상태-액션 히스토리를 단일 시간적 컨텍스트 토큰으로 요약함으로써 무시할 수 있는 비용으로 히스토리 인식 모델링을 지원합니다. 시뮬레이션 및 실제 플랫폼에서 13가지 다양한 교차 체화 작업에 걸친 광범위한 실험을 통해 우리 접근 방식의 효과를 검증했습니다. 액션 사전 지식 없이 VLA를 훈련한 경우와 비교하여, 우리 모델은 더 빠른 수렴, 더 높은 성공률, 그리고 데이터가 부족한 실제 작업에서 훨씬 더 강력한 성능을 달성했습니다. 또한, 1단계에서 액션 데이터를 확장하면 더 일반화 가능한 액션 사전 지식이 생성되어 하위 VLA 성능을 직접적으로 향상시킵니다.

## 핵심 내용
대부분의 Vision-Language-Action (VLA) 모델은 Vision-Language Model (VLM) 백본에 액션 모듈을 부착하고 전체 정책을 공동으로 최적화하는 방식으로 구축됩니다. 이 설계는 VLM으로부터 강력한 시각 및 언어 사전 지식을 상속받지만, 액션 모듈은 물리적 움직임을 거의 처음부터 학습해야 합니다. 그 결과, 정책은 명시적인 움직임 사전 지식이 부족하여 초기 최적화가 시간적 액션 동역학과 교차 모달 정렬을 동시에 발견해야 하며, 이는 교차 체화 환경에서 더욱 심화됩니다. 본 연구에서는 교차 모달 VLA 정렬 이전에 액션 모듈을 움직임 사전 지식으로 사전 학습하는 방법을 제안합니다. 구체적으로, VLA 훈련이 시작되기 전에 액션 모듈에 교차 체화 시간적 움직임 구조를 부여하는 2단계 훈련 프레임워크를 도입합니다. 1단계에서는 경량의 흐름 매칭 기반 인코더-디코더 액션 모듈이 시각 또는 언어 토큰을 처리하지 않고 조건 없는 액션 궤적만으로 시간적 움직임 구조를 효율적으로 학습합니다. 2단계에서는 이렇게 학습된 사전 지식이 디코더 재사용 및 초기 단계 잠재 증류를 통해 VLA 훈련으로 전이되어, 시각-언어 특징을 액션 임베딩 공간과 정렬하면서도 종단 간 정책 개선을 가능하게 합니다. 또한, 훈련된 인코더는 간결한 히스토리 압축기 역할을 하여 상태-액션 히스토리를 단일 시간적 컨텍스트 토큰으로 요약함으로써 무시할 수 있는 비용으로 히스토리 인식 모델링을 지원합니다. 시뮬레이션 및 실제 플랫폼에서 13가지 다양한 교차 체화 작업에 걸친 광범위한 실험을 통해 우리 접근 방식의 효과를 검증했습니다. 액션 사전 지식 없이 VLA를 훈련한 경우와 비교하여, 우리 모델은 더 빠른 수렴, 더 높은 성공률, 그리고 데이터가 부족한 실제 작업에서 훨씬 더 강력한 성능을 달성했습니다. 또한, 1단계에서 액션 데이터를 확장하면 더 일반화 가능한 액션 사전 지식이 생성되어 하위 VLA 성능을 직접적으로 향상시킵니다.

## 参考
- http://arxiv.org/abs/2606.26095v1

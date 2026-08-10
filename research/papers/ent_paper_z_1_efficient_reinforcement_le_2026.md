---
$id: ent_paper_z_1_efficient_reinforcement_le_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Z-1: Efficient Reinforcement Learning for Vision-Language-Action Models'
  zh: 'Z-1: Efficient Reinforcement Learning for Vision-Language-Action Models'
  ko: 'Z-1: Efficient Reinforcement Learning for Vision-Language-Action Models'
summary:
  en: 'arXiv:2606.31846v1 Announce Type: new Abstract: Vision-Language-Action (VLA) models offer a promising framework for
    robotic manipulation by connecting language instructions, visual observations, and continuous control. However, most existing
    policies remain limited by behavior cloning or supervised fine-tuning (SFT) from fixed demonstrations, which provides
    limited opportunity to improve from the policy''s own failures. In this paper, we present Z-1, a reinforcement learning
    (RL) post-training framework for flow-based VLA models. Built on top of $\pi_{0.5}$, Z-1 uses only publicly released RoboCasa
    demonstrations for SFT and then applies a task-wise Group Relative Policy Optimization (GRPO) strategy across $24$ standard
    RoboCasa tasks. To improve the efficiency and stability of online optimization, Z-1 combines shared-prefix rollout construction,
    tree-structured trajectory branching, completion-aware reward calibration, and selective joint training of VLM and Action
    Expert. Across all $24$ RoboCasa tasks, Z-1 achieves an average success rate of $80.6\%$, improving over its SFT initialization
    by $13.2\%$ points and outperforms the published sota models. These results show that systematic GRPO post-training can
    substantially improve flow-based VLA policies without additional private demonstrations.'
  zh: Z-1 是一个面向流式视觉-语言-动作（VLA）模型的强化学习后训练框架，基于 π₀.5 构建。它仅使用公开的 RoboCasa 演示数据进行监督微调（SFT），然后通过任务级分组相对策略优化（GRPO）在 24 个标准 RoboCasa
    任务上优化策略。Z-1 在全部任务上取得了 80.6% 的平均成功率，比 SFT 初始化提升 13.2 个百分点，超越了已发表的最优模型。
  ko: 'arXiv:2606.31846v1 Announce Type: new Abstract: Vision-Language-Action (VLA) models offer a promising framework for
    robotic manipulation by connecting language instructions, visual observations, and continuous control. However, most existing
    policies remain limited by behavior cloning or supervised fine-tuning (SFT) from fixed demonstrations, which provides
    limited opportunity to improve from the policy''s own failures. In this paper, we present Z-1, a reinforcement learning
    (RL) post-training framework for flow-based VLA models. Built on top of $\pi_{0.5}$, Z-1 uses only publicly released RoboCasa
    demonstrations for SFT and then applies a task-wise Group Relative Policy Optimization (GRPO) strategy across $24$ standard
    RoboCasa tasks. To improve the efficiency and stability of online optimization, Z-1 combines shared-prefix rollout construction,
    tree-structured trajectory branching, completion-aware reward calibration, and selective joint training of VLM and Action
    Expert. Across all $24$ RoboCasa tasks, Z-1 achieves an average success rate of $80.6\%$, improving over its SFT initialization
    by $13.2\%$ points and outperforms the published sota models. These results show that systematic GRPO post-training can
    substantially improve flow-based VLA policies without additional private demonstrations.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- z_1
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31846v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1144 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Z-1: Efficient Reinforcement Learning for Vision-Language-Action Models'
  url: https://arxiv.org/abs/2606.31846
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Z-1 由研究者提出，旨在解决现有 VLA 模型仅依赖行为克隆或监督微调、无法从自身失败中学习的问题。该框架以 π₀.5 为基础，仅使用公开的 RoboCasa 演示数据进行 SFT，随后在 24 个任务上应用任务级 GRPO 策略进行在线强化学习。为了提升在线优化的效率与稳定性，Z-1 引入了共享前缀轨迹构建、树状轨迹分支、完成感知奖励校准以及 VLM 与动作专家的选择性联合训练。实验表明，Z-1 在 24 个 RoboCasa 任务上平均成功率达到 80.6%，较 SFT 初始化提升 13.2 个百分点，并超越了已发表的最优模型，证明了系统化 GRPO 后训练能显著改进流式 VLA 策略，且无需额外私有演示数据。

## 核心内容
### 方法
Z-1 是一个针对流式 VLA 模型的强化学习后训练框架，其核心流程如下：
- **基础模型**：基于 π₀.5 构建，这是一个流式 VLA 模型。
- **监督微调（SFT）**：仅使用公开的 RoboCasa 演示数据进行 SFT，作为初始策略。
- **强化学习后训练**：在 24 个标准 RoboCasa 任务上应用任务级 GRPO 策略。GRPO 是一种分组相对策略优化方法，通过比较同一任务内不同轨迹的回报来更新策略。

### 架构与优化
为了提升在线优化的效率与稳定性，Z-1 结合了以下技术：
- **共享前缀轨迹构建**：通过共享轨迹前缀减少重复计算，提高采样效率。
- **树状轨迹分支**：在轨迹中引入分支结构，允许策略探索多种后续动作，增加探索多样性。
- **完成感知奖励校准**：根据任务完成状态动态调整奖励信号，避免稀疏奖励问题。
- **选择性联合训练**：在训练中同时优化视觉-语言模型（VLM）和动作专家，但仅选择性地更新部分参数，以保持稳定性。

### 实验设置
- **任务**：24 个标准 RoboCasa 任务，涵盖多种机器人操作场景。
- **基线**：与 SFT 初始化策略及已发表的最优模型（sota）进行比较。
- **评估指标**：平均成功率（Average Success Rate）。

### 关键结果
- Z-1 在全部 24 个 RoboCasa 任务上取得了 **80.6%** 的平均成功率。
- 相比 SFT 初始化（67.4%），提升了 **13.2 个百分点**。
- 超越了已发表的最优模型（sota），且无需额外私有演示数据。

### 结论
Z-1 证明了系统化的 GRPO 后训练可以显著提升流式 VLA 策略的性能，仅依赖公开数据即可实现超越现有最优模型的效果。该框架为机器人操作中的强化学习后训练提供了高效且稳定的解决方案。

## Overview
Vision-Language-Action (VLA) models offer a promising framework for robotic manipulation by connecting language instructions, visual observations, and continuous control. However, most existing policies remain limited by behavior cloning or supervised fine-tuning (SFT) from fixed demonstrations, which provides limited opportunity to improve from the policy's own failures. In this paper, we present Z-1, a reinforcement learning (RL) post-training framework for flow-based VLA models. Built on top of $π_{0.5}$, Z-1 uses only publicly released RoboCasa demonstrations for SFT and then applies a task-wise Group Relative Policy Optimization (GRPO) strategy across $24$ standard RoboCasa tasks. To improve the efficiency and stability of online optimization, Z-1 combines shared-prefix rollout construction, tree-structured trajectory branching, completion-aware reward calibration, and selective joint training of VLM and Action Expert. Across all $24$ RoboCasa tasks, Z-1 achieves an average success rate of $80.6\%$, improving over its SFT initialization by $13.2\%$ points and outperforms the published sota models. These results show that systematic GRPO post-training can substantially improve flow-based VLA policies without additional private demonstrations.

## 参考
- http://arxiv.org/abs/2606.31846v1

## 개요
Z-1은 연구자들이 제안한 것으로, 기존 VLA 모델이 행동 복제나 지도 미세 조정에만 의존하여 자체 실패로부터 학습할 수 없는 문제를 해결하기 위해 설계되었습니다. 이 프레임워크는 π₀.5를 기반으로 하며, 공개된 RoboCasa 데모 데이터만을 사용하여 SFT를 수행한 후, 24개 작업에 작업 수준 GRPO 전략을 적용하여 온라인 강화 학습을 진행합니다. 온라인 최적화의 효율성과 안정성을 높이기 위해 Z-1은 공유 접두사 궤적 구축, 트리형 궤적 분기, 완료 인식 보상 보정, VLM과 행동 전문가의 선택적 공동 훈련을 도입했습니다. 실험 결과, Z-1은 24개 RoboCasa 작업에서 평균 성공률 80.6%를 달성하여 SFT 초기화 대비 13.2% 포인트 향상되었으며, 발표된 최적 모델을 능가하여 체계적인 GRPO 후훈련이 추가 비공개 데모 데이터 없이도 스트리밍 VLA 정책을 크게 개선할 수 있음을 입증했습니다.

## 핵심 내용
### 방법
Z-1은 스트리밍 VLA 모델을 위한 강화 학습 후훈련 프레임워크로, 핵심 절차는 다음과 같습니다:
- **기본 모델**: π₀.5를 기반으로 구축된 스트리밍 VLA 모델입니다.
- **지도 미세 조정(SFT)**: 공개된 RoboCasa 데모 데이터만을 사용하여 SFT를 수행하고, 이를 초기 정책으로 사용합니다.
- **강화 학습 후훈련**: 24개 표준 RoboCasa 작업에 작업 수준 GRPO 전략을 적용합니다. GRPO는 그룹 상대 정책 최적화 방법으로, 동일 작업 내 서로 다른 궤적의 보상을 비교하여 정책을 업데이트합니다.

### 아키텍처 및 최적화
온라인 최적화의 효율성과 안정성을 높이기 위해 Z-1은 다음 기술을 결합합니다:
- **공유 접두사 궤적 구축**: 공유 궤적 접두사를 통해 중복 계산을 줄이고 샘플링 효율성을 높입니다.
- **트리형 궤적 분기**: 궤적에 분기 구조를 도입하여 정책이 다양한 후속 행동을 탐색할 수 있게 하고 탐색 다양성을 증가시킵니다.
- **완료 인식 보상 보정**: 작업 완료 상태에 따라 보상 신호를 동적으로 조정하여 희소 보상 문제를 방지합니다.
- **선택적 공동 훈련**: 훈련 중 시각-언어 모델(VLM)과 행동 전문가를 동시에 최적화하지만, 일부 매개변수만 선택적으로 업데이트하여 안정성을 유지합니다.

### 실험 설정
- **작업**: 다양한 로봇 조작 시나리오를 포함한 24개 표준 RoboCasa 작업.
- **기준선**: SFT 초기화 정책 및 발표된 최적 모델(sota)과 비교.
- **평가 지표**: 평균 성공률(Average Success Rate).

### 주요 결과
- Z-1은 전체 24개 RoboCasa 작업에서 **80.6%** 의 평균 성공률을 달성했습니다.
- SFT 초기화(67.4%) 대비 **13.2% 포인트** 향상되었습니다.
- 추가 비공개 데모 데이터 없이도 발표된 최적 모델(sota)을 능가했습니다.

### 결론
Z-1은 체계적인 GRPO 후훈련이 공개 데이터만으로도 기존 최적 모델을 능가하는 성과를 내며 스트리밍 VLA 정책의 성능을 크게 향상시킬 수 있음을 입증했습니다. 이 프레임워크는 로봇 조작에서 강화 학습 후훈련을 위한 효율적이고 안정적인 솔루션을 제공합니다.

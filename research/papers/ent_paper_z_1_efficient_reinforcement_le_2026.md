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
  zh: 'arXiv:2606.31846v1 Announce Type: new Abstract: Vision-Language-Action (VLA) models offer a promising framework for
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31846v1.
sources:
- id: src_001
  type: paper
  title: 'Z-1: Efficient Reinforcement Learning for Vision-Language-Action Models'
  url: https://arxiv.org/abs/2606.31846
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models offer a promising framework for robotic manipulation by connecting language instructions, visual observations, and continuous control. However, most existing policies remain limited by behavior cloning or supervised fine-tuning (SFT) from fixed demonstrations, which provides limited opportunity to improve from the policy's own failures. In this paper, we present Z-1, a reinforcement learning (RL) post-training framework for flow-based VLA models. Built on top of $π_{0.5}$, Z-1 uses only publicly released RoboCasa demonstrations for SFT and then applies a task-wise Group Relative Policy Optimization (GRPO) strategy across $24$ standard RoboCasa tasks. To improve the efficiency and stability of online optimization, Z-1 combines shared-prefix rollout construction, tree-structured trajectory branching, completion-aware reward calibration, and selective joint training of VLM and Action Expert. Across all $24$ RoboCasa tasks, Z-1 achieves an average success rate of $80.6\%$, improving over its SFT initialization by $13.2\%$ points and outperforms the published sota models. These results show that systematic GRPO post-training can substantially improve flow-based VLA policies without additional private demonstrations.

## 核心内容
Vision-Language-Action (VLA) models offer a promising framework for robotic manipulation by connecting language instructions, visual observations, and continuous control. However, most existing policies remain limited by behavior cloning or supervised fine-tuning (SFT) from fixed demonstrations, which provides limited opportunity to improve from the policy's own failures. In this paper, we present Z-1, a reinforcement learning (RL) post-training framework for flow-based VLA models. Built on top of $π_{0.5}$, Z-1 uses only publicly released RoboCasa demonstrations for SFT and then applies a task-wise Group Relative Policy Optimization (GRPO) strategy across $24$ standard RoboCasa tasks. To improve the efficiency and stability of online optimization, Z-1 combines shared-prefix rollout construction, tree-structured trajectory branching, completion-aware reward calibration, and selective joint training of VLM and Action Expert. Across all $24$ RoboCasa tasks, Z-1 achieves an average success rate of $80.6\%$, improving over its SFT initialization by $13.2\%$ points and outperforms the published sota models. These results show that systematic GRPO post-training can substantially improve flow-based VLA policies without additional private demonstrations.

## 参考
- http://arxiv.org/abs/2606.31846v1

## Overview
Vision-Language-Action (VLA) models offer a promising framework for robotic manipulation by connecting language instructions, visual observations, and continuous control. However, most existing policies remain limited by behavior cloning or supervised fine-tuning (SFT) from fixed demonstrations, which provides limited opportunity to improve from the policy's own failures. In this paper, we present Z-1, a reinforcement learning (RL) post-training framework for flow-based VLA models. Built on top of $π_{0.5}$, Z-1 uses only publicly released RoboCasa demonstrations for SFT and then applies a task-wise Group Relative Policy Optimization (GRPO) strategy across $24$ standard RoboCasa tasks. To improve the efficiency and stability of online optimization, Z-1 combines shared-prefix rollout construction, tree-structured trajectory branching, completion-aware reward calibration, and selective joint training of VLM and Action Expert. Across all $24$ RoboCasa tasks, Z-1 achieves an average success rate of $80.6\%$, improving over its SFT initialization by $13.2\%$ points and outperforms the published sota models. These results show that systematic GRPO post-training can substantially improve flow-based VLA policies without additional private demonstrations.

## Content
Vision-Language-Action (VLA) models offer a promising framework for robotic manipulation by connecting language instructions, visual observations, and continuous control. However, most existing policies remain limited by behavior cloning or supervised fine-tuning (SFT) from fixed demonstrations, which provides limited opportunity to improve from the policy's own failures. In this paper, we present Z-1, a reinforcement learning (RL) post-training framework for flow-based VLA models. Built on top of $π_{0.5}$, Z-1 uses only publicly released RoboCasa demonstrations for SFT and then applies a task-wise Group Relative Policy Optimization (GRPO) strategy across $24$ standard RoboCasa tasks. To improve the efficiency and stability of online optimization, Z-1 combines shared-prefix rollout construction, tree-structured trajectory branching, completion-aware reward calibration, and selective joint training of VLM and Action Expert. Across all $24$ RoboCasa tasks, Z-1 achieves an average success rate of $80.6\%$, improving over its SFT initialization by $13.2\%$ points and outperforms the published sota models. These results show that systematic GRPO post-training can substantially improve flow-based VLA policies without additional private demonstrations.

## 개요
Vision-Language-Action (VLA) 모델은 언어 명령, 시각적 관찰 및 연속 제어를 연결하여 로봇 조작을 위한 유망한 프레임워크를 제공합니다. 그러나 대부분의 기존 정책은 고정된 시연에서의 행동 복제 또는 지도 미세 조정(SFT)에 의해 제한되어, 정책 자체의 실패로부터 개선할 기회가 거의 없습니다. 본 논문에서는 흐름 기반 VLA 모델을 위한 강화 학습(RL) 사후 훈련 프레임워크인 Z-1을 제시합니다. $π_{0.5}$를 기반으로 구축된 Z-1은 공개적으로 출시된 RoboCasa 시연만을 SFT에 사용한 후, $24$개의 표준 RoboCasa 작업에 걸쳐 작업별 그룹 상대 정책 최적화(GRPO) 전략을 적용합니다. 온라인 최적화의 효율성과 안정성을 향상시키기 위해 Z-1은 공유 접두사 롤아웃 구성, 트리 구조 궤적 분기, 완료 인식 보상 보정, VLM 및 Action Expert의 선택적 공동 훈련을 결합합니다. 모든 $24$개의 RoboCasa 작업에서 Z-1은 평균 성공률 $80.6\%$를 달성하여 SFT 초기화 대비 $13.2\%$ 포인트 향상되었으며, 발표된 최신 모델을 능가합니다. 이러한 결과는 체계적인 GRPO 사후 훈련이 추가적인 비공개 시연 없이도 흐름 기반 VLA 정책을 크게 개선할 수 있음을 보여줍니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 언어 명령, 시각적 관찰 및 연속 제어를 연결하여 로봇 조작을 위한 유망한 프레임워크를 제공합니다. 그러나 대부분의 기존 정책은 고정된 시연에서의 행동 복제 또는 지도 미세 조정(SFT)에 의해 제한되어, 정책 자체의 실패로부터 개선할 기회가 거의 없습니다. 본 논문에서는 흐름 기반 VLA 모델을 위한 강화 학습(RL) 사후 훈련 프레임워크인 Z-1을 제시합니다. $π_{0.5}$를 기반으로 구축된 Z-1은 공개적으로 출시된 RoboCasa 시연만을 SFT에 사용한 후, $24$개의 표준 RoboCasa 작업에 걸쳐 작업별 그룹 상대 정책 최적화(GRPO) 전략을 적용합니다. 온라인 최적화의 효율성과 안정성을 향상시키기 위해 Z-1은 공유 접두사 롤아웃 구성, 트리 구조 궤적 분기, 완료 인식 보상 보정, VLM 및 Action Expert의 선택적 공동 훈련을 결합합니다. 모든 $24$개의 RoboCasa 작업에서 Z-1은 평균 성공률 $80.6\%$를 달성하여 SFT 초기화 대비 $13.2\%$ 포인트 향상되었으며, 발표된 최신 모델을 능가합니다. 이러한 결과는 체계적인 GRPO 사후 훈련이 추가적인 비공개 시연 없이도 흐름 기반 VLA 정책을 크게 개선할 수 있음을 보여줍니다.

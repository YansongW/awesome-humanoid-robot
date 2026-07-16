---
$id: ent_paper_rl_from_physical_feedback_alig_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RL from Physical Feedback: Aligning Large Motion Models with Humanoid Control'
  zh: 'RL from Physical Feedback: Aligning Large Motion Models with Humanoid Control'
  ko: 'RL from Physical Feedback: Aligning Large Motion Models with Humanoid Control'
summary:
  en: 'RL from Physical Feedback: Aligning Large Motion Models with Humanoid Control is a 2025 work on physics-based character
    animation for humanoid robots.'
  zh: 'RL from Physical Feedback: Aligning Large Motion Models with Humanoid Control is a 2025 work on physics-based character
    animation for humanoid robots.'
  ko: 'RL from Physical Feedback: Aligning Large Motion Models with Humanoid Control is a 2025 work on physics-based character
    animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- physics_based
- rl_from_physical_feedback
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.12769v1.
sources:
- id: src_001
  type: paper
  title: 'RL from Physical Feedback: Aligning Large Motion Models with Humanoid Control (arXiv)'
  url: https://arxiv.org/abs/2506.12769
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
This paper focuses on a critical challenge in robotics: translating text-driven human motions into executable actions for humanoid robots, enabling efficient and cost-effective learning of new behaviors. While existing text-to-motion generation methods achieve semantic alignment between language and motion, they often produce kinematically or physically infeasible motions unsuitable for real-world deployment. To bridge this sim-to-real gap, we propose Reinforcement Learning from Physical Feedback (RLPF), a novel framework that integrates physics-aware motion evaluation with text-conditioned motion generation. RLPF employs a motion tracking policy to assess feasibility in a physics simulator, generating rewards for fine-tuning the motion generator. Furthermore, RLPF introduces an alignment verification module to preserve semantic fidelity to text instructions. This joint optimization ensures both physical plausibility and instruction alignment. Extensive experiments show that RLPF greatly outperforms baseline methods in generating physically feasible motions while maintaining semantic correspondence with text instruction, enabling successful deployment on real humanoid robots.

## 核心内容
This paper focuses on a critical challenge in robotics: translating text-driven human motions into executable actions for humanoid robots, enabling efficient and cost-effective learning of new behaviors. While existing text-to-motion generation methods achieve semantic alignment between language and motion, they often produce kinematically or physically infeasible motions unsuitable for real-world deployment. To bridge this sim-to-real gap, we propose Reinforcement Learning from Physical Feedback (RLPF), a novel framework that integrates physics-aware motion evaluation with text-conditioned motion generation. RLPF employs a motion tracking policy to assess feasibility in a physics simulator, generating rewards for fine-tuning the motion generator. Furthermore, RLPF introduces an alignment verification module to preserve semantic fidelity to text instructions. This joint optimization ensures both physical plausibility and instruction alignment. Extensive experiments show that RLPF greatly outperforms baseline methods in generating physically feasible motions while maintaining semantic correspondence with text instruction, enabling successful deployment on real humanoid robots.

## 参考
- http://arxiv.org/abs/2506.12769v1

## Overview
This paper focuses on a critical challenge in robotics: translating text-driven human motions into executable actions for humanoid robots, enabling efficient and cost-effective learning of new behaviors. While existing text-to-motion generation methods achieve semantic alignment between language and motion, they often produce kinematically or physically infeasible motions unsuitable for real-world deployment. To bridge this sim-to-real gap, we propose Reinforcement Learning from Physical Feedback (RLPF), a novel framework that integrates physics-aware motion evaluation with text-conditioned motion generation. RLPF employs a motion tracking policy to assess feasibility in a physics simulator, generating rewards for fine-tuning the motion generator. Furthermore, RLPF introduces an alignment verification module to preserve semantic fidelity to text instructions. This joint optimization ensures both physical plausibility and instruction alignment. Extensive experiments show that RLPF greatly outperforms baseline methods in generating physically feasible motions while maintaining semantic correspondence with text instruction, enabling successful deployment on real humanoid robots.

## Content
This paper focuses on a critical challenge in robotics: translating text-driven human motions into executable actions for humanoid robots, enabling efficient and cost-effective learning of new behaviors. While existing text-to-motion generation methods achieve semantic alignment between language and motion, they often produce kinematically or physically infeasible motions unsuitable for real-world deployment. To bridge this sim-to-real gap, we propose Reinforcement Learning from Physical Feedback (RLPF), a novel framework that integrates physics-aware motion evaluation with text-conditioned motion generation. RLPF employs a motion tracking policy to assess feasibility in a physics simulator, generating rewards for fine-tuning the motion generator. Furthermore, RLPF introduces an alignment verification module to preserve semantic fidelity to text instructions. This joint optimization ensures both physical plausibility and instruction alignment. Extensive experiments show that RLPF greatly outperforms baseline methods in generating physically feasible motions while maintaining semantic correspondence with text instruction, enabling successful deployment on real humanoid robots.

## 개요
본 논문은 로봇 공학의 중요한 과제, 즉 텍스트 기반 인간 동작을 휴머노이드 로봇이 실행 가능한 행동으로 변환하여 새로운 행동을 효율적이고 비용 효과적으로 학습할 수 있도록 하는 데 초점을 맞춥니다. 기존의 텍스트-동작 생성 방법은 언어와 동작 간의 의미적 정렬을 달성하지만, 종종 운동학적 또는 물리적으로 실행 불가능한 동작을 생성하여 실제 환경에 적용하기에 부적합합니다. 이러한 시뮬레이션-현실 격차를 해소하기 위해, 우리는 물리 인식 동작 평가와 텍스트 조건 동작 생성을 통합하는 새로운 프레임워크인 RLPF(Reinforcement Learning from Physical Feedback)를 제안합니다. RLPF는 동작 추적 정책을 사용하여 물리 시뮬레이터에서 실행 가능성을 평가하고, 동작 생성기를 미세 조정하기 위한 보상을 생성합니다. 또한, RLPF는 텍스트 명령에 대한 의미적 충실도를 유지하기 위해 정렬 검증 모듈을 도입합니다. 이 공동 최적화는 물리적 타당성과 명령 정렬을 모두 보장합니다. 광범위한 실험을 통해 RLPF는 텍스트 명령과의 의미적 대응을 유지하면서 물리적으로 실행 가능한 동작을 생성하는 데 있어 기준 방법보다 크게 우수한 성능을 보여주며, 실제 휴머노이드 로봇에 성공적으로 배포될 수 있음을 입증합니다.

## 핵심 내용
본 논문은 로봇 공학의 중요한 과제, 즉 텍스트 기반 인간 동작을 휴머노이드 로봇이 실행 가능한 행동으로 변환하여 새로운 행동을 효율적이고 비용 효과적으로 학습할 수 있도록 하는 데 초점을 맞춥니다. 기존의 텍스트-동작 생성 방법은 언어와 동작 간의 의미적 정렬을 달성하지만, 종종 운동학적 또는 물리적으로 실행 불가능한 동작을 생성하여 실제 환경에 적용하기에 부적합합니다. 이러한 시뮬레이션-현실 격차를 해소하기 위해, 우리는 물리 인식 동작 평가와 텍스트 조건 동작 생성을 통합하는 새로운 프레임워크인 RLPF(Reinforcement Learning from Physical Feedback)를 제안합니다. RLPF는 동작 추적 정책을 사용하여 물리 시뮬레이터에서 실행 가능성을 평가하고, 동작 생성기를 미세 조정하기 위한 보상을 생성합니다. 또한, RLPF는 텍스트 명령에 대한 의미적 충실도를 유지하기 위해 정렬 검증 모듈을 도입합니다. 이 공동 최적화는 물리적 타당성과 명령 정렬을 모두 보장합니다. 광범위한 실험을 통해 RLPF는 텍스트 명령과의 의미적 대응을 유지하면서 물리적으로 실행 가능한 동작을 생성하는 데 있어 기준 방법보다 크게 우수한 성능을 보여주며, 실제 휴머노이드 로봇에 성공적으로 배포될 수 있음을 입증합니다.

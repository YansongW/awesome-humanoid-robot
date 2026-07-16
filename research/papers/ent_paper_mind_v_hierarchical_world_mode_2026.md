---
$id: ent_paper_mind_v_hierarchical_world_mode_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MIND-V: Hierarchical World Model for Long-Horizon Robotic Manipulation with RL-based Physical Alignment'
  zh: 'MIND-V: Hierarchical World Model for Long-Horizon Robotic Manipulation with RL-based Physical Alignment'
  ko: 'MIND-V: Hierarchical World Model for Long-Horizon Robotic Manipulation with RL-based Physical Alignment'
summary:
  en: 'arXiv:2512.06628v4 Announce Type: replace Abstract: Scalable embodied intelligence is constrained by the scarcity of
    diverse, long-horizon robotic manipulation data. Existing video world models in this domain are limited to synthesizing
    short clips of simple actions and often rely on manually defined trajectories. To this end, we introduce MIND-V, a cognitive
    hierarchical world model designed to synthesize physically plausible and logically coherent videos of long-horizon robotic
    manipulation. Inspired by cognitive science, MIND-V bridges high-level reasoning with pixel-level synthesis through three
    core components: a Semantic Reasoning Hub (SRH) that leverages a pre-trained vision-language model for task planning;
    a Behavioral Semantic Bridge (BSB) that translates abstract instructions into domain-invariant representations; and a
    Motor Video Generator (MVG) for conditional video rendering. MIND-V employs Staged Visual Future Rollouts, a test-time
    optimization strategy to enhance long-horizon robustness. To enforce adherence to physical laws, we introduce a GRPO reinforcement
    learning post-training phase guided by a novel Physical Foresight Coherence (PFC) reward. PFC leverages the V-JEPA2 world
    model as a physics referee to penalize implausible dynamics in the latent feature space. Experiments confirm MIND-V''s
    SOTA performance in long-horizon simulation and its significant value for policy learning, introducing a scalable and
    fully autonomous framework for embodied data synthesis.'
  zh: 'arXiv:2512.06628v4 Announce Type: replace Abstract: Scalable embodied intelligence is constrained by the scarcity of
    diverse, long-horizon robotic manipulation data. Existing video world models in this domain are limited to synthesizing
    short clips of simple actions and often rely on manually defined trajectories. To this end, we introduce MIND-V, a cognitive
    hierarchical world model designed to synthesize physically plausible and logically coherent videos of long-horizon robotic
    manipulation. Inspired by cognitive science, MIND-V bridges high-level reasoning with pixel-level synthesis through three
    core components: a Semantic Reasoning Hub (SRH) that leverages a pre-trained vision-language model for task planning;
    a Behavioral Semantic Bridge (BSB) that translates abstract instructions into domain-invariant representations; and a
    Motor Video Generator (MVG) for conditional video rendering. MIND-V employs Staged Visual Future Rollouts, a test-time
    optimization strategy to enhance long-horizon robustness. To enforce adherence to physical laws, we introduce a GRPO reinforcement
    learning post-training phase guided by a novel Physical Foresight Coherence (PFC) reward. PFC leverages the V-JEPA2 world
    model as a physics referee to penalize implausible dynamics in the latent feature space. Experiments confirm MIND-V''s
    SOTA performance in long-horizon simulation and its significant value for policy learning, introducing a scalable and
    fully autonomous framework for embodied data synthesis.'
  ko: 'arXiv:2512.06628v4 Announce Type: replace Abstract: Scalable embodied intelligence is constrained by the scarcity of
    diverse, long-horizon robotic manipulation data. Existing video world models in this domain are limited to synthesizing
    short clips of simple actions and often rely on manually defined trajectories. To this end, we introduce MIND-V, a cognitive
    hierarchical world model designed to synthesize physically plausible and logically coherent videos of long-horizon robotic
    manipulation. Inspired by cognitive science, MIND-V bridges high-level reasoning with pixel-level synthesis through three
    core components: a Semantic Reasoning Hub (SRH) that leverages a pre-trained vision-language model for task planning;
    a Behavioral Semantic Bridge (BSB) that translates abstract instructions into domain-invariant representations; and a
    Motor Video Generator (MVG) for conditional video rendering. MIND-V employs Staged Visual Future Rollouts, a test-time
    optimization strategy to enhance long-horizon robustness. To enforce adherence to physical laws, we introduce a GRPO reinforcement
    learning post-training phase guided by a novel Physical Foresight Coherence (PFC) reward. PFC leverages the V-JEPA2 world
    model as a physics referee to penalize implausible dynamics in the latent feature space. Experiments confirm MIND-V''s
    SOTA performance in long-horizon simulation and its significant value for policy learning, introducing a scalable and
    fully autonomous framework for embodied data synthesis.'
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
- mind_v
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.06628v4.
sources:
- id: src_001
  type: paper
  title: 'MIND-V: Hierarchical World Model for Long-Horizon Robotic Manipulation with RL-based Physical Alignment (arXiv)'
  url: https://arxiv.org/abs/2512.06628
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Scalable embodied intelligence is constrained by the scarcity of diverse, long-horizon robotic manipulation data. Existing video world models in this domain are limited to synthesizing short clips of simple actions and often rely on manually defined trajectories. To this end, we introduce MIND-V, a cognitive hierarchical world model designed to synthesize physically plausible and logically coherent videos of long-horizon robotic manipulation. Inspired by cognitive science, MIND-V bridges high-level reasoning with pixel-level synthesis through three core components: a Semantic Reasoning Hub (SRH) that leverages a pre-trained vision-language model for task planning; a Behavioral Semantic Bridge (BSB) that translates abstract instructions into domain-invariant representations; and a Motor Video Generator (MVG) for conditional video rendering. MIND-V employs Staged Visual Future Rollouts, a test-time optimization strategy to enhance long-horizon robustness. To enforce adherence to physical laws, we introduce a GRPO reinforcement learning post-training phase guided by a novel Physical Foresight Coherence (PFC) reward. PFC leverages the V-JEPA2 world model as a physics referee to penalize implausible dynamics in the latent feature space. Experiments confirm MIND-V's SOTA performance in long-horizon simulation and its significant value for policy learning, introducing a scalable and fully autonomous framework for embodied data synthesis.

## 核心内容
Scalable embodied intelligence is constrained by the scarcity of diverse, long-horizon robotic manipulation data. Existing video world models in this domain are limited to synthesizing short clips of simple actions and often rely on manually defined trajectories. To this end, we introduce MIND-V, a cognitive hierarchical world model designed to synthesize physically plausible and logically coherent videos of long-horizon robotic manipulation. Inspired by cognitive science, MIND-V bridges high-level reasoning with pixel-level synthesis through three core components: a Semantic Reasoning Hub (SRH) that leverages a pre-trained vision-language model for task planning; a Behavioral Semantic Bridge (BSB) that translates abstract instructions into domain-invariant representations; and a Motor Video Generator (MVG) for conditional video rendering. MIND-V employs Staged Visual Future Rollouts, a test-time optimization strategy to enhance long-horizon robustness. To enforce adherence to physical laws, we introduce a GRPO reinforcement learning post-training phase guided by a novel Physical Foresight Coherence (PFC) reward. PFC leverages the V-JEPA2 world model as a physics referee to penalize implausible dynamics in the latent feature space. Experiments confirm MIND-V's SOTA performance in long-horizon simulation and its significant value for policy learning, introducing a scalable and fully autonomous framework for embodied data synthesis.

## 参考
- http://arxiv.org/abs/2512.06628v4

## Overview
Scalable embodied intelligence is constrained by the scarcity of diverse, long-horizon robotic manipulation data. Existing video world models in this domain are limited to synthesizing short clips of simple actions and often rely on manually defined trajectories. To this end, we introduce MIND-V, a cognitive hierarchical world model designed to synthesize physically plausible and logically coherent videos of long-horizon robotic manipulation. Inspired by cognitive science, MIND-V bridges high-level reasoning with pixel-level synthesis through three core components: a Semantic Reasoning Hub (SRH) that leverages a pre-trained vision-language model for task planning; a Behavioral Semantic Bridge (BSB) that translates abstract instructions into domain-invariant representations; and a Motor Video Generator (MVG) for conditional video rendering. MIND-V employs Staged Visual Future Rollouts, a test-time optimization strategy to enhance long-horizon robustness. To enforce adherence to physical laws, we introduce a GRPO reinforcement learning post-training phase guided by a novel Physical Foresight Coherence (PFC) reward. PFC leverages the V-JEPA2 world model as a physics referee to penalize implausible dynamics in the latent feature space. Experiments confirm MIND-V's SOTA performance in long-horizon simulation and its significant value for policy learning, introducing a scalable and fully autonomous framework for embodied data synthesis.

## Content
Scalable embodied intelligence is constrained by the scarcity of diverse, long-horizon robotic manipulation data. Existing video world models in this domain are limited to synthesizing short clips of simple actions and often rely on manually defined trajectories. To this end, we introduce MIND-V, a cognitive hierarchical world model designed to synthesize physically plausible and logically coherent videos of long-horizon robotic manipulation. Inspired by cognitive science, MIND-V bridges high-level reasoning with pixel-level synthesis through three core components: a Semantic Reasoning Hub (SRH) that leverages a pre-trained vision-language model for task planning; a Behavioral Semantic Bridge (BSB) that translates abstract instructions into domain-invariant representations; and a Motor Video Generator (MVG) for conditional video rendering. MIND-V employs Staged Visual Future Rollouts, a test-time optimization strategy to enhance long-horizon robustness. To enforce adherence to physical laws, we introduce a GRPO reinforcement learning post-training phase guided by a novel Physical Foresight Coherence (PFC) reward. PFC leverages the V-JEPA2 world model as a physics referee to penalize implausible dynamics in the latent feature space. Experiments confirm MIND-V's SOTA performance in long-horizon simulation and its significant value for policy learning, introducing a scalable and fully autonomous framework for embodied data synthesis.

## 개요
확장 가능한 체화 지능은 다양하고 장기적인 로봇 조작 데이터의 부족으로 인해 제약을 받고 있습니다. 이 분야의 기존 비디오 월드 모델은 단순한 동작의 짧은 클립을 합성하는 데 한정되어 있으며, 종종 수동으로 정의된 궤적에 의존합니다. 이러한 문제를 해결하기 위해, 우리는 장기적인 로봇 조작의 물리적으로 타당하고 논리적으로 일관된 비디오를 합성하도록 설계된 인지 계층적 월드 모델인 MIND-V를 소개합니다. 인지 과학에서 영감을 받은 MIND-V는 세 가지 핵심 구성 요소를 통해 고수준 추론과 픽셀 수준 합성을 연결합니다: 작업 계획을 위해 사전 훈련된 비전-언어 모델을 활용하는 의미 추론 허브(SRH); 추상적 명령을 도메인 불변 표현으로 변환하는 행동 의미 브리지(BSB); 조건부 비디오 렌더링을 위한 모터 비디오 생성기(MVG). MIND-V는 장기적 견고성을 향상시키기 위한 테스트 시간 최적화 전략인 단계적 시각적 미래 롤아웃(Staged Visual Future Rollouts)을 사용합니다. 물리 법칙 준수를 강화하기 위해, 우리는 새로운 물리적 예측 일관성(PFC) 보상에 의해 안내되는 GRPO 강화 학습 사후 훈련 단계를 도입합니다. PFC는 V-JEPA2 월드 모델을 물리 심판으로 활용하여 잠재 특징 공간에서 타당하지 않은 동역학에 페널티를 부과합니다. 실험을 통해 MIND-V의 장기 시뮬레이션에서의 최첨단 성능과 정책 학습에 대한 중요한 가치를 확인하였으며, 체화 데이터 합성을 위한 확장 가능하고 완전 자율적인 프레임워크를 소개합니다.

## 핵심 내용
확장 가능한 체화 지능은 다양하고 장기적인 로봇 조작 데이터의 부족으로 인해 제약을 받고 있습니다. 이 분야의 기존 비디오 월드 모델은 단순한 동작의 짧은 클립을 합성하는 데 한정되어 있으며, 종종 수동으로 정의된 궤적에 의존합니다. 이러한 문제를 해결하기 위해, 우리는 장기적인 로봇 조작의 물리적으로 타당하고 논리적으로 일관된 비디오를 합성하도록 설계된 인지 계층적 월드 모델인 MIND-V를 소개합니다. 인지 과학에서 영감을 받은 MIND-V는 세 가지 핵심 구성 요소를 통해 고수준 추론과 픽셀 수준 합성을 연결합니다: 작업 계획을 위해 사전 훈련된 비전-언어 모델을 활용하는 의미 추론 허브(SRH); 추상적 명령을 도메인 불변 표현으로 변환하는 행동 의미 브리지(BSB); 조건부 비디오 렌더링을 위한 모터 비디오 생성기(MVG). MIND-V는 장기적 견고성을 향상시키기 위한 테스트 시간 최적화 전략인 단계적 시각적 미래 롤아웃(Staged Visual Future Rollouts)을 사용합니다. 물리 법칙 준수를 강화하기 위해, 우리는 새로운 물리적 예측 일관성(PFC) 보상에 의해 안내되는 GRPO 강화 학습 사후 훈련 단계를 도입합니다. PFC는 V-JEPA2 월드 모델을 물리 심판으로 활용하여 잠재 특징 공간에서 타당하지 않은 동역학에 페널티를 부과합니다. 실험을 통해 MIND-V의 장기 시뮬레이션에서의 최첨단 성능과 정책 학습에 대한 중요한 가치를 확인하였으며, 체화 데이터 합성을 위한 확장 가능하고 완전 자율적인 프레임워크를 소개합니다.

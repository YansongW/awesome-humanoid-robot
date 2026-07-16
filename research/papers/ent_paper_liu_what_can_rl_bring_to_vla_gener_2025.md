---
$id: ent_paper_liu_what_can_rl_bring_to_vla_gener_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: What Can RL Bring to VLA Generalization? An Empirical Study
  zh: What Can RL Bring to VLA Generalization? An Empirical Study
  ko: What Can RL Bring to VLA Generalization? An Empirical Study
summary:
  en: What Can RL Bring to VLA Generalization? An Empirical Study (What Can RL Bring to VLA Generalization? An Empirical Study),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Shenzhen International Graduate School,
    Tsinghua University, Institute for Interdisciplinary Information Sciences, Tsinghua University, Department of Electronic
    Engineering, Tsinghua University, and published at NIPS25.
  zh: What Can RL Bring to VLA Generalization? An Empirical Study (What Can RL Bring to VLA Generalization? An Empirical Study),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Shenzhen International Graduate School,
    Tsinghua University, Institute for Interdisciplinary Information Sciences, Tsinghua University, Department of Electronic
    Engineering, Tsinghua University, and published at NIPS25.
  ko: What Can RL Bring to VLA Generalization? An Empirical Study (What Can RL Bring to VLA Generalization? An Empirical Study),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Shenzhen International Graduate School,
    Tsinghua University, Institute for Interdisciplinary Information Sciences, Tsinghua University, Department of Electronic
    Engineering, Tsinghua University, and published at NIPS25.
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
- vision_language_action
- vla
- what_can_rl_bring_to_vla_gener
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.19789v4.
sources:
- id: src_001
  type: paper
  title: What Can RL Bring to VLA Generalization? An Empirical Study (arXiv)
  url: https://arxiv.org/abs/2505.19789
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: What Can RL Bring to VLA Generalization? An Empirical Study source
  url: https://doi.org/10.48550/arXiv.2505.19789
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Large Vision-Language Action (VLA) models have shown significant potential for embodied AI. However, their predominant training via supervised fine-tuning (SFT) limits generalization due to susceptibility to compounding errors under distribution shifts. Reinforcement learning (RL) offers a path to overcome these limitations by optimizing for task objectives via trial-and-error, yet a systematic understanding of its specific generalization benefits for VLAs compared to SFT is lacking. To address this, our study introduces a comprehensive benchmark for evaluating VLA generalization and systematically investigates the impact of RL fine-tuning across diverse visual, semantic, and execution dimensions. Our extensive experiments reveal that RL fine-tuning, particularly with PPO, significantly enhances generalization in semantic understanding and execution robustness over SFT, while maintaining comparable visual robustness. We identify PPO as a more effective RL algorithm for VLAs than LLM-derived methods like DPO and GRPO. We also develop a simple recipe for efficient PPO training on VLAs, and demonstrate its practical utility for improving VLA generalization. The project page is at https://rlvla.github.io

## 核心内容
Large Vision-Language Action (VLA) models have shown significant potential for embodied AI. However, their predominant training via supervised fine-tuning (SFT) limits generalization due to susceptibility to compounding errors under distribution shifts. Reinforcement learning (RL) offers a path to overcome these limitations by optimizing for task objectives via trial-and-error, yet a systematic understanding of its specific generalization benefits for VLAs compared to SFT is lacking. To address this, our study introduces a comprehensive benchmark for evaluating VLA generalization and systematically investigates the impact of RL fine-tuning across diverse visual, semantic, and execution dimensions. Our extensive experiments reveal that RL fine-tuning, particularly with PPO, significantly enhances generalization in semantic understanding and execution robustness over SFT, while maintaining comparable visual robustness. We identify PPO as a more effective RL algorithm for VLAs than LLM-derived methods like DPO and GRPO. We also develop a simple recipe for efficient PPO training on VLAs, and demonstrate its practical utility for improving VLA generalization. The project page is at https://rlvla.github.io

## 参考
- http://arxiv.org/abs/2505.19789v4

## Overview
Large Vision-Language Action (VLA) models have shown significant potential for embodied AI. However, their predominant training via supervised fine-tuning (SFT) limits generalization due to susceptibility to compounding errors under distribution shifts. Reinforcement learning (RL) offers a path to overcome these limitations by optimizing for task objectives via trial-and-error, yet a systematic understanding of its specific generalization benefits for VLAs compared to SFT is lacking. To address this, our study introduces a comprehensive benchmark for evaluating VLA generalization and systematically investigates the impact of RL fine-tuning across diverse visual, semantic, and execution dimensions. Our extensive experiments reveal that RL fine-tuning, particularly with PPO, significantly enhances generalization in semantic understanding and execution robustness over SFT, while maintaining comparable visual robustness. We identify PPO as a more effective RL algorithm for VLAs than LLM-derived methods like DPO and GRPO. We also develop a simple recipe for efficient PPO training on VLAs, and demonstrate its practical utility for improving VLA generalization. The project page is at https://rlvla.github.io

## Content
Large Vision-Language Action (VLA) models have shown significant potential for embodied AI. However, their predominant training via supervised fine-tuning (SFT) limits generalization due to susceptibility to compounding errors under distribution shifts. Reinforcement learning (RL) offers a path to overcome these limitations by optimizing for task objectives via trial-and-error, yet a systematic understanding of its specific generalization benefits for VLAs compared to SFT is lacking. To address this, our study introduces a comprehensive benchmark for evaluating VLA generalization and systematically investigates the impact of RL fine-tuning across diverse visual, semantic, and execution dimensions. Our extensive experiments reveal that RL fine-tuning, particularly with PPO, significantly enhances generalization in semantic understanding and execution robustness over SFT, while maintaining comparable visual robustness. We identify PPO as a more effective RL algorithm for VLAs than LLM-derived methods like DPO and GRPO. We also develop a simple recipe for efficient PPO training on VLAs, and demonstrate its practical utility for improving VLA generalization. The project page is at https://rlvla.github.io

## 개요
Large Vision-Language Action (VLA) 모델은 임베디드 AI에서 상당한 잠재력을 보여주고 있습니다. 그러나 지도 미세 조정(SFT)을 통한 주된 훈련 방식은 분포 변화 하에서 오류 누적에 취약하여 일반화 능력을 제한합니다. 강화 학습(RL)은 시행착오를 통해 작업 목표를 최적화함으로써 이러한 한계를 극복할 수 있는 경로를 제공하지만, SFT와 비교하여 VLA에 대한 특정 일반화 이점에 대한 체계적인 이해는 부족합니다. 이를 해결하기 위해, 본 연구는 VLA 일반화를 평가하기 위한 포괄적인 벤치마크를 도입하고, 다양한 시각적, 의미적, 실행적 차원에서 RL 미세 조정의 영향을 체계적으로 조사합니다. 광범위한 실험을 통해 RL 미세 조정, 특히 PPO를 사용한 경우, SFT에 비해 의미 이해와 실행 견고성에서 일반화를 크게 향상시키면서 시각적 견고성은 유사하게 유지함을 밝혔습니다. 우리는 PPO가 DPO 및 GRPO와 같은 LLM 기반 방법보다 VLA에 더 효과적인 RL 알고리즘임을 확인했습니다. 또한 VLA에 대한 효율적인 PPO 훈련을 위한 간단한 레시피를 개발하고, VLA 일반화 개선을 위한 실용적 유용성을 입증했습니다. 프로젝트 페이지는 https://rlvla.github.io 에 있습니다.

## 핵심 내용
Large Vision-Language Action (VLA) 모델은 임베디드 AI에서 상당한 잠재력을 보여주고 있습니다. 그러나 지도 미세 조정(SFT)을 통한 주된 훈련 방식은 분포 변화 하에서 오류 누적에 취약하여 일반화 능력을 제한합니다. 강화 학습(RL)은 시행착오를 통해 작업 목표를 최적화함으로써 이러한 한계를 극복할 수 있는 경로를 제공하지만, SFT와 비교하여 VLA에 대한 특정 일반화 이점에 대한 체계적인 이해는 부족합니다. 이를 해결하기 위해, 본 연구는 VLA 일반화를 평가하기 위한 포괄적인 벤치마크를 도입하고, 다양한 시각적, 의미적, 실행적 차원에서 RL 미세 조정의 영향을 체계적으로 조사합니다. 광범위한 실험을 통해 RL 미세 조정, 특히 PPO를 사용한 경우, SFT에 비해 의미 이해와 실행 견고성에서 일반화를 크게 향상시키면서 시각적 견고성은 유사하게 유지함을 밝혔습니다. 우리는 PPO가 DPO 및 GRPO와 같은 LLM 기반 방법보다 VLA에 더 효과적인 RL 알고리즘임을 확인했습니다. 또한 VLA에 대한 효율적인 PPO 훈련을 위한 간단한 레시피를 개발하고, VLA 일반화 개선을 위한 실용적 유용성을 입증했습니다. 프로젝트 페이지는 https://rlvla.github.io 에 있습니다.

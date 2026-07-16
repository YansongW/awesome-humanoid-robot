---
$id: ent_paper_fang_dualvla_building_a_generalizab_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action'
  zh: DualVLA
  ko: 'DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action'
summary:
  en: 'DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action (DualVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by MoE Key Laboratory of Brain-inspired Intelligent
    Perception and Cognition, University of Science and Technology of China, State Key Laboratory of Multimedia Information
    Processing, School of Computer Science, Peking University, CUHK.'
  zh: 'DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action (DualVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by MoE Key Laboratory of Brain-inspired Intelligent
    Perception and Cognition, University of Science and Technology of China, State Key Laboratory of Multimedia Information
    Processing, School of Computer Science, Peking University, CUHK.'
  ko: 'DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action (DualVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by MoE Key Laboratory of Brain-inspired Intelligent
    Perception and Cognition, University of Science and Technology of China, State Key Laboratory of Multimedia Information
    Processing, School of Computer Science, Peking University, CUHK.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dualvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.22134v1.
sources:
- id: src_001
  type: paper
  title: 'DualVLA: Building a Generalizable Embodied Agent via Partial Decoupling of Reasoning and Action (arXiv)'
  url: https://arxiv.org/abs/2511.22134
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DualVLA source
  url: https://doi.org/10.48550/arXiv.2511.22134
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
To build a generalizable Vision-Language-Action (VLA) model with strong reasoning ability, a common strategy is to first train a specialist VLA on robot demonstrations to acquire reliable manipulation skills, and then incorporate mixed annotated robot data together with multimodal data to restore broader reasoning capabilities. However, we observe that the resulting reasoning VLA often suffers from degraded action performance compared to the specialist model before fine-tuning, a phenomenon we refer to as action degeneration. To address this issue, we propose DualVLA, which enhances action performance through carefully designed post-training while still preserving reasoning capability. We first introduce a dual-layer data pruning method that removes redundant embodied reasoning, preventing it from adversely influencing action learning. To further strengthen action generation, we design a dual-teacher adaptive distillation strategy that assigns different supervision signals to different data domains while maintaining reasoning ability. To fill the evaluation gap for generalist VLAs, we also propose VLA Score, which decouples VLA capability into reasoning, intention, action, and alignment dimensions for a more fine-grained assessment. Experiments show that DualVLA achieves an average success rate of 61.0 in SimplerEnv and an average score of 65.4 across eight competitive multimodal benchmarks, demonstrating a stronger balance between precise action execution and multimodal understanding. Project Website: https://costaliya.github.io/DualVLA/.

## 核心内容
To build a generalizable Vision-Language-Action (VLA) model with strong reasoning ability, a common strategy is to first train a specialist VLA on robot demonstrations to acquire reliable manipulation skills, and then incorporate mixed annotated robot data together with multimodal data to restore broader reasoning capabilities. However, we observe that the resulting reasoning VLA often suffers from degraded action performance compared to the specialist model before fine-tuning, a phenomenon we refer to as action degeneration. To address this issue, we propose DualVLA, which enhances action performance through carefully designed post-training while still preserving reasoning capability. We first introduce a dual-layer data pruning method that removes redundant embodied reasoning, preventing it from adversely influencing action learning. To further strengthen action generation, we design a dual-teacher adaptive distillation strategy that assigns different supervision signals to different data domains while maintaining reasoning ability. To fill the evaluation gap for generalist VLAs, we also propose VLA Score, which decouples VLA capability into reasoning, intention, action, and alignment dimensions for a more fine-grained assessment. Experiments show that DualVLA achieves an average success rate of 61.0 in SimplerEnv and an average score of 65.4 across eight competitive multimodal benchmarks, demonstrating a stronger balance between precise action execution and multimodal understanding. Project Website: https://costaliya.github.io/DualVLA/.

## 参考
- http://arxiv.org/abs/2511.22134v1

## Overview
To build a generalizable Vision-Language-Action (VLA) model with strong reasoning ability, a common strategy is to first train a specialist VLA on robot demonstrations to acquire reliable manipulation skills, and then incorporate mixed annotated robot data together with multimodal data to restore broader reasoning capabilities. However, we observe that the resulting reasoning VLA often suffers from degraded action performance compared to the specialist model before fine-tuning, a phenomenon we refer to as action degeneration. To address this issue, we propose DualVLA, which enhances action performance through carefully designed post-training while still preserving reasoning capability. We first introduce a dual-layer data pruning method that removes redundant embodied reasoning, preventing it from adversely influencing action learning. To further strengthen action generation, we design a dual-teacher adaptive distillation strategy that assigns different supervision signals to different data domains while maintaining reasoning ability. To fill the evaluation gap for generalist VLAs, we also propose VLA Score, which decouples VLA capability into reasoning, intention, action, and alignment dimensions for a more fine-grained assessment. Experiments show that DualVLA achieves an average success rate of 61.0 in SimplerEnv and an average score of 65.4 across eight competitive multimodal benchmarks, demonstrating a stronger balance between precise action execution and multimodal understanding. Project Website: https://costaliya.github.io/DualVLA/.

## Content
To build a generalizable Vision-Language-Action (VLA) model with strong reasoning ability, a common strategy is to first train a specialist VLA on robot demonstrations to acquire reliable manipulation skills, and then incorporate mixed annotated robot data together with multimodal data to restore broader reasoning capabilities. However, we observe that the resulting reasoning VLA often suffers from degraded action performance compared to the specialist model before fine-tuning, a phenomenon we refer to as action degeneration. To address this issue, we propose DualVLA, which enhances action performance through carefully designed post-training while still preserving reasoning capability. We first introduce a dual-layer data pruning method that removes redundant embodied reasoning, preventing it from adversely influencing action learning. To further strengthen action generation, we design a dual-teacher adaptive distillation strategy that assigns different supervision signals to different data domains while maintaining reasoning ability. To fill the evaluation gap for generalist VLAs, we also propose VLA Score, which decouples VLA capability into reasoning, intention, action, and alignment dimensions for a more fine-grained assessment. Experiments show that DualVLA achieves an average success rate of 61.0 in SimplerEnv and an average score of 65.4 across eight competitive multimodal benchmarks, demonstrating a stronger balance between precise action execution and multimodal understanding. Project Website: https://costaliya.github.io/DualVLA/.

## 개요
강력한 추론 능력을 갖춘 일반화 가능한 Vision-Language-Action (VLA) 모델을 구축하기 위한 일반적인 전략은 먼저 로봇 시연 데이터를 통해 전문가 VLA를 학습시켜 신뢰할 수 있는 조작 기술을 습득한 후, 혼합된 주석 처리된 로봇 데이터와 멀티모달 데이터를 함께 통합하여 더 넓은 추론 능력을 복원하는 것입니다. 그러나 우리는 결과적으로 얻어진 추론 VLA가 미세 조정 전의 전문가 모델에 비해 종종 저하된 행동 성능을 보인다는 점을 관찰했으며, 이를 행동 퇴화(action degeneration) 현상이라고 부릅니다. 이 문제를 해결하기 위해 우리는 DualVLA를 제안합니다. DualVLA는 추론 능력을 유지하면서도 신중하게 설계된 사후 학습(post-training)을 통해 행동 성능을 향상시킵니다. 먼저, 중복된 체화된 추론(embodied reasoning)을 제거하여 행동 학습에 부정적인 영향을 미치지 않도록 하는 이중 계층 데이터 정리(dual-layer data pruning) 방법을 도입합니다. 행동 생성을 더욱 강화하기 위해, 우리는 추론 능력을 유지하면서도 서로 다른 데이터 도메인에 다른 감독 신호를 할당하는 이중 교사 적응형 증류(dual-teacher adaptive distillation) 전략을 설계합니다. 일반주의 VLA에 대한 평가 격차를 해소하기 위해, 우리는 VLA Score도 제안합니다. 이는 VLA 능력을 추론, 의도, 행동 및 정렬 차원으로 분리하여 더 세분화된 평가를 가능하게 합니다. 실험 결과, DualVLA는 SimplerEnv에서 평균 성공률 61.0을 달성하고, 8개의 경쟁력 있는 멀티모달 벤치마크에서 평균 점수 65.4를 기록하여 정밀한 행동 실행과 멀티모달 이해 간의 더 강력한 균형을 보여줍니다. 프로젝트 웹사이트: https://costaliya.github.io/DualVLA/.

## 핵심 내용
강력한 추론 능력을 갖춘 일반화 가능한 Vision-Language-Action (VLA) 모델을 구축하기 위한 일반적인 전략은 먼저 로봇 시연 데이터를 통해 전문가 VLA를 학습시켜 신뢰할 수 있는 조작 기술을 습득한 후, 혼합된 주석 처리된 로봇 데이터와 멀티모달 데이터를 함께 통합하여 더 넓은 추론 능력을 복원하는 것입니다. 그러나 우리는 결과적으로 얻어진 추론 VLA가 미세 조정 전의 전문가 모델에 비해 종종 저하된 행동 성능을 보인다는 점을 관찰했으며, 이를 행동 퇴화(action degeneration) 현상이라고 부릅니다. 이 문제를 해결하기 위해 우리는 DualVLA를 제안합니다. DualVLA는 추론 능력을 유지하면서도 신중하게 설계된 사후 학습(post-training)을 통해 행동 성능을 향상시킵니다. 먼저, 중복된 체화된 추론(embodied reasoning)을 제거하여 행동 학습에 부정적인 영향을 미치지 않도록 하는 이중 계층 데이터 정리(dual-layer data pruning) 방법을 도입합니다. 행동 생성을 더욱 강화하기 위해, 우리는 추론 능력을 유지하면서도 서로 다른 데이터 도메인에 다른 감독 신호를 할당하는 이중 교사 적응형 증류(dual-teacher adaptive distillation) 전략을 설계합니다. 일반주의 VLA에 대한 평가 격차를 해소하기 위해, 우리는 VLA Score도 제안합니다. 이는 VLA 능력을 추론, 의도, 행동 및 정렬 차원으로 분리하여 더 세분화된 평가를 가능하게 합니다. 실험 결과, DualVLA는 SimplerEnv에서 평균 성공률 61.0을 달성하고, 8개의 경쟁력 있는 멀티모달 벤치마크에서 평균 점수 65.4를 기록하여 정밀한 행동 실행과 멀티모달 이해 간의 더 강력한 균형을 보여줍니다. 프로젝트 웹사이트: https://costaliya.github.io/DualVLA/.

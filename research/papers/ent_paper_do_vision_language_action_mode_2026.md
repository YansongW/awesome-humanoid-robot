---
$id: ent_paper_do_vision_language_action_mode_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Do Vision-Language-Action Models Mean What They Say? On the Role of Faithfulness in Embodied Reasoning
  zh: Do Vision-Language-Action Models Mean What They Say? On the Role of Faithfulness in Embodied Reasoning
  ko: Do Vision-Language-Action Models Mean What They Say? On the Role of Faithfulness in Embodied Reasoning
summary:
  en: 'arXiv:2607.04681v1 Announce Type: new Abstract: Embodied Chain-of-Thought has emerged as a promising mechanism to enhance
    robot decision-making and interpretability in black-box Vision-Language Action (VLA) models. However, whether this verbalized
    Chain-of-Thought truthfully reflects the policy''s underlying decision process remains poorly understood. We distinguish
    between functional reasoning, in which reasoning improves task performance, and faithful reasoning, in which reasoning
    truly reflects the policy''s internal decision process. We argue that SoTA alignment strategies offer a necessary but
    insufficient notion of faithfulness, admitting reasoning whose intermediate steps can mask the causal links in action
    prediction through confounding factors (e.g., reasoning that is ungrounded in the environment and internally disconnected
    or inconsistent), restricting policy generalization. We study this gap through a human evaluation of a SoTA reasoning
    model for autonomous driving, revealing an inconsistent coupling between reasoning quality and downstream trajectory improvement.
    We then operationalize a behavioral surrogate for embodied faithfulness through a learned critic, Pinocchio, scoring observation
    grounding and stepwise coherence, and use this critic as a dense reward signal in post-training an embodied policy with
    reinforcement learning. Across withheld driving benchmarks, our post-trained planner improves faithfulness by 4% and 18%
    over SoTA alignment and trajectory error post-training baselines, respectively, while maintaining competitive downstream
    task performance. Finally, on a synthetic out-of-distribution test set, post-training for faithfulness improves policy
    responsiveness to rare counterfactual scenarios by 1.6x that of a SoTA policy, suggesting that faithful reasoning traces
    contribute to more robust, generalizable, and interpretable embodied intelligence. Project page: https://mjf-su.github.io/pinocchio/'
  zh: 'arXiv:2607.04681v1 Announce Type: new Abstract: Embodied Chain-of-Thought has emerged as a promising mechanism to enhance
    robot decision-making and interpretability in black-box Vision-Language Action (VLA) models. However, whether this verbalized
    Chain-of-Thought truthfully reflects the policy''s underlying decision process remains poorly understood. We distinguish
    between functional reasoning, in which reasoning improves task performance, and faithful reasoning, in which reasoning
    truly reflects the policy''s internal decision process. We argue that SoTA alignment strategies offer a necessary but
    insufficient notion of faithfulness, admitting reasoning whose intermediate steps can mask the causal links in action
    prediction through confounding factors (e.g., reasoning that is ungrounded in the environment and internally disconnected
    or inconsistent), restricting policy generalization. We study this gap through a human evaluation of a SoTA reasoning
    model for autonomous driving, revealing an inconsistent coupling between reasoning quality and downstream trajectory improvement.
    We then operationalize a behavioral surrogate for embodied faithfulness through a learned critic, Pinocchio, scoring observation
    grounding and stepwise coherence, and use this critic as a dense reward signal in post-training an embodied policy with
    reinforcement learning. Across withheld driving benchmarks, our post-trained planner improves faithfulness by 4% and 18%
    over SoTA alignment and trajectory error post-training baselines, respectively, while maintaining competitive downstream
    task performance. Finally, on a synthetic out-of-distribution test set, post-training for faithfulness improves policy
    responsiveness to rare counterfactual scenarios by 1.6x that of a SoTA policy, suggesting that faithful reasoning traces
    contribute to more robust, generalizable, and interpretable embodied intelligence. Project page: https://mjf-su.github.io/pinocchio/'
  ko: 'arXiv:2607.04681v1 Announce Type: new Abstract: Embodied Chain-of-Thought has emerged as a promising mechanism to enhance
    robot decision-making and interpretability in black-box Vision-Language Action (VLA) models. However, whether this verbalized
    Chain-of-Thought truthfully reflects the policy''s underlying decision process remains poorly understood. We distinguish
    between functional reasoning, in which reasoning improves task performance, and faithful reasoning, in which reasoning
    truly reflects the policy''s internal decision process. We argue that SoTA alignment strategies offer a necessary but
    insufficient notion of faithfulness, admitting reasoning whose intermediate steps can mask the causal links in action
    prediction through confounding factors (e.g., reasoning that is ungrounded in the environment and internally disconnected
    or inconsistent), restricting policy generalization. We study this gap through a human evaluation of a SoTA reasoning
    model for autonomous driving, revealing an inconsistent coupling between reasoning quality and downstream trajectory improvement.
    We then operationalize a behavioral surrogate for embodied faithfulness through a learned critic, Pinocchio, scoring observation
    grounding and stepwise coherence, and use this critic as a dense reward signal in post-training an embodied policy with
    reinforcement learning. Across withheld driving benchmarks, our post-trained planner improves faithfulness by 4% and 18%
    over SoTA alignment and trajectory error post-training baselines, respectively, while maintaining competitive downstream
    task performance. Finally, on a synthetic out-of-distribution test set, post-training for faithfulness improves policy
    responsiveness to rare counterfactual scenarios by 1.6x that of a SoTA policy, suggesting that faithful reasoning traces
    contribute to more robust, generalizable, and interpretable embodied intelligence. Project page: https://mjf-su.github.io/pinocchio/'
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
- do_vision_language_action_mode
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04681v1.
sources:
- id: src_001
  type: paper
  title: Do Vision-Language-Action Models Mean What They Say? On the Role of Faithfulness in Embodied Reasoning (arXiv)
  url: https://arxiv.org/abs/2607.04681
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Embodied Chain-of-Thought has emerged as a promising mechanism to enhance robot decision-making and interpretability in black-box Vision-Language Action (VLA) models. However, whether this verbalized Chain-of-Thought truthfully reflects the policy's underlying decision process remains poorly understood. We distinguish between functional reasoning, in which reasoning improves task performance, and faithful reasoning, in which reasoning truly reflects the policy's internal decision process. We argue that SoTA alignment strategies offer a necessary but insufficient notion of faithfulness, admitting reasoning whose intermediate steps can mask the causal links in action prediction through confounding factors (e.g., reasoning that is ungrounded in the environment and internally disconnected or inconsistent), restricting policy generalization. We study this gap through a human evaluation of a SoTA reasoning model for autonomous driving, revealing an inconsistent coupling between reasoning quality and downstream trajectory improvement. We then operationalize a behavioral surrogate for embodied faithfulness through a learned critic, Pinocchio, scoring observation grounding and stepwise coherence, and use this critic as a dense reward signal in post-training an embodied policy with reinforcement learning. Across withheld driving benchmarks, our post-trained planner improves faithfulness by 4% and 18% over SoTA alignment and trajectory error post-training baselines, respectively, while maintaining competitive downstream task performance. Finally, on a synthetic out-of-distribution test set, post-training for faithfulness improves policy responsiveness to rare counterfactual scenarios by 1.6x that of a SoTA policy, suggesting that faithful reasoning traces contribute to more robust, generalizable, and interpretable embodied intelligence. Project page: https://mjf-su.github.io/pinocchio/

## 核心内容
Embodied Chain-of-Thought has emerged as a promising mechanism to enhance robot decision-making and interpretability in black-box Vision-Language Action (VLA) models. However, whether this verbalized Chain-of-Thought truthfully reflects the policy's underlying decision process remains poorly understood. We distinguish between functional reasoning, in which reasoning improves task performance, and faithful reasoning, in which reasoning truly reflects the policy's internal decision process. We argue that SoTA alignment strategies offer a necessary but insufficient notion of faithfulness, admitting reasoning whose intermediate steps can mask the causal links in action prediction through confounding factors (e.g., reasoning that is ungrounded in the environment and internally disconnected or inconsistent), restricting policy generalization. We study this gap through a human evaluation of a SoTA reasoning model for autonomous driving, revealing an inconsistent coupling between reasoning quality and downstream trajectory improvement. We then operationalize a behavioral surrogate for embodied faithfulness through a learned critic, Pinocchio, scoring observation grounding and stepwise coherence, and use this critic as a dense reward signal in post-training an embodied policy with reinforcement learning. Across withheld driving benchmarks, our post-trained planner improves faithfulness by 4% and 18% over SoTA alignment and trajectory error post-training baselines, respectively, while maintaining competitive downstream task performance. Finally, on a synthetic out-of-distribution test set, post-training for faithfulness improves policy responsiveness to rare counterfactual scenarios by 1.6x that of a SoTA policy, suggesting that faithful reasoning traces contribute to more robust, generalizable, and interpretable embodied intelligence. Project page: https://mjf-su.github.io/pinocchio/

## 参考
- http://arxiv.org/abs/2607.04681v1

## Overview
Embodied Chain-of-Thought has emerged as a promising mechanism to enhance robot decision-making and interpretability in black-box Vision-Language Action (VLA) models. However, whether this verbalized Chain-of-Thought truthfully reflects the policy's underlying decision process remains poorly understood. We distinguish between functional reasoning, in which reasoning improves task performance, and faithful reasoning, in which reasoning truly reflects the policy's internal decision process. We argue that SoTA alignment strategies offer a necessary but insufficient notion of faithfulness, admitting reasoning whose intermediate steps can mask the causal links in action prediction through confounding factors (e.g., reasoning that is ungrounded in the environment and internally disconnected or inconsistent), restricting policy generalization. We study this gap through a human evaluation of a SoTA reasoning model for autonomous driving, revealing an inconsistent coupling between reasoning quality and downstream trajectory improvement. We then operationalize a behavioral surrogate for embodied faithfulness through a learned critic, Pinocchio, scoring observation grounding and stepwise coherence, and use this critic as a dense reward signal in post-training an embodied policy with reinforcement learning. Across withheld driving benchmarks, our post-trained planner improves faithfulness by 4% and 18% over SoTA alignment and trajectory error post-training baselines, respectively, while maintaining competitive downstream task performance. Finally, on a synthetic out-of-distribution test set, post-training for faithfulness improves policy responsiveness to rare counterfactual scenarios by 1.6x that of a SoTA policy, suggesting that faithful reasoning traces contribute to more robust, generalizable, and interpretable embodied intelligence. Project page: https://mjf-su.github.io/pinocchio/

## Content
Embodied Chain-of-Thought has emerged as a promising mechanism to enhance robot decision-making and interpretability in black-box Vision-Language Action (VLA) models. However, whether this verbalized Chain-of-Thought truthfully reflects the policy's underlying decision process remains poorly understood. We distinguish between functional reasoning, in which reasoning improves task performance, and faithful reasoning, in which reasoning truly reflects the policy's internal decision process. We argue that SoTA alignment strategies offer a necessary but insufficient notion of faithfulness, admitting reasoning whose intermediate steps can mask the causal links in action prediction through confounding factors (e.g., reasoning that is ungrounded in the environment and internally disconnected or inconsistent), restricting policy generalization. We study this gap through a human evaluation of a SoTA reasoning model for autonomous driving, revealing an inconsistent coupling between reasoning quality and downstream trajectory improvement. We then operationalize a behavioral surrogate for embodied faithfulness through a learned critic, Pinocchio, scoring observation grounding and stepwise coherence, and use this critic as a dense reward signal in post-training an embodied policy with reinforcement learning. Across withheld driving benchmarks, our post-trained planner improves faithfulness by 4% and 18% over SoTA alignment and trajectory error post-training baselines, respectively, while maintaining competitive downstream task performance. Finally, on a synthetic out-of-distribution test set, post-training for faithfulness improves policy responsiveness to rare counterfactual scenarios by 1.6x that of a SoTA policy, suggesting that faithful reasoning traces contribute to more robust, generalizable, and interpretable embodied intelligence. Project page: https://mjf-su.github.io/pinocchio/

## 개요
Embodied Chain-of-Thought는 블랙박스 Vision-Language Action (VLA) 모델에서 로봇의 의사 결정과 해석 가능성을 향상시키는 유망한 메커니즘으로 부상했습니다. 그러나 이러한 언어화된 Chain-of-Thought가 정책의 근본적인 의사 결정 과정을 진실되게 반영하는지 여부는 아직 잘 이해되지 않고 있습니다. 우리는 추론이 작업 성능을 향상시키는 기능적 추론과 추론이 정책의 내부 의사 결정 과정을 진실되게 반영하는 충실한 추론을 구분합니다. 우리는 SoTA 정렬 전략이 필요하지만 충분하지 않은 충실성 개념을 제공한다고 주장하며, 이는 중간 단계가 혼란 요인(예: 환경에 근거하지 않고 내부적으로 단절되거나 일관성이 없는 추론)을 통해 행동 예측의 인과 관계를 가릴 수 있는 추론을 허용하여 정책 일반화를 제한합니다. 우리는 자율 주행을 위한 SoTA 추론 모델의 인간 평가를 통해 이러한 격차를 연구하며, 추론 품질과 하위 궤적 개선 사이의 불일치하는 결합을 밝혀냅니다. 그런 다음 학습된 비평가인 Pinocchio를 통해 관찰 근거와 단계적 일관성을 평가하는 행동적 대리 지표를 구현하고, 이 비평가를 강화 학습을 통한 임베디드 정책의 사후 훈련에서 밀집 보상 신호로 사용합니다. 보류된 운전 벤치마크에서 사후 훈련된 플래너는 SoTA 정렬 및 궤적 오류 사후 훈련 기준선 대비 각각 4% 및 18%의 충실성 향상을 보이며 경쟁력 있는 하위 작업 성능을 유지합니다. 마지막으로 합성 분포 외 테스트 세트에서 충실성을 위한 사후 훈련은 드문 반사실적 시나리오에 대한 정책 응답성을 SoTA 정책 대비 1.6배 향상시켜, 충실한 추론 흔적이 더 강건하고 일반화 가능하며 해석 가능한 임베디드 지능에 기여함을 시사합니다. 프로젝트 페이지: https://mjf-su.github.io/pinocchio/

## 핵심 내용
Embodied Chain-of-Thought는 블랙박스 Vision-Language Action (VLA) 모델에서 로봇의 의사 결정과 해석 가능성을 향상시키는 유망한 메커니즘으로 부상했습니다. 그러나 이러한 언어화된 Chain-of-Thought가 정책의 근본적인 의사 결정 과정을 진실되게 반영하는지 여부는 아직 잘 이해되지 않고 있습니다. 우리는 추론이 작업 성능을 향상시키는 기능적 추론과 추론이 정책의 내부 의사 결정 과정을 진실되게 반영하는 충실한 추론을 구분합니다. 우리는 SoTA 정렬 전략이 필요하지만 충분하지 않은 충실성 개념을 제공한다고 주장하며, 이는 중간 단계가 혼란 요인(예: 환경에 근거하지 않고 내부적으로 단절되거나 일관성이 없는 추론)을 통해 행동 예측의 인과 관계를 가릴 수 있는 추론을 허용하여 정책 일반화를 제한합니다. 우리는 자율 주행을 위한 SoTA 추론 모델의 인간 평가를 통해 이러한 격차를 연구하며, 추론 품질과 하위 궤적 개선 사이의 불일치하는 결합을 밝혀냅니다. 그런 다음 학습된 비평가인 Pinocchio를 통해 관찰 근거와 단계적 일관성을 평가하는 행동적 대리 지표를 구현하고, 이 비평가를 강화 학습을 통한 임베디드 정책의 사후 훈련에서 밀집 보상 신호로 사용합니다. 보류된 운전 벤치마크에서 사후 훈련된 플래너는 SoTA 정렬 및 궤적 오류 사후 훈련 기준선 대비 각각 4% 및 18%의 충실성 향상을 보이며 경쟁력 있는 하위 작업 성능을 유지합니다. 마지막으로 합성 분포 외 테스트 세트에서 충실성을 위한 사후 훈련은 드문 반사실적 시나리오에 대한 정책 응답성을 SoTA 정책 대비 1.6배 향상시켜, 충실한 추론 흔적이 더 강건하고 일반화 가능하며 해석 가능한 임베디드 지능에 기여함을 시사합니다. 프로젝트 페이지: https://mjf-su.github.io/pinocchio/

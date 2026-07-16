---
$id: ent_paper_zhao_more_unlocking_scalability_in_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MoRE: Unlocking Scalability in Reinforcement Learning for Quadruped Vision-Language-Action Models'
  zh: MoRE
  ko: 'MoRE: Unlocking Scalability in Reinforcement Learning for Quadruped Vision-Language-Action Models'
summary:
  en: 'MoRE: Unlocking Scalability in Reinforcement Learning for Quadruped Vision-Language-Action Models (MoRE), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Sun Yat-sen University, Guangdong Key Laboratory
    of Big Data Analysis and Processing, X-Era AI Lab, and published at ICRA25.'
  zh: 'MoRE: Unlocking Scalability in Reinforcement Learning for Quadruped Vision-Language-Action Models (MoRE), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Sun Yat-sen University, Guangdong Key Laboratory
    of Big Data Analysis and Processing, X-Era AI Lab, and published at ICRA25.'
  ko: 'MoRE: Unlocking Scalability in Reinforcement Learning for Quadruped Vision-Language-Action Models (MoRE), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Sun Yat-sen University, Guangdong Key Laboratory
    of Big Data Analysis and Processing, X-Era AI Lab, and published at ICRA25.'
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
- more
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.08007v1.
sources:
- id: src_001
  type: website
  title: MoRE source
  url: https://doi.org/10.1109/ICRA55743.2025.11128601
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Developing versatile quadruped robots that can smoothly perform various actions and tasks in real-world environments remains a significant challenge. This paper introduces a novel vision-language-action (VLA) model, mixture of robotic experts (MoRE), for quadruped robots that aim to introduce reinforcement learning (RL) for fine-tuning large-scale VLA models with a large amount of mixed-quality data. MoRE integrates multiple low-rank adaptation modules as distinct experts within a dense multi-modal large language model (MLLM), forming a sparse-activated mixture-of-experts model. This design enables the model to effectively adapt to a wide array of downstream tasks. Moreover, we employ a reinforcement learning-based training objective to train our model as a Q-function after deeply exploring the structural properties of our tasks. Effective learning from automatically collected mixed-quality data enhances data efficiency and model performance. Extensive experiments demonstrate that MoRE outperforms all baselines across six different skills and exhibits superior generalization capabilities in out-of-distribution scenarios. We further validate our method in real-world scenarios, confirming the practicality of our approach and laying a solid foundation for future research on multi-task learning in quadruped robots.

## 核心内容
Developing versatile quadruped robots that can smoothly perform various actions and tasks in real-world environments remains a significant challenge. This paper introduces a novel vision-language-action (VLA) model, mixture of robotic experts (MoRE), for quadruped robots that aim to introduce reinforcement learning (RL) for fine-tuning large-scale VLA models with a large amount of mixed-quality data. MoRE integrates multiple low-rank adaptation modules as distinct experts within a dense multi-modal large language model (MLLM), forming a sparse-activated mixture-of-experts model. This design enables the model to effectively adapt to a wide array of downstream tasks. Moreover, we employ a reinforcement learning-based training objective to train our model as a Q-function after deeply exploring the structural properties of our tasks. Effective learning from automatically collected mixed-quality data enhances data efficiency and model performance. Extensive experiments demonstrate that MoRE outperforms all baselines across six different skills and exhibits superior generalization capabilities in out-of-distribution scenarios. We further validate our method in real-world scenarios, confirming the practicality of our approach and laying a solid foundation for future research on multi-task learning in quadruped robots.

## 参考
- http://arxiv.org/abs/2503.08007v1

## Overview
Developing versatile quadruped robots that can smoothly perform various actions and tasks in real-world environments remains a significant challenge. This paper introduces a novel vision-language-action (VLA) model, mixture of robotic experts (MoRE), for quadruped robots that aim to introduce reinforcement learning (RL) for fine-tuning large-scale VLA models with a large amount of mixed-quality data. MoRE integrates multiple low-rank adaptation modules as distinct experts within a dense multi-modal large language model (MLLM), forming a sparse-activated mixture-of-experts model. This design enables the model to effectively adapt to a wide array of downstream tasks. Moreover, we employ a reinforcement learning-based training objective to train our model as a Q-function after deeply exploring the structural properties of our tasks. Effective learning from automatically collected mixed-quality data enhances data efficiency and model performance. Extensive experiments demonstrate that MoRE outperforms all baselines across six different skills and exhibits superior generalization capabilities in out-of-distribution scenarios. We further validate our method in real-world scenarios, confirming the practicality of our approach and laying a solid foundation for future research on multi-task learning in quadruped robots.

## Content
Developing versatile quadruped robots that can smoothly perform various actions and tasks in real-world environments remains a significant challenge. This paper introduces a novel vision-language-action (VLA) model, mixture of robotic experts (MoRE), for quadruped robots that aim to introduce reinforcement learning (RL) for fine-tuning large-scale VLA models with a large amount of mixed-quality data. MoRE integrates multiple low-rank adaptation modules as distinct experts within a dense multi-modal large language model (MLLM), forming a sparse-activated mixture-of-experts model. This design enables the model to effectively adapt to a wide array of downstream tasks. Moreover, we employ a reinforcement learning-based training objective to train our model as a Q-function after deeply exploring the structural properties of our tasks. Effective learning from automatically collected mixed-quality data enhances data efficiency and model performance. Extensive experiments demonstrate that MoRE outperforms all baselines across six different skills and exhibits superior generalization capabilities in out-of-distribution scenarios. We further validate our method in real-world scenarios, confirming the practicality of our approach and laying a solid foundation for future research on multi-task learning in quadruped robots.

## 개요
실제 환경에서 다양한 동작과 작업을 원활히 수행할 수 있는 다재다능한 사족 로봇을 개발하는 것은 여전히 중요한 과제입니다. 본 논문은 혼합 품질의 대규모 데이터를 활용하여 대규모 VLA 모델을 미세 조정하기 위해 강화 학습(RL)을 도입하는 것을 목표로 하는 사족 로봇용 새로운 시각-언어-행동(VLA) 모델, 혼합 로봇 전문가(MoRE)를 소개합니다. MoRE는 밀집된 다중 모달 대규모 언어 모델(MLLM) 내에 여러 저랭크 적응 모듈을 개별 전문가로 통합하여 희소 활성화 혼합 전문가 모델을 형성합니다. 이 설계는 모델이 다양한 하위 작업에 효과적으로 적응할 수 있도록 합니다. 또한, 작업의 구조적 특성을 깊이 탐구한 후 강화 학습 기반 훈련 목표를 사용하여 모델을 Q-함수로 훈련합니다. 자동으로 수집된 혼합 품질 데이터로부터 효과적으로 학습함으로써 데이터 효율성과 모델 성능을 향상시킵니다. 광범위한 실험을 통해 MoRE가 여섯 가지 다양한 기술에서 모든 기준 모델을 능가하며, 분포 외 시나리오에서 뛰어난 일반화 능력을 보여줌을 입증했습니다. 실제 환경에서도 방법을 추가로 검증하여 접근 방식의 실용성을 확인하고, 사족 로봇의 다중 작업 학습에 대한 향후 연구를 위한 견고한 기반을 마련했습니다.

## 핵심 내용
실제 환경에서 다양한 동작과 작업을 원활히 수행할 수 있는 다재다능한 사족 로봇을 개발하는 것은 여전히 중요한 과제입니다. 본 논문은 혼합 품질의 대규모 데이터를 활용하여 대규모 VLA 모델을 미세 조정하기 위해 강화 학습(RL)을 도입하는 것을 목표로 하는 사족 로봇용 새로운 시각-언어-행동(VLA) 모델, 혼합 로봇 전문가(MoRE)를 소개합니다. MoRE는 밀집된 다중 모달 대규모 언어 모델(MLLM) 내에 여러 저랭크 적응 모듈을 개별 전문가로 통합하여 희소 활성화 혼합 전문가 모델을 형성합니다. 이 설계는 모델이 다양한 하위 작업에 효과적으로 적응할 수 있도록 합니다. 또한, 작업의 구조적 특성을 깊이 탐구한 후 강화 학습 기반 훈련 목표를 사용하여 모델을 Q-함수로 훈련합니다. 자동으로 수집된 혼합 품질 데이터로부터 효과적으로 학습함으로써 데이터 효율성과 모델 성능을 향상시킵니다. 광범위한 실험을 통해 MoRE가 여섯 가지 다양한 기술에서 모든 기준 모델을 능가하며, 분포 외 시나리오에서 뛰어난 일반화 능력을 보여줌을 입증했습니다. 실제 환경에서도 방법을 추가로 검증하여 접근 방식의 실용성을 확인하고, 사족 로봇의 다중 작업 학습에 대한 향후 연구를 위한 견고한 기반을 마련했습니다.

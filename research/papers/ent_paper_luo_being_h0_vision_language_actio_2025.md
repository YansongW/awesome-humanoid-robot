---
$id: ent_paper_luo_being_h0_vision_language_actio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos'
  zh: Being-H0
  ko: 'Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos'
summary:
  en: 'Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos (Being-H0), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Renmin University of China, BeingBeyond.'
  zh: 'Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos (Being-H0), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Renmin University of China, BeingBeyond.'
  ko: 'Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos (Being-H0), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Renmin University of China, BeingBeyond.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- being_h0
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.15597v1.
sources:
- id: src_001
  type: paper
  title: 'Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos (arXiv)'
  url: https://arxiv.org/abs/2507.15597
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Being-H0 source
  url: https://doi.org/10.48550/arXiv.2507.15597
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We introduce Being-H0, a dexterous Vision-Language-Action model (VLA) trained on large-scale human videos. Existing VLAs struggle with complex manipulation tasks requiring high dexterity and generalize poorly to novel scenarios and tasks, primarily due to their reliance on synthetic data with significant sim-to-real gaps or teleoperated demonstrations lacking scale and diversity. To address this data bottleneck, we propose leveraging human hands as a foundation manipulator, capitalizing on the rich dexterity and scalability present in web data. Our approach centers on physical instruction tuning, a novel training paradigm that combines large-scale VLA pretraining from human videos, physical space alignment for 3D reasoning, and post-training adaptation for robotic tasks. Additionally, we introduce a part-level motion tokenization method which achieves millimeter-level reconstruction accuracy to model precise hand trajectories for action learning. To support our proposed paradigm, we further develop a comprehensive data curation pipeline that integrates heterogeneous sources -- including motion capture, VR, and RGB-only videos -- into a large-scale dataset with millions of motion-based instructional instances. We empirically show the excellence of Being-H0 in hand motion generation and instruction following, and it also scales well with model and data sizes. Importantly, we observe the expected gains of Being-H0 in real-world robotic manipulation as physical instruction tuning is applied. More details are available at https://beingbeyond.github.io/Being-H0.

## 核心内容
We introduce Being-H0, a dexterous Vision-Language-Action model (VLA) trained on large-scale human videos. Existing VLAs struggle with complex manipulation tasks requiring high dexterity and generalize poorly to novel scenarios and tasks, primarily due to their reliance on synthetic data with significant sim-to-real gaps or teleoperated demonstrations lacking scale and diversity. To address this data bottleneck, we propose leveraging human hands as a foundation manipulator, capitalizing on the rich dexterity and scalability present in web data. Our approach centers on physical instruction tuning, a novel training paradigm that combines large-scale VLA pretraining from human videos, physical space alignment for 3D reasoning, and post-training adaptation for robotic tasks. Additionally, we introduce a part-level motion tokenization method which achieves millimeter-level reconstruction accuracy to model precise hand trajectories for action learning. To support our proposed paradigm, we further develop a comprehensive data curation pipeline that integrates heterogeneous sources -- including motion capture, VR, and RGB-only videos -- into a large-scale dataset with millions of motion-based instructional instances. We empirically show the excellence of Being-H0 in hand motion generation and instruction following, and it also scales well with model and data sizes. Importantly, we observe the expected gains of Being-H0 in real-world robotic manipulation as physical instruction tuning is applied. More details are available at https://beingbeyond.github.io/Being-H0.

## 参考
- http://arxiv.org/abs/2507.15597v1

## Overview
We introduce Being-H0, a dexterous Vision-Language-Action model (VLA) trained on large-scale human videos. Existing VLAs struggle with complex manipulation tasks requiring high dexterity and generalize poorly to novel scenarios and tasks, primarily due to their reliance on synthetic data with significant sim-to-real gaps or teleoperated demonstrations lacking scale and diversity. To address this data bottleneck, we propose leveraging human hands as a foundation manipulator, capitalizing on the rich dexterity and scalability present in web data. Our approach centers on physical instruction tuning, a novel training paradigm that combines large-scale VLA pretraining from human videos, physical space alignment for 3D reasoning, and post-training adaptation for robotic tasks. Additionally, we introduce a part-level motion tokenization method which achieves millimeter-level reconstruction accuracy to model precise hand trajectories for action learning. To support our proposed paradigm, we further develop a comprehensive data curation pipeline that integrates heterogeneous sources -- including motion capture, VR, and RGB-only videos -- into a large-scale dataset with millions of motion-based instructional instances. We empirically show the excellence of Being-H0 in hand motion generation and instruction following, and it also scales well with model and data sizes. Importantly, we observe the expected gains of Being-H0 in real-world robotic manipulation as physical instruction tuning is applied. More details are available at https://beingbeyond.github.io/Being-H0.

## Content
We introduce Being-H0, a dexterous Vision-Language-Action model (VLA) trained on large-scale human videos. Existing VLAs struggle with complex manipulation tasks requiring high dexterity and generalize poorly to novel scenarios and tasks, primarily due to their reliance on synthetic data with significant sim-to-real gaps or teleoperated demonstrations lacking scale and diversity. To address this data bottleneck, we propose leveraging human hands as a foundation manipulator, capitalizing on the rich dexterity and scalability present in web data. Our approach centers on physical instruction tuning, a novel training paradigm that combines large-scale VLA pretraining from human videos, physical space alignment for 3D reasoning, and post-training adaptation for robotic tasks. Additionally, we introduce a part-level motion tokenization method which achieves millimeter-level reconstruction accuracy to model precise hand trajectories for action learning. To support our proposed paradigm, we further develop a comprehensive data curation pipeline that integrates heterogeneous sources -- including motion capture, VR, and RGB-only videos -- into a large-scale dataset with millions of motion-based instructional instances. We empirically show the excellence of Being-H0 in hand motion generation and instruction following, and it also scales well with model and data sizes. Importantly, we observe the expected gains of Being-H0 in real-world robotic manipulation as physical instruction tuning is applied. More details are available at https://beingbeyond.github.io/Being-H0.

## 개요
우리는 대규모 인간 비디오로 훈련된 고도로 정밀한 Vision-Language-Action 모델(VLA)인 Being-H0를 소개합니다. 기존 VLA는 높은 손재주가 필요한 복잡한 조작 작업에 어려움을 겪고, 새로운 시나리오와 작업에 대한 일반화 성능이 낮습니다. 이는 주로 시뮬레이션과 실제 환경 간의 큰 차이가 있는 합성 데이터나 규모와 다양성이 부족한 원격 조작 시연에 의존하기 때문입니다. 이러한 데이터 병목 현상을 해결하기 위해, 우리는 인간의 손을 기반 조작기로 활용하여 웹 데이터에 존재하는 풍부한 손재주와 확장성을 활용할 것을 제안합니다. 우리의 접근 방식은 물리적 명령 튜닝(physical instruction tuning)이라는 새로운 훈련 패러다임에 중점을 둡니다. 이는 인간 비디오로부터의 대규모 VLA 사전 훈련, 3D 추론을 위한 물리적 공간 정렬, 로봇 작업을 위한 사후 훈련 적응을 결합합니다. 또한, 우리는 행동 학습을 위한 정밀한 손 궤적을 모델링하기 위해 밀리미터 수준의 재구성 정확도를 달성하는 부분 수준 동작 토큰화 방법(part-level motion tokenization method)을 소개합니다. 제안된 패러다임을 지원하기 위해, 우리는 모션 캡처, VR, RGB 전용 비디오를 포함한 이질적 소스를 통합하여 수백만 개의 동작 기반 명령 인스턴스로 구성된 대규모 데이터셋을 구축하는 포괄적인 데이터 큐레이션 파이프라인을 추가로 개발했습니다. 우리는 Being-H0가 손 동작 생성 및 명령 수행에서 뛰어난 성능을 보이며, 모델 및 데이터 크기에 따라 잘 확장됨을 실증적으로 보여줍니다. 중요하게도, 물리적 명령 튜닝이 적용됨에 따라 실제 로봇 조작에서 Being-H0의 기대된 성능 향상을 관찰했습니다. 자세한 내용은 https://beingbeyond.github.io/Being-H0에서 확인할 수 있습니다.

## 핵심 내용
우리는 대규모 인간 비디오로 훈련된 고도로 정밀한 Vision-Language-Action 모델(VLA)인 Being-H0를 소개합니다. 기존 VLA는 높은 손재주가 필요한 복잡한 조작 작업에 어려움을 겪고, 새로운 시나리오와 작업에 대한 일반화 성능이 낮습니다. 이는 주로 시뮬레이션과 실제 환경 간의 큰 차이가 있는 합성 데이터나 규모와 다양성이 부족한 원격 조작 시연에 의존하기 때문입니다. 이러한 데이터 병목 현상을 해결하기 위해, 우리는 인간의 손을 기반 조작기로 활용하여 웹 데이터에 존재하는 풍부한 손재주와 확장성을 활용할 것을 제안합니다. 우리의 접근 방식은 물리적 명령 튜닝(physical instruction tuning)이라는 새로운 훈련 패러다임에 중점을 둡니다. 이는 인간 비디오로부터의 대규모 VLA 사전 훈련, 3D 추론을 위한 물리적 공간 정렬, 로봇 작업을 위한 사후 훈련 적응을 결합합니다. 또한, 우리는 행동 학습을 위한 정밀한 손 궤적을 모델링하기 위해 밀리미터 수준의 재구성 정확도를 달성하는 부분 수준 동작 토큰화 방법(part-level motion tokenization method)을 소개합니다. 제안된 패러다임을 지원하기 위해, 우리는 모션 캡처, VR, RGB 전용 비디오를 포함한 이질적 소스를 통합하여 수백만 개의 동작 기반 명령 인스턴스로 구성된 대규모 데이터셋을 구축하는 포괄적인 데이터 큐레이션 파이프라인을 추가로 개발했습니다. 우리는 Being-H0가 손 동작 생성 및 명령 수행에서 뛰어난 성능을 보이며, 모델 및 데이터 크기에 따라 잘 확장됨을 실증적으로 보여줍니다. 중요하게도, 물리적 명령 튜닝이 적용됨에 따라 실제 로봇 조작에서 Being-H0의 기대된 성능 향상을 관찰했습니다. 자세한 내용은 https://beingbeyond.github.io/Being-H0에서 확인할 수 있습니다.

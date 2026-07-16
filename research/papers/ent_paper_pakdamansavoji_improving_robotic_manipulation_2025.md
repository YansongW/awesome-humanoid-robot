---
$id: ent_paper_pakdamansavoji_improving_robotic_manipulation_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Improving Robotic Manipulation Robustness via NICE Scene Surgery
  zh: NICE
  ko: Improving Robotic Manipulation Robustness via NICE Scene Surgery
summary:
  en: Improving Robotic Manipulation Robustness via NICE Scene Surgery (NICE), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Huawei Canada.
  zh: Improving Robotic Manipulation Robustness via NICE Scene Surgery (NICE), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Huawei Canada.
  ko: Improving Robotic Manipulation Robustness via NICE Scene Surgery (NICE), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Huawei Canada.
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
- nice
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.22777v1.
sources:
- id: src_001
  type: paper
  title: Improving Robotic Manipulation Robustness via NICE Scene Surgery (arXiv)
  url: https://arxiv.org/abs/2511.22777
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: NICE source
  url: https://doi.org/10.48550/arXiv.2511.22777
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Learning robust visuomotor policies for robotic manipulation remains a challenge in real-world settings, where visual distractors can significantly degrade performance and safety. In this work, we propose an effective and scalable framework, Naturalistic Inpainting for Context Enhancement (NICE). Our method minimizes out-of-distribution (OOD) gap in imitation learning by increasing visual diversity through construction of new experiences using existing demonstrations. By utilizing image generative frameworks and large language models, NICE performs three editing operations, object replacement, restyling, and removal of distracting (non-target) objects. These changes preserve spatial relationships without obstructing target objects and maintain action-label consistency. Unlike previous approaches, NICE requires no additional robot data collection, simulator access, or custom model training, making it readily applicable to existing robotic datasets.   Using real-world scenes, we showcase the capability of our framework in producing photo-realistic scene enhancement. For downstream tasks, we use NICE data to finetune a vision-language model (VLM) for spatial affordance prediction and a vision-language-action (VLA) policy for object manipulation. Our evaluations show that NICE successfully minimizes OOD gaps, resulting in over 20% improvement in accuracy for affordance prediction in highly cluttered scenes. For manipulation tasks, success rate increases on average by 11% when testing in environments populated with distractors in different quantities. Furthermore, we show that our method improves visual robustness, lowering target confusion by 6%, and enhances safety by reducing collision rate by 7%.

## 核心内容
Learning robust visuomotor policies for robotic manipulation remains a challenge in real-world settings, where visual distractors can significantly degrade performance and safety. In this work, we propose an effective and scalable framework, Naturalistic Inpainting for Context Enhancement (NICE). Our method minimizes out-of-distribution (OOD) gap in imitation learning by increasing visual diversity through construction of new experiences using existing demonstrations. By utilizing image generative frameworks and large language models, NICE performs three editing operations, object replacement, restyling, and removal of distracting (non-target) objects. These changes preserve spatial relationships without obstructing target objects and maintain action-label consistency. Unlike previous approaches, NICE requires no additional robot data collection, simulator access, or custom model training, making it readily applicable to existing robotic datasets.   Using real-world scenes, we showcase the capability of our framework in producing photo-realistic scene enhancement. For downstream tasks, we use NICE data to finetune a vision-language model (VLM) for spatial affordance prediction and a vision-language-action (VLA) policy for object manipulation. Our evaluations show that NICE successfully minimizes OOD gaps, resulting in over 20% improvement in accuracy for affordance prediction in highly cluttered scenes. For manipulation tasks, success rate increases on average by 11% when testing in environments populated with distractors in different quantities. Furthermore, we show that our method improves visual robustness, lowering target confusion by 6%, and enhances safety by reducing collision rate by 7%.

## 参考
- http://arxiv.org/abs/2511.22777v1

## Overview
Learning robust visuomotor policies for robotic manipulation remains a challenge in real-world settings, where visual distractors can significantly degrade performance and safety. In this work, we propose an effective and scalable framework, Naturalistic Inpainting for Context Enhancement (NICE). Our method minimizes out-of-distribution (OOD) gap in imitation learning by increasing visual diversity through construction of new experiences using existing demonstrations. By utilizing image generative frameworks and large language models, NICE performs three editing operations, object replacement, restyling, and removal of distracting (non-target) objects. These changes preserve spatial relationships without obstructing target objects and maintain action-label consistency. Unlike previous approaches, NICE requires no additional robot data collection, simulator access, or custom model training, making it readily applicable to existing robotic datasets. Using real-world scenes, we showcase the capability of our framework in producing photo-realistic scene enhancement. For downstream tasks, we use NICE data to finetune a vision-language model (VLM) for spatial affordance prediction and a vision-language-action (VLA) policy for object manipulation. Our evaluations show that NICE successfully minimizes OOD gaps, resulting in over 20% improvement in accuracy for affordance prediction in highly cluttered scenes. For manipulation tasks, success rate increases on average by 11% when testing in environments populated with distractors in different quantities. Furthermore, we show that our method improves visual robustness, lowering target confusion by 6%, and enhances safety by reducing collision rate by 7%.

## Content
Learning robust visuomotor policies for robotic manipulation remains a challenge in real-world settings, where visual distractors can significantly degrade performance and safety. In this work, we propose an effective and scalable framework, Naturalistic Inpainting for Context Enhancement (NICE). Our method minimizes out-of-distribution (OOD) gap in imitation learning by increasing visual diversity through construction of new experiences using existing demonstrations. By utilizing image generative frameworks and large language models, NICE performs three editing operations, object replacement, restyling, and removal of distracting (non-target) objects. These changes preserve spatial relationships without obstructing target objects and maintain action-label consistency. Unlike previous approaches, NICE requires no additional robot data collection, simulator access, or custom model training, making it readily applicable to existing robotic datasets. Using real-world scenes, we showcase the capability of our framework in producing photo-realistic scene enhancement. For downstream tasks, we use NICE data to finetune a vision-language model (VLM) for spatial affordance prediction and a vision-language-action (VLA) policy for object manipulation. Our evaluations show that NICE successfully minimizes OOD gaps, resulting in over 20% improvement in accuracy for affordance prediction in highly cluttered scenes. For manipulation tasks, success rate increases on average by 11% when testing in environments populated with distractors in different quantities. Furthermore, we show that our method improves visual robustness, lowering target confusion by 6%, and enhances safety by reducing collision rate by 7%.

## 개요
로봇 조작을 위한 강건한 시각-운동 정책을 학습하는 것은 실제 환경에서 여전히 어려운 과제로, 시각적 방해 요소가 성능과 안전성을 크게 저하시킬 수 있습니다. 본 연구에서는 효과적이고 확장 가능한 프레임워크인 NICE(Naturalistic Inpainting for Context Enhancement)를 제안합니다. 우리의 방법은 기존 시연 데이터를 활용하여 새로운 경험을 구성함으로써 시각적 다양성을 증가시켜 모방 학습에서의 분포 외(OOD) 격차를 최소화합니다. 이미지 생성 프레임워크와 대규모 언어 모델을 활용하여 NICE는 객체 교체, 스타일 변경, 방해(비대상) 객체 제거라는 세 가지 편집 작업을 수행합니다. 이러한 변경은 공간 관계를 유지하고 대상 객체를 방해하지 않으며 행동 레이블 일관성을 유지합니다. 이전 접근 방식과 달리 NICE는 추가 로봇 데이터 수집, 시뮬레이터 접근 또는 맞춤형 모델 학습이 필요하지 않아 기존 로봇 데이터셋에 쉽게 적용할 수 있습니다. 실제 장면을 사용하여 우리의 프레임워크가 사실적인 장면 향상을 생성하는 능력을 입증합니다. 다운스트림 작업을 위해 NICE 데이터를 사용하여 공간 어포던스 예측을 위한 시각-언어 모델(VLM)과 객체 조작을 위한 시각-언어-행동(VLA) 정책을 미세 조정합니다. 평가 결과, NICE가 OOD 격차를 성공적으로 최소화하여 복잡한 장면에서 어포던스 예측 정확도가 20% 이상 향상되었습니다. 조작 작업의 경우, 다양한 양의 방해 요소가 있는 환경에서 테스트했을 때 성공률이 평균 11% 증가했습니다. 또한, 우리의 방법이 시각적 강건성을 개선하여 대상 혼동을 6% 낮추고 충돌률을 7% 감소시켜 안전성을 향상시킴을 보여줍니다.

## 핵심 내용
로봇 조작을 위한 강건한 시각-운동 정책을 학습하는 것은 실제 환경에서 여전히 어려운 과제로, 시각적 방해 요소가 성능과 안전성을 크게 저하시킬 수 있습니다. 본 연구에서는 효과적이고 확장 가능한 프레임워크인 NICE(Naturalistic Inpainting for Context Enhancement)를 제안합니다. 우리의 방법은 기존 시연 데이터를 활용하여 새로운 경험을 구성함으로써 시각적 다양성을 증가시켜 모방 학습에서의 분포 외(OOD) 격차를 최소화합니다. 이미지 생성 프레임워크와 대규모 언어 모델을 활용하여 NICE는 객체 교체, 스타일 변경, 방해(비대상) 객체 제거라는 세 가지 편집 작업을 수행합니다. 이러한 변경은 공간 관계를 유지하고 대상 객체를 방해하지 않으며 행동 레이블 일관성을 유지합니다. 이전 접근 방식과 달리 NICE는 추가 로봇 데이터 수집, 시뮬레이터 접근 또는 맞춤형 모델 학습이 필요하지 않아 기존 로봇 데이터셋에 쉽게 적용할 수 있습니다. 실제 장면을 사용하여 우리의 프레임워크가 사실적인 장면 향상을 생성하는 능력을 입증합니다. 다운스트림 작업을 위해 NICE 데이터를 사용하여 공간 어포던스 예측을 위한 시각-언어 모델(VLM)과 객체 조작을 위한 시각-언어-행동(VLA) 정책을 미세 조정합니다. 평가 결과, NICE가 OOD 격차를 성공적으로 최소화하여 복잡한 장면에서 어포던스 예측 정확도가 20% 이상 향상되었습니다. 조작 작업의 경우, 다양한 양의 방해 요소가 있는 환경에서 테스트했을 때 성공률이 평균 11% 증가했습니다. 또한, 우리의 방법이 시각적 강건성을 개선하여 대상 혼동을 6% 낮추고 충돌률을 7% 감소시켜 안전성을 향상시킴을 보여줍니다.

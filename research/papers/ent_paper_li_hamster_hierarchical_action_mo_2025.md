---
$id: ent_paper_li_hamster_hierarchical_action_mo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HAMSTER: Hierarchical Action Models For Open-World Robot Manipulation'
  zh: HAMSTER
  ko: 'HAMSTER: Hierarchical Action Models For Open-World Robot Manipulation'
summary:
  en: 'HAMSTER: Hierarchical Action Models For Open-World Robot Manipulation (HAMSTER), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by MIT CSAIL, Nvidia, and published at ICLR25.'
  zh: 'HAMSTER: Hierarchical Action Models For Open-World Robot Manipulation (HAMSTER), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by MIT CSAIL, Nvidia, and published at ICLR25.'
  ko: 'HAMSTER: Hierarchical Action Models For Open-World Robot Manipulation (HAMSTER), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by MIT CSAIL, Nvidia, and published at ICLR25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hamster
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.05485v4.
sources:
- id: src_001
  type: paper
  title: HAMSTER source
  url: https://openreview.net/forum?id=h7aQxzKbq6
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Large foundation models have shown strong open-world generalization to complex problems in vision and language, but similar levels of generalization have yet to be achieved in robotics. One fundamental challenge is the lack of robotic data, which are typically obtained through expensive on-robot operation. A promising remedy is to leverage cheaper, off-domain data such as action-free videos, hand-drawn sketches or simulation data. In this work, we posit that hierarchical vision-language-action (VLA) models can be more effective in utilizing off-domain data than standard monolithic VLA models that directly finetune vision-language models (VLMs) to predict actions. In particular, we study a class of hierarchical VLA models, where the high-level VLM is finetuned to produce a coarse 2D path indicating the desired robot end-effector trajectory given an RGB image and a task description. The intermediate 2D path prediction is then served as guidance to the low-level, 3D-aware control policy capable of precise manipulation. Doing so alleviates the high-level VLM from fine-grained action prediction, while reducing the low-level policy's burden on complex task-level reasoning. We show that, with the hierarchical design, the high-level VLM can transfer across significant domain gaps between the off-domain finetuning data and real-robot testing scenarios, including differences on embodiments, dynamics, visual appearances and task semantics, etc. In the real-robot experiments, we observe an average of 20% improvement in success rate across seven different axes of generalization over OpenVLA, representing a 50% relative gain. Visual results, code, and dataset are provided at: https://hamster-robot.github.io/

## 核心内容
Large foundation models have shown strong open-world generalization to complex problems in vision and language, but similar levels of generalization have yet to be achieved in robotics. One fundamental challenge is the lack of robotic data, which are typically obtained through expensive on-robot operation. A promising remedy is to leverage cheaper, off-domain data such as action-free videos, hand-drawn sketches or simulation data. In this work, we posit that hierarchical vision-language-action (VLA) models can be more effective in utilizing off-domain data than standard monolithic VLA models that directly finetune vision-language models (VLMs) to predict actions. In particular, we study a class of hierarchical VLA models, where the high-level VLM is finetuned to produce a coarse 2D path indicating the desired robot end-effector trajectory given an RGB image and a task description. The intermediate 2D path prediction is then served as guidance to the low-level, 3D-aware control policy capable of precise manipulation. Doing so alleviates the high-level VLM from fine-grained action prediction, while reducing the low-level policy's burden on complex task-level reasoning. We show that, with the hierarchical design, the high-level VLM can transfer across significant domain gaps between the off-domain finetuning data and real-robot testing scenarios, including differences on embodiments, dynamics, visual appearances and task semantics, etc. In the real-robot experiments, we observe an average of 20% improvement in success rate across seven different axes of generalization over OpenVLA, representing a 50% relative gain. Visual results, code, and dataset are provided at: https://hamster-robot.github.io/

## 参考
- http://arxiv.org/abs/2502.05485v4

## Overview
Large foundation models have shown strong open-world generalization to complex problems in vision and language, but similar levels of generalization have yet to be achieved in robotics. One fundamental challenge is the lack of robotic data, which are typically obtained through expensive on-robot operation. A promising remedy is to leverage cheaper, off-domain data such as action-free videos, hand-drawn sketches or simulation data. In this work, we posit that hierarchical vision-language-action (VLA) models can be more effective in utilizing off-domain data than standard monolithic VLA models that directly finetune vision-language models (VLMs) to predict actions. In particular, we study a class of hierarchical VLA models, where the high-level VLM is finetuned to produce a coarse 2D path indicating the desired robot end-effector trajectory given an RGB image and a task description. The intermediate 2D path prediction is then served as guidance to the low-level, 3D-aware control policy capable of precise manipulation. Doing so alleviates the high-level VLM from fine-grained action prediction, while reducing the low-level policy's burden on complex task-level reasoning. We show that, with the hierarchical design, the high-level VLM can transfer across significant domain gaps between the off-domain finetuning data and real-robot testing scenarios, including differences on embodiments, dynamics, visual appearances and task semantics, etc. In the real-robot experiments, we observe an average of 20% improvement in success rate across seven different axes of generalization over OpenVLA, representing a 50% relative gain. Visual results, code, and dataset are provided at: https://hamster-robot.github.io/

## Content
Large foundation models have shown strong open-world generalization to complex problems in vision and language, but similar levels of generalization have yet to be achieved in robotics. One fundamental challenge is the lack of robotic data, which are typically obtained through expensive on-robot operation. A promising remedy is to leverage cheaper, off-domain data such as action-free videos, hand-drawn sketches or simulation data. In this work, we posit that hierarchical vision-language-action (VLA) models can be more effective in utilizing off-domain data than standard monolithic VLA models that directly finetune vision-language models (VLMs) to predict actions. In particular, we study a class of hierarchical VLA models, where the high-level VLM is finetuned to produce a coarse 2D path indicating the desired robot end-effector trajectory given an RGB image and a task description. The intermediate 2D path prediction is then served as guidance to the low-level, 3D-aware control policy capable of precise manipulation. Doing so alleviates the high-level VLM from fine-grained action prediction, while reducing the low-level policy's burden on complex task-level reasoning. We show that, with the hierarchical design, the high-level VLM can transfer across significant domain gaps between the off-domain finetuning data and real-robot testing scenarios, including differences on embodiments, dynamics, visual appearances and task semantics, etc. In the real-robot experiments, we observe an average of 20% improvement in success rate across seven different axes of generalization over OpenVLA, representing a 50% relative gain. Visual results, code, and dataset are provided at: https://hamster-robot.github.io/

## 개요
대규모 기반 모델은 시각 및 언어 분야의 복잡한 문제에 대해 강력한 개방형 일반화 능력을 보여주었지만, 로봇 공학에서는 아직 유사한 수준의 일반화가 달성되지 못했습니다. 근본적인 과제 중 하나는 일반적으로 고가의 로봇 직접 조작을 통해 얻어지는 로봇 데이터의 부족입니다. 유망한 해결책은 동작이 없는 비디오, 손으로 그린 스케치 또는 시뮬레이션 데이터와 같은 저렴한 도메인 외 데이터를 활용하는 것입니다. 본 연구에서는 계층적 시각-언어-행동(VLA) 모델이 행동을 예측하기 위해 시각-언어 모델(VLM)을 직접 미세 조정하는 표준 모놀리식 VLA 모델보다 도메인 외 데이터를 활용하는 데 더 효과적일 수 있다고 가정합니다. 특히, 우리는 고수준 VLM이 RGB 이미지와 작업 설명이 주어졌을 때 원하는 로봇 엔드 이펙터 궤적을 나타내는 대략적인 2D 경로를 생성하도록 미세 조정되는 계층적 VLA 모델 클래스를 연구합니다. 중간 2D 경로 예측은 정밀한 조작이 가능한 저수준의 3D 인식 제어 정책에 대한 지침으로 사용됩니다. 이를 통해 고수준 VLM은 세분화된 행동 예측 부담을 덜고, 저수준 정책은 복잡한 작업 수준 추론 부담을 줄일 수 있습니다. 우리는 계층적 설계를 통해 고수준 VLM이 도메인 외 미세 조정 데이터와 실제 로봇 테스트 시나리오 간의 상당한 도메인 격차(구현체, 동역학, 시각적 외관, 작업 의미론 등의 차이 포함)를 넘어 전이할 수 있음을 보여줍니다. 실제 로봇 실험에서 우리는 OpenVLA 대비 7가지 일반화 축에서 평균 20%의 성공률 향상(상대적 50% 증가)을 관찰했습니다. 시각적 결과, 코드 및 데이터셋은 다음에서 제공됩니다: https://hamster-robot.github.io/

## 핵심 내용
대규모 기반 모델은 시각 및 언어 분야의 복잡한 문제에 대해 강력한 개방형 일반화 능력을 보여주었지만, 로봇 공학에서는 아직 유사한 수준의 일반화가 달성되지 못했습니다. 근본적인 과제 중 하나는 일반적으로 고가의 로봇 직접 조작을 통해 얻어지는 로봇 데이터의 부족입니다. 유망한 해결책은 동작이 없는 비디오, 손으로 그린 스케치 또는 시뮬레이션 데이터와 같은 저렴한 도메인 외 데이터를 활용하는 것입니다. 본 연구에서는 계층적 시각-언어-행동(VLA) 모델이 행동을 예측하기 위해 시각-언어 모델(VLM)을 직접 미세 조정하는 표준 모놀리식 VLA 모델보다 도메인 외 데이터를 활용하는 데 더 효과적일 수 있다고 가정합니다. 특히, 우리는 고수준 VLM이 RGB 이미지와 작업 설명이 주어졌을 때 원하는 로봇 엔드 이펙터 궤적을 나타내는 대략적인 2D 경로를 생성하도록 미세 조정되는 계층적 VLA 모델 클래스를 연구합니다. 중간 2D 경로 예측은 정밀한 조작이 가능한 저수준의 3D 인식 제어 정책에 대한 지침으로 사용됩니다. 이를 통해 고수준 VLM은 세분화된 행동 예측 부담을 덜고, 저수준 정책은 복잡한 작업 수준 추론 부담을 줄일 수 있습니다. 우리는 계층적 설계를 통해 고수준 VLM이 도메인 외 미세 조정 데이터와 실제 로봇 테스트 시나리오 간의 상당한 도메인 격차(구현체, 동역학, 시각적 외관, 작업 의미론 등의 차이 포함)를 넘어 전이할 수 있음을 보여줍니다. 실제 로봇 실험에서 우리는 OpenVLA 대비 7가지 일반화 축에서 평균 20%의 성공률 향상(상대적 50% 증가)을 관찰했습니다. 시각적 결과, 코드 및 데이터셋은 다음에서 제공됩니다: https://hamster-robot.github.io/

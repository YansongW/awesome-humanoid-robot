---
$id: ent_paper_spiridonov_generalist_robot_manipulation_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Generalist Robot Manipulation beyond Action Labeled Data
  zh: MotoVLA
  ko: Generalist Robot Manipulation beyond Action Labeled Data
summary:
  en: Generalist Robot Manipulation beyond Action Labeled Data (MotoVLA), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by INSAIT, Sofia University “St. Kliment Ohridski”, ETH Zurich, and published at CoRL25.
  zh: Generalist Robot Manipulation beyond Action Labeled Data (MotoVLA), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by INSAIT, Sofia University “St. Kliment Ohridski”, ETH Zurich, and published at CoRL25.
  ko: Generalist Robot Manipulation beyond Action Labeled Data (MotoVLA), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by INSAIT, Sofia University “St. Kliment Ohridski”, ETH Zurich, and published at CoRL25.
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
- motovla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.19958v1.
sources:
- id: src_001
  type: paper
  title: Generalist Robot Manipulation beyond Action Labeled Data (arXiv)
  url: https://arxiv.org/abs/2509.19958
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MotoVLA source
  url: https://doi.org/10.48550/arXiv.2509.19958
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent advances in generalist robot manipulation leverage pre-trained Vision-Language Models (VLMs) and large-scale robot demonstrations to tackle diverse tasks in a zero-shot manner. A key challenge remains: scaling high-quality, action-labeled robot demonstration data, which existing methods rely on for robustness and generalization. To address this, we propose a method that benefits from videos without action labels - featuring humans and/or robots in action - enhancing open-vocabulary performance and enabling data-efficient learning of new tasks. Our method extracts dense, dynamic 3D point clouds at the hand or gripper location and uses a proposed 3D dynamics predictor for self-supervision. This predictor is then tuned to an action predictor using a smaller labeled dataset for action alignment. We show that our method not only learns from unlabeled human and robot demonstrations - improving downstream generalist robot policies - but also enables robots to learn new tasks without action labels (i.e., out-of-action generalization) in both real-world and simulated settings.

## 核心内容
Recent advances in generalist robot manipulation leverage pre-trained Vision-Language Models (VLMs) and large-scale robot demonstrations to tackle diverse tasks in a zero-shot manner. A key challenge remains: scaling high-quality, action-labeled robot demonstration data, which existing methods rely on for robustness and generalization. To address this, we propose a method that benefits from videos without action labels - featuring humans and/or robots in action - enhancing open-vocabulary performance and enabling data-efficient learning of new tasks. Our method extracts dense, dynamic 3D point clouds at the hand or gripper location and uses a proposed 3D dynamics predictor for self-supervision. This predictor is then tuned to an action predictor using a smaller labeled dataset for action alignment. We show that our method not only learns from unlabeled human and robot demonstrations - improving downstream generalist robot policies - but also enables robots to learn new tasks without action labels (i.e., out-of-action generalization) in both real-world and simulated settings.

## 参考
- http://arxiv.org/abs/2509.19958v1

## Overview
Recent advances in generalist robot manipulation leverage pre-trained Vision-Language Models (VLMs) and large-scale robot demonstrations to tackle diverse tasks in a zero-shot manner. A key challenge remains: scaling high-quality, action-labeled robot demonstration data, which existing methods rely on for robustness and generalization. To address this, we propose a method that benefits from videos without action labels - featuring humans and/or robots in action - enhancing open-vocabulary performance and enabling data-efficient learning of new tasks. Our method extracts dense, dynamic 3D point clouds at the hand or gripper location and uses a proposed 3D dynamics predictor for self-supervision. This predictor is then tuned to an action predictor using a smaller labeled dataset for action alignment. We show that our method not only learns from unlabeled human and robot demonstrations - improving downstream generalist robot policies - but also enables robots to learn new tasks without action labels (i.e., out-of-action generalization) in both real-world and simulated settings.

## Content
Recent advances in generalist robot manipulation leverage pre-trained Vision-Language Models (VLMs) and large-scale robot demonstrations to tackle diverse tasks in a zero-shot manner. A key challenge remains: scaling high-quality, action-labeled robot demonstration data, which existing methods rely on for robustness and generalization. To address this, we propose a method that benefits from videos without action labels - featuring humans and/or robots in action - enhancing open-vocabulary performance and enabling data-efficient learning of new tasks. Our method extracts dense, dynamic 3D point clouds at the hand or gripper location and uses a proposed 3D dynamics predictor for self-supervision. This predictor is then tuned to an action predictor using a smaller labeled dataset for action alignment. We show that our method not only learns from unlabeled human and robot demonstrations - improving downstream generalist robot policies - but also enables robots to learn new tasks without action labels (i.e., out-of-action generalization) in both real-world and simulated settings.

## 개요
최근 범용 로봇 조작 기술의 발전은 사전 학습된 시각-언어 모델(VLM)과 대규모 로봇 시연 데이터를 활용하여 다양한 작업을 제로샷 방식으로 처리합니다. 여전히 중요한 과제는 기존 방법이 강건성과 일반화를 위해 의존하는 고품질의 행동 레이블이 있는 로봇 시연 데이터를 확장하는 것입니다. 이를 해결하기 위해, 우리는 행동 레이블이 없는 비디오(인간 및/또는 로봇의 행동 포함)를 활용하여 개방형 어휘 성능을 향상시키고 새로운 작업의 데이터 효율적 학습을 가능하게 하는 방법을 제안합니다. 우리의 방법은 손 또는 그리퍼 위치에서 밀집된 동적 3D 포인트 클라우드를 추출하고, 제안된 3D 역학 예측기를 사용하여 자기 지도 학습을 수행합니다. 그런 다음 이 예측기는 더 작은 레이블 데이터셋을 사용하여 행동 정렬을 위한 행동 예측기로 미세 조정됩니다. 우리는 이 방법이 레이블이 없는 인간 및 로봇 시연 데이터를 학습하여 하위 범용 로봇 정책을 개선할 뿐만 아니라, 실제 환경과 시뮬레이션 환경 모두에서 행동 레이블 없이 새로운 작업을 학습(즉, 행동 외 일반화)할 수 있음을 보여줍니다.

## 핵심 내용
최근 범용 로봇 조작 기술의 발전은 사전 학습된 시각-언어 모델(VLM)과 대규모 로봇 시연 데이터를 활용하여 다양한 작업을 제로샷 방식으로 처리합니다. 여전히 중요한 과제는 기존 방법이 강건성과 일반화를 위해 의존하는 고품질의 행동 레이블이 있는 로봇 시연 데이터를 확장하는 것입니다. 이를 해결하기 위해, 우리는 행동 레이블이 없는 비디오(인간 및/또는 로봇의 행동 포함)를 활용하여 개방형 어휘 성능을 향상시키고 새로운 작업의 데이터 효율적 학습을 가능하게 하는 방법을 제안합니다. 우리의 방법은 손 또는 그리퍼 위치에서 밀집된 동적 3D 포인트 클라우드를 추출하고, 제안된 3D 역학 예측기를 사용하여 자기 지도 학습을 수행합니다. 그런 다음 이 예측기는 더 작은 레이블 데이터셋을 사용하여 행동 정렬을 위한 행동 예측기로 미세 조정됩니다. 우리는 이 방법이 레이블이 없는 인간 및 로봇 시연 데이터를 학습하여 하위 범용 로봇 정책을 개선할 뿐만 아니라, 실제 환경과 시뮬레이션 환경 모두에서 행동 레이블 없이 새로운 작업을 학습(즉, 행동 외 일반화)할 수 있음을 보여줍니다.

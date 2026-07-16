---
$id: ent_paper_shortcut_trajectory_planning_f_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Shortcut Trajectory Planning for Efficient Offline Reinforcement Learning
  zh: Shortcut Trajectory Planning for Efficient Offline Reinforcement Learning
  ko: Shortcut Trajectory Planning for Efficient Offline Reinforcement Learning
summary:
  en: 'arXiv:2607.09336v1 Announce Type: cross Abstract: Diffusion-based trajectory planners have shown strong performance
    in offline reinforcement learning, but their iterative denoising process often incurs high inference cost. Consistency-based
    planners reduce the number of sampling steps, yet they typically rely on a two-stage teacher--student distillation pipeline
    that increases training cost and may introduce instability. We propose Shortcut Trajectory Planning (STP), an offline
    model-based reinforcement learning framework that incorporates shortcut models as efficient trajectory generators. STP
    trains a conditional shortcut trajectory model in a single stage, supports adjustable one-step and few-step inference
    through step-size conditioning, and selects candidate plans using a critic augmented with feasibility-aware correction.
    Across standard D4RL benchmarks, including locomotion, navigation, manipulation, and dexterous control tasks, STP achieves
    strong performance while simplifying the training pipeline for fast generative planning.'
  zh: 'arXiv:2607.09336v1 Announce Type: cross Abstract: Diffusion-based trajectory planners have shown strong performance
    in offline reinforcement learning, but their iterative denoising process often incurs high inference cost. Consistency-based
    planners reduce the number of sampling steps, yet they typically rely on a two-stage teacher--student distillation pipeline
    that increases training cost and may introduce instability. We propose Shortcut Trajectory Planning (STP), an offline
    model-based reinforcement learning framework that incorporates shortcut models as efficient trajectory generators. STP
    trains a conditional shortcut trajectory model in a single stage, supports adjustable one-step and few-step inference
    through step-size conditioning, and selects candidate plans using a critic augmented with feasibility-aware correction.
    Across standard D4RL benchmarks, including locomotion, navigation, manipulation, and dexterous control tasks, STP achieves
    strong performance while simplifying the training pipeline for fast generative planning.'
  ko: 'arXiv:2607.09336v1 Announce Type: cross Abstract: Diffusion-based trajectory planners have shown strong performance
    in offline reinforcement learning, but their iterative denoising process often incurs high inference cost. Consistency-based
    planners reduce the number of sampling steps, yet they typically rely on a two-stage teacher--student distillation pipeline
    that increases training cost and may introduce instability. We propose Shortcut Trajectory Planning (STP), an offline
    model-based reinforcement learning framework that incorporates shortcut models as efficient trajectory generators. STP
    trains a conditional shortcut trajectory model in a single stage, supports adjustable one-step and few-step inference
    through step-size conditioning, and selects candidate plans using a critic augmented with feasibility-aware correction.
    Across standard D4RL benchmarks, including locomotion, navigation, manipulation, and dexterous control tasks, STP achieves
    strong performance while simplifying the training pipeline for fast generative planning.'
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
- shortcut_trajectory_planning_f
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09336v1.
sources:
- id: src_001
  type: paper
  title: Shortcut Trajectory Planning for Efficient Offline Reinforcement Learning (arXiv)
  url: https://arxiv.org/abs/2607.09336
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
Diffusion-based trajectory planners have shown strong performance in offline reinforcement learning, but their iterative denoising process often incurs high inference cost. Consistency-based planners reduce the number of sampling steps, yet they typically rely on a two-stage teacher--student distillation pipeline that increases training cost and may introduce instability. We propose Shortcut Trajectory Planning (STP), an offline model-based reinforcement learning framework that incorporates shortcut models as efficient trajectory generators. STP trains a conditional shortcut trajectory model in a single stage, supports adjustable one-step and few-step inference through step-size conditioning, and selects candidate plans using a critic augmented with feasibility-aware correction. Across standard D4RL benchmarks, including locomotion, navigation, manipulation, and dexterous control tasks, STP achieves strong performance while simplifying the training pipeline for fast generative planning.

## 核心内容
Diffusion-based trajectory planners have shown strong performance in offline reinforcement learning, but their iterative denoising process often incurs high inference cost. Consistency-based planners reduce the number of sampling steps, yet they typically rely on a two-stage teacher--student distillation pipeline that increases training cost and may introduce instability. We propose Shortcut Trajectory Planning (STP), an offline model-based reinforcement learning framework that incorporates shortcut models as efficient trajectory generators. STP trains a conditional shortcut trajectory model in a single stage, supports adjustable one-step and few-step inference through step-size conditioning, and selects candidate plans using a critic augmented with feasibility-aware correction. Across standard D4RL benchmarks, including locomotion, navigation, manipulation, and dexterous control tasks, STP achieves strong performance while simplifying the training pipeline for fast generative planning.

## 参考
- http://arxiv.org/abs/2607.09336v1

## Overview
Diffusion-based trajectory planners have shown strong performance in offline reinforcement learning, but their iterative denoising process often incurs high inference cost. Consistency-based planners reduce the number of sampling steps, yet they typically rely on a two-stage teacher--student distillation pipeline that increases training cost and may introduce instability. We propose Shortcut Trajectory Planning (STP), an offline model-based reinforcement learning framework that incorporates shortcut models as efficient trajectory generators. STP trains a conditional shortcut trajectory model in a single stage, supports adjustable one-step and few-step inference through step-size conditioning, and selects candidate plans using a critic augmented with feasibility-aware correction. Across standard D4RL benchmarks, including locomotion, navigation, manipulation, and dexterous control tasks, STP achieves strong performance while simplifying the training pipeline for fast generative planning.

## Content
Diffusion-based trajectory planners have shown strong performance in offline reinforcement learning, but their iterative denoising process often incurs high inference cost. Consistency-based planners reduce the number of sampling steps, yet they typically rely on a two-stage teacher--student distillation pipeline that increases training cost and may introduce instability. We propose Shortcut Trajectory Planning (STP), an offline model-based reinforcement learning framework that incorporates shortcut models as efficient trajectory generators. STP trains a conditional shortcut trajectory model in a single stage, supports adjustable one-step and few-step inference through step-size conditioning, and selects candidate plans using a critic augmented with feasibility-aware correction. Across standard D4RL benchmarks, including locomotion, navigation, manipulation, and dexterous control tasks, STP achieves strong performance while simplifying the training pipeline for fast generative planning.

## 개요
확산 기반 궤적 계획기는 오프라인 강화 학습에서 뛰어난 성능을 보여주었지만, 반복적인 잡음 제거 과정으로 인해 추론 비용이 높은 경우가 많습니다. 일관성 기반 계획기는 샘플링 단계 수를 줄이지만, 일반적으로 훈련 비용을 증가시키고 불안정성을 초래할 수 있는 2단계 교사-학생 증류 파이프라인에 의존합니다. 본 논문에서는 효율적인 궤적 생성기로서 단축 모델을 통합하는 오프라인 모델 기반 강화 학습 프레임워크인 단축 궤적 계획(STP)을 제안합니다. STP는 단일 단계로 조건부 단축 궤적 모델을 훈련하고, 단계 크기 조건화를 통해 조정 가능한 1단계 및 소수 단계 추론을 지원하며, 실현 가능성 인식 보정이 추가된 비평가를 사용하여 후보 계획을 선택합니다. 보행, 항법, 조작 및 정밀 제어 작업을 포함한 표준 D4RL 벤치마크에서 STP는 빠른 생성 계획을 위한 훈련 파이프라인을 단순화하면서 강력한 성능을 달성합니다.

## 핵심 내용
확산 기반 궤적 계획기는 오프라인 강화 학습에서 뛰어난 성능을 보여주었지만, 반복적인 잡음 제거 과정으로 인해 추론 비용이 높은 경우가 많습니다. 일관성 기반 계획기는 샘플링 단계 수를 줄이지만, 일반적으로 훈련 비용을 증가시키고 불안정성을 초래할 수 있는 2단계 교사-학생 증류 파이프라인에 의존합니다. 본 논문에서는 효율적인 궤적 생성기로서 단축 모델을 통합하는 오프라인 모델 기반 강화 학습 프레임워크인 단축 궤적 계획(STP)을 제안합니다. STP는 단일 단계로 조건부 단축 궤적 모델을 훈련하고, 단계 크기 조건화를 통해 조정 가능한 1단계 및 소수 단계 추론을 지원하며, 실현 가능성 인식 보정이 추가된 비평가를 사용하여 후보 계획을 선택합니다. 보행, 항법, 조작 및 정밀 제어 작업을 포함한 표준 D4RL 벤치마크에서 STP는 빠른 생성 계획을 위한 훈련 파이프라인을 단순화하면서 강력한 성능을 달성합니다.

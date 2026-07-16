---
$id: ent_paper_pdf_hr_pose_distance_fields_fo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PDF-HR: Pose Distance Fields for Humanoid Robots'
  zh: 'PDF-HR: Pose Distance Fields for Humanoid Robots'
  ko: 'PDF-HR: Pose Distance Fields for Humanoid Robots'
summary:
  en: 'PDF-HR: Pose Distance Fields for Humanoid Robots is a 2026 work on loco-manipulation and whole-body-control for humanoid
    robots.'
  zh: 'PDF-HR: Pose Distance Fields for Humanoid Robots is a 2026 work on loco-manipulation and whole-body-control for humanoid
    robots.'
  ko: 'PDF-HR: Pose Distance Fields for Humanoid Robots is a 2026 work on loco-manipulation and whole-body-control for humanoid
    robots.'
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
- loco_manipulation
- pdf_hr
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.04851v1.
sources:
- id: src_001
  type: paper
  title: 'PDF-HR: Pose Distance Fields for Humanoid Robots (arXiv)'
  url: https://arxiv.org/abs/2602.04851
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Pose and motion priors play a crucial role in humanoid robotics. Although such priors have been widely studied in human motion recovery (HMR) domain with a range of models, their adoption for humanoid robots remains limited, largely due to the scarcity of high-quality humanoid motion data. In this work, we introduce Pose Distance Fields for Humanoid Robots (PDF-HR), a lightweight prior that represents the robot pose distribution as a continuous and differentiable manifold. Given an arbitrary pose, PDF-HR predicts its distance to a large corpus of retargeted robot poses, yielding a smooth measure of pose plausibility that is well suited for optimization and control. PDF-HR can be integrated as a reward shaping term, a regularizer, or a standalone plausibility scorer across diverse pipelines. We evaluate PDF-HR on various humanoid tasks, including single-trajectory motion tracking, general motion tracking, style-based motion mimicry, and general motion retargeting. Experiments show that this plug-and-play prior consistently and substantially strengthens strong baselines. Code and models will be released.

## 核心内容
Pose and motion priors play a crucial role in humanoid robotics. Although such priors have been widely studied in human motion recovery (HMR) domain with a range of models, their adoption for humanoid robots remains limited, largely due to the scarcity of high-quality humanoid motion data. In this work, we introduce Pose Distance Fields for Humanoid Robots (PDF-HR), a lightweight prior that represents the robot pose distribution as a continuous and differentiable manifold. Given an arbitrary pose, PDF-HR predicts its distance to a large corpus of retargeted robot poses, yielding a smooth measure of pose plausibility that is well suited for optimization and control. PDF-HR can be integrated as a reward shaping term, a regularizer, or a standalone plausibility scorer across diverse pipelines. We evaluate PDF-HR on various humanoid tasks, including single-trajectory motion tracking, general motion tracking, style-based motion mimicry, and general motion retargeting. Experiments show that this plug-and-play prior consistently and substantially strengthens strong baselines. Code and models will be released.

## 参考
- http://arxiv.org/abs/2602.04851v1

## Overview
Pose and motion priors play a crucial role in humanoid robotics. Although such priors have been widely studied in human motion recovery (HMR) domain with a range of models, their adoption for humanoid robots remains limited, largely due to the scarcity of high-quality humanoid motion data. In this work, we introduce Pose Distance Fields for Humanoid Robots (PDF-HR), a lightweight prior that represents the robot pose distribution as a continuous and differentiable manifold. Given an arbitrary pose, PDF-HR predicts its distance to a large corpus of retargeted robot poses, yielding a smooth measure of pose plausibility that is well suited for optimization and control. PDF-HR can be integrated as a reward shaping term, a regularizer, or a standalone plausibility scorer across diverse pipelines. We evaluate PDF-HR on various humanoid tasks, including single-trajectory motion tracking, general motion tracking, style-based motion mimicry, and general motion retargeting. Experiments show that this plug-and-play prior consistently and substantially strengthens strong baselines. Code and models will be released.

## Content
Pose and motion priors play a crucial role in humanoid robotics. Although such priors have been widely studied in human motion recovery (HMR) domain with a range of models, their adoption for humanoid robots remains limited, largely due to the scarcity of high-quality humanoid motion data. In this work, we introduce Pose Distance Fields for Humanoid Robots (PDF-HR), a lightweight prior that represents the robot pose distribution as a continuous and differentiable manifold. Given an arbitrary pose, PDF-HR predicts its distance to a large corpus of retargeted robot poses, yielding a smooth measure of pose plausibility that is well suited for optimization and control. PDF-HR can be integrated as a reward shaping term, a regularizer, or a standalone plausibility scorer across diverse pipelines. We evaluate PDF-HR on various humanoid tasks, including single-trajectory motion tracking, general motion tracking, style-based motion mimicry, and general motion retargeting. Experiments show that this plug-and-play prior consistently and substantially strengthens strong baselines. Code and models will be released.

## 개요
포즈 및 모션 사전 정보는 휴머노이드 로봇공학에서 중요한 역할을 합니다. 이러한 사전 정보는 다양한 모델을 통해 인간 동작 복원(HMR) 분야에서 널리 연구되어 왔지만, 휴머노이드 로봇에 적용되는 사례는 고품질 휴머노이드 동작 데이터의 부족으로 인해 여전히 제한적입니다. 본 연구에서는 로봇 포즈 분포를 연속적이고 미분 가능한 다양체로 표현하는 경량 사전 정보인 PDF-HR(Pose Distance Fields for Humanoid Robots)을 소개합니다. 임의의 포즈가 주어지면 PDF-HR은 대규모 리타겟팅된 로봇 포즈 코퍼스와의 거리를 예측하여 최적화 및 제어에 적합한 부드러운 포즈 타당성 측정값을 제공합니다. PDF-HR은 다양한 파이프라인에서 보상 형성 항, 정규화기 또는 독립형 타당성 스코어러로 통합될 수 있습니다. 단일 궤적 모션 추적, 일반 모션 추적, 스타일 기반 모션 모방, 일반 모션 리타겟팅 등 다양한 휴머노이드 작업에서 PDF-HR을 평가했습니다. 실험 결과, 이 플러그 앤 플레이 사전 정보가 강력한 기준 모델을 일관되게 크게 강화하는 것으로 나타났습니다. 코드와 모델은 공개될 예정입니다.

## 핵심 내용
포즈 및 모션 사전 정보는 휴머노이드 로봇공학에서 중요한 역할을 합니다. 이러한 사전 정보는 다양한 모델을 통해 인간 동작 복원(HMR) 분야에서 널리 연구되어 왔지만, 휴머노이드 로봇에 적용되는 사례는 고품질 휴머노이드 동작 데이터의 부족으로 인해 여전히 제한적입니다. 본 연구에서는 로봇 포즈 분포를 연속적이고 미분 가능한 다양체로 표현하는 경량 사전 정보인 PDF-HR(Pose Distance Fields for Humanoid Robots)을 소개합니다. 임의의 포즈가 주어지면 PDF-HR은 대규모 리타겟팅된 로봇 포즈 코퍼스와의 거리를 예측하여 최적화 및 제어에 적합한 부드러운 포즈 타당성 측정값을 제공합니다. PDF-HR은 다양한 파이프라인에서 보상 형성 항, 정규화기 또는 독립형 타당성 스코어러로 통합될 수 있습니다. 단일 궤적 모션 추적, 일반 모션 추적, 스타일 기반 모션 모방, 일반 모션 리타겟팅 등 다양한 휴머노이드 작업에서 PDF-HR을 평가했습니다. 실험 결과, 이 플러그 앤 플레이 사전 정보가 강력한 기준 모델을 일관되게 크게 강화하는 것으로 나타났습니다. 코드와 모델은 공개될 예정입니다.

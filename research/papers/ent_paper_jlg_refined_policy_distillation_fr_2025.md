---
$id: ent_paper_jlg_refined_policy_distillation_fr_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Refined Policy Distillation: From VLA Generalists to RL Experts'
  zh: RPD
  ko: 'Refined Policy Distillation: From VLA Generalists to RL Experts'
summary:
  en: 'Refined Policy Distillation: From VLA Generalists to RL Experts (RPD), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by University of Technology Nuremberg, and published at IROS25.'
  zh: 'Refined Policy Distillation: From VLA Generalists to RL Experts (RPD), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by University of Technology Nuremberg, and published at IROS25.'
  ko: 'Refined Policy Distillation: From VLA Generalists to RL Experts (RPD), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by University of Technology Nuremberg, and published at IROS25.'
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
- rpd
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.05833v2.
sources:
- id: src_001
  type: website
  title: RPD source
  url: https://doi.org/10.1109/IROS60139.2025.11246761
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action Models (VLAs) have demonstrated remarkable generalization capabilities in real-world experiments. However, their success rates are often not on par with expert policies, and they require fine-tuning when the setup changes. In this work, we introduce Refined Policy Distillation (RPD), a novel Reinforcement Learning (RL)-based policy refinement method that bridges this performance gap through a combination of on-policy RL with behavioral cloning. The core idea of RPD is to distill and refine VLAs into compact, high-performing expert policies by guiding the student policy during RL exploration using the actions of a teacher VLA, resulting in increased sample efficiency and faster convergence. We complement our method by fine-tuned versions of Octo and OpenVLA for ManiSkill3 to evaluate RPD in simulation. While this is a key requirement for applying RL, it also yields new insights beyond existing studies on VLA performance in real-world settings. Our experimental results across various manipulation tasks show that RPD enables the RL student to learn expert policies that outperform the VLA teacher in both dense and sparse reward settings, while also achieving faster convergence than the RL baseline. Our approach is even robust to changes in camera perspective and can generalize to task variations that the underlying VLA cannot solve. Our code, dataset, VLA checkpoints, and videos are available at https://refined-policy-distillation.github.io

## 核心内容
Vision-Language-Action Models (VLAs) have demonstrated remarkable generalization capabilities in real-world experiments. However, their success rates are often not on par with expert policies, and they require fine-tuning when the setup changes. In this work, we introduce Refined Policy Distillation (RPD), a novel Reinforcement Learning (RL)-based policy refinement method that bridges this performance gap through a combination of on-policy RL with behavioral cloning. The core idea of RPD is to distill and refine VLAs into compact, high-performing expert policies by guiding the student policy during RL exploration using the actions of a teacher VLA, resulting in increased sample efficiency and faster convergence. We complement our method by fine-tuned versions of Octo and OpenVLA for ManiSkill3 to evaluate RPD in simulation. While this is a key requirement for applying RL, it also yields new insights beyond existing studies on VLA performance in real-world settings. Our experimental results across various manipulation tasks show that RPD enables the RL student to learn expert policies that outperform the VLA teacher in both dense and sparse reward settings, while also achieving faster convergence than the RL baseline. Our approach is even robust to changes in camera perspective and can generalize to task variations that the underlying VLA cannot solve. Our code, dataset, VLA checkpoints, and videos are available at https://refined-policy-distillation.github.io

## 参考
- http://arxiv.org/abs/2503.05833v2

## Overview
Vision-Language-Action Models (VLAs) have demonstrated remarkable generalization capabilities in real-world experiments. However, their success rates are often not on par with expert policies, and they require fine-tuning when the setup changes. In this work, we introduce Refined Policy Distillation (RPD), a novel Reinforcement Learning (RL)-based policy refinement method that bridges this performance gap through a combination of on-policy RL with behavioral cloning. The core idea of RPD is to distill and refine VLAs into compact, high-performing expert policies by guiding the student policy during RL exploration using the actions of a teacher VLA, resulting in increased sample efficiency and faster convergence. We complement our method by fine-tuned versions of Octo and OpenVLA for ManiSkill3 to evaluate RPD in simulation. While this is a key requirement for applying RL, it also yields new insights beyond existing studies on VLA performance in real-world settings. Our experimental results across various manipulation tasks show that RPD enables the RL student to learn expert policies that outperform the VLA teacher in both dense and sparse reward settings, while also achieving faster convergence than the RL baseline. Our approach is even robust to changes in camera perspective and can generalize to task variations that the underlying VLA cannot solve. Our code, dataset, VLA checkpoints, and videos are available at https://refined-policy-distillation.github.io

## Content
Vision-Language-Action Models (VLAs) have demonstrated remarkable generalization capabilities in real-world experiments. However, their success rates are often not on par with expert policies, and they require fine-tuning when the setup changes. In this work, we introduce Refined Policy Distillation (RPD), a novel Reinforcement Learning (RL)-based policy refinement method that bridges this performance gap through a combination of on-policy RL with behavioral cloning. The core idea of RPD is to distill and refine VLAs into compact, high-performing expert policies by guiding the student policy during RL exploration using the actions of a teacher VLA, resulting in increased sample efficiency and faster convergence. We complement our method by fine-tuned versions of Octo and OpenVLA for ManiSkill3 to evaluate RPD in simulation. While this is a key requirement for applying RL, it also yields new insights beyond existing studies on VLA performance in real-world settings. Our experimental results across various manipulation tasks show that RPD enables the RL student to learn expert policies that outperform the VLA teacher in both dense and sparse reward settings, while also achieving faster convergence than the RL baseline. Our approach is even robust to changes in camera perspective and can generalize to task variations that the underlying VLA cannot solve. Our code, dataset, VLA checkpoints, and videos are available at https://refined-policy-distillation.github.io

## 개요
Vision-Language-Action Models (VLA)는 실제 환경 실험에서 뛰어난 일반화 능력을 입증했습니다. 그러나 성공률이 종종 전문가 정책에 미치지 못하며, 설정이 변경될 때 미세 조정이 필요합니다. 본 연구에서는 온-폴리시 RL과 행동 복제를 결합하여 이러한 성능 격차를 해소하는 새로운 강화 학습 기반 정책 개선 방법인 Refined Policy Distillation (RPD)을 소개합니다. RPD의 핵심 아이디어는 교사 VLA의 행동을 사용하여 RL 탐색 중 학생 정책을 안내함으로써 VLA를 소형의 고성능 전문가 정책으로 증류 및 개선하여 샘플 효율성을 높이고 수렴 속도를 가속화하는 것입니다. 우리는 시뮬레이션에서 RPD를 평가하기 위해 ManiSkill3용 Octo 및 OpenVLA의 미세 조정 버전으로 방법을 보완합니다. 이는 RL을 적용하기 위한 핵심 요구 사항이면서도 실제 환경에서 VLA 성능에 대한 기존 연구를 넘어 새로운 통찰력을 제공합니다. 다양한 조작 작업에 걸친 실험 결과는 RPD가 RL 학생이 밀집 보상 및 희소 보상 설정 모두에서 VLA 교사를 능가하는 전문가 정책을 학습할 수 있게 하며, RL 기준선보다 빠른 수렴을 달성함을 보여줍니다. 우리의 접근 방식은 카메라 시점 변화에도 강건하며, 기본 VLA가 해결할 수 없는 작업 변형에도 일반화할 수 있습니다. 코드, 데이터셋, VLA 체크포인트 및 비디오는 https://refined-policy-distillation.github.io 에서 확인할 수 있습니다.

## 핵심 내용
Vision-Language-Action Models (VLA)는 실제 환경 실험에서 뛰어난 일반화 능력을 입증했습니다. 그러나 성공률이 종종 전문가 정책에 미치지 못하며, 설정이 변경될 때 미세 조정이 필요합니다. 본 연구에서는 온-폴리시 RL과 행동 복제를 결합하여 이러한 성능 격차를 해소하는 새로운 강화 학습 기반 정책 개선 방법인 Refined Policy Distillation (RPD)을 소개합니다. RPD의 핵심 아이디어는 교사 VLA의 행동을 사용하여 RL 탐색 중 학생 정책을 안내함으로써 VLA를 소형의 고성능 전문가 정책으로 증류 및 개선하여 샘플 효율성을 높이고 수렴 속도를 가속화하는 것입니다. 우리는 시뮬레이션에서 RPD를 평가하기 위해 ManiSkill3용 Octo 및 OpenVLA의 미세 조정 버전으로 방법을 보완합니다. 이는 RL을 적용하기 위한 핵심 요구 사항이면서도 실제 환경에서 VLA 성능에 대한 기존 연구를 넘어 새로운 통찰력을 제공합니다. 다양한 조작 작업에 걸친 실험 결과는 RPD가 RL 학생이 밀집 보상 및 희소 보상 설정 모두에서 VLA 교사를 능가하는 전문가 정책을 학습할 수 있게 하며, RL 기준선보다 빠른 수렴을 달성함을 보여줍니다. 우리의 접근 방식은 카메라 시점 변화에도 강건하며, 기본 VLA가 해결할 수 없는 작업 변형에도 일반화할 수 있습니다. 코드, 데이터셋, VLA 체크포인트 및 비디오는 https://refined-policy-distillation.github.io 에서 확인할 수 있습니다.

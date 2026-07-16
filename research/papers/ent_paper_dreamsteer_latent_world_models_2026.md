---
$id: ent_paper_dreamsteer_latent_world_models_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DREAMSTEER: Latent World Models Can Steer VLA Policies During Deployment Without Any Finetuning'
  zh: 'DREAMSTEER: Latent World Models Can Steer VLA Policies During Deployment Without Any Finetuning'
  ko: 'DREAMSTEER: Latent World Models Can Steer VLA Policies During Deployment Without Any Finetuning'
summary:
  en: 'arXiv:2607.02865v1 Announce Type: new Abstract: Pretrained vision-language-action (VLA) policies show promising zero-shot
    generalization, but often fail under deployment-time distribution shift, leading to decreased robustness and inconsistent
    instruction following. While prior work commonly tackles this by finetuning on in-distribution data, it assumes demonstrations
    collected on tasks in the target environment. In this work, we propose DREAMSTEER, a deployment-time steering framework
    for pretrained VLAs without any finetuning or parameter modifications. The key insight in DREAMSTEER is to leverage a
    latent world model and a value model to steer pretrained VLA policies. During deployment, DREAMSTEER samples candidate
    action chunks from a VLA policy and predefined motion primitives, imagines their outcomes using an action-conditioned
    latent world model, and ranks the imagined trajectories with a language-conditioned value model. Across four real-world
    manipulation benchmarks with unseen objects, DREAMSTEER improves task success rate from 23.75% to 66.25% and instruction-following
    accuracy from 38.75% to 56.25% over the base VLA policy.'
  zh: 'arXiv:2607.02865v1 Announce Type: new Abstract: Pretrained vision-language-action (VLA) policies show promising zero-shot
    generalization, but often fail under deployment-time distribution shift, leading to decreased robustness and inconsistent
    instruction following. While prior work commonly tackles this by finetuning on in-distribution data, it assumes demonstrations
    collected on tasks in the target environment. In this work, we propose DREAMSTEER, a deployment-time steering framework
    for pretrained VLAs without any finetuning or parameter modifications. The key insight in DREAMSTEER is to leverage a
    latent world model and a value model to steer pretrained VLA policies. During deployment, DREAMSTEER samples candidate
    action chunks from a VLA policy and predefined motion primitives, imagines their outcomes using an action-conditioned
    latent world model, and ranks the imagined trajectories with a language-conditioned value model. Across four real-world
    manipulation benchmarks with unseen objects, DREAMSTEER improves task success rate from 23.75% to 66.25% and instruction-following
    accuracy from 38.75% to 56.25% over the base VLA policy.'
  ko: 'arXiv:2607.02865v1 Announce Type: new Abstract: Pretrained vision-language-action (VLA) policies show promising zero-shot
    generalization, but often fail under deployment-time distribution shift, leading to decreased robustness and inconsistent
    instruction following. While prior work commonly tackles this by finetuning on in-distribution data, it assumes demonstrations
    collected on tasks in the target environment. In this work, we propose DREAMSTEER, a deployment-time steering framework
    for pretrained VLAs without any finetuning or parameter modifications. The key insight in DREAMSTEER is to leverage a
    latent world model and a value model to steer pretrained VLA policies. During deployment, DREAMSTEER samples candidate
    action chunks from a VLA policy and predefined motion primitives, imagines their outcomes using an action-conditioned
    latent world model, and ranks the imagined trajectories with a language-conditioned value model. Across four real-world
    manipulation benchmarks with unseen objects, DREAMSTEER improves task success rate from 23.75% to 66.25% and instruction-following
    accuracy from 38.75% to 56.25% over the base VLA policy.'
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
- dreamsteer
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02865v1.
sources:
- id: src_001
  type: paper
  title: 'DREAMSTEER: Latent World Models Can Steer VLA Policies During Deployment Without Any Finetuning (arXiv)'
  url: https://arxiv.org/abs/2607.02865
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Pretrained vision-language-action (VLA) policies show promising zero-shot generalization, but often fail under deployment-time distribution shift, leading to decreased robustness and inconsistent instruction following. While prior work commonly tackles this by finetuning on in-distribution data, it assumes demonstrations collected on tasks in the target environment. In this work, we propose DREAMSTEER, a deployment-time steering framework for pretrained VLAs without any finetuning or parameter modifications. The key insight in DREAMSTEER is to leverage a latent world model and a value model to steer pretrained VLA policies. During deployment, DREAMSTEER samples candidate action chunks from a VLA policy and predefined motion primitives, imagines their outcomes using an action-conditioned latent world model, and ranks the imagined trajectories with a language-conditioned value model. Across four real-world manipulation benchmarks with unseen objects, DREAMSTEER improves task success rate from 23.75% to 66.25% and instruction-following accuracy from 38.75% to 56.25% over the base VLA policy.

## 核心内容
Pretrained vision-language-action (VLA) policies show promising zero-shot generalization, but often fail under deployment-time distribution shift, leading to decreased robustness and inconsistent instruction following. While prior work commonly tackles this by finetuning on in-distribution data, it assumes demonstrations collected on tasks in the target environment. In this work, we propose DREAMSTEER, a deployment-time steering framework for pretrained VLAs without any finetuning or parameter modifications. The key insight in DREAMSTEER is to leverage a latent world model and a value model to steer pretrained VLA policies. During deployment, DREAMSTEER samples candidate action chunks from a VLA policy and predefined motion primitives, imagines their outcomes using an action-conditioned latent world model, and ranks the imagined trajectories with a language-conditioned value model. Across four real-world manipulation benchmarks with unseen objects, DREAMSTEER improves task success rate from 23.75% to 66.25% and instruction-following accuracy from 38.75% to 56.25% over the base VLA policy.

## 参考
- http://arxiv.org/abs/2607.02865v1

## Overview
Pretrained vision-language-action (VLA) policies show promising zero-shot generalization, but often fail under deployment-time distribution shift, leading to decreased robustness and inconsistent instruction following. While prior work commonly tackles this by finetuning on in-distribution data, it assumes demonstrations collected on tasks in the target environment. In this work, we propose DREAMSTEER, a deployment-time steering framework for pretrained VLAs without any finetuning or parameter modifications. The key insight in DREAMSTEER is to leverage a latent world model and a value model to steer pretrained VLA policies. During deployment, DREAMSTEER samples candidate action chunks from a VLA policy and predefined motion primitives, imagines their outcomes using an action-conditioned latent world model, and ranks the imagined trajectories with a language-conditioned value model. Across four real-world manipulation benchmarks with unseen objects, DREAMSTEER improves task success rate from 23.75% to 66.25% and instruction-following accuracy from 38.75% to 56.25% over the base VLA policy.

## Content
Pretrained vision-language-action (VLA) policies show promising zero-shot generalization, but often fail under deployment-time distribution shift, leading to decreased robustness and inconsistent instruction following. While prior work commonly tackles this by finetuning on in-distribution data, it assumes demonstrations collected on tasks in the target environment. In this work, we propose DREAMSTEER, a deployment-time steering framework for pretrained VLAs without any finetuning or parameter modifications. The key insight in DREAMSTEER is to leverage a latent world model and a value model to steer pretrained VLA policies. During deployment, DREAMSTEER samples candidate action chunks from a VLA policy and predefined motion primitives, imagines their outcomes using an action-conditioned latent world model, and ranks the imagined trajectories with a language-conditioned value model. Across four real-world manipulation benchmarks with unseen objects, DREAMSTEER improves task success rate from 23.75% to 66.25% and instruction-following accuracy from 38.75% to 56.25% over the base VLA policy.

## 개요
사전 훈련된 비전-언어-행동(VLA) 정책은 유망한 제로샷 일반화를 보여주지만, 배포 시 분포 변화 하에서 종종 실패하여 견고성이 저하되고 명령 수행이 일관되지 않습니다. 기존 연구는 일반적으로 분포 내 데이터에 대한 미세 조정을 통해 이를 해결하지만, 이는 대상 환경의 작업에 대해 수집된 시연 데이터를 가정합니다. 본 연구에서는 미세 조정이나 파라미터 수정 없이 사전 훈련된 VLA를 위한 배포 시 조향 프레임워크인 DREAMSTEER를 제안합니다. DREAMSTEER의 핵심 통찰은 잠재 세계 모델과 가치 모델을 활용하여 사전 훈련된 VLA 정책을 조향하는 것입니다. 배포 중 DREAMSTEER는 VLA 정책과 사전 정의된 동작 프리미티브에서 후보 행동 청크를 샘플링하고, 행동 조건부 잠재 세계 모델을 사용하여 그 결과를 상상한 후, 언어 조건부 가치 모델로 상상된 궤적을 순위화합니다. 보이지 않는 객체를 포함한 네 가지 실제 조작 벤치마크에서 DREAMSTEER는 기본 VLA 정책 대비 작업 성공률을 23.75%에서 66.25%로, 명령 수행 정확도를 38.75%에서 56.25%로 향상시킵니다.

## 핵심 내용
사전 훈련된 비전-언어-행동(VLA) 정책은 유망한 제로샷 일반화를 보여주지만, 배포 시 분포 변화 하에서 종종 실패하여 견고성이 저하되고 명령 수행이 일관되지 않습니다. 기존 연구는 일반적으로 분포 내 데이터에 대한 미세 조정을 통해 이를 해결하지만, 이는 대상 환경의 작업에 대해 수집된 시연 데이터를 가정합니다. 본 연구에서는 미세 조정이나 파라미터 수정 없이 사전 훈련된 VLA를 위한 배포 시 조향 프레임워크인 DREAMSTEER를 제안합니다. DREAMSTEER의 핵심 통찰은 잠재 세계 모델과 가치 모델을 활용하여 사전 훈련된 VLA 정책을 조향하는 것입니다. 배포 중 DREAMSTEER는 VLA 정책과 사전 정의된 동작 프리미티브에서 후보 행동 청크를 샘플링하고, 행동 조건부 잠재 세계 모델을 사용하여 그 결과를 상상한 후, 언어 조건부 가치 모델로 상상된 궤적을 순위화합니다. 보이지 않는 객체를 포함한 네 가지 실제 조작 벤치마크에서 DREAMSTEER는 기본 VLA 정책 대비 작업 성공률을 23.75%에서 66.25%로, 명령 수행 정확도를 38.75%에서 56.25%로 향상시킵니다.

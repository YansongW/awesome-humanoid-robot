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
  zh: DREAMSTEER 是一种无需微调或参数修改的部署时引导框架，用于提升预训练视觉-语言-动作（VLA）策略在分布偏移下的鲁棒性。其核心创新在于利用潜在世界模型和价值模型，在部署时对候选动作进行想象与排序，从而显著改善任务成功率与指令遵循准确率。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02865v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'DREAMSTEER: Latent World Models Can Steer VLA Policies During Deployment Without Any Finetuning (arXiv)'
  url: https://arxiv.org/abs/2607.02865
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
预训练的 VLA 策略在零样本泛化上表现良好，但在部署时遇到分布偏移常会失败，导致鲁棒性下降和指令执行不一致。现有方法通常依赖目标环境中的演示数据进行微调，但 DREAMSTEER 提出了一种无需任何微调或参数修改的部署时引导方案。它通过潜在世界模型想象候选动作的结果，并用语言条件价值模型对想象轨迹进行排序，从而选择最优动作。在四个涉及未见物体的真实操作基准上，DREAMSTEER 将任务成功率从 23.75% 提升至 66.25%，指令遵循准确率从 38.75% 提升至 56.25%。

## 核心内容
### 方法概述
DREAMSTEER 的核心思想是在部署阶段利用潜在世界模型和价值模型来引导预训练 VLA 策略，无需任何微调或参数修改。具体流程如下：
- **候选动作采样**：从 VLA 策略和预定义的运动基元中采样候选动作块。
- **想象结果**：使用动作条件的潜在世界模型来想象这些候选动作的未来轨迹。
- **轨迹排序**：通过语言条件的价值模型对想象轨迹进行排序，选择最优动作执行。

### 实验设置与结果
- **基准测试**：在四个真实世界操作基准上进行评估，涉及未见物体。
- **性能提升**：
  - 任务成功率：从基础 VLA 策略的 23.75% 提升至 66.25%。
  - 指令遵循准确率：从 38.75% 提升至 56.25%。
- **关键优势**：无需收集目标环境中的演示数据，也无需对模型进行任何参数调整，即可在部署时有效应对分布偏移。

## Overview
Pretrained vision-language-action (VLA) policies show promising zero-shot generalization, but often fail under deployment-time distribution shift, leading to decreased robustness and inconsistent instruction following. While prior work commonly tackles this by finetuning on in-distribution data, it assumes demonstrations collected on tasks in the target environment. In this work, we propose DREAMSTEER, a deployment-time steering framework for pretrained VLAs without any finetuning or parameter modifications. The key insight in DREAMSTEER is to leverage a latent world model and a value model to steer pretrained VLA policies. During deployment, DREAMSTEER samples candidate action chunks from a VLA policy and predefined motion primitives, imagines their outcomes using an action-conditioned latent world model, and ranks the imagined trajectories with a language-conditioned value model. Across four real-world manipulation benchmarks with unseen objects, DREAMSTEER improves task success rate from 23.75% to 66.25% and instruction-following accuracy from 38.75% to 56.25% over the base VLA policy.

## 개요
사전 훈련된 비전-언어-행동(VLA) 정책은 유망한 제로샷 일반화를 보여주지만, 배포 시 분포 변화 하에서 종종 실패하여 견고성이 저하되고 명령 수행이 일관되지 않습니다. 기존 연구는 일반적으로 분포 내 데이터에 대한 미세 조정을 통해 이를 해결하지만, 이는 대상 환경의 작업에 대해 수집된 시연 데이터를 가정합니다. 본 연구에서는 미세 조정이나 파라미터 수정 없이 사전 훈련된 VLA를 위한 배포 시 조향 프레임워크인 DREAMSTEER를 제안합니다. DREAMSTEER의 핵심 통찰은 잠재 세계 모델과 가치 모델을 활용하여 사전 훈련된 VLA 정책을 조향하는 것입니다. 배포 중 DREAMSTEER는 VLA 정책과 사전 정의된 동작 프리미티브에서 후보 행동 청크를 샘플링하고, 행동 조건부 잠재 세계 모델을 사용하여 그 결과를 상상한 후, 언어 조건부 가치 모델로 상상된 궤적을 순위화합니다. 보이지 않는 객체를 포함한 네 가지 실제 조작 벤치마크에서 DREAMSTEER는 기본 VLA 정책 대비 작업 성공률을 23.75%에서 66.25%로, 명령 수행 정확도를 38.75%에서 56.25%로 향상시킵니다.

## 핵심 내용
사전 훈련된 비전-언어-행동(VLA) 정책은 유망한 제로샷 일반화를 보여주지만, 배포 시 분포 변화 하에서 종종 실패하여 견고성이 저하되고 명령 수행이 일관되지 않습니다. 기존 연구는 일반적으로 분포 내 데이터에 대한 미세 조정을 통해 이를 해결하지만, 이는 대상 환경의 작업에 대해 수집된 시연 데이터를 가정합니다. 본 연구에서는 미세 조정이나 파라미터 수정 없이 사전 훈련된 VLA를 위한 배포 시 조향 프레임워크인 DREAMSTEER를 제안합니다. DREAMSTEER의 핵심 통찰은 잠재 세계 모델과 가치 모델을 활용하여 사전 훈련된 VLA 정책을 조향하는 것입니다. 배포 중 DREAMSTEER는 VLA 정책과 사전 정의된 동작 프리미티브에서 후보 행동 청크를 샘플링하고, 행동 조건부 잠재 세계 모델을 사용하여 그 결과를 상상한 후, 언어 조건부 가치 모델로 상상된 궤적을 순위화합니다. 보이지 않는 객체를 포함한 네 가지 실제 조작 벤치마크에서 DREAMSTEER는 기본 VLA 정책 대비 작업 성공률을 23.75%에서 66.25%로, 명령 수행 정확도를 38.75%에서 56.25%로 향상시킵니다.

## 参考
- http://arxiv.org/abs/2607.02865v1

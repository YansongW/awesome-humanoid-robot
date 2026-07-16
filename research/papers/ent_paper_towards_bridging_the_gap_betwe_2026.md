---
$id: ent_paper_towards_bridging_the_gap_betwe_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control
  zh: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control
  ko: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control
summary:
  en: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control is a 2026 work
    on sim-to-real for humanoid robots, with open-source code available.
  zh: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control is a 2026 work
    on sim-to-real for humanoid robots, with open-source code available.
  ko: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control is a 2026 work
    on sim-to-real for humanoid robots, with open-source code available.
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
- sim_to_real
- towards_bridging_the_gap_betwe
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.21363v3.
sources:
- id: src_001
  type: paper
  title: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control (arXiv)
  url: https://arxiv.org/abs/2601.21363
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control project page
  url: https://lift-humanoid.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Reinforcement learning (RL) is widely used for humanoid control, with on-policy methods such as Proximal Policy Optimization (PPO) enabling robust training via large-scale parallel simulation and, in some cases, zero-shot deployment to real robots. However, the low sample efficiency of on-policy algorithms limits safe adaptation to new environments. Although off-policy RL and model-based RL have shown improved sample efficiency, the gap between large-scale pretraining and efficient finetuning on humanoids still exists. In this paper, we find that off-policy Soft Actor-Critic (SAC), with large-batch update and a high Update-To-Data (UTD) ratio, reliably supports large-scale pretraining of humanoid locomotion policies, achieving zero-shot deployment on real robots. For adaptation, we demonstrate that these SAC-pretrained policies can be finetuned in new environments and out-of-distribution tasks using model-based methods. Data collection in the new environment executes a deterministic policy while stochastic exploration is instead confined to a physics-informed world model. This separation mitigates the risks of random exploration during adaptation while preserving exploratory coverage for improvement. Overall, the approach couples the wall-clock efficiency of large-scale simulation during pretraining with the sample efficiency of model-based learning during fine-tuning. For code and videos, see https://lift-humanoid.github.io

## 核心内容
Reinforcement learning (RL) is widely used for humanoid control, with on-policy methods such as Proximal Policy Optimization (PPO) enabling robust training via large-scale parallel simulation and, in some cases, zero-shot deployment to real robots. However, the low sample efficiency of on-policy algorithms limits safe adaptation to new environments. Although off-policy RL and model-based RL have shown improved sample efficiency, the gap between large-scale pretraining and efficient finetuning on humanoids still exists. In this paper, we find that off-policy Soft Actor-Critic (SAC), with large-batch update and a high Update-To-Data (UTD) ratio, reliably supports large-scale pretraining of humanoid locomotion policies, achieving zero-shot deployment on real robots. For adaptation, we demonstrate that these SAC-pretrained policies can be finetuned in new environments and out-of-distribution tasks using model-based methods. Data collection in the new environment executes a deterministic policy while stochastic exploration is instead confined to a physics-informed world model. This separation mitigates the risks of random exploration during adaptation while preserving exploratory coverage for improvement. Overall, the approach couples the wall-clock efficiency of large-scale simulation during pretraining with the sample efficiency of model-based learning during fine-tuning. For code and videos, see https://lift-humanoid.github.io

## 参考
- http://arxiv.org/abs/2601.21363v3

## Overview
Reinforcement learning (RL) is widely used for humanoid control, with on-policy methods such as Proximal Policy Optimization (PPO) enabling robust training via large-scale parallel simulation and, in some cases, zero-shot deployment to real robots. However, the low sample efficiency of on-policy algorithms limits safe adaptation to new environments. Although off-policy RL and model-based RL have shown improved sample efficiency, the gap between large-scale pretraining and efficient finetuning on humanoids still exists. In this paper, we find that off-policy Soft Actor-Critic (SAC), with large-batch update and a high Update-To-Data (UTD) ratio, reliably supports large-scale pretraining of humanoid locomotion policies, achieving zero-shot deployment on real robots. For adaptation, we demonstrate that these SAC-pretrained policies can be finetuned in new environments and out-of-distribution tasks using model-based methods. Data collection in the new environment executes a deterministic policy while stochastic exploration is instead confined to a physics-informed world model. This separation mitigates the risks of random exploration during adaptation while preserving exploratory coverage for improvement. Overall, the approach couples the wall-clock efficiency of large-scale simulation during pretraining with the sample efficiency of model-based learning during fine-tuning. For code and videos, see https://lift-humanoid.github.io

## Content
Reinforcement learning (RL) is widely used for humanoid control, with on-policy methods such as Proximal Policy Optimization (PPO) enabling robust training via large-scale parallel simulation and, in some cases, zero-shot deployment to real robots. However, the low sample efficiency of on-policy algorithms limits safe adaptation to new environments. Although off-policy RL and model-based RL have shown improved sample efficiency, the gap between large-scale pretraining and efficient finetuning on humanoids still exists. In this paper, we find that off-policy Soft Actor-Critic (SAC), with large-batch update and a high Update-To-Data (UTD) ratio, reliably supports large-scale pretraining of humanoid locomotion policies, achieving zero-shot deployment on real robots. For adaptation, we demonstrate that these SAC-pretrained policies can be finetuned in new environments and out-of-distribution tasks using model-based methods. Data collection in the new environment executes a deterministic policy while stochastic exploration is instead confined to a physics-informed world model. This separation mitigates the risks of random exploration during adaptation while preserving exploratory coverage for improvement. Overall, the approach couples the wall-clock efficiency of large-scale simulation during pretraining with the sample efficiency of model-based learning during fine-tuning. For code and videos, see https://lift-humanoid.github.io

## 개요
강화 학습(RL)은 인간형 로봇 제어에 널리 사용되며, Proximal Policy Optimization(PPO)과 같은 온-폴리시 방법은 대규모 병렬 시뮬레이션을 통한 강건한 훈련과 경우에 따라 실제 로봇으로의 제로샷 배치를 가능하게 합니다. 그러나 온-폴리시 알고리즘의 낮은 샘플 효율성은 새로운 환경에 대한 안전한 적응을 제한합니다. 오프-폴리시 RL과 모델 기반 RL이 샘플 효율성을 개선했음에도 불구하고, 인간형 로봇에서 대규모 사전 훈련과 효율적인 미세 조정 사이의 격차는 여전히 존재합니다. 본 논문에서는 대규모 배치 업데이트와 높은 UTD(Update-To-Data) 비율을 갖춘 오프-폴리시 Soft Actor-Critic(SAC)이 인간형 로봇 보행 정책의 대규모 사전 훈련을 안정적으로 지원하며, 실제 로봇에서 제로샷 배치를 달성함을 발견했습니다. 적응을 위해, 이러한 SAC 사전 훈련된 정책이 모델 기반 방법을 사용하여 새로운 환경과 분포 외 과제에서 미세 조정될 수 있음을 입증합니다. 새로운 환경에서의 데이터 수집은 결정론적 정책을 실행하는 반면, 확률적 탐색은 물리 정보 기반 세계 모델에 국한됩니다. 이러한 분리는 적응 중 무작위 탐색의 위험을 완화하면서도 개선을 위한 탐색 범위를 유지합니다. 전반적으로, 이 접근 방식은 사전 훈련 중 대규모 시뮬레이션의 벽시계 효율성과 미세 조정 중 모델 기반 학습의 샘플 효율성을 결합합니다. 코드와 비디오는 https://lift-humanoid.github.io 에서 확인할 수 있습니다.

## 핵심 내용
강화 학습(RL)은 인간형 로봇 제어에 널리 사용되며, Proximal Policy Optimization(PPO)과 같은 온-폴리시 방법은 대규모 병렬 시뮬레이션을 통한 강건한 훈련과 경우에 따라 실제 로봇으로의 제로샷 배치를 가능하게 합니다. 그러나 온-폴리시 알고리즘의 낮은 샘플 효율성은 새로운 환경에 대한 안전한 적응을 제한합니다. 오프-폴리시 RL과 모델 기반 RL이 샘플 효율성을 개선했음에도 불구하고, 인간형 로봇에서 대규모 사전 훈련과 효율적인 미세 조정 사이의 격차는 여전히 존재합니다. 본 논문에서는 대규모 배치 업데이트와 높은 UTD(Update-To-Data) 비율을 갖춘 오프-폴리시 Soft Actor-Critic(SAC)이 인간형 로봇 보행 정책의 대규모 사전 훈련을 안정적으로 지원하며, 실제 로봇에서 제로샷 배치를 달성함을 발견했습니다. 적응을 위해, 이러한 SAC 사전 훈련된 정책이 모델 기반 방법을 사용하여 새로운 환경과 분포 외 과제에서 미세 조정될 수 있음을 입증합니다. 새로운 환경에서의 데이터 수집은 결정론적 정책을 실행하는 반면, 확률적 탐색은 물리 정보 기반 세계 모델에 국한됩니다. 이러한 분리는 적응 중 무작위 탐색의 위험을 완화하면서도 개선을 위한 탐색 범위를 유지합니다. 전반적으로, 이 접근 방식은 사전 훈련 중 대규모 시뮬레이션의 벽시계 효율성과 미세 조정 중 모델 기반 학습의 샘플 효율성을 결합합니다. 코드와 비디오는 https://lift-humanoid.github.io 에서 확인할 수 있습니다.

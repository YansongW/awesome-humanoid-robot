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
  zh: 本文提出一种结合大规模预训练与高效微调的人形机器人控制方法。该方法利用SAC算法进行大规模预训练，实现零样本部署；在微调阶段采用基于模型的策略，通过分离确定性执行与随机探索，提升样本效率并降低风险。代码已开源。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.21363v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
本文针对人形机器人控制中大规模预训练与高效微调之间的差距问题，提出了一种结合SAC与基于模型方法的解决方案。研究发现，采用大批次更新和高UTD比率的SAC算法能够可靠地支持人形机器人运动策略的大规模预训练，并实现零样本部署。在微调阶段，该方法利用基于模型的世界模型进行随机探索，同时保持确定性策略执行，从而在适应新环境时降低随机探索风险，提升样本效率。整体方法兼顾了预训练阶段的大规模仿真效率与微调阶段的样本效率。

## 核心内容
### 方法概述
本文针对人形机器人控制中大规模预训练与高效微调之间的差距，提出了一种两阶段方法：
- **预训练阶段**：采用off-policy的Soft Actor-Critic (SAC)算法，通过大批次更新和高Update-To-Data (UTD)比率，在并行仿真环境中进行大规模训练，实现零样本部署到真实机器人。
- **微调阶段**：利用基于模型的方法对预训练策略进行微调。在新环境中，数据收集采用确定性策略执行，而随机探索则被限制在一个基于物理的世界模型内。这种分离设计降低了适应过程中随机探索的风险，同时保留了改进所需的探索覆盖范围。

### 实验设置与关键数字
- 实验基于人形机器人控制任务，使用大规模并行仿真进行预训练。
- 预训练阶段采用SAC算法，UTD比率设置为较高值（具体数值未在摘要中给出）。
- 微调阶段在新环境和分布外任务中进行，验证了方法的适应能力。
- 代码和视频已开源，详见 https://lift-humanoid.github.io

### 结论
该方法通过耦合大规模仿真预训练与基于模型微调，有效弥合了人形机器人控制中大规模预训练与高效微调之间的差距，实现了零样本部署与样本高效的适应。

## Overview
Reinforcement learning (RL) is widely used for humanoid control, with on-policy methods such as Proximal Policy Optimization (PPO) enabling robust training via large-scale parallel simulation and, in some cases, zero-shot deployment to real robots. However, the low sample efficiency of on-policy algorithms limits safe adaptation to new environments. Although off-policy RL and model-based RL have shown improved sample efficiency, the gap between large-scale pretraining and efficient finetuning on humanoids still exists. In this paper, we find that off-policy Soft Actor-Critic (SAC), with large-batch update and a high Update-To-Data (UTD) ratio, reliably supports large-scale pretraining of humanoid locomotion policies, achieving zero-shot deployment on real robots. For adaptation, we demonstrate that these SAC-pretrained policies can be finetuned in new environments and out-of-distribution tasks using model-based methods. Data collection in the new environment executes a deterministic policy while stochastic exploration is instead confined to a physics-informed world model. This separation mitigates the risks of random exploration during adaptation while preserving exploratory coverage for improvement. Overall, the approach couples the wall-clock efficiency of large-scale simulation during pretraining with the sample efficiency of model-based learning during fine-tuning. For code and videos, see https://lift-humanoid.github.io

## 개요
강화 학습(RL)은 인간형 로봇 제어에 널리 사용되며, Proximal Policy Optimization(PPO)과 같은 온-폴리시 방법은 대규모 병렬 시뮬레이션을 통한 강건한 훈련과 경우에 따라 실제 로봇으로의 제로샷 배치를 가능하게 합니다. 그러나 온-폴리시 알고리즘의 낮은 샘플 효율성은 새로운 환경에 대한 안전한 적응을 제한합니다. 오프-폴리시 RL과 모델 기반 RL이 샘플 효율성을 개선했음에도 불구하고, 인간형 로봇에서 대규모 사전 훈련과 효율적인 미세 조정 사이의 격차는 여전히 존재합니다. 본 논문에서는 대규모 배치 업데이트와 높은 UTD(Update-To-Data) 비율을 갖춘 오프-폴리시 Soft Actor-Critic(SAC)이 인간형 로봇 보행 정책의 대규모 사전 훈련을 안정적으로 지원하며, 실제 로봇에서 제로샷 배치를 달성함을 발견했습니다. 적응을 위해, 이러한 SAC 사전 훈련된 정책이 모델 기반 방법을 사용하여 새로운 환경과 분포 외 과제에서 미세 조정될 수 있음을 입증합니다. 새로운 환경에서의 데이터 수집은 결정론적 정책을 실행하는 반면, 확률적 탐색은 물리 정보 기반 세계 모델에 국한됩니다. 이러한 분리는 적응 중 무작위 탐색의 위험을 완화하면서도 개선을 위한 탐색 범위를 유지합니다. 전반적으로, 이 접근 방식은 사전 훈련 중 대규모 시뮬레이션의 벽시계 효율성과 미세 조정 중 모델 기반 학습의 샘플 효율성을 결합합니다. 코드와 비디오는 https://lift-humanoid.github.io 에서 확인할 수 있습니다.

## 핵심 내용
강화 학습(RL)은 인간형 로봇 제어에 널리 사용되며, Proximal Policy Optimization(PPO)과 같은 온-폴리시 방법은 대규모 병렬 시뮬레이션을 통한 강건한 훈련과 경우에 따라 실제 로봇으로의 제로샷 배치를 가능하게 합니다. 그러나 온-폴리시 알고리즘의 낮은 샘플 효율성은 새로운 환경에 대한 안전한 적응을 제한합니다. 오프-폴리시 RL과 모델 기반 RL이 샘플 효율성을 개선했음에도 불구하고, 인간형 로봇에서 대규모 사전 훈련과 효율적인 미세 조정 사이의 격차는 여전히 존재합니다. 본 논문에서는 대규모 배치 업데이트와 높은 UTD(Update-To-Data) 비율을 갖춘 오프-폴리시 Soft Actor-Critic(SAC)이 인간형 로봇 보행 정책의 대규모 사전 훈련을 안정적으로 지원하며, 실제 로봇에서 제로샷 배치를 달성함을 발견했습니다. 적응을 위해, 이러한 SAC 사전 훈련된 정책이 모델 기반 방법을 사용하여 새로운 환경과 분포 외 과제에서 미세 조정될 수 있음을 입증합니다. 새로운 환경에서의 데이터 수집은 결정론적 정책을 실행하는 반면, 확률적 탐색은 물리 정보 기반 세계 모델에 국한됩니다. 이러한 분리는 적응 중 무작위 탐색의 위험을 완화하면서도 개선을 위한 탐색 범위를 유지합니다. 전반적으로, 이 접근 방식은 사전 훈련 중 대규모 시뮬레이션의 벽시계 효율성과 미세 조정 중 모델 기반 학습의 샘플 효율성을 결합합니다. 코드와 비디오는 https://lift-humanoid.github.io 에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2601.21363v3

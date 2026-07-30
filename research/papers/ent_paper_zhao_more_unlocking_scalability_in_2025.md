---
$id: ent_paper_zhao_more_unlocking_scalability_in_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MoRE: Unlocking Scalability in Reinforcement Learning for Quadruped Vision-Language-Action Models'
  zh: MoRE
  ko: 'MoRE: Unlocking Scalability in Reinforcement Learning for Quadruped Vision-Language-Action Models'
summary:
  en: 'MoRE: Unlocking Scalability in Reinforcement Learning for Quadruped Vision-Language-Action Models (MoRE), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Sun Yat-sen University, Guangdong Key Laboratory
    of Big Data Analysis and Processing, X-Era AI Lab, and published at ICRA25.'
  zh: MoRE 是由中山大学、广东省大数据分析与处理重点实验室及 X-Era AI Lab 于 ICRA25 提出的四足机器人视觉-语言-动作模型。其核心贡献在于通过混合专家架构与强化学习微调，实现大规模混合质量数据的高效利用，在六项技能任务中超越所有基线，并展现出卓越的泛化能力。
  ko: 'MoRE: Unlocking Scalability in Reinforcement Learning for Quadruped Vision-Language-Action Models (MoRE), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Sun Yat-sen University, Guangdong Key Laboratory
    of Big Data Analysis and Processing, X-Era AI Lab, and published at ICRA25.'
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
- more
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.08007v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: website
  title: MoRE source
  url: https://doi.org/10.1109/ICRA55743.2025.11128601
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
MoRE 针对四足机器人多任务学习的挑战，创新性地将多个低秩适配模块作为独立专家嵌入密集多模态大语言模型，构建稀疏激活的混合专家架构。该设计使模型能灵活适应多种下游任务，同时通过基于强化学习的 Q 函数训练目标，有效利用自动收集的混合质量数据提升数据效率与模型性能。实验表明，MoRE 在六项不同技能任务中均优于基线方法，并在分布外场景中展现出更强的泛化能力，真实环境验证进一步确认了其实用性。

## 核心内容
### 方法架构
MoRE 的核心创新在于将多个低秩适配模块（LoRA）作为独立专家嵌入密集多模态大语言模型（MLLM），形成稀疏激活的混合专家模型（MoE）。这种设计使模型在保持基础能力的同时，能针对不同任务动态激活相关专家模块，有效适应多样化下游任务。

### 训练策略
- 采用强化学习（RL）训练目标，将模型训练为 Q 函数，通过深入分析任务结构特性优化学习过程。
- 利用自动收集的混合质量数据（mixed-quality data）进行训练，显著提升数据效率与模型性能。

### 实验设置与结果
- 在六项不同技能任务（如导航、抓取等）中，MoRE 均超越所有基线方法。
- 在分布外（out-of-distribution）场景中，模型展现出更强的泛化能力。
- 真实环境验证进一步确认了方法的实用性，为四足机器人多任务学习研究奠定基础。

## Overview
Developing versatile quadruped robots that can smoothly perform various actions and tasks in real-world environments remains a significant challenge. This paper introduces a novel vision-language-action (VLA) model, mixture of robotic experts (MoRE), for quadruped robots that aim to introduce reinforcement learning (RL) for fine-tuning large-scale VLA models with a large amount of mixed-quality data. MoRE integrates multiple low-rank adaptation modules as distinct experts within a dense multi-modal large language model (MLLM), forming a sparse-activated mixture-of-experts model. This design enables the model to effectively adapt to a wide array of downstream tasks. Moreover, we employ a reinforcement learning-based training objective to train our model as a Q-function after deeply exploring the structural properties of our tasks. Effective learning from automatically collected mixed-quality data enhances data efficiency and model performance. Extensive experiments demonstrate that MoRE outperforms all baselines across six different skills and exhibits superior generalization capabilities in out-of-distribution scenarios. We further validate our method in real-world scenarios, confirming the practicality of our approach and laying a solid foundation for future research on multi-task learning in quadruped robots.

## 개요
실제 환경에서 다양한 동작과 작업을 원활히 수행할 수 있는 다재다능한 사족 로봇을 개발하는 것은 여전히 중요한 과제입니다. 본 논문은 혼합 품질의 대규모 데이터를 활용하여 대규모 VLA 모델을 미세 조정하기 위해 강화 학습(RL)을 도입하는 것을 목표로 하는 사족 로봇용 새로운 시각-언어-행동(VLA) 모델, 혼합 로봇 전문가(MoRE)를 소개합니다. MoRE는 밀집된 다중 모달 대규모 언어 모델(MLLM) 내에 여러 저랭크 적응 모듈을 개별 전문가로 통합하여 희소 활성화 혼합 전문가 모델을 형성합니다. 이 설계는 모델이 다양한 하위 작업에 효과적으로 적응할 수 있도록 합니다. 또한, 작업의 구조적 특성을 깊이 탐구한 후 강화 학습 기반 훈련 목표를 사용하여 모델을 Q-함수로 훈련합니다. 자동으로 수집된 혼합 품질 데이터로부터 효과적으로 학습함으로써 데이터 효율성과 모델 성능을 향상시킵니다. 광범위한 실험을 통해 MoRE가 여섯 가지 다양한 기술에서 모든 기준 모델을 능가하며, 분포 외 시나리오에서 뛰어난 일반화 능력을 보여줌을 입증했습니다. 실제 환경에서도 방법을 추가로 검증하여 접근 방식의 실용성을 확인하고, 사족 로봇의 다중 작업 학습에 대한 향후 연구를 위한 견고한 기반을 마련했습니다.

## 핵심 내용
실제 환경에서 다양한 동작과 작업을 원활히 수행할 수 있는 다재다능한 사족 로봇을 개발하는 것은 여전히 중요한 과제입니다. 본 논문은 혼합 품질의 대규모 데이터를 활용하여 대규모 VLA 모델을 미세 조정하기 위해 강화 학습(RL)을 도입하는 것을 목표로 하는 사족 로봇용 새로운 시각-언어-행동(VLA) 모델, 혼합 로봇 전문가(MoRE)를 소개합니다. MoRE는 밀집된 다중 모달 대규모 언어 모델(MLLM) 내에 여러 저랭크 적응 모듈을 개별 전문가로 통합하여 희소 활성화 혼합 전문가 모델을 형성합니다. 이 설계는 모델이 다양한 하위 작업에 효과적으로 적응할 수 있도록 합니다. 또한, 작업의 구조적 특성을 깊이 탐구한 후 강화 학습 기반 훈련 목표를 사용하여 모델을 Q-함수로 훈련합니다. 자동으로 수집된 혼합 품질 데이터로부터 효과적으로 학습함으로써 데이터 효율성과 모델 성능을 향상시킵니다. 광범위한 실험을 통해 MoRE가 여섯 가지 다양한 기술에서 모든 기준 모델을 능가하며, 분포 외 시나리오에서 뛰어난 일반화 능력을 보여줌을 입증했습니다. 실제 환경에서도 방법을 추가로 검증하여 접근 방식의 실용성을 확인하고, 사족 로봇의 다중 작업 학습에 대한 향후 연구를 위한 견고한 기반을 마련했습니다.

## 参考
- http://arxiv.org/abs/2503.08007v1

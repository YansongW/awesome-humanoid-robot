---
$id: ent_paper_zhang_align_then_steer_adapting_the_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Align-Then-stEer: Adapting the Vision-Language Action Models through Unified Latent Guidance'
  zh: ATE
  ko: 'Align-Then-stEer: Adapting the Vision-Language Action Models through Unified Latent Guidance'
summary:
  en: 'Align-Then-stEer: Adapting the Vision-Language Action Models through Unified Latent Guidance (ATE), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute of Artificial Intelligence, China Telecom,
    Tsinghua University, The Chinese University of Hong Kong, Shenzhen, Northwestern Polytechnical University.'
  zh: Align-Then-stEer (ATE) 是一种2025年提出的数据高效、即插即用的视觉-语言-动作模型适配框架，由中国电信人工智能研究院、清华大学、香港中文大学（深圳）及西北工业大学联合开发。其核心贡献在于通过统一潜在空间对齐不同动作分布，并利用引导机制微调扩散或流基VLA模型，在仿真和真实场景的跨实体与跨任务操作中显著提升成功率。
  ko: 'Align-Then-stEer: Adapting the Vision-Language Action Models through Unified Latent Guidance (ATE), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute of Artificial Intelligence, China Telecom,
    Tsinghua University, The Chinese University of Hong Kong, Shenzhen, Northwestern Polytechnical University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ate
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.02055v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Align-Then-stEer: Adapting the Vision-Language Action Models through Unified Latent Guidance (arXiv)'
  url: https://arxiv.org/abs/2509.02055
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ATE source
  url: https://doi.org/10.48550/arXiv.2509.02055
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
针对预训练VLA模型在下游任务中因实体或任务差异导致的动作分布不匹配问题，ATE提出两阶段解决方案：首先通过变分自编码器（约束反向KL散度）将适配动作嵌入预训练动作潜在分布的模式中，构建统一潜在空间；随后在微调阶段通过引导机制驱动模型输出向目标域偏移。实验表明，在仿真环境中ATE相比直接微调方法将多任务平均成功率提升最高9.8%，在真实跨实体场景中更实现32%的成功率增益，为VLA模型部署提供了轻量化通用方案。

## 核心内容
### 方法架构
- **对齐阶段（Align）**：利用变分自编码器（VAE）构建统一潜在空间，通过反向KL散度约束将下游任务的适配动作嵌入预训练动作潜在分布的模式中，从而消除不同实体或任务间的动作空间差异。
- **引导阶段（Steer）**：在微调扩散或流基VLA模型时，引入引导机制（guidance mechanism）驱动模型输出分布向目标域偏移，无需修改预训练模型主干。

### 实验设置
- **仿真环境**：基于多个跨实体（不同机器人形态）与跨任务（如抓取、堆叠）操作基准，对比直接微调（Direct Fine-tuning）与ATE方法。
- **真实场景**：在真实机器人平台上进行跨实体操作实验，评估ATE的泛化能力。

### 关键结果
- **仿真性能**：ATE将多任务平均成功率提升最高9.8%（相比直接微调），在部分任务上成功率绝对值超过85%。
- **真实场景**：在跨实体设置中，ATE实现32%的成功率增益，显著优于基线方法。
- **数据效率**：仅需少量目标域数据即可完成适配，无需大规模重新训练。

### 结论
ATE通过统一潜在空间对齐与引导机制，为VLA模型提供了一种轻量化、即插即用的适配方案，大幅提升了其在新型机器人平台和任务中的部署实用性。

## Overview
Vision-Language-Action (VLA) models pre-trained on large, diverse datasets show remarkable potential for general-purpose robotic manipulation. However, a primary bottleneck remains in adapting these models to downstream tasks, especially when the robot's embodiment or the task itself differs from the pre-training data. This discrepancy leads to a significant mismatch in action distributions, demanding extensive data and compute for effective fine-tuning. To address this challenge, we introduce \textbf{Align-Then-stEer (\texttt{ATE})}, a novel, data-efficient, and plug-and-play adaptation framework. \texttt{ATE} first aligns disparate action spaces by constructing a unified latent space, where a variational autoencoder constrained by reverse KL divergence embeds adaptation actions into modes of the pre-training action latent distribution. Subsequently, it steers the diffusion- or flow-based VLA's generation process during fine-tuning via a guidance mechanism that pushes the model's output distribution towards the target domain. We conduct extensive experiments on cross-embodiment and cross-task manipulation in both simulation and real world. Compared to direct fine-tuning of representative VLAs, our method improves the average multi-task success rate by up to \textbf{9.8\%} in simulation and achieves a striking \textbf{32\% success rate gain} in a real-world cross-embodiment setting. Our work presents a general and lightweight solution that greatly enhances the practicality of deploying VLA models to new robotic platforms and tasks.

## Overview
Vision-Language-Action (VLA) models pre-trained on large, diverse datasets show remarkable potential for general-purpose robotic manipulation. However, a primary bottleneck remains in adapting these models to downstream tasks, especially when the robot's embodiment or the task itself differs from the pre-training data. This discrepancy leads to a significant mismatch in action distributions, demanding extensive data and compute for effective fine-tuning. To address this challenge, we introduce **Align-Then-stEer (\texttt{ATE})**, a novel, data-efficient, and plug-and-play adaptation framework. \texttt{ATE} first aligns disparate action spaces by constructing a unified latent space, where a variational autoencoder constrained by reverse KL divergence embeds adaptation actions into modes of the pre-training action latent distribution. Subsequently, it steers the diffusion- or flow-based VLA's generation process during fine-tuning via a guidance mechanism that pushes the model's output distribution towards the target domain. We conduct extensive experiments on cross-embodiment and cross-task manipulation in both simulation and real world. Compared to direct fine-tuning of representative VLAs, our method improves the average multi-task success rate by up to **9.8%** in simulation and achieves a striking **32% success rate gain** in a real-world cross-embodiment setting. Our work presents a general and lightweight solution that greatly enhances the practicality of deploying VLA models to new robotic platforms and tasks.

## Content
Vision-Language-Action (VLA) models pre-trained on large, diverse datasets show remarkable potential for general-purpose robotic manipulation. However, a primary bottleneck remains in adapting these models to downstream tasks, especially when the robot's embodiment or the task itself differs from the pre-training data. This discrepancy leads to a significant mismatch in action distributions, demanding extensive data and compute for effective fine-tuning. To address this challenge, we introduce **Align-Then-stEer (\texttt{ATE})**, a novel, data-efficient, and plug-and-play adaptation framework. \texttt{ATE} first aligns disparate action spaces by constructing a unified latent space, where a variational autoencoder constrained by reverse KL divergence embeds adaptation actions into modes of the pre-training action latent distribution. Subsequently, it steers the diffusion- or flow-based VLA's generation process during fine-tuning via a guidance mechanism that pushes the model's output distribution towards the target domain. We conduct extensive experiments on cross-embodiment and cross-task manipulation in both simulation and real world. Compared to direct fine-tuning of representative VLAs, our method improves the average multi-task success rate by up to **9.8%** in simulation and achieves a striking **32% success rate gain** in a real-world cross-embodiment setting. Our work presents a general and lightweight solution that greatly enhances the practicality of deploying VLA models to new robotic platforms and tasks.

## 개요
대규모 다양한 데이터셋으로 사전 학습된 Vision-Language-Action (VLA) 모델은 범용 로봇 조작에 놀라운 잠재력을 보여줍니다. 그러나 이러한 모델을 하위 작업에 적용하는 데 있어 주요 병목 현상은 여전히 존재하며, 특히 로봇의 구현 방식이나 작업 자체가 사전 학습 데이터와 다를 때 두드러집니다. 이러한 불일치는 행동 분포에 상당한 차이를 초래하여 효과적인 미세 조정을 위해 방대한 데이터와 계산 자원을 필요로 합니다. 이 문제를 해결하기 위해 우리는 \textbf{Align-Then-stEer (\texttt{ATE})}라는 새롭고 데이터 효율적이며 플러그 앤 플레이 방식의 적응 프레임워크를 소개합니다. \texttt{ATE}는 먼저 통합된 잠재 공간을 구축하여 서로 다른 행동 공간을 정렬합니다. 여기서 역 KL 발산으로 제약된 변분 오토인코더가 적응 행동을 사전 학습 행동 잠재 분포의 모드에 임베딩합니다. 그런 다음 미세 조정 중에 모델의 출력 분포를 대상 도메인으로 밀어내는 안내 메커니즘을 통해 확산 또는 흐름 기반 VLA의 생성 과정을 조정합니다. 우리는 시뮬레이션과 실제 환경 모두에서 교차 구현 및 교차 작업 조작에 대한 광범위한 실험을 수행했습니다. 대표적인 VLA의 직접 미세 조정과 비교하여, 우리 방법은 시뮬레이션에서 평균 다중 작업 성공률을 최대 \textbf{9.8\%} 향상시키고, 실제 교차 구현 환경에서 놀라운 \textbf{32\% 성공률 향상}을 달성했습니다. 우리의 연구는 새로운 로봇 플랫폼과 작업에 VLA 모델을 배포하는 실용성을 크게 향상시키는 일반적이고 가벼운 솔루션을 제시합니다.

## 핵심 내용
대규모 다양한 데이터셋으로 사전 학습된 Vision-Language-Action (VLA) 모델은 범용 로봇 조작에 놀라운 잠재력을 보여줍니다. 그러나 이러한 모델을 하위 작업에 적용하는 데 있어 주요 병목 현상은 여전히 존재하며, 특히 로봇의 구현 방식이나 작업 자체가 사전 학습 데이터와 다를 때 두드러집니다. 이러한 불일치는 행동 분포에 상당한 차이를 초래하여 효과적인 미세 조정을 위해 방대한 데이터와 계산 자원을 필요로 합니다. 이 문제를 해결하기 위해 우리는 \textbf{Align-Then-stEer (\texttt{ATE})}라는 새롭고 데이터 효율적이며 플러그 앤 플레이 방식의 적응 프레임워크를 소개합니다. \texttt{ATE}는 먼저 통합된 잠재 공간을 구축하여 서로 다른 행동 공간을 정렬합니다. 여기서 역 KL 발산으로 제약된 변분 오토인코더가 적응 행동을 사전 학습 행동 잠재 분포의 모드에 임베딩합니다. 그런 다음 미세 조정 중에 모델의 출력 분포를 대상 도메인으로 밀어내는 안내 메커니즘을 통해 확산 또는 흐름 기반 VLA의 생성 과정을 조정합니다. 우리는 시뮬레이션과 실제 환경 모두에서 교차 구현 및 교차 작업 조작에 대한 광범위한 실험을 수행했습니다. 대표적인 VLA의 직접 미세 조정과 비교하여, 우리 방법은 시뮬레이션에서 평균 다중 작업 성공률을 최대 \textbf{9.8\%} 향상시키고, 실제 교차 구현 환경에서 놀라운 \textbf{32\% 성공률 향상}을 달성했습니다. 우리의 연구는 새로운 로봇 플랫폼과 작업에 VLA 모델을 배포하는 실용성을 크게 향상시키는 일반적이고 가벼운 솔루션을 제시합니다.

## 参考
- http://arxiv.org/abs/2509.02055v2

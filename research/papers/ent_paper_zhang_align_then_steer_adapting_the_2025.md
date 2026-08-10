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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.02055v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (774 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2509.02055v2

## 개요
사전 훈련된 VLA 모델이 하위 작업에서 엔터티 또는 작업 차이로 인해 발생하는 동작 분포 불일치 문제를 해결하기 위해, ATE는 두 단계 솔루션을 제안한다: 먼저 변분 오토인코더(역방향 KL 발산 제약)를 통해 적응 동작을 사전 훈련된 동작 잠재 분포의 모드에 임베딩하여 통합 잠재 공간을 구축한다; 이후 미세 조정 단계에서 유도 메커니즘을 통해 모델 출력이 목표 도메인으로 이동하도록 유도한다. 실험 결과, 시뮬레이션 환경에서 ATE는 직접 미세 조정 방법에 비해 다중 작업 평균 성공률을 최대 9.8% 향상시켰으며, 실제 교차 엔터티 시나리오에서는 32%의 성공률 향상을 달성하여 VLA 모델 배포를 위한 경량화된 범용 솔루션을 제공한다.

## 핵심 내용
### 방법 아키텍처
- **정렬 단계(Align)**: 변분 오토인코더(VAE)를 활용하여 통합 잠재 공간을 구축하고, 역방향 KL 발산 제약을 통해 하위 작업의 적응 동작을 사전 훈련된 동작 잠재 분포의 모드에 임베딩하여 서로 다른 엔터티 또는 작업 간의 동작 공간 차이를 제거한다.
- **유도 단계(Steer)**: 확산 또는 흐름 기반 VLA 모델을 미세 조정할 때, 유도 메커니즘을 도입하여 모델 출력 분포가 목표 도메인으로 이동하도록 유도하며, 사전 훈련된 모델의 백본을 수정할 필요가 없다.

### 실험 설정
- **시뮬레이션 환경**: 여러 교차 엔터티(다양한 로봇 형태) 및 교차 작업(예: 파지, 적재) 조작 벤치마크를 기반으로 직접 미세 조정(Direct Fine-tuning)과 ATE 방법을 비교한다.
- **실제 시나리오**: 실제 로봇 플랫폼에서 교차 엔터티 조작 실험을 수행하여 ATE의 일반화 능력을 평가한다.

### 주요 결과
- **시뮬레이션 성능**: ATE는 다중 작업 평균 성공률을 최대 9.8% 향상시켰으며(직접 미세 조정 대비), 일부 작업에서는 성공률 절대값이 85%를 초과한다.
- **실제 시나리오**: 교차 엔터티 설정에서 ATE는 32%의 성공률 향상을 달성하여 기준 방법보다 현저히 우수하다.
- **데이터 효율성**: 소량의 목표 도메인 데이터만으로 적응이 가능하며, 대규모 재훈련이 필요하지 않다.

### 결론
ATE는 통합 잠재 공간 정렬과 유도 메커니즘을 통해 VLA 모델에 경량화되고 플러그 앤 플레이 방식의 적응 솔루션을 제공하여, 새로운 로봇 플랫폼과 작업에서의 배포 실용성을 크게 향상시킨다.

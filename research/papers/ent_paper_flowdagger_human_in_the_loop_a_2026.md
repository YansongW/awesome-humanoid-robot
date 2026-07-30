---
$id: ent_paper_flowdagger_human_in_the_loop_a_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FlowDAgger: Human-in-the-Loop Adaptation of Generative Robot Policies in Latent Space'
  zh: 'FlowDAgger: Human-in-the-Loop Adaptation of Generative Robot Policies in Latent Space'
  ko: 'FlowDAgger: Human-in-the-Loop Adaptation of Generative Robot Policies in Latent Space'
summary:
  en: 'arXiv:2607.08877v1 Announce Type: new Abstract: Pretrained generative robot policies based on flow matching and diffusion
    have achieved impressive results across a wide range of manipulation tasks. Yet real-world deployments routinely expose
    failure modes outside the pretraining distribution. Closing these gaps typically requires large-scale data collection
    or online reinforcement learning on physical hardware, which is impractical for rapid and safe adaptation. We present
    FlowDAgger, a sample- and compute-efficient method for adapting frozen generative robot policies from human interventions
    in latent space. Our key idea is action inversion: each human expert action is mapped to the noise that would have produced
    it under the frozen base policy, using reverse-time integration followed by local refinement. The resulting inverted noise
    provides supervision for a lightweight latent policy that steers the base model at deployment time, enabling rapid skill
    acquisition while preserving its behavioral priors. We evaluate FlowDAgger in simulation and on real-world bimanual and
    single-arm manipulation, adapting both action-head VLAs and world-action models from a handful of interventions. FlowDAgger
    outperforms supervised fine-tuning and latent-space RL baselines and preserves pretrained skills on held-out tasks, offering
    a practical path for adapting robot foundation models in the real world. Website: https://microsoft.github.io/FlowDAgger'
  zh: FlowDAgger 是微软提出的一种样本与计算高效的机器人策略适应方法，通过人类干预在潜空间中对冻结的生成式机器人策略进行适配。其核心创新是动作反演技术，将人类专家动作映射为冻结基策略下的噪声，从而训练轻量级潜策略来引导基模型，实现快速技能获取并保留预训练行为先验。在仿真和真实世界的双臂及单臂操作任务中，FlowDAgger
    优于监督微调和潜空间强化学习基线，并保持了对保留任务的预训练技能。
  ko: 'arXiv:2607.08877v1 Announce Type: new Abstract: Pretrained generative robot policies based on flow matching and diffusion
    have achieved impressive results across a wide range of manipulation tasks. Yet real-world deployments routinely expose
    failure modes outside the pretraining distribution. Closing these gaps typically requires large-scale data collection
    or online reinforcement learning on physical hardware, which is impractical for rapid and safe adaptation. We present
    FlowDAgger, a sample- and compute-efficient method for adapting frozen generative robot policies from human interventions
    in latent space. Our key idea is action inversion: each human expert action is mapped to the noise that would have produced
    it under the frozen base policy, using reverse-time integration followed by local refinement. The resulting inverted noise
    provides supervision for a lightweight latent policy that steers the base model at deployment time, enabling rapid skill
    acquisition while preserving its behavioral priors. We evaluate FlowDAgger in simulation and on real-world bimanual and
    single-arm manipulation, adapting both action-head VLAs and world-action models from a handful of interventions. FlowDAgger
    outperforms supervised fine-tuning and latent-space RL baselines and preserves pretrained skills on held-out tasks, offering
    a practical path for adapting robot foundation models in the real world. Website: https://microsoft.github.io/FlowDAgger'
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
- flowdagger
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.08877v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'FlowDAgger: Human-in-the-Loop Adaptation of Generative Robot Policies in Latent Space (arXiv)'
  url: https://arxiv.org/abs/2607.08877
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
FlowDAgger 针对预训练生成式机器人策略在真实部署中暴露的分布外失败模式，提出了一种无需大规模数据收集或在线强化学习的实用适应方案。该方法通过动作反演将人类干预动作转化为潜空间中的噪声监督信号，训练一个轻量级潜策略来在部署时调整基模型的行为。实验涵盖仿真和真实世界的双臂及单臂操作任务，适配了动作头视觉语言模型和世界动作模型，仅需少量人类干预即可实现高效适应。与监督微调和潜空间强化学习基线相比，FlowDAgger 在目标任务上表现更优，同时不损害基模型在保留任务上的预训练技能。

## 核心内容
### 方法核心
- **动作反演**：将每个人类专家动作通过逆向时间积分和局部细化，映射为冻结基策略下产生该动作的噪声。这一过程使得人类干预能够转化为潜空间中的监督信号。
- **轻量级潜策略**：基于反演得到的噪声训练一个轻量级潜策略，在部署时引导基模型的行为，实现快速技能获取的同时保留基模型的预训练行为先验。

### 实验设置
- **任务类型**：仿真和真实世界的双臂及单臂操作任务。
- **适配模型**：动作头视觉语言模型（action-head VLAs）和世界动作模型（world-action models）。
- **干预数量**：仅需少量人类干预即可完成适应。

### 关键结果
- **性能对比**：FlowDAgger 在目标任务上优于监督微调和潜空间强化学习基线。
- **技能保留**：在保留任务上，FlowDAgger 能够保持预训练技能，不会出现灾难性遗忘。
- **效率优势**：相比需要大规模数据收集或在线强化学习的方法，FlowDAgger 在样本和计算效率上显著提升。

### 结论
FlowDAgger 提供了一种实用的路径，通过人类干预在潜空间中适配机器人基础模型，兼顾了快速适应和技能保留，适用于真实世界的机器人部署场景。

## Overview
Pretrained generative robot policies based on flow matching and diffusion have achieved impressive results across a wide range of manipulation tasks. Yet real-world deployments routinely expose failure modes outside the pretraining distribution. Closing these gaps typically requires large-scale data collection or online reinforcement learning on physical hardware, which is impractical for rapid and safe adaptation. We present FlowDAgger, a sample- and compute-efficient method for adapting frozen generative robot policies from human interventions in latent space. Our key idea is action inversion: each human expert action is mapped to the noise that would have produced it under the frozen base policy, using reverse-time integration followed by local refinement. The resulting inverted noise provides supervision for a lightweight latent policy that steers the base model at deployment time, enabling rapid skill acquisition while preserving its behavioral priors. We evaluate FlowDAgger in simulation and on real-world bimanual and single-arm manipulation, adapting both action-head VLAs and world-action models from a handful of interventions. FlowDAgger outperforms supervised fine-tuning and latent-space RL baselines and preserves pretrained skills on held-out tasks, offering a practical path for adapting robot foundation models in the real world. Website: https://microsoft.github.io/FlowDAgger

## 개요
Flow 매칭 및 확산 기반의 사전 학습된 생성 로봇 정책은 다양한 조작 작업에서 인상적인 결과를 달성했습니다. 그러나 실제 환경 배포에서는 사전 학습 분포를 벗어난 실패 모드가 자주 발생합니다. 이러한 격차를 해소하려면 일반적으로 대규모 데이터 수집이나 물리적 하드웨어에서의 온라인 강화 학습이 필요하며, 이는 빠르고 안전한 적응에 비실용적입니다. 우리는 잠재 공간에서 인간의 개입을 통해 고정된 생성 로봇 정책을 적응시키는 샘플 및 계산 효율적인 방법인 FlowDAgger를 제시합니다. 핵심 아이디어는 행동 역전입니다. 각 인간 전문가 행동은 역방향 시간 적분과 국소 정제를 통해 고정된 기본 정책 하에서 이를 생성했을 노이즈에 매핑됩니다. 결과적으로 역전된 노이즈는 경량 잠재 정책에 대한 감독을 제공하여 배포 시 기본 모델을 조정하며, 행동 사전을 유지하면서 빠른 기술 습득을 가능하게 합니다. 우리는 시뮬레이션과 실제 양팔 및 단일 팔 조작에서 FlowDAgger를 평가하며, 소수의 개입으로 행동 헤드 VLA와 세계-행동 모델을 모두 적응시킵니다. FlowDAgger는 지도 미세 조정 및 잠재 공간 강화 학습 기준을 능가하며, 보류된 작업에서 사전 학습된 기술을 유지하여 실제 세계에서 로봇 기반 모델을 적응시키는 실용적인 경로를 제공합니다. 웹사이트: https://microsoft.github.io/FlowDAgger

## 핵심 내용
Flow 매칭 및 확산 기반의 사전 학습된 생성 로봇 정책은 다양한 조작 작업에서 인상적인 결과를 달성했습니다. 그러나 실제 환경 배포에서는 사전 학습 분포를 벗어난 실패 모드가 자주 발생합니다. 이러한 격차를 해소하려면 일반적으로 대규모 데이터 수집이나 물리적 하드웨어에서의 온라인 강화 학습이 필요하며, 이는 빠르고 안전한 적응에 비실용적입니다. 우리는 잠재 공간에서 인간의 개입을 통해 고정된 생성 로봇 정책을 적응시키는 샘플 및 계산 효율적인 방법인 FlowDAgger를 제시합니다. 핵심 아이디어는 행동 역전입니다. 각 인간 전문가 행동은 역방향 시간 적분과 국소 정제를 통해 고정된 기본 정책 하에서 이를 생성했을 노이즈에 매핑됩니다. 결과적으로 역전된 노이즈는 경량 잠재 정책에 대한 감독을 제공하여 배포 시 기본 모델을 조정하며, 행동 사전을 유지하면서 빠른 기술 습득을 가능하게 합니다. 우리는 시뮬레이션과 실제 양팔 및 단일 팔 조작에서 FlowDAgger를 평가하며, 소수의 개입으로 행동 헤드 VLA와 세계-행동 모델을 모두 적응시킵니다. FlowDAgger는 지도 미세 조정 및 잠재 공간 강화 학습 기준을 능가하며, 보류된 작업에서 사전 학습된 기술을 유지하여 실제 세계에서 로봇 기반 모델을 적응시키는 실용적인 경로를 제공합니다. 웹사이트: https://microsoft.github.io/FlowDAgger

## 参考
- http://arxiv.org/abs/2607.08877v1

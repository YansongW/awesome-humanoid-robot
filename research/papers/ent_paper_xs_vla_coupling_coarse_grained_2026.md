---
$id: ent_paper_xs_vla_coupling_coarse_grained_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'XS-VLA: Coupling Coarse-grained Spatial Distillation with Latent Flow Matching for Lightweight Robotic Control'
  zh: 'XS-VLA: Coupling Coarse-grained Spatial Distillation with Latent Flow Matching for Lightweight Robotic Control'
  ko: 'XS-VLA: Coupling Coarse-grained Spatial Distillation with Latent Flow Matching for Lightweight Robotic Control'
summary:
  en: 'arXiv:2607.04171v1 Announce Type: new Abstract: Large Vision-Language Models (LVLMs) have shown strong multimodal understanding
    and spatial grounding, but their computational cost limits real-time robotic control. In contrast, lightweight models
    are suitable for edge deployment but often suffer from "spatial blindness", namely weak native spatial prediction ability.
    Training Vision-Language-Action (VLA) models on mixed human demonstrations can also degrade policy performance due to
    highly diverse behaviors. To address these limitations, we propose XS-VLA, a two-stage framework for efficient and spatially
    grounded robotic manipulation. First, we distill spatial semantic knowledge from Qwen3-VL-4B into the SmolVLM2-0.25B backbone
    by fine-tuning on curated coarse-grained spatial descriptions, turning the lightweight model into a spatially grounded
    engine. Second, we use this enhanced backbone to condition a Latent Flow Matching policy. Unlike deterministic controllers,
    our policy combines a Conditional Variational Autoencoder (CVAE) with Flow Matching dynamics to model complex multimodal
    action distributions. On the LIBERO benchmark, XS-VLA achieves state-of-the-art performance among models with fewer than
    0.5B parameters. It improves average success rates by up to 7.2 percent, including a 23 percent gain on LIBERO-Long, over
    the SmolVLA 0.25B baseline, and outperforms the larger 2.2B vanilla SmolVLA. Ablations show that spatial tuning and generative
    latent flow control substantially improve lightweight VLA performance, delivering a 3.2 times speedup in mission execution
    over the previous lightweight flow matching policy.'
  zh: XS-VLA 是一个两阶段轻量级机器人操控框架，由研究团队提出，旨在解决轻量级模型的空间盲视问题。其核心贡献在于：通过粗粒度空间蒸馏将大模型的空间语义知识注入小模型，并利用潜流匹配策略建模多模态动作分布，在 LIBERO 基准上以低于
    0.5B 参数达到最优性能。
  ko: 'arXiv:2607.04171v1 Announce Type: new Abstract: Large Vision-Language Models (LVLMs) have shown strong multimodal understanding
    and spatial grounding, but their computational cost limits real-time robotic control. In contrast, lightweight models
    are suitable for edge deployment but often suffer from "spatial blindness", namely weak native spatial prediction ability.
    Training Vision-Language-Action (VLA) models on mixed human demonstrations can also degrade policy performance due to
    highly diverse behaviors. To address these limitations, we propose XS-VLA, a two-stage framework for efficient and spatially
    grounded robotic manipulation. First, we distill spatial semantic knowledge from Qwen3-VL-4B into the SmolVLM2-0.25B backbone
    by fine-tuning on curated coarse-grained spatial descriptions, turning the lightweight model into a spatially grounded
    engine. Second, we use this enhanced backbone to condition a Latent Flow Matching policy. Unlike deterministic controllers,
    our policy combines a Conditional Variational Autoencoder (CVAE) with Flow Matching dynamics to model complex multimodal
    action distributions. On the LIBERO benchmark, XS-VLA achieves state-of-the-art performance among models with fewer than
    0.5B parameters. It improves average success rates by up to 7.2 percent, including a 23 percent gain on LIBERO-Long, over
    the SmolVLA 0.25B baseline, and outperforms the larger 2.2B vanilla SmolVLA. Ablations show that spatial tuning and generative
    latent flow control substantially improve lightweight VLA performance, delivering a 3.2 times speedup in mission execution
    over the previous lightweight flow matching policy.'
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
- xs_vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04171v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'XS-VLA: Coupling Coarse-grained Spatial Distillation with Latent Flow Matching for Lightweight Robotic Control (arXiv)'
  url: https://arxiv.org/abs/2607.04171
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
大型视觉语言模型虽具备强大的多模态理解与空间定位能力，但计算成本过高，难以用于实时机器人控制。轻量级模型虽适合边缘部署，却常因空间预测能力弱而表现不佳。XS-VLA 框架分两步解决此问题：首先从 Qwen3-VL-4B 向 SmolVLM2-0.25B 蒸馏空间语义知识，使其具备空间感知能力；然后利用增强后的骨干网络驱动潜流匹配策略，该策略结合条件变分自编码器与流匹配动力学，能有效建模复杂多模态动作分布。在 LIBERO 基准上，XS-VLA 在参数少于 0.5B 的模型中达到最优，平均成功率提升最高 7.2%，其中 LIBERO-Long 任务提升 23%，甚至超越参数更大的 2.2B SmolVLA 模型。

## 核心内容
### 方法架构
XS-VLA 采用两阶段框架：
- **第一阶段：空间蒸馏**  
  从 Qwen3-VL-4B 教师模型向 SmolVLM2-0.25B 学生模型蒸馏空间语义知识。通过在精心筛选的粗粒度空间描述数据上微调，将轻量级模型转化为具备空间感知能力的引擎，解决其“空间盲视”问题。
- **第二阶段：潜流匹配策略**  
  利用增强后的骨干网络作为条件，驱动 Latent Flow Matching 策略。该策略结合 Conditional Variational Autoencoder (CVAE) 与 Flow Matching 动力学，能够建模复杂多模态动作分布，区别于传统确定性控制器。

### 实验设置与关键结果
- **基准测试**：在 LIBERO 基准上评估，包含多个任务场景。
- **性能对比**：
  - 在参数少于 0.5B 的模型中达到最优（state-of-the-art）。
  - 相比 SmolVLA 0.25B 基线，平均成功率提升最高 7.2%，其中 LIBERO-Long 任务提升 23%。
  - 超越参数更大的 2.2B 原始 SmolVLA 模型。
- **消融实验**：
  - 空间调优（spatial tuning）与生成式潜流控制（generative latent flow control）显著提升轻量级 VLA 性能。
  - 相比之前的轻量级流匹配策略，任务执行速度提升 3.2 倍。

### 结论
XS-VLA 通过粗粒度空间蒸馏与潜流匹配策略，有效解决了轻量级模型的空间盲视与多模态动作分布建模难题，在 LIBERO 基准上以极小参数规模取得领先性能，同时大幅提升执行效率。

## Overview
Large Vision-Language Models (LVLMs) have shown strong multimodal understanding and spatial grounding, but their computational cost limits real-time robotic control. In contrast, lightweight models are suitable for edge deployment but often suffer from "spatial blindness", namely weak native spatial prediction ability. Training Vision-Language-Action (VLA) models on mixed human demonstrations can also degrade policy performance due to highly diverse behaviors. To address these limitations, we propose XS-VLA, a two-stage framework for efficient and spatially grounded robotic manipulation. First, we distill spatial semantic knowledge from Qwen3-VL-4B into the SmolVLM2-0.25B backbone by fine-tuning on curated coarse-grained spatial descriptions, turning the lightweight model into a spatially grounded engine. Second, we use this enhanced backbone to condition a Latent Flow Matching policy. Unlike deterministic controllers, our policy combines a Conditional Variational Autoencoder (CVAE) with Flow Matching dynamics to model complex multimodal action distributions. On the LIBERO benchmark, XS-VLA achieves state-of-the-art performance among models with fewer than 0.5B parameters. It improves average success rates by up to 7.2 percent, including a 23 percent gain on LIBERO-Long, over the SmolVLA 0.25B baseline, and outperforms the larger 2.2B vanilla SmolVLA. Ablations show that spatial tuning and generative latent flow control substantially improve lightweight VLA performance, delivering a 3.2 times speedup in mission execution over the previous lightweight flow matching policy.

## 개요
대규모 시각-언어 모델(LVLMs)은 강력한 다중 모드 이해와 공간적 접지 능력을 보여주지만, 계산 비용으로 인해 실시간 로봇 제어에 한계가 있습니다. 반면, 경량 모델은 엣지 배포에 적합하지만 종종 "공간적 맹점", 즉 약한 고유 공간 예측 능력으로 인해 어려움을 겪습니다. 혼합된 인간 시연 데이터로 시각-언어-행동(VLA) 모델을 훈련하면 매우 다양한 행동으로 인해 정책 성능이 저하될 수도 있습니다. 이러한 한계를 해결하기 위해, 우리는 효율적이고 공간적으로 접지된 로봇 조작을 위한 2단계 프레임워크인 XS-VLA를 제안합니다. 첫째, 큐레이션된 조잡한 공간 설명에 대해 미세 조정을 통해 Qwen3-VL-4B의 공간 의미 지식을 SmolVLM2-0.25B 백본으로 증류하여 경량 모델을 공간적으로 접지된 엔진으로 전환합니다. 둘째, 이 강화된 백본을 사용하여 잠재 흐름 매칭 정책을 조건화합니다. 결정론적 제어기와 달리, 우리의 정책은 조건부 변분 오토인코더(CVAE)와 흐름 매칭 동역학을 결합하여 복잡한 다중 모드 행동 분포를 모델링합니다. LIBERO 벤치마크에서 XS-VLA는 0.5B 미만의 매개변수를 가진 모델 중 최고 성능을 달성합니다. SmolVLA 0.25B 기준선 대비 평균 성공률을 최대 7.2% 향상시키며, LIBERO-Long에서는 23% 향상을 포함하고, 더 큰 2.2B 바닐라 SmolVLA를 능가합니다. 절제 연구는 공간 튜닝과 생성적 잠재 흐름 제어가 경량 VLA 성능을 크게 향상시켜, 이전 경량 흐름 매칭 정책 대비 임무 실행에서 3.2배의 속도 향상을 제공함을 보여줍니다.

## 핵심 내용
대규모 시각-언어 모델(LVLMs)은 강력한 다중 모드 이해와 공간적 접지 능력을 보여주지만, 계산 비용으로 인해 실시간 로봇 제어에 한계가 있습니다. 반면, 경량 모델은 엣지 배포에 적합하지만 종종 "공간적 맹점", 즉 약한 고유 공간 예측 능력으로 인해 어려움을 겪습니다. 혼합된 인간 시연 데이터로 시각-언어-행동(VLA) 모델을 훈련하면 매우 다양한 행동으로 인해 정책 성능이 저하될 수도 있습니다. 이러한 한계를 해결하기 위해, 우리는 효율적이고 공간적으로 접지된 로봇 조작을 위한 2단계 프레임워크인 XS-VLA를 제안합니다. 첫째, 큐레이션된 조잡한 공간 설명에 대해 미세 조정을 통해 Qwen3-VL-4B의 공간 의미 지식을 SmolVLM2-0.25B 백본으로 증류하여 경량 모델을 공간적으로 접지된 엔진으로 전환합니다. 둘째, 이 강화된 백본을 사용하여 잠재 흐름 매칭 정책을 조건화합니다. 결정론적 제어기와 달리, 우리의 정책은 조건부 변분 오토인코더(CVAE)와 흐름 매칭 동역학을 결합하여 복잡한 다중 모드 행동 분포를 모델링합니다. LIBERO 벤치마크에서 XS-VLA는 0.5B 미만의 매개변수를 가진 모델 중 최고 성능을 달성합니다. SmolVLA 0.25B 기준선 대비 평균 성공률을 최대 7.2% 향상시키며, LIBERO-Long에서는 23% 향상을 포함하고, 더 큰 2.2B 바닐라 SmolVLA를 능가합니다. 절제 연구는 공간 튜닝과 생성적 잠재 흐름 제어가 경량 VLA 성능을 크게 향상시켜, 이전 경량 흐름 매칭 정책 대비 임무 실행에서 3.2배의 속도 향상을 제공함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2607.04171v1

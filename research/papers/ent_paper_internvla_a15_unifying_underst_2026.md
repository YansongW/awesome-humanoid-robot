---
$id: ent_paper_internvla_a15_unifying_underst_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'InternVLA-A1.5: Unifying Understanding, Latent Foresight, and Action for Compositional Generalization'
  zh: 'InternVLA-A1.5: Unifying Understanding, Latent Foresight, and Action for Compositional Generalization'
  ko: 'InternVLA-A1.5: Unifying Understanding, Latent Foresight, and Action for Compositional Generalization'
summary:
  en: 'arXiv:2607.04988v1 Announce Type: new Abstract: Unified models for robot manipulation aim to equip one policy with
    both the semantic priors of pretrained VLMs and the physical dynamics learned through future prediction. In practice,
    existing designs tend to erode the semantics of the pretrained backbone, suffer interference among heterogeneous objectives,
    and learn future prediction from scratch in pixel space, leaving the dynamics priors of pretrained video generators unexploited.
    We present InternVLA-A1.5, which builds the policy on a native VLM backbone that keeps training on VQA and subtask prediction,
    and attaches a lightweight unified expert for continuous action generation. Future prediction is recast as a latent-querying
    problem, where a small set of learnable foresight tokens condenses the task-relevant future into a compact latent code
    under the supervision of a frozen pretrained video generation model, so the policy inherits world-model dynamics priors
    without ever learning pixel-level generation. The video branch is discarded at inference, keeping real-time control. Pretrained
    on 1.2M robot episodes and 3M multimodal samples, InternVLA-A1.5 achieves the best overall results on all six simulation
    benchmarks. In the real world, the preserved semantics deliver the strongest compositional generalization on held-out
    instruction bindings, and the two designs together sustain long-horizon execution.'
  zh: InternVLA-A1.5 是一个面向机器人操作的统一模型，由上海人工智能实验室等机构提出。其核心贡献在于将未来预测重构为潜在查询问题，利用冻结的预训练视频生成模型监督可学习的“预见令牌”，在不学习像素级生成的前提下继承世界模型动力学先验。该模型在全部六个仿真基准上取得最佳综合结果，并在真实世界中展现出最强的组合泛化能力。
  ko: 'arXiv:2607.04988v1 Announce Type: new Abstract: Unified models for robot manipulation aim to equip one policy with
    both the semantic priors of pretrained VLMs and the physical dynamics learned through future prediction. In practice,
    existing designs tend to erode the semantics of the pretrained backbone, suffer interference among heterogeneous objectives,
    and learn future prediction from scratch in pixel space, leaving the dynamics priors of pretrained video generators unexploited.
    We present InternVLA-A1.5, which builds the policy on a native VLM backbone that keeps training on VQA and subtask prediction,
    and attaches a lightweight unified expert for continuous action generation. Future prediction is recast as a latent-querying
    problem, where a small set of learnable foresight tokens condenses the task-relevant future into a compact latent code
    under the supervision of a frozen pretrained video generation model, so the policy inherits world-model dynamics priors
    without ever learning pixel-level generation. The video branch is discarded at inference, keeping real-time control. Pretrained
    on 1.2M robot episodes and 3M multimodal samples, InternVLA-A1.5 achieves the best overall results on all six simulation
    benchmarks. In the real world, the preserved semantics deliver the strongest compositional generalization on held-out
    instruction bindings, and the two designs together sustain long-horizon execution.'
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
- internvla_a15
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04988v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'InternVLA-A1.5: Unifying Understanding, Latent Foresight, and Action for Compositional Generalization (arXiv)'
  url: https://arxiv.org/abs/2607.04988
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
InternVLA-A1.5 旨在解决现有统一模型在融合视觉语言模型语义先验与物理动力学时面临的语义侵蚀、目标干扰及像素空间未来预测效率低等问题。该模型基于原生 VLM 骨干网络，持续进行 VQA 和子任务预测训练，并附加轻量级统一专家模块用于连续动作生成。未来预测被重新定义为潜在查询任务，通过一组可学习的“预见令牌”在冻结的预训练视频生成模型监督下，将任务相关未来压缩为紧凑的潜在代码，从而继承世界模型动力学先验。推理时丢弃视频分支以保持实时控制，模型在 120 万机器人片段和 300 万多模态样本上预训练后，在六个仿真基准上均取得最佳结果，并在真实世界中展现出强大的组合泛化与长时程执行能力。

## 核心内容
### 方法架构
- **骨干网络**：基于原生 VLM 骨干，持续进行 VQA 和子任务预测训练，保留语义先验。
- **动作生成**：附加轻量级统一专家模块，用于连续动作生成，避免异构目标干扰。
- **未来预测**：将未来预测重构为潜在查询问题，使用一组可学习的“预见令牌”在冻结的预训练视频生成模型监督下，将任务相关未来压缩为紧凑潜在代码，无需学习像素级生成。
- **推理优化**：推理时丢弃视频分支，保持实时控制。

### 实验设置
- **预训练数据**：120 万机器人操作片段和 300 万多模态样本。
- **仿真基准**：在全部六个仿真基准上进行评估，包括组合泛化与长时程任务。
- **真实世界测试**：评估保留语义在未见指令绑定上的组合泛化能力，以及两个设计共同支撑的长时程执行效果。

### 关键结果
- **仿真性能**：在所有六个仿真基准上取得最佳综合结果。
- **真实世界表现**：保留的语义在未见指令绑定上展现出最强的组合泛化能力；未来预测与语义保留设计共同支撑长时程执行。

### 结论
InternVLA-A1.5 通过将未来预测重构为潜在查询问题，有效利用预训练视频生成模型的动力学先验，避免了像素级生成的学习开销，同时保持实时控制。该模型在仿真和真实世界中均展现出优异的组合泛化与长时程执行能力。

## Overview
Unified models for robot manipulation aim to equip one policy with both the semantic priors of pretrained VLMs and the physical dynamics learned through future prediction. In practice, existing designs tend to erode the semantics of the pretrained backbone, suffer interference among heterogeneous objectives, and learn future prediction from scratch in pixel space, leaving the dynamics priors of pretrained video generators unexploited. We present InternVLA-A1.5, which builds the policy on a native VLM backbone that keeps training on VQA and subtask prediction, and attaches a lightweight unified expert for continuous action generation. Future prediction is recast as a latent-querying problem, where a small set of learnable foresight tokens condenses the task-relevant future into a compact latent code under the supervision of a frozen pretrained video generation model, so the policy inherits world-model dynamics priors without ever learning pixel-level generation. The video branch is discarded at inference, keeping real-time control. Pretrained on 1.2M robot episodes and 3M multimodal samples, InternVLA-A1.5 achieves the best overall results on all six simulation benchmarks. In the real world, the preserved semantics deliver the strongest compositional generalization on held-out instruction bindings, and the two designs together sustain long-horizon execution.

## 개요
로봇 조작을 위한 통합 모델은 사전 훈련된 VLM의 의미적 사전 지식과 미래 예측을 통해 학습된 물리적 동역학을 하나의 정책에 탑재하는 것을 목표로 합니다. 실제로 기존 설계는 사전 훈련된 백본의 의미를 약화시키고, 이질적인 목표 간 간섭을 겪으며, 픽셀 공간에서 처음부터 미래 예측을 학습하여 사전 훈련된 비디오 생성기의 동역학 사전 지식을 활용하지 못하는 경향이 있습니다. 우리는 InternVLA-A1.5를 제시합니다. 이는 VQA 및 하위 작업 예측에 대해 지속적으로 훈련되는 네이티브 VLM 백본 위에 정책을 구축하고, 연속 동작 생성을 위한 경량 통합 전문가를 부착합니다. 미래 예측은 잠재 질의 문제로 재구성되며, 소수의 학습 가능한 예견 토큰이 동결된 사전 훈련된 비디오 생성 모델의 감독 하에 작업 관련 미래를 컴팩트한 잠재 코드로 압축하여, 정책이 픽셀 수준 생성을 학습하지 않고도 세계 모델 동역학 사전 지식을 상속받습니다. 비디오 분기는 추론 시 폐기되어 실시간 제어를 유지합니다. 120만 개의 로봇 에피소드와 300만 개의 멀티모달 샘플로 사전 훈련된 InternVLA-A1.5는 6개의 시뮬레이션 벤치마크 모두에서 최고의 종합 결과를 달성합니다. 실제 세계에서는 보존된 의미가 보류된 명령 바인딩에서 가장 강력한 구성적 일반화를 제공하며, 두 설계가 함께 장기 실행을 유지합니다.

## 핵심 내용
로봇 조작을 위한 통합 모델은 사전 훈련된 VLM의 의미적 사전 지식과 미래 예측을 통해 학습된 물리적 동역학을 하나의 정책에 탑재하는 것을 목표로 합니다. 실제로 기존 설계는 사전 훈련된 백본의 의미를 약화시키고, 이질적인 목표 간 간섭을 겪으며, 픽셀 공간에서 처음부터 미래 예측을 학습하여 사전 훈련된 비디오 생성기의 동역학 사전 지식을 활용하지 못하는 경향이 있습니다. 우리는 InternVLA-A1.5를 제시합니다. 이는 VQA 및 하위 작업 예측에 대해 지속적으로 훈련되는 네이티브 VLM 백본 위에 정책을 구축하고, 연속 동작 생성을 위한 경량 통합 전문가를 부착합니다. 미래 예측은 잠재 질의 문제로 재구성되며, 소수의 학습 가능한 예견 토큰이 동결된 사전 훈련된 비디오 생성 모델의 감독 하에 작업 관련 미래를 컴팩트한 잠재 코드로 압축하여, 정책이 픽셀 수준 생성을 학습하지 않고도 세계 모델 동역학 사전 지식을 상속받습니다. 비디오 분기는 추론 시 폐기되어 실시간 제어를 유지합니다. 120만 개의 로봇 에피소드와 300만 개의 멀티모달 샘플로 사전 훈련된 InternVLA-A1.5는 6개의 시뮬레이션 벤치마크 모두에서 최고의 종합 결과를 달성합니다. 실제 세계에서는 보존된 의미가 보류된 명령 바인딩에서 가장 강력한 구성적 일반화를 제공하며, 두 설계가 함께 장기 실행을 유지합니다.

## 参考
- http://arxiv.org/abs/2607.04988v1

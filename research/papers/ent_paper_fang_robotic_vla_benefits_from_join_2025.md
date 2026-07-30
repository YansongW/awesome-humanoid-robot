---
$id: ent_paper_fang_robotic_vla_benefits_from_join_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robotic VLA Benefits from Joint Learning with Motion Image Diffusion
  zh: Robotic VLA Benefits from Joint Learning with Motion Image Diffusion
  ko: Robotic VLA Benefits from Joint Learning with Motion Image Diffusion
summary:
  en: Robotic VLA Benefits from Joint Learning with Motion Image Diffusion (Robotic VLA Benefits from Joint Learning with
    Motion Image Diffusion), is a 2025 large vision-language-action model for robotic manipulation, introduced by Salesforce,
    Stanford University.
  zh: Salesforce与斯坦福大学于2025年提出一种联合运动图像扩散的VLA模型，通过双头架构（动作头+运动头）增强机器人操作中的运动推理能力。该方法在LIBERO基准上达到97.5%成功率，在RoboTwin基准上达到58.0%，真实环境性能提升23%。
  ko: Robotic VLA Benefits from Joint Learning with Motion Image Diffusion (Robotic VLA Benefits from Joint Learning with
    Motion Image Diffusion), is a 2025 large vision-language-action model for robotic manipulation, introduced by Salesforce,
    Stanford University.
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
- robotic_manipulation
- robotic_vla_benefits_from_join
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.18007v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Robotic VLA Benefits from Joint Learning with Motion Image Diffusion (arXiv)
  url: https://arxiv.org/abs/2512.18007
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Robotic VLA Benefits from Joint Learning with Motion Image Diffusion source
  url: https://doi.org/10.48550/arXiv.2512.18007
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有VLA模型直接模仿专家轨迹，缺乏对动作后果的预测性推理。本研究提出联合学习策略，在标准VLA架构中增加基于Diffusion Transformer的运动头，用于预测光流运动图像。双头联合训练使共享的VLM骨干网络同时学习控制与运动知识，构建时间连贯且物理可解释的表征。该方法不改变标准VLA的推理路径，保持测试时延不变，在仿真与真实实验中均显著提升成功率。

## 核心内容
### 方法架构
- **双头设计**：在标准VLA的动作头（预测动作块）基础上，增加运动头（基于DiT）预测光流运动图像，捕捉未来动态。
- **联合训练**：两个头共享VLM骨干网络，通过联合损失函数训练，使表征同时耦合机器人控制与运动知识。
- **推理不变性**：测试时仅使用动作头，运动头仅用于训练阶段，不增加推理延迟。

### 实验设置
- **基准测试**：LIBERO（仿真）、RoboTwin（仿真）、真实机器人操作任务。
- **基线模型**：pi-series VLA（无运动头版本）。
- **评估指标**：任务成功率（%）。

### 关键结果
- **LIBERO基准**：成功率从基线提升至97.5%。
- **RoboTwin基准**：成功率从基线提升至58.0%。
- **真实环境**：性能提升23%，验证运动推理能力增强的有效性。

### 结论
联合运动图像扩散学习显著提升VLA模型的运动推理能力，在不增加推理成本的前提下实现性能突破，为大规模VLA模型提供可扩展的增强方案。

## Overview
Vision-Language-Action (VLA) models have achieved remarkable progress in robotic manipulation by mapping multimodal observations and instructions directly to actions. However, they typically mimic expert trajectories without predictive motion reasoning, which limits their ability to reason about what actions to take. To address this limitation, we propose joint learning with motion image diffusion, a novel strategy that enhances VLA models with motion reasoning capabilities. Our method extends the VLA architecture with a dual-head design: while the action head predicts action chunks as in vanilla VLAs, an additional motion head, implemented as a Diffusion Transformer (DiT), predicts optical-flow-based motion images that capture future dynamics. The two heads are trained jointly, enabling the shared VLM backbone to learn representations that couple robot control with motion knowledge. This joint learning builds temporally coherent and physically grounded representations without modifying the inference pathway of standard VLAs, thereby maintaining test-time latency. Experiments in both simulation and real-world environments demonstrate that joint learning with motion image diffusion improves the success rate of pi-series VLAs to 97.5% on the LIBERO benchmark and 58.0% on the RoboTwin benchmark, yielding a 23% improvement in real-world performance and validating its effectiveness in enhancing the motion reasoning capability of large-scale VLAs.

## 개요
Vision-Language-Action (VLA) 모델은 다중 모달 관찰과 명령을 직접 행동으로 매핑하여 로봇 조작 분야에서 놀라운 진전을 이루었습니다. 그러나 이러한 모델은 일반적으로 예측적 움직임 추론 없이 전문가 궤적을 모방하므로, 어떤 행동을 취해야 하는지 추론하는 능력이 제한됩니다. 이러한 한계를 해결하기 위해, 우리는 움직임 이미지 확산을 통한 공동 학습(joint learning with motion image diffusion)이라는 새로운 전략을 제안하며, 이는 VLA 모델에 움직임 추론 능력을 부여합니다. 우리의 방법은 이중 헤드(dual-head) 설계로 VLA 아키텍처를 확장합니다: 액션 헤드는 기본 VLA와 같이 행동 청크(action chunks)를 예측하는 반면, 확산 트랜스포머(Diffusion Transformer, DiT)로 구현된 추가적인 움직임 헤드는 미래 역학을 포착하는 광학 흐름 기반 움직임 이미지를 예측합니다. 두 헤드는 공동으로 훈련되어, 공유된 VLM 백본이 로봇 제어와 움직임 지식을 결합한 표현을 학습할 수 있게 합니다. 이 공동 학습은 표준 VLA의 추론 경로를 수정하지 않고 시간적으로 일관되고 물리적으로 기반을 둔 표현을 구축하여, 테스트 시 지연 시간을 유지합니다. 시뮬레이션 및 실제 환경 모두에서의 실험은 움직임 이미지 확산을 통한 공동 학습이 pi-시리즈 VLA의 성공률을 LIBERO 벤치마크에서 97.5%, RoboTwin 벤치마크에서 58.0%로 향상시키며, 실제 환경 성능에서 23%의 개선을 가져와 대규모 VLA의 움직임 추론 능력을 향상시키는 효과를 입증합니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 다중 모달 관찰과 명령을 직접 행동으로 매핑하여 로봇 조작 분야에서 놀라운 진전을 이루었습니다. 그러나 이러한 모델은 일반적으로 예측적 움직임 추론 없이 전문가 궤적을 모방하므로, 어떤 행동을 취해야 하는지 추론하는 능력이 제한됩니다. 이러한 한계를 해결하기 위해, 우리는 움직임 이미지 확산을 통한 공동 학습(joint learning with motion image diffusion)이라는 새로운 전략을 제안하며, 이는 VLA 모델에 움직임 추론 능력을 부여합니다. 우리의 방법은 이중 헤드(dual-head) 설계로 VLA 아키텍처를 확장합니다: 액션 헤드는 기본 VLA와 같이 행동 청크(action chunks)를 예측하는 반면, 확산 트랜스포머(Diffusion Transformer, DiT)로 구현된 추가적인 움직임 헤드는 미래 역학을 포착하는 광학 흐름 기반 움직임 이미지를 예측합니다. 두 헤드는 공동으로 훈련되어, 공유된 VLM 백본이 로봇 제어와 움직임 지식을 결합한 표현을 학습할 수 있게 합니다. 이 공동 학습은 표준 VLA의 추론 경로를 수정하지 않고 시간적으로 일관되고 물리적으로 기반을 둔 표현을 구축하여, 테스트 시 지연 시간을 유지합니다. 시뮬레이션 및 실제 환경 모두에서의 실험은 움직임 이미지 확산을 통한 공동 학습이 pi-시리즈 VLA의 성공률을 LIBERO 벤치마크에서 97.5%, RoboTwin 벤치마크에서 58.0%로 향상시키며, 실제 환경 성능에서 23%의 개선을 가져와 대규모 VLA의 움직임 추론 능력을 향상시키는 효과를 입증합니다.

## 参考
- http://arxiv.org/abs/2512.18007v1

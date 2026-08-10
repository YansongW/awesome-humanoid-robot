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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.18007v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (657 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2512.18007v1

## 개요
기존 VLA 모델은 전문가 궤적을 직접 모방하며, 행동 결과에 대한 예측적 추론이 부족하다. 본 연구는 표준 VLA 아키텍처에 Diffusion Transformer 기반 모션 헤드를 추가하여 광학 흐름 모션 이미지를 예측하는 공동 학습 전략을 제안한다. 이중 헤드 공동 훈련을 통해 공유된 VLM 백본 네트워크가 제어 지식과 모션 지식을 동시에 학습하여 시간적으로 일관되고 물리적으로 해석 가능한 표현을 구축한다. 이 방법은 표준 VLA의 추론 경로를 변경하지 않아 테스트 지연 시간을 유지하며, 시뮬레이션 및 실제 실험 모두에서 성공률을 크게 향상시킨다.

## 핵심 내용
### 방법 아키텍처
- **이중 헤드 설계**: 표준 VLA의 액션 헤드(액션 블록 예측)에 더해, DiT 기반 모션 헤드를 추가하여 광학 흐름 모션 이미지를 예측하고 미래 동역학을 포착한다.
- **공동 훈련**: 두 헤드가 VLM 백본 네트워크를 공유하며, 공동 손실 함수로 훈련하여 표현이 로봇 제어와 모션 지식을 동시에 결합하도록 한다.
- **추론 불변성**: 테스트 시 액션 헤드만 사용하고, 모션 헤드는 훈련 단계에서만 사용되므로 추론 지연 시간이 증가하지 않는다.

### 실험 설정
- **벤치마크 테스트**: LIBERO(시뮬레이션), RoboTwin(시뮬레이션), 실제 로봇 조작 작업.
- **기준 모델**: pi-series VLA(모션 헤드 없는 버전).
- **평가 지표**: 작업 성공률(%).

### 주요 결과
- **LIBERO 벤치마크**: 성공률이 기준 대비 97.5%로 향상.
- **RoboTwin 벤치마크**: 성공률이 기준 대비 58.0%로 향상.
- **실제 환경**: 성능이 23% 향상되어 모션 추론 능력 강화의 효과를 검증.

### 결론
공동 모션 이미지 확산 학습은 VLA 모델의 모션 추론 능력을 크게 향상시키며, 추론 비용 증가 없이 성능 돌파구를 달성하여 대규모 VLA 모델에 확장 가능한 강화 방안을 제공한다.

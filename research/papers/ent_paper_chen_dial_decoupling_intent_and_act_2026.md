---
$id: ent_paper_chen_dial_decoupling_intent_and_act_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DIAL: Decoupling Intent and Action via Latent World Modeling for End-to-End
    VLA'
  zh: DIAL：通过潜在世界建模解耦意图与行动的端到端视觉-语言-行动模型
  ko: 'DIAL: 잠재 세계 모델링을 통한 의도와 행동의 분리를 위한 종단형 VLA'
summary:
  en: DIAL introduces a dual-system VLA architecture that uses a VLM-based System-2
    for latent visual foresight and a lightweight System-1 policy for latent inverse
    dynamics, achieving state-of-the-art data efficiency on RoboCasa GR1 Tabletop
    and real-world deployment on the IRON-R01-1.11 humanoid robot.
  zh: DIAL提出了一种双系统VLA架构，利用基于VLM的System-2进行潜在视觉预见，并由轻量级System-1策略通过潜在逆动力学解码动作，在RoboCasa
    GR1 Tabletop基准上实现了最先进的数据效率，并在IRON-R01-1.11人形机器人上完成了真实世界部署。
  ko: DIAL은 VLM 기반 System-2를 활용한 잠재적 시각적 예측과 가벼운 System-1 정책을 통한 잠재 역역학으로 행동을 디코딩하는
    이중 시스템 VLA 아키텍처를 제안하여 RoboCasa GR1 Tabletop 벤치마크에서 최첨단 데이터 효율성을 달성하고 IRON-R01-1.11
    휴머노이드 로봇에서 실제 세계 배포를 수행했다.
domains:
- 07_ai_models_algorithms
- 10_evaluation_benchmarks
- 02_components
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- intelligence
- knowledge
tags:
- vla
- vision_language_action
- latent_world_modeling
- latent_inverse_dynamics
- system_2_system_1
- humanoid_manipulation
- gr1
- iron_r01
- qwen2_5_vl
- robocasa
- data_efficiency
- zero_shot_generalization
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review against
    full paper before promotion to verified.
sources:
- id: src_001
  type: paper
  title: 'DIAL: Decoupling Intent and Action via Latent World Modeling for End-to-End
    VLA'
  url: https://arxiv.org/abs/2603.29844
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## Overview

DIAL (Decoupling Intent and Action via Latent World Modeling) is an end-to-end Vision-Language-Action (VLA) framework that addresses the limitations of existing VLAs which treat Vision-Language Models (VLMs) primarily as multimodal encoders. Instead of directly mapping vision-language features to low-level actions, DIAL introduces a differentiable latent intent bottleneck that separates high-level decision making from low-level motor execution. A VLM-based System-2 performs latent world modeling by synthesizing future visual features within the native feature space of the VLM's vision encoder, explicitly encoding the model's intent. A lightweight System-1 policy then decodes this predicted intent together with the current observation into precise robot actions through latent inverse dynamics.

To ensure stable optimization, DIAL employs a two-stage training paradigm. The first stage is a decoupled warmup phase in which System-2 learns to predict latent futures while System-1 learns motor control under ground-truth future guidance within a unified feature space. The second stage transitions to seamless end-to-end joint optimization, allowing action-aware gradients to refine the VLM backbone in a controlled manner while preserving its pre-trained knowledge. The framework is instantiated with Qwen2.5-VL-3B as the VLM backbone, a Vision Transformer (ViT) as the vision encoder, and a Diffusion Transformer (DiT) as the System-1 policy.

## Key Contributions

- Novel dual-system VLA architecture with a differentiable latent visual foresight bottleneck that structurally grounds actions in the VLM's intent.
- Decoupled-to-unified training paradigm that independently warms up System-2 foresight and System-1 motor control before stable end-to-end joint optimization.
- State-of-the-art data efficiency on RoboCasa GR1 Tabletop using 10× fewer demonstrations and strong scalability via cross-embodiment human data.
- Real-world deployment on the IRON-R01-1.11 humanoid robot demonstrating robust zero-shot generalization and multi-stage coordination.

## Relevance to Humanoid Robotics

DIAL is directly relevant to humanoid robotics because it is explicitly evaluated on the humanoid GR1 simulation benchmark and deployed on the real-world IRON-R01-1.11 humanoid robot. The paper reports that DIAL learns physically grounded manipulation priors from heterogeneous human demonstrations and exhibits robust zero-shot generalization to unseen objects and novel configurations during real-world deployment. This demonstrates a pathway for data-efficient, end-to-end VLA learning on humanoid platforms for manipulation and multi-stage coordination tasks.

The work also contributes to the components and evaluation domains by providing a concrete algorithmic instantiation that combines a general-purpose VLM (Qwen2.5-VL-3B) with humanoid-specific benchmarks and hardware. Its emphasis on preserving pre-trained semantic representations while enabling action-aware fine-tuning is particularly important for humanoid robots, which must handle diverse, language-conditioned manipulation tasks in open-world environments.

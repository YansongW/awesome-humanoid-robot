---
$id: ent_formalism_transformer_action_decoder
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: formalism
names:
  en: Transformer Action Decoder Formalism
  zh: Transformer 动作解码器形式化
  ko: Transformer 액션 디코더 공식화
summary:
  en: A formal generative framework that decodes robot actions from visual-language context using a Transformer architecture and a learned action token vocabulary.
  zh: 一种使用 Transformer 架构和学习的动作 token 词表，从视觉-语言上下文解码机器人动作的形式化生成框架。
  ko: Transformer 아키텍처와 학습된 액션 토큰 어휘를 사용하여 시각-언어 맥락에서 로봇 동작을 디코딩하는 공식적 생성 프레임워크이다.
domains:
- 07_ai_models_algorithms
- 00_foundations
layers:
- intelligence
- foundations
functional_roles:
- intelligence
- knowledge
tags:
- vla
- transformer
- action_decoder
- autoregressive_generation
- humanoid_robot
theoretical_depth:
- formalism
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Common abstraction across VLAs such as OpenVLA, RT-2, and π0.
sources:
- id: src_vaswani_2017
  type: paper
  title: 'Vaswani et al., Attention Is All You Need, NeurIPS 2017'
  url: https://arxiv.org/abs/1706.03762
  date: '2017-06-12'
  accessed_at: '2026-06-26'
- id: src_openvla_2024
  type: paper
  title: 'OpenVLA: An Open-Source Vision-Language-Action Model'
  url: https://arxiv.org/abs/2406.09246
  date: '2024-06-13'
  accessed_at: '2026-06-26'
related_entities:
- id: ent_self_attention_equation
  relationship: includes
  description:
    en: The Transformer action decoder includes scaled dot-product self-attention.
    zh: Transformer 动作解码器包含缩放点积自注意力。
    ko: Transformer 액션 디코더는 스케일드 닷프로덕트 셀프 어텐션을 포함한다.
- id: ent_foundation_linear_algebra
  relationship: has_prerequisite
  description:
    en: The decoder's matrix operations and attention mechanics rest on linear algebra.
    zh: 解码器的矩阵运算和注意力机制以线性代数为基础。
    ko: 디코더의 행렬 연산과 어텐션 메커니즘은 선형대수학에 기반한다.
---

## 抽象

> **生活实例**：想象一个同声传译员，她一边听演讲（视觉-语言上下文），一边逐字输出翻译（动作 token）。Transformer 动作解码器形式化就是这位译员的工作流程：用注意力机制“听”上下文，再一个 token 一个 token 地“说”出动作。
>
> **自然语言逻辑**：把动作生成看作条件生成问题；Transformer 编码器处理视觉和语言输入，解码器通过自回归方式预测动作 token 序列；softmax 输出在动作词表上的概率分布。

## Overview

The Transformer action-decoder formalism unifies perception, language, and control in VLAs. It treats robot actions as a sequence of tokens and models the conditional distribution \(P(a_1, \dots, a_T \mid \text{image}, \text{text})\) using a Transformer. During inference, action tokens are sampled or greedily decoded and then mapped back to continuous motor commands.

## Key Characteristics

- Visual and language inputs are encoded into a shared context representation.
- The decoder is autoregressive, predicting each action token conditioned on previous tokens and context.
- Self-attention captures long-range dependencies across the action sequence.
- Output logits are converted to action tokens via argmax or sampling.

## Relevance to Humanoid Robotics

Humanoid actions are high-dimensional and temporally extended. The Transformer action decoder provides a principled way to model these dependencies while leveraging pretrained vision-language backbones, making it a key formalism for whole-body humanoid VLAs.

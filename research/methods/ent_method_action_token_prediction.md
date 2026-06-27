---
$id: ent_method_action_token_prediction
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Action Token Prediction
  zh: 动作 token 预测
  ko: 액션 토큰 예측
summary:
  en: A method that frames robot action generation as an autoregressive next-token prediction problem, mirroring language modeling but outputting discretized or continuous action tokens.
  zh: 一种将机器人动作生成建模为自回归“下一个 token 预测”问题的方法，类似于语言建模，但输出离散或连续的动作 token。
  ko: 언어 모델링과 유사하지만 이산적 또는 연속적인 액션 토큰을 출력하는 자기회귀적 다음 토큰 예측 문제로 로봇 동작 생성을 구성하는 방법이다.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- intelligence
- knowledge
tags:
- vla
- action_token
- autoregressive_modeling
- next_token_prediction
- humanoid_robot
theoretical_depth:
- method
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Core mechanism in modern VLAs such as OpenVLA and RT-2.
sources:
- id: src_openvla_2024
  type: paper
  title: 'OpenVLA: An Open-Source Vision-Language-Action Model'
  url: https://arxiv.org/abs/2406.09246
  date: '2024-06-13'
  accessed_at: '2026-06-26'
related_entities:
- id: ent_formalism_transformer_action_decoder
  relationship: formalizes
  description:
    en: Action token prediction instantiates a Transformer action-decoder formalism.
    zh: 动作 token 预测实例化了 Transformer 动作解码器的形式化。
    ko: 액션 토큰 예측은 Transformer 액션 디코더 공식화를 구현한다.
- id: ent_foundation_linear_algebra
  relationship: has_prerequisite
  description:
    en: Action token prediction relies on linear-algebraic operations inside the Transformer.
    zh: 动作 token 预测依赖 Transformer 内部的线性代数运算。
    ko: 액션 토큰 예측은 Transformer 낶부의 선형대수학 연산에 의존한다.
---

## 抽象

> **生活实例**：想象你教一个 apprentice 做菜，你每次只说“下一步该做什么”，比如“切洋葱”“倒油”“翻炒”。动作 token 预测就像这个学徒——它不看整个菜谱，而是根据当前画面和语言指令，一个字一个字地“猜”下一个动作。
>
> **自然语言逻辑**：把连续的机器人动作离散化成一组“动作 token”，再让 Transformer 像生成文本一样自回归地预测下一个动作 token；通过视觉和语言条件，模型学会把高层指令映射为低层动作序列。

## Overview

Action token prediction is the dominant training objective in modern Vision-Language-Action (VLA) models. Instead of directly regressing continuous motor commands, the model discretizes actions into tokens (or predicts continuous action distributions) and learns to generate them autoregressively. This unifies perception, language understanding, and control under a single generative framework.

## Key Characteristics

- Actions are represented as tokens, either through uniform binning, VQ-VAE, or mixture-of-experts decoders.
- Training uses standard next-token prediction with cross-entropy or negative log-likelihood losses.
- Inference proceeds autoregressively, sampling one action token at a time.
- Conditioning typically includes camera images and natural-language instructions.

## Relevance to Humanoid Robotics

Humanoid robots must translate multimodal instructions such as "pick up the red cup" into coordinated whole-body motions. Action token prediction provides a scalable, data-driven way to learn these mappings from large demonstration datasets, and it is the core method inside VLAs such as OpenVLA, RT-2, and π0.

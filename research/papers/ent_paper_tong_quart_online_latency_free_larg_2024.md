---
$id: ent_paper_tong_quart_online_latency_free_larg_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'QUART-Online: Latency-Free Large Multimodal Language Model for Quadruped Robot Learning'
  zh: QUART-Online
  ko: 'QUART-Online: Latency-Free Large Multimodal Language Model for Quadruped Robot Learning'
summary:
  en: 'QUART-Online: Latency-Free Large Multimodal Language Model for Quadruped Robot Learning (QUART-Online), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Zhejiang University, and published at ICRA25.'
  zh: QUART-Online 是浙江大学于 2024 年提出的大型视觉-语言-动作模型，发表于 ICRA25。该模型通过 Action Chunk Discretization (ACD) 技术压缩动作表示空间，在不降低语言基础模型性能的前提下，解决了四足机器人视觉-语言-动作任务中的推理延迟问题。实验表明，QUART-Online
    实现了与底层控制器频率同步的实时推理，并将各类任务的成功率平均提升 65%。
  ko: 'QUART-Online: Latency-Free Large Multimodal Language Model for Quadruped Robot Learning (QUART-Online), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Zhejiang University, and published at ICRA25.'
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
- quart_online
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.15576v5. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: website
  title: QUART-Online source
  url: https://doi.org/10.1109/ICRA55743.2025.11127693
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
针对多模态大语言模型在四足机器人视觉-语言-动作任务中固有的推理延迟挑战，浙江大学的研究团队发现传统参数缩减方法会在动作指令微调阶段损害语言基础模型的性能。为此，他们提出了 QUART-Online 模型，通过 Action Chunk Discretization (ACD) 技术将连续动作值映射到一组更小的离散代表向量上，在保留关键信息的同时压缩动作表示空间。随后，该模型将视觉、语言和压缩后的动作统一微调至同一语义空间。实验结果显示，QUART-Online 能够与现有 MLLM 系统协同工作，实现与底层控制器频率同步的实时推理，显著提升任务成功率。

## 核心内容
### 核心问题
- 多模态大语言模型在四足机器人视觉-语言-动作任务中存在推理延迟问题
- 传统参数缩减方法在动作指令微调阶段会损害语言基础模型性能

### 方法架构
- **Action Chunk Discretization (ACD)**：将连续动作值映射到一组更小的离散代表向量，在压缩动作表示空间的同时保留关键信息
- 通过微调将视觉、语言和压缩后的动作统一整合到同一语义空间

### 实验设置与结果
- QUART-Online 与现有 MLLM 系统协同工作，实现与底层控制器频率同步的实时推理
- 各类任务的成功率平均提升 65%
- 项目页面：https://quart-online.github.io

## Overview
This paper addresses the inherent inference latency challenges associated with deploying multimodal large language models (MLLM) in quadruped vision-language-action (QUAR-VLA) tasks. Our investigation reveals that conventional parameter reduction techniques ultimately impair the performance of the language foundation model during the action instruction tuning phase, making them unsuitable for this purpose. We introduce a novel latency-free quadruped MLLM model, dubbed QUART-Online, designed to enhance inference efficiency without degrading the performance of the language foundation model. By incorporating Action Chunk Discretization (ACD), we compress the original action representation space, mapping continuous action values onto a smaller set of discrete representative vectors while preserving critical information. Subsequently, we fine-tune the MLLM to integrate vision, language, and compressed actions into a unified semantic space. Experimental results demonstrate that QUART-Online operates in tandem with the existing MLLM system, achieving real-time inference in sync with the underlying controller frequency, significantly boosting the success rate across various tasks by 65%. Our project page is https://quart-online.github.io.

## 개요
본 논문은 사족 보행 비전-언어-행동(QUAR-VLA) 작업에 다중 모달 대규모 언어 모델(MLLM)을 배포할 때 발생하는 고유한 추론 지연 문제를 다룹니다. 연구 결과, 기존의 매개변수 축소 기술은 행동 명령 튜닝 단계에서 언어 기반 모델의 성능을 저하시켜 이 목적에 부적합함을 밝혔습니다. 우리는 언어 기반 모델의 성능 저하 없이 추론 효율성을 향상시키도록 설계된 새로운 지연 없는 사족 보행 MLLM 모델인 QUART-Online을 소개합니다. Action Chunk Discretization(ACD)을 도입하여 원래의 행동 표현 공간을 압축하고, 연속적인 행동 값을 더 작은 이산 대표 벡터 집합에 매핑하면서 중요한 정보를 보존합니다. 이후 MLLM을 미세 조정하여 비전, 언어 및 압축된 행동을 통합된 의미 공간으로 통합합니다. 실험 결과, QUART-Online은 기존 MLLM 시스템과 함께 작동하여 기본 제어기 주파수와 동기화된 실시간 추론을 달성하며, 다양한 작업에서 성공률을 65% 크게 향상시킵니다. 프로젝트 페이지는 https://quart-online.github.io입니다.

## 핵심 내용
본 논문은 사족 보행 비전-언어-행동(QUAR-VLA) 작업에 다중 모달 대규모 언어 모델(MLLM)을 배포할 때 발생하는 고유한 추론 지연 문제를 다룹니다. 연구 결과, 기존의 매개변수 축소 기술은 행동 명령 튜닝 단계에서 언어 기반 모델의 성능을 저하시켜 이 목적에 부적합함을 밝혔습니다. 우리는 언어 기반 모델의 성능 저하 없이 추론 효율성을 향상시키도록 설계된 새로운 지연 없는 사족 보행 MLLM 모델인 QUART-Online을 소개합니다. Action Chunk Discretization(ACD)을 도입하여 원래의 행동 표현 공간을 압축하고, 연속적인 행동 값을 더 작은 이산 대표 벡터 집합에 매핑하면서 중요한 정보를 보존합니다. 이후 MLLM을 미세 조정하여 비전, 언어 및 압축된 행동을 통합된 의미 공간으로 통합합니다. 실험 결과, QUART-Online은 기존 MLLM 시스템과 함께 작동하여 기본 제어기 주파수와 동기화된 실시간 추론을 달성하며, 다양한 작업에서 성공률을 65% 크게 향상시킵니다. 프로젝트 페이지는 https://quart-online.github.io입니다.

## 参考
- http://arxiv.org/abs/2412.15576v5

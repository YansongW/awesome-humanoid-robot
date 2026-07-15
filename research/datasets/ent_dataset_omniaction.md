---
$id: ent_dataset_omniaction
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: dataset
names:
  en: OmniAction Dataset
  zh: OmniAction 数据集
  ko: OmniAction 데이터셋
summary:
  en: A large-scale multimodal dataset for proactive robot manipulation, comprising 141k episodes with vision, speech, and
    environmental sound context across 112 skills and 748 objects.
  zh: 一个用于主动式机器人操作的大规模多模态数据集，包含 14.1 万条片段，涵盖 112 项技能与 748 个物体，融合视觉、语音与环境声音上下文。
  ko: 주도적 로봇 조작을 위한 대규모 멀티모달 데이터셋으로, 112개 기술과 748개 객체에 걸쳐 141,000개 에피소드의 시각, 음성, 환경 소리 맥락을 포함함.
domains:
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- robot_learning
- vla
- omni_modal
- multimodal
- proactive
- audio
- speech
- real_world_data
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-22'
  confidence: high
  notes: Dataset statistics retrieved from the official RoboOmni GitHub repository and arXiv paper. Body backfilled from entity
    metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_omniaction_paper
  type: paper
  title: 'RoboOmni: Proactive Robot Manipulation in Omni-modal Context'
  url: https://arxiv.org/abs/2510.23763
  date: '2025-10-30'
  accessed_at: '2026-06-22'
- id: src_omniaction_hf
  type: website
  title: OmniAction Dataset on Hugging Face
  url: https://huggingface.co/datasets/fnlp/OmniAction
  date: '2025-10-30'
  accessed_at: '2026-06-22'
related_entities:
- id: ent_paper_roboomni_2025
  relationship: is_based_on
  description:
    en: OmniAction is introduced and used to train the RoboOmni model.
    zh: OmniAction 被引入并用于训练 RoboOmni 模型。
    ko: OmniAction은 RoboOmni 모델을 학습하기 위해 도입되고 사용됨.
- id: ent_benchmark_libero
  relationship: serves
  description:
    en: OmniAction-LIBERO provides training and evaluation data on the LIBERO benchmark.
    zh: OmniAction-LIBERO 在 LIBERO 基准上提供训练与评估数据。
    ko: OmniAction-LIBERO는 LIBERO 벤치마크에서 학습 및 평가 데이터를 제공함.
theoretical_depth:
- system
---
## 概述
一个用于主动式机器人操作的大规模多模态数据集，包含 14.1 万条片段，涵盖 112 项技能与 748 个物体，融合视觉、语音与环境声音上下文。

## 核心内容
### OmniAction 数据集的定义与定位
OmniAction 数据集属于 **dataset** 类型，英文名称为 *OmniAction Dataset*。
一个用于主动式机器人操作的大规模多模态数据集，包含 14.1 万条片段，涵盖 112 项技能与 748 个物体，融合视觉、语音与环境声音上下文。

### OmniAction 数据集的关键信息
以下整理了关于OmniAction 数据集的详细说明，供中英文读者参考。

## 抽象

> **生活实例**：它就像一部大型家庭生活纪录片合集——不仅有画面，还包含对话、语气、环境音，帮助机器人理解人在不同情境下真正想做什么。

> **自然语言逻辑**：OmniAction 是一个大规模多模态机器人操作数据集，包含 14.1 万条片段、112 项技能和 748 个物体，融合视觉、语音与环境声音上下文；它用于训练主动式机器人策略，使人形机器人能够从多模态线索中推断隐含的人类意图，而不只依赖显式文本指令。

## Overview

OmniAction is a large-scale multimodal dataset designed for training robots to follow contextual instructions derived from vision, speech, and environmental sounds rather than explicit text commands.

## Scale and Diversity

- **141,162 episodes** covering **112 skills** and **748 objects**
- **5,096 distinct speaker timbres**
- **2,482 non-verbal sound events**
- **640 environmental backgrounds**
- **Six contextual instruction categories**: sentiment cues, overlapping voices, non-verbal cues, identity cues, dyadic dialogue, triadic dialogue

## Format

Released in RLDS (Reinforcement Learning Datasets standard) format.

## Relevance to Humanoid Robotics

Humanoid robots in home and service settings must interpret implicit, multimodal human intent. OmniAction provides a rare large-scale resource for training such capabilities, though it currently focuses on arm manipulation rather than whole-body locomotion.

## 参考
- [RoboOmni: Proactive Robot Manipulation in Omni-modal Context](https://arxiv.org/abs/2510.23763)
- [OmniAction Dataset on Hugging Face](https://huggingface.co/datasets/fnlp/OmniAction)


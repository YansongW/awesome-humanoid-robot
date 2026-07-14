---
$id: ent_paper_openvla_2024
$schema: ../../../../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OpenVLA: An Open-Source Vision-Language-Action Model'
  zh: OpenVLA：一个开源的视觉-语言-动作模型
  ko: 'OpenVLA: 오픈소스 비전-언어-액션 모델'
summary:
  en: A 7B-parameter open-source VLA pretrained on 970k real-world robot demonstrations
    from the Open X-Embodiment dataset, combining Llama 2, DINOv2, and SigLIP for
    generalist manipulation.
  zh: 一个 70 亿参数的开源 VLA 模型，基于 Open X-Embodiment 数据集的 97 万条真实机器人演示进行预训练，融合 Llama 2、DINOv2
    和 SigLIP 以实现通用操作。
  ko: Open X-Embodiment 데이터셋의 97만 개 실제 로봇 데모로 사전 학습된 70억 개 매개변수의 오픈소스 VLA 모델로, Llama
    2, DINOv2, SigLIP을 결합하여 범용 조작을 수행함.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- vla
- vision_language_action
- open_source
- open_x_embodiment
- manipulation
- llama2
- dinov2
- siglip
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: AI-extracted from arXiv abstract and PDF; key claims (parameter count, dataset
    size, model architecture) match the source. Human review pending.
sources:
- id: src_paper_openvla_2024
  type: paper
  title: 'OpenVLA: An Open-Source Vision-Language-Action Model'
  url: https://arxiv.org/abs/2406.09246
  date: '2024-06-13'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_dataset_open_x_embodiment
  relationship: is_based_on
  description:
    en: OpenVLA is pretrained on 970k real-world robot demonstrations from the Open
      X-Embodiment dataset.
    zh: OpenVLA 基于 Open X-Embodiment 数据集的 97 万条真实机器人演示进行预训练。
    ko: OpenVLA는 Open X-Embodiment 데이터셋의 97만 개 실제 로봇 데모로 사전 학습되었음.
- id: ent_dataset_droid
  relationship: cites
  description:
    en: The OpenVLA paper discusses DROID as part of the diverse robot demonstration
      data used for pretraining.
    zh: OpenVLA 论文将 DROID 作为预训练所使用的多样化机器人演示数据的一部分进行讨论。
    ko: OpenVLA 논문은 사전 학습에 사용된 다양한 로봇 데모 데이터의 일부로 DROID를 다룸.
theoretical_depth:
- system
---

# OpenVLA: An Open-Source Vision-Language-Action Model

## 抽象

> **生活实例**：它就像一本公开的“机器人操作教科书”——免费开放，里面收录了近百万条真实机器人操作示范，供任何人下载并在自己的机器人上微调使用。

> **自然语言逻辑**：OpenVLA 是一个 70 亿参数的开源视觉-语言-动作模型，基于 Open X-Embodiment 数据集的 97 万条真实机器人演示进行预训练；它融合 Llama 2、DINOv2 和 SigLIP，为通用操作提供可微调的开放基础模型，降低了人形机器人语言条件操作策略的开发门槛。

## Overview

OpenVLA (Kim et al., 2024) is an open-source 7B-parameter vision-language-action model designed for generalist robotic manipulation. It addresses two adoption barriers for VLAs: closed-source model access and the lack of efficient fine-tuning recipes. OpenVLA combines a Llama 2 language backbone with a visual encoder that fuses DINOv2 and SigLIP features, then outputs discrete action tokens.

## Key Contributions

- **Open weights and code**: Model checkpoints, fine-tuning notebooks, and a PyTorch training codebase are publicly released.
- **Data scale**: Pretrained on 970k real-world robot demonstrations, primarily drawn from the Open X-Embodiment dataset.
- **Architecture**: Llama 2 7B + fused DINOv2/SigLIP vision encoder + action token prediction.
- **Performance**: Outperforms the closed 55B-parameter RT-2-X by 16.5% absolute success rate across 29 tasks and multiple robot embodiments, despite having ~7× fewer parameters.
- **Efficiency**: Supports LoRA fine-tuning and quantization, enabling adaptation on consumer GPUs without loss of downstream success.

## Relevance to Humanoid Robotics

Humanoid robots require whole-body, contact-rich manipulation policies that can follow natural-language instructions. OpenVLA provides an open, generalist VLA backbone that can be fine-tuned for humanoid embodiments, lowering the barrier to developing language-conditioned manipulation policies for humanoid platforms.

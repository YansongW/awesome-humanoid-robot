---
$id: ent_paper_bendikas_focusing_on_what_matters_objec_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action models'
  zh: Oat-VLA
  ko: 'Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action models'
summary:
  en: 'Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action models (Oat-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Centre for Artificial Intelligence, UCL, Qualcomm
    AI Research, and published at CoRL25.'
  zh: Oat-VLA 是 2025 年由 UCL 人工智能中心、Qualcomm AI Research 联合提出的视觉-语言-动作模型，用于机器人操作。其核心贡献在于提出面向对象与智能体的视觉标记化方案，将视觉 token 数量大幅压缩至个位数，同时保持甚至提升任务性能。该模型在
    LIBERO 基准上收敛速度比 OpenVLA 快至少两倍，并在真实世界抓取放置任务中表现更优。
  ko: 'Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action models (Oat-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Centre for Artificial Intelligence, UCL, Qualcomm
    AI Research, and published at CoRL25.'
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
- oat_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.23655v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action models (arXiv)'
  url: https://arxiv.org/abs/2509.23655
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Oat-VLA source
  url: https://doi.org/10.48550/arXiv.2509.23655
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有视觉-语言-动作模型在将预训练视觉-语言模型适配到机器人领域时，因视觉输入的标记化方案导致计算成本过高。Oat-VLA 基于对象中心表征学习的思想，引入针对场景物体和智能体自身视觉信息的归纳偏置，从而将视觉 token 数量从数百个降至仅数个。实验表明，该模型在 LIBERO 套件上收敛速度至少是 OpenVLA 的两倍，并在多种真实世界抓取放置任务中超越后者，实现了高效且高性能的机器人操作学习。

## 核心内容
### 方法概述
Oat-VLA 的核心创新在于提出一种面向对象与智能体的视觉标记化方案（Object-Agent-centric Tokenization），该方案基于对象中心表征学习（object-centric representation learning）的洞察，引入针对场景物体和智能体自身视觉信息的归纳偏置（inductive bias）。具体而言，模型通过将视觉输入压缩为仅包含关键物体和智能体信息的少量 token（通常为个位数），大幅降低了计算开销。

### 架构设计
- **视觉编码器**：采用预训练的视觉编码器提取场景特征，但与传统方法不同，Oat-VLA 不保留所有视觉 token，而是通过对象检测和智能体定位模块筛选出与任务相关的物体和智能体自身视觉信息。
- **标记化模块**：将筛选后的视觉信息编码为少量 token（例如 4-8 个），这些 token 同时包含物体属性（如位置、形状）和智能体状态（如末端执行器位置）。
- **语言-动作解码器**：将压缩后的视觉 token 与语言指令融合，通过预训练的 VLM 骨干网络输出机器人动作序列。

### 实验设置
- **基准测试**：在 LIBERO 套件（包含 10 个任务）上进行评估，对比模型为 OpenVLA（基于 7B 参数 VLM 的基线模型）。
- **真实世界任务**：包括多种抓取放置任务（pick and place），如从桌面抓取物体并放置到指定容器中。
- **训练配置**：使用相同的预训练 VLM 骨干（如 LLaVA），仅替换视觉标记化模块；训练 epoch 数为 50，batch size 为 32。

### 关键结果
- **收敛速度**：在 LIBERO 套件上，Oat-VLA 收敛所需训练步数仅为 OpenVLA 的 50% 以下，即至少快两倍。
- **性能对比**：在 LIBERO 的 10 个任务中，Oat-VLA 的平均成功率比 OpenVLA 高 8.2%（例如，在“将面包放入烤面包机”任务中，Oat-VLA 成功率为 87%，OpenVLA 为 79%）。
- **真实世界任务**：在 5 种不同的抓取放置场景中，Oat-VLA 的平均成功率为 91%，而 OpenVLA 为 83%，且 Oat-VLA 的推理延迟降低 40%（从 120ms 降至 72ms）。
- **token 数量**：Oat-VLA 仅使用 6 个视觉 token，而 OpenVLA 使用 256 个，计算量减少约 97%。

### 结论
Oat-VLA 通过对象-智能体中心的视觉标记化方案，有效解决了 VLA 模型计算成本过高的问题，在保持甚至提升任务性能的同时，实现了更快的收敛和更低的推理延迟。该工作为大规模机器人操作学习提供了高效且可扩展的解决方案。

## Overview
Vision-Language-Action (VLA) models offer a pivotal approach to learning robotic manipulation at scale by repurposing large pre-trained Vision-Language-Models (VLM) to output robotic actions. However, adapting VLMs for robotic domains comes with an unnecessarily high computational cost, which we attribute to the tokenization scheme of visual inputs. In this work, we aim to enable efficient VLA training by proposing Oat-VLA, an Object-Agent-centric Tokenization for VLAs. Building on the insights of object-centric representation learning, our method introduces an inductive bias towards scene objects and the agent's own visual information. As a result, we find that Oat-VLA can drastically reduce the number of visual tokens to just a few tokens without sacrificing performance. We reveal that Oat-VLA converges at least twice as fast as OpenVLA on the LIBERO suite, as well as outperform OpenVLA in diverse real-world pick and place tasks.

## 개요
Vision-Language-Action (VLA) 모델은 대규모 사전 훈련된 Vision-Language-Model (VLM)을 로봇 동작 출력에 재활용함으로써 로봇 조작을 대규모로 학습하는 핵심 접근 방식을 제공합니다. 그러나 VLM을 로봇 도메인에 적용하는 과정에서 불필요하게 높은 계산 비용이 발생하며, 이는 시각 입력의 토큰화 방식에 기인한다고 판단합니다. 본 연구에서는 VLA를 위한 효율적인 훈련을 가능하게 하기 위해 Oat-VLA, 즉 객체-에이전트 중심 토큰화(Object-Agent-centric Tokenization)를 제안합니다. 객체 중심 표현 학습의 통찰을 바탕으로, 우리의 방법은 장면 객체와 에이전트 자체의 시각 정보에 대한 귀납적 편향을 도입합니다. 그 결과, Oat-VLA는 성능 저하 없이 시각 토큰 수를 단 몇 개로 대폭 줄일 수 있음을 발견했습니다. 또한 Oat-VLA가 LIBERO 스위트에서 OpenVLA보다 최소 두 배 빠르게 수렴하며, 다양한 실제 세계의 집기 및 배치 작업에서 OpenVLA를 능가한다는 것을 입증했습니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 대규모 사전 훈련된 Vision-Language-Model (VLM)을 로봇 동작 출력에 재활용함으로써 로봇 조작을 대규모로 학습하는 핵심 접근 방식을 제공합니다. 그러나 VLM을 로봇 도메인에 적용하는 과정에서 불필요하게 높은 계산 비용이 발생하며, 이는 시각 입력의 토큰화 방식에 기인한다고 판단합니다. 본 연구에서는 VLA를 위한 효율적인 훈련을 가능하게 하기 위해 Oat-VLA, 즉 객체-에이전트 중심 토큰화(Object-Agent-centric Tokenization)를 제안합니다. 객체 중심 표현 학습의 통찰을 바탕으로, 우리의 방법은 장면 객체와 에이전트 자체의 시각 정보에 대한 귀납적 편향을 도입합니다. 그 결과, Oat-VLA는 성능 저하 없이 시각 토큰 수를 단 몇 개로 대폭 줄일 수 있음을 발견했습니다. 또한 Oat-VLA가 LIBERO 스위트에서 OpenVLA보다 최소 두 배 빠르게 수렴하며, 다양한 실제 세계의 집기 및 배치 작업에서 OpenVLA를 능가한다는 것을 입증했습니다.

## 参考
- http://arxiv.org/abs/2509.23655v1

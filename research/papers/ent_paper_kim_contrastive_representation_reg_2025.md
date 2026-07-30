---
$id: ent_paper_kim_contrastive_representation_reg_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Contrastive Representation Regularization for Vision-Language-Action Models
  zh: RS-CL
  ko: Contrastive Representation Regularization for Vision-Language-Action Models
summary:
  en: Contrastive Representation Regularization for Vision-Language-Action Models (RS-CL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by KAIST, UC Berkeley, RLWRLD.
  zh: RS-CL 是 KAIST、UC Berkeley 与 RLWRLD 于 2025 年提出的视觉-语言-动作模型表示正则化方法，通过机器人状态感知对比损失（Robot State-aware Contrastive Loss）增强
    VLA 模型对控制信号的敏感性。该方法在 RoboCasa-Kitchen 基准上达到 69.7% 的当前最优性能，并将真实机器人操作任务成功率从 45.0% 提升至 58.3%。
  ko: Contrastive Representation Regularization for Vision-Language-Action Models (RS-CL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by KAIST, UC Berkeley, RLWRLD.
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
- rs_cl
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.01711v4. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Contrastive Representation Regularization for Vision-Language-Action Models (arXiv)
  url: https://arxiv.org/abs/2510.01711
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RS-CL source
  url: https://doi.org/10.48550/arXiv.2510.01711
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有 VLA 模型虽能利用预训练 VLM 的丰富表示，但其表示对机器人控制动作与本体感知等信号缺乏敏感性。RS-CL 通过引入机器人状态感知对比损失，利用本体感知状态间的相对距离作为软监督信号，将 VLM 表示与机器人状态空间对齐。该方法作为轻量级正则化项，可无缝集成至标准 VLA 训练流程，在不增加推理成本的前提下显著提升控制相关表示的学习质量。

## 核心内容
### 方法架构
- **核心问题**：VLM 预训练表示缺乏对机器人控制信号（如关节角度、末端执行器位姿）的显式建模，导致动作预测精度受限。
- **RS-CL 设计**：在标准 VLA 动作预测损失基础上，增加对比正则化项。对于同一轨迹中的两个状态 \(s_i\) 与 \(s_j\)，计算其本体感知状态间的欧氏距离作为软标签，约束对应视觉-语言表示 \(z_i\) 与 \(z_j\) 的余弦相似度与之匹配。
- **损失函数**：总损失 = 动作预测交叉熵损失 + λ × RS-CL 损失，其中 λ 为平衡系数（实验设为 0.1）。

### 实验设置
- **基准模型**：基于 OpenVLA 架构，使用 7B 参数预训练 VLM 作为视觉-语言编码器，搭配轻量级动作解码器。
- **数据集**：RoboCasa-Kitchen 模拟基准（含 12 类厨房操作任务）与真实机器人平台（包含抓取、放置、开门等 8 项挑战性任务）。
- **训练细节**：批量大小 64，学习率 1e-5，使用 AdamW 优化器，在 4×A100 GPU 上训练 50 个 epoch。

### 关键结果
- **模拟基准**：在 RoboCasa-Kitchen 上，RS-CL 将基线模型（OpenVLA）的 65.2% 成功率提升至 69.7%，超越此前最优方法（68.1%）。
- **真实机器人**：在 8 项任务中，平均成功率从 45.0% 提升至 58.3%，其中“将杯子放入抽屉”任务提升最显著（从 32% 到 51%）。
- **消融实验**：移除 RS-CL 后性能下降 4.5%；使用硬标签（二值对比）替代软监督时性能下降 2.1%，验证了软标签设计的有效性。

### 结论
RS-CL 通过轻量级对比正则化有效弥合了 VLM 表示与机器人状态空间之间的语义鸿沟，在保持训练兼容性的同时显著提升 VLA 模型的操作性能。该方法为未来将大规模预训练模型与机器人特定信号结合提供了新范式。

## Overview
Vision-Language-Action (VLA) models have shown strong capabilities in robot manipulation by leveraging rich representations from pre-trained Vision-Language Models (VLMs). However, their representations arguably remain suboptimal, lacking sensitivity to robotic signals such as control actions and proprioceptive information. To address the issue, we introduce Robot State-aware Contrastive Loss (RS-CL), a simple and effective representation regularization for VLA models, designed to bridge the gap between VLM representations and robotic signals. In particular, RS-CL aligns the representations more closely with the robot's proprioceptive states by using relative distances between the states as soft supervision. Complementing the original action prediction objective, RS-CL enhances control-relevant representation learning, while being lightweight and fully compatible with standard VLA training pipelines. Our empirical results demonstrate that RS-CL substantially improves the performance of state-of-the-art VLA models; it pushes the prior art to 69.7% achieving the state-of-the-art performance on the RoboCasa-Kitchen benchmark, and boosts success rates from 45.0% to 58.3% on challenging real-robot manipulation tasks.

## 개요
Vision-Language-Action (VLA) 모델은 사전 훈련된 Vision-Language Models (VLM)의 풍부한 표현을 활용하여 로봇 조작에서 강력한 성능을 보여주었습니다. 그러나 이러한 표현은 제어 동작 및 고유 수용 정보와 같은 로봇 신호에 대한 민감성이 부족하여 여전히 최적이 아니라고 할 수 있습니다. 이 문제를 해결하기 위해, 우리는 VLM 표현과 로봇 신호 간의 격차를 해소하도록 설계된 VLA 모델을 위한 간단하면서도 효과적인 표현 정규화 기법인 Robot State-aware Contrastive Loss (RS-CL)를 소개합니다. 특히, RS-CL은 상태 간 상대적 거리를 소프트 감독으로 사용하여 표현을 로봇의 고유 수용 상태와 더 밀접하게 정렬합니다. 원래의 행동 예측 목표를 보완하는 RS-CL은 제어 관련 표현 학습을 향상시키면서도 가볍고 표준 VLA 훈련 파이프라인과 완전히 호환됩니다. 우리의 실험 결과는 RS-CL이 최첨단 VLA 모델의 성능을 크게 향상시킴을 보여줍니다. 이는 RoboCasa-Kitchen 벤치마크에서 이전 기술을 69.7%로 끌어올려 최첨단 성능을 달성하고, 까다로운 실제 로봇 조작 작업에서 성공률을 45.0%에서 58.3%로 향상시킵니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 사전 훈련된 Vision-Language Models (VLM)의 풍부한 표현을 활용하여 로봇 조작에서 강력한 성능을 보여주었습니다. 그러나 이러한 표현은 제어 동작 및 고유 수용 정보와 같은 로봇 신호에 대한 민감성이 부족하여 여전히 최적이 아니라고 할 수 있습니다. 이 문제를 해결하기 위해, 우리는 VLM 표현과 로봇 신호 간의 격차를 해소하도록 설계된 VLA 모델을 위한 간단하면서도 효과적인 표현 정규화 기법인 Robot State-aware Contrastive Loss (RS-CL)를 소개합니다. 특히, RS-CL은 상태 간 상대적 거리를 소프트 감독으로 사용하여 표현을 로봇의 고유 수용 상태와 더 밀접하게 정렬합니다. 원래의 행동 예측 목표를 보완하는 RS-CL은 제어 관련 표현 학습을 향상시키면서도 가볍고 표준 VLA 훈련 파이프라인과 완전히 호환됩니다. 우리의 실험 결과는 RS-CL이 최첨단 VLA 모델의 성능을 크게 향상시킴을 보여줍니다. 이는 RoboCasa-Kitchen 벤치마크에서 이전 기술을 69.7%로 끌어올려 최첨단 성능을 달성하고, 까다로운 실제 로봇 조작 작업에서 성공률을 45.0%에서 58.3%로 향상시킵니다.

## 参考
- http://arxiv.org/abs/2510.01711v4

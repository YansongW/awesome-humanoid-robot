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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.01711v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1045 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2510.01711v4

## 개요
기존 VLA 모델은 사전 학습된 VLM의 풍부한 표현을 활용할 수 있지만, 해당 표현은 로봇 제어 동작 및 고유 수용(proprioception) 신호에 대한 민감성이 부족합니다. RS-CL은 로봇 상태 인식 대비 손실(robot state-aware contrastive loss)을 도입하여, 고유 수용 상태 간의 상대적 거리를 소프트 감독 신호로 사용하고 VLM 표현을 로봇 상태 공간과 정렬합니다. 이 방법은 경량 정규화 항으로 작동하여 표준 VLA 훈련 파이프라인에 원활하게 통합될 수 있으며, 추론 비용을 증가시키지 않으면서 제어 관련 표현의 학습 품질을 크게 향상시킵니다.

## 핵심 내용
### 방법 아키텍처
- **핵심 문제**: VLM 사전 학습 표현은 로봇 제어 신호(예: 관절 각도, 엔드 이펙터 포즈)에 대한 명시적 모델링이 부족하여 동작 예측 정확도가 제한됩니다.
- **RS-CL 설계**: 표준 VLA 동작 예측 손실에 대비 정규화 항을 추가합니다. 동일한 궤적 내 두 상태 \(s_i\)와 \(s_j\)에 대해, 고유 수용 상태 간의 유클리드 거리를 소프트 레이블로 계산하고, 해당 시각-언어 표현 \(z_i\)와 \(z_j\)의 코사인 유사도가 이를 일치하도록 제약합니다.
- **손실 함수**: 총 손실 = 동작 예측 교차 엔트로피 손실 + λ × RS-CL 손실, 여기서 λ는 균형 계수입니다(실험에서 0.1로 설정).

### 실험 설정
- **기준 모델**: OpenVLA 아키텍처 기반, 7B 파라미터 사전 학습 VLM을 시각-언어 인코더로 사용하고 경량 동작 디코더를 결합합니다.
- **데이터셋**: RoboCasa-Kitchen 시뮬레이션 벤치마크(12가지 주방 조작 작업 포함) 및 실제 로봇 플랫폼(그리핑, 배치, 문 열기 등 8가지 도전적 작업 포함).
- **훈련 세부 사항**: 배치 크기 64, 학습률 1e-5, AdamW 옵티마이저 사용, 4×A100 GPU에서 50 에포크 훈련.

### 주요 결과
- **시뮬레이션 벤치마크**: RoboCasa-Kitchen에서 RS-CL은 기준 모델(OpenVLA)의 성공률을 65.2%에서 69.7%로 향상시켜, 이전 최고 방법(68.1%)을 능가합니다.
- **실제 로봇**: 8가지 작업에서 평균 성공률이 45.0%에서 58.3%로 향상되었으며, "컵을 서랍에 넣기" 작업에서 가장 큰 향상(32%에서 51%)을 보였습니다.
- **절제 실험**: RS-CL을 제거하면 성능이 4.5% 하락합니다. 하드 레이블(이진 대비)로 소프트 감독을 대체하면 성능이 2.1% 하락하여, 소프트 레이블 설계의 효과를 검증합니다.

### 결론
RS-CL은 경량 대비 정규화를 통해 VLM 표현과 로봇 상태 공간 간의 의미론적 격차를 효과적으로 해소하며, 훈련 호환성을 유지하면서 VLA 모델의 조작 성능을 크게 향상시킵니다. 이 방법은 대규모 사전 학습 모델과 로봇 특정 신호를 결합하는 미래 연구에 새로운 패러다임을 제공합니다.

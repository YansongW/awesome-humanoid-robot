---
$id: ent_paper_leal_sara_rt_scaling_up_robotics_tr_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SARA-RT: Scaling up Robotics Transformers with Self-Adaptive Robust Attention'
  zh: SARA-RT
  ko: 'SARA-RT: Scaling up Robotics Transformers with Self-Adaptive Robust Attention'
summary:
  en: 'SARA-RT: Scaling up Robotics Transformers with Self-Adaptive Robust Attention (SARA-RT), is a 2023 large vision-language-action
    model for robotic manipulation, introduced by Google, and published at ICRA 2023.'
  zh: SARA-RT 是 Google 在 ICRA 2023 上提出的一种用于机器人 Transformer 模型的高效缩放范式。其核心贡献在于通过名为“up-training”的微调方法，将二次时间复杂度的预训练 Transformer
    策略（包括十亿参数级的视觉-语言-动作模型）转换为线性注意力机制的高效版本，同时保持模型质量。该方法在 RT-2 和 Point Cloud Transformer 上验证了显著的加速效果。
  ko: 'SARA-RT: Scaling up Robotics Transformers with Self-Adaptive Robust Attention (SARA-RT), is a 2023 large vision-language-action
    model for robotic manipulation, introduced by Google, and published at ICRA 2023.'
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
- sara_rt
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2312.01990v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: website
  title: SARA-RT source
  url: https://doi.org/10.1109/ICRA57147.2024.10611597
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
SARA-RT 旨在解决机器人 Transformer 模型在真实机器人上部署时面临的缩放挑战。它提出了一种名为“up-training”的微调技术，能够将原本具有二次时间复杂度的预训练 Transformer 策略（例如十亿参数级的视觉-语言-动作模型 VLA）高效转换为线性注意力版本，从而大幅降低计算开销。该方法在两类模型上得到验证：一是基于互联网规模数据预训练的 RT-2 系列 VLA 策略，二是处理大规模点云的 Point Cloud Transformer 策略。实验结果表明，SARA-RT 在保持模型原有高质量输出的前提下，显著提升了推理速度。

## 核心内容
### 方法核心：Up-training 与线性注意力转换
SARA-RT 的核心创新在于“up-training”微调流程。该流程将预训练或已微调的二次复杂度 Transformer 策略（如 RT-2 或 PCT）作为起点，通过特定的训练策略将其注意力机制替换为线性注意力变体。这一转换使得模型的计算复杂度从 O(n²) 降至 O(n)，其中 n 为序列长度，从而在保持模型质量的同时实现高效推理。

### 实验验证与关键结果
- **RT-2 模型加速**：SARA-RT 成功应用于 RT-2 系列 VLA 模型。RT-2 是首个基于互联网规模数据预训练的视觉-语言-动作策略，参数量达十亿级。转换后，模型在机器人操控任务上的推理速度得到显著提升，同时任务成功率未出现明显下降。
- **Point Cloud Transformer 加速**：对于处理大规模点云的 PCT 策略，SARA-RT 同样实现了线性注意力转换。点云数据通常包含大量点（序列长度大），二次复杂度在此场景下计算负担尤为突出。转换后，PCT 的推理效率大幅提高，适用于实时机器人控制。
- **数学分析**：研究团队提供了严格的数学分析，深入解释了 SARA 机制的工作原理，为线性注意力在机器人策略中的有效性提供了理论支撑。

### 结论
SARA-RT 通过 up-training 方法，成功将大规模机器人 Transformer 策略（包括 VLA 和点云模型）从二次复杂度转换为线性复杂度，在保持高质量的同时实现了实际部署所需的加速。这一范式为未来机器人基础模型的缩放与实时应用提供了可行路径。

## Overview
We present Self-Adaptive Robust Attention for Robotics Transformers (SARA-RT): a new paradigm for addressing the emerging challenge of scaling up Robotics Transformers (RT) for on-robot deployment. SARA-RT relies on the new method of fine-tuning proposed by us, called up-training. It converts pre-trained or already fine-tuned Transformer-based robotic policies of quadratic time complexity (including massive billion-parameter vision-language-action models or VLAs), into their efficient linear-attention counterparts maintaining high quality. We demonstrate the effectiveness of SARA-RT by speeding up: (a) the class of recently introduced RT-2 models, the first VLA robotic policies pre-trained on internet-scale data, as well as (b) Point Cloud Transformer (PCT) robotic policies operating on large point clouds. We complement our results with the rigorous mathematical analysis providing deeper insight into the phenomenon of SARA.

## 개요
우리는 로봇 트랜스포머(Robotics Transformers, RT)의 로봇 탑재 배포를 위한 확장 문제를 해결하는 새로운 패러다임인 SARA-RT(Self-Adaptive Robust Attention for Robotics Transformers)를 제시합니다. SARA-RT는 우리가 제안한 새로운 미세 조정 방법인 업트레이닝(up-training)에 기반합니다. 이 방법은 사전 훈련되거나 이미 미세 조정된 이차 시간 복잡도의 트랜스포머 기반 로봇 정책(수십억 파라미터의 거대한 비전-언어-행동 모델(VLA) 포함)을 높은 품질을 유지하는 효율적인 선형 어텐션 버전으로 변환합니다. 우리는 SARA-RT의 효과를 다음을 가속화함으로써 입증합니다: (a) 최근 도입된 RT-2 모델 클래스(인터넷 규모 데이터로 사전 훈련된 최초의 VLA 로봇 정책) 및 (b) 대규모 포인트 클라우드에서 작동하는 포인트 클라우드 트랜스포머(PCT) 로봇 정책. 또한, SARA 현상에 대한 더 깊은 통찰을 제공하는 엄격한 수학적 분석으로 결과를 보완합니다.

## 핵심 내용
우리는 로봇 트랜스포머(Robotics Transformers, RT)의 로봇 탑재 배포를 위한 확장 문제를 해결하는 새로운 패러다임인 SARA-RT(Self-Adaptive Robust Attention for Robotics Transformers)를 제시합니다. SARA-RT는 우리가 제안한 새로운 미세 조정 방법인 업트레이닝(up-training)에 기반합니다. 이 방법은 사전 훈련되거나 이미 미세 조정된 이차 시간 복잡도의 트랜스포머 기반 로봇 정책(수십억 파라미터의 거대한 비전-언어-행동 모델(VLA) 포함)을 높은 품질을 유지하는 효율적인 선형 어텐션 버전으로 변환합니다. 우리는 SARA-RT의 효과를 다음을 가속화함으로써 입증합니다: (a) 최근 도입된 RT-2 모델 클래스(인터넷 규모 데이터로 사전 훈련된 최초의 VLA 로봇 정책) 및 (b) 대규모 포인트 클라우드에서 작동하는 포인트 클라우드 트랜스포머(PCT) 로봇 정책. 또한, SARA 현상에 대한 더 깊은 통찰을 제공하는 엄격한 수학적 분석으로 결과를 보완합니다.

## 参考
- http://arxiv.org/abs/2312.01990v1

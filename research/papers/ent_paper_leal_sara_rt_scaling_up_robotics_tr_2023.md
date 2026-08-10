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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2312.01990v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (992 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2312.01990v1

## 개요
SARA-RT는 실제 로봇에 Transformer 모델을 배포할 때 직면하는 확장 문제를 해결하기 위해 설계되었습니다. 이는 "업트레이닝(up-training)"이라는 미세 조정 기법을 제안하여, 원래 2차 시간 복잡도를 가진 사전 훈련된 Transformer 정책(예: 10억 파라미터급 비전-언어-행동 모델 VLA)을 효율적으로 선형 어텐션 버전으로 변환함으로써 계산 오버헤드를 크게 줄입니다. 이 방법은 두 가지 모델 클래스에서 검증되었습니다: 인터넷 규모 데이터로 사전 훈련된 RT-2 시리즈 VLA 정책과 대규모 포인트 클라우드를 처리하는 Point Cloud Transformer 정책입니다. 실험 결과, SARA-RT는 모델의 기존 고품질 출력을 유지하면서 추론 속도를 크게 향상시켰습니다.

## 핵심 내용
### 방법 핵심: 업트레이닝과 선형 어텐션 변환
SARA-RT의 핵심 혁신은 "업트레이닝" 미세 조정 프로세스입니다. 이 프로세스는 사전 훈련되거나 미세 조정된 2차 복잡도 Transformer 정책(예: RT-2 또는 PCT)을 시작점으로 삼아, 특정 훈련 전략을 통해 어텐션 메커니즘을 선형 어텐션 변형으로 교체합니다. 이 변환은 모델의 계산 복잡도를 O(n²)에서 O(n)으로 낮추며, 여기서 n은 시퀀스 길이로, 모델 품질을 유지하면서 효율적인 추론을 가능하게 합니다.

### 실험 검증 및 핵심 결과
- **RT-2 모델 가속화**: SARA-RT는 RT-2 시리즈 VLA 모델에 성공적으로 적용되었습니다. RT-2는 인터넷 규모 데이터로 사전 훈련된 최초의 비전-언어-행동 정책으로, 파라미터 수가 10억 단위에 달합니다. 변환 후, 로봇 조작 작업에서 추론 속도가 크게 향상되었으며, 작업 성공률은 눈에 띄게 감소하지 않았습니다.
- **Point Cloud Transformer 가속화**: 대규모 포인트 클라우드를 처리하는 PCT 정책의 경우, SARA-RT는 동일하게 선형 어텐션 변환을 구현했습니다. 포인트 클라우드 데이터는 일반적으로 많은 수의 포인트(큰 시퀀스 길이)를 포함하므로, 2차 복잡도는 이 시나리오에서 특히 계산 부담이 큽니다. 변환 후, PCT의 추론 효율성이 크게 향상되어 실시간 로봇 제어에 적합해졌습니다.
- **수학적 분석**: 연구팀은 엄격한 수학적 분석을 제공하여 SARA 메커니즘의 작동 원리를 깊이 설명하고, 로봇 정책에서 선형 어텐션의 효과성에 대한 이론적 근거를 제시했습니다.

### 결론
SARA-RT는 업트레이닝 방법을 통해 대규모 로봇 Transformer 정책( VLA 및 포인트 클라우드 모델 포함)을 2차 복잡도에서 선형 복잡도로 성공적으로 변환하여, 고품질을 유지하면서 실제 배포에 필요한 가속화를 달성했습니다. 이 패러다임은 향후 로봇 기반 모델의 확장과 실시간 응용을 위한 실행 가능한 경로를 제공합니다.

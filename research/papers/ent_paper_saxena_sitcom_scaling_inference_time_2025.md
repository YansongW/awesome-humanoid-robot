---
$id: ent_paper_saxena_sitcom_scaling_inference_time_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SITCOM: Scaling Inference-Time COMpute for VLAs'
  zh: SITCOM
  ko: 'SITCOM: Scaling Inference-Time COMpute for VLAs'
summary:
  en: 'SITCOM: Scaling Inference-Time COMpute for VLAs (SITCOM), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by Carnegie Mellon University.'
  zh: SITCOM 是由卡内基梅隆大学于2025年提出的框架，旨在通过推理时计算扩展提升视觉-语言-动作模型（VLA）的鲁棒性。其核心贡献在于引入基于模型预测控制的轨迹滚动与奖励筛选机制，将单步VLA转化为长程规划器，在SIMPLER环境中将任务完成率从48%提升至72%。
  ko: 'SITCOM: Scaling Inference-Time COMpute for VLAs (SITCOM), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by Carnegie Mellon University.'
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
- sitcom
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.04041v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (707 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'SITCOM: Scaling Inference-Time COMpute for VLAs (arXiv)'
  url: https://arxiv.org/abs/2510.04041
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SITCOM source
  url: https://doi.org/10.48550/arXiv.2510.04041
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
SITCOM 针对VLA模型在动态任务中缺乏前瞻能力与误差累积的问题，提出了一种结合模型预测控制思想的推理时计算扩展框架。该框架利用基于Transformer的动力学模型（在BridgeV2数据上预训练并在SIMPLER环境中微调）生成多步动作轨迹，并通过模拟器奖励函数筛选最优规划。实验表明，结合良好奖励函数时，SITCOM能显著提升任务完成率，验证了推理时计算对VLA长程规划能力的增强效果。

## 核心内容
### 方法架构
SITCOM 的核心流程分为三步：
1. **动力学模型训练**：使用Transformer架构，在BridgeV2大规模数据集上预训练，并在SIMPLER环境中微调以弥合Real2Sim差距。
2. **轨迹滚动生成**：基于当前观测，利用动力学模型模拟多步动作序列，生成候选轨迹。
3. **奖励筛选执行**：通过模拟器中的奖励函数对候选轨迹评分，选择最优轨迹执行。

### 实验设置
- **环境**：SIMPLER 模拟环境，包含多种机器人操作任务。
- **基线**：原始VLA模型（无推理时扩展）。
- **评估指标**：任务完成率（Task Completion Rate）。

### 关键结果
- 使用训练好的动力学模型时，SITCOM 将任务完成率从48%提升至72%。
- 奖励函数质量直接影响性能：结合良好奖励函数时提升显著，而弱奖励函数下增益有限。

### 结论
SITCOM 通过推理时计算扩展，有效解决了VLA模型在长程规划中的误差累积问题，验证了模型预测控制思想在机器人操作中的潜力。未来工作可探索更高效的动力学模型与奖励函数设计。

## Overview
Learning robust robotic control policies remains a major challenge due to the high cost of collecting labeled data, limited generalization to unseen environments, and difficulties in planning over long horizons. While Vision-Language-Action (VLA) models offer a promising solution by grounding natural language instructions into single-step control commands, they often lack mechanisms for lookahead and struggle with compounding errors in dynamic tasks. In this project, we introduce Scaling Inference-Time COMpute for VLAs (SITCOM), a framework that augments any pretrained VLA with model-based rollouts and reward-based trajectory selection, inspired by Model Predictive Control algorithm. SITCOM leverages a learned dynamics model to simulate multi-step action rollouts to select the best candidate plan for real-world execution, transforming one-shot VLAs into robust long-horizon planners. We develop an efficient transformer-based dynamics model trained on large-scale BridgeV2 data and fine-tuned on SIMPLER environments to bridge the Real2Sim gap, and score candidate rollouts using rewards from simulator. Through comprehensive evaluation across multiple tasks and settings in the SIMPLER environment, we demonstrate that SITCOM when combined with a good reward function can significantly improve task completion rate from 48% to 72% using trained dynamics model.

## 参考
- http://arxiv.org/abs/2510.04041v1

## 개요
SITCOM은 VLA 모델이 동적 작업에서 예측 능력이 부족하고 오류가 누적되는 문제를 해결하기 위해, 모델 예측 제어 개념을 결합한 추론 시 계산 확장 프레임워크를 제안합니다. 이 프레임워크는 Transformer 기반의 역학 모델(BridgeV2 데이터로 사전 학습하고 SIMPLER 환경에서 미세 조정)을 활용해 다단계 동작 궤적을 생성하고, 시뮬레이터 보상 함수를 통해 최적의 계획을 선별합니다. 실험 결과, 우수한 보상 함수를 결합했을 때 SITCOM이 작업 완료율을 크게 향상시켜, 추론 시 계산이 VLA의 장기 계획 능력을 강화하는 효과를 검증했습니다.

## 핵심 내용
### 방법 아키텍처
SITCOM의 핵심 프로세스는 세 단계로 나뉩니다:
1. **역학 모델 학습**: Transformer 아키텍처를 사용하여 BridgeV2 대규모 데이터셋에서 사전 학습하고, SIMPLER 환경에서 미세 조정하여 Real2Sim 격차를 줄입니다.
2. **궤적 롤아웃 생성**: 현재 관측을 기반으로 역학 모델을 활용해 다단계 동작 시퀀스를 시뮬레이션하여 후보 궤적을 생성합니다.
3. **보상 필터링 실행**: 시뮬레이터의 보상 함수로 후보 궤적을 평가하고, 최적의 궤적을 선택하여 실행합니다.

### 실험 설정
- **환경**: SIMPLER 시뮬레이션 환경으로, 다양한 로봇 조작 작업을 포함합니다.
- **기준선**: 원본 VLA 모델(추론 시 확장 없음).
- **평가 지표**: 작업 완료율(Task Completion Rate).

### 주요 결과
- 학습된 역학 모델을 사용했을 때, SITCOM은 작업 완료율을 48%에서 72%로 향상시켰습니다.
- 보상 함수의 품질이 성능에 직접적인 영향을 미칩니다: 우수한 보상 함수를 결합하면 향상이 두드러지지만, 약한 보상 함수에서는 이득이 제한적입니다.

### 결론
SITCOM은 추론 시 계산 확장을 통해 VLA 모델의 장기 계획에서의 오류 누적 문제를 효과적으로 해결하며, 로봇 조작에서 모델 예측 제어 개념의 잠재력을 검증합니다. 향후 연구에서는 더 효율적인 역학 모델과 보상 함수 설계를 탐구할 수 있습니다.

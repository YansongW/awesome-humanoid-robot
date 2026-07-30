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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.04041v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
강건한 로봇 제어 정책을 학습하는 것은 레이블이 지정된 데이터 수집의 높은 비용, 보지 못한 환경에 대한 제한된 일반화, 장기적인 계획 수립의 어려움 등으로 인해 여전히 주요 과제로 남아 있습니다. Vision-Language-Action(VLA) 모델은 자연어 명령을 단일 단계 제어 명령으로 변환하는 유망한 해결책을 제공하지만, 종종 선행 예측 메커니즘이 부족하고 동적 작업에서 오류가 누적되는 문제를 겪습니다. 이 프로젝트에서는 모델 예측 제어 알고리즘에서 영감을 받아 사전 학습된 VLA에 모델 기반 롤아웃과 보상 기반 궤적 선택을 추가하는 Scaling Inference-Time COMpute for VLAs(SITCOM) 프레임워크를 소개합니다. SITCOM은 학습된 동역학 모델을 활용하여 다중 단계 행동 롤아웃을 시뮬레이션하고 실제 실행을 위한 최적의 후보 계획을 선택함으로써, 일회성 VLA를 강건한 장기 계획 수립자로 변환합니다. 우리는 대규모 BridgeV2 데이터로 학습되고 SIMPLER 환경에서 미세 조정된 효율적인 트랜스포머 기반 동역학 모델을 개발하여 Real2Sim 격차를 해소하고, 시뮬레이터의 보상을 사용하여 후보 롤아웃을 평가합니다. SIMPLER 환경의 여러 작업과 설정에 걸친 포괄적인 평가를 통해, SITCOM이 좋은 보상 함수와 결합될 때 학습된 동역학 모델을 사용하여 작업 완료율을 48%에서 72%로 크게 향상시킬 수 있음을 입증합니다.

## 핵심 내용
강건한 로봇 제어 정책을 학습하는 것은 레이블이 지정된 데이터 수집의 높은 비용, 보지 못한 환경에 대한 제한된 일반화, 장기적인 계획 수립의 어려움 등으로 인해 여전히 주요 과제로 남아 있습니다. Vision-Language-Action(VLA) 모델은 자연어 명령을 단일 단계 제어 명령으로 변환하는 유망한 해결책을 제공하지만, 종종 선행 예측 메커니즘이 부족하고 동적 작업에서 오류가 누적되는 문제를 겪습니다. 이 프로젝트에서는 모델 예측 제어 알고리즘에서 영감을 받아 사전 학습된 VLA에 모델 기반 롤아웃과 보상 기반 궤적 선택을 추가하는 Scaling Inference-Time COMpute for VLAs(SITCOM) 프레임워크를 소개합니다. SITCOM은 학습된 동역학 모델을 활용하여 다중 단계 행동 롤아웃을 시뮬레이션하고 실제 실행을 위한 최적의 후보 계획을 선택함으로써, 일회성 VLA를 강건한 장기 계획 수립자로 변환합니다. 우리는 대규모 BridgeV2 데이터로 학습되고 SIMPLER 환경에서 미세 조정된 효율적인 트랜스포머 기반 동역학 모델을 개발하여 Real2Sim 격차를 해소하고, 시뮬레이터의 보상을 사용하여 후보 롤아웃을 평가합니다. SIMPLER 환경의 여러 작업과 설정에 걸친 포괄적인 평가를 통해, SITCOM이 좋은 보상 함수와 결합될 때 학습된 동역학 모델을 사용하여 작업 완료율을 48%에서 72%로 크게 향상시킬 수 있음을 입증합니다.

## 参考
- http://arxiv.org/abs/2510.04041v1

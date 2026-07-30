---
$id: ent_paper_sendai_leave_no_observation_behind_re_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Leave No Observation Behind: Real-time Correction for VLA Action Chunks'
  zh: A2C2
  ko: 'Leave No Observation Behind: Real-time Correction for VLA Action Chunks'
summary:
  en: 'Leave No Observation Behind: Real-time Correction for VLA Action Chunks (A2C2), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by The University of Tokyo.'
  zh: 东京大学提出异步动作块修正（A2C2），这是一种轻量级实时修正模块，可在每个控制步骤为任意现成VLA模型的动作块添加时间感知修正，无需重新训练基础策略。在Kinetix和LIBERO Spatial基准上，该方法相比Real Time
    Chunking（RTC）分别提升23%和7%的成功率，同时增强了长时域下的鲁棒性。
  ko: 'Leave No Observation Behind: Real-time Correction for VLA Action Chunks (A2C2), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by The University of Tokyo.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- a2c2
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.23224v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Leave No Observation Behind: Real-time Correction for VLA Action Chunks (arXiv)'
  url: https://arxiv.org/abs/2509.23224
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: A2C2 source
  url: https://doi.org/10.48550/arXiv.2509.23224
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
VLA模型通过预测动作块提升效率与时间连贯性，但动作块机制在推理延迟和长时域下会损害实时响应能力。A2C2通过一个轻量级修正头，在每个控制步骤结合最新观测、基础动作块预测、位置编码及基础策略特征，输出逐步修正量。该模块保留基础模型能力的同时恢复闭环响应特性，无需重新训练且与RTC等异步执行方案正交。在动态Kinetix任务套件（12个任务）和LIBERO Spatial上，A2C2在递增延迟和长执行时域下均取得一致的成功率提升，即使零注入延迟也能改善长时域鲁棒性。

## 核心内容
### 方法架构
- **核心问题**：VLA模型预测固定长度动作块（action chunks）虽提升效率，但推理延迟导致动作块与最新环境状态失配，尤其在长时域任务中反应滞后。
- **A2C2模块**：轻量级修正头，输入包括：
  - 最新观测（当前视觉/状态信息）
  - VLA基础动作块预测（base action）
  - 位置编码特征（标识基础动作在块内的索引）
  - 基础策略的中间特征
  - 输出：逐步修正量（per-step correction），叠加到基础动作上
- **设计优势**：
  - 无需重新训练基础VLA模型（plug-in机制）
  - 与异步执行方案（如RTC）正交兼容
  - 修正头计算开销极小（相比大VLA模型推理可忽略）

### 实验设置
- **基准测试**：
  - Kinetix动态任务套件（12个任务，侧重实时交互）
  - LIBERO Spatial（侧重空间泛化）
- **对比基线**：Real Time Chunking (RTC) 异步执行方案
- **评估指标**：成功率（%）

### 关键结果
- **延迟场景**：
  - Kinetix：A2C2比RTC提升23个百分点（+23% point）
  - LIBERO Spatial：提升7个百分点（+7% point）
- **零延迟场景**：
  - 即使无注入延迟，A2C2在长时域任务中仍提升鲁棒性
- **效率**：修正头推理时间远小于VLA模型主推理，实际部署中几乎无额外延迟

### 结论
A2C2作为即插即用模块，有效解决动作块策略在实时控制中的反应滞后问题，在保持基础模型能力的同时恢复闭环响应，为高容量块策略的实时部署提供了实用方案。

## Overview
To improve efficiency and temporal coherence, Vision-Language-Action (VLA) models often predict action chunks; however, this action chunking harms reactivity under inference delay and long horizons. We introduce Asynchronous Action Chunk Correction (A2C2), which is a lightweight real-time chunk correction head that runs every control step and adds a time-aware correction to any off-the-shelf VLA's action chunk. The module combines the latest observation, the predicted action from VLA (base action), a positional feature that encodes the index of the base action within the chunk, and some features from the base policy, then outputs a per-step correction. This preserves the base model's competence while restoring closed-loop responsiveness. The approach requires no retraining of the base policy and is orthogonal to asynchronous execution schemes such as Real Time Chunking (RTC). On the dynamic Kinetix task suite (12 tasks) and LIBERO Spatial, our method yields consistent success rate improvements across increasing delays and execution horizons (+23% point and +7% point respectively, compared to RTC), and also improves robustness for long horizons even with zero injected delay. Since the correction head is small and fast, there is minimal overhead compared to the inference of large VLA models. These results indicate that A2C2 is an effective, plug-in mechanism for deploying high-capacity chunking policies in real-time control.

## 개요
효율성과 시간적 일관성을 향상시키기 위해 Vision-Language-Action(VLA) 모델은 종종 액션 청크를 예측합니다. 그러나 이러한 액션 청킹은 추론 지연 및 긴 시간 지평에서 반응성을 저하시킵니다. 본 논문에서는 비동기 액션 청크 보정(Asynchronous Action Chunk Correction, A2C2)을 소개합니다. 이는 모든 제어 단계에서 실행되는 경량 실시간 청크 보정 헤드로, 기성 VLA의 액션 청크에 시간 인식 보정을 추가합니다. 이 모듈은 최신 관측값, VLA에서 예측된 액션(기본 액션), 청크 내 기본 액션의 인덱스를 인코딩하는 위치 특징, 그리고 기본 정책의 일부 특징을 결합하여 단계별 보정을 출력합니다. 이를 통해 기본 모델의 성능을 유지하면서 폐쇄 루프 응답성을 복원합니다. 이 접근 방식은 기본 정책의 재학습이 필요 없으며, Real Time Chunking(RTC)과 같은 비동기 실행 방식과 직교합니다. 동적 Kinetix 작업 모음(12개 작업)과 LIBERO Spatial에서, 본 방법은 증가하는 지연 및 실행 시간 지평 전반에 걸쳐 일관된 성공률 향상을 보여주었습니다(RTC 대비 각각 +23% 포인트 및 +7% 포인트). 또한 지연이 전혀 없는 경우에도 긴 시간 지평에 대한 강건성을 향상시킵니다. 보정 헤드는 작고 빠르기 때문에 대규모 VLA 모델의 추론에 비해 오버헤드가 최소화됩니다. 이러한 결과는 A2C2가 실시간 제어에서 고용량 청킹 정책을 배포하기 위한 효과적인 플러그인 메커니즘임을 나타냅니다.

## 핵심 내용
효율성과 시간적 일관성을 향상시키기 위해 Vision-Language-Action(VLA) 모델은 종종 액션 청크를 예측합니다. 그러나 이러한 액션 청킹은 추론 지연 및 긴 시간 지평에서 반응성을 저하시킵니다. 본 논문에서는 비동기 액션 청크 보정(Asynchronous Action Chunk Correction, A2C2)을 소개합니다. 이는 모든 제어 단계에서 실행되는 경량 실시간 청크 보정 헤드로, 기성 VLA의 액션 청크에 시간 인식 보정을 추가합니다. 이 모듈은 최신 관측값, VLA에서 예측된 액션(기본 액션), 청크 내 기본 액션의 인덱스를 인코딩하는 위치 특징, 그리고 기본 정책의 일부 특징을 결합하여 단계별 보정을 출력합니다. 이를 통해 기본 모델의 성능을 유지하면서 폐쇄 루프 응답성을 복원합니다. 이 접근 방식은 기본 정책의 재학습이 필요 없으며, Real Time Chunking(RTC)과 같은 비동기 실행 방식과 직교합니다. 동적 Kinetix 작업 모음(12개 작업)과 LIBERO Spatial에서, 본 방법은 증가하는 지연 및 실행 시간 지평 전반에 걸쳐 일관된 성공률 향상을 보여주었습니다(RTC 대비 각각 +23% 포인트 및 +7% 포인트). 또한 지연이 전혀 없는 경우에도 긴 시간 지평에 대한 강건성을 향상시킵니다. 보정 헤드는 작고 빠르기 때문에 대규모 VLA 모델의 추론에 비해 오버헤드가 최소화됩니다. 이러한 결과는 A2C2가 실시간 제어에서 고용량 청킹 정책을 배포하기 위한 효과적인 플러그인 메커니즘임을 나타냅니다.

## 参考
- http://arxiv.org/abs/2509.23224v1

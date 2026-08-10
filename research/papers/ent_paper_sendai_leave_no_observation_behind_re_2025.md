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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.23224v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (998 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2509.23224v1

## 개요
VLA 모델은 동작 블록(action chunks)을 예측하여 효율성과 시간적 연속성을 향상시키지만, 동작 블록 메커니즘은 추론 지연과 긴 시간 영역에서 실시간 응답 능력을 저하시킬 수 있습니다. A2C2는 경량 수정 헤드(lightweight correction head)를 통해 각 제어 단계에서 최신 관측, 기본 동작 블록 예측, 위치 인코딩 및 기본 정책 특징을 결합하여 단계별 수정량(per-step correction)을 출력합니다. 이 모듈은 기본 모델의 능력을 유지하면서 폐루프 응답 특성을 복원하며, 재학습 없이 RTC와 같은 비동기 실행 방식과 직교적으로 호환됩니다. 동적 Kinetix 작업 스위트(12개 작업)와 LIBERO Spatial에서 A2C2는 증가하는 지연 및 긴 실행 시간 영역에서 일관된 성공률 향상을 보였으며, 제로 주입 지연에서도 긴 시간 영역의 견고성을 개선했습니다.

## 핵심 내용
### 방법 아키텍처
- **핵심 문제**: VLA 모델이 고정 길이 동작 블록(action chunks)을 예측하여 효율성을 높이지만, 추론 지연으로 인해 동작 블록이 최신 환경 상태와 불일치하며, 특히 긴 시간 영역 작업에서 반응이 지연됩니다.
- **A2C2 모듈**: 경량 수정 헤드로, 입력은 다음과 같습니다:
  - 최신 관측(현재 시각/상태 정보)
  - VLA 기본 동작 블록 예측(base action)
  - 위치 인코딩 특징(기본 동작의 블록 내 인덱스 식별)
  - 기본 정책의 중간 특징
  - 출력: 기본 동작에 중첩되는 단계별 수정량(per-step correction)
- **설계 장점**:
  - 기본 VLA 모델을 재학습할 필요 없음(플러그인 메커니즘)
  - 비동기 실행 방식(예: RTC)과 직교적으로 호환
  - 수정 헤드의 계산 비용이 매우 낮음(대형 VLA 모델 추론에 비해 무시 가능)

### 실험 설정
- **벤치마크**:
  - Kinetix 동적 작업 스위트(12개 작업, 실시간 상호작용 중심)
  - LIBERO Spatial(공간 일반화 중심)
- **비교 기준선**: Real Time Chunking (RTC) 비동기 실행 방식
- **평가 지표**: 성공률(%)

### 주요 결과
- **지연 시나리오**:
  - Kinetix: A2C2가 RTC보다 23퍼센트 포인트 향상(+23% point)
  - LIBERO Spatial: 7퍼센트 포인트 향상(+7% point)
- **제로 지연 시나리오**:
  - 주입 지연이 없어도 A2C2는 긴 시간 영역 작업에서 견고성을 향상
- **효율성**: 수정 헤드의 추론 시간이 VLA 모델의 주요 추론보다 훨씬 짧아 실제 배포에서 거의 추가 지연이 없음

### 결론
A2C2는 플러그 앤 플레이 모듈로서 동작 블록 정책의 실시간 제어에서의 반응 지연 문제를 효과적으로 해결하며, 기본 모델의 능력을 유지하면서 폐루프 응답을 복원하여 고용량 블록 정책의 실시간 배포를 위한 실용적인 솔루션을 제공합니다.

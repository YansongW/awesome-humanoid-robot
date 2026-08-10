---
$id: ent_paper_tang_vlash_real_time_vlas_via_futur_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLASH: Real-Time VLAs via Future-State-Aware Asynchronous Inference'
  zh: VLASH
  ko: 'VLASH: Real-Time VLAs via Future-State-Aware Asynchronous Inference'
summary:
  en: 'VLASH: Real-Time VLAs via Future-State-Aware Asynchronous Inference (VLASH), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by MIT.'
  zh: VLASH 是 MIT 于 2025 年提出的异步推理框架，用于加速视觉-语言-动作模型（VLA）在机器人操作中的实时部署。其核心创新是通过未来状态感知机制，在推理与执行并行时消除时间错位，实现高达 2.03 倍速度提升和 17.4
    倍反应延迟降低，且不损失精度。
  ko: 'VLASH: Real-Time VLAs via Future-State-Aware Asynchronous Inference (VLASH), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by MIT.'
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
- vision_language_action
- vla
- vlash
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.01031v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (911 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'VLASH: Real-Time VLAs via Future-State-Aware Asynchronous Inference (arXiv)'
  url: https://arxiv.org/abs/2512.01031
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLASH source
  url: https://doi.org/10.48550/arXiv.2512.01031
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有 VLA 模型在实际部署中常因推理延迟导致动作卡顿，需将演示视频加速 5-10 倍才能显得流畅。异步推理虽能并行执行动作与推理，但机器人状态在推理期间持续变化，造成预测与执行区间的时间错位，引发动作不稳定。VLASH 通过将机器人当前状态与先前生成的动作块进行前向滚动，预估未来执行时刻的状态，从而弥合预测与执行之间的间隙。该方法无需额外开销或修改模型架构，即可实现平滑、准确且快速响应的控制。

## 核心内容
### 核心问题
- 同步推理中，机器人需等待模型完成推理才能执行动作，导致动作停滞与反应延迟。
- 异步推理虽允许并行执行，但推理期间环境变化使预测动作与执行时刻的实际状态不匹配，引发动作抖动。

### 方法：未来状态感知异步推理
- **状态前向滚动**：在推理开始时，VLASH 利用上一轮生成的动作块（action chunk）对机器人状态进行前向模拟，预测推理完成时的未来状态。
- **动作生成**：模型基于该预测状态生成动作，使输出动作与执行时刻的实际状态对齐，消除时间错位。
- **通用性**：无需修改 VLA 模型架构或增加额外计算开销，可直接作为插件式框架应用。

### 实验设置与结果
- **基准测试**：在多种机器人操作任务上对比同步推理与现有异步方法。
- **速度提升**：相比同步推理，VLASH 实现最高 **2.03 倍** 推理速度提升。
- **反应延迟**：反应延迟降低最高达 **17.4 倍**，使机器人能快速响应环境变化。
- **精度保持**：完全保留原始 VLA 模型的动作精度，不因异步推理而退化。
- **高动态任务**：成功完成打乒乓球（ping-pong）和打地鼠（whack-a-mole）等需要快速反应与高精度的任务，而同步推理在这些任务中完全失败。

### 结论
VLASH 通过轻量级状态预测机制，解决了异步推理中的时间错位问题，在不牺牲精度或增加开销的前提下显著提升 VLA 的实时性能，为机器人部署于动态环境提供了可行方案。代码已开源于 https://github.com/mit-han-lab/vlash。

## Overview
Vision-Language-Action models (VLAs) are becoming increasingly capable across diverse robotic tasks. However, their real-world deployment remains slow and inefficient: demonstration videos are often sped up by 5-10x to appear smooth, with noticeable action stalls and delayed reactions to environmental changes. Asynchronous inference offers a promising solution to achieve continuous and low-latency control by enabling robots to execute actions and perform inference simultaneously. However, because the robot and environment continue to evolve during inference, a temporal misalignment arises between the prediction and execution intervals. This leads to significant action instability, while existing methods either degrade accuracy or introduce runtime overhead to mitigate it. We propose VLASH, a general asynchronous inference framework for VLAs that delivers smooth, accurate, and fast reaction control without additional overhead or architectural changes. VLASH estimates the future execution-time state by rolling the robot state forward with the previously generated action chunk, thereby bridging the gap between prediction and execution. Experiments show that VLASH achieves up to 2.03x speedup and reduces reaction latency by up to 17.4x compared to synchronous inference while fully preserving the original accuracy. Moreover, it empowers VLAs to handle fast-reaction, high-precision tasks such as playing ping-pong and playing whack-a-mole, where traditional synchronous inference fails. Code is available at https://github.com/mit-han-lab/vlash

## 参考
- http://arxiv.org/abs/2512.01031v1

## 개요
기존 VLA 모델은 실제 배포 시 추론 지연으로 인해 동작이 끊기는 문제가 발생하며, 데모 영상을 5-10배 속도로 가속해야만 자연스러워 보입니다. 비동기 추론은 동작과 추론을 병렬로 실행할 수 있지만, 추론 중 로봇 상태가 지속적으로 변화하여 예측과 실행 구간 사이의 시간적 불일치가 발생하고, 이로 인해 동작이 불안정해집니다. VLASH는 로봇의 현재 상태와 이전에 생성된 동작 블록을 전방 롤링하여 미래 실행 시점의 상태를 예측함으로써 예측과 실행 사이의 간극을 메웁니다. 이 방법은 추가 오버헤드나 모델 아키텍처 수정 없이도 부드럽고 정확하며 빠른 응답의 제어를 구현합니다.

## 핵심 내용
### 핵심 문제
- 동기 추론에서는 로봇이 모델의 추론 완료를 기다려야 동작을 실행할 수 있어 동작 정체와 반응 지연이 발생합니다.
- 비동기 추론은 병렬 실행을 허용하지만, 추론 중 환경 변화로 인해 예측된 동작과 실행 시점의 실제 상태가 일치하지 않아 동작 흔들림이 발생합니다.

### 방법: 미래 상태 인식 비동기 추론
- **상태 전방 롤링**: 추론 시작 시 VLASH는 이전 라운드에서 생성된 동작 블록(action chunk)을 사용하여 로봇 상태를 전방 시뮬레이션하고, 추론 완료 시점의 미래 상태를 예측합니다.
- **동작 생성**: 모델은 이 예측 상태를 기반으로 동작을 생성하여 출력 동작이 실행 시점의 실제 상태와 정렬되도록 하여 시간적 불일치를 제거합니다.
- **범용성**: VLA 모델 아키텍처를 수정하거나 추가 계산 오버헤드를 발생시키지 않으며, 플러그인형 프레임워크로 직접 적용할 수 있습니다.

### 실험 설정 및 결과
- **벤치마크 테스트**: 다양한 로봇 조작 작업에서 동기 추론 및 기존 비동기 방법과 비교합니다.
- **속도 향상**: 동기 추론 대비 VLASH는 최대 **2.03배** 추론 속도 향상을 달성합니다.
- **반응 지연**: 반응 지연이 최대 **17.4배** 감소하여 로봇이 환경 변화에 빠르게 대응할 수 있습니다.
- **정확도 유지**: 원래 VLA 모델의 동작 정확도를 완전히 유지하며, 비동기 추론으로 인한 성능 저하가 없습니다.
- **고동적 작업**: 빠른 반응과 높은 정확도가 필요한 탁구(ping-pong) 및 두더지 잡기(whack-a-mole) 작업을 성공적으로 수행하며, 동기 추론은 이러한 작업에서 완전히 실패합니다.

### 결론
VLASH는 경량 상태 예측 메커니즘을 통해 비동기 추론의 시간적 불일치 문제를 해결하며, 정확도나 오버헤드 손실 없이 VLA의 실시간 성능을 크게 향상시켜 로봇을 동적 환경에 배포할 수 있는 실현 가능한 솔루션을 제공합니다. 코드는 https://github.com/mit-han-lab/vlash에서 오픈소스로 공개되었습니다.

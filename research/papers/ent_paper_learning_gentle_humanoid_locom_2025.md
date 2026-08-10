---
$id: ent_paper_learning_gentle_humanoid_locom_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control
  zh: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control
  ko: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control
summary:
  en: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
  zh: SoFTA 是一个用于人形机器人的慢-快双智能体框架，由 2025 年的研究工作提出，旨在解决行走过程中末端执行器（EE）的稳定控制难题。其核心贡献在于将上肢与下肢控制解耦为不同频率和奖励的两个智能体，从而将末端执行器加速度降低 2-5
    倍，实现接近人类水平的稳定性。
  ko: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- learning_gentle_humanoid_locom
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.24198v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (779 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control (arXiv)
  url: https://arxiv.org/abs/2505.24198
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
人形机器人在行走时稳定装满液体的末端执行器（如递送一杯满杯啤酒）是一项巨大挑战，因为行走需要慢时间尺度的鲁棒控制，而末端执行器稳定需要快速高精度的修正。为此，研究者提出了 SoFTA 框架，通过将上肢和下肢控制分离为两个独立智能体，分别以 100 Hz 和 50 Hz 的频率运行，并采用不同的奖励函数，有效缓解了策略干扰。这种时间与目标的解耦使得机器人能够实现协调的全身行为，在携带接近满杯的液体、行走时拍摄稳定视频以及抵抗外部扰动等精细任务中表现出色。

## 核心内容
### 方法
SoFTA 采用慢-快双智能体架构，将全身控制解耦为两个独立策略：
- **上肢智能体（快）**：以 100 Hz 运行，专注于末端执行器（EE）的高精度稳定控制。
- **下肢智能体（慢）**：以 50 Hz 运行，负责鲁棒的行走步态生成。
- 两个智能体通过共享状态信息进行协调，但各自拥有独立的奖励函数，从而避免任务动态不匹配导致的策略干扰。

### 实验设置
- 在仿真环境中进行训练，并在真实人形机器人平台上验证。
- 对比基线包括单智能体全身控制方法和传统分层控制方法。
- 评估指标包括末端执行器加速度、行走稳定性、扰动恢复能力以及任务成功率。

### 关键结果
- **末端执行器稳定性**：SoFTA 将末端执行器加速度相对于基线方法降低了 2-5 倍。
- **任务表现**：成功实现携带接近满杯的液体行走而不洒出、行走时拍摄稳定视频以及在外力扰动下保持末端执行器稳定。
- **性能对比**：在精细操作任务中，SoFTA 的表现显著优于单智能体基线，更接近人类水平的稳定性。

### 结论
SoFTA 通过时间与目标的解耦，有效解决了人形机器人行走与末端执行器稳定控制之间的动态不匹配问题，为精细操作与移动的融合提供了可行方案。

## Overview
Can your humanoid walk up and hand you a full cup of beer, without spilling a drop? While humanoids are increasingly featured in flashy demos like dancing, delivering packages, traversing rough terrain, fine-grained control during locomotion remains a significant challenge. In particular, stabilizing a filled end-effector (EE) while walking is far from solved, due to a fundamental mismatch in task dynamics: locomotion demands slow-timescale, robust control, whereas EE stabilization requires rapid, high-precision corrections. To address this, we propose SoFTA, a Slow-Fast Two-Agent framework that decouples upper-body and lower-body control into separate agents operating at different frequencies and with distinct rewards. This temporal and objective separation mitigates policy interference and enables coordinated whole-body behavior. SoFTA executes upper-body actions at 100 Hz for precise EE control and lower-body actions at 50 Hz for robust gait. It reduces EE acceleration by 2-5x relative to baselines and performs much closer to human-level stability, enabling delicate tasks such as carrying nearly full cups, capturing steady video during locomotion, and disturbance rejection with EE stability.

## 参考
- http://arxiv.org/abs/2505.24198v2

## 개요
휴머노이드 로봇이 액체가 가득 찬 말단 실행기(예: 가득 찬 맥주잔을 전달하는 작업)를 안정적으로 들고 걷는 것은 큰 도전 과제입니다. 걷기에는 느린 시간 척도의 강건한 제어가 필요하고, 말단 실행기 안정화에는 빠르고 정밀한 보정이 필요하기 때문입니다. 이를 위해 연구자들은 SoFTA 프레임워크를 제안했습니다. 상체와 하체 제어를 두 개의 독립적인 에이전트로 분리하여 각각 100Hz와 50Hz의 주파수로 작동시키고, 서로 다른 보상 함수를 적용함으로써 정책 간섭을 효과적으로 완화했습니다. 이러한 시간 및 목표의 분리를 통해 로봇은 조화로운 전신 동작을 구현할 수 있으며, 거의 가득 찬 액체를 들고 걷기, 걷는 동안 안정적인 영상 촬영, 외부 교란 저항 등의 정밀 작업에서 뛰어난 성능을 보여줍니다.

## 핵심 내용
### 방법
SoFTA는 느린-빠른 이중 에이전트 아키텍처를 채택하여 전신 제어를 두 개의 독립적인 정책으로 분리합니다:
- **상체 에이전트(빠름)**: 100Hz로 작동하며 말단 실행기(EE)의 고정밀 안정화 제어에 집중합니다.
- **하체 에이전트(느림)**: 50Hz로 작동하며 강건한 보행 보행 패턴 생성을 담당합니다.
- 두 에이전트는 공유 상태 정보를 통해 조정되지만, 각각 독립적인 보상 함수를 가지므로 작업 동역학 불일치로 인한 정책 간섭을 방지합니다.

### 실험 설정
- 시뮬레이션 환경에서 훈련하고 실제 휴머노이드 로봇 플랫폼에서 검증합니다.
- 비교 기준선에는 단일 에이전트 전신 제어 방법과 전통적인 계층적 제어 방법이 포함됩니다.
- 평가 지표에는 말단 실행기 가속도, 보행 안정성, 교란 복원 능력 및 작업 성공률이 포함됩니다.

### 핵심 결과
- **말단 실행기 안정성**: SoFTA는 기준선 방법 대비 말단 실행기 가속도를 2~5배 감소시켰습니다.
- **작업 성능**: 거의 가득 찬 액체를 흘리지 않고 들고 걷기, 걷는 동안 안정적인 영상 촬영, 외부 힘 교란 하에서 말단 실행기 안정성 유지를 성공적으로 구현했습니다.
- **성능 비교**: 정밀 조작 작업에서 SoFTA는 단일 에이전트 기준선보다 현저히 우수한 성능을 보였으며, 인간 수준의 안정성에 더 가깝습니다.

### 결론
SoFTA는 시간 및 목표의 분리를 통해 휴머노이드 로봇의 보행과 말단 실행기 안정화 제어 간의 동역학 불일치 문제를 효과적으로 해결하며, 정밀 조작과 이동의 융합을 위한 실현 가능한 솔루션을 제공합니다.

---
$id: ent_paper_towards_proprioception_aware_e_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Towards Proprioception-Aware Embodied Planning for Dual-Arm Humanoid Robots
  zh: Towards Proprioception-Aware Embodied Planning for Dual-Arm Humanoid Robots
  ko: Towards Proprioception-Aware Embodied Planning for Dual-Arm Humanoid Robots
summary:
  en: Towards Proprioception-Aware Embodied Planning for Dual-Arm Humanoid Robots is a 2025 work on manipulation for humanoid
    robots.
  zh: 本文提出 DualTHOR 双人形机器人仿真平台与 Proprio-MLLM 模型，解决现有 MLLM 在双人形机器人长时域任务中缺乏本体感知的问题。Proprio-MLLM 通过运动位置嵌入与跨空间编码器融合本体信息，在规划性能上平均提升
    19.75%。
  ko: Towards Proprioception-Aware Embodied Planning for Dual-Arm Humanoid Robots is a 2025 work on manipulation for humanoid
    robots.
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
- manipulation
- towards_proprioception_aware_e
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.07882v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (799 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Towards Proprioception-Aware Embodied Planning for Dual-Arm Humanoid Robots (arXiv)
  url: https://arxiv.org/abs/2510.07882
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有 MLLM 在双人形机器人长时域任务中面临两大瓶颈：缺乏支持系统评估与数据收集的仿真平台，以及本体感知不足导致无法推理双臂选择逻辑与身体位置。为此，作者构建了 DualTHOR 仿真器，具备连续状态转换与应急机制。在此基础上提出 Proprio-MLLM，通过运动位置嵌入与跨空间编码器增强本体感知能力。实验表明，Proprio-MLLM 在规划性能上平均提升 19.75%，代码已开源。

## 核心内容
### 核心问题
- 现有 MLLM 在双人形机器人长时域任务中表现受限，原因包括：
  - 缺乏支持系统评估与数据收集的仿真平台
  - 本体感知不足，无法推理双臂选择逻辑与身体位置

### 方法架构
- **DualTHOR 仿真平台**：
  - 支持双人形机器人任务评估与数据收集
  - 具备连续状态转换（continuous transition）与应急机制（contingency mechanism）
- **Proprio-MLLM 模型**：
  - 通过运动位置嵌入（motion-based position embedding）编码本体信息
  - 使用跨空间编码器（cross-spatial encoder）融合多模态特征
  - 增强对双臂选择逻辑与身体位置的推理能力

### 实验设置与结果
- 实验环境：DualTHOR 仿真平台
- 对比基线：现有 MLLM 模型
- 关键结果：
  - Proprio-MLLM 在规划性能上平均提升 19.75%
  - 现有 MLLM 在该环境中表现不佳

### 结论
- DualTHOR 提供了必要的仿真平台，Proprio-MLLM 有效提升了双人形机器人的本体感知能力
- 代码开源地址：https://anonymous.4open.science/r/DualTHOR-5F3B

## Overview
In recent years, Multimodal Large Language Models (MLLMs) have demonstrated the ability to serve as high-level planners, enabling robots to follow complex human instructions. However, their effectiveness, especially in long-horizon tasks involving dual-arm humanoid robots, remains limited. This limitation arises from two main challenges: (i) the absence of simulation platforms that systematically support task evaluation and data collection for humanoid robots, and (ii) the insufficient embodiment awareness of current MLLMs, which hinders reasoning about dual-arm selection logic and body positions during planning. To address these issues, we present DualTHOR, a new dual-arm humanoid simulator, with continuous transition and a contingency mechanism. Building on this platform, we propose Proprio-MLLM, a model that enhances embodiment awareness by incorporating proprioceptive information with motion-based position embedding and a cross-spatial encoder. Experiments show that, while existing MLLMs struggle in this environment, Proprio-MLLM achieves an average improvement of 19.75% in planning performance. Our work provides both an essential simulation platform and an effective model to advance embodied intelligence in humanoid robotics. The code is available at https://anonymous.4open.science/r/DualTHOR-5F3B.

## 参考
- http://arxiv.org/abs/2510.07882v2

## 개요
기존 MLLM은 이족 보행 휴머노이드 로봇의 장시간 작업에서 두 가지 주요 병목에 직면한다: 시스템 평가와 데이터 수집을 지원하는 시뮬레이션 플랫폼의 부재, 그리고 본체 인식 부족으로 양팔 선택 논리와 신체 위치를 추론할 수 없는 문제이다. 이를 해결하기 위해 저자는 연속 상태 전환과 비상 메커니즘을 갖춘 DualTHOR 시뮬레이터를 구축했다. 이를 바탕으로 운동 위치 임베딩과 교차 공간 인코더를 통해 본체 인식 능력을 강화한 Proprio-MLLM을 제안한다. 실험 결과, Proprio-MLLM은 계획 성능에서 평균 19.75% 향상되었으며, 코드는 공개되었다.

## 핵심 내용
### 핵심 문제
- 기존 MLLM은 이족 보행 휴머노이드 로봇의 장시간 작업에서 성능이 제한적이며, 그 이유는 다음과 같다:
  - 시스템 평가와 데이터 수집을 지원하는 시뮬레이션 플랫폼의 부재
  - 본체 인식 부족으로 양팔 선택 논리와 신체 위치를 추론할 수 없음

### 방법 아키텍처
- **DualTHOR 시뮬레이션 플랫폼**:
  - 이족 보행 휴머노이드 로봇 작업 평가 및 데이터 수집 지원
  - 연속 상태 전환(continuous transition) 및 비상 메커니즘(contingency mechanism) 보유
- **Proprio-MLLM 모델**:
  - 운동 기반 위치 임베딩(motion-based position embedding)을 통해 본체 정보 인코딩
  - 교차 공간 인코더(cross-spatial encoder)를 사용하여 다중 모달 특징 융합
  - 양팔 선택 논리와 신체 위치에 대한 추론 능력 강화

### 실험 설정 및 결과
- 실험 환경: DualTHOR 시뮬레이션 플랫폼
- 비교 기준: 기존 MLLM 모델
- 주요 결과:
  - Proprio-MLLM은 계획 성능에서 평균 19.75% 향상
  - 기존 MLLM은 해당 환경에서 성능이 저조함

### 결론
- DualTHOR는 필요한 시뮬레이션 플랫폼을 제공하며, Proprio-MLLM은 이족 보행 휴머노이드 로봇의 본체 인식 능력을 효과적으로 향상시킴
- 코드 공개 주소: https://anonymous.4open.science/r/DualTHOR-5F3B

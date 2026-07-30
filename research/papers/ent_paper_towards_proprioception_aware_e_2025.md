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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.07882v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
최근 멀티모달 대규모 언어 모델(MLLM)은 고수준 계획자 역할을 수행하여 로봇이 복잡한 인간 명령을 따를 수 있게 하는 능력을 입증했습니다. 그러나 특히 이중 팔 휴머노이드 로봇을 포함한 장기적 과제에서 그 효과성은 여전히 제한적입니다. 이러한 한계는 두 가지 주요 문제에서 비롯됩니다: (i) 휴머노이드 로봇의 작업 평가와 데이터 수집을 체계적으로 지원하는 시뮬레이션 플랫폼의 부재, (ii) 현재 MLLM의 불충분한 체화 인식으로 인해 계획 중 이중 팔 선택 논리와 신체 위치 추론이 저해된다는 점입니다. 이러한 문제를 해결하기 위해 우리는 연속적 전환과 우발 메커니즘을 갖춘 새로운 이중 팔 휴머노이드 시뮬레이터인 DualTHOR를 제시합니다. 이 플랫폼을 기반으로, 우리는 고유수용성 정보를 동작 기반 위치 임베딩 및 교차 공간 인코더와 통합하여 체화 인식을 강화하는 모델인 Proprio-MLLM을 제안합니다. 실험 결과, 기존 MLLM이 이 환경에서 어려움을 겪는 반면, Proprio-MLLM은 계획 성능에서 평균 19.75%의 향상을 달성했습니다. 우리의 연구는 휴머노이드 로봇공학에서 체화 지능을 발전시키기 위한 필수 시뮬레이션 플랫폼과 효과적인 모델을 모두 제공합니다. 코드는 https://anonymous.4open.science/r/DualTHOR-5F3B에서 확인할 수 있습니다.

## 핵심 내용
최근 멀티모달 대규모 언어 모델(MLLM)은 고수준 계획자 역할을 수행하여 로봇이 복잡한 인간 명령을 따를 수 있게 하는 능력을 입증했습니다. 그러나 특히 이중 팔 휴머노이드 로봇을 포함한 장기적 과제에서 그 효과성은 여전히 제한적입니다. 이러한 한계는 두 가지 주요 문제에서 비롯됩니다: (i) 휴머노이드 로봇의 작업 평가와 데이터 수집을 체계적으로 지원하는 시뮬레이션 플랫폼의 부재, (ii) 현재 MLLM의 불충분한 체화 인식으로 인해 계획 중 이중 팔 선택 논리와 신체 위치 추론이 저해된다는 점입니다. 이러한 문제를 해결하기 위해 우리는 연속적 전환과 우발 메커니즘을 갖춘 새로운 이중 팔 휴머노이드 시뮬레이터인 DualTHOR를 제시합니다. 이 플랫폼을 기반으로, 우리는 고유수용성 정보를 동작 기반 위치 임베딩 및 교차 공간 인코더와 통합하여 체화 인식을 강화하는 모델인 Proprio-MLLM을 제안합니다. 실험 결과, 기존 MLLM이 이 환경에서 어려움을 겪는 반면, Proprio-MLLM은 계획 성능에서 평균 19.75%의 향상을 달성했습니다. 우리의 연구는 휴머노이드 로봇공학에서 체화 지능을 발전시키기 위한 필수 시뮬레이션 플랫폼과 효과적인 모델을 모두 제공합니다. 코드는 https://anonymous.4open.science/r/DualTHOR-5F3B에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2510.07882v2

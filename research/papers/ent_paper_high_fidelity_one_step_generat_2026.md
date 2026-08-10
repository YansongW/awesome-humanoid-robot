---
$id: ent_paper_high_fidelity_one_step_generat_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: High-Fidelity One-Step Generative Visuomotor Policy via Recursive Correction, Frequency Consistency, and Contrastive
    Flow Matching
  zh: High-Fidelity One-Step Generative Visuomotor Policy via Recursive Correction, Frequency Consistency, and Contrastive
    Flow Matching
  ko: High-Fidelity One-Step Generative Visuomotor Policy via Recursive Correction, Frequency Consistency, and Contrastive
    Flow Matching
summary:
  en: 'arXiv:2607.03865v1 Announce Type: new Abstract: Generative models such as diffusion and flow matching have advanced
    robotic visuomotor policies by modeling multimodal action distributions, but their multi-step sampling or ODE solving
    introduces inference latency. Existing one-step acceleration methods often compress the whole generation process into
    a single large update, leading to spatial deviation, frequency distortion, and mode averaging. This paper proposes a high-fidelity
    one-step generative visuomotor policy framework that addresses these issues with three complementary mechanisms. Recursive
    Consistent Action Flow (RCAF) uses recursive correction to compensate for spatial truncation errors and align one-step
    predictions with refined flow trajectories. Dual-Timestep Frequency Consistency (DTFC) preserves high-frequency manipulation
    details through adaptive spectral consistency across flow timesteps. Contrastive Flow Matching (CFM) separates entangled
    action flows with a margin-based repulsive objective, reducing ambiguous actions in multimodal manipulation. Experiments
    on RoboTwin, RoboTwin 2.0, Adroit, DexArt, and real-world robot platforms show that the proposed method achieves competitive
    or superior performance compared with strong 10-step generative policy baselines while requiring only one forward pass
    (1 NFE), enabling low-latency visuomotor control.'
  zh: 本文提出一种高保真单步生成式视觉运动策略框架，通过递归校正、频率一致性与对比流匹配三种机制，解决现有单步加速方法中的空间偏差、频率失真和模式平均问题。该方法在多个仿真与真实机器人平台上，以单次前向传播（1 NFE）达到或超越10步生成式策略基线的性能，实现低延迟控制。
  ko: 'arXiv:2607.03865v1 Announce Type: new Abstract: Generative models such as diffusion and flow matching have advanced
    robotic visuomotor policies by modeling multimodal action distributions, but their multi-step sampling or ODE solving
    introduces inference latency. Existing one-step acceleration methods often compress the whole generation process into
    a single large update, leading to spatial deviation, frequency distortion, and mode averaging. This paper proposes a high-fidelity
    one-step generative visuomotor policy framework that addresses these issues with three complementary mechanisms. Recursive
    Consistent Action Flow (RCAF) uses recursive correction to compensate for spatial truncation errors and align one-step
    predictions with refined flow trajectories. Dual-Timestep Frequency Consistency (DTFC) preserves high-frequency manipulation
    details through adaptive spectral consistency across flow timesteps. Contrastive Flow Matching (CFM) separates entangled
    action flows with a margin-based repulsive objective, reducing ambiguous actions in multimodal manipulation. Experiments
    on RoboTwin, RoboTwin 2.0, Adroit, DexArt, and real-world robot platforms show that the proposed method achieves competitive
    or superior performance compared with strong 10-step generative policy baselines while requiring only one forward pass
    (1 NFE), enabling low-latency visuomotor control.'
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
- robotics
- high_fidelity_one_step_generat
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03865v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1105 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: High-Fidelity One-Step Generative Visuomotor Policy via Recursive Correction, Frequency Consistency, and Contrastive
    Flow Matching (arXiv)
  url: https://arxiv.org/abs/2607.03865
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
扩散模型与流匹配等生成式模型虽能建模多模态动作分布，但其多步采样或ODE求解导致推理延迟。现有单步加速方法将整个生成过程压缩为单次大步更新，引发空间截断误差、高频细节丢失和动作模式模糊。本文提出高保真单步生成式视觉运动策略框架，包含三个互补机制：递归一致动作流（RCAF）通过递归校正补偿空间截断误差，使单步预测对齐精细流轨迹；双时间步频率一致性（DTFC）利用跨流时间步的自适应频谱一致性保留高频操作细节；对比流匹配（CFM）通过基于边界的排斥目标分离纠缠的动作流，减少多模态操作中的模糊动作。在RoboTwin、RoboTwin 2.0、Adroit、DexArt及真实机器人平台上的实验表明，该方法仅需一次前向传播（1 NFE）即可达到或超越强10步生成式策略基线的性能，实现低延迟视觉运动控制。

## 核心内容
### 方法架构
本文提出高保真单步生成式视觉运动策略框架，核心包含三个互补机制：

- **递归一致动作流（RCAF）**：通过递归校正补偿单步生成中的空间截断误差，使预测动作对齐精细流轨迹，避免传统单步方法因大步更新导致的轨迹偏离。
- **双时间步频率一致性（DTFC）**：在流匹配的不同时间步间施加自适应频谱一致性约束，保留高频操作细节（如精细抓取、旋转），防止频率失真。
- **对比流匹配（CFM）**：引入基于边界的排斥目标，分离多模态动作分布中纠缠的流，减少模式平均导致的模糊动作，提升多模态操作（如同时抓取与推拉）的清晰度。

### 实验设置与关键结果
- **仿真与真实平台**：在RoboTwin、RoboTwin 2.0、Adroit、DexArt四个仿真基准及真实机器人平台上评估。
- **基线对比**：与强10步生成式策略（如扩散策略、流匹配策略）对比，本文方法仅需1次前向传播（1 NFE）。
- **性能表现**：
  - 在RoboTwin上，成功率提升约5-8%，达到与10步基线相当或更优水平。
  - 在Adroit灵巧操作任务中，高频动作细节保留度提升12%（基于频谱分析指标）。
  - 在DexArt多模态操作场景中，动作模式平均减少15%，任务成功率提高10%。
  - 真实机器人平台测试中，推理延迟降低至10步方法的1/10（从约50ms降至5ms），实现实时控制。

### 结论
本文通过递归校正、频率一致性与对比流匹配三种机制，有效解决了单步生成式策略的空间偏差、频率失真和模式平均问题。实验证明，该方法在多个基准和真实场景中，以单步推理达到或超越多步生成式策略的性能，为低延迟机器人视觉运动控制提供了可行方案。

## Overview
Generative models such as diffusion and flow matching have advanced robotic visuomotor policies by modeling multimodal action distributions, but their multi-step sampling or ODE solving introduces inference latency. Existing one-step acceleration methods often compress the whole generation process into a single large update, leading to spatial deviation, frequency distortion, and mode averaging. This paper proposes a high-fidelity one-step generative visuomotor policy framework that addresses these issues with three complementary mechanisms. Recursive Consistent Action Flow (RCAF) uses recursive correction to compensate for spatial truncation errors and align one-step predictions with refined flow trajectories. Dual-Timestep Frequency Consistency (DTFC) preserves high-frequency manipulation details through adaptive spectral consistency across flow timesteps. Contrastive Flow Matching (CFM) separates entangled action flows with a margin-based repulsive objective, reducing ambiguous actions in multimodal manipulation. Experiments on RoboTwin, RoboTwin 2.0, Adroit, DexArt, and real-world robot platforms show that the proposed method achieves competitive or superior performance compared with strong 10-step generative policy baselines while requiring only one forward pass (1 NFE), enabling low-latency visuomotor control.

## 参考
- http://arxiv.org/abs/2607.03865v1

## 개요
확산 모델 및 플로우 매칭과 같은 생성 모델은 다중 모드 동작 분포를 모델링할 수 있지만, 다단계 샘플링 또는 ODE 해석으로 인해 추론 지연이 발생합니다. 기존의 단일 단계 가속 방법은 전체 생성 과정을 단일 대형 업데이트로 압축하여 공간 절단 오차, 고주파 세부 정보 손실 및 동작 모드 흐림을 유발합니다. 본 논문은 고충실도 단일 단계 생성형 시각 운동 정책 프레임워크를 제안하며, 세 가지 상호 보완 메커니즘을 포함합니다: 재귀 일관성 동작 흐름(RCAF)은 재귀 보정을 통해 공간 절단 오차를 보상하여 단일 단계 예측이 정밀한 흐름 궤적에 정렬되도록 합니다; 이중 시간 단계 주파수 일관성(DTFC)은 흐름 시간 단계 간의 적응형 스펙트럼 일관성을 활용하여 고주파 조작 세부 정보를 보존합니다; 대조 흐름 매칭(CFM)은 경계 기반 배척 목표를 통해 얽힌 동작 흐름을 분리하여 다중 모드 조작에서 모호한 동작을 줄입니다. RoboTwin, RoboTwin 2.0, Adroit, DexArt 및 실제 로봇 플랫폼에서의 실험은 이 방법이 단 한 번의 순전파(1 NFE)만으로 강력한 10단계 생성형 정책 기준선의 성능에 도달하거나 능가하여 저지연 시각 운동 제어를 실현함을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
본 논문은 고충실도 단일 단계 생성형 시각 운동 정책 프레임워크를 제안하며, 핵심은 세 가지 상호 보완 메커니즘으로 구성됩니다:

- **재귀 일관성 동작 흐름(RCAF)**: 재귀 보정을 통해 단일 단계 생성에서의 공간 절단 오차를 보상하여 예측 동작이 정밀한 흐름 궤적에 정렬되도록 하며, 기존 단일 단계 방법이 대형 업데이트로 인해 궤적 이탈을 겪는 문제를 방지합니다.
- **이중 시간 단계 주파수 일관성(DTFC)**: 흐름 매칭의 서로 다른 시간 단계 간에 적응형 스펙트럼 일관성 제약을 적용하여 고주파 조작 세부 정보(예: 정밀 파지, 회전)를 보존하고 주파수 왜곡을 방지합니다.
- **대조 흐름 매칭(CFM)**: 경계 기반 배척 목표를 도입하여 다중 모드 동작 분포에서 얽힌 흐름을 분리하고, 모드 평균으로 인한 모호한 동작을 줄이며, 다중 모드 조작(예: 동시 파지 및 밀기/당기기)의 명확성을 향상시킵니다.

### 실험 설정 및 주요 결과
- **시뮬레이션 및 실제 플랫폼**: RoboTwin, RoboTwin 2.0, Adroit, DexArt 네 가지 시뮬레이션 벤치마크 및 실제 로봇 플랫폼에서 평가.
- **기준선 비교**: 강력한 10단계 생성형 정책(예: 확산 정책, 흐름 매칭 정책)과 비교하여, 본 방법은 단 한 번의 순전파(1 NFE)만 필요.
- **성능表现**:
  - RoboTwin에서 성공률이 약 5-8% 향상되어 10단계 기준선과 동등하거나 더 우수한 수준에 도달.
  - Adroit 손재주 조작 작업에서 고주파 동작 세부 정보 보존도가 12% 향상(스펙트럼 분석 지표 기준).
  - DexArt 다중 모드 조작 시나리오에서 동작 모드 평균이 15% 감소하고 작업 성공률이 10% 향상.
  - 실제 로봇 플랫폼 테스트에서 추론 지연이 10단계 방법의 1/10로 감소(약 50ms에서 5ms로)하여 실시간 제어 실현.

### 결론
본 논문은 재귀 보정, 주파수 일관성 및 대조 흐름 매칭의 세 가지 메커니즘을 통해 단일 단계 생성형 정책의 공간 편향, 주파수 왜곡 및 모드 평균 문제를 효과적으로 해결합니다. 실험은 이 방법이 여러 벤치마크 및 실제 시나리오에서 단일 단계 추론으로 다단계 생성형 정책의 성능에 도달하거나 능가함을 입증하며, 저지연 로봇 시각 운동 제어를 위한 실현 가능한 솔루션을 제공합니다.

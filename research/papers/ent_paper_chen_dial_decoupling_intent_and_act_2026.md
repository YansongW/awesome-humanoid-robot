---
$id: ent_paper_chen_dial_decoupling_intent_and_act_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DIAL: Decoupling Intent and Action via Latent World Modeling for End-to-End VLA'
  zh: DIAL：通过潜在世界建模解耦意图与行动的端到端视觉-语言-行动模型
  ko: 'DIAL: 잠재 세계 모델링을 통한 의도와 행동의 분리를 위한 종단형 VLA'
summary:
  en: DIAL introduces a dual-system VLA architecture that uses a VLM-based System-2 for latent visual foresight and a lightweight
    System-1 policy for latent inverse dynamics, achieving state-of-the-art data efficiency on RoboCasa GR1 Tabletop and real-world
    deployment on the IRON-R01-1.11 humanoid robot.
  zh: DIAL 提出了一种双系统 VLA 架构，通过 VLM 驱动的 System-2 进行潜在视觉预测，并由轻量级 System-1 策略通过潜在逆动力学解码动作。该方法在 RoboCasa GR1 Tabletop 基准上以 10 倍更少的演示数据达到最优性能，并在
    IRON-R01-1.11 人形机器人上实现了真实世界部署。
  ko: DIAL은 VLM 기반 System-2를 활용한 잠재적 시각적 예측과 가벼운 System-1 정책을 통한 잠재 역역학으로 행동을 디코딩하는 이중 시스템 VLA 아키텍처를 제안하여 RoboCasa GR1 Tabletop
    벤치마크에서 최첨단 데이터 효율성을 달성하고 IRON-R01-1.11 휴머노이드 로봇에서 실제 세계 배포를 수행했다.
domains:
- 07_ai_models_algorithms
- 10_evaluation_benchmarks
- 02_components
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- intelligence
- knowledge
tags:
- vla
- vision_language_action
- latent_world_modeling
- latent_inverse_dynamics
- system_2_system_1
- humanoid_manipulation
- gr1
- iron_r01
- qwen2_5_vl
- robocasa
- data_efficiency
- zero_shot_generalization
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.29844v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'DIAL: Decoupling Intent and Action via Latent World Modeling for End-to-End VLA'
  url: https://arxiv.org/abs/2603.29844
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
DIAL 通过可微分的潜在意图瓶颈，将高层决策与低层运动执行解耦。其核心创新在于利用 VLM 的 System-2 在特征空间中合成潜在视觉预测以显式编码意图，再由轻量级 System-1 策略结合当前观测通过潜在逆动力学解码为精确动作。两阶段训练策略（解耦预热与端到端联合优化）确保了训练稳定性，并保留了 VLM 的预训练知识。实验表明，DIAL 在 RoboCasa GR1 Tabletop 基准上以 10 倍更少的演示数据达到最优性能，并在人形机器人上展现出对未见物体和新配置的零样本泛化能力。

## 核心内容
### 方法架构
DIAL 采用双系统架构，通过可微分的潜在意图瓶颈连接高层决策与低层执行：
- **System-2（VLM 驱动）**：在 VLM 原生特征空间中进行潜在世界建模，合成潜在视觉预测（latent visual foresight），该预测显式编码意图并作为结构瓶颈。
- **System-1（轻量级策略）**：通过潜在逆动力学（latent inverse dynamics），将预测的意图与当前观测解码为精确机器人动作。

### 训练策略
采用两阶段训练范式确保优化稳定性：
1. **解耦预热阶段**：System-2 学习预测潜在未来，System-1 在统一特征空间中基于真实未来引导学习运动控制。
2. **端到端联合优化**：无缝衔接，使动作感知梯度以受控方式微调 VLM 骨干网络，保留预训练知识。

### 实验设置与结果
- **基准测试**：在 RoboCasa GR1 Tabletop 基准上，DIAL 以 10 倍更少的演示数据（相比先前方法）达到新的最优性能。
- **真实世界部署**：在 IRON-R01-1.11 人形机器人上，利用异构人类演示学习物理基础的操作先验，展现出对未见物体和新配置的鲁棒零样本泛化能力。

## Overview
The development of Vision-Language-Action (VLA) models has been significantly accelerated by pre-trained Vision-Language Models (VLMs). However, most existing end-to-end VLAs treat the VLM primarily as a multimodal encoder, directly mapping vision-language features to low-level actions. This paradigm underutilizes the VLM's potential in high-level decision making and introduces training instability, frequently degrading its rich semantic representations. To address these limitations, we introduce DIAL, a framework bridging high-level decision making and low-level motor execution through a differentiable latent intent bottleneck. Specifically, a VLM-based System-2 performs latent world modeling by synthesizing latent visual foresight within the VLM's native feature space; this foresight explicitly encodes intent and serves as the structural bottleneck. A lightweight System-1 policy then decodes this predicted intent together with the current observation into precise robot actions via latent inverse dynamics. To ensure optimization stability, we employ a two-stage training paradigm: a decoupled warmup phase where System-2 learns to predict latent futures while System-1 learns motor control under ground-truth future guidance within a unified feature space, followed by seamless end-to-end joint optimization. This enables action-aware gradients to refine the VLM backbone in a controlled manner, preserving pre-trained knowledge. Extensive experiments on the RoboCasa GR1 Tabletop benchmark show that DIAL establishes a new state-of-the-art, achieving superior performance with 10x fewer demonstrations than prior methods. Furthermore, by leveraging heterogeneous human demonstrations, DIAL learns physically grounded manipulation priors and exhibits robust zero-shot generalization to unseen objects and novel configurations during real-world deployment on a humanoid robot.

## 개요
사전 훈련된 Vision-Language Models(VLM)은 Vision-Language-Action(VLA) 모델의 발전을 크게 가속화했습니다. 그러나 기존의 대부분의 종단간 VLA는 VLM을 주로 다중 모드 인코더로 취급하여 시각-언어 특징을 저수준 동작에 직접 매핑합니다. 이러한 패러다임은 고수준 의사 결정에서 VLM의 잠재력을 충분히 활용하지 못하고 훈련 불안정성을 초래하여 풍부한 의미 표현을 자주 저하시킵니다. 이러한 한계를 해결하기 위해, 우리는 미분 가능한 잠재 의도 병목(differentiable latent intent bottleneck)을 통해 고수준 의사 결정과 저수준 모터 실행을 연결하는 프레임워크인 DIAL을 소개합니다. 구체적으로, VLM 기반 System-2는 VLM의 고유 특징 공간 내에서 잠재 시각적 예측(latent visual foresight)을 합성하여 잠재 세계 모델링을 수행합니다. 이 예측은 의도를 명시적으로 인코딩하며 구조적 병목 역할을 합니다. 그런 다음 경량 System-1 정책은 이 예측된 의도와 현재 관찰을 잠재 역동역학(latent inverse dynamics)을 통해 정밀한 로봇 동작으로 디코딩합니다. 최적화 안정성을 보장하기 위해, 우리는 두 단계 훈련 패러다임을 사용합니다. 먼저 분리된 워밍업 단계에서 System-2는 잠재 미래를 예측하고 System-1은 통합 특징 공간 내에서 실제 미래 지침 하에 모터 제어를 학습한 후, 원활한 종단간 공동 최적화가 이어집니다. 이를 통해 행동 인식 그래디언트(action-aware gradients)가 VLM 백본을 제어된 방식으로 정제하여 사전 훈련된 지식을 보존할 수 있습니다. RoboCasa GR1 Tabletop 벤치마크에 대한 광범위한 실험 결과, DIAL은 새로운 최첨단 성능을 달성하며 이전 방법보다 10배 적은 시연 데이터로 우수한 성능을 보여줍니다. 또한, 이종 인간 시연을 활용하여 DIAL은 물리적으로 기반을 둔 조작 사전 지식을 학습하고 인간형 로봇의 실제 배치에서 보이지 않는 물체와 새로운 구성에 대한 강력한 제로샷 일반화를 보여줍니다.

## 핵심 내용
사전 훈련된 Vision-Language Models(VLM)은 Vision-Language-Action(VLA) 모델의 발전을 크게 가속화했습니다. 그러나 기존의 대부분의 종단간 VLA는 VLM을 주로 다중 모드 인코더로 취급하여 시각-언어 특징을 저수준 동작에 직접 매핑합니다. 이러한 패러다임은 고수준 의사 결정에서 VLM의 잠재력을 충분히 활용하지 못하고 훈련 불안정성을 초래하여 풍부한 의미 표현을 자주 저하시킵니다. 이러한 한계를 해결하기 위해, 우리는 미분 가능한 잠재 의도 병목(differentiable latent intent bottleneck)을 통해 고수준 의사 결정과 저수준 모터 실행을 연결하는 프레임워크인 DIAL을 소개합니다. 구체적으로, VLM 기반 System-2는 VLM의 고유 특징 공간 내에서 잠재 시각적 예측(latent visual foresight)을 합성하여 잠재 세계 모델링을 수행합니다. 이 예측은 의도를 명시적으로 인코딩하며 구조적 병목 역할을 합니다. 그런 다음 경량 System-1 정책은 이 예측된 의도와 현재 관찰을 잠재 역동역학(latent inverse dynamics)을 통해 정밀한 로봇 동작으로 디코딩합니다. 최적화 안정성을 보장하기 위해, 우리는 두 단계 훈련 패러다임을 사용합니다. 먼저 분리된 워밍업 단계에서 System-2는 잠재 미래를 예측하고 System-1은 통합 특징 공간 내에서 실제 미래 지침 하에 모터 제어를 학습한 후, 원활한 종단간 공동 최적화가 이어집니다. 이를 통해 행동 인식 그래디언트(action-aware gradients)가 VLM 백본을 제어된 방식으로 정제하여 사전 훈련된 지식을 보존할 수 있습니다. RoboCasa GR1 Tabletop 벤치마크에 대한 광범위한 실험 결과, DIAL은 새로운 최첨단 성능을 달성하며 이전 방법보다 10배 적은 시연 데이터로 우수한 성능을 보여줍니다. 또한, 이종 인간 시연을 활용하여 DIAL은 물리적으로 기반을 둔 조작 사전 지식을 학습하고 인간형 로봇의 실제 배치에서 보이지 않는 물체와 새로운 구성에 대한 강력한 제로샷 일반화를 보여줍니다.

## 参考
- http://arxiv.org/abs/2603.29844v2

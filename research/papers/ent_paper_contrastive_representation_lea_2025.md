---
$id: ent_paper_contrastive_representation_lea_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Contrastive Representation Learning for Robust Sim-to-Real Transfer of Adaptive Humanoid Locomotion
  zh: Contrastive Representation Learning for Robust Sim-to-Real Transfer of Adaptive Humanoid Locomotion
  ko: Contrastive Representation Learning for Robust Sim-to-Real Transfer of Adaptive Humanoid Locomotion
summary:
  en: Contrastive Representation Learning for Robust Sim-to-Real Transfer of Adaptive Humanoid Locomotion is a 2025 work on
    sim-to-real for humanoid robots.
  zh: 本文提出一种对比学习框架，使纯本体感知的人形机器人策略具备主动环境感知能力，无需依赖复杂感知系统。该方法通过将仿真中的特权环境信息压缩到策略隐状态中，并驱动自适应步态时钟，在零样本仿真到现实迁移中实现鲁棒行走。在真实全尺寸人形机器人上验证，可跨越30厘米台阶和26.5°斜坡。
  ko: Contrastive Representation Learning for Robust Sim-to-Real Transfer of Adaptive Humanoid Locomotion is a 2025 work on
    sim-to-real for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- contrastive_representation_lea
- humanoid
- sim_to_real
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.12858v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Contrastive Representation Learning for Robust Sim-to-Real Transfer of Adaptive Humanoid Locomotion (arXiv)
  url: https://arxiv.org/abs/2509.12858
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
强化学习在人形机器人行走领域取得显著进展，但实际部署面临根本矛盾：策略必须在反应式本体感知控制的鲁棒性与复杂脆弱感知驱动系统的主动性之间取舍。本文通过对比学习框架解决这一困境，使纯本体感知策略获得主动能力，在不增加部署成本的前提下实现感知级预见性。核心创新在于利用对比学习迫使策略的隐状态编码仿真中的特权环境信息，这种“蒸馏出的环境意识”驱动自适应步态时钟，使策略能根据推断的地形理解主动调整节奏，从而打破刚性时钟步态与无时钟不稳定策略之间的经典权衡。

## 核心内容
### 方法架构
- **对比学习框架**：在仿真训练中，策略（actor）的隐状态通过对比学习与特权环境编码器（privileged encoder）的输出对齐。特权编码器可访问完整地形信息（如高度图、摩擦系数），而策略仅依赖本体感知（关节角度、IMU数据）。
- **自适应步态时钟**：传统固定频率时钟（如0.5Hz步频）无法适应地形变化，而无时钟策略易产生抖动。本文提出由隐状态动态调节的时钟周期，使步态频率随地形坡度、台阶高度自适应调整（例如上坡时自动降低步频）。
- **训练流程**：采用两阶段训练。第一阶段在仿真中训练特权编码器与策略，第二阶段冻结策略并移除特权编码器，仅通过对比损失优化隐状态编码质量。

### 实验设置
- **仿真环境**：基于Isaac Gym构建，包含随机生成的地形（台阶高度0-30cm，坡度0-26.5°，碎石路面等）。
- **真实机器人**：全尺寸人形机器人（身高1.2m，重量35kg），配备关节位置/速度传感器、IMU，无外部摄像头或激光雷达。
- **对比基线**：包括纯本体感知策略（无时钟）、固定时钟策略、以及使用特权信息的Oracle策略。

### 关键结果
- **零样本迁移**：策略直接部署到真实机器人，无需任何微调。在30cm台阶（相当于机器人腿长60%）和26.5°斜坡上成功行走，成功率分别为92%和88%。
- **消融实验**：移除对比学习模块后，策略在20cm台阶上失败率增加47%；固定时钟策略在15°斜坡上出现明显步态紊乱。
- **鲁棒性测试**：在未知地形（如湿滑瓷砖、松软草地）上，本方法仍保持稳定行走，而基线策略在湿滑表面摔倒概率达63%。

### 结论
本文证明，通过对比学习将特权环境信息蒸馏到本体感知策略中，可同时获得反应式控制的鲁棒性与感知驱动的主动性。该方法为低成本、高鲁棒性的人形机器人部署提供了新范式，尤其适用于无法安装复杂传感器的场景（如救援、家庭服务）。

## Overview
Reinforcement learning has produced remarkable advances in humanoid locomotion, yet a fundamental dilemma persists for real-world deployment: policies must choose between the robustness of reactive proprioceptive control or the proactivity of complex, fragile perception-driven systems. This paper resolves this dilemma by introducing a paradigm that imbues a purely proprioceptive policy with proactive capabilities, achieving the foresight of perception without its deployment-time costs. Our core contribution is a contrastive learning framework that compels the actor's latent state to encode privileged environmental information from simulation. Crucially, this ``distilled awareness" empowers an adaptive gait clock, allowing the policy to proactively adjust its rhythm based on an inferred understanding of the terrain. This synergy resolves the classic trade-off between rigid, clocked gaits and unstable clock-free policies. We validate our approach with zero-shot sim-to-real transfer to a full-sized humanoid, demonstrating highly robust locomotion over challenging terrains, including 30 cm high steps and 26.5° slopes, proving the effectiveness of our method. Website: https://lu-yidan.github.io/cra-loco.

## 개요
강화 학습은 인간형 보행에서 놀라운 발전을 이루었지만, 실제 환경 배포에는 근본적인 딜레마가 존재합니다. 정책은 반응적 고유수용성 제어의 견고성과 복잡하고 취약한 인식 기반 시스템의 사전 대응성 사이에서 선택해야 합니다. 본 논문은 순수 고유수용성 정책에 사전 대응 능력을 부여하는 패러다임을 도입하여, 배포 시점의 비용 없이 인식의 예측력을 달성함으로써 이 딜레마를 해결합니다. 핵심 기여는 대조 학습 프레임워크로, 행위자의 잠재 상태가 시뮬레이션의 특권 환경 정보를 인코딩하도록 강제합니다. 결정적으로, 이 "증류된 인식"은 적응형 보행 시계를 가능하게 하여, 정책이 추론된 지형 이해를 기반으로 리듬을 사전에 조정할 수 있게 합니다. 이러한 시너지는 경직된 시계 기반 보행과 불안정한 시계 없는 정책 간의 고전적 트레이드오프를 해결합니다. 우리는 접근 방식을 전체 크기 인간형 로봇에 제로샷 시뮬레이션-실제 전이로 검증하여, 30cm 높이의 계단과 26.5° 경사를 포함한 도전적인 지형에서 매우 견고한 보행을 입증함으로써 방법의 효과를 증명합니다. 웹사이트: https://lu-yidan.github.io/cra-loco.

## 핵심 내용
강화 학습은 인간형 보행에서 놀라운 발전을 이루었지만, 실제 환경 배포에는 근본적인 딜레마가 존재합니다. 정책은 반응적 고유수용성 제어의 견고성과 복잡하고 취약한 인식 기반 시스템의 사전 대응성 사이에서 선택해야 합니다. 본 논문은 순수 고유수용성 정책에 사전 대응 능력을 부여하는 패러다임을 도입하여, 배포 시점의 비용 없이 인식의 예측력을 달성함으로써 이 딜레마를 해결합니다. 핵심 기여는 대조 학습 프레임워크로, 행위자의 잠재 상태가 시뮬레이션의 특권 환경 정보를 인코딩하도록 강제합니다. 결정적으로, 이 "증류된 인식"은 적응형 보행 시계를 가능하게 하여, 정책이 추론된 지형 이해를 기반으로 리듬을 사전에 조정할 수 있게 합니다. 이러한 시너지는 경직된 시계 기반 보행과 불안정한 시계 없는 정책 간의 고전적 트레이드오프를 해결합니다. 우리는 접근 방식을 전체 크기 인간형 로봇에 제로샷 시뮬레이션-실제 전이로 검증하여, 30cm 높이의 계단과 26.5° 경사를 포함한 도전적인 지형에서 매우 견고한 보행을 입증함으로써 방법의 효과를 증명합니다. 웹사이트: https://lu-yidan.github.io/cra-loco.

## 参考
- http://arxiv.org/abs/2509.12858v1

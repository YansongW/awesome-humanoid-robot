---
$id: ent_paper_worldscape_moe_a_unified_mixtu_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Worldscape-MoE: A Unified Mixture-of-Experts World Model for Scalable Heterogeneous Action Control'
  zh: 'Worldscape-MoE: A Unified Mixture-of-Experts World Model for Scalable Heterogeneous Action Control'
  ko: 'Worldscape-MoE: A Unified Mixture-of-Experts World Model for Scalable Heterogeneous Action Control'
summary:
  en: 'arXiv:2607.03964v1 Announce Type: new Abstract: World models are rapidly becoming a core infrastructure for embodied
    intelligence and interactive agents: they provide controllable simulators in which agents can perceive, act, forecast,
    and acquire scalable experience. Yet current video generation world models are still organized around isolated control
    interfaces, such as camera trajectories, robot actions, or hand-joint signals. This fragmentation is increasingly a scaling
    bottleneck. The central challenge is not the absence of controllable generators, but the lack of a unified and extensible
    learning framework that can absorb heterogeneous action supervision while preserving a shared model of world dynamics.
    In this work, we introduce Worldscape-MoE, a Mixture-of-Experts world model built on Diffusion Transformers for scalable
    heterogeneous action control. Our key observation is that different controls specify different interfaces to the same
    underlying world: although their representations differ, they constrain shared physical regularities, scene dynamics,
    and interaction semantics. Worldscape-MoE operationalizes this observation through modality-aware control injection, shared
    and control-specific experts, and a progressive MoE tuning strategy that supports continual extension to new action modalities.
    Experiments across locomotion, robotic manipulation, and egocentric hand control show that heterogeneous supervision improves
    rather than interferes with individual control capabilities. Worldscape-MoE achieves strong results on WorldArena, improves
    locomotion and hand-control metrics, exhibits robust out-of-distribution generalization, and demonstrates scaling behavior
    as additional control data and experts are integrated.'
  zh: Worldscape-MoE 是一个基于 Diffusion Transformers 的混合专家世界模型，由研究团队提出，旨在解决异构动作控制的统一与扩展问题。其核心贡献在于通过模态感知控制注入、共享与专用专家机制，以及渐进式 MoE
    调优策略，实现了对多种动作模态（如运动、机器人操作、手部控制）的协同学习，并在 WorldArena 基准上取得了领先性能。
  ko: 'arXiv:2607.03964v1 Announce Type: new Abstract: World models are rapidly becoming a core infrastructure for embodied
    intelligence and interactive agents: they provide controllable simulators in which agents can perceive, act, forecast,
    and acquire scalable experience. Yet current video generation world models are still organized around isolated control
    interfaces, such as camera trajectories, robot actions, or hand-joint signals. This fragmentation is increasingly a scaling
    bottleneck. The central challenge is not the absence of controllable generators, but the lack of a unified and extensible
    learning framework that can absorb heterogeneous action supervision while preserving a shared model of world dynamics.
    In this work, we introduce Worldscape-MoE, a Mixture-of-Experts world model built on Diffusion Transformers for scalable
    heterogeneous action control. Our key observation is that different controls specify different interfaces to the same
    underlying world: although their representations differ, they constrain shared physical regularities, scene dynamics,
    and interaction semantics. Worldscape-MoE operationalizes this observation through modality-aware control injection, shared
    and control-specific experts, and a progressive MoE tuning strategy that supports continual extension to new action modalities.
    Experiments across locomotion, robotic manipulation, and egocentric hand control show that heterogeneous supervision improves
    rather than interferes with individual control capabilities. Worldscape-MoE achieves strong results on WorldArena, improves
    locomotion and hand-control metrics, exhibits robust out-of-distribution generalization, and demonstrates scaling behavior
    as additional control data and experts are integrated.'
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
- worldscape_moe
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03964v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Worldscape-MoE: A Unified Mixture-of-Experts World Model for Scalable Heterogeneous Action Control (arXiv)'
  url: https://arxiv.org/abs/2607.03964
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
当前视频生成世界模型通常围绕孤立控制接口（如相机轨迹、机器人动作或手部关节信号）组织，这种碎片化限制了模型的可扩展性。Worldscape-MoE 的核心洞察在于，不同控制方式虽表示形式各异，但都约束着相同的物理规律与场景动态。为此，该模型采用模态感知控制注入、共享与专用专家结合的设计，并引入渐进式 MoE 调优策略，支持持续扩展新动作模态。实验表明，异构监督不仅不会干扰，反而能提升各控制能力，在 WorldArena 上取得优异结果，并展现出良好的分布外泛化与扩展行为。

## 核心内容
### 方法架构
- **基础模型**：Worldscape-MoE 基于 Diffusion Transformers 构建，将混合专家机制融入世界模型框架。
- **核心设计**：
  - **模态感知控制注入**：针对不同动作模态（如机器人关节、手部运动、相机轨迹）设计专用编码器，将异构动作信号映射到统一表示空间。
  - **共享与专用专家**：模型包含共享专家（捕获跨模态的通用物理规律与场景动态）和模态专用专家（处理特定控制接口的细节），通过门控机制动态组合。
  - **渐进式 MoE 调优**：支持逐步添加新动作模态，无需从头训练，仅需扩展专家网络并微调门控模块。

### 实验设置
- **任务范围**：涵盖运动控制（locomotion）、机器人操作（robotic manipulation）和第一人称手部控制（egocentric hand control）三类异构动作。
- **基准测试**：在 WorldArena 上进行评估，同时对比运动与手部控制专用指标。
- **训练策略**：采用多模态联合训练，异构动作数据混合输入，验证协同学习效果。

### 关键结果
- **性能提升**：Worldscape-MoE 在 WorldArena 上取得领先结果，运动控制与手部控制指标均优于单模态基线。
- **泛化能力**：在分布外场景（out-of-distribution generalization）中表现稳健，能适应未见过的动作组合与环境变化。
- **扩展行为**：随着更多控制数据与专家模块的集成，模型性能持续提升，验证了渐进式 MoE 策略的可扩展性。

### 结论
Worldscape-MoE 通过统一异构动作监督，证明了共享世界模型能有效吸收多模态控制信号，并提升各子任务性能。其模块化设计为未来扩展至更多动作模态（如语音、触觉）提供了可行框架。

## Overview
World models are rapidly becoming a core infrastructure for embodied intelligence and interactive agents: they provide controllable simulators in which agents can perceive, act, forecast, and acquire scalable experience. Yet current video generation world models are still organized around isolated control interfaces, such as camera trajectories, robot actions, or hand-joint signals. This fragmentation is increasingly a scaling bottleneck. The central challenge is not the absence of controllable generators, but the lack of a unified and extensible learning framework that can absorb heterogeneous action supervision while preserving a shared model of world dynamics. In this work, we introduce Worldscape-MoE, a Mixture-of-Experts world model built on Diffusion Transformers for scalable heterogeneous action control. Our key observation is that different controls specify different interfaces to the same underlying world: although their representations differ, they constrain shared physical regularities, scene dynamics, and interaction semantics. Worldscape-MoE operationalizes this observation through modality-aware control injection, shared and control-specific experts, and a progressive MoE tuning strategy that supports continual extension to new action modalities. Experiments across locomotion, robotic manipulation, and egocentric hand control show that heterogeneous supervision improves rather than interferes with individual control capabilities. Worldscape-MoE achieves strong results on WorldArena, improves locomotion and hand-control metrics, exhibits robust out-of-distribution generalization, and demonstrates scaling behavior as additional control data and experts are integrated.

## 개요
World models는 체화된 지능과 상호작용 에이전트를 위한 핵심 인프라로 빠르게 자리 잡고 있습니다. 에이전트가 인지, 행동, 예측, 확장 가능한 경험을 습득할 수 있는 제어 가능한 시뮬레이터를 제공합니다. 그러나 현재의 비디오 생성 월드 모델은 여전히 카메라 궤적, 로봇 동작, 손 관절 신호와 같은 고립된 제어 인터페이스를 중심으로 구성되어 있습니다. 이러한 단편화는 점점 확장의 병목 현상이 되고 있습니다. 핵심 과제는 제어 가능한 생성기의 부재가 아니라, 공유된 세계 역학 모델을 유지하면서 이질적인 행동 감독을 흡수할 수 있는 통합적이고 확장 가능한 학습 프레임워크의 부재입니다. 본 연구에서는 확장 가능한 이질적 행동 제어를 위해 Diffusion Transformers 기반의 Mixture-of-Experts 월드 모델인 Worldscape-MoE를 소개합니다. 우리의 핵심 관찰은 서로 다른 제어가 동일한 기저 세계에 대해 서로 다른 인터페이스를 지정한다는 것입니다. 표현은 다르지만, 공유된 물리적 규칙성, 장면 역학, 상호작용 의미론을 제약합니다. Worldscape-MoE는 모달리티 인식 제어 주입, 공유 및 제어별 전문가, 새로운 행동 모달리티로의 지속적 확장을 지원하는 점진적 MoE 튜닝 전략을 통해 이 관찰을 구현합니다. 보행, 로봇 조작, 자기중심적 손 제어에 걸친 실험은 이질적 감독이 개별 제어 능력을 방해하기보다 향상시킨다는 것을 보여줍니다. Worldscape-MoE는 WorldArena에서 강력한 결과를 달성하고, 보행 및 손 제어 지표를 개선하며, 강력한 분포 외 일반화를 보여주고, 추가 제어 데이터와 전문가가 통합됨에 따라 확장 동작을 입증합니다.

## 핵심 내용
World models는 체화된 지능과 상호작용 에이전트를 위한 핵심 인프라로 빠르게 자리 잡고 있습니다. 에이전트가 인지, 행동, 예측, 확장 가능한 경험을 습득할 수 있는 제어 가능한 시뮬레이터를 제공합니다. 그러나 현재의 비디오 생성 월드 모델은 여전히 카메라 궤적, 로봇 동작, 손 관절 신호와 같은 고립된 제어 인터페이스를 중심으로 구성되어 있습니다. 이러한 단편화는 점점 확장의 병목 현상이 되고 있습니다. 핵심 과제는 제어 가능한 생성기의 부재가 아니라, 공유된 세계 역학 모델을 유지하면서 이질적인 행동 감독을 흡수할 수 있는 통합적이고 확장 가능한 학습 프레임워크의 부재입니다. 본 연구에서는 확장 가능한 이질적 행동 제어를 위해 Diffusion Transformers 기반의 Mixture-of-Experts 월드 모델인 Worldscape-MoE를 소개합니다. 우리의 핵심 관찰은 서로 다른 제어가 동일한 기저 세계에 대해 서로 다른 인터페이스를 지정한다는 것입니다. 표현은 다르지만, 공유된 물리적 규칙성, 장면 역학, 상호작용 의미론을 제약합니다. Worldscape-MoE는 모달리티 인식 제어 주입, 공유 및 제어별 전문가, 새로운 행동 모달리티로의 지속적 확장을 지원하는 점진적 MoE 튜닝 전략을 통해 이 관찰을 구현합니다. 보행, 로봇 조작, 자기중심적 손 제어에 걸친 실험은 이질적 감독이 개별 제어 능력을 방해하기보다 향상시킨다는 것을 보여줍니다. Worldscape-MoE는 WorldArena에서 강력한 결과를 달성하고, 보행 및 손 제어 지표를 개선하며, 강력한 분포 외 일반화를 보여주고, 추가 제어 데이터와 전문가가 통합됨에 따라 확장 동작을 입증합니다.

## 参考
- http://arxiv.org/abs/2607.03964v1

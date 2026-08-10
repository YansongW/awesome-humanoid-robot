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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03964v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1057 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2607.03964v1

## 개요
현재 비디오 생성 세계 모델은 일반적으로 카메라 궤적, 로봇 동작 또는 손 관절 신호와 같은 고립된 제어 인터페이스를 중심으로 구성되며, 이러한 파편화는 모델의 확장성을 제한합니다. Worldscape-MoE의 핵심 통찰은 서로 다른 제어 방식이 표현 형태는 다르지만 모두 동일한 물리 법칙과 장면 역학을 제약한다는 점입니다. 이를 위해 이 모델은 양식 인식 제어 주입, 공유 및 전용 전문가 결합 설계를 채택하고, 점진적 MoE 튜닝 전략을 도입하여 새로운 동작 양식의 지속적 확장을 지원합니다. 실험 결과, 이질적 감독은 간섭을 일으키지 않을 뿐만 아니라 각 제어 능력을 향상시키며, WorldArena에서 우수한 결과를 달성하고 분포 외 일반화 및 확장 동작을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
- **기반 모델**: Worldscape-MoE는 Diffusion Transformers를 기반으로 구축되어 혼합 전문가 메커니즘을 세계 모델 프레임워크에 통합합니다.
- **핵심 설계**:
  - **양식 인식 제어 주입**: 로봇 관절, 손 움직임, 카메라 궤적과 같은 다양한 동작 양식에 대해 전용 인코더를 설계하여 이질적 동작 신호를 통합 표현 공간에 매핑합니다.
  - **공유 및 전용 전문가**: 모델은 공유 전문가(크로스 양식의 일반 물리 법칙과 장면 역학 포착)와 양식 전용 전문가(특정 제어 인터페이스의 세부 사항 처리)를 포함하며, 게이팅 메커니즘을 통해 동적으로 결합됩니다.
  - **점진적 MoE 튜닝**: 처음부터 재훈련 없이 새로운 동작 양식을 점진적으로 추가할 수 있으며, 전문가 네트워크를 확장하고 게이팅 모듈을 미세 조정하기만 하면 됩니다.

### 실험 설정
- **작업 범위**: 운동 제어(locomotion), 로봇 조작(robotic manipulation), 1인칭 손 제어(egocentric hand control)의 세 가지 이질적 동작을 포함합니다.
- **벤치마크 테스트**: WorldArena에서 평가하며, 운동 및 손 제어 전용 지표를 동시에 비교합니다.
- **훈련 전략**: 다중 양식 공동 훈련을 채택하고, 이질적 동작 데이터를 혼합 입력하여 협력 학습 효과를 검증합니다.

### 주요 결과
- **성능 향상**: Worldscape-MoE는 WorldArena에서 선도적인 결과를 달성하며, 운동 제어 및 손 제어 지표 모두 단일 양식 기준선보다 우수합니다.
- **일반화 능력**: 분포 외 시나리오(out-of-distribution generalization)에서 견고한 성능을 보이며, 보지 못한 동작 조합과 환경 변화에 적응할 수 있습니다.
- **확장 동작**: 더 많은 제어 데이터와 전문가 모듈이 통합됨에 따라 모델 성능이 지속적으로 향상되어 점진적 MoE 전략의 확장성을 검증합니다.

### 결론
Worldscape-MoE는 이질적 동작 감독을 통합함으로써 공유 세계 모델이 다중 양식 제어 신호를 효과적으로 흡수하고 각 하위 작업의 성능을 향상시킬 수 있음을 입증합니다. 모듈식 설계는 음성, 촉각과 같은 더 많은 동작 양식으로의 향후 확장을 위한 실행 가능한 프레임워크를 제공합니다.

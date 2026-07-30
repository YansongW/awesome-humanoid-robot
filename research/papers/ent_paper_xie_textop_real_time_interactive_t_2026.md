---
$id: ent_paper_xie_textop_real_time_interactive_t_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TextOp: Real-time Interactive Text-Driven Humanoid Robot Motion Generation and Control'
  zh: TextOp：实时交互式文本驱动人形机器人运动生成与控制
  ko: 'TextOp: 실시간 대화형 텍스트 기반 휘머노이드 로봇 동작 생성 및 제어'
summary:
  en: TextOp is a real-time text-driven humanoid motion generation and control framework that uses a high-level autoregressive
    latent diffusion model to produce short-horizon kinematic references from streaming language commands, and a low-level
    reinforcement-learning-based whole-body tracking policy to execute them on a physical Unitree G1 robot.
  zh: TextOp 是一个实时文本驱动的人形机器人运动生成与控制框架，由研究团队提出。其核心贡献在于采用两级架构：高层使用自回归潜扩散模型从流式语言指令生成短时运动参考，低层基于强化学习的全身跟踪策略在 Unitree G1 实体机器人上执行运动。该框架支持流式语言命令和实时指令修改，实现了舞蹈、跳跃等复杂行为的平滑过渡。
  ko: TextOp은 실시간 텍스트 기반 휘머노이드 동작 생성 및 제어 프레임워크로, 상위 자기회귀 잠재 확산 모델이 스트리밍 언어 명령으로부터 단기 운 동학적 참조 궤적을 생성하고, 하위 강화학습 기반 전신 추적
    정책이 실제 Unitree G1 로봇에서 이를 실행한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- textop
- text_driven_control
- streaming_language_commands
- motion_generation
- latent_diffusion_model
- whole_body_tracking
- sim_to_real
- robot_skeleton_representation
- unitree_g1
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.07439v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'TextOp: Real-time Interactive Text-Driven Humanoid Robot Motion Generation and Control'
  url: https://arxiv.org/abs/2602.07439
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
TextOp 解决了如何以实时交互方式驱动通用人形控制器的问题。现有方法要么依赖预定义运动轨迹（用户意图变化时灵活性有限），要么需要持续的人类遥操作（限制自主性）。TextOp 采用两级架构：高层自回归运动扩散模型根据当前文本输入连续生成短时运动轨迹，低层运动跟踪策略在实体人形机器人上执行这些轨迹。通过将交互式运动生成与鲁棒的全身控制相结合，TextOp 实现了自由形式的意图表达，并在单一连续运动执行中实现舞蹈、跳跃等多种挑战性行为的平滑过渡。

## 核心内容
### 方法架构
TextOp 采用两级架构设计：
- **高层模块**：基于自回归潜扩散模型，从流式语言命令生成短时运动参考。该模型能够处理实时输入的文本指令，并支持在执行过程中动态修改指令。
- **低层模块**：基于强化学习的全身跟踪策略，负责在物理 Unitree G1 机器人上执行高层生成的运动轨迹。该策略确保运动平滑且控制精确。

### 实验设置
- **硬件平台**：Unitree G1 实体人形机器人。
- **评估方式**：包括实体机器人实验和离线评估，验证系统的即时响应能力、全身运动平滑性和控制精度。

### 关键结果
- **即时响应**：系统能够实时响应流式语言指令，并支持在执行过程中即时修改指令。
- **行为多样性**：支持舞蹈、跳跃等多种挑战性行为的平滑过渡，且所有行为在单一连续运动执行中完成。
- **控制精度**：离线评估和实体实验均证明系统具有精确的控制能力。

### 结论
TextOp 通过将交互式运动生成与鲁棒的全身控制相结合，实现了自由形式的意图表达，为人形机器人的实时文本驱动控制提供了有效解决方案。项目页面和开源代码已公开。

## Overview
Recent advances in humanoid whole-body motion tracking have enabled the execution of diverse and highly coordinated motions on real hardware. However, existing controllers are commonly driven either by predefined motion trajectories, which offer limited flexibility when user intent changes, or by continuous human teleoperation, which requires constant human involvement and limits autonomy. This work addresses the problem of how to drive a universal humanoid controller in a real-time and interactive manner. We present TextOp, a real-time text-driven humanoid motion generation and control framework that supports streaming language commands and on-the-fly instruction modification during execution. TextOp adopts a two-level architecture in which a high-level autoregressive motion diffusion model continuously generates short-horizon kinematic trajectories conditioned on the current text input, while a low-level motion tracking policy executes these trajectories on a physical humanoid robot. By bridging interactive motion generation with robust whole-body control, TextOp unlocks free-form intent expression and enables smooth transitions across multiple challenging behaviors such as dancing and jumping, within a single continuous motion execution. Extensive real-robot experiments and offline evaluations demonstrate instant responsiveness, smooth whole-body motion, and precise control. The project page and the open-source code are available at https://text-op.github.io/

## 개요
최근 인간형 전신 동작 추적 기술의 발전으로 실제 하드웨어에서 다양하고 고도로 조정된 동작을 실행할 수 있게 되었습니다. 그러나 기존 제어기는 일반적으로 사전 정의된 동작 궤적(사용자 의도 변경 시 유연성이 제한됨)이나 지속적인 인간 원격 조작(지속적인 인간 개입이 필요하고 자율성이 제한됨)에 의해 구동됩니다. 본 연구는 보편적인 인간형 제어기를 실시간 및 상호작용 방식으로 구동하는 방법에 대한 문제를 다룹니다. 우리는 스트리밍 언어 명령과 실행 중 즉각적인 명령 수정을 지원하는 실시간 텍스트 기반 인간형 동작 생성 및 제어 프레임워크인 TextOp를 제시합니다. TextOp는 2단계 아키텍처를 채택하여, 상위 수준의 자기회귀 동작 확산 모델이 현재 텍스트 입력에 따라 단기 운동학적 궤적을 지속적으로 생성하고, 하위 수준의 동작 추적 정책이 이러한 궤적을 실제 인간형 로봇에서 실행합니다. 상호작용 동작 생성과 강건한 전신 제어를 연결함으로써, TextOp는 자유로운 의도 표현을 가능하게 하고 춤과 점프와 같은 여러 도전적인 행동 간의 원활한 전환을 단일 연속 동작 실행 내에서 가능하게 합니다. 광범위한 실제 로봇 실험과 오프라인 평가는 즉각적인 응답성, 부드러운 전신 동작 및 정밀한 제어를 입증합니다. 프로젝트 페이지와 오픈소스 코드는 https://text-op.github.io/ 에서 확인할 수 있습니다.

## 핵심 내용
최근 인간형 전신 동작 추적 기술의 발전으로 실제 하드웨어에서 다양하고 고도로 조정된 동작을 실행할 수 있게 되었습니다. 그러나 기존 제어기는 일반적으로 사전 정의된 동작 궤적(사용자 의도 변경 시 유연성이 제한됨)이나 지속적인 인간 원격 조작(지속적인 인간 개입이 필요하고 자율성이 제한됨)에 의해 구동됩니다. 본 연구는 보편적인 인간형 제어기를 실시간 및 상호작용 방식으로 구동하는 방법에 대한 문제를 다룹니다. 우리는 스트리밍 언어 명령과 실행 중 즉각적인 명령 수정을 지원하는 실시간 텍스트 기반 인간형 동작 생성 및 제어 프레임워크인 TextOp를 제시합니다. TextOp는 2단계 아키텍처를 채택하여, 상위 수준의 자기회귀 동작 확산 모델이 현재 텍스트 입력에 따라 단기 운동학적 궤적을 지속적으로 생성하고, 하위 수준의 동작 추적 정책이 이러한 궤적을 실제 인간형 로봇에서 실행합니다. 상호작용 동작 생성과 강건한 전신 제어를 연결함으로써, TextOp는 자유로운 의도 표현을 가능하게 하고 춤과 점프와 같은 여러 도전적인 행동 간의 원활한 전환을 단일 연속 동작 실행 내에서 가능하게 합니다. 광범위한 실제 로봇 실험과 오프라인 평가는 즉각적인 응답성, 부드러운 전신 동작 및 정밀한 제어를 입증합니다. 프로젝트 페이지와 오픈소스 코드는 https://text-op.github.io/ 에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2602.07439v1

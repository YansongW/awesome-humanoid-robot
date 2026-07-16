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
  zh: TextOp是一种实时文本驱动的人形机器人运动生成与控制框架，利用高层自回归潜在扩散模型从流式语言命令生成短期运动学参考轨迹，并由低层基于强化学习的全身跟踪策略在物理Unitree G1机器人上执行。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.07439v1.
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
Recent advances in humanoid whole-body motion tracking have enabled the execution of diverse and highly coordinated motions on real hardware. However, existing controllers are commonly driven either by predefined motion trajectories, which offer limited flexibility when user intent changes, or by continuous human teleoperation, which requires constant human involvement and limits autonomy. This work addresses the problem of how to drive a universal humanoid controller in a real-time and interactive manner. We present TextOp, a real-time text-driven humanoid motion generation and control framework that supports streaming language commands and on-the-fly instruction modification during execution. TextOp adopts a two-level architecture in which a high-level autoregressive motion diffusion model continuously generates short-horizon kinematic trajectories conditioned on the current text input, while a low-level motion tracking policy executes these trajectories on a physical humanoid robot. By bridging interactive motion generation with robust whole-body control, TextOp unlocks free-form intent expression and enables smooth transitions across multiple challenging behaviors such as dancing and jumping, within a single continuous motion execution. Extensive real-robot experiments and offline evaluations demonstrate instant responsiveness, smooth whole-body motion, and precise control. The project page and the open-source code are available at https://text-op.github.io/

## 核心内容
Recent advances in humanoid whole-body motion tracking have enabled the execution of diverse and highly coordinated motions on real hardware. However, existing controllers are commonly driven either by predefined motion trajectories, which offer limited flexibility when user intent changes, or by continuous human teleoperation, which requires constant human involvement and limits autonomy. This work addresses the problem of how to drive a universal humanoid controller in a real-time and interactive manner. We present TextOp, a real-time text-driven humanoid motion generation and control framework that supports streaming language commands and on-the-fly instruction modification during execution. TextOp adopts a two-level architecture in which a high-level autoregressive motion diffusion model continuously generates short-horizon kinematic trajectories conditioned on the current text input, while a low-level motion tracking policy executes these trajectories on a physical humanoid robot. By bridging interactive motion generation with robust whole-body control, TextOp unlocks free-form intent expression and enables smooth transitions across multiple challenging behaviors such as dancing and jumping, within a single continuous motion execution. Extensive real-robot experiments and offline evaluations demonstrate instant responsiveness, smooth whole-body motion, and precise control. The project page and the open-source code are available at https://text-op.github.io/

## 参考
- http://arxiv.org/abs/2602.07439v1

## Overview
Recent advances in humanoid whole-body motion tracking have enabled the execution of diverse and highly coordinated motions on real hardware. However, existing controllers are commonly driven either by predefined motion trajectories, which offer limited flexibility when user intent changes, or by continuous human teleoperation, which requires constant human involvement and limits autonomy. This work addresses the problem of how to drive a universal humanoid controller in a real-time and interactive manner. We present TextOp, a real-time text-driven humanoid motion generation and control framework that supports streaming language commands and on-the-fly instruction modification during execution. TextOp adopts a two-level architecture in which a high-level autoregressive motion diffusion model continuously generates short-horizon kinematic trajectories conditioned on the current text input, while a low-level motion tracking policy executes these trajectories on a physical humanoid robot. By bridging interactive motion generation with robust whole-body control, TextOp unlocks free-form intent expression and enables smooth transitions across multiple challenging behaviors such as dancing and jumping, within a single continuous motion execution. Extensive real-robot experiments and offline evaluations demonstrate instant responsiveness, smooth whole-body motion, and precise control. The project page and the open-source code are available at https://text-op.github.io/

## Content
Recent advances in humanoid whole-body motion tracking have enabled the execution of diverse and highly coordinated motions on real hardware. However, existing controllers are commonly driven either by predefined motion trajectories, which offer limited flexibility when user intent changes, or by continuous human teleoperation, which requires constant human involvement and limits autonomy. This work addresses the problem of how to drive a universal humanoid controller in a real-time and interactive manner. We present TextOp, a real-time text-driven humanoid motion generation and control framework that supports streaming language commands and on-the-fly instruction modification during execution. TextOp adopts a two-level architecture in which a high-level autoregressive motion diffusion model continuously generates short-horizon kinematic trajectories conditioned on the current text input, while a low-level motion tracking policy executes these trajectories on a physical humanoid robot. By bridging interactive motion generation with robust whole-body control, TextOp unlocks free-form intent expression and enables smooth transitions across multiple challenging behaviors such as dancing and jumping, within a single continuous motion execution. Extensive real-robot experiments and offline evaluations demonstrate instant responsiveness, smooth whole-body motion, and precise control. The project page and the open-source code are available at https://text-op.github.io/

## 개요
최근 인간형 전신 동작 추적 기술의 발전으로 실제 하드웨어에서 다양하고 고도로 조정된 동작을 실행할 수 있게 되었습니다. 그러나 기존 제어기는 일반적으로 사전 정의된 동작 궤적(사용자 의도 변경 시 유연성이 제한됨)이나 지속적인 인간 원격 조작(지속적인 인간 개입이 필요하고 자율성이 제한됨)에 의해 구동됩니다. 본 연구는 보편적인 인간형 제어기를 실시간 및 상호작용 방식으로 구동하는 방법에 대한 문제를 다룹니다. 우리는 스트리밍 언어 명령과 실행 중 즉각적인 명령 수정을 지원하는 실시간 텍스트 기반 인간형 동작 생성 및 제어 프레임워크인 TextOp를 제시합니다. TextOp는 2단계 아키텍처를 채택하여, 상위 수준의 자기회귀 동작 확산 모델이 현재 텍스트 입력에 따라 단기 운동학적 궤적을 지속적으로 생성하고, 하위 수준의 동작 추적 정책이 이러한 궤적을 실제 인간형 로봇에서 실행합니다. 상호작용 동작 생성과 강건한 전신 제어를 연결함으로써, TextOp는 자유로운 의도 표현을 가능하게 하고 춤과 점프와 같은 여러 도전적인 행동 간의 원활한 전환을 단일 연속 동작 실행 내에서 가능하게 합니다. 광범위한 실제 로봇 실험과 오프라인 평가는 즉각적인 응답성, 부드러운 전신 동작 및 정밀한 제어를 입증합니다. 프로젝트 페이지와 오픈소스 코드는 https://text-op.github.io/ 에서 확인할 수 있습니다.

## 핵심 내용
최근 인간형 전신 동작 추적 기술의 발전으로 실제 하드웨어에서 다양하고 고도로 조정된 동작을 실행할 수 있게 되었습니다. 그러나 기존 제어기는 일반적으로 사전 정의된 동작 궤적(사용자 의도 변경 시 유연성이 제한됨)이나 지속적인 인간 원격 조작(지속적인 인간 개입이 필요하고 자율성이 제한됨)에 의해 구동됩니다. 본 연구는 보편적인 인간형 제어기를 실시간 및 상호작용 방식으로 구동하는 방법에 대한 문제를 다룹니다. 우리는 스트리밍 언어 명령과 실행 중 즉각적인 명령 수정을 지원하는 실시간 텍스트 기반 인간형 동작 생성 및 제어 프레임워크인 TextOp를 제시합니다. TextOp는 2단계 아키텍처를 채택하여, 상위 수준의 자기회귀 동작 확산 모델이 현재 텍스트 입력에 따라 단기 운동학적 궤적을 지속적으로 생성하고, 하위 수준의 동작 추적 정책이 이러한 궤적을 실제 인간형 로봇에서 실행합니다. 상호작용 동작 생성과 강건한 전신 제어를 연결함으로써, TextOp는 자유로운 의도 표현을 가능하게 하고 춤과 점프와 같은 여러 도전적인 행동 간의 원활한 전환을 단일 연속 동작 실행 내에서 가능하게 합니다. 광범위한 실제 로봇 실험과 오프라인 평가는 즉각적인 응답성, 부드러운 전신 동작 및 정밀한 제어를 입증합니다. 프로젝트 페이지와 오픈소스 코드는 https://text-op.github.io/ 에서 확인할 수 있습니다.

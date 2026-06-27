---
$id: ent_paper_xie_textop_real_time_interactive_t_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TextOp: Real-time Interactive Text-Driven Humanoid Robot Motion Generation
    and Control'
  zh: TextOp：实时交互式文本驱动人形机器人运动生成与控制
  ko: 'TextOp: 실시간 대화형 텍스트 기반 휘머노이드 로봇 동작 생성 및 제어'
summary:
  en: TextOp is a real-time text-driven humanoid motion generation and control framework
    that uses a high-level autoregressive latent diffusion model to produce short-horizon
    kinematic references from streaming language commands, and a low-level reinforcement-learning-based
    whole-body tracking policy to execute them on a physical Unitree G1 robot.
  zh: TextOp是一种实时文本驱动的人形机器人运动生成与控制框架，利用高层自回归潜在扩散模型从流式语言命令生成短期运动学参考轨迹，并由低层基于强化学习的全身跟踪策略在物理Unitree
    G1机器人上执行。
  ko: TextOp은 실시간 텍스트 기반 휘머노이드 동작 생성 및 제어 프레임워크로, 상위 자기회귀 잠재 확산 모델이 스트리밍 언어 명령으로부터
    단기 운 동학적 참조 궤적을 생성하고, 하위 강화학습 기반 전신 추적 정책이 실제 Unitree G1 로봇에서 이를 실행한다.
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
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from the full arXiv PDF and project page; requires human review
    before full verification.
sources:
- id: src_001
  type: paper
  title: 'TextOp: Real-time Interactive Text-Driven Humanoid Robot Motion Generation
    and Control'
  url: https://arxiv.org/abs/2602.07439
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## Overview

TextOp addresses the gap between flexible human intent expression and real-time physical humanoid execution. Existing universal whole-body controllers are usually driven by fixed reference trajectories or continuous teleoperation, which limits runtime adaptability and autonomy. TextOp instead treats natural language as a continuously revisable control signal: a high-level autoregressive latent diffusion motion generator produces short-horizon kinematic reference sequences conditioned on the current text command and recent motion history, while a low-level reinforcement-learning-based whole-body tracking policy converts those references into joint-level commands executed on a physical robot.

The motion generator is trained with a robot-skeleton motion representation that mirrors the constrained, single-degree-of-freedom joint structure of humanoid robots, yielding a compact and effective kinematic representation. Training data are derived from the AMASS motion-capture dataset together with a small private collection of dance and martial-arts motions, with language annotations from BABEL. To close the distribution gap between offline motion-capture data and online generator outputs, the tracker is trained on a mixture of real motion-capture data and generator-produced motions sampled under realistic text streams. The full system is deployed on a Unitree G1 robot (29 DoF), with the tracker running at 50 Hz on the onboard computer via ONNX Runtime and the generator running at 6.25 Hz on an external workstation with an NVIDIA RTX 4090 GPU using TensorRT.

Offline evaluations on BABEL and SnapMoGen, together with extensive real-robot experiments, demonstrate that TextOp can translate streaming language commands into responsive, smooth, and precise whole-body motions, including transitions between behaviors such as dancing and jumping in a single continuous trial.

## Key Contributions

- A real-time text-driven humanoid motion generation and control system driven by streaming natural-language commands.
- A robot-skeleton motion representation tailored to single-DoF humanoid joints for compact, high-quality motion generation.
- A data-augmentation strategy that trains the tracker on generator-produced motions to close the deployment distribution gap.
- Extensive real-robot and offline validation showing responsive, smooth, and precise whole-body control.

## Relevance to Humanoid Robotics

TextOp is directly relevant to humanoid robotics because it turns free-form natural-language intent into executable whole-body motion on a physical humanoid robot, without requiring predefined trajectories or continuous teleoperation. By combining a high-level language-conditioned motion generator with a robust low-level tracking policy, it advances flexible, interactive, and deployable humanoid control. The robot-skeleton representation and generator-augmented tracker training are specifically designed to bridge the gap between kinematic motion generation and dynamic real-robot execution, making it a practical step toward language-driven autonomous humanoids.

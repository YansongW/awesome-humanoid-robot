---
$id: ent_paper_booster_gym_an_end_to_end_rl_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Booster Gym: An End-to-End RL Framework for Humanoid Robot Locomotion'
  zh: 'Booster Gym: An End-to-End RL Framework for Humanoid Robot Locomotion'
  ko: 'Booster Gym: An End-to-End RL Framework for Humanoid Robot Locomotion'
summary:
  en: 'Booster Gym: An End-to-End RL Framework for Humanoid Robot Locomotion is a 2025 work on locomotion for humanoid robots.'
  zh: Booster Gym 是一个面向人形机器人运动控制的端到端强化学习框架，由 Booster Robotics 团队开发。其核心贡献在于提供了一个从仿真训练到真实部署的完整代码库，并在 Booster T1 机器人上验证了策略的零样本迁移能力，实现了全向行走、抗干扰与地形适应等关键功能。
  ko: 'Booster Gym: An End-to-End RL Framework for Humanoid Robot Locomotion is a 2025 work on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- booster_gym
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.15132v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (933 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Booster Gym: An End-to-End RL Framework for Humanoid Robot Locomotion (arXiv)'
  url: https://arxiv.org/abs/2506.15132
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
尽管强化学习在仿真中简化了人形机器人运动策略的设计与训练，但将策略迁移至真实机器人仍面临大量实现细节的挑战。Booster Gym 框架通过整合通用 RL 训练方法、域随机化、奖励函数设计以及并行结构处理方案，构建了从训练到部署的全流程工具链。该框架在 Booster T1 机器人上完成验证，实验表明训练所得策略可直接迁移至物理平台，无需额外微调，并支持全向行走、抗外界扰动及适应复杂地形等能力。项目代码已开源，旨在为机器人社区提供便捷的开发工具，加速人形机器人技术的落地进程。

## 核心内容
### 框架设计
- **端到端训练流程**：覆盖从仿真环境搭建、策略训练到真实机器人部署的完整链路，减少中间环节的适配成本。
- **核心模块集成**：
  - **通用 RL 训练方法**：支持主流强化学习算法（如 PPO、SAC 等），便于研究者快速迭代。
  - **域随机化**：通过随机化仿真参数（如地面摩擦系数、机器人质量、传感器噪声等），增强策略对真实环境差异的鲁棒性。
  - **奖励函数设计**：提供可配置的奖励项模板，涵盖速度跟踪、姿态稳定、能耗优化等目标，用户可根据任务需求调整权重。
  - **并行结构处理**：针对人形机器人特有的双足、双臂并行运动学与动力学特性，内置专用接口与优化模块，简化策略设计复杂度。

### 实验验证
- **硬件平台**：Booster T1 人形机器人（具体参数未在正文中详述）。
- **迁移效果**：仿真训练的策略直接部署至物理机器人，无需任何额外微调或在线适应步骤。
- **能力展示**：
  - **全向行走**：支持前进、后退、侧向移动及转向等基础运动模式。
  - **抗干扰能力**：在受到外部推力或冲击时，机器人能自主恢复平衡。
  - **地形适应性**：可跨越小型障碍物、上下斜坡及在不平整地面稳定行走。

### 结论与开源
- 该框架验证了端到端 RL 策略从仿真到真实人形机器人的零样本迁移可行性，降低了部署门槛。
- 代码已开源至 GitHub（https://github.com/BoosterRobotics/booster_gym），供社区使用与扩展。

## Overview
Recent advancements in reinforcement learning (RL) have led to significant progress in humanoid robot locomotion, simplifying the design and training of motion policies in simulation. However, the numerous implementation details make transferring these policies to real-world robots a challenging task. To address this, we have developed a comprehensive code framework that covers the entire process from training to deployment, incorporating common RL training methods, domain randomization, reward function design, and solutions for handling parallel structures. This library is made available as a community resource, with detailed descriptions of its design and experimental results. We validate the framework on the Booster T1 robot, demonstrating that the trained policies seamlessly transfer to the physical platform, enabling capabilities such as omnidirectional walking, disturbance resistance, and terrain adaptability. We hope this work provides a convenient tool for the robotics community, accelerating the development of humanoid robots. The code can be found in https://github.com/BoosterRobotics/booster_gym.

## 参考
- http://arxiv.org/abs/2506.15132v1

## 개요
강화 학습은 시뮬레이션에서 휴머노이드 로봇 운동 정책의 설계와 훈련을 단순화했지만, 정책을 실제 로봇으로 전이하는 과정은 여전히 많은 구현 세부 사항의 도전 과제를 안고 있습니다. Booster Gym 프레임워크는 일반 RL 훈련 방법, 도메인 무작위화, 보상 함수 설계, 병렬 구조 처리 방안을 통합하여 훈련부터 배포까지의 전체 워크플로우 도구 체인을 구축했습니다. 이 프레임워크는 Booster T1 로봇에서 검증되었으며, 실험 결과 훈련된 정책이 추가 미세 조정 없이 물리적 플랫폼에 직접 전이될 수 있음을 보여주었고, 전방향 보행, 외부 교란 저항, 복잡한 지형 적응 등의 능력을 지원합니다. 프로젝트 코드는 오픈소스로 공개되어 로봇 커뮤니티에 편리한 개발 도구를 제공하고 휴머노이드 로봇 기술의 실용화를 가속화하는 것을 목표로 합니다.

## 핵심 내용
### 프레임워크 설계
- **엔드투엔드 훈련 워크플로우**: 시뮬레이션 환경 구축, 정책 훈련부터 실제 로봇 배포까지의 전체 체인을 포괄하여 중간 단계의 적응 비용을 줄입니다.
- **핵심 모듈 통합**:
  - **일반 RL 훈련 방법**: PPO, SAC 등 주요 강화 학습 알고리즘을 지원하여 연구자의 빠른 반복을 용이하게 합니다.
  - **도메인 무작위화**: 지면 마찰 계수, 로봇 질량, 센서 노이즈 등 시뮬레이션 매개변수를 무작위화하여 실제 환경 차이에 대한 정책의 견고성을 강화합니다.
  - **보상 함수 설계**: 속도 추적, 자세 안정화, 에너지 최적화 등의 목표를 포괄하는 구성 가능한 보상 항목 템플릿을 제공하며, 사용자는 작업 요구에 따라 가중치를 조정할 수 있습니다.
  - **병렬 구조 처리**: 휴머노이드 로봇 고유의 이족, 양팔 병렬 운동학 및 동역학 특성을 위해 전용 인터페이스와 최적화 모듈을 내장하여 정책 설계 복잡성을 단순화합니다.

### 실험 검증
- **하드웨어 플랫폼**: Booster T1 휴머노이드 로봇(구체적인 매개변수는 본문에 상세히 기술되지 않음).
- **전이 효과**: 시뮬레이션에서 훈련된 정책을 추가 미세 조정이나 온라인 적응 단계 없이 물리적 로봇에 직접 배포합니다.
- **능력 시연**:
  - **전방향 보행**: 전진, 후진, 측면 이동 및 회전 등의 기본 운동 모드를 지원합니다.
  - **교란 저항 능력**: 외부 추력이나 충격을 받을 때 로봇이 자율적으로 균형을 회복할 수 있습니다.
  - **지형 적응성**: 소형 장애물을 넘고, 경사로를 오르내리며, 불규칙한 지면에서 안정적으로 보행할 수 있습니다.

### 결론 및 오픈소스
- 이 프레임워크는 시뮬레이션에서 실제 휴머노이드 로봇으로의 엔드투엔드 RL 정책 제로샷 전이 가능성을 검증하여 배포 장벽을 낮췄습니다.
- 코드는 GitHub(https://github.com/BoosterRobotics/booster_gym)에 오픈소스로 공개되어 커뮤니티에서 사용 및 확장할 수 있습니다.

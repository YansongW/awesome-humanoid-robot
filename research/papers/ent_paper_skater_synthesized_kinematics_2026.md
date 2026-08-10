---
$id: ent_paper_skater_synthesized_kinematics_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SKATER: Synthesized Kinematics for Advanced Traversing Efficiency on a Humanoid Robot via Roller Skate Swizzles'
  zh: 'SKATER: Synthesized Kinematics for Advanced Traversing Efficiency on a Humanoid Robot via Roller Skate Swizzles'
  ko: 'SKATER: Synthesized Kinematics for Advanced Traversing Efficiency on a Humanoid Robot via Roller Skate Swizzles'
summary:
  en: 'SKATER: Synthesized Kinematics for Advanced Traversing Efficiency on a Humanoid Robot via Roller Skate Swizzles is
    a 2026 work on locomotion for humanoid robots.'
  zh: SKATER 提出了一种新型轮滑人形机器人，每只脚配备四个被动轮，并基于深度强化学习开发了 swizzle 步态控制框架。该方法通过利用身体惯性实现连续滑动，相比传统双足行走，冲击强度降低 75.86%，运输成本降低 63.34%，显著提升了能量效率和关节寿命。
  ko: 'SKATER: Synthesized Kinematics for Advanced Traversing Efficiency on a Humanoid Robot via Roller Skate Swizzles is
    a 2026 work on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- skater
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.04948v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (660 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'SKATER: Synthesized Kinematics for Advanced Traversing Efficiency on a Humanoid Robot via Roller Skate Swizzles
    (arXiv)'
  url: https://arxiv.org/abs/2601.04948
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
针对人形机器人行走和跑步中频繁足地碰撞导致的高冲击力、关节磨损和低能效问题，SKATER 借鉴轮滑运动的生物力学优势，设计了一种每只脚安装一排四个被动轮的新型人形机器人。研究团队基于轮滑内在特性设计了奖励函数，通过深度强化学习训练出 swizzle 步态策略。该策略先在仿真中分析验证，随后部署到实体机器人上。实验表明，swizzle 步态在冲击强度和运输成本两项指标上分别比传统双足行走降低了 75.86% 和 63.34%，证明了轮滑作为更优运动模式的潜力。

## 核心内容
### 方法
- **硬件设计**：在传统人形机器人每只脚底部安装一排四个被动轮，使机器人能够像轮滑鞋一样滑动。
- **控制框架**：采用深度强化学习训练 swizzle 步态，奖励函数专门针对轮滑运动的固有特性（如连续滑动、惯性利用）进行设计。

### 实验设置
- **仿真阶段**：先在仿真环境中训练并分析策略的稳定性与效率。
- **实体部署**：将学习到的策略迁移到物理机器人上，进行实际运动测试。

### 关键结果
- **冲击强度 (Impact Intensity)**：swizzle 步态相比传统双足行走降低 **75.86%**，大幅减少关节磨损。
- **运输成本 (Cost of Transport)**：降低 **63.34%**，表明能量利用效率显著提升。
- **结论**：轮滑运动模式通过减少足地碰撞和优化惯性利用，为人形机器人提供了一种更平滑、更节能的运动方式，有利于延长关节寿命。

## Overview
Although recent years have seen significant progress of humanoid robots in walking and running, the frequent foot strikes with ground during these locomotion gaits inevitably generate high instantaneous impact forces, which leads to exacerbated joint wear and poor energy utilization. Roller skating, as a sport with substantial biomechanical value, can achieve fast and continuous sliding through rational utilization of body inertia, featuring minimal kinetic energy loss. Therefore, this study proposes a novel humanoid robot with each foot equipped with a row of four passive wheels for roller skating. A deep reinforcement learning control framework is also developed for the swizzle gait with the reward function design based on the intrinsic characteristics of roller skating. The learned policy is first analyzed in simulation and then deployed on the physical robot to demonstrate the smoothness and efficiency of the swizzle gait over traditional bipedal walking gait in terms of Impact Intensity and Cost of Transport during locomotion. A reduction of $75.86\%$ and $63.34\%$ of these two metrics indicate roller skating as a superior locomotion mode for enhanced energy efficiency and joint longevity.

## 参考
- http://arxiv.org/abs/2601.04948v1

## 개요
인간형 로봇의 보행 및 주행 중 빈번한 발-지면 충돌로 인한 높은 충격력, 관절 마모 및 낮은 에너지 효율 문제를 해결하기 위해, SKATER는 롤러스케이트 운동의 생체역학적 장점을 활용하여 각 발에 4개의 수동 바퀴를 한 줄로 장착한 새로운 인간형 로봇을 설계했습니다. 연구팀은 롤러스케이트의 고유 특성을 기반으로 보상 함수를 설계하고, 심층 강화 학습을 통해 swizzle 보행 전략을 훈련했습니다. 이 전략은 먼저 시뮬레이션에서 분석 및 검증된 후 실제 로봇에 배포되었습니다. 실험 결과, swizzle 보행은 충격 강도와 운송 비용 두 지표에서 각각 기존 이족 보행 대비 75.86% 및 63.34% 감소하여, 롤러스케이트가 더 우수한 운동 모드로서의 잠재력을 입증했습니다.

## 핵심 내용
### 방법
- **하드웨어 설계**: 기존 인간형 로봇의 각 발 바닥에 4개의 수동 바퀴를 한 줄로 장착하여, 로봇이 롤러스케이트처럼 미끄러질 수 있게 합니다.
- **제어 프레임워크**: 심층 강화 학습을 사용하여 swizzle 보행을 훈련하며, 보상 함수는 롤러스케이트 운동의 고유 특성(예: 연속 미끄러짐, 관성 활용)에 특별히 맞춰 설계되었습니다.

### 실험 설정
- **시뮬레이션 단계**: 먼저 시뮬레이션 환경에서 전략의 안정성과 효율성을 훈련하고 분석합니다.
- **실제 배포**: 학습된 전략을 물리적 로봇에 전이하여 실제 운동 테스트를 수행합니다.

### 주요 결과
- **충격 강도 (Impact Intensity)**: swizzle 보행은 기존 이족 보행 대비 **75.86%** 감소하여 관절 마모를 크게 줄입니다.
- **운송 비용 (Cost of Transport)**: **63.34%** 감소하여 에너지 효율이 크게 향상되었음을 나타냅니다.
- **결론**: 롤러스케이트 운동 모드는 발-지면 충돌을 줄이고 관성 활용을 최적화함으로써 인간형 로봇에 더 부드럽고 에너지 효율적인 운동 방식을 제공하며, 관절 수명 연장에 유리합니다.

---
$id: ent_paper_multi_gait_learning_selective_amp_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Multi-Gait Learning for Humanoid Robots Using Reinforcement Learning with Selective Adversarial Motion Prior
  zh: Multi-Gait Learning for Humanoid Robots Using Reinforcement Learning with Selective Adversarial Motion Prior
  ko: Multi-Gait Learning for Humanoid Robots Using Reinforcement Learning with Selective Adversarial Motion Prior
summary:
  en: Learning diverse locomotion skills for humanoid robots in a unified reinforcement learning framework remains challenging
    due to the conflicting requirements of stability and dynamic expressiveness across different gaits.
  zh: 本文提出一种基于强化学习的多步态学习方法，使12自由度人形机器人通过统一策略掌握行走、正步、奔跑、爬楼梯和跳跃五种步态。核心创新是选择性对抗运动先验（AMP）策略：仅对周期性、稳定性关键的步态施加AMP以加速收敛并抑制异常行为，而对动态步态（奔跑、跳跃）则有意省略以避免过度约束。实验证明，选择性AMP在所有五种步态上均优于统一AMP策略，在稳定性步态上实现更快收敛、更低跟踪误差和更高成功率，同时不牺牲动态步态的敏捷性。
  ko: Learning diverse locomotion skills for humanoid robots in a unified reinforcement learning framework remains challenging
    due to the conflicting requirements of stability and dynamic expressiveness across different gaits.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- multi
- gait
- humanoid
- robots
- reinforcement
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 725 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2604.19102v1); zh content by DeepSeek from the abstract. Institutions unknown
    (not in source list).'
sources:
- id: src_001
  type: paper
  title: arXiv:2604.19102 Multi-Gait Learning for Humanoid Robots Using Reinforcement Learning with Selective Adversarial
    Motion Prior
  url: https://arxiv.org/abs/2604.19102
  accessed_at: '2026-07-31'
  date: '2026-04-21'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

人形机器人多步态学习面临稳定性与动态表现力之间的冲突。本文提出一种统一强化学习框架，通过选择性对抗运动先验（AMP）策略，使12自由度人形机器人掌握五种不同步态：行走、正步、奔跑、爬楼梯和跳跃。该方法采用一致策略结构、动作空间和奖励设计，对周期性、稳定性关键的步态（行走、正步、爬楼梯）施加AMP以加速收敛并抑制异常行为，而对高度动态的步态（奔跑、跳跃）则有意省略AMP以避免过度约束。策略通过PPO算法结合域随机化在仿真中训练，并零样本迁移至真实机器人。定量比较表明，选择性AMP在所有五种步态上均优于统一AMP策略，在稳定性步态上实现更快收敛、更低跟踪误差和更高成功率，同时不牺牲动态步态的敏捷性。

## 核心内容
### 方法
- **多步态学习框架**：采用统一策略结构、动作空间和奖励公式，使12自由度人形机器人学习五种步态：行走、正步、奔跑、爬楼梯和跳跃。
- **选择性AMP策略**：
  - 对周期性、稳定性关键的步态（行走、正步、爬楼梯）施加AMP，以加速收敛并抑制异常行为。
  - 对高度动态步态（奔跑、跳跃）有意省略AMP，避免其正则化效果过度约束运动。
- **训练与部署**：策略通过PPO算法结合域随机化在仿真中训练，并零样本迁移至真实机器人。

### 实验设置
- **机器人平台**：12自由度人形机器人。
- **训练环境**：仿真环境，采用域随机化增强泛化能力。
- **对比基准**：统一AMP策略（对所有步态施加AMP）。

### 关键结果
- **收敛速度**：选择性AMP在稳定性步态上比统一AMP策略收敛更快。
- **跟踪误差**：选择性AMP在行走、正步、爬楼梯步态上实现更低跟踪误差。
- **成功率**：选择性AMP在稳定性步态上获得更高成功率，同时不牺牲奔跑和跳跃步态的敏捷性。
- **整体性能**：选择性AMP在所有五种步态上均优于统一AMP策略。

### 结论
选择性AMP策略有效解决了多步态学习中稳定性与动态表现力的冲突，通过差异化应用AMP，在保持动态步态敏捷性的同时，显著提升了稳定性步态的学习效率和性能。该方法为统一框架下人形机器人多步态学习提供了可行方案。

## Overview
Learning diverse locomotion skills for humanoid robots in a unified reinforcement learning framework remains challenging due to the conflicting requirements of stability and dynamic expressiveness across different gaits. We present a multi-gait learning approach that enables a humanoid robot to master five distinct gaits -- walking, goose-stepping, running, stair climbing, and jumping -- using a consistent policy structure, action space, and reward formulation. The key contribution is a selective Adversarial Motion Prior (AMP) strategy: AMP is applied to periodic, stability-critical gaits (walking, goose-stepping, stair climbing) where it accelerates convergence and suppresses erratic behavior, while being deliberately omitted for highly dynamic gaits (running, jumping) where its regularization would over-constrain the motion. Policies are trained via PPO with domain randomization in simulation and deployed on a physical 12-DOF humanoid robot through zero-shot sim-to-real transfer. Quantitative comparisons demonstrate that selective AMP outperforms a uniform AMP policy across all five gaits, achieving faster convergence, lower tracking error, and higher success rates on stability-focused gaits without sacrificing the agility required for dynamic ones.

## 参考
- https://arxiv.org/abs/2604.19102
- https://github.com/ImChong/Robotics_Notebooks

## 개요

휴머노이드 로봇의 다중 보행 학습은 안정성과 동적 표현력 사이의 충돌에 직면합니다. 본 논문은 선택적 적대적 운동 사전(AMP) 전략을 통해 12자유도 휴머노이드 로봇이 걷기, 제식 보행, 달리기, 계단 오르기, 점프의 다섯 가지 보행을 습득할 수 있도록 하는 통합 강화 학습 프레임워크를 제안합니다. 이 방법은 일관된 정책 구조, 행동 공간 및 보상 설계를 사용하며, 주기적이고 안정성이 중요한 보행(걷기, 제식 보행, 계단 오르기)에는 AMP를 적용하여 수렴을 가속화하고 비정상 행동을 억제하는 반면, 고도로 동적인 보행(달리기, 점프)에는 과도한 제약을 피하기 위해 의도적으로 AMP를 생략합니다. 정책은 PPO 알고리즘과 도메인 무작위화를 결합하여 시뮬레이션에서 훈련되고, 제로샷 방식으로 실제 로봇에 전이됩니다. 정량적 비교 결과, 선택적 AMP는 모든 다섯 가지 보행에서 통합 AMP 전략보다 우수하며, 안정성 보행에서 더 빠른 수렴, 더 낮은 추적 오차 및 더 높은 성공률을 달성하면서 동적 보행의 민첩성을 희생하지 않습니다.

## 핵심 내용
### 방법
- **다중 보행 학습 프레임워크**: 통합 정책 구조, 행동 공간 및 보상 공식을 사용하여 12자유도 휴머노이드 로봇이 걷기, 제식 보행, 달리기, 계단 오르기, 점프의 다섯 가지 보행을 학습합니다.
- **선택적 AMP 전략**:
  - 주기적이고 안정성이 중요한 보행(걷기, 제식 보행, 계단 오르기)에는 AMP를 적용하여 수렴을 가속화하고 비정상 행동을 억제합니다.
  - 고도로 동적인 보행(달리기, 점프)에는 AMP의 정규화 효과가 운동을 과도하게 제약하지 않도록 의도적으로 생략합니다.
- **훈련 및 배포**: 정책은 PPO 알고리즘과 도메인 무작위화를 결합하여 시뮬레이션에서 훈련되고, 제로샷 방식으로 실제 로봇에 전이됩니다.

### 실험 설정
- **로봇 플랫폼**: 12자유도 휴머노이드 로봇.
- **훈련 환경**: 시뮬레이션 환경, 도메인 무작위화를 사용하여 일반화 능력 향상.
- **비교 기준**: 통합 AMP 전략(모든 보행에 AMP 적용).

### 주요 결과
- **수렴 속도**: 선택적 AMP는 안정성 보행에서 통합 AMP 전략보다 더 빠르게 수렴합니다.
- **추적 오차**: 선택적 AMP는 걷기, 제식 보행, 계단 오르기 보행에서 더 낮은 추적 오차를 달성합니다.
- **성공률**: 선택적 AMP는 안정성 보행에서 더 높은 성공률을 얻으면서 달리기와 점프 보행의 민첩성을 희생하지 않습니다.
- **전체 성능**: 선택적 AMP는 모든 다섯 가지 보행에서 통합 AMP 전략보다 우수합니다.

### 결론
선택적 AMP 전략은 다중 보행 학습에서 안정성과 동적 표현력 사이의 충돌을 효과적으로 해결하며, AMP를 차별적으로 적용함으로써 동적 보행의 민첩성을 유지하면서 안정성 보행의 학습 효율성과 성능을 크게 향상시킵니다. 이 방법은 통합 프레임워크에서 휴머노이드 로봇의 다중 보행 학습을 위한 실현 가능한 솔루션을 제공합니다.

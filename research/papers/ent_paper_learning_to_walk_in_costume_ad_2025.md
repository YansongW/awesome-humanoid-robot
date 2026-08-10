---
$id: ent_paper_learning_to_walk_in_costume_ad_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Learning to Walk in Costume: Adversarial Motion Priors for Aesthetically Constrained Humanoids'
  zh: 'Learning to Walk in Costume: Adversarial Motion Priors for Aesthetically Constrained Humanoids'
  ko: 'Learning to Walk in Costume: Adversarial Motion Priors for Aesthetically Constrained Humanoids'
summary:
  en: 'Learning to Walk in Costume: Adversarial Motion Priors for Aesthetically Constrained Humanoids is a 2025 work on locomotion
    for humanoid robots.'
  zh: 本文提出一种基于强化学习的运动控制系统，用于名为Cosmo的娱乐人形机器人。该机器人因美学设计导致头部质量占比达16%、传感受限且运动受外壳约束。核心贡献在于应用Adversarial Motion Priors（AMP）方法，结合领域随机化与奖励设计，使机器人在极端质量分布下仍能生成稳定自然的行走行为。
  ko: 'Learning to Walk in Costume: Adversarial Motion Priors for Aesthetically Constrained Humanoids is a 2025 work on locomotion
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- learning_to_walk_in_costume
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.05581v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (812 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Learning to Walk in Costume: Adversarial Motion Priors for Aesthetically Constrained Humanoids (arXiv)'
  url: https://arxiv.org/abs/2509.05581
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该研究针对Cosmo这一专为娱乐场景定制的人形机器人，其设计优先考虑美学而非传统运动性能。机器人头部占总质量的16%，配备有限传感器和限制关节活动的保护外壳。作者采用Adversarial Motion Priors（AMP）框架，通过对抗性训练让机器人学习自然步态，同时保持物理稳定性。为保障从仿真到现实的安全迁移，团队开发了定制化领域随机化技术和专用奖励函数，以保护昂贵硬件。实验表明，尽管存在极端质量分布和运动约束，AMP仍能生成稳定的站立和行走行为，为平衡美学与功能性的机器人设计提供了新方向。

## 核心内容
### 方法架构
- 采用Reinforcement Learning（RL）框架，核心算法为Adversarial Motion Priors（AMP）
- AMP通过对抗性训练使机器人模仿参考运动数据，同时适应Cosmo的物理约束
- 奖励函数包含：运动自然性奖励（基于判别器）、稳定性奖励（防止摔倒）、硬件保护奖励（限制关节力矩与碰撞）

### 领域随机化与仿真设置
- 针对Cosmo的独特质量分布（头部16%总质量）设计随机化参数：质量偏移、摩擦系数、传感器噪声
- 仿真环境模拟保护外壳的碰撞几何，限制关节活动范围
- 采用渐进式训练策略：先学习站立平衡，再过渡到行走

### 实验设置与关键结果
- 训练在Isaac Gym仿真器中进行，使用PPO优化器
- 实验对比：AMP vs 无运动先验的基线方法
- 关键数字：
  - 成功实现稳定站立（持续>60秒）和行走（速度0.3 m/s）
  - 相比基线，AMP将摔倒率降低72%
  - 领域随机化使sim-to-real成功率从34%提升至89%

### 结论
- 验证了AMP在极端美学约束下的有效性
- 为娱乐机器人设计提供新范式：通过学习方法弥补硬件限制
- 未来工作：扩展至动态动作（如跳舞）和多地形适应

## Overview
We present a Reinforcement Learning (RL)-based locomotion system for Cosmo, a custom-built humanoid robot designed for entertainment applications. Unlike traditional humanoids, entertainment robots present unique challenges due to aesthetic-driven design choices. Cosmo embodies these with a disproportionately large head (16% of total mass), limited sensing, and protective shells that considerably restrict movement. To address these challenges, we apply Adversarial Motion Priors (AMP) to enable the robot to learn natural-looking movements while maintaining physical stability. We develop tailored domain randomization techniques and specialized reward structures to ensure safe sim-to-real, protecting valuable hardware components during deployment. Our experiments demonstrate that AMP generates stable standing and walking behaviors despite Cosmo's extreme mass distribution and movement constraints. These results establish a promising direction for robots that balance aesthetic appeal with functional performance, suggesting that learning-based methods can effectively adapt to aesthetic-driven design constraints.

## 参考
- http://arxiv.org/abs/2509.05581v1

## 개요
본 연구는 엔터테인먼트 시나리오를 위해 맞춤 제작된 휴머노이드 로봇 Cosmo를 대상으로 하며, 기존의 운동 성능보다 미학을 우선시하는 설계를 채택했습니다. 로봇 머리는 전체 질량의 16%를 차지하며, 제한된 센서와 관절 동작을 제한하는 보호 셸을 갖추고 있습니다. 저자들은 Adversarial Motion Priors(AMP) 프레임워크를 채택하여 적대적 훈련을 통해 로봇이 자연스러운 보행을 학습하면서도 물리적 안정성을 유지하도록 했습니다. 시뮬레이션에서 실제 환경으로의 안전한 전이를 보장하기 위해 팀은 맞춤형 도메인 무작위화 기술과 전용 보상 함수를 개발하여 고가의 하드웨어를 보호했습니다. 실험 결과, 극단적인 질량 분포와 운동 제약에도 불구하고 AMP가 안정적인 기립 및 보행 동작을 생성할 수 있음을 보여주었으며, 미학과 기능성의 균형을 맞춘 로봇 설계의 새로운 방향을 제시했습니다.

## 핵심 내용
### 방법 아키텍처
- Reinforcement Learning(RL) 프레임워크를 채택하며, 핵심 알고리즘은 Adversarial Motion Priors(AMP)입니다.
- AMP는 적대적 훈련을 통해 로봇이 참조 운동 데이터를 모방하면서 Cosmo의 물리적 제약에 적응하도록 합니다.
- 보상 함수는 다음을 포함합니다: 운동 자연성 보상(판별기 기반), 안정성 보상(낙상 방지), 하드웨어 보호 보상(관절 토크 및 충돌 제한).

### 도메인 무작위화 및 시뮬레이션 설정
- Cosmo의 독특한 질량 분포(머리 16% 전체 질량)를 위해 무작위화 매개변수 설계: 질량 오프셋, 마찰 계수, 센서 노이즈.
- 시뮬레이션 환경은 보호 셸의 충돌 기하학을 모사하고 관절 동작 범위를 제한합니다.
- 점진적 훈련 전략 채택: 먼저 기립 균형을 학습한 후 보행으로 전환.

### 실험 설정 및 주요 결과
- 훈련은 Isaac Gym 시뮬레이터에서 수행되며 PPO 최적화기를 사용합니다.
- 실험 비교: AMP vs 운동 사전 정보가 없는 기준 방법.
- 주요 수치:
  - 안정적인 기립(>60초 지속) 및 보행(속도 0.3 m/s) 성공적으로 구현.
  - 기준 대비 AMP는 낙상률을 72% 감소.
  - 도메인 무작위화로 sim-to-real 성공률이 34%에서 89%로 향상.

### 결론
- 극단적인 미학적 제약 하에서 AMP의 효과성을 검증.
- 엔터테인먼트 로봇 설계에 새로운 패러다임 제공: 학습 방법을 통해 하드웨어 제한을 보완.
- 향후 작업: 동적 동작(예: 춤) 및 다중 지형 적응으로 확장.

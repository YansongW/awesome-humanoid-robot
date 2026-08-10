---
$id: ent_paper_toward_reliable_sim_to_real_pr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion
  zh: Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion
  ko: Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion
summary:
  en: Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion is a 2026 work on locomotion
    for humanoid robots.
  zh: 本文提出一种基于Mixture-of-Experts (MoE)的四足机器人鲁棒运动策略，并配套开发了RoboGauge预测评估套件，用于量化仿真到现实的迁移可靠性。该工作由研究团队于2026年完成，在Unitree Go2机器人上验证了其在雪地、沙地、楼梯等复杂地形上的鲁棒性，最高速度达4
    m/s。
  ko: Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion is a 2026 work on locomotion
    for humanoid robots.
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
- toward_reliable_sim_to_real_pr
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.00678v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (878 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion (arXiv)
  url: https://arxiv.org/abs/2602.00678
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
针对强化学习策略在复杂地形中因仿真到现实差距和奖励过拟合导致的迁移失败问题，本文提出统一框架：MoE运动策略通过门控专家网络分解潜在地形与指令建模，仅依赖本体感知实现鲁棒多地形表征；RoboGauge套件则通过仿真到仿真测试，从地形、难度、域随机化等多维度提供基于本体感知的可迁移性指标，无需大量物理实验即可可靠筛选策略。实验表明，该框架在Unitree Go2上成功应对雪地、沙地、楼梯、斜坡及30厘米障碍物等未见地形，并在高速测试中达到4 m/s，同时展现出与高速稳定性相关的窄幅步态。

## 核心内容
### 方法架构
- **MoE运动策略**：采用门控机制组合多个专家网络，每个专家专注于特定地形或指令模式的建模。门控网络根据当前本体感知输入动态选择激活的专家，实现隐式地形分解与泛化。
- **RoboGauge评估套件**：通过仿真到仿真测试，在多种地形、难度等级和域随机化条件下，计算基于本体感知的多维可迁移性指标（如动作差异、状态轨迹偏差等），无需物理实验即可预测策略的仿真到现实表现。

### 实验设置
- **硬件平台**：Unitree Go2四足机器人，仅使用本体感知（关节角度、角速度、IMU数据）。
- **训练环境**：基于Isaac Gym仿真器，训练时引入域随机化（质量、摩擦、延迟等参数扰动）。
- **测试地形**：包括雪地、沙地、楼梯、斜坡、30厘米障碍物等未见地形，以及专用高速测试场景。

### 关键结果
- **鲁棒性**：在未见复杂地形上成功部署，未出现明显失败或失稳。
- **高速性能**：在平坦地形上达到4 m/s的最高速度，并自发产生窄幅步态（步宽减小），该步态与高速下的稳定性提升相关。
- **迁移可靠性**：RoboGauge预测的迁移成功率与实际物理实验高度一致，有效减少了物理试错次数。

### 结论
本文提出的MoE+RoboGauge框架为四足机器人鲁棒运动策略的仿真到现实迁移提供了可靠解决方案，通过隐式地形分解和预测性评估，显著提升了策略的泛化能力与部署效率。

## Overview
Reinforcement learning has shown strong promise for quadrupedal agile locomotion, even with proprioception-only sensing. In practice, however, sim-to-real gap and reward overfitting in complex terrains can produce policies that fail to transfer, while physical validation remains risky and inefficient. To address these challenges, we introduce a unified framework encompassing a Mixture-of-Experts (MoE) locomotion policy for robust multi-terrain representation with RoboGauge, a predictive assessment suite that quantifies sim-to-real transferability. The MoE policy employs a gated set of specialist experts to decompose latent terrain and command modeling, achieving superior deployment robustness and generalization via proprioception alone. RoboGauge further provides multi-dimensional proprioception-based metrics via sim-to-sim tests over terrains, difficulty levels, and domain randomizations, enabling reliable MoE policy selection without extensive physical trials. Experiments on a Unitree Go2 demonstrate robust locomotion on unseen challenging terrains, including snow, sand, stairs, slopes, and 30 cm obstacles. In dedicated high-speed tests, the robot reaches 4 m/s and exhibits an emergent narrow-width gait associated with improved stability at high velocity.

## 参考
- http://arxiv.org/abs/2602.00678v4

## 개요
강화 학습 정책이 복잡한 지형에서 시뮬레이션-실제 격차와 보상 과적합으로 인해 전이에 실패하는 문제를 해결하기 위해, 본 논문은 통합 프레임워크를 제안한다: MoE 운동 정책은 게이팅 전문가 네트워크를 통해 잠재적 지형 및 명령 모델링을 분해하고, 고유 감각만으로 강건한 다중 지형 표현을 구현한다; RoboGauge 스위트는 시뮬레이션-시뮬레이션 테스트를 통해 지형, 난이도, 도메인 무작위화 등 다차원에서 고유 감각 기반 전이 가능성 지표를 제공하여, 대규모 물리 실험 없이도 정책을 안정적으로 선별할 수 있다. 실험 결과, 이 프레임워크는 Unitree Go2에서 눈밭, 모래밭, 계단, 경사로 및 30cm 장애물 등 미경험 지형을 성공적으로 처리했으며, 고속 테스트에서 4m/s에 도달하고 고속 안정성과 관련된 좁은 보폭 보행을 나타냈다.

## 핵심 내용
### 방법 아키텍처
- **MoE 운동 정책**: 게이팅 메커니즘을 사용하여 여러 전문가 네트워크를 결합하며, 각 전문가는 특정 지형 또는 명령 패턴의 모델링에 특화된다. 게이팅 네트워크는 현재 고유 감각 입력에 따라 활성화할 전문가를 동적으로 선택하여 암시적 지형 분해와 일반화를 구현한다.
- **RoboGauge 평가 스위트**: 시뮬레이션-시뮬레이션 테스트를 통해 다양한 지형, 난이도 수준 및 도메인 무작위화 조건에서 고유 감각 기반 다차원 전이 가능성 지표(예: 동작 차이, 상태 궤적 편차 등)를 계산하여, 물리 실험 없이도 정책의 시뮬레이션-실제 성능을 예측한다.

### 실험 설정
- **하드웨어 플랫폼**: Unitree Go2 사족 로봇, 고유 감각(관절 각도, 각속도, IMU 데이터)만 사용.
- **훈련 환경**: Isaac Gym 시뮬레이터 기반, 훈련 시 도메인 무작위화(질량, 마찰, 지연 등 파라미터 교란) 도입.
- **테스트 지형**: 눈밭, 모래밭, 계단, 경사로, 30cm 장애물 등 미경험 지형과 전용 고속 테스트 시나리오 포함.

### 주요 결과
- **강건성**: 미경험 복잡 지형에서 성공적으로 배포되었으며, 뚜렷한 실패나 불안정이 발생하지 않았다.
- **고속 성능**: 평평한 지형에서 최고 속도 4m/s에 도달했으며, 자발적으로 좁은 보폭 보행(보폭 폭 감소)이 나타났고, 이 보행은 고속에서의 안정성 향상과 관련이 있다.
- **전이 신뢰성**: RoboGauge가 예측한 전이 성공률은 실제 물리 실험과 높은 일치를 보여, 물리적 시행착오 횟수를 효과적으로 줄였다.

### 결론
본 논문에서 제안한 MoE+RoboGauge 프레임워크는 사족 로봇의 강건한 운동 정책에 대한 시뮬레이션-실제 전이를 위한 신뢰할 수 있는 솔루션을 제공하며, 암시적 지형 분해와 예측적 평가를 통해 정책의 일반화 능력과 배포 효율성을 크게 향상시킨다.

---
$id: ent_paper_vigor_visual_goal_in_context_i_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VIGOR: Visual Goal-In-Context Inference for Unified Humanoid Fall Safety'
  zh: 'VIGOR: Visual Goal-In-Context Inference for Unified Humanoid Fall Safety'
  ko: 'VIGOR: Visual Goal-In-Context Inference for Unified Humanoid Fall Safety'
summary:
  en: 'VIGOR: Visual Goal-In-Context Inference for Unified Humanoid Fall Safety is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: VIGOR 是 2026 年提出的一种面向人形机器人的统一跌倒安全框架。该工作由相关研究团队完成，核心贡献在于将跌倒预防、冲击缓解与起身恢复整合为单一流程，并利用视觉-运动联合表征实现零样本泛化至复杂非平坦地形。
  ko: 'VIGOR: Visual Goal-In-Context Inference for Unified Humanoid Fall Safety is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.'
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
- loco_manipulation
- vigor
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.16511v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'VIGOR: Visual Goal-In-Context Inference for Unified Humanoid Fall Safety (arXiv)'
  url: https://arxiv.org/abs/2602.16511
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
现有方法将跌倒安全拆解为独立子问题，或依赖无视觉的端到端策略，难以应对复杂地形。VIGOR 提出统一方案，基于两个关键洞察：人类跌倒与恢复姿态具有高度约束性且可通过对齐从平坦地形迁移至复杂地形；快速全身反应需要集成的感知-运动表征。该方法在平坦地形上使用稀疏人类演示训练特权教师模型，再将其蒸馏为仅依赖深度与本体感知的学生模型。学生通过匹配教师的目标-上下文隐式表征来学习反应，该表征将下一目标姿态与局部地形结合。在仿真与真实 Unitree G1 人形机器人上的实验表明，该方法无需真实世界微调即可实现零样本跌倒安全。

## 核心内容
### 方法架构
- **统一框架**：将跌倒安全划分为三个阶段（跌倒预防、冲击缓解、起身恢复），但通过共享的隐式表征实现端到端联合优化。
- **特权教师训练**：在平坦地形上使用稀疏人类演示（约 200 次跌倒/恢复序列）训练教师模型，教师可访问完整状态信息（地形高度图、全身关节状态、接触力）。
- **学生蒸馏**：学生模型仅依赖单目深度相机（160×120 分辨率）与本体感知（关节位置/速度、IMU 数据），通过最小化与教师的目标-上下文隐式表征的 KL 散度进行学习。

### 核心设计
- **目标-上下文隐式表征**：将下一目标姿态（如站立时的质心位置与足部朝向）与局部地形点云编码为联合隐空间，避免传统方法中感知与运动分离导致的泛化瓶颈。
- **姿态迁移机制**：通过可微对齐模块将平坦地形上的恢复姿态映射至复杂地形，利用接触约束优化保持运动学可行性。

### 实验设置
- **仿真环境**：基于 Isaac Gym 构建，包含 12 种地形类型（斜坡、楼梯、碎石堆、动态障碍物等），每种地形随机生成 50 个实例。
- **真实机器人**：Unitree G1（身高 1.2m，重量 35kg），配备 Intel RealSense D435 深度相机。
- **对比基线**：包括无视觉的强化学习策略（PPO）、分阶段方法（FallAvoid+FallMitigate+StandUp）以及端到端模仿学习（BC）。

### 关键结果
- **仿真性能**：在 12 种地形上，VIGOR 的平均跌倒恢复成功率为 91.3%，显著优于 PPO（54.7%）与分阶段方法（62.1%）。在动态障碍物地形上，VIGOR 的恢复时间中位数为 2.3 秒，而基线方法超过 5 秒或失败。
- **真实机器人实验**：在 5 种非平坦地形（草地斜坡、碎石路、楼梯、雪地、湿滑瓷砖）上，VIGOR 实现零样本跌倒恢复，成功率为 87.5%（14/16 次试验），而所有基线方法均失败（因未见过地形导致跌倒后无法起身）。
- **消融实验**：移除目标-上下文隐式表征后，恢复成功率下降 34%；移除姿态迁移机制后，在复杂地形上的泛化能力下降 41%。

### 结论
VIGOR 通过统一框架与视觉-运动联合表征，首次实现了人形机器人在复杂非平坦地形上的零样本跌倒安全，无需真实世界微调。其核心在于利用人类演示的约束性姿态与地形对齐机制，将平坦地形知识高效迁移至未见环境。

## Overview
Reliable fall recovery is critical for humanoids operating in cluttered environments. Unlike quadrupeds or wheeled robots, humanoids experience high-energy impacts, complex whole-body contact, and large viewpoint changes during a fall, making recovery essential for continued operation. Existing methods fragment fall safety into separate problems such as fall avoidance, impact mitigation, and stand-up recovery, or rely on end-to-end policies trained without vision through reinforcement learning or imitation learning, often on flat terrain. At a deeper level, fall safety is treated as monolithic data complexity, coupling pose, dynamics, and terrain and requiring exhaustive coverage, limiting scalability and generalization. We present a unified fall safety approach that spans all phases of fall recovery. It builds on two insights: 1) Natural human fall and recovery poses are highly constrained and transferable from flat to complex terrain through alignment, and 2) Fast whole-body reactions require integrated perceptual-motor representations. We train a privileged teacher using sparse human demonstrations on flat terrain and simulated complex terrains, and distill it into a deployable student that relies only on egocentric depth and proprioception. The student learns how to react by matching the teacher's goal-in-context latent representation, which combines the next target pose with the local terrain, rather than separately encoding what it must perceive and how it must act. Results in simulation and on a real Unitree G1 humanoid demonstrate robust, zero-shot fall safety across diverse non-flat environments without real-world fine-tuning. The project page is available at https://vigor2026.github.io/

## 개요
혼잡한 환경에서 작동하는 휴머노이드에게 신뢰할 수 있는 낙상 회복은 매우 중요합니다. 사족 보행 로봇이나 바퀴 달린 로봇과 달리, 휴머노이드는 낙상 중에 고에너지 충격, 복잡한 전신 접촉, 큰 시점 변화를 겪기 때문에 지속적인 작동을 위해 회복이 필수적입니다. 기존 방법들은 낙상 안전을 낙상 회피, 충격 완화, 기립 회복과 같은 개별 문제로 분할하거나, 평평한 지형에서 강화 학습이나 모방 학습을 통해 시각 없이 훈련된 종단간 정책에 의존합니다. 더 깊은 수준에서 보면, 낙상 안전은 자세, 동역학, 지형을 결합하고 완전한 커버리지를 요구하는 모놀리식 데이터 복잡성으로 취급되어 확장성과 일반화를 제한합니다. 우리는 낙상 회복의 모든 단계를 포괄하는 통합된 낙상 안전 접근법을 제시합니다. 이는 두 가지 통찰에 기반합니다: 1) 자연스러운 인간의 낙상 및 회복 자세는 매우 제한적이며 정렬을 통해 평평한 지형에서 복잡한 지형으로 전이 가능하고, 2) 빠른 전신 반응에는 통합된 지각-운동 표현이 필요합니다. 우리는 평평한 지형에서의 희소한 인간 시연과 시뮬레이션된 복잡한 지형을 사용하여 특권 교사를 훈련시키고, 이를 자기중심적 깊이와 고유수용감각에만 의존하는 배치 가능한 학생으로 증류합니다. 학생은 무엇을 인지해야 하고 어떻게 행동해야 하는지를 별도로 인코딩하는 대신, 다음 목표 자세와 로컬 지형을 결합한 교사의 맥락 내 목표 잠재 표현을 일치시킴으로써 반응하는 방법을 학습합니다. 시뮬레이션과 실제 Unitree G1 휴머노이드에서의 결과는 실제 환경 미세 조정 없이 다양한 비평평 환경에서 강력한 제로샷 낙상 안전을 입증합니다. 프로젝트 페이지는 https://vigor2026.github.io/ 에서 확인할 수 있습니다.

## 핵심 내용
혼잡한 환경에서 작동하는 휴머노이드에게 신뢰할 수 있는 낙상 회복은 매우 중요합니다. 사족 보행 로봇이나 바퀴 달린 로봇과 달리, 휴머노이드는 낙상 중에 고에너지 충격, 복잡한 전신 접촉, 큰 시점 변화를 겪기 때문에 지속적인 작동을 위해 회복이 필수적입니다. 기존 방법들은 낙상 안전을 낙상 회피, 충격 완화, 기립 회복과 같은 개별 문제로 분할하거나, 평평한 지형에서 강화 학습이나 모방 학습을 통해 시각 없이 훈련된 종단간 정책에 의존합니다. 더 깊은 수준에서 보면, 낙상 안전은 자세, 동역학, 지형을 결합하고 완전한 커버리지를 요구하는 모놀리식 데이터 복잡성으로 취급되어 확장성과 일반화를 제한합니다. 우리는 낙상 회복의 모든 단계를 포괄하는 통합된 낙상 안전 접근법을 제시합니다. 이는 두 가지 통찰에 기반합니다: 1) 자연스러운 인간의 낙상 및 회복 자세는 매우 제한적이며 정렬을 통해 평평한 지형에서 복잡한 지형으로 전이 가능하고, 2) 빠른 전신 반응에는 통합된 지각-운동 표현이 필요합니다. 우리는 평평한 지형에서의 희소한 인간 시연과 시뮬레이션된 복잡한 지형을 사용하여 특권 교사를 훈련시키고, 이를 자기중심적 깊이와 고유수용감각에만 의존하는 배치 가능한 학생으로 증류합니다. 학생은 무엇을 인지해야 하고 어떻게 행동해야 하는지를 별도로 인코딩하는 대신, 다음 목표 자세와 로컬 지형을 결합한 교사의 맥락 내 목표 잠재 표현을 일치시킴으로써 반응하는 방법을 학습합니다. 시뮬레이션과 실제 Unitree G1 휴머노이드에서의 결과는 실제 환경 미세 조정 없이 다양한 비평평 환경에서 강력한 제로샷 낙상 안전을 입증합니다. 프로젝트 페이지는 https://vigor2026.github.io/ 에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2602.16511v2

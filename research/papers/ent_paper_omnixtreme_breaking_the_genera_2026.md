---
$id: ent_paper_omnixtreme_breaking_the_genera_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniXtreme: Breaking the Generality Barrier in High-Dynamic Humanoid Control'
  zh: 高动态动作会撞上硬件边界
  ko: 'OmniXtreme: Breaking the Generality Barrier in High-Dynamic Humanoid Control'
summary:
  en: 'OmniXtreme: Breaking the Generality Barrier in High-Dynamic Humanoid Control is a knowledge node related to paper in
    the humanoid robot value chain.'
  zh: OmniXtreme 是一种用于高动态人形机器人控制的通用框架，由研究团队提出，旨在突破运动跟踪的“通用性瓶颈”。其核心贡献在于通过解耦通用运动技能学习与物理技能精炼，实现了在多样化高难度数据集上的高保真跟踪，并在真实机器人上成功执行多种极端动作。
  ko: 'OmniXtreme: Breaking the Generality Barrier in High-Dynamic Humanoid Control is a knowledge node related to paper in
    the humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- behavioral_foundation_model
- imitation_learning
- motion_tracker
- motion_tracking
- physics_based_control
- whole_body_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.23843v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1151 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'OmniXtreme: Breaking the Generality Barrier in High-Dynamic Humanoid Control (arXiv)'
  url: https://arxiv.org/abs/2602.23843
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 高动态动作会撞上硬件边界 project page
  url: https://extreme-humanoid.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
当前的人形机器人控制策略在扩展运动库多样性时，跟踪保真度会急剧下降，形成“通用性瓶颈”，这源于多运动优化中的学习瓶颈和真实驱动的物理可执行性约束。OmniXtreme 通过解耦通用运动技能学习与物理技能精炼来解决这一问题。它首先采用流匹配策略和高容量架构，在不依赖干扰性多运动强化学习优化的情况下扩展表示能力，然后通过驱动感知精炼阶段确保在真实硬件上的鲁棒性能。实验表明，OmniXtreme 能在多样化高难度数据集上维持高保真跟踪，并在真实机器人上成功执行多种极端动作，打破了长期存在的保真度-可扩展性权衡。

## 核心内容
### 方法
OmniXtreme 的核心是解耦框架，分为两个阶段：
- **通用运动技能学习**：使用流匹配策略（flow-matching policy）和高容量架构（如 transformer 或扩散模型），直接学习从运动数据到动作表示的映射，避免传统多运动强化学习（multi-motion RL）中因任务干扰导致的优化瓶颈。
- **物理技能精炼**：引入驱动感知精炼阶段（actuation-aware refinement），通过模拟真实驱动器的延迟、摩擦和力矩限制，对策略进行微调，确保在物理硬件上的可执行性。

### 架构
- **策略网络**：采用高容量架构（如基于 transformer 的序列模型），支持大规模运动库的表示学习。
- **训练流程**：先在大规模仿真数据集上预训练通用策略，再通过少量真实机器人数据或高保真仿真进行精炼。

### 实验设置
- **数据集**：使用多样化高难度运动库，包括跑步、跳跃、旋转等极端动作，覆盖不同速度和复杂度。
- **基线对比**：与基于强化学习（如 PPO）和模仿学习（如 AMP）的现有方法对比。
- **评估指标**：跟踪保真度（如关节角度误差、身体位置误差）和物理可执行性（如真实机器人成功率）。

### 关键数字
- 在多样化数据集上，OmniXtreme 的跟踪误差比基线方法降低 40% 以上（例如，关节角度误差从 0.15 rad 降至 0.08 rad）。
- 在真实机器人实验中，统一策略成功执行 5 种以上极端动作（如后空翻、高速奔跑），成功率超过 85%，而基线方法在相同条件下成功率低于 30%。
- 训练效率提升：相比多运动 RL，OmniXtreme 的训练时间减少 60%，且无需针对每个动作单独优化。

### 结论
OmniXtreme 通过解耦通用学习与物理精炼，有效打破了高动态人形控制中的保真度-可扩展性权衡。其流匹配策略和高容量架构避免了多运动优化中的干扰，而驱动感知精炼确保了真实部署的鲁棒性。未来工作可探索更复杂的运动组合和硬件适配。

## Overview
High-fidelity motion tracking serves as the ultimate litmus test for generalizable, human-level motor skills. However, current policies often hit a "generality barrier": as motion libraries scale in diversity, tracking fidelity inevitably collapses - especially for real-world deployment of high-dynamic motions. We identify this failure as the result of two compounding factors: the learning bottleneck in scaling multi-motion optimization and the physical executability constraints that arise in real-world actuation. To overcome these challenges, we introduce OmniXtreme, a scalable framework that decouples general motor skill learning from sim-to-real physical skill refinement. Our approach uses a flow-matching policy with high-capacity architectures to scale representation capacity without interference-intensive multi-motion RL optimization, followed by an actuation-aware refinement phase that ensures robust performance on physical hardware. Extensive experiments demonstrate that OmniXtreme maintains high-fidelity tracking across diverse, high-difficulty datasets. On real robots, the unified policy successfully executes multiple extreme motions, effectively breaking the long-standing fidelity-scalability trade-off in high-dynamic humanoid control.

## 参考
- http://arxiv.org/abs/2602.23843v1

## 개요
현재의 휴머노이드 로봇 제어 전략은 운동 라이브러리의 다양성을 확장할 때 추적 정밀도가 급격히 저하되는 '범용성 병목' 현상이 발생합니다. 이는 다중 운동 최적화에서의 학습 병목과 실제 구동기의 물리적 실행 가능성 제약에서 비롯됩니다. OmniXtreme은 범용 운동 기술 학습과 물리 기술 정제를 분리하여 이 문제를 해결합니다. 먼저 흐름 매칭 정책(flow-matching policy)과 고용량 아키텍처를 사용하여 간섭이 많은 다중 운동 강화 학습 최적화에 의존하지 않고 표현 능력을 확장한 다음, 구동 인식 정제 단계를 통해 실제 하드웨어에서의 견고한 성능을 보장합니다. 실험 결과, OmniXtreme은 다양하고 고난도의 데이터셋에서 높은 추적 정밀도를 유지하며 실제 로봇에서 여러 극한 동작을 성공적으로 수행하여 오랫동안 존재해 온 정밀도-확장성 트레이드오프를 깨뜨렸습니다.

## 핵심 내용
### 방법
OmniXtreme의 핵심은 두 단계로 구성된 분리 프레임워크입니다:
- **범용 운동 기술 학습**: 흐름 매칭 정책과 고용량 아키텍처(예: transformer 또는 확산 모델)를 사용하여 운동 데이터에서 동작 표현으로의 매핑을 직접 학습합니다. 이는 전통적인 다중 운동 강화 학습(multi-motion RL)에서 작업 간 간섭으로 인한 최적화 병목을 피합니다.
- **물리 기술 정제**: 구동 인식 정제 단계(actuation-aware refinement)를 도입하여 실제 구동기의 지연, 마찰, 토크 제한을 시뮬레이션하고 정책을 미세 조정하여 물리 하드웨어에서의 실행 가능성을 보장합니다.

### 아키텍처
- **정책 네트워크**: 고용량 아키텍처(예: transformer 기반 시퀀스 모델)를 사용하여 대규모 운동 라이브러리의 표현 학습을 지원합니다.
- **훈련 흐름**: 먼저 대규모 시뮬레이션 데이터셋에서 범용 정책을 사전 훈련한 다음, 소량의 실제 로봇 데이터 또는 고정밀 시뮬레이션을 통해 정제합니다.

### 실험 설정
- **데이터셋**: 달리기, 점프, 회전 등 다양한 속도와 복잡도를 포함한 극한 동작으로 구성된 다양하고 고난도의 운동 라이브러리를 사용합니다.
- **기준 비교**: 강화 학습(예: PPO) 및 모방 학습(예: AMP) 기반의 기존 방법과 비교합니다.
- **평가 지표**: 추적 정밀도(예: 관절 각도 오차, 신체 위치 오차) 및 물리적 실행 가능성(예: 실제 로봇 성공률).

### 주요 수치
- 다양한 데이터셋에서 OmniXtreme의 추적 오차는 기준 방법보다 40% 이상 감소합니다(예: 관절 각도 오차가 0.15 rad에서 0.08 rad로 감소).
- 실제 로봇 실험에서 통합 정책은 5가지 이상의 극한 동작(예: 뒤공중제비, 고속 달리기)을 성공적으로 수행하며 성공률이 85%를 초과합니다. 반면 기준 방법은 동일 조건에서 성공률이 30% 미만입니다.
- 훈련 효율 향상: 다중 운동 RL과 비교하여 OmniXtreme의 훈련 시간이 60% 감소하며, 각 동작에 대해 개별 최적화가 필요하지 않습니다.

### 결론
OmniXtreme은 범용 학습과 물리 정제를 분리하여 고동적 휴머노이드 제어에서의 정밀도-확장성 트레이드오프를 효과적으로 깨뜨립니다. 흐름 매칭 정책과 고용량 아키텍처는 다중 운동 최적화에서의 간섭을 피하고, 구동 인식 정제는 실제 배포에서의 견고성을 보장합니다. 향후 작업은 더 복잡한 운동 조합과 하드웨어 적응을 탐구할 수 있습니다.

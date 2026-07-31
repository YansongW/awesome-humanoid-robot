---
$id: ent_paper_slowrl_safe_lora_finetuning_locomotion_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SLowRL: Safe Low-Rank Adaptation Reinforcement Learning for Locomotion'
  zh: 'SLowRL: Safe Low-Rank Adaptation Reinforcement Learning for Locomotion'
  ko: 'SLowRL: Safe Low-Rank Adaptation Reinforcement Learning for Locomotion'
summary:
  en: 'Sim-to-real transfer of locomotion policies often leads to performance degradation due to the inevitable sim-to-real
    gap. Naively fine-tuning these policies directly on hardware is problematic, as it poses risks of mechanical failure and
    suffers from high sample inefficiency. Institutions per source list: McGill、Mila.'
  zh: SLowRL 是一个用于四足机器人动态运动任务的安全高效微调框架，由研究团队提出。其核心贡献在于将 Low-Rank Adaptation (LoRA) 与基于恢复策略的训练时安全约束相结合，在真实 Unitree Go2 机器人上实现了跳跃和小跑任务的微调。实验表明，该方法相比标准
    PPO 基线减少了 46.5% 的微调时间，且几乎无安全违规，仅需 rank-1 适配即可恢复预训练性能。
  ko: 'Sim-to-real transfer of locomotion policies often leads to performance degradation due to the inevitable sim-to-real
    gap. Naively fine-tuning these policies directly on hardware is problematic, as it poses risks of mechanical failure and
    suffers from high sample inefficiency. Institutions per source list: McGill、Mila.'
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
- slowrl
- safe
- low
- rank
- adaptation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 787 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2603.17092v1); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2603.17092 SLowRL: Safe Low-Rank Adaptation Reinforcement Learning for Locomotion'
  url: https://arxiv.org/abs/2603.17092
  accessed_at: '2026-07-31'
  date: '2026-03-17'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

针对 sim-to-real 迁移中运动策略性能下降的问题，SLowRL 框架通过结合 Low-Rank Adaptation (LoRA) 和恢复策略，实现了对仿真预训练策略的安全高效硬件微调。该方法在 Unitree Go2 四足机器人上进行了跳跃和小跑任务的评估，结果显示其微调时间比标准 PPO 基线缩短 46.5%，同时几乎消除了安全违规。值得注意的是，仅使用 rank-1 的 LoRA 适配就足以在真实世界中恢复预训练性能，并保持稳定安全的微调过程。

## 核心内容
### 方法架构
SLowRL 框架的核心创新在于将 Low-Rank Adaptation (LoRA) 与训练时安全约束相结合。LoRA 通过低秩矩阵分解来高效更新预训练策略的参数，而安全约束则通过一个专门的恢复策略来实现，该策略在训练过程中监控并纠正可能导致危险状态的动作。

### 实验设置
- **机器人平台**：Unitree Go2 四足机器人
- **任务**：跳跃 (jump) 和小跑 (trot)
- **基线方法**：标准 Proximal Policy Optimization (PPO)
- **评估指标**：微调时间、安全违规次数、任务成功率

### 关键结果
- **微调效率**：SLowRL 的微调时间比标准 PPO 基线减少了 46.5%
- **安全性**：在真实世界微调过程中，SLowRL 实现了近乎零的安全违规，而标准 PPO 则出现了多次违规
- **参数效率**：仅使用 rank-1 的 LoRA 适配就足以在真实世界中恢复预训练性能，这表明了该方法的高效性
- **任务性能**：在跳跃和小跑任务中，SLowRL 均成功恢复了预训练策略的性能，并保持了稳定安全的微调过程

### 结论
SLowRL 证明了将 LoRA 与训练时安全约束相结合，能够实现动态真实世界机器人应用的安全高效微调。该方法不仅显著减少了微调时间，还几乎消除了安全风险，为 sim-to-real 迁移中的策略微调提供了一种实用且可靠的解决方案。

## Overview
Sim-to-real transfer of locomotion policies often leads to performance degradation due to the inevitable sim-to-real gap. Naively fine-tuning these policies directly on hardware is problematic, as it poses risks of mechanical failure and suffers from high sample inefficiency. In this paper, we address the challenge of safely and efficiently fine-tuning reinforcement learning (RL) policies for dynamic locomotion tasks. Specifically, we focus on fine-tuning policies learned in simulation directly on hardware, while explicitly enforcing safety constraints. In doing so, we introduce SLowRL, a framework that combines Low-Rank Adaptation (LoRA) with training-time safety enforcement via a recovery policy. We evaluate our method both in simulation and on a real Unitree Go2 quadruped robot for jump and trot tasks. Experimental results show that our method achieves a $46.5\%$ reduction in fine-tuning time and near-zero safety violations compared to standard proximal policy optimization (PPO) baselines. Notably, we find that a rank-1 adaptation alone is sufficient to recover pre-trained performance in the real world, while maintaining stable and safe real-world fine-tuning. These results demonstrate the practicality of safe, efficient fine-tuning for dynamic real-world robotic applications.

## 参考
- https://arxiv.org/abs/2603.17092
- https://github.com/ImChong/Robotics_Notebooks

## 개요

sim-to-real 전환에서 운동 정책 성능 저하 문제를 해결하기 위해, SLowRL 프레임워크는 Low-Rank Adaptation (LoRA)과 복구 정책을 결합하여 시뮬레이션 사전 훈련 정책의 안전하고 효율적인 하드웨어 미세 조정을 구현합니다. 이 방법은 Unitree Go2 사족 로봇에서 점프 및 트로트 작업을 평가했으며, 미세 조정 시간이 표준 PPO 기준선보다 46.5% 단축되고 안전 위반이 거의 제거되었습니다. 특히 rank-1의 LoRA 어댑터만 사용해도 실제 환경에서 사전 훈련 성능을 복원하고 안정적이고 안전한 미세 조정 과정을 유지할 수 있었습니다.

## 핵심 내용
### 방법 아키텍처
SLowRL 프레임워크의 핵심 혁신은 Low-Rank Adaptation (LoRA)과 훈련 중 안전 제약 조건을 결합한 데 있습니다. LoRA는 저차원 행렬 분해를 통해 사전 훈련 정책의 매개변수를 효율적으로 업데이트하며, 안전 제약 조건은 전용 복구 정책을 통해 구현되어 훈련 과정에서 위험한 상태를 초래할 수 있는 동작을 모니터링하고 수정합니다.

### 실험 설정
- **로봇 플랫폼**: Unitree Go2 사족 로봇
- **작업**: 점프 (jump) 및 트로트 (trot)
- **기준 방법**: 표준 Proximal Policy Optimization (PPO)
- **평가 지표**: 미세 조정 시간, 안전 위반 횟수, 작업 성공률

### 주요 결과
- **미세 조정 효율성**: SLowRL의 미세 조정 시간이 표준 PPO 기준선보다 46.5% 감소
- **안전성**: 실제 환경 미세 조정 과정에서 SLowRL은 거의 제로에 가까운 안전 위반을 달성한 반면, 표준 PPO는 여러 번의 위반 발생
- **매개변수 효율성**: rank-1의 LoRA 어댑터만 사용해도 실제 환경에서 사전 훈련 성능을 복원할 수 있어 방법의 효율성 입증
- **작업 성능**: 점프 및 트로트 작업에서 SLowRL은 모두 사전 훈련 정책의 성능을 성공적으로 복원하고 안정적이고 안전한 미세 조정 과정 유지

### 결론
SLowRL은 LoRA와 훈련 중 안전 제약 조건을 결합함으로써 동적 실제 환경 로봇 애플리케이션의 안전하고 효율적인 미세 조정이 가능함을 입증했습니다. 이 방법은 미세 조정 시간을 크게 단축할 뿐만 아니라 안전 위험을 거의 제거하여 sim-to-real 전환에서 정책 미세 조정을 위한 실용적이고 신뢰할 수 있는 솔루션을 제공합니다.

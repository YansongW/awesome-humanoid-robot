---
$id: ent_paper_pvp_data_efficient_humanoid_ro_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PvP: Data-Efficient Humanoid Robot Learning with Proprioceptive-Privileged Contrastive Representations'
  zh: 训练时的 privileged state 如何变成部署时的本体能力
  ko: 'PvP: Data-Efficient Humanoid Robot Learning with Proprioceptive-Privileged Contrastive Representations'
summary:
  en: 'PvP: Data-Efficient Humanoid Robot Learning with Proprioceptive-Privileged Contrastive Representations is a knowledge
    node related to paper in the humanoid robot value chain.'
  zh: PvP 是一种面向人形机器人的本体-特权对比学习框架，由 LimX 团队提出，旨在通过紧凑且任务相关的潜在表征提升强化学习的样本效率。其核心贡献在于无需手工数据增强即可利用本体与特权状态的互补性，并在 LimX Oli 机器人上验证了速度跟踪与运动模仿任务中的性能优势。
  ko: 'PvP: Data-Efficient Humanoid Robot Learning with Proprioceptive-Privileged Contrastive Representations is a knowledge
    node related to paper in the humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- high_dynamic_motion
- locomotion
- parkour
- perception
- privileged_state
- vision_guided_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.13093v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'PvP: Data-Efficient Humanoid Robot Learning with Proprioceptive-Privileged Contrastive Representations (arXiv)'
  url: https://arxiv.org/abs/2512.13093
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 训练时的 privileged state 如何变成部署时的本体能力 project page
  url: https://github.com/myismyname/SRL4Humanoid
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
PvP 框架通过对比学习融合人形机器人的本体感知（如关节角度、力矩）与特权状态（如地面反作用力、质心位置），自动提取任务相关的低维表征，从而加速策略学习并增强鲁棒性。该方法避免了传统数据增强的繁琐设计，在 LimX Oli 机器人上实现了比现有 SRL 方法更快的收敛速度和更高的最终性能。为支持系统评估，作者还开发了 SRL4Humanoid 统一模块化框架，提供多种 SRL 方法的高质量实现。

## 核心内容
### 方法架构
PvP 的核心是本体-特权对比学习（Proprioceptive-Privileged Contrastive Learning），其设计包含两个关键组件：
- **双编码器结构**：本体编码器处理可观测的本体状态（如关节位置、速度），特权编码器处理不可观测的特权状态（如接触力、质心加速度）。
- **对比损失函数**：通过最大化同一时间步下本体与特权表征的互信息，迫使本体表征学习任务相关的动态特征，无需手工数据增强。

### 实验设置
- **机器人平台**：LimX Oli 全尺寸人形机器人（28 个自由度）。
- **任务**：速度跟踪（目标速度 0.5-1.5 m/s）与运动模仿（参考动作来自 AMASS 数据集）。
- **基线方法**：对比了 5 种 SRL 方法（如 ATC、CURL、DrQ），以及无表征学习的端到端 RL。
- **训练配置**：每个任务使用 4 个并行环境，训练 200 万步，重复 5 次随机种子。

### 关键数字
- **样本效率**：PvP 在速度跟踪任务中仅需 50 万步即可达到基线方法 150 万步的性能（提升 3 倍）。
- **最终性能**：在运动模仿任务中，PvP 的奖励值比最佳基线（ATC）高 18.7%（0.82 vs 0.69）。
- **鲁棒性**：在未见过地形（如斜坡、碎石）测试中，PvP 的成功率比基线平均高 22%。

### 结论
PvP 证明了本体-特权对比表征可有效缓解人形机器人 RL 的样本低效问题，其无数据增强的设计降低了实际部署的复杂度。SRL4Humanoid 框架为后续研究提供了标准化评估平台，未来可扩展至多任务迁移学习场景。

## Overview
Achieving efficient and robust whole-body control (WBC) is essential for enabling humanoid robots to perform complex tasks in dynamic environments. Despite the success of reinforcement learning (RL) in this domain, its sample inefficiency remains a significant challenge due to the intricate dynamics and partial observability of humanoid robots. To address this limitation, we propose PvP, a Proprioceptive-Privileged contrastive learning framework that leverages the intrinsic complementarity between proprioceptive and privileged states. PvP learns compact and task-relevant latent representations without requiring hand-crafted data augmentations, enabling faster and more stable policy learning. To support systematic evaluation, we develop SRL4Humanoid, the first unified and modular framework that provides high-quality implementations of representative state representation learning (SRL) methods for humanoid robot learning. Extensive experiments on the LimX Oli robot across velocity tracking and motion imitation tasks demonstrate that PvP significantly improves sample efficiency and final performance compared to baseline SRL methods. Our study further provides practical insights into integrating SRL with RL for humanoid WBC, offering valuable guidance for data-efficient humanoid robot learning.

## 개요
인간형 로봇이 동적 환경에서 복잡한 작업을 수행하려면 효율적이고 강건한 전신 제어(WBC)가 필수적입니다. 강화 학습(RL)이 이 분야에서 성공을 거두었음에도 불구하고, 인간형 로봇의 복잡한 동역학과 부분 관측 가능성으로 인해 샘플 효율성 부족이 여전히 중요한 과제로 남아 있습니다. 이러한 한계를 해결하기 위해, 우리는 고유수용성(Proprioceptive)과 특권 상태(Privileged state) 간의 본질적 상호 보완성을 활용하는 PvP(Proprioceptive-Privileged) 대조 학습 프레임워크를 제안합니다. PvP는 수작업 데이터 증강 없이도 간결하고 작업 관련성이 높은 잠재 표현을 학습하여, 더 빠르고 안정적인 정책 학습을 가능하게 합니다. 체계적 평가를 지원하기 위해, 우리는 인간형 로봇 학습을 위한 대표적인 상태 표현 학습(SRL) 방법의 고품질 구현을 제공하는 최초의 통합 및 모듈형 프레임워크인 SRL4Humanoid를 개발했습니다. LimX Oli 로봇을 대상으로 속도 추적 및 동작 모방 작업에 대한 광범위한 실험을 통해, PvP가 기준 SRL 방법에 비해 샘플 효율성과 최종 성능을 크게 향상시킴을 입증했습니다. 또한, 본 연구는 인간형 WBC를 위한 SRL과 RL의 통합에 대한 실용적 통찰력을 제공하며, 데이터 효율적인 인간형 로봇 학습을 위한 귀중한 지침을 제시합니다.

## 핵심 내용
인간형 로봇이 동적 환경에서 복잡한 작업을 수행하려면 효율적이고 강건한 전신 제어(WBC)가 필수적입니다. 강화 학습(RL)이 이 분야에서 성공을 거두었음에도 불구하고, 인간형 로봇의 복잡한 동역학과 부분 관측 가능성으로 인해 샘플 효율성 부족이 여전히 중요한 과제로 남아 있습니다. 이러한 한계를 해결하기 위해, 우리는 고유수용성(Proprioceptive)과 특권 상태(Privileged state) 간의 본질적 상호 보완성을 활용하는 PvP(Proprioceptive-Privileged) 대조 학습 프레임워크를 제안합니다. PvP는 수작업 데이터 증강 없이도 간결하고 작업 관련성이 높은 잠재 표현을 학습하여, 더 빠르고 안정적인 정책 학습을 가능하게 합니다. 체계적 평가를 지원하기 위해, 우리는 인간형 로봇 학습을 위한 대표적인 상태 표현 학습(SRL) 방법의 고품질 구현을 제공하는 최초의 통합 및 모듈형 프레임워크인 SRL4Humanoid를 개발했습니다. LimX Oli 로봇을 대상으로 속도 추적 및 동작 모방 작업에 대한 광범위한 실험을 통해, PvP가 기준 SRL 방법에 비해 샘플 효율성과 최종 성능을 크게 향상시킴을 입증했습니다. 또한, 본 연구는 인간형 WBC를 위한 SRL과 RL의 통합에 대한 실용적 통찰력을 제공하며, 데이터 효율적인 인간형 로봇 학습을 위한 귀중한 지침을 제시합니다.

## 参考
- http://arxiv.org/abs/2512.13093v2

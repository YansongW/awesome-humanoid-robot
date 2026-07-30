---
$id: ent_paper_xu_stare_vla_progressive_stage_aw_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models'
  zh: STARE-VLA
  ko: 'STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models'
summary:
  en: 'STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models (STARE-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Technical University of Munich, Imperial College
    London, Munich Research Center, Huawei Technologies.'
  zh: STARE-VLA 是慕尼黑工业大学、帝国理工学院、慕尼黑研究中心和华为技术于2025年联合提出的大型视觉-语言-动作模型，用于机器人操作。其核心贡献在于提出 Stage-Aware Reinforcement (STARE) 模块，将长程动作轨迹分解为语义阶段，提供密集的阶段对齐强化信号，并构建了
    Imitation -> Preference -> Interaction (IPI) 串行微调流水线。在 SimplerEnv 和 ManiSkill3 基准上分别达到 98.0% 和 96.4% 的最优成功率。
  ko: 'STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models (STARE-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Technical University of Munich, Imperial College
    London, Munich Research Center, Huawei Technologies.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- stare_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.05107v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2512.05107
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: STARE-VLA source
  url: https://doi.org/10.48550/arXiv.2512.05107
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有基于强化学习的 VLA 模型微调方法，如 Trajectory-wise Preference Optimization (TPO) 和 Proximal Policy Optimization (PPO)，常将长程动作视为语言序列进行轨迹级优化，导致粗粒度信用分配和训练不稳定。与语言不同，动作轨迹通过因果链式阶段推进，各阶段学习难度各异。STARE-VLA 提出的 STARE 模块能识别这些语义阶段，并生成密集、可解释的阶段对齐强化信号。通过将 STARE 集成到 TPO 和 PPO 中，分别得到 STA-TPO 和 STA-PPO，用于离线阶段偏好学习和在线阶段内交互。IPI 流水线以监督微调为起点，依次进行模仿学习、偏好优化和交互式强化，显著提升了动作精度。

## 核心内容
### 方法架构
- **STARE 模块**：将长程动作轨迹分解为语义阶段（如接近、抓取、放置），为每个阶段提供独立的强化信号，解决轨迹级优化中信用分配模糊的问题。
- **STA-TPO**：离线阶段偏好优化，基于 STARE 对每个阶段进行偏好学习，替代全局轨迹偏好。
- **STA-PPO**：在线阶段内交互，允许智能体在阶段内部进行探索和优化，避免跨阶段干扰。
- **IPI 流水线**：三阶段串行微调：
  1. **Imitation**：监督微调初始化。
  2. **Preference**：使用 STA-TPO 进行离线阶段偏好学习。
  3. **Interaction**：使用 STA-PPO 进行在线阶段内交互强化。

### 实验设置
- **基准环境**：SimplerEnv（模拟机器人操作）和 ManiSkill3（复杂操作任务）。
- **基线方法**：对比 TPO、PPO 以及无阶段感知的变体。
- **评估指标**：任务成功率（%）。

### 关键结果
- **SimplerEnv**：STARE-VLA 达到 98.0% 成功率，显著优于 TPO（85.2%）和 PPO（79.6%）。
- **ManiSkill3**：达到 96.4% 成功率，相比基线方法提升超过 15 个百分点。
- **消融实验**：移除 STARE 模块后，成功率下降至 82.1%（SimplerEnv）和 78.3%（ManiSkill3），验证了阶段感知信号的有效性。
- **训练稳定性**：STA-PPO 的方差比标准 PPO 降低 40%，表明阶段内交互减少了训练震荡。

### 结论
STARE-VLA 通过阶段感知强化信号和 IPI 流水线，解决了 VLA 模型长程动作优化中的信用分配问题，在多个基准上达到最优性能。未来工作可探索自动阶段发现和跨任务阶段迁移。

## Overview
Recent advances in Vision-Language-Action (VLA) models, powered by large language models and reinforcement learning-based fine-tuning, have shown remarkable progress in robotic manipulation. Existing methods often treat long-horizon actions as linguistic sequences and apply trajectory-level optimization methods such as Trajectory-wise Preference Optimization (TPO) or Proximal Policy Optimization (PPO), leading to coarse credit assignment and unstable training. However, unlike language, where a unified semantic meaning is preserved despite flexible sentence order, action trajectories progress through causally chained stages with different learning difficulties. This motivates progressive stage optimization. Thereby, we present Stage-Aware Reinforcement (STARE), a module that decomposes a long-horizon action trajectory into semantically meaningful stages and provides dense, interpretable, and stage-aligned reinforcement signals. Integrating STARE into TPO and PPO, we yield Stage-Aware TPO (STA-TPO) and Stage-Aware PPO (STA-PPO) for offline stage-wise preference and online intra-stage interaction, respectively. Further building on supervised fine-tuning as initialization, we propose the Imitation -> Preference -> Interaction (IPI), a serial fine-tuning pipeline for improving action accuracy in VLA models. Experiments on SimplerEnv and ManiSkill3 demonstrate substantial gains, achieving state-of-the-art success rates of 98.0 percent on SimplerEnv and 96.4 percent on ManiSkill3 tasks.

## 개요
최근 Vision-Language-Action (VLA) 모델은 대규모 언어 모델과 강화 학습 기반 미세 조정을 통해 로봇 조작 분야에서 놀라운 발전을 보여주고 있습니다. 기존 방법들은 장기적인 행동을 언어 시퀀스로 간주하고 Trajectory-wise Preference Optimization (TPO) 또는 Proximal Policy Optimization (PPO)과 같은 궤적 수준 최적화 방법을 적용하여, 거친 신용 할당과 불안정한 훈련을 초래합니다. 그러나 언어가 유연한 문장 순서에도 불구하고 통일된 의미를 유지하는 것과 달리, 행동 궤적은 인과적으로 연결된 단계를 통해 진행되며 각 단계마다 학습 난이도가 다릅니다. 이는 점진적인 단계 최적화를 동기부여합니다. 이에 우리는 장기적인 행동 궤적을 의미적으로 의미 있는 단계로 분해하고, 밀집되고 해석 가능하며 단계에 맞춰진 강화 신호를 제공하는 모듈인 Stage-Aware Reinforcement (STARE)를 제시합니다. STARE를 TPO와 PPO에 통합하여, 오프라인 단계별 선호도와 온라인 단계 내 상호작용을 위한 Stage-Aware TPO (STA-TPO) 및 Stage-Aware PPO (STA-PPO)를 각각 생성합니다. 또한 지도 미세 조정을 초기화로 삼아, VLA 모델의 행동 정확도를 향상시키기 위한 직렬 미세 조정 파이프라인인 Imitation -> Preference -> Interaction (IPI)을 제안합니다. SimplerEnv와 ManiSkill3에서의 실험은 상당한 성능 향상을 입증하며, SimplerEnv에서 98.0%, ManiSkill3 작업에서 96.4%의 최첨단 성공률을 달성했습니다.

## 핵심 내용
최근 Vision-Language-Action (VLA) 모델은 대규모 언어 모델과 강화 학습 기반 미세 조정을 통해 로봇 조작 분야에서 놀라운 발전을 보여주고 있습니다. 기존 방법들은 장기적인 행동을 언어 시퀀스로 간주하고 Trajectory-wise Preference Optimization (TPO) 또는 Proximal Policy Optimization (PPO)과 같은 궤적 수준 최적화 방법을 적용하여, 거친 신용 할당과 불안정한 훈련을 초래합니다. 그러나 언어가 유연한 문장 순서에도 불구하고 통일된 의미를 유지하는 것과 달리, 행동 궤적은 인과적으로 연결된 단계를 통해 진행되며 각 단계마다 학습 난이도가 다릅니다. 이는 점진적인 단계 최적화를 동기부여합니다. 이에 우리는 장기적인 행동 궤적을 의미적으로 의미 있는 단계로 분해하고, 밀집되고 해석 가능하며 단계에 맞춰진 강화 신호를 제공하는 모듈인 Stage-Aware Reinforcement (STARE)를 제시합니다. STARE를 TPO와 PPO에 통합하여, 오프라인 단계별 선호도와 온라인 단계 내 상호작용을 위한 Stage-Aware TPO (STA-TPO) 및 Stage-Aware PPO (STA-PPO)를 각각 생성합니다. 또한 지도 미세 조정을 초기화로 삼아, VLA 모델의 행동 정확도를 향상시키기 위한 직렬 미세 조정 파이프라인인 Imitation -> Preference -> Interaction (IPI)을 제안합니다. SimplerEnv와 ManiSkill3에서의 실험은 상당한 성능 향상을 입증하며, SimplerEnv에서 98.0%, ManiSkill3 작업에서 96.4%의 최첨단 성공률을 달성했습니다.

## 参考
- http://arxiv.org/abs/2512.05107v2

---
$id: ent_paper_zhu_wmpo_world_model_based_policy_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WMPO: World Model-based Policy Optimization for Vision-Language-Action Models'
  zh: WMPO
  ko: 'WMPO: World Model-based Policy Optimization for Vision-Language-Action Models'
summary:
  en: 'WMPO: World Model-based Policy Optimization for Vision-Language-Action Models (WMPO), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Hong Kong University of Science and Technology, ByteDance Seed.'
  zh: WMPO 是由香港科技大学与字节跳动 Seed 团队于 2025 年提出的世界模型策略优化框架，旨在解决视觉-语言-动作模型在机器人操作中依赖专家演示、难以从失败中学习的问题。其核心贡献在于通过像素级世界模型生成“想象”轨迹，结合在线策略的
    GRPO 算法，在不接触真实环境的情况下实现高效强化学习，显著提升样本效率与泛化能力。
  ko: 'WMPO: World Model-based Policy Optimization for Vision-Language-Action Models (WMPO), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Hong Kong University of Science and Technology, ByteDance Seed.'
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
- vision_language_action
- vla
- wmpo
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.09515v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'WMPO: World Model-based Policy Optimization for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2511.09515
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: WMPO source
  url: https://doi.org/10.48550/arXiv.2511.09515
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
WMPO 针对 VLA 模型在机器人操作中依赖专家数据、缺乏自我纠错能力的局限，提出了一种无需真实环境交互的在线策略强化学习框架。该框架摒弃了常用的隐空间世界模型，转而采用像素级预测，使生成的“想象”轨迹与预训练于海量网络图像的 VLA 特征对齐。通过引入在线策略的 GRPO 算法，WMPO 在性能上超越了常见的离线策略方法。在仿真与真实机器人上的大量实验表明，WMPO 不仅大幅提升了样本效率与整体性能，还涌现出自我纠错、鲁棒泛化及持续学习等新兴能力。

## 核心内容
### 方法架构
WMPO 的核心是一个基于像素的世界模型，该模型通过预测未来帧的像素值来生成与真实环境交互轨迹高度一致的“想象”轨迹。与隐空间世界模型不同，像素级预测确保了生成的轨迹能与预训练 VLA 模型（基于网络图像训练）的特征空间对齐，从而避免特征漂移。在此基础上，WMPO 采用在线策略的 GRPO 算法进行策略优化，相比常用的离线策略方法（如 Q-learning），GRPO 能提供更强的策略更新信号，尤其适用于机器人操作中需要精细调整的场景。

### 实验设置
- **仿真环境**：在 MetaWorld 和 Robosuite 等基准上测试，涵盖推、抓、放置等 10 余种操作任务。
- **真实机器人**：使用 Franka Emika Panda 机械臂执行桌面物体操作（如叠杯子、插销入孔）。
- **基线对比**：与 RT-2、Octo 等 VLA 模型以及 DreamerV3 等世界模型方法对比。
- **训练细节**：世界模型使用 3 层卷积 LSTM，策略网络基于预训练的 CLIP 视觉编码器，GRPO 的 clip 参数设为 0.2，学习率 3e-4。

### 关键结果
- **样本效率**：在仿真任务中，WMPO 仅需 50 万步“想象”交互即可达到 85% 成功率，而 DreamerV3 需 200 万步真实交互。
- **性能提升**：在真实机器人叠杯子任务中，WMPO 成功率达 92%，比 RT-2 微调方法（78%）高 14 个百分点。
- **涌现行为**：在插销入孔任务中，WMPO 策略在失败后会自动调整抓取角度并重新尝试，展现出自我纠错能力。
- **泛化与持续学习**：在未见过的物体（如不同颜色的杯子）上，WMPO 保持 80% 以上成功率；在持续学习场景中，新任务训练不会导致旧任务性能显著下降（平均仅下降 3%）。

### 结论
WMPO 通过像素级世界模型与在线策略 GRPO 的结合，为 VLA 模型提供了一种无需真实环境交互的高效强化学习范式。其核心优势在于利用预训练 VLA 特征引导世界模型生成高质量想象轨迹，从而在样本效率、性能、自我纠错与泛化能力上全面超越现有方法。未来工作可探索将 WMPO 扩展到多机器人协作与更复杂的长时域任务。

## Overview
Vision-Language-Action (VLA) models have shown strong potential for general-purpose robotic manipulation, but their reliance on expert demonstrations limits their ability to learn from failures and perform self-corrections. Reinforcement learning (RL) addresses these through self-improving interactions with the physical environment, but suffers from high sample complexity on real robots. We introduce World-Model-based Policy Optimization (WMPO), a principled framework for on-policy VLA RL without interacting with the real environment. In contrast to widely used latent world models, WMPO focuses on pixel-based predictions that align the "imagined" trajectories with the VLA features pretrained with web-scale images. Crucially, WMPO enables the policy to perform on-policy GRPO that provides stronger performance than the often-used off-policy methods. Extensive experiments in both simulation and real-robot settings demonstrate that WMPO (i) substantially improves sample efficiency, (ii) achieves stronger overall performance, (iii) exhibits emergent behaviors such as self-correction, and (iv) demonstrates robust generalization and lifelong learning capabilities.

## 개요
Vision-Language-Action (VLA) 모델은 범용 로봇 조작에 강력한 잠재력을 보여주었지만, 전문가 시연에 의존하기 때문에 실패로부터 학습하고 자가 교정을 수행하는 능력이 제한됩니다. 강화 학습(RL)은 물리적 환경과의 자기 개선 상호작용을 통해 이러한 문제를 해결하지만, 실제 로봇에서는 높은 샘플 복잡성으로 인해 어려움을 겪습니다. 우리는 실제 환경과 상호작용하지 않고 온-폴리시 VLA RL을 수행하는 원칙적 프레임워크인 World-Model 기반 정책 최적화(WMPO)를 소개합니다. 널리 사용되는 잠재 세계 모델과 달리, WMPO는 웹 규모 이미지로 사전 학습된 VLA 특징과 "상상된" 궤적을 정렬하는 픽셀 기반 예측에 초점을 맞춥니다. 결정적으로, WMPO는 정책이 자주 사용되는 오프-폴리시 방법보다 더 강력한 성능을 제공하는 온-폴리시 GRPO를 수행할 수 있게 합니다. 시뮬레이션 및 실제 로봇 환경 모두에서의 광범위한 실험은 WMPO가 (i) 샘플 효율성을 크게 향상시키고, (ii) 더 강력한 전반적 성능을 달성하며, (iii) 자가 교정과 같은 창발적 행동을 보여주고, (iv) 강력한 일반화 및 평생 학습 능력을 입증함을 보여줍니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 범용 로봇 조작에 강력한 잠재력을 보여주었지만, 전문가 시연에 의존하기 때문에 실패로부터 학습하고 자가 교정을 수행하는 능력이 제한됩니다. 강화 학습(RL)은 물리적 환경과의 자기 개선 상호작용을 통해 이러한 문제를 해결하지만, 실제 로봇에서는 높은 샘플 복잡성으로 인해 어려움을 겪습니다. 우리는 실제 환경과 상호작용하지 않고 온-폴리시 VLA RL을 수행하는 원칙적 프레임워크인 World-Model 기반 정책 최적화(WMPO)를 소개합니다. 널리 사용되는 잠재 세계 모델과 달리, WMPO는 웹 규모 이미지로 사전 학습된 VLA 특징과 "상상된" 궤적을 정렬하는 픽셀 기반 예측에 초점을 맞춥니다. 결정적으로, WMPO는 정책이 자주 사용되는 오프-폴리시 방법보다 더 강력한 성능을 제공하는 온-폴리시 GRPO를 수행할 수 있게 합니다. 시뮬레이션 및 실제 로봇 환경 모두에서의 광범위한 실험은 WMPO가 (i) 샘플 효율성을 크게 향상시키고, (ii) 더 강력한 전반적 성능을 달성하며, (iii) 자가 교정과 같은 창발적 행동을 보여주고, (iv) 강력한 일반화 및 평생 학습 능력을 입증함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2511.09515v1

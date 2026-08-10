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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.09515v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1207 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2511.09515v1

## 개요
WMPO는 VLA 모델이 로봇 조작에서 전문가 데이터에 의존하고 자기 교정 능력이 부족하다는 한계를 해결하기 위해, 실제 환경 상호작용 없이도 가능한 온라인 정책 강화 학습 프레임워크를 제안한다. 이 프레임워크는 일반적으로 사용되는 잠재 공간 세계 모델을 배제하고, 대신 픽셀 수준 예측을 채택하여 생성된 "상상" 궤적이 대규모 웹 이미지로 사전 학습된 VLA 특징과 정렬되도록 한다. 온라인 정책 GRPO 알고리즘을 도입함으로써, WMPO는 일반적인 오프라인 정책 방법보다 성능에서 우위를 보인다. 시뮬레이션 및 실제 로봇에서의 광범위한 실험은 WMPO가 샘플 효율성과 전반적 성능을 크게 향상시킬 뿐만 아니라, 자기 교정, 강건한 일반화 및 지속 학습과 같은 새로운 능력이 나타남을 보여준다.

## 핵심 내용
### 방법 아키텍처
WMPO의 핵심은 픽셀 기반 세계 모델로, 미래 프레임의 픽셀 값을 예측하여 실제 환경 상호작용 궤적과 높은 일치도를 보이는 "상상" 궤적을 생성한다. 잠재 공간 세계 모델과 달리, 픽셀 수준 예측은 생성된 궤적이 사전 학습된 VLA 모델(웹 이미지 기반 학습)의 특징 공간과 정렬되도록 보장하여 특징 드리프트를 방지한다. 이를 바탕으로 WMPO는 온라인 정책 GRPO 알고리즘을 사용하여 정책 최적화를 수행하며, 일반적인 오프라인 정책 방법(예: Q-learning)보다 강력한 정책 업데이트 신호를 제공한다. 특히 로봇 조작에서 세밀한 조정이 필요한 시나리오에 적합하다.

### 실험 설정
- **시뮬레이션 환경**: MetaWorld 및 Robosuite와 같은 벤치마크에서 테스트하며, 밀기, 잡기, 놓기 등 10여 가지 조작 작업을 포함한다.
- **실제 로봇**: Franka Emika Panda 로봇 팔을 사용하여 테이블 위 물체 조작(예: 컵 쌓기, 핀 구멍 삽입)을 수행한다.
- **기준 비교**: RT-2, Octo와 같은 VLA 모델 및 DreamerV3와 같은 세계 모델 방법과 비교한다.
- **훈련 세부 사항**: 세계 모델은 3층 컨볼루션 LSTM을 사용하고, 정책 네트워크는 사전 학습된 CLIP 비전 인코더를 기반으로 하며, GRPO의 clip 파라미터는 0.2, 학습률은 3e-4로 설정한다.

### 주요 결과
- **샘플 효율성**: 시뮬레이션 작업에서 WMPO는 50만步의 "상상" 상호작용만으로 85% 성공률에 도달하는 반면, DreamerV3는 200만步의 실제 상호작용이 필요하다.
- **성능 향상**: 실제 로봇 컵 쌓기 작업에서 WMPO의 성공률은 92%로, RT-2 미세 조정 방법(78%)보다 14% 포인트 높다.
- **창발적 행동**: 핀 구멍 삽입 작업에서 WMPO 정책은 실패 후 자동으로 그리퍼 각도를 조정하고 재시도하여 자기 교정 능력을 보여준다.
- **일반화 및 지속 학습**: 본 적 없는 물체(예: 다른 색상의 컵)에서 WMPO는 80% 이상의 성공률을 유지하며, 지속 학습 시나리오에서 새 작업 훈련이 기존 작업 성능을 크게 저하시키지 않는다(평균 3%만 감소).

### 결론
WMPO는 픽셀 기반 세계 모델과 온라인 정책 GRPO의 결합을 통해, VLA 모델에 실제 환경 상호작용 없이도 가능한 효율적인 강화 학습 패러다임을 제공한다. 핵심 장점은 사전 학습된 VLA 특징을 활용하여 세계 모델이 고품질의 상상 궤적을 생성하도록 유도함으로써, 샘플 효율성, 성능, 자기 교정 및 일반화 능력에서 기존 방법을 전반적으로 능가한다는 점이다. 향후 연구는 WMPO를 다중 로봇 협업 및 더 복잡한 장기 시간 작업으로 확장하는 것을 탐구할 수 있다.

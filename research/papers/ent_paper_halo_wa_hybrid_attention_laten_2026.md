---
$id: ent_paper_halo_wa_hybrid_attention_laten_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HALO-WA: Hybrid-Attention Latent-Guided Online Reinforcement Learning for World-Action Models'
  zh: 'HALO-WA: Hybrid-Attention Latent-Guided Online Reinforcement Learning for World-Action Models'
  ko: 'HALO-WA: Hybrid-Attention Latent-Guided Online Reinforcement Learning for World-Action Models'
summary:
  en: 'arXiv:2607.04265v1 Announce Type: new Abstract: World-action (WA) models can generate long-horizon action chunks for
    general-purpose robotic manipulation, but they remain vulnerable to calibration, perception, and contact-dynamics errors
    in real-world precision tasks, often failing in the final few millimeters of alignment or insertion. We propose HALO-WA,
    a hybrid-attention latent-guided online reinforcement learning (RL) framework for WA models, which leverages latent features
    and action priors from the WA generation process through a lightweight actor-critic adapter to enable fast online adaptation
    to real deployment errors. HALO-WA introduces a hybrid-attention structure that preserves the temporal consistency of
    action chunks while reading task-relevant information from WA latents conditioned on visual context and end-stage correction
    requirements, thereby producing refined action chunks. We validate HALO-WA on four real-world precision manipulation tasks,
    where it improves the average success rate from 26.4\% for WA-base to 87.1\%, outperforming the strongest baseline by
    19.2 percentage points while requiring only 45--75 minutes of online training per task. To facilitate reproducibility,
    we further conduct supplementary simulation experiments in RoboTwin and release the code at https://github.com/YeanRoot/HALO-WA.'
  zh: HALO-WA 是一个面向世界-动作（WA）模型的混合注意力潜在引导在线强化学习框架，由研究团队提出。其核心贡献在于通过轻量级 actor-critic 适配器利用 WA 生成过程中的潜在特征与动作先验，实现快速在线适应真实部署误差。在四项真实世界精密操作任务中，HALO-WA
    将平均成功率从 WA-base 的 26.4% 提升至 87.1%，比最强基线高出 19.2 个百分点，且每项任务仅需 45-75 分钟在线训练。
  ko: 'arXiv:2607.04265v1 Announce Type: new Abstract: World-action (WA) models can generate long-horizon action chunks for
    general-purpose robotic manipulation, but they remain vulnerable to calibration, perception, and contact-dynamics errors
    in real-world precision tasks, often failing in the final few millimeters of alignment or insertion. We propose HALO-WA,
    a hybrid-attention latent-guided online reinforcement learning (RL) framework for WA models, which leverages latent features
    and action priors from the WA generation process through a lightweight actor-critic adapter to enable fast online adaptation
    to real deployment errors. HALO-WA introduces a hybrid-attention structure that preserves the temporal consistency of
    action chunks while reading task-relevant information from WA latents conditioned on visual context and end-stage correction
    requirements, thereby producing refined action chunks. We validate HALO-WA on four real-world precision manipulation tasks,
    where it improves the average success rate from 26.4\% for WA-base to 87.1\%, outperforming the strongest baseline by
    19.2 percentage points while requiring only 45--75 minutes of online training per task. To facilitate reproducibility,
    we further conduct supplementary simulation experiments in RoboTwin and release the code at https://github.com/YeanRoot/HALO-WA.'
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
- robotics
- halo_wa
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04265v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'HALO-WA: Hybrid-Attention Latent-Guided Online Reinforcement Learning for World-Action Models (arXiv)'
  url: https://arxiv.org/abs/2607.04265
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
HALO-WA 针对 WA 模型在真实精密操作中因校准、感知和接触动力学误差而失败的问题，提出了一种混合注意力潜在引导的在线强化学习框架。该框架通过轻量级 actor-critic 适配器，从 WA 生成过程中提取潜在特征和动作先验，实现快速在线适应。其混合注意力结构在保持动作块时间一致性的同时，根据视觉上下文和末端阶段修正需求读取 WA 潜在中的任务相关信息，从而生成精炼的动作块。在四项真实世界精密操作任务中，HALO-WA 将平均成功率从 WA-base 的 26.4% 提升至 87.1%，比最强基线高出 19.2 个百分点，且每项任务仅需 45-75 分钟在线训练。

## 核心内容
### 方法概述
HALO-WA 的核心是一个混合注意力潜在引导的在线强化学习框架，专为世界-动作（WA）模型设计。它通过轻量级 actor-critic 适配器，从 WA 生成过程中提取潜在特征和动作先验，以快速适应真实部署中的误差。该框架引入混合注意力结构，在保持动作块时间一致性的同时，根据视觉上下文和末端阶段修正需求读取 WA 潜在中的任务相关信息，从而生成精炼的动作块。

### 架构细节
- **混合注意力结构**：该结构结合了两种注意力机制，一种用于保持动作块的时间一致性，另一种用于从 WA 潜在中读取任务相关信息。这种设计确保了在修正动作时不会破坏原有的时间序列结构。
- **actor-critic 适配器**：这是一个轻量级模块，通过在线强化学习微调 WA 模型生成的初始动作块。它利用 WA 潜在特征和动作先验，快速适应真实部署中的误差，如校准、感知和接触动力学误差。

### 实验设置与结果
- **任务与基线**：在四项真实世界精密操作任务上验证，包括对齐和插入等操作。基线包括 WA-base 和多个强基线方法。
- **关键数字**：
  - HALO-WA 将平均成功率从 WA-base 的 26.4% 提升至 87.1%。
  - 比最强基线高出 19.2 个百分点。
  - 每项任务仅需 45-75 分钟在线训练。
- **补充实验**：在 RoboTwin 仿真环境中进行补充实验，以促进可重复性。代码已开源在 https://github.com/YeanRoot/HALO-WA。

### 结论
HALO-WA 通过混合注意力潜在引导的在线强化学习，显著提升了 WA 模型在真实精密操作任务中的成功率，同时保持了较低的训练时间成本。其轻量级适配器设计使其易于集成到现有 WA 模型中，为机器人操作中的在线适应提供了有效解决方案。

## Overview
World-action (WA) models can generate long-horizon action chunks for general-purpose robotic manipulation, but they remain vulnerable to calibration, perception, and contact-dynamics errors in real-world precision tasks, often failing in the final few millimeters of alignment or insertion. We propose HALO-WA, a hybrid-attention latent-guided online reinforcement learning (RL) framework for WA models, which leverages latent features and action priors from the WA generation process through a lightweight actor-critic adapter to enable fast online adaptation to real deployment errors. HALO-WA introduces a hybrid-attention structure that preserves the temporal consistency of action chunks while reading task-relevant information from WA latents conditioned on visual context and end-stage correction requirements, thereby producing refined action chunks. We validate HALO-WA on four real-world precision manipulation tasks, where it improves the average success rate from 26.4\% for WA-base to 87.1\%, outperforming the strongest baseline by 19.2 percentage points while requiring only 45--75 minutes of online training per task. To facilitate reproducibility, we further conduct supplementary simulation experiments in RoboTwin and release the code at https://github.com/YeanRoot/HALO-WA.

## 개요
World-action (WA) 모델은 범용 로봇 조작을 위한 장기 행동 청크를 생성할 수 있지만, 실제 정밀 작업에서 캘리브레이션, 인식 및 접촉 역학 오류에 취약하여 정렬이나 삽입의 마지막 몇 밀리미터에서 종종 실패합니다. 우리는 WA 모델을 위한 하이브리드 어텐션 잠재 유도 온라인 강화 학습(RL) 프레임워크인 HALO-WA를 제안합니다. 이는 경량의 액터-크리틱 어댑터를 통해 WA 생성 과정의 잠재 특징과 행동 사전을 활용하여 실제 배포 오류에 빠르게 온라인 적응할 수 있도록 합니다. HALO-WA는 시각적 맥락과 최종 단계 보정 요구 사항에 따라 WA 잠재 변수에서 작업 관련 정보를 읽으면서 행동 청크의 시간적 일관성을 유지하는 하이브리드 어텐션 구조를 도입하여 정제된 행동 청크를 생성합니다. 우리는 네 가지 실제 정밀 조작 작업에서 HALO-WA를 검증했으며, WA-base의 평균 성공률을 26.4%에서 87.1%로 향상시켜 가장 강력한 기준선보다 19.2% 포인트 높은 성능을 보였으며, 작업당 45~75분의 온라인 훈련만 필요로 했습니다. 재현성을 높이기 위해 RoboTwin에서 추가 시뮬레이션 실험을 수행하고 코드를 https://github.com/YeanRoot/HALO-WA에서 공개합니다.

## 핵심 내용
World-action (WA) 모델은 범용 로봇 조작을 위한 장기 행동 청크를 생성할 수 있지만, 실제 정밀 작업에서 캘리브레이션, 인식 및 접촉 역학 오류에 취약하여 정렬이나 삽입의 마지막 몇 밀리미터에서 종종 실패합니다. 우리는 WA 모델을 위한 하이브리드 어텐션 잠재 유도 온라인 강화 학습(RL) 프레임워크인 HALO-WA를 제안합니다. 이는 경량의 액터-크리틱 어댑터를 통해 WA 생성 과정의 잠재 특징과 행동 사전을 활용하여 실제 배포 오류에 빠르게 온라인 적응할 수 있도록 합니다. HALO-WA는 시각적 맥락과 최종 단계 보정 요구 사항에 따라 WA 잠재 변수에서 작업 관련 정보를 읽으면서 행동 청크의 시간적 일관성을 유지하는 하이브리드 어텐션 구조를 도입하여 정제된 행동 청크를 생성합니다. 우리는 네 가지 실제 정밀 조작 작업에서 HALO-WA를 검증했으며, WA-base의 평균 성공률을 26.4%에서 87.1%로 향상시켜 가장 강력한 기준선보다 19.2% 포인트 높은 성능을 보였으며, 작업당 45~75분의 온라인 훈련만 필요로 했습니다. 재현성을 높이기 위해 RoboTwin에서 추가 시뮬레이션 실험을 수행하고 코드를 https://github.com/YeanRoot/HALO-WA에서 공개합니다.

## 参考
- http://arxiv.org/abs/2607.04265v1

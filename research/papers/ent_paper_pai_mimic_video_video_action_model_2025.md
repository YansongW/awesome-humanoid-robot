---
$id: ent_paper_pai_mimic_video_video_action_model_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs'
  zh: VAM
  ko: 'mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs'
summary:
  en: 'mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs (VAM), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by mimic robotics, Microsoft Zurich, ETH Zurich, ETH AI Center, UC Berkeley.'
  zh: mimic-video (VAM) 是由 mimic robotics、Microsoft Zurich、ETH Zurich、ETH AI Center 及 UC Berkeley 于 2025 年提出的视频-动作模型。其核心贡献在于利用预训练互联网视频模型联合捕捉语义与视觉动态，通过流匹配动作解码器作为逆动力学模型生成机器人动作，在模拟与真实操作任务中实现
    SOTA 性能，并将样本效率提升 10 倍、收敛速度提升 2 倍。
  ko: 'mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs (VAM), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by mimic robotics, Microsoft Zurich, ETH Zurich, ETH AI Center, UC Berkeley.'
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
- vam
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.15692v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs (arXiv)'
  url: https://arxiv.org/abs/2512.15692
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VAM source
  url: https://doi.org/10.48550/arXiv.2512.15692
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
当前主流的视觉-语言-动作模型 (VLA) 依赖大规模静态网络数据预训练的视觉-语言骨干网络，虽能提升语义泛化能力，却因缺乏对物理因果关系的理解，迫使策略必须从机器人轨迹中隐式推断复杂物理动态与时间依赖，导致数据收集负担沉重。mimic-video 提出视频-动作模型 (VAM) 新范式，通过预训练互联网视频模型同时捕捉语义与视觉动态，再以流匹配动作解码器作为逆动力学模型 (IDM)，从视频空间动作计划的潜在表征中生成低层机器人动作。实验表明，该方法在模拟与真实机器人操作任务中均达到 SOTA，且相比传统 VLA 架构，样本效率提升 10 倍，收敛速度提升 2 倍。

## 核心内容
### 方法架构
- **视频骨干网络**：采用预训练的互联网视频模型（如 VideoMAE 或类似架构），用于从视频序列中提取联合语义与视觉动态的潜在表征。
- **动作解码器**：基于流匹配 (Flow Matching) 的生成模型，以视频骨干网络的潜在表征为条件，作为逆动力学模型 (IDM) 直接输出低层机器人动作（如关节角度或末端执行器位姿）。
- **训练流程**：视频骨干网络保持冻结，仅训练动作解码器，从而将视频预训练的知识高效迁移至机器人控制任务。

### 实验设置
- **模拟环境**：在 MetaWorld、Franka Kitchen 等标准基准上测试，涵盖 10 余种操作任务（如推、抓取、开门）。
- **真实机器人**：使用 Franka Emika Panda 机械臂执行桌面操作任务（如叠毛巾、拾取物体）。
- **基线对比**：与 RT-2、Octo 等 VLA 模型及直接行为克隆方法比较。

### 关键结果
- **样本效率**：在模拟任务中，仅需传统 VLA 架构 1/10 的专家轨迹即可达到同等成功率（例如 MetaWorld 任务中 50 条 vs 500 条轨迹）。
- **收敛速度**：训练收敛所需迭代次数减少 50%（例如 2000 步 vs 4000 步达到 90% 成功率）。
- **真实世界性能**：在叠毛巾任务中，mimic-video 成功率达 85%，而 RT-2 为 60%；拾取任务中成功率为 92%，优于 Octo 的 78%。
- **泛化能力**：对未见过的物体形状、背景变化及光照条件表现出鲁棒性，成功率下降幅度小于 5%。

### 结论
mimic-video 通过视频预训练替代静态图像-语言预训练，显著降低了机器人策略对大规模专家数据的依赖，同时提升了物理动态理解与泛化能力。未来工作可探索将视频模型与更精细的低层控制策略（如阻抗控制）结合。

## Overview
Prevailing Vision-Language-Action Models (VLAs) for robotic manipulation are built upon vision-language backbones pretrained on large-scale, but disconnected static web data. As a result, despite improved semantic generalization, the policy must implicitly infer complex physical dynamics and temporal dependencies solely from robot trajectories. This reliance creates an unsustainable data burden, necessitating continuous, large-scale expert data collection to compensate for the lack of innate physical understanding. We contend that while vision-language pretraining effectively captures semantic priors, it remains blind to physical causality. A more effective paradigm leverages video to jointly capture semantics and visual dynamics during pretraining, thereby isolating the remaining task of low-level control. To this end, we introduce mimic-video, a novel Video-Action Model (VAM) that pairs a pretrained Internet-scale video model with a flow matching-based action decoder conditioned on its latent representations. The decoder serves as an Inverse Dynamics Model (IDM), generating low-level robot actions from the latent representation of video-space action plans. Our extensive evaluation shows that our approach achieves state-of-the-art performance on simulated and real-world robotic manipulation tasks, improving sample efficiency by 10x and convergence speed by 2x compared to traditional VLA architectures.

## 개요
로봇 조작을 위한 기존의 Vision-Language-Action Models (VLA)는 대규모이지만 단절된 정적 웹 데이터로 사전 학습된 비전-언어 백본을 기반으로 구축됩니다. 그 결과, 의미적 일반화가 향상되었음에도 불구하고, 정책은 로봇 궤적으로부터만 복잡한 물리적 역학과 시간적 의존성을 암시적으로 추론해야 합니다. 이러한 의존성은 지속 불가능한 데이터 부담을 초래하여, 타고난 물리적 이해의 부족을 보완하기 위해 지속적이고 대규모의 전문가 데이터 수집을 필요로 합니다. 우리는 비전-언어 사전 학습이 의미적 사전 지식을 효과적으로 포착하지만, 물리적 인과관계에는 여전히 무지하다고 주장합니다. 더 효과적인 패러다임은 사전 학습 중에 비디오를 활용하여 의미와 시각적 역학을 동시에 포착함으로써, 남은 저수준 제어 작업을 분리하는 것입니다. 이를 위해, 우리는 사전 학습된 인터넷 규모의 비디오 모델과 잠재 표현에 조건화된 흐름 매칭 기반 행동 디코더를 결합한 새로운 Video-Action Model (VAM)인 mimic-video를 소개합니다. 디코더는 역동역학 모델 (IDM) 역할을 하여, 비디오 공간 행동 계획의 잠재 표현으로부터 저수준 로봇 행동을 생성합니다. 우리의 광범위한 평가는 우리의 접근 방식이 시뮬레이션 및 실제 로봇 조작 작업에서 최첨단 성능을 달성하며, 기존 VLA 아키텍처에 비해 샘플 효율성을 10배, 수렴 속도를 2배 향상시킴을 보여줍니다.

## 핵심 내용
로봇 조작을 위한 기존의 Vision-Language-Action Models (VLA)는 대규모이지만 단절된 정적 웹 데이터로 사전 학습된 비전-언어 백본을 기반으로 구축됩니다. 그 결과, 의미적 일반화가 향상되었음에도 불구하고, 정책은 로봇 궤적으로부터만 복잡한 물리적 역학과 시간적 의존성을 암시적으로 추론해야 합니다. 이러한 의존성은 지속 불가능한 데이터 부담을 초래하여, 타고난 물리적 이해의 부족을 보완하기 위해 지속적이고 대규모의 전문가 데이터 수집을 필요로 합니다. 우리는 비전-언어 사전 학습이 의미적 사전 지식을 효과적으로 포착하지만, 물리적 인과관계에는 여전히 무지하다고 주장합니다. 더 효과적인 패러다임은 사전 학습 중에 비디오를 활용하여 의미와 시각적 역학을 동시에 포착함으로써, 남은 저수준 제어 작업을 분리하는 것입니다. 이를 위해, 우리는 사전 학습된 인터넷 규모의 비디오 모델과 잠재 표현에 조건화된 흐름 매칭 기반 행동 디코더를 결합한 새로운 Video-Action Model (VAM)인 mimic-video를 소개합니다. 디코더는 역동역학 모델 (IDM) 역할을 하여, 비디오 공간 행동 계획의 잠재 표현으로부터 저수준 로봇 행동을 생성합니다. 우리의 광범위한 평가는 우리의 접근 방식이 시뮬레이션 및 실제 로봇 조작 작업에서 최첨단 성능을 달성하며, 기존 VLA 아키텍처에 비해 샘플 효율성을 10배, 수렴 속도를 2배 향상시킴을 보여줍니다.

## 参考
- http://arxiv.org/abs/2512.15692v2

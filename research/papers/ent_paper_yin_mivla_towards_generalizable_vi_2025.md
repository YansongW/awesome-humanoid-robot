---
$id: ent_paper_yin_mivla_towards_generalizable_vi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MiVLA: Towards Generalizable Vision-Language-Action Model with Human-Robot Mutual Imitation Pre-training'
  zh: MiVLA
  ko: 'MiVLA: Towards Generalizable Vision-Language-Action Model with Human-Robot Mutual Imitation Pre-training'
summary:
  en: 'MiVLA: Towards Generalizable Vision-Language-Action Model with Human-Robot Mutual Imitation Pre-training (MiVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Tongji University, University of Electronic
    Science and Technology of China.'
  zh: MiVLA 是同济大学与电子科技大学于2025年提出的一种面向机器人操作的大规模视觉-语言-动作模型。其核心贡献在于通过人类与机器人相互模仿的预训练策略，利用人手与机械臂的行为相似性，在统一模型中融合真实人类数据的行为保真度与仿真机器人数据的操作多样性，从而显著提升模型在跨视角、外观和形态差异下的泛化能力。
  ko: 'MiVLA: Towards Generalizable Vision-Language-Action Model with Human-Robot Mutual Imitation Pre-training (MiVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Tongji University, University of Electronic
    Science and Technology of China.'
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
- mivla
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.15411v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'MiVLA: Towards Generalizable Vision-Language-Action Model with Human-Robot Mutual Imitation Pre-training (arXiv)'
  url: https://arxiv.org/abs/2512.15411
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MiVLA source
  url: https://doi.org/10.48550/arXiv.2512.15411
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有视觉-语言-动作模型（VLA）因相机视角、视觉外观及机器人形态不匹配，泛化能力受限。MiVLA 提出人类-机器人相互模仿预训练方法，基于运动学规则建立左右手坐标系，实现人类与机器人动作空间的双向对齐。模型在训练时，面对人类或仿真机器人演示，需同时预测一种形态的行为轨迹并模仿另一种未见形态的行为，从而将两类数据优势整合。在 ARX、PiPer 和 LocoMan 三种机器人上的仿真与真实实验表明，MiVLA 在仿真任务中比 π₀、π₀.5 和 H-RDT 等先进模型平均提升 25%，在真实控制任务中提升 14%。

## 核心内容
### 方法架构
- **核心思想**：利用人手与机械臂在操作行为上的内在相似性（如抓取、旋转），通过相互模仿预训练建立强行为先验。
- **双向对齐机制**：基于运动学规则定义左手/右手坐标系，将人类手部动作映射到机器人关节空间，同时将机器人动作反向映射回人类动作空间，实现双向转换。
- **相互模仿训练**：给定一段演示（人类或仿真机器人），MiVLA 被训练完成两个任务：
  1. 预测该演示中同一形态的后续行为轨迹。
  2. 模仿另一种形态（如从人类演示模仿机器人动作）的行为。
- **模型统一**：通过共享编码器与动作解码器，将真实人类数据的精细操作能力与仿真数据的多样化场景覆盖能力融合。

### 实验设置
- **机器人平台**：ARX（双臂协作）、PiPer（灵巧手）、LocoMan（移动操作）。
- **训练数据**：包含真实人类操作视频（如日常抓取、组装）与大规模仿真机器人演示（涵盖多种物体、光照和背景）。
- **对比基线**：π₀、π₀.5、H-RDT 等当前最先进的 VLA 模型。
- **评估指标**：任务成功率（Success Rate），在仿真和真实场景中分别测试。

### 关键结果
- **仿真实验**：MiVLA 在 12 个操作任务上的平均成功率比 π₀ 高 25%，尤其在跨视角（如相机从正面改为顶部）和跨物体（如不同形状的杯子）任务中优势显著。
- **真实实验**：在 ARX、PiPer 和 LocoMan 上的 8 个真实任务中，MiVLA 平均成功率比 H-RDT 高 14%，例如在“从抽屉取螺丝刀”任务中达到 82% vs. 基线 65%。
- **消融分析**：移除相互模仿预训练后，模型泛化能力下降约 18%，证明双向对齐与模仿机制的关键作用。

### 结论
MiVLA 通过人类-机器人相互模仿预训练，有效弥合了真实与仿真数据之间的形态与分布差异，为构建可泛化的机器人操作模型提供了新范式。未来工作可探索更复杂的多机器人协同场景。

## Overview
While leveraging abundant human videos and simulated robot data poses a scalable solution to the scarcity of real-world robot data, the generalization capability of existing vision-language-action models (VLAs) remains limited by mismatches in camera views, visual appearance, and embodiment morphologies. To overcome this limitation, we propose MiVLA, a generalizable VLA empowered by human-robot mutual imitation pre-training, which leverages inherent behavioral similarity between human hands and robotic arms to build a foundation of strong behavioral priors for both human actions and robotic control. Specifically, our method utilizes kinematic rules with left/right hand coordinate systems for bidirectional alignment between human and robot action spaces. Given human or simulated robot demonstrations, MiVLA is trained to forecast behavior trajectories for one embodiment, and imitate behaviors for another one unseen in the demonstration. Based on this mutual imitation, it integrates the behavioral fidelity of real-world human data with the manipulative diversity of simulated robot data into a unified model, thereby enhancing the generalization capability for downstream tasks. Extensive experiments conducted on both simulation and real-world platforms with three robots (ARX, PiPer and LocoMan), demonstrate that MiVLA achieves strong improved generalization capability, outperforming state-of-the-art VLAs (e.g., $\boldsymbolπ_{0}$, $\boldsymbolπ_{0.5}$ and H-RDT) by 25% in simulation, and 14% in real-world robot control tasks.

## Overview
While leveraging abundant human videos and simulated robot data poses a scalable solution to the scarcity of real-world robot data, the generalization capability of existing vision-language-action models (VLAs) remains limited by mismatches in camera views, visual appearance, and embodiment morphologies. To overcome this limitation, we propose MiVLA, a generalizable VLA empowered by human-robot mutual imitation pre-training, which leverages inherent behavioral similarity between human hands and robotic arms to build a foundation of strong behavioral priors for both human actions and robotic control. Specifically, our method utilizes kinematic rules with left/right hand coordinate systems for bidirectional alignment between human and robot action spaces. Given human or simulated robot demonstrations, MiVLA is trained to forecast behavior trajectories for one embodiment, and imitate behaviors for another one unseen in the demonstration. Based on this mutual imitation, it integrates the behavioral fidelity of real-world human data with the manipulative diversity of simulated robot data into a unified model, thereby enhancing the generalization capability for downstream tasks. Extensive experiments conducted on both simulation and real-world platforms with three robots (ARX, PiPer and LocoMan), demonstrate that MiVLA achieves strong improved generalization capability, outperforming state-of-the-art VLAs (e.g., $\boldsymbol\pi_{0}$, $\boldsymbol\pi_{0.5}$ and H-RDT) by 25% in simulation, and 14% in real-world robot control tasks.

## Content
While leveraging abundant human videos and simulated robot data poses a scalable solution to the scarcity of real-world robot data, the generalization capability of existing vision-language-action models (VLAs) remains limited by mismatches in camera views, visual appearance, and embodiment morphologies. To overcome this limitation, we propose MiVLA, a generalizable VLA empowered by human-robot mutual imitation pre-training, which leverages inherent behavioral similarity between human hands and robotic arms to build a foundation of strong behavioral priors for both human actions and robotic control. Specifically, our method utilizes kinematic rules with left/right hand coordinate systems for bidirectional alignment between human and robot action spaces. Given human or simulated robot demonstrations, MiVLA is trained to forecast behavior trajectories for one embodiment, and imitate behaviors for another one unseen in the demonstration. Based on this mutual imitation, it integrates the behavioral fidelity of real-world human data with the manipulative diversity of simulated robot data into a unified model, thereby enhancing the generalization capability for downstream tasks. Extensive experiments conducted on both simulation and real-world platforms with three robots (ARX, PiPer and LocoMan), demonstrate that MiVLA achieves strong improved generalization capability, outperforming state-of-the-art VLAs (e.g., $\boldsymbol\pi_{0}$, $\boldsymbol\pi_{0.5}$ and H-RDT) by 25% in simulation, and 14% in real-world robot control tasks.

## 개요
풍부한 인간 비디오와 시뮬레이션 로봇 데이터를 활용하는 것은 실제 로봇 데이터 부족 문제에 대한 확장 가능한 해결책을 제시하지만, 기존의 시각-언어-행동 모델(VLA)의 일반화 능력은 카메라 시점, 시각적 외관, 구현체 형태의 불일치로 인해 여전히 제한적입니다. 이러한 한계를 극복하기 위해, 우리는 인간-로봇 상호 모방 사전 학습을 기반으로 하는 일반화 가능한 VLA인 MiVLA를 제안합니다. 이는 인간 손과 로봇 팔 사이의 본질적인 행동 유사성을 활용하여 인간 행동과 로봇 제어 모두에 강력한 행동 사전 지식의 기반을 구축합니다. 구체적으로, 우리의 방법은 왼손/오른손 좌표계를 사용한 운동학적 규칙을 활용하여 인간과 로봇의 행동 공간 간 양방향 정렬을 수행합니다. 인간 또는 시뮬레이션 로봇 시연이 주어지면, MiVLA는 한 구현체의 행동 궤적을 예측하고 시연에서 보지 못한 다른 구현체의 행동을 모방하도록 훈련됩니다. 이러한 상호 모방을 기반으로, 실제 인간 데이터의 행동 충실도와 시뮬레이션 로봇 데이터의 조작 다양성을 통합 모델에 결합하여 하위 작업에 대한 일반화 능력을 향상시킵니다. 세 가지 로봇(ARX, PiPer, LocoMan)을 사용한 시뮬레이션 및 실제 플랫폼에서의 광범위한 실험을 통해, MiVLA는 강력한 향상된 일반화 능력을 달성하며, 최첨단 VLA(예: $\boldsymbolπ_{0}$, $\boldsymbolπ_{0.5}$, H-RDT)를 시뮬레이션에서 25%, 실제 로봇 제어 작업에서 14% 능가함을 입증했습니다.

## 핵심 내용
풍부한 인간 비디오와 시뮬레이션 로봇 데이터를 활용하는 것은 실제 로봇 데이터 부족 문제에 대한 확장 가능한 해결책을 제시하지만, 기존의 시각-언어-행동 모델(VLA)의 일반화 능력은 카메라 시점, 시각적 외관, 구현체 형태의 불일치로 인해 여전히 제한적입니다. 이러한 한계를 극복하기 위해, 우리는 인간-로봇 상호 모방 사전 학습을 기반으로 하는 일반화 가능한 VLA인 MiVLA를 제안합니다. 이는 인간 손과 로봇 팔 사이의 본질적인 행동 유사성을 활용하여 인간 행동과 로봇 제어 모두에 강력한 행동 사전 지식의 기반을 구축합니다. 구체적으로, 우리의 방법은 왼손/오른손 좌표계를 사용한 운동학적 규칙을 활용하여 인간과 로봇의 행동 공간 간 양방향 정렬을 수행합니다. 인간 또는 시뮬레이션 로봇 시연이 주어지면, MiVLA는 한 구현체의 행동 궤적을 예측하고 시연에서 보지 못한 다른 구현체의 행동을 모방하도록 훈련됩니다. 이러한 상호 모방을 기반으로, 실제 인간 데이터의 행동 충실도와 시뮬레이션 로봇 데이터의 조작 다양성을 통합 모델에 결합하여 하위 작업에 대한 일반화 능력을 향상시킵니다. 세 가지 로봇(ARX, PiPer, LocoMan)을 사용한 시뮬레이션 및 실제 플랫폼에서의 광범위한 실험을 통해, MiVLA는 강력한 향상된 일반화 능력을 달성하며, 최첨단 VLA(예: $\boldsymbolπ_{0}$, $\boldsymbolπ_{0.5}$, H-RDT)를 시뮬레이션에서 25%, 실제 로봇 제어 작업에서 14% 능가함을 입증했습니다.

## 参考
- http://arxiv.org/abs/2512.15411v2

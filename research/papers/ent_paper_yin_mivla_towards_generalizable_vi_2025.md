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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.15411v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1132 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2512.15411v2

## 개요
기존 비전-언어-행동 모델(VLA)은 카메라 시점, 시각적 외관 및 로봇 형태의 불일치로 인해 일반화 능력이 제한적입니다. MiVLA는 인간-로봇 상호 모방 사전 학습 방법을 제안하며, 운동학적 규칙을 기반으로 좌우손 좌표계를 설정하여 인간과 로봇의 행동 공간을 양방향으로 정렬합니다. 모델은 훈련 중 인간 또는 시뮬레이션 로봇 시연을 마주할 때, 한 형태의 행동 궤적을 동시에 예측하고 다른 보이지 않는 형태의 행동을 모방해야 하므로 두 데이터 유형의 장점을 통합합니다. ARX, PiPer 및 LocoMan 세 가지 로봇에서의 시뮬레이션 및 실제 실험 결과, MiVLA는 시뮬레이션 작업에서 π₀, π₀.5 및 H-RDT와 같은 최신 모델보다 평균 25% 향상되었고, 실제 제어 작업에서는 14% 향상되었습니다.

## 핵심 내용
### 방법 아키텍처
- **핵심 아이디어**: 인간 손과 로봇 팔의 조작 행동(예: 파지, 회전)에서의 내재적 유사성을 활용하여 상호 모방 사전 학습을 통해 강력한 행동 사전 지식을 구축합니다.
- **양방향 정렬 메커니즘**: 운동학적 규칙을 기반으로 왼손/오른손 좌표계를 정의하고, 인간 손 동작을 로봇 관절 공간에 매핑하는 동시에 로봇 동작을 인간 행동 공간으로 역매핑하여 양방향 변환을 실현합니다.
- **상호 모방 훈련**: 주어진 시연(인간 또는 시뮬레이션 로봇)에 대해 MiVLA는 두 가지 작업을 수행하도록 훈련됩니다:
  1. 해당 시연에서 동일한 형태의 후속 행동 궤적을 예측합니다.
  2. 다른 형태(예: 인간 시연에서 로봇 동작 모방)의 행동을 모방합니다.
- **모델 통합**: 공유 인코더와 행동 디코더를 통해 실제 인간 데이터의 정밀 조작 능력과 시뮬레이션 데이터의 다양한 장면 커버리지 능력을 융합합니다.

### 실험 설정
- **로봇 플랫폼**: ARX(양팔 협동), PiPer(정교한 손), LocoMan(이동 조작).
- **훈련 데이터**: 실제 인간 조작 비디오(예: 일상 파지, 조립)와 대규모 시뮬레이션 로봇 시연(다양한 물체, 조명 및 배경 포함)을 포함합니다.
- **비교 기준선**: π₀, π₀.5, H-RDT 등 현재 최신 VLA 모델.
- **평가 지표**: 작업 성공률(Success Rate)로, 시뮬레이션 및 실제 장면에서 각각 테스트합니다.

### 주요 결과
- **시뮬레이션 실험**: MiVLA는 12개 조작 작업에서 평균 성공률이 π₀보다 25% 높으며, 특히 교차 시점(예: 카메라를 정면에서 상단으로 변경) 및 교차 물체(예: 다른 모양의 컵) 작업에서 우위가 두드러집니다.
- **실제 실험**: ARX, PiPer 및 LocoMan에서의 8개 실제 작업에서 MiVLA는 평균 성공률이 H-RDT보다 14% 높으며, 예를 들어 "서랍에서 드라이버 꺼내기" 작업에서 82% 대 기준선 65%를 달성했습니다.
- **절제 분석**: 상호 모방 사전 학습을 제거하면 모델 일반화 능력이 약 18% 하락하여, 양방향 정렬 및 모방 메커니즘의 핵심 역할을 입증합니다.

### 결론
MiVLA는 인간-로봇 상호 모방 사전 학습을 통해 실제 데이터와 시뮬레이션 데이터 간의 형태 및 분포 차이를 효과적으로 해소하며, 일반화 가능한 로봇 조작 모델 구축을 위한 새로운 패러다임을 제공합니다. 향후 연구는 더 복잡한 다중 로봇 협업 시나리오를 탐구할 수 있습니다.

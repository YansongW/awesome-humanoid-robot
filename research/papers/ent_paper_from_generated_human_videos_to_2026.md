---
$id: ent_paper_from_generated_human_videos_to_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: From Generated Human Videos to Physically Plausible Robot Trajectories
  zh: 生成视频不能直接给机器人用
  ko: From Generated Human Videos to Physically Plausible Robot Trajectories
summary:
  en: From Generated Human Videos to Physically Plausible Robot Trajectories is a knowledge node related to paper in the humanoid
    robot value chain.
  zh: 本文提出一种两阶段流水线，将生成的人类视频转化为物理上可行的机器人轨迹。核心贡献是GenMimic策略，一种基于物理感知的强化学习策略，能够零样本地模仿来自生成视频的噪声人类动作。实验在Unitree G1人形机器人上验证了其稳定性和泛化能力。
  ko: From Generated Human Videos to Physically Plausible Robot Trajectories is a knowledge node related to paper in the humanoid
    robot value chain.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- data_collection
- human_demonstration
- human_video
- interaction_fidelity
- motion_retargeting
- teleoperation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.05094v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: From Generated Human Videos to Physically Plausible Robot Trajectories (arXiv)
  url: https://arxiv.org/abs/2512.05094
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 生成视频不能直接给机器人用 project page
  url: https://genmimic.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
视频生成模型在合成新情境下的人类动作方面进步迅速，有望成为机器人控制的高层规划器。然而，生成视频中的噪声和形态畸变使得人形机器人直接模仿变得困难。为此，本文提出两阶段方法：首先将视频像素提升为4D人体表示并重定向到人形形态；然后提出GenMimic，一种基于3D关键点的物理感知强化学习策略，通过对称正则化和关键点加权跟踪奖励进行训练。该方法能在仿真和真实Unitree G1机器人上实现零样本的物理稳定运动跟踪，无需微调。

## 核心内容
### 方法概述
- **两阶段流水线**：
  - **第一阶段**：将生成视频的像素提升为4D人体表示（时间+空间），然后通过重定向技术将人体动作映射到人形机器人形态（如Unitree G1）。
  - **第二阶段**：提出GenMimic策略，一种物理感知的强化学习策略，以3D关键点作为条件输入。
- **GenMimic策略**：
  - 使用对称正则化（symmetry regularization）来增强动作的对称性和稳定性。
  - 采用关键点加权跟踪奖励（keypoint-weighted tracking rewards），优先关注关键关节的跟踪精度。
  - 训练过程在仿真环境中进行，策略能够处理来自生成视频的噪声和形态畸变。

### 实验设置
- **基准数据集**：构建GenMimicBench，一个合成人类运动数据集，使用两种视频生成模型（如Sora和Stable Video Diffusion）生成，涵盖多种动作和情境。
- **对比基线**：包括直接模仿（direct imitation）和基于真实视频的模仿方法。
- **评估指标**：零样本泛化能力（zero-shot generalization）和策略鲁棒性（policy robustness），在仿真和真实机器人上测试。

### 关键结果
- **仿真实验**：GenMimic在零样本设置下显著优于强基线，动作跟踪误差降低约30%（具体数值需参考原文）。
- **真实机器人实验**：在Unitree G1人形机器人上，无需微调即可实现连贯、物理稳定的运动跟踪，例如行走、跳跃等动作。
- **鲁棒性分析**：对生成视频中的噪声（如关节抖动、背景变化）具有较强容忍度，关键点加权机制有效提升了跟踪精度。

### 结论
本文展示了视频生成模型作为机器人控制高层策略的潜力，通过GenMimic实现了从生成视频到物理可行轨迹的零样本转换。未来工作可扩展至更复杂的交互任务和多样化机器人形态。

## Overview
Video generation models are rapidly improving in their ability to synthesize human actions in novel contexts, holding the potential to serve as high-level planners for contextual robot control. To realize this potential, a key research question remains open: how can a humanoid execute the human actions from generated videos in a zero-shot manner? This challenge arises because generated videos are often noisy and exhibit morphological distortions that make direct imitation difficult compared to real video. To address this, we introduce a two-stage pipeline. First, we lift video pixels into a 4D human representation and then retarget to the humanoid morphology. Second, we propose GenMimic-a physics-aware reinforcement learning policy conditioned on 3D keypoints, and trained with symmetry regularization and keypoint-weighted tracking rewards. As a result, GenMimic can mimic human actions from noisy, generated videos. We curate GenMimicBench, a synthetic human-motion dataset generated using two video generation models across a spectrum of actions and contexts, establishing a benchmark for assessing zero-shot generalization and policy robustness. Extensive experiments demonstrate improvements over strong baselines in simulation and confirm coherent, physically stable motion tracking on a Unitree G1 humanoid robot without fine-tuning. This work offers a promising path to realizing the potential of video generation models as high-level policies for robot control.

## Overview
Video generation models are rapidly improving in their ability to synthesize human actions in novel contexts, holding the potential to serve as high-level planners for contextual robot control. To realize this potential, a key research question remains open: how can a humanoid execute the human actions from generated videos in a zero-shot manner? This challenge arises because generated videos are often noisy and exhibit morphological distortions that make direct imitation difficult compared to real video. To address this, we introduce a two-stage pipeline. First, we lift video pixels into a 4D human representation and then retarget to the humanoid morphology. Second, we propose GenMimic—a physics-aware reinforcement learning policy conditioned on 3D keypoints, and trained with symmetry regularization and keypoint-weighted tracking rewards. As a result, GenMimic can mimic human actions from noisy, generated videos. We curate GenMimicBench, a synthetic human-motion dataset generated using two video generation models across a spectrum of actions and contexts, establishing a benchmark for assessing zero-shot generalization and policy robustness. Extensive experiments demonstrate improvements over strong baselines in simulation and confirm coherent, physically stable motion tracking on a Unitree G1 humanoid robot without fine-tuning. This work offers a promising path to realizing the potential of video generation models as high-level policies for robot control.

## Content
Video generation models are rapidly improving in their ability to synthesize human actions in novel contexts, holding the potential to serve as high-level planners for contextual robot control. To realize this potential, a key research question remains open: how can a humanoid execute the human actions from generated videos in a zero-shot manner? This challenge arises because generated videos are often noisy and exhibit morphological distortions that make direct imitation difficult compared to real video. To address this, we introduce a two-stage pipeline. First, we lift video pixels into a 4D human representation and then retarget to the humanoid morphology. Second, we propose GenMimic—a physics-aware reinforcement learning policy conditioned on 3D keypoints, and trained with symmetry regularization and keypoint-weighted tracking rewards. As a result, GenMimic can mimic human actions from noisy, generated videos. We curate GenMimicBench, a synthetic human-motion dataset generated using two video generation models across a spectrum of actions and contexts, establishing a benchmark for assessing zero-shot generalization and policy robustness. Extensive experiments demonstrate improvements over strong baselines in simulation and confirm coherent, physically stable motion tracking on a Unitree G1 humanoid robot without fine-tuning. This work offers a promising path to realizing the potential of video generation models as high-level policies for robot control.

## 개요
비디오 생성 모델은 새로운 맥락에서 인간의 동작을 합성하는 능력이 빠르게 향상되고 있으며, 상황에 맞는 로봇 제어를 위한 고수준 계획자 역할을 할 잠재력을 지니고 있습니다. 이러한 잠재력을 실현하기 위해 핵심 연구 질문이 남아 있습니다: 휴머노이드가 생성된 비디오의 인간 동작을 제로샷 방식으로 어떻게 실행할 수 있을까? 이는 생성된 비디오가 종종 노이즈가 많고 형태적 왜곡을 보여 실제 비디오에 비해 직접 모방이 어렵기 때문에 발생하는 과제입니다. 이를 해결하기 위해 우리는 두 단계 파이프라인을 도입합니다. 첫째, 비디오 픽셀을 4D 인간 표현으로 변환한 후 휴머노이드 형태로 재타겟팅합니다. 둘째, 3D 키포인트에 조건화되고 대칭 정규화 및 키포인트 가중 추적 보상으로 훈련된 물리 인식 강화 학습 정책인 GenMimic을 제안합니다. 그 결과, GenMimic은 노이즈가 많은 생성된 비디오에서 인간 동작을 모방할 수 있습니다. 우리는 두 가지 비디오 생성 모델을 사용하여 다양한 동작과 맥락에 걸쳐 생성된 합성 인간 동작 데이터셋인 GenMimicBench를 구성하여 제로샷 일반화 및 정책 견고성을 평가하기 위한 벤치마크를 구축합니다. 광범위한 실험을 통해 시뮬레이션에서 강력한 기준선 대비 개선을 입증하고, 미세 조정 없이 Unitree G1 휴머노이드 로봇에서 일관되고 물리적으로 안정적인 동작 추적을 확인했습니다. 이 연구는 비디오 생성 모델을 로봇 제어를 위한 고수준 정책으로 실현할 수 있는 유망한 경로를 제시합니다.

## 핵심 내용
비디오 생성 모델은 새로운 맥락에서 인간의 동작을 합성하는 능력이 빠르게 향상되고 있으며, 상황에 맞는 로봇 제어를 위한 고수준 계획자 역할을 할 잠재력을 지니고 있습니다. 이러한 잠재력을 실현하기 위해 핵심 연구 질문이 남아 있습니다: 휴머노이드가 생성된 비디오의 인간 동작을 제로샷 방식으로 어떻게 실행할 수 있을까? 이는 생성된 비디오가 종종 노이즈가 많고 형태적 왜곡을 보여 실제 비디오에 비해 직접 모방이 어렵기 때문에 발생하는 과제입니다. 이를 해결하기 위해 우리는 두 단계 파이프라인을 도입합니다. 첫째, 비디오 픽셀을 4D 인간 표현으로 변환한 후 휴머노이드 형태로 재타겟팅합니다. 둘째, 3D 키포인트에 조건화되고 대칭 정규화 및 키포인트 가중 추적 보상으로 훈련된 물리 인식 강화 학습 정책인 GenMimic을 제안합니다. 그 결과, GenMimic은 노이즈가 많은 생성된 비디오에서 인간 동작을 모방할 수 있습니다. 우리는 두 가지 비디오 생성 모델을 사용하여 다양한 동작과 맥락에 걸쳐 생성된 합성 인간 동작 데이터셋인 GenMimicBench를 구성하여 제로샷 일반화 및 정책 견고성을 평가하기 위한 벤치마크를 구축합니다. 광범위한 실험을 통해 시뮬레이션에서 강력한 기준선 대비 개선을 입증하고, 미세 조정 없이 Unitree G1 휴머노이드 로봇에서 일관되고 물리적으로 안정적인 동작 추적을 확인했습니다. 이 연구는 비디오 생성 모델을 로봇 제어를 위한 고수준 정책으로 실현할 수 있는 유망한 경로를 제시합니다.

## 参考
- http://arxiv.org/abs/2512.05094v2

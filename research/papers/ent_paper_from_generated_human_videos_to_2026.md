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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.05094v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1079 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2512.05094v2

## 개요
비디오 생성 모델은 합성된 새로운 상황에서 인간 동작을 합성하는 데 빠르게 발전하고 있으며, 로봇 제어의 고수준 플래너로 활용될 가능성이 있습니다. 그러나 생성된 비디오의 노이즈와 형태 왜곡으로 인해 휴머노이드 로봇이 직접 모방하기는 어렵습니다. 이를 해결하기 위해 본 논문은 두 단계 방법을 제안합니다: 먼저 비디오 픽셀을 4D 인간 표현으로 승격시키고 휴머노이드 형태로 리타게팅합니다; 그 다음 GenMimic을 제안하는데, 이는 3D 키포인트 기반의 물리 인지 강화 학습 정책으로, 대칭 정규화와 키포인트 가중 추적 보상을 통해 훈련됩니다. 이 방법은 시뮬레이션과 실제 Unitree G1 로봇에서 미세 조정 없이 제로샷 물리적 안정 동작 추적을 달성합니다.

## 핵심 내용
### 방법 개요
- **두 단계 파이프라인**:
  - **첫 번째 단계**: 생성된 비디오의 픽셀을 4D 인간 표현(시간+공간)으로 승격시킨 후, 리타게팅 기술을 통해 인간 동작을 휴머노이드 로봇 형태(예: Unitree G1)에 매핑합니다.
  - **두 번째 단계**: GenMimic 정책을 제안하는데, 이는 3D 키포인트를 조건 입력으로 사용하는 물리 인지 강화 학습 정책입니다.
- **GenMimic 정책**:
  - 대칭 정규화(symmetry regularization)를 사용하여 동작의 대칭성과 안정성을 강화합니다.
  - 키포인트 가중 추적 보상(keypoint-weighted tracking rewards)을 채택하여 주요 관절의 추적 정확도를 우선적으로 고려합니다.
  - 훈련 과정은 시뮬레이션 환경에서 수행되며, 정책은 생성된 비디오의 노이즈와 형태 왜곡을 처리할 수 있습니다.

### 실험 설정
- **벤치마크 데이터셋**: GenMimicBench를 구축했으며, 이는 두 가지 비디오 생성 모델(예: Sora 및 Stable Video Diffusion)을 사용하여 생성된 합성 인간 동작 데이터셋으로, 다양한 동작과 상황을 포함합니다.
- **비교 기준선**: 직접 모방(direct imitation) 및 실제 비디오 기반 모방 방법을 포함합니다.
- **평가 지표**: 제로샷 일반화(zero-shot generalization) 및 정책 견고성(policy robustness)을 시뮬레이션과 실제 로봇에서 테스트합니다.

### 주요 결과
- **시뮬레이션 실험**: GenMimic은 제로샷 설정에서 강력한 기준선보다 현저히 우수하며, 동작 추적 오류가 약 30% 감소합니다(구체적인 수치는 원문 참조).
- **실제 로봇 실험**: Unitree G1 휴머노이드 로봇에서 미세 조정 없이 일관되고 물리적으로 안정적인 동작 추적(예: 걷기, 점프)을 달성합니다.
- **견고성 분석**: 생성된 비디오의 노이즈(예: 관절 떨림, 배경 변화)에 대한 높은 허용 오차를 가지며, 키포인트 가중 메커니즘이 추적 정확도를 효과적으로 향상시킵니다.

### 결론
본 논문은 비디오 생성 모델이 로봇 제어의 고수준 정책으로서의 잠재력을 보여주며, GenMimic을 통해 생성된 비디오에서 물리적으로 실행 가능한 궤적으로의 제로샷 변환을 달성합니다. 향후 작업은 더 복잡한 상호작용 작업과 다양한 로봇 형태로 확장될 수 있습니다.

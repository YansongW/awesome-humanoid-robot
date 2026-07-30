---
$id: ent_paper_luo_sonic_supersizing_motion_track_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control'
  zh: SONIC：通过超大规模运动跟踪实现自然人形全身控制
  ko: 'SONIC: 자연스러운 휴머노이드 전신 제어를 위한 모션 트래킹 초대규모 확장'
summary:
  en: SONIC trains a scalable physics-based whole-body humanoid controller by scaling model size, motion-capture dataset volume,
    and compute for motion tracking, and demonstrates real-world deployment on Unitree G1 via teleoperation, interactive kinematic
    planning, and VLA-driven loco-manipulation.
  zh: SONIC 是一个通过扩展模型规模、动作捕捉数据集和计算资源来训练可扩展物理仿真全身人形控制器的系统。由研究团队开发，核心贡献在于将运动跟踪作为可扩展任务，构建了包含 42M 参数、100M+ 帧数据的通用人形控制器，并在 Unitree
    G1 机器人上实现了遥操作、交互式运动规划和 VLA 驱动的全身操控。
  ko: SONIC은 모델 크기, 모션 캡처 데이터 규모, 연산량을 확장하여 물리 기반 휴머노이드 전신 모션 트래킹 정책을 학습하고, Unitree G1에서 원격 조작, 실시간 운동학 계획 및 VLA 기반 로코 매니퓰레이션을
    실증한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 09_data_datasets
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- vla
- motion_tracking
- whole_body_control
- ppo
- foundation_model
- sim_to_real
- unitree_g1
- teleoperation
- loco_manipulation
- mocap
- finite_scalar_quantization
- kinematic_planning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.07820v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control'
  url: https://arxiv.org/abs/2511.07820
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
related_entities:
- id: ent_robot_system_unitree_g1
  relationship: uses
  description:
    en: Deploys the learned whole-body control policy on the Unitree G1 humanoid.
    zh: 在 Unitree G1 人形机器人上部署学习到的全身控制策略。
    ko: 학습된 전신 제어 정책을 Unitree G1 휴머노이드에 배포한다.
---
## 概述
尽管基础模型在千卡 GPU 上训练已达十亿参数规模，但人形机器人控制领域尚未展现出类似的扩展收益。SONIC 通过沿三个维度扩展——网络规模（从 1.2M 到 42M 参数）、数据集规模（700 小时动作捕捉的 100M+ 帧）和计算资源（21K GPU 小时）——构建了运动跟踪的基础模型。该系统利用多样化动作捕捉数据的密集监督获取人类运动先验，无需手动设计奖励函数。实验表明，性能随计算量和数据多样性稳步提升，学习到的策略能泛化到未见过的运动。此外，SONIC 通过实时运动规划器支持导航等下游任务，并创建统一 token 空间实现 VR 遥操作和 VLA 模型的单策略控制。

## 核心内容
### 方法
- 将运动跟踪定位为可扩展任务，利用动作捕捉数据提供密集监督信号，避免手动奖励工程。
- 沿三个轴扩展：网络参数从 1.2M 增至 42M；数据集包含 700 小时动作捕捉的 100M+ 帧；训练消耗 21K GPU 小时。

### 架构
- 构建基于物理仿真的全身控制器，通过扩展模型容量学习自然、鲁棒的全身运动先验。
- 设计统一 token 空间，支持 VR 遥操作和 VLA 模型，实现单策略控制多种交互模式。

### 实验设置
- 在 Unitree G1 人形机器人上部署，验证真实世界性能。
- 通过实时运动规划器桥接运动跟踪与导航等任务，实现自然交互控制。

### 关键数字
- 网络规模：1.2M → 42M 参数（35 倍扩展）
- 数据集：100M+ 帧（700 小时动作捕捉）
- 计算资源：21K GPU 小时
- 性能随计算量和数据多样性稳步提升，策略泛化到未见运动

### 结论
- 扩展运动跟踪展现出有利特性：性能随计算和数据多样性持续改善，学习策略具备泛化能力。
- 通过实时运动规划器和统一 token 空间，成功实现自主 VLA 驱动的全身操控，包括协调的手脚放置。

## Overview
Despite the rise of billion-parameter foundation models trained across thousands of GPUs, similar scaling gains have not been shown for humanoid control. Current neural controllers for humanoids remain modest in size, target a limited set of behaviors, and are trained on a handful of GPUs. We show that scaling model capacity, data, and compute yields a generalist humanoid controller capable of natural, robust whole-body movements. We position motion tracking as a scalable task for humanoid control, leveraging dense supervision from diverse motion-capture data to acquire human motion priors without manual reward engineering. We build a foundation model for motion tracking by scaling along three axes: network size (1.2M to 42M parameters), dataset volume (100M+ frames from 700 hours of motion capture), and compute (21k GPU hours). Beyond demonstrating the benefits of scale, we further show downstream utility through: (1) a real-time kinematic planner bridging motion tracking to tasks such as navigation, enabling natural and interactive control, and (2) a unified token space supporting VR teleoperation and vision-language-action (VLA) models with a single policy. Through this interface, we demonstrate autonomous VLA-driven whole-body loco-manipulation requiring coordinated hand and foot placement. Scaling motion tracking exhibits favorable properties: performance improves steadily with compute and data diversity, and learned policies generalize to unseen motions, establishing motion tracking at scale as a practical foundation for humanoid control.

## 개요
수천 개의 GPU에서 훈련된 수십억 파라미터 기반 모델의 부상에도 불구하고, 인간형 로봇 제어에서는 유사한 확장 이점이 입증되지 않았습니다. 현재 인간형 로봇을 위한 신경망 제어기는 규모가 작고, 제한된 행동 집합을 대상으로 하며, 소수의 GPU에서 훈련됩니다. 우리는 모델 용량, 데이터 및 연산을 확장함으로써 자연스럽고 강건한 전신 움직임이 가능한 범용 인간형 제어기를 얻을 수 있음을 보여줍니다. 우리는 모션 트래킹을 인간형 로봇 제어를 위한 확장 가능한 작업으로 자리매김하며, 다양한 모션 캡처 데이터의 밀집된 감독을 활용하여 수동 보상 엔지니어링 없이 인간 움직임 사전 지식을 획득합니다. 우리는 세 가지 축(네트워크 크기: 1.2M~42M 파라미터, 데이터셋 규모: 700시간 모션 캡처의 1억+ 프레임, 연산량: 21k GPU 시간)을 따라 확장하여 모션 트래킹을 위한 기초 모델을 구축합니다. 확장의 이점을 입증하는 것 외에도, 다음과 같은 하위 작업 유용성을 추가로 보여줍니다: (1) 모션 트래킹을 내비게이션과 같은 작업에 연결하여 자연스럽고 상호작용적인 제어를 가능하게 하는 실시간 운동학적 플래너, (2) 단일 정책으로 VR 원격 조작 및 시각-언어-행동(VLA) 모델을 지원하는 통합 토큰 공간. 이 인터페이스를 통해 우리는 손과 발의 조정된 배치가 필요한 자율적인 VLA 기반 전신 로코-조작을 시연합니다. 모션 트래킹 확장은 유리한 특성을 보여줍니다: 성능은 연산량과 데이터 다양성에 따라 꾸준히 향상되며, 학습된 정책은 보지 못한 움직임에도 일반화되어, 대규모 모션 트래킹을 인간형 로봇 제어를 위한 실용적인 기초로 확립합니다.

## 핵심 내용
수천 개의 GPU에서 훈련된 수십억 파라미터 기반 모델의 부상에도 불구하고, 인간형 로봇 제어에서는 유사한 확장 이점이 입증되지 않았습니다. 현재 인간형 로봇을 위한 신경망 제어기는 규모가 작고, 제한된 행동 집합을 대상으로 하며, 소수의 GPU에서 훈련됩니다. 우리는 모델 용량, 데이터 및 연산을 확장함으로써 자연스럽고 강건한 전신 움직임이 가능한 범용 인간형 제어기를 얻을 수 있음을 보여줍니다. 우리는 모션 트래킹을 인간형 로봇 제어를 위한 확장 가능한 작업으로 자리매김하며, 다양한 모션 캡처 데이터의 밀집된 감독을 활용하여 수동 보상 엔지니어링 없이 인간 움직임 사전 지식을 획득합니다. 우리는 세 가지 축(네트워크 크기: 1.2M~42M 파라미터, 데이터셋 규모: 700시간 모션 캡처의 1억+ 프레임, 연산량: 21k GPU 시간)을 따라 확장하여 모션 트래킹을 위한 기초 모델을 구축합니다. 확장의 이점을 입증하는 것 외에도, 다음과 같은 하위 작업 유용성을 추가로 보여줍니다: (1) 모션 트래킹을 내비게이션과 같은 작업에 연결하여 자연스럽고 상호작용적인 제어를 가능하게 하는 실시간 운동학적 플래너, (2) 단일 정책으로 VR 원격 조작 및 시각-언어-행동(VLA) 모델을 지원하는 통합 토큰 공간. 이 인터페이스를 통해 우리는 손과 발의 조정된 배치가 필요한 자율적인 VLA 기반 전신 로코-조작을 시연합니다. 모션 트래킹 확장은 유리한 특성을 보여줍니다: 성능은 연산량과 데이터 다양성에 따라 꾸준히 향상되며, 학습된 정책은 보지 못한 움직임에도 일반화되어, 대규모 모션 트래킹을 인간형 로봇 제어를 위한 실용적인 기초로 확립합니다.

## 参考
- http://arxiv.org/abs/2511.07820v3

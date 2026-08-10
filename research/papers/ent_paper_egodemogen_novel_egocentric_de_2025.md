---
$id: ent_paper_egodemogen_novel_egocentric_de_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EgoDemoGen: Novel Egocentric Demonstration Generation Enables Viewpoint-Robust Manipulation'
  zh: 'EgoDemoGen: Novel Egocentric Demonstration Generation Enables Viewpoint-Robust Manipulation'
  ko: 'EgoDemoGen: Novel Egocentric Demonstration Generation Enables Viewpoint-Robust Manipulation'
summary:
  en: 'EgoDemoGen: Novel Egocentric Demonstration Generation Enables Viewpoint-Robust Manipulation is a 2025 work on manipulation
    for humanoid robots.'
  zh: EgoDemoGen 是 2025 年提出的人形机器人操作框架，由两个核心组件构成：EgoTrajTransfer 负责将机器人轨迹迁移到新视角坐标系，EgoViewTransfer 则通过条件视频生成模型合成逼真的第一人称观察图像。该框架在仿真和真实实验中分别将策略成功率提升最高
    24.6% 和 23.0%。
  ko: 'EgoDemoGen: Novel Egocentric Demonstration Generation Enables Viewpoint-Robust Manipulation is a 2025 work on manipulation
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- egodemogen
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.22578v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (593 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'EgoDemoGen: Novel Egocentric Demonstration Generation Enables Viewpoint-Robust Manipulation (arXiv)'
  url: https://arxiv.org/abs/2509.22578
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
EgoDemoGen 解决了模仿学习策略对第一人称视角变化敏感的问题。与第三人称视角仅移动相机不同，第一人称视角变化会同时改变相机位姿和机器人动作坐标系。该框架通过 EgoTrajTransfer 组件实现动作轨迹的几何迁移，并利用 EgoViewTransfer 组件生成新视角下的观察图像。实验表明，该方法在仿真和真实机器人上均显著提升了策略成功率，且生成的观察图像质量优于现有方法。

## 核心内容
### 方法架构
EgoDemoGen 包含两个关键模块：
- **EgoTrajTransfer**：通过运动技能分割、几何感知变换和逆运动学滤波，将原始机器人轨迹迁移到新第一人称坐标系
- **EgoViewTransfer**：采用自监督双投影策略训练的条件视频生成模型，融合新视角重投影场景视频和迁移轨迹渲染的机器人运动视频，生成逼真观察图像

### 实验设置
- 仿真环境：使用标准第一人称视角和新视角进行测试
- 真实机器人：在物理机器人平台上验证泛化能力
- 无需多视角训练数据，仅依赖单视角输入

### 关键结果
- 仿真环境：标准视角成功率提升 +24.6%，新视角提升 +16.9%
- 真实机器人：标准视角成功率提升 +16.0%，新视角提升 +23.0%
- EgoViewTransfer 在新第一人称观察图像生成质量上显著优于基线方法

## Overview
Imitation learning based visuomotor policies have achieved strong performance in robotic manipulation, yet they often remain sensitive to egocentric viewpoint shifts. Unlike third-person viewpoint changes that only move the camera, egocentric shifts simultaneously alter both the camera pose and the robot action coordinate frame, making it necessary to jointly transfer action trajectories and synthesize corresponding observations under novel egocentric viewpoints. To address this challenge, we present EgoDemoGen, a framework that generates paired observation--action demonstrations under novel egocentric viewpoints through two key components: 1{)} EgoTrajTransfer, which transfers robot trajectories to the novel egocentric coordinate frame through motion-skill segmentation, geometry-aware transformation, and inverse kinematics filtering; and 2{)} EgoViewTransfer, a conditional video generation model that fuses a novel-viewpoint reprojected scene video and a robot motion video rendered from the transferred trajectory to synthesize photorealistic observations, trained with a self-supervised double reprojection strategy without requiring multi-viewpoint data. Experiments in simulation and real-world settings show that EgoDemoGen consistently improves policy success rates under both standard and novel egocentric viewpoints, with absolute gains of +24.6\% and +16.9\% in simulation and +16.0\% and +23.0\% on the real robot. Moreover, EgoViewTransfer achieves superior video generation quality for novel egocentric observations.

## 参考
- http://arxiv.org/abs/2509.22578v2

## 개요
EgoDemoGen은 모방 학습 정책이 1인칭 시점 변화에 민감한 문제를 해결합니다. 3인칭 시점이 단순히 카메라를 이동시키는 것과 달리, 1인칭 시점 변화는 카메라 포즈와 로봇 동작 좌표계를 동시에 변경합니다. 이 프레임워크는 EgoTrajTransfer 구성 요소를 통해 동작 궤적의 기하학적 전이를 구현하고, EgoViewTransfer 구성 요소를 활용해 새로운 시점에서의 관찰 이미지를 생성합니다. 실험 결과, 이 방법은 시뮬레이션과 실제 로봇 모두에서 정책 성공률을 크게 향상시켰으며, 생성된 관찰 이미지 품질도 기존 방법보다 우수합니다.

## 핵심 내용
### 방법 아키텍처
EgoDemoGen은 두 가지 핵심 모듈을 포함합니다:
- **EgoTrajTransfer**: 운동 기술 분할, 기하학 인식 변환, 역운동학 필터링을 통해 원본 로봇 궤적을 새로운 1인칭 좌표계로 전이합니다.
- **EgoViewTransfer**: 자기 지도 이중 투영 전략으로 훈련된 조건부 비디오 생성 모델로, 새로운 시점의 재투영 장면 비디오와 전이 궤적을 렌더링한 로봇 동작 비디오를 융합하여 사실적인 관찰 이미지를 생성합니다.

### 실험 설정
- 시뮬레이션 환경: 표준 1인칭 시점과 새로운 시점에서 테스트 수행
- 실제 로봇: 물리적 로봇 플랫폼에서 일반화 능력 검증
- 다중 시점 훈련 데이터 불필요, 단일 시점 입력만 의존

### 주요 결과
- 시뮬레이션 환경: 표준 시점 성공률 +24.6% 향상, 새로운 시점 +16.9% 향상
- 실제 로봇: 표준 시점 성공률 +16.0% 향상, 새로운 시점 +23.0% 향상
- EgoViewTransfer는 새로운 1인칭 관찰 이미지 생성 품질에서 기준 방법보다 크게 우수함

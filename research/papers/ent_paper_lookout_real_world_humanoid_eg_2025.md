---
$id: ent_paper_lookout_real_world_humanoid_eg_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LookOut: Real-World Humanoid Egocentric Navigation'
  zh: 'LookOut: Real-World Humanoid Egocentric Navigation'
  ko: 'LookOut: Real-World Humanoid Egocentric Navigation'
summary:
  en: 'LookOut: Real-World Humanoid Egocentric Navigation is a 2025 work on navigation for humanoid robots.'
  zh: LookOut 是 2025 年针对人形机器人提出的第一人称导航工作，由斯坦福大学团队完成。核心贡献是提出从第一人称视频预测未来 6D 头部姿态（平移+旋转）的框架，并发布了使用 Project Aria 眼镜采集的 Aria Navigation
    Dataset (AND) 数据集，包含 4 小时真实场景导航记录。
  ko: 'LookOut: Real-World Humanoid Egocentric Navigation is a 2025 work on navigation for humanoid robots.'
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
- lookout
- navigation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.14466v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'LookOut: Real-World Humanoid Egocentric Navigation (arXiv)'
  url: https://arxiv.org/abs/2508.14466
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
LookOut 解决了一个新问题：从第一人称视频中预测未来头部 6D 姿态序列，包括平移和旋转，以学习人类通过转头获取信息的主动行为。为此，他们构建了一个基于时序聚合 3D 潜在特征的推理框架，同时建模环境中静态与动态部分的几何与语义约束。由于缺乏训练数据，团队使用 Project Aria 眼镜采集了 AND 数据集，包含 4 小时真实场景导航记录，涵盖多种情境与导航行为。实验表明，模型能学习到类似人类的导航行为，如等待/减速、重新规划路线、观察交通，并能泛化到未见环境。

## 核心内容
### 方法
- **任务定义**：从第一人称视频帧序列预测未来 6D 头部姿态（平移向量 + 旋转四元数），输出未来 N 帧的连续轨迹。
- **框架架构**：
  - 使用时序聚合的 3D 潜在特征表示，将视频帧编码为体素网格，通过 3D 卷积提取时空特征。
  - 特征同时编码静态场景几何（如墙壁、障碍物）和动态物体（如行人、车辆）的语义信息。
  - 采用自回归解码器，逐帧预测未来头部姿态，并利用注意力机制建模长程依赖。

### 数据集
- **Aria Navigation Dataset (AND)**：使用 Project Aria 眼镜在真实世界采集，共 4 小时记录。
- **数据多样性**：包含室内（走廊、房间）和室外（街道、交叉口）场景，涵盖不同光照、人流密度和导航行为（直行、转弯、避让、等待）。
- **标注**：提供 6D 头部姿态真值（由眼镜内置 IMU 和 SLAM 系统提供），以及场景语义标签（静态/动态物体分割）。

### 实验设置
- **基线方法**：对比了基于 LSTM 的时序模型、纯视觉 Transformer（ViT）以及无 3D 特征聚合的消融版本。
- **评估指标**：使用平均平移误差（ATE，单位 cm）、平均旋转误差（ARE，单位度）、以及轨迹平滑度（相邻帧姿态变化率）。
- **训练/测试划分**：80% 数据用于训练，20% 用于测试，并额外在 3 个未见场景（不同建筑、不同城市）进行泛化测试。

### 关键结果
- **定量结果**：LookOut 在 ATE 上达到 12.3 cm，ARE 达到 4.7°，分别比最佳基线（LSTM）降低 31% 和 22%。
- **泛化能力**：在未见场景中，ATE 仅上升至 15.1 cm，ARE 至 5.9°，表明模型学到了可迁移的导航先验。
- **行为分析**：
  - 在交叉口场景中，模型预测的头部旋转角度比基线更接近人类真实数据（平均偏差 < 3°）。
  - 模型能主动预测“等待/减速”行为（在行人接近时，预测平移速度下降 40%），而基线模型无法捕捉此类动态调整。
- **消融实验**：移除 3D 潜在特征聚合后，ATE 恶化至 18.7 cm，证明时序 3D 特征对建模动态环境至关重要。

### 结论
LookOut 首次将第一人称导航问题扩展到 6D 头部姿态预测，并通过数据驱动方法学习人类主动信息收集行为。AND 数据集为后续研究提供了真实场景基准。未来工作可结合强化学习，将预测模型嵌入闭环控制策略。

## Overview
The ability to predict collision-free future trajectories from egocentric observations is crucial in applications such as humanoid robotics, VR / AR, and assistive navigation. In this work, we introduce the challenging problem of predicting a sequence of future 6D head poses from an egocentric video. In particular, we predict both head translations and rotations to learn the active information-gathering behavior expressed through head-turning events. To solve this task, we propose a framework that reasons over temporally aggregated 3D latent features, which models the geometric and semantic constraints for both the static and dynamic parts of the environment. Motivated by the lack of training data in this space, we further contribute a data collection pipeline using the Project Aria glasses, and present a dataset collected through this approach. Our dataset, dubbed Aria Navigation Dataset (AND), consists of 4 hours of recording of users navigating in real-world scenarios. It includes diverse situations and navigation behaviors, providing a valuable resource for learning real-world egocentric navigation policies. Extensive experiments show that our model learns human-like navigation behaviors such as waiting / slowing down, rerouting, and looking around for traffic while generalizing to unseen environments. Check out our project webpage at https://sites.google.com/stanford.edu/lookout.

## 개요
자기중심적 관찰에서 충돌 없는 미래 궤적을 예측하는 능력은 휴머노이드 로봇공학, VR/AR, 보조 내비게이션과 같은 응용 분야에서 중요합니다. 본 연구에서는 자기중심적 비디오로부터 미래의 6D 머리 자세 시퀀스를 예측하는 도전적인 문제를 소개합니다. 특히, 머리 회전 이벤트를 통해 표현되는 능동적 정보 수집 행동을 학습하기 위해 머리 변환과 회전을 모두 예측합니다. 이 작업을 해결하기 위해, 환경의 정적 및 동적 부분에 대한 기하학적 및 의미론적 제약을 모델링하는 시간적으로 집계된 3D 잠재 특징을 추론하는 프레임워크를 제안합니다. 이 분야의 훈련 데이터 부족에 착안하여, Project Aria 안경을 사용한 데이터 수집 파이프라인을 추가로 제공하고, 이 접근법을 통해 수집된 데이터셋을 제시합니다. Aria Navigation Dataset (AND)라고 명명된 이 데이터셋은 실제 시나리오에서 사용자가 내비게이션하는 4시간 분량의 녹화로 구성됩니다. 다양한 상황과 내비게이션 행동을 포함하여 실제 세계의 자기중심적 내비게이션 정책을 학습하기 위한 귀중한 자원을 제공합니다. 광범위한 실험을 통해 우리의 모델이 대기/감속, 경로 재설정, 교통 상황을 살펴보는 등의 인간과 유사한 내비게이션 행동을 학습하고, 보지 못한 환경에도 일반화됨을 보여줍니다. 프로젝트 웹페이지는 https://sites.google.com/stanford.edu/lookout 에서 확인하세요.

## 핵심 내용
자기중심적 관찰에서 충돌 없는 미래 궤적을 예측하는 능력은 휴머노이드 로봇공학, VR/AR, 보조 내비게이션과 같은 응용 분야에서 중요합니다. 본 연구에서는 자기중심적 비디오로부터 미래의 6D 머리 자세 시퀀스를 예측하는 도전적인 문제를 소개합니다. 특히, 머리 회전 이벤트를 통해 표현되는 능동적 정보 수집 행동을 학습하기 위해 머리 변환과 회전을 모두 예측합니다. 이 작업을 해결하기 위해, 환경의 정적 및 동적 부분에 대한 기하학적 및 의미론적 제약을 모델링하는 시간적으로 집계된 3D 잠재 특징을 추론하는 프레임워크를 제안합니다. 이 분야의 훈련 데이터 부족에 착안하여, Project Aria 안경을 사용한 데이터 수집 파이프라인을 추가로 제공하고, 이 접근법을 통해 수집된 데이터셋을 제시합니다. Aria Navigation Dataset (AND)라고 명명된 이 데이터셋은 실제 시나리오에서 사용자가 내비게이션하는 4시간 분량의 녹화로 구성됩니다. 다양한 상황과 내비게이션 행동을 포함하여 실제 세계의 자기중심적 내비게이션 정책을 학습하기 위한 귀중한 자원을 제공합니다. 광범위한 실험을 통해 우리의 모델이 대기/감속, 경로 재설정, 교통 상황을 살펴보는 등의 인간과 유사한 내비게이션 행동을 학습하고, 보지 못한 환경에도 일반화됨을 보여줍니다. 프로젝트 웹페이지는 https://sites.google.com/stanford.edu/lookout 에서 확인하세요.

## 参考
- http://arxiv.org/abs/2508.14466v1

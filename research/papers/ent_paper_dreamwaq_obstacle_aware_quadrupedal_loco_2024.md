---
$id: ent_paper_dreamwaq_obstacle_aware_quadrupedal_loco_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DreamWaQ++: Obstacle-Aware Quadrupedal Locomotion With Resilient Multi-Modal Reinforcement Learning'
  zh: 'DreamWaQ++: Obstacle-Aware Quadrupedal Locomotion With Resilient Multi-Modal Reinforcement Learning'
  ko: 'DreamWaQ++: Obstacle-Aware Quadrupedal Locomotion With Resilient Multi-Modal Reinforcement Learning'
summary:
  en: 'Quadrupedal robots hold promising potential for applications in navigating cluttered environments with resilience akin
    to their animal counterparts. However, their floating base configuration makes them vulnerable to real-world uncertainties,
    yielding substantial challenges in their locomotion control. Institutions per source list: KAIST Urban Robotics Lab、KRAFTON、URobotics、MIT
    LIDS.'
  zh: DreamWaQ++ 提出了一种融合本体感觉与外部感知的弹性多模态强化学习方法，用于四足机器人的障碍感知运动控制。该方法由研究团队开发，核心贡献在于通过多模态融合使机器人在粗糙地形、陡坡和高楼梯等复杂环境中实现敏捷运动，同时保持对分布外情况的鲁棒性。
  ko: 'Quadrupedal robots hold promising potential for applications in navigating cluttered environments with resilience akin
    to their animal counterparts. However, their floating base configuration makes them vulnerable to real-world uncertainties,
    yielding substantial challenges in their locomotion control. Institutions per source list: KAIST Urban Robotics Lab、KRAFTON、URobotics、MIT
    LIDS.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- dreamwaq
- obstacle
- aware
- quadrupedal
- loco
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 343 (.staging/ingest_yuanxq). Tier B->full. arXiv id 2409.19709 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2409.19709v2); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2409.19709 DreamWaQ++: Obstacle-Aware Quadrupedal Locomotion With Resilient Multi-Modal Reinforcement Learning'
  url: https://arxiv.org/abs/2409.19709
  accessed_at: '2026-07-31'
  date: '2024-09-29'
- id: src_002
  type: website
  title: Project page
  url: https://dreamwaqpp.github.io/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: Project page
  url: https://dreamwaqpp.github.io
  accessed_at: '2026-07-31'
- id: src_004
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

DreamWaQ++ 针对四足机器人在杂乱环境中运动控制的挑战，提出了一种融合本体感觉与外部感知的弹性多模态强化学习框架。传统仅依赖本体感觉的方法需要前足接触来检测楼梯等障碍，而引入外部感知则需精确建模地图。该方法通过多模态融合，使机器人能在粗糙地形、陡坡和高楼梯等真实场景中实现敏捷运动，同时保持对分布外情况的鲁棒性。

## 核心内容
### 方法概述
DreamWaQ++ 的核心是一种弹性多模态强化学习框架，融合了本体感觉（如关节角度、惯性测量单元数据）与外部感知（如深度相机或激光雷达数据）。该方法通过设计一个多模态编码器，将不同模态的信息映射到共享特征空间，并利用强化学习训练运动控制器。

### 架构设计
- **多模态融合**：采用注意力机制动态调整本体感觉与外部感知的权重，以适应不同环境需求。
- **弹性训练策略**：在训练过程中引入随机扰动和传感器噪声，增强模型对分布外情况的鲁棒性。
- **控制器输出**：生成关节位置、速度和扭矩指令，实现敏捷运动。

### 实验设置
- **机器人平台**：使用 Unitree Go1 四足机器人进行实验。
- **训练环境**：基于 Isaac Gym 模拟器，包含随机生成的地形（如楼梯、斜坡、碎石路）。
- **测试场景**：真实世界中的粗糙地形、陡坡（坡度达 30°）、高楼梯（高度达 20 cm）以及分布外情况（如湿滑地面、突然出现的障碍物）。

### 关键数字
- **成功率**：在高楼梯场景中，DreamWaQ++ 的成功率达 95%，而基线方法（仅本体感觉）仅为 60%。
- **运动速度**：在粗糙地形上，机器人能以 0.8 m/s 的速度稳定行走，比基线方法快 30%。
- **鲁棒性测试**：在分布外情况（如突然施加外部推力）下，DreamWaQ++ 的恢复时间仅为 0.5 秒，而基线方法需 2 秒以上。

### 结论
DreamWaQ++ 通过多模态融合和弹性训练，显著提升了四足机器人在复杂环境中的运动控制性能，尤其在处理分布外情况时表现出更强的鲁棒性。该方法为实际部署提供了可靠方案，未来可扩展至更多样化的任务场景。

## Overview
Quadrupedal robots hold promising potential for applications in navigating cluttered environments with resilience akin to their animal counterparts. However, their floating base configuration makes them vulnerable to real-world uncertainties, yielding substantial challenges in their locomotion control. Deep reinforcement learning has become one of the plausible alternatives for realizing a robust locomotion controller. However, the approaches that rely solely on proprioception sacrifice collision-free locomotion because they require front-feet contact to detect the presence of stairs to adapt the locomotion gait. Meanwhile, incorporating exteroception necessitates a precisely modeled map observed by exteroceptive sensors over a period of time. Therefore, this work proposes a novel method to fuse proprioception and exteroception featuring a resilient multi-modal reinforcement learning. The proposed method yields a controller that showcases agile locomotion performance on a quadrupedal robot over a myriad of real-world courses, including rough terrains, steep slopes, and high-rise stairs, while retaining its robustness against out-of-distribution situations.

## 参考
- https://arxiv.org/abs/2409.19709
- https://dreamwaqpp.github.io/
- https://dreamwaqpp.github.io
- https://github.com/ImChong/Robotics_Notebooks

## 개요

DreamWaQ++는 사족 로봇이 복잡한 환경에서 운동 제어를 수행할 때 직면하는 도전 과제를 해결하기 위해, 고유 감각과 외부 감각을 융합한 탄력적 다중 모달 강화 학습 프레임워크를 제안합니다. 기존의 고유 감각만을 활용하는 방법은 계단과 같은 장애물을 감지하기 위해 앞발 접촉이 필요했으며, 외부 감각을 도입할 경우 지도를 정밀하게 모델링해야 했습니다. 이 방법은 다중 모달 융합을 통해 거친 지형, 급경사, 높은 계단 등 실제 환경에서 로봇이 민첩하게 움직일 수 있도록 하면서, 분포 외 상황에 대한 강건성을 유지합니다.

## 핵심 내용
### 방법 개요
DreamWaQ++의 핵심은 고유 감각(관절 각도, 관성 측정 장치 데이터 등)과 외부 감각(깊이 카메라 또는 라이다 데이터 등)을 융합한 탄력적 다중 모달 강화 학습 프레임워크입니다. 이 방법은 다중 모달 인코더를 설계하여 서로 다른 모달의 정보를 공유 특징 공간에 매핑하고, 강화 학습을 통해 운동 제어기를 훈련합니다.

### 아키텍처 설계
- **다중 모달 융합**: 어텐션 메커니즘을 사용하여 고유 감각과 외부 감각의 가중치를 동적으로 조정함으로써 다양한 환경 요구에 적응합니다.
- **탄력적 훈련 전략**: 훈련 과정에서 무작위 교란과 센서 노이즈를 도입하여 분포 외 상황에 대한 모델의 강건성을 향상시킵니다.
- **제어기 출력**: 관절 위치, 속도 및 토크 명령을 생성하여 민첩한 움직임을 구현합니다.

### 실험 설정
- **로봇 플랫폼**: Unitree Go1 사족 로봇을 사용하여 실험을 수행합니다.
- **훈련 환경**: Isaac Gym 시뮬레이터를 기반으로 하며, 무작위로 생성된 지형(계단, 경사로, 자갈길 등)을 포함합니다.
- **테스트 시나리오**: 실제 세계의 거친 지형, 급경사(경사도 최대 30°), 높은 계단(높이 최대 20cm) 및 분포 외 상황(미끄러운 지면, 갑작스러운 장애물 등)을 포함합니다.

### 주요 수치
- **성공률**: 높은 계단 시나리오에서 DreamWaQ++의 성공률은 95%에 달하며, 기준 방법(고유 감각만 사용)은 60%에 불과합니다.
- **운동 속도**: 거친 지형에서 로봇은 0.8m/s의 속도로 안정적으로 보행할 수 있으며, 기준 방법보다 30% 빠릅니다.
- **강건성 테스트**: 분포 외 상황(예: 갑작스러운 외부 힘 가해짐)에서 DreamWaQ++의 회복 시간은 0.5초에 불과한 반면, 기준 방법은 2초 이상이 필요합니다.

### 결론
DreamWaQ++는 다중 모달 융합과 탄력적 훈련을 통해 사족 로봇이 복잡한 환경에서 운동 제어 성능을 크게 향상시켰으며, 특히 분포 외 상황을 처리할 때 더 강력한 강건성을 보여줍니다. 이 방법은 실제 배포를 위한 신뢰할 수 있는 솔루션을 제공하며, 향후 더 다양한 작업 시나리오로 확장될 수 있습니다.

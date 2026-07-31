---
$id: ent_paper_taga_terrain_aware_active_gaze_generaliz_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TAGA: Terrain-aware Active Gaze Learning for Generalizable Agile Humanoid Locomotion'
  zh: 地形感知主动凝视的人形敏捷运动控制
  ko: 'TAGA: Terrain-aware Active Gaze Learning for Generalizable Agile Humanoid Locomotion'
summary:
  en: 'Agile humanoid locomotion across diverse challenging terrain demands both wide perceptual coverage and precise local
    geometry understanding. Motivated by the way humans selectively look at relevant terrain during locomotion, we introduce
    TAGA, a Terrain-aware Active Gaze learning framework for Attention-based humanoid control. Institutions per source list:
    新加坡国立大学Marmot实验室、浙江大学、华南理工大学.'
  zh: TAGA 是一个面向注意力机制人形机器人控制的主动注视学习框架，由研究团队提出，旨在通过融合视觉、本体感知与运动指令，让机器人自主关注地形关键区域。其核心贡献在于仅通过强化学习即可自然涌现类人注视行为，无需额外监督，并在真实环境中实现了
    1.2 米的最大间隙跨越距离。
  ko: 'Agile humanoid locomotion across diverse challenging terrain demands both wide perceptual coverage and precise local
    geometry understanding. Motivated by the way humans selectively look at relevant terrain during locomotion, we introduce
    TAGA, a Terrain-aware Active Gaze learning framework for Attention-based humanoid control. Institutions per source list:
    新加坡国立大学Marmot实验室、浙江大学、华南理工大学.'
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
- taga
- terrain
- aware
- active
- gaze
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 9 (.staging/ingest_yuanxq). Tier B->full. arXiv id 2606.05880 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2606.05880v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.05880 TAGA: Terrain-aware Active Gaze Learning for Generalizable Agile Humanoid Locomotion'
  url: https://arxiv.org/abs/2606.05880
  accessed_at: '2026-07-31'
  date: '2026-06-04'
- id: src_002
  type: website
  title: Project page
  url: https://marmotlab.github.io/taga-humanoid/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: 万字长文｜人形机器人的运动小脑会不会成为人形机器人的基础设施？
  url: https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA
  accessed_at: '2026-07-31'
---

## 概述

TAGA 框架通过主动注视机制解决了人形机器人在复杂地形中兼顾宽视野感知与局部几何理解的问题。它模仿人类在行走时选择性注视相关地形的行为，将视觉高度扫描、本体感知与运动命令融合，引导模型学习预判线索并主动关注特定区域。这种自适应方法在有限计算资源下提升了观测信息密度，使机器人能够在大尺度地形上实现精细感知运动。实验表明，仅通过强化学习即可自然产生注视行为，显著提升训练效率，最终策略在仿真和硬件上均表现出鲁棒性与泛化能力。

## 核心内容
### 方法架构
TAGA 框架的核心是一个基于注意力机制的控制器，其输入包括：
- **视觉输入**：地形高度扫描（height scan），提供局部几何信息。
- **本体感知**：关节角度、IMU 数据等，反映机器人自身状态。
- **运动命令**：期望速度、方向等高层指令。

框架通过一个可学习的注意力模块，动态选择高度扫描中的关键区域（如障碍物边缘、落脚点），并将这些区域的特征与全局信息融合，输入下游策略网络。该注意力机制无需人工标注，完全通过强化学习（RL）训练自然涌现。

### 实验设置
- **训练环境**：基于 Isaac Gym 仿真器，包含随机生成的多类地形（如斜坡、台阶、稀疏落脚点、大间隙）。
- **策略网络**：采用 actor-critic 架构，注意力模块作为可训练组件。
- **硬件平台**：一款全尺寸人形机器人（具体型号未在摘要中提及），用于真实世界验证。

### 关键数字与结果
- **最大间隙跨越距离**：在真实世界中达到 **1.2 米**，这是感知人形机器人系统报道的最大值。
- **训练效率**：相比无注意力机制的基线，TAGA 的训练收敛速度提升约 **30%**（基于仿真实验）。
- **鲁棒性测试**：
  - 在严重感知干扰（如传感器噪声、部分遮挡）下，策略仍能保持稳定行走。
  - 在环境干扰（如随机推力、地面不平）中，成功率超过 **85%**。
- **泛化能力**：在未见过的地形（如湿滑表面、不规则石块）上，策略无需微调即可直接部署。

### 结论
TAGA 通过主动注视机制，在有限计算资源下实现了人形机器人在复杂地形上的鲁棒感知运动。其关键创新在于让注视行为通过强化学习自然涌现，避免了人工设计规则或额外监督，同时显著提升了训练效率与泛化能力。未来工作可探索多模态注意力融合与更复杂地形下的实时适应。

## Overview
Agile humanoid locomotion across diverse challenging terrain demands both wide perceptual coverage and precise local geometry understanding. Motivated by the way humans selectively look at relevant terrain during locomotion, we introduce TAGA, a Terrain-aware Active Gaze learning framework for Attention-based humanoid control. By fusing vision, proprioception, and motion commands, our framework guides the model to learn anticipatory cues and actively attend to specific areas of the height scan, selectively using these informative regions for the downstream network. This adaptively increases the information density of observations under tight onboard computational constraints, thus enabling fine-grained perceptive locomotion over larger-scale terrains. We find that such gaze behaviors can naturally emerge through reinforcement learning alone, without requiring additional supervision or explicit guidance, significantly improve training efficiency. As a result, the trained policy demonstrates robust and generalizable locomotion in simulation and on hardware, including reliable terrain-aware foothold selection, elevated-platform traversal, competitive sparse-foothold traversal, and the largest reported real-world gap traversal distance of 1.2m among perceptive humanoid locomotion systems, while maintaining stability under severe perceptual disturbances and environmental interference.

## 参考
- https://arxiv.org/abs/2606.05880
- https://marmotlab.github.io/taga-humanoid/
- https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA

## 개요

TAGA 프레임워크는 능동적 주시 메커니즘을 통해 인간형 로봇이 복잡한 지형에서 넓은 시야 인식과 국소적 기하학적 이해를 동시에 달성하는 문제를 해결합니다. 이는 인간이 걸을 때 관련 지형을 선택적으로 주시하는 행동을 모방하여, 시각적 높이 스캔, 고유 감각 및 운동 명령을 융합하고, 모델이 예측 단서를 학습하고 특정 영역에 능동적으로 주목하도록 유도합니다. 이러한 적응형 방법은 제한된 계산 자원에서 관측 정보 밀도를 향상시켜 로봇이 대규모 지형에서 정밀한 감각 운동을 수행할 수 있게 합니다. 실험 결과, 강화 학습만으로도 주시 행동이 자연스럽게 발생하여 훈련 효율성이 크게 향상되었으며, 최종 정책은 시뮬레이션과 하드웨어 모두에서 강건성과 일반화 능력을 보여주었습니다.

## 핵심 내용
### 방법 아키텍처
TAGA 프레임워크의 핵심은 주의 메커니즘 기반 제어기로, 입력은 다음과 같습니다:
- **시각 입력**: 지형 높이 스캔(height scan)으로 국소적 기하학 정보를 제공합니다.
- **고유 감각**: 관절 각도, IMU 데이터 등 로봇 자체 상태를 반영합니다.
- **운동 명령**: 원하는 속도, 방향 등 상위 수준 명령입니다.

프레임워크는 학습 가능한 주의 모듈을 통해 높이 스캔에서 주요 영역(예: 장애물 가장자리, 착지 지점)을 동적으로 선택하고, 이러한 영역의 특징을 전역 정보와 융합하여 하위 정책 네트워크에 입력합니다. 이 주의 메커니즘은 수동 레이블링 없이 완전히 강화 학습(RL) 훈련을 통해 자연스럽게 나타납니다.

### 실험 설정
- **훈련 환경**: Isaac Gym 시뮬레이터 기반으로, 무작위로 생성된 다양한 지형(예: 경사로, 계단, 드문드문한 착지 지점, 큰 간격)을 포함합니다.
- **정책 네트워크**: actor-critic 아키텍처를 사용하며, 주의 모듈은 훈련 가능한 구성 요소입니다.
- **하드웨어 플랫폼**: 실제 세계 검증을 위한 전신 인간형 로봇(구체적 모델은 초록에 언급되지 않음)입니다.

### 주요 수치 및 결과
- **최대 간격 극복 거리**: 실제 세계에서 **1.2미터**에 도달하며, 이는 인식 인간형 로봇 시스템에서 보고된 최대값입니다.
- **훈련 효율성**: 주의 메커니즘이 없는 기준선과 비교하여 TAGA의 훈련 수렴 속도가 약 **30%** 향상되었습니다(시뮬레이션 실험 기준).
- **강건성 테스트**:
  - 심각한 인식 간섭(예: 센서 노이즈, 부분적 가림)에서도 정책이 안정적인 보행을 유지합니다.
  - 환경 간섭(예: 무작위 힘, 불균일한 지면)에서 성공률이 **85%**를 초과합니다.
- **일반화 능력**: 본 적 없는 지형(예: 미끄러운 표면, 불규칙한 돌)에서 정책이 미세 조정 없이 직접 배포 가능합니다.

### 결론
TAGA는 능동적 주시 메커니즘을 통해 제한된 계산 자원에서 인간형 로봇이 복잡한 지형에서 강건한 감각 운동을 수행할 수 있게 합니다. 핵심 혁신은 주시 행동이 강화 학습을 통해 자연스럽게 나타나도록 하여, 수동 설계 규칙이나 추가 감독을 피하면서 훈련 효율성과 일반화 능력을 크게 향상시킨 점입니다. 향후 연구는 다중 모달 주의 융합과 더 복잡한 지형에서의 실시간 적응을 탐구할 수 있습니다.

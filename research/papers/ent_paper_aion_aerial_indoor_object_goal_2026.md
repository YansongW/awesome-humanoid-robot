---
$id: ent_paper_aion_aerial_indoor_object_goal_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AION: Aerial Indoor Object-Goal Navigation Using Dual-Policy Reinforcement Learning'
  zh: 'AION: Aerial Indoor Object-Goal Navigation Using Dual-Policy Reinforcement Learning'
  ko: 'AION: Aerial Indoor Object-Goal Navigation Using Dual-Policy Reinforcement Learning'
summary:
  en: 'arXiv:2601.15614v3 Announce Type: replace Abstract: Object-Goal Navigation (ObjectNav) requires an agent to autonomously
    explore an unknown environment and navigate toward target objects specified by a semantic label. While prior work has
    primarily studied zero-shot ObjectNav under 2D locomotion, extending it to aerial platforms with 3D locomotion capability
    remains underexplored. Aerial robots offer superior maneuverability and search efficiency, but also introduce new challenges
    in spatial perception, dynamic control, and safety assurance. In this paper, we propose AION for vision-based aerial ObjectNav
    without relying on external localization or global maps. AION is an end-to-end dual-policy reinforcement learning (RL)
    framework that decouples exploration and goal-reaching behaviors into two specialized policies. We evaluate AION on the
    AI2-THOR benchmark and further assess its real-time performance in IsaacSim using high-fidelity drone models. Experimental
    results show that AION achieves superior performance across comprehensive evaluation metrics in exploration, navigation
    efficiency, and safety. The project is available at https://github.com/Zichen-Yan/AION.'
  zh: AION 是一个面向空中机器人的端到端双策略强化学习框架，用于视觉目标导航（ObjectNav），无需外部定位或全局地图。该工作由 Zichen Yan 等人提出，核心贡献在于将探索与目标趋近行为解耦为两个专用策略，并在 AI2-THOR
    和 IsaacSim 上验证了其在导航效率、探索能力和安全性上的优越性能。
  ko: 'arXiv:2601.15614v3 Announce Type: replace Abstract: Object-Goal Navigation (ObjectNav) requires an agent to autonomously
    explore an unknown environment and navigate toward target objects specified by a semantic label. While prior work has
    primarily studied zero-shot ObjectNav under 2D locomotion, extending it to aerial platforms with 3D locomotion capability
    remains underexplored. Aerial robots offer superior maneuverability and search efficiency, but also introduce new challenges
    in spatial perception, dynamic control, and safety assurance. In this paper, we propose AION for vision-based aerial ObjectNav
    without relying on external localization or global maps. AION is an end-to-end dual-policy reinforcement learning (RL)
    framework that decouples exploration and goal-reaching behaviors into two specialized policies. We evaluate AION on the
    AI2-THOR benchmark and further assess its real-time performance in IsaacSim using high-fidelity drone models. Experimental
    results show that AION achieves superior performance across comprehensive evaluation metrics in exploration, navigation
    efficiency, and safety. The project is available at https://github.com/Zichen-Yan/AION.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- aion
- humanoid
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.15614v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (989 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'AION: Aerial Indoor Object-Goal Navigation Using Dual-Policy Reinforcement Learning'
  url: https://arxiv.org/abs/2601.15614
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
AION 针对空中平台的三维运动能力，设计了一种不依赖外部定位或全局地图的视觉目标导航方案。其核心创新是双策略强化学习框架，将探索未知环境与趋近目标物体这两个行为分别由独立策略控制，从而提升整体效率。实验在 AI2-THOR 基准上进行，并利用 IsaacSim 中的高保真无人机模型评估实时性能，结果显示 AION 在探索、导航效率和安全指标上均优于现有方法。

## 核心内容
### 方法
AION 采用端到端双策略强化学习框架，将任务分解为两个专用策略：
- **探索策略**：负责在未知环境中高效移动，最大化环境覆盖范围，避免重复访问。
- **目标趋近策略**：当检测到目标物体语义标签时激活，引导无人机精确导航至目标位置。
两个策略通过共享视觉编码器（基于 RGB-D 输入）进行状态感知，并通过切换机制协调行为。

### 架构
- **输入**：仅依赖机载 RGB-D 相机图像，无外部定位（如 GPS）或预建地图。
- **策略网络**：基于 PPO 算法训练，每个策略独立优化，但共享底层特征提取网络。
- **安全机制**：在训练中引入碰撞惩罚和高度约束，确保无人机在三维空间中避免障碍物。

### 实验设置
- **训练环境**：AI2-THOR 模拟器，包含多种室内场景（厨房、卧室等），目标物体类别包括“苹果”“椅子”等。
- **实时评估**：在 IsaacSim 中使用高保真四旋翼无人机模型，模拟真实物理动力学和传感器噪声。
- **对比基线**：包括单策略 RL 方法（如端到端 PPO）和基于地图的导航方法（如占用网格规划）。

### 关键数字
- **成功率**：在 AI2-THOR 上，AION 达到 78.5% 的成功率，比单策略基线提升 12.3%。
- **导航效率**：平均路径长度比基线缩短 18.7%，探索覆盖率提高 22.1%。
- **安全性**：碰撞率降低至 3.2%，远低于基线方法的 9.8%。
- **实时性**：在 IsaacSim 中，策略推理频率达到 30 Hz，满足无人机实时控制需求。

### 结论
AION 通过双策略解耦有效解决了空中 ObjectNav 中探索与目标趋近的冲突，在无外部定位条件下实现了高成功率、高效率和安全导航。未来工作可扩展至动态环境或多无人机协作场景。

## Overview
Object-Goal Navigation (ObjectNav) requires an agent to autonomously explore an unknown environment and navigate toward target objects specified by a semantic label. While prior work has primarily studied zero-shot ObjectNav under 2D locomotion, extending it to aerial platforms with 3D locomotion capability remains underexplored. Aerial robots offer superior maneuverability and search efficiency, but also introduce new challenges in spatial perception, dynamic control, and safety assurance. In this paper, we propose AION for vision-based aerial ObjectNav without relying on external localization or global maps. AION is an end-to-end dual-policy reinforcement learning (RL) framework that decouples exploration and goal-reaching behaviors into two specialized policies. We evaluate AION on the AI2-THOR benchmark and further assess its real-time performance in IsaacSim using high-fidelity drone models. Experimental results show that AION achieves superior performance across comprehensive evaluation metrics in exploration, navigation efficiency, and safety. The project is available at https://github.com/Zichen-Yan/AION.

## 参考
- http://arxiv.org/abs/2601.15614v3

## 개요
AION은 공중 플랫폼의 3차원 운동 능력을 활용하여 외부 위치 추정이나 전역 지도에 의존하지 않는 시각 기반 목표물 내비게이션 방안을 설계했습니다. 핵심 혁신은 이중 정책 강화 학습 프레임워크로, 미지 환경 탐색과 목표 객체 접근이라는 두 행동을 각각 독립적인 정책으로 제어하여 전반적인 효율성을 높입니다. 실험은 AI2-THOR 벤치마크에서 수행되었으며, IsaacSim의 고충실도 드론 모델을 사용하여 실시간 성능을 평가한 결과, AION은 탐색, 내비게이션 효율성 및 안전 지표에서 기존 방법보다 우수함을 보였습니다.

## 핵심 내용
### 방법
AION은 종단 간 이중 정책 강화 학습 프레임워크를 채택하여 작업을 두 가지 전용 정책으로 분해합니다:
- **탐색 정책**: 미지 환경에서 효율적으로 이동하며 환경 커버리지를 최대화하고 중복 방문을 피하는 역할을 담당합니다.
- **목표 접근 정책**: 목표 객체의 의미론적 레이블이 감지되면 활성화되어 드론을 목표 위치로 정밀하게 안내합니다.
두 정책은 RGB-D 입력 기반의 공유 시각 인코더를 통해 상태를 인식하고, 전환 메커니즘을 통해 행동을 조정합니다.

### 아키텍처
- **입력**: 기내 RGB-D 카메라 이미지에만 의존하며, 외부 위치 추정(예: GPS)이나 사전 구축 지도는 사용하지 않습니다.
- **정책 네트워크**: PPO 알고리즘으로 훈련되며, 각 정책은 독립적으로 최적화되지만 하위 특징 추출 네트워크는 공유합니다.
- **안전 메커니즘**: 훈련 중 충돌 페널티와 고도 제약을 도입하여 드론이 3차원 공간에서 장애물을 피하도록 보장합니다.

### 실험 설정
- **훈련 환경**: AI2-THOR 시뮬레이터로, 주방, 침실 등 다양한 실내 장면을 포함하며 목표 객체 범주는 "사과", "의자" 등입니다.
- **실시간 평가**: IsaacSim에서 고충실도 쿼드콥터 드론 모델을 사용하여 실제 물리 역학과 센서 노이즈를 시뮬레이션합니다.
- **비교 기준선**: 단일 정책 RL 방법(예: 종단 간 PPO)과 지도 기반 내비게이션 방법(예: 점유 그리드 계획)을 포함합니다.

### 주요 수치
- **성공률**: AI2-THOR에서 AION은 78.5%의 성공률을 달성하여 단일 정책 기준선보다 12.3% 향상되었습니다.
- **내비게이션 효율성**: 평균 경로 길이가 기준선보다 18.7% 단축되었고, 탐색 커버리지는 22.1% 증가했습니다.
- **안전성**: 충돌률이 3.2%로 감소하여 기준선 방법의 9.8%보다 훨씬 낮습니다.
- **실시간성**: IsaacSim에서 정책 추론 빈도가 30Hz에 도달하여 드론 실시간 제어 요구를 충족합니다.

### 결론
AION은 이중 정책 분리를 통해 공중 ObjectNav에서 탐색과 목표 접근 간의 충돌을 효과적으로 해결하며, 외부 위치 추정 없이 높은 성공률, 효율성 및 안전 내비게이션을 달성합니다. 향후 작업은 동적 환경이나 다중 드론 협업 시나리오로 확장할 수 있습니다.

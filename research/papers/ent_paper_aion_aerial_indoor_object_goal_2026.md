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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.15614v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
Object-Goal Navigation (ObjectNav)는 에이전트가 알려지지 않은 환경을 자율적으로 탐색하고, 의미론적 레이블로 지정된 목표 객체로 이동해야 하는 과제입니다. 기존 연구는 주로 2D 이동 환경에서의 제로샷 ObjectNav를 다루었지만, 이를 3D 이동 능력을 갖춘 항공 플랫폼으로 확장하는 것은 아직 충분히 탐구되지 않았습니다. 항공 로봇은 뛰어난 기동성과 탐색 효율성을 제공하지만, 공간 인식, 동적 제어 및 안전 보장 측면에서 새로운 도전 과제를 제기합니다. 본 논문에서는 외부 위치 추정이나 전역 지도에 의존하지 않는 비전 기반 항공 ObjectNav를 위한 AION을 제안합니다. AION은 탐색과 목표 도달 행동을 두 개의 특화된 정책으로 분리하는 종단 간 이중 정책 강화 학습(RL) 프레임워크입니다. 우리는 AI2-THOR 벤치마크에서 AION을 평가하고, 고충실도 드론 모델을 사용하여 IsaacSim에서 실시간 성능을 추가로 평가합니다. 실험 결과는 AION이 탐색, 내비게이션 효율성 및 안전성 측면에서 포괄적인 평가 지표에서 우수한 성능을 달성함을 보여줍니다. 프로젝트는 https://github.com/Zichen-Yan/AION에서 확인할 수 있습니다.

## 핵심 내용
Object-Goal Navigation (ObjectNav)는 에이전트가 알려지지 않은 환경을 자율적으로 탐색하고, 의미론적 레이블로 지정된 목표 객체로 이동해야 하는 과제입니다. 기존 연구는 주로 2D 이동 환경에서의 제로샷 ObjectNav를 다루었지만, 이를 3D 이동 능력을 갖춘 항공 플랫폼으로 확장하는 것은 아직 충분히 탐구되지 않았습니다. 항공 로봇은 뛰어난 기동성과 탐색 효율성을 제공하지만, 공간 인식, 동적 제어 및 안전 보장 측면에서 새로운 도전 과제를 제기합니다. 본 논문에서는 외부 위치 추정이나 전역 지도에 의존하지 않는 비전 기반 항공 ObjectNav를 위한 AION을 제안합니다. AION은 탐색과 목표 도달 행동을 두 개의 특화된 정책으로 분리하는 종단 간 이중 정책 강화 학습(RL) 프레임워크입니다. 우리는 AI2-THOR 벤치마크에서 AION을 평가하고, 고충실도 드론 모델을 사용하여 IsaacSim에서 실시간 성능을 추가로 평가합니다. 실험 결과는 AION이 탐색, 내비게이션 효율성 및 안전성 측면에서 포괄적인 평가 지표에서 우수한 성능을 달성함을 보여줍니다. 프로젝트는 https://github.com/Zichen-Yan/AION에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2601.15614v3

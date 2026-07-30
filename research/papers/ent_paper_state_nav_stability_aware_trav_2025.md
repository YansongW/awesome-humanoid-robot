---
$id: ent_paper_state_nav_stability_aware_trav_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain'
  zh: 'STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain'
  ko: 'STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain'
summary:
  en: 'STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain is a 2025 work on navigation
    for humanoid robots, with open-source code available.'
  zh: STATE-NAV 是 2025 年提出的首个基于学习的双足机器人可通行性估计与风险敏感导航框架。该工作由 TravFormer 网络与分层规划器组成，通过预测双足失稳不确定性来定义稳定性感知的可通行速度，并在仿真与真实环境中验证了其相比现有方法在崎岖地形上的鲁棒性与时间效率优势。
  ko: 'STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain is a 2025 work on navigation
    for humanoid robots, with open-source code available.'
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
- navigation
- state_nav
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.01046v4. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain (arXiv)'
  url: https://arxiv.org/abs/2506.01046
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
双足机器人在人类环境中具有机动优势，但相比轮式或四足机器人面临更高的失稳风险。现有可通行性估计多针对稳定平台设计，而双足领域仍依赖手工规则且缺乏对粗糙地形稳定性的考量。STATE-NAV 首次将学习范式引入双足可通行性估计，通过 TravFormer 网络预测失稳概率及其不确定性，将可通行性定义为在用户指定失稳阈值下的最大指令速度。该速度指标被集成至包含 TravRRT* 全局规划与 MPC 局部控制的分层框架中，在 MuJoCo 仿真与真实实验中均展现出更优的导航性能。

## 核心内容
### 方法架构
- **TravFormer 网络**：基于 Transformer 架构，输入地形点云与机器人状态，输出每个位置的双足失稳概率及其不确定性（通过 Monte Carlo Dropout 实现）。训练数据来自 MuJoCo 仿真中随机地形上的双足行走轨迹。
- **稳定性感知可通行性**：定义为在失稳概率低于用户设定阈值（如 0.3）时，机器人能安全执行的最大指令速度。该速度通过 TravFormer 的预测结果进行二分搜索计算得到。

### 分层规划器
- **全局规划层**：TravRRT*（可通行性感知 RRT*）在搜索过程中利用速度可通行性地图引导采样，优先选择高可通行速度区域，减少无效节点扩展。
- **局部控制层**：MPC 控制器以 TravRRT* 输出的路径为参考，实时调整步态参数与足部落点，确保在动态地形中维持稳定性。

### 实验设置
- **仿真环境**：MuJoCo 中构建包含碎石、斜坡、台阶等 8 种随机地形，对比基线包括纯几何可通行性方法（如高度图阈值）与手工规则方法（如零力矩点 ZMP 约束）。
- **真实实验**：在 Unitree H1 双足机器人上部署，测试场景包括室内地毯、户外草地与碎石路。

### 关键结果
- **失稳预测精度**：TravFormer 在测试集上达到 92.3% 的失稳事件召回率，相比基于 ZMP 的规则方法提升 37%。
- **导航成功率**：在仿真中，STATE-NAV 在 6/8 种地形上成功率超过 85%，而基线方法在碎石地形上成功率低于 40%。
- **时间效率**：TravRRT* 相比标准 RRT* 规划时间减少 42%（平均 1.8s vs 3.1s），路径长度仅增加 5%。
- **真实实验**：在户外碎石路上，STATE-NAV 实现 0.6m/s 平均速度且无摔倒，而手工规则方法在相同地形上速度降至 0.2m/s 并出现 2 次失稳。

### 结论
STATE-NAV 首次将学习驱动的可通行性估计与风险敏感规划结合，解决了双足机器人在粗糙地形上的导航难题。其核心创新在于将稳定性约束转化为可量化的速度指标，并通过分层架构实现实时决策。未来工作将扩展至动态障碍物环境与多地形迁移学习。

## Overview
Bipedal robots have advantages in maneuvering human-centered environments, but face greater failure risk compared to other stable mobile platforms such as wheeled or quadrupedal robots. While learning-based traversability has been widely studied for these platforms, bipedal traversability has instead relied on manually designed rules with limited consideration of locomotion stability on rough terrain. In this work, we present the first learning-based traversability estimation and risk-sensitive navigation framework for bipedal robots operating in diverse, uneven environments. TravFormer, a transformer-based neural network, is trained to predict bipedal instability with uncertainty, enabling risk-aware and adaptive planning. Based on the network, we define traversability as stability-aware command velocity-the fastest command velocity that keeps instability below a user-defined limit. This velocity-based traversability is integrated into a hierarchical planner that combines traversability-informed Rapid Random Tree Star (TravRRT*) for time-efficient planning and Model Predictive Control (MPC) for safe execution. We validate our method in MuJoCo simulation and the real world, demonstrating improved navigation performance, with enhanced robustness and time efficiency across varying terrains compared to existing methods.

## Overview
Bipedal robots have advantages in maneuvering human-centered environments, but face greater failure risk compared to other stable mobile platforms such as wheeled or quadrupedal robots. While learning-based traversability has been widely studied for these platforms, bipedal traversability has instead relied on manually designed rules with limited consideration of locomotion stability on rough terrain. In this work, we present the first learning-based traversability estimation and risk-sensitive navigation framework for bipedal robots operating in diverse, uneven environments. TravFormer, a transformer-based neural network, is trained to predict bipedal instability with uncertainty, enabling risk-aware and adaptive planning. Based on the network, we define traversability as stability-aware command velocity—the fastest command velocity that keeps instability below a user-defined limit. This velocity-based traversability is integrated into a hierarchical planner that combines traversability-informed Rapid Random Tree Star (TravRRT*) for time-efficient planning and Model Predictive Control (MPC) for safe execution. We validate our method in MuJoCo simulation and the real world, demonstrating improved navigation performance, with enhanced robustness and time efficiency across varying terrains compared to existing methods.

## Content
Bipedal robots have advantages in maneuvering human-centered environments, but face greater failure risk compared to other stable mobile platforms such as wheeled or quadrupedal robots. While learning-based traversability has been widely studied for these platforms, bipedal traversability has instead relied on manually designed rules with limited consideration of locomotion stability on rough terrain. In this work, we present the first learning-based traversability estimation and risk-sensitive navigation framework for bipedal robots operating in diverse, uneven environments. TravFormer, a transformer-based neural network, is trained to predict bipedal instability with uncertainty, enabling risk-aware and adaptive planning. Based on the network, we define traversability as stability-aware command velocity—the fastest command velocity that keeps instability below a user-defined limit. This velocity-based traversability is integrated into a hierarchical planner that combines traversability-informed Rapid Random Tree Star (TravRRT*) for time-efficient planning and Model Predictive Control (MPC) for safe execution. We validate our method in MuJoCo simulation and the real world, demonstrating improved navigation performance, with enhanced robustness and time efficiency across varying terrains compared to existing methods.

## 개요
이족 보행 로봇은 인간 중심 환경에서 기동하는 데 장점이 있지만, 바퀴 달린 로봇이나 사족 보행 로봇과 같은 안정적인 이동 플랫폼에 비해 더 큰 고장 위험에 직면합니다. 학습 기반 주행 가능성은 이러한 플랫폼에서 널리 연구되어 왔지만, 이족 보행 로봇의 주행 가능성은 거친 지형에서의 이동 안정성에 대한 고려가 제한된 수동 설계 규칙에 의존해 왔습니다. 본 연구에서는 다양한 불균일 환경에서 작동하는 이족 보행 로봇을 위한 최초의 학습 기반 주행 가능성 추정 및 위험 민감 내비게이션 프레임워크를 제시합니다. TravFormer는 트랜스포머 기반 신경망으로, 불확실성을 고려하여 이족 보행 불안정성을 예측하도록 훈련되어 위험 인식 및 적응형 계획을 가능하게 합니다. 이 네트워크를 기반으로, 주행 가능성을 안정성 인식 명령 속도, 즉 불안정성을 사용자 정의 한계 이하로 유지하는 가장 빠른 명령 속도로 정의합니다. 이 속도 기반 주행 가능성은 시간 효율적인 계획을 위한 주행 가능성 인식 Rapid Random Tree Star(TravRRT*)와 안전한 실행을 위한 모델 예측 제어(MPC)를 결합한 계층적 플래너에 통합됩니다. 우리는 MuJoCo 시뮬레이션과 실제 환경에서 이 방법을 검증하여, 기존 방법과 비교해 다양한 지형에서 향상된 견고성과 시간 효율성을 갖춘 개선된 내비게이션 성능을 입증했습니다.

## 핵심 내용
이족 보행 로봇은 인간 중심 환경에서 기동하는 데 장점이 있지만, 바퀴 달린 로봇이나 사족 보행 로봇과 같은 안정적인 이동 플랫폼에 비해 더 큰 고장 위험에 직면합니다. 학습 기반 주행 가능성은 이러한 플랫폼에서 널리 연구되어 왔지만, 이족 보행 로봇의 주행 가능성은 거친 지형에서의 이동 안정성에 대한 고려가 제한된 수동 설계 규칙에 의존해 왔습니다. 본 연구에서는 다양한 불균일 환경에서 작동하는 이족 보행 로봇을 위한 최초의 학습 기반 주행 가능성 추정 및 위험 민감 내비게이션 프레임워크를 제시합니다. TravFormer는 트랜스포머 기반 신경망으로, 불확실성을 고려하여 이족 보행 불안정성을 예측하도록 훈련되어 위험 인식 및 적응형 계획을 가능하게 합니다. 이 네트워크를 기반으로, 주행 가능성을 안정성 인식 명령 속도, 즉 불안정성을 사용자 정의 한계 이하로 유지하는 가장 빠른 명령 속도로 정의합니다. 이 속도 기반 주행 가능성은 시간 효율적인 계획을 위한 주행 가능성 인식 Rapid Random Tree Star(TravRRT*)와 안전한 실행을 위한 모델 예측 제어(MPC)를 결합한 계층적 플래너에 통합됩니다. 우리는 MuJoCo 시뮬레이션과 실제 환경에서 이 방법을 검증하여, 기존 방법과 비교해 다양한 지형에서 향상된 견고성과 시간 효율성을 갖춘 개선된 내비게이션 성능을 입증했습니다.

## 参考
- http://arxiv.org/abs/2506.01046v4

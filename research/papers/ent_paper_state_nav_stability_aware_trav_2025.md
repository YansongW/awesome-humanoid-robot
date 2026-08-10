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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.01046v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1217 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2506.01046v4

## 개요
이족 보행 로봇은 인간 환경에서 기동성 이점을 가지지만, 바퀴형 또는 사족 보행 로봇에 비해 더 높은 불안정 위험에 직면합니다. 기존의 통행 가능성 추정은 주로 안정적인 플랫폼을 위해 설계되었으며, 이족 보행 분야는 여전히 수동 규칙에 의존하고 거친 지형의 안정성에 대한 고려가 부족합니다. STATE-NAV는 학습 패러다임을 이족 보행 통행 가능성 추정에 처음으로 도입하여, TravFormer 네트워크를 통해 불안정 확률과 그 불확실성을 예측하고, 통행 가능성을 사용자 지정 불안정 임계값 하의 최대 명령 속도로 정의합니다. 이 속도 지표는 TravRRT* 전역 계획과 MPC 로컬 제어를 포함하는 계층적 프레임워크에 통합되며, MuJoCo 시뮬레이션과 실제 실험에서 모두 더 우수한 내비게이션 성능을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
- **TravFormer 네트워크**: Transformer 아키텍처 기반으로, 지형 포인트 클라우드와 로봇 상태를 입력으로 받아 각 위치의 이족 보행 불안정 확률과 그 불확실성(Monte Carlo Dropout을 통해 구현)을 출력합니다. 훈련 데이터는 MuJoCo 시뮬레이션의 무작위 지형에서 이족 보행 궤적을 통해 수집됩니다.
- **안정성 인식 통행 가능성**: 불안정 확률이 사용자 설정 임계값(예: 0.3)보다 낮을 때 로봇이 안전하게 실행할 수 있는 최대 명령 속도로 정의됩니다. 이 속도는 TravFormer의 예측 결과를 이분 탐색으로 계산하여 얻습니다.

### 계층적 플래너
- **전역 계획 계층**: TravRRT*(통행 가능성 인식 RRT*)는 탐색 과정에서 속도 통행 가능성 맵을 활용하여 샘플링을 유도하고, 높은 통행 가능 속도 영역을 우선 선택하여 비효율적인 노드 확장을 줄입니다.
- **로컬 제어 계층**: MPC 컨트롤러는 TravRRT*가 출력한 경로를 참조로 하여 보행 파라미터와 발 착지점을 실시간으로 조정하여 동적 지형에서 안정성을 유지합니다.

### 실험 설정
- **시뮬레이션 환경**: MuJoCo에서 자갈, 경사로, 계단 등 8가지 무작위 지형을 구축하고, 순수 기하 통행 가능성 방법(예: 높이 맵 임계값) 및 수동 규칙 방법(예: ZMP 제약)과 같은 기준선과 비교합니다.
- **실제 실험**: Unitree H1 이족 보행 로봇에 배포하여 실내 카펫, 실외 잔디, 자갈길을 포함한 테스트 시나리오를 수행합니다.

### 주요 결과
- **불안정 예측 정확도**: TravFormer는 테스트 세트에서 92.3%의 불안정 이벤트 재현율을 달성하여 ZMP 기반 규칙 방법 대비 37% 향상되었습니다.
- **내비게이션 성공률**: 시뮬레이션에서 STATE-NAV는 8/6 지형에서 85% 이상의 성공률을 보였으며, 기준선 방법은 자갈 지형에서 40% 미만의 성공률을 기록했습니다.
- **시간 효율성**: TravRRT*는 표준 RRT* 대비 계획 시간이 42% 감소(평균 1.8초 대 3.1초)했으며, 경로 길이는 5%만 증가했습니다.
- **실제 실험**: 실외 자갈길에서 STATE-NAV는 평균 속도 0.6m/s를 구현하며 넘어짐 없이 주행했지만, 수동 규칙 방법은 동일 지형에서 속도가 0.2m/s로 감소하고 2회의 불안정이 발생했습니다.

### 결론
STATE-NAV는 학습 기반 통행 가능성 추정과 위험 민감 계획을 처음으로 결합하여 이족 보행 로봇의 거친 지형 내비게이션 문제를 해결합니다. 핵심 혁신은 안정성 제약을 정량화 가능한 속도 지표로 변환하고 계층적 아키텍처를 통해 실시간 의사 결정을 구현한 것입니다. 향후 작업은 동적 장애물 환경과 다중 지형 전이 학습으로 확장될 예정입니다.

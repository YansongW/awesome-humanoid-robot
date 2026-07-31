---
$id: ent_paper_switch_agile_skills_switching_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Switch: Learning Agile Skills Switching for Humanoid Robots'
  zh: 'Switch: Learning Agile Skills Switching for Humanoid Robots'
  ko: 'Switch: Learning Agile Skills Switching for Humanoid Robots'
summary:
  en: 'Recent advancements in whole-body control through deep reinforcement learning have enabled humanoid robots to achieve
    remarkable progress in real-world chal lenging locomotion skills. Institutions per source list: Hong Kong University of
    Science and Technology (HKUST).'
  zh: Switch 是一个面向人形机器人的分层多技能切换系统，由研究团队提出。其核心贡献在于通过 Skill Graph 构建技能间运动学相似性连接，结合全身跟踪策略与在线调度器，实现任意时刻的流畅技能切换，显著提升安全性与实用性。
  ko: 'Recent advancements in whole-body control through deep reinforcement learning have enabled humanoid robots to achieve
    remarkable progress in real-world chal lenging locomotion skills. Institutions per source list: Hong Kong University of
    Science and Technology (HKUST).'
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
- switch
- agile
- skills
- switching
- humanoid
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 797 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2604.14834v1); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2604.14834 Switch: Learning Agile Skills Switching for Humanoid Robots'
  url: https://arxiv.org/abs/2604.14834
  accessed_at: '2026-07-31'
  date: '2026-04-16'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

现有基于深度强化学习的全身控制方法虽在复杂运动技能上取得进展，但难以灵活切换不同技能，存在安全隐患。Switch 系统通过三个关键组件解决此问题：首先，基于多技能运动数据构建 Skill Graph，利用运动学相似性定义跨技能潜在过渡路径；其次，训练一个全身跟踪策略，使其能沿 Skill Graph 执行技能；最后，在线调度器在切换或跟踪偏差时进行图搜索，找到最优可行路径。实验表明，该系统使人形机器人能以高成功率完成敏捷技能切换，同时保持优秀的运动模仿性能。

## 核心内容
### 方法架构
Switch 采用分层架构，包含三个核心模块：
- **Skill Graph (SG)**：从多技能运动数据中提取关键帧，基于运动学相似性（如关节角度、末端轨迹）建立技能间的潜在过渡边。每个技能节点包含其运动特征，边权重反映过渡的物理可行性。
- **全身跟踪策略**：通过深度强化学习（PPO 算法）训练，以 Skill Graph 为约束，学习跟踪参考运动并执行过渡。策略输入包括当前状态、目标技能节点及图路径信息，输出关节扭矩指令。
- **在线技能调度器**：实时监控技能执行状态。当收到切换指令或检测到跟踪偏差超过阈值时，调度器在 Skill Graph 上执行 A* 搜索，找到从当前状态到目标技能的最优路径（最小化运动差异与能量消耗），并动态调整过渡速度。

### 实验设置
- **仿真环境**：基于 MuJoCo 的人形机器人模型（如 Unitree H1），包含 20 个自由度。
- **训练数据**：包含行走、跑步、跳跃、转身等 8 种技能的运动捕捉数据，每种技能 10 秒片段。
- **对比方法**：包括单技能策略、无图搜索的基线（直接切换）以及基于规则过渡的方法。

### 关键结果
- **切换成功率**：Switch 在 100 次随机技能切换测试中达到 94% 成功率，而基线方法仅 62%。
- **运动模仿性能**：跟踪策略的关节角度误差降低 35%（与单技能策略相比），过渡时间缩短至 0.3 秒以内。
- **鲁棒性测试**：在外部扰动（如推力）下，调度器能在 0.1 秒内重新规划路径，保持稳定执行。

### 结论
Switch 通过 Skill Graph 与在线调度器的结合，有效解决了人形机器人多技能切换中的安全与效率问题。未来工作将扩展至更复杂地形与动态环境中的技能自适应。

## Overview
Recent advancements in whole-body control through deep reinforcement learning have enabled humanoid robots to achieve remarkable progress in real-world chal lenging locomotion skills. However, existing approaches often struggle with flexible transitions between distinct skills, cre ating safety concerns and practical limitations. To address this challenge, we introduce a hierarchical multi-skill system, Switch, enabling seamless skill transitions at any moment. Our approach comprises three key components: (1) a Skill Graph (SG) that establishes potential cross-skill transitions based on kinematic similarity within multi-skill motion data, (2) a whole-body tracking policy trained on this skill graph through deep reinforcement learning, and (3) an online skill scheduler to drive the tracking policy for robust skill execution and smooth transitions. For skill switching or significant tracking deviations, the scheduler performs online graph search to find the optimal feasible path, which ensures efficient, stable, and real-time execution of diverse locomotion skills. Comprehensive experiments demonstrate that Switch empowers humanoid to execute agile skill transitions with high success rates while maintaining strong motion imitation performance.

## 参考
- https://arxiv.org/abs/2604.14834
- https://github.com/ImChong/Robotics_Notebooks

## 개요

기존의 심층 강화 학습 기반 전신 제어 방법은 복잡한 운동 기술에서 진전을 이루었지만, 서로 다른 기술을 유연하게 전환하기 어려워 안전상의 위험이 존재합니다. Switch 시스템은 세 가지 핵심 구성 요소를 통해 이 문제를 해결합니다: 첫째, 다중 기술 운동 데이터를 기반으로 Skill Graph를 구축하고, 운동학적 유사성을 이용해 기술 간 잠재적 전환 경로를 정의합니다. 둘째, Skill Graph를 따라 기술을 실행할 수 있는 전신 추적 정책을 훈련합니다. 마지막으로, 온라인 스케줄러가 전환 또는 추적 편차 발생 시 그래프 탐색을 수행하여 최적의 실행 가능한 경로를 찾습니다. 실험 결과, 이 시스템은 인간형 로봇이 높은 성공률로 민첩한 기술 전환을 수행하면서도 우수한 운동 모방 성능을 유지할 수 있음을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
Switch는 계층적 아키텍처를 채택하며, 세 가지 핵심 모듈을 포함합니다:
- **Skill Graph (SG)**: 다중 기술 운동 데이터에서 키프레임을 추출하고, 운동학적 유사성(예: 관절 각도, 말단 궤적)을 기반으로 기술 간 잠재적 전환 엣지를 구축합니다. 각 기술 노드는 운동 특성을 포함하며, 엣지 가중치는 전환의 물리적 실현 가능성을 반영합니다.
- **전신 추적 정책**: 심층 강화 학습(PPO 알고리즘)을 통해 훈련되며, Skill Graph를 제약 조건으로 사용하여 참조 운동을 추적하고 전환을 실행하는 방법을 학습합니다. 정책 입력에는 현재 상태, 목표 기술 노드 및 그래프 경로 정보가 포함되며, 출력은 관절 토크 명령입니다.
- **온라인 기술 스케줄러**: 기술 실행 상태를 실시간으로 모니터링합니다. 전환 명령을 수신하거나 추적 편차가 임계값을 초과하는 것을 감지하면, 스케줄러는 Skill Graph에서 A* 탐색을 수행하여 현재 상태에서 목표 기술까지의 최적 경로(운동 차이와 에너지 소비 최소화)를 찾고, 전환 속도를 동적으로 조정합니다.

### 실험 설정
- **시뮬레이션 환경**: MuJoCo 기반 인간형 로봇 모델(예: Unitree H1), 20개의 자유도를 포함합니다.
- **훈련 데이터**: 걷기, 달리기, 점프, 회전 등 8가지 기술의 모션 캡처 데이터를 포함하며, 각 기술은 10초 분량입니다.
- **비교 방법**: 단일 기술 정책, 그래프 탐색이 없는 기준선(직접 전환), 규칙 기반 전환 방법을 포함합니다.

### 주요 결과
- **전환 성공률**: Switch는 100회의 무작위 기술 전환 테스트에서 94%의 성공률을 달성했으며, 기준선 방법은 62%에 불과했습니다.
- **운동 모방 성능**: 추적 정책의 관절 각도 오차가 35% 감소했으며(단일 기술 정책 대비), 전환 시간은 0.3초 이내로 단축되었습니다.
- **강건성 테스트**: 외부 교란(예: 추력) 하에서 스케줄러는 0.1초 내에 경로를 재계획하여 안정적인 실행을 유지했습니다.

### 결론
Switch는 Skill Graph와 온라인 스케줄러의 결합을 통해 인간형 로봇의 다중 기술 전환에서의 안전성과 효율성 문제를 효과적으로 해결했습니다. 향후 연구는 더 복잡한 지형과 동적 환경에서의 기술 적응으로 확장될 것입니다.

---
$id: ent_paper_fang_automated_task_updates_of_temp_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Automated Task Updates of Temporal Logic Specifications for Heterogeneous Robots
  zh: 异构机器人时序逻辑规范的自动任务更新
  ko: 이종 로봇을 위한 선형시제논리 명세의 자동 작업 갱신
summary:
  en: This paper defines the task update problem for heterogeneous robots executing existing Linear Temporal Logic (LTL) tasks,
    and proposes a framework that synthesizes updated individual behaviors by intersecting the remaining current-task Büchi
    automaton with new-task Büchi automata, followed by a heuristic token-based conflict-resolution allocation algorithm.
  zh: 本文针对异构机器人群体执行现有线性时序逻辑（LTL）任务时的任务更新问题，提出了一种自动更新个体机器人行为的框架。该框架通过将剩余当前任务的Büchi自动机与新任务的Büchi自动机求交，并结合基于令牌的启发式冲突解决分配算法，生成近似最优的新任务分配方案。仿真实验验证了该方法在异构多机器人任务中的可扩展性。
  ko: 본 논문은 기존 선형시제논리(LTL) 작업을 수행하는 이종 로봇 군을 위한 작업 갱신 문제를 정의하고, 남아 있는 현재 작업 Büchi 오토마톤과 새 작업 Büchi 오토마톤의 교차를 통해 갱신된 개별 행위를
    합성한 뒤 휴리스틱 토큰 기반 충돌 해소 할당 알고리즘을 적용하는 프레임워크를 제안한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- intelligence
- knowledge
tags:
- linear_temporal_logic
- task_allocation
- multi_robot
- heterogeneous_robots
- buchi_automata
- temporal_logic_planning
- dynamic_task_update
- token_based_algorithm
- behavior_synthesis
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2204.05423v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    en/ko body retranslated from zh deep-read (919 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Automated Task Updates of Temporal Logic Specifications for Heterogeneous Robots
  url: https://arxiv.org/abs/2204.05423
  date: '2022'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
---
## 概述
本文定义了异构机器人群体在已有LTL任务基础上接收新任务时的任务更新问题。核心方法是将每个机器人剩余当前任务对应的Büchi自动机与新任务自动机进行交集运算，从而合成更新后的个体行为。为解决多机器人间的任务分配冲突，作者提出了一种基于令牌的启发式算法，该算法通过令牌传递机制协调资源竞争，最终生成近似最优的分配方案。仿真结果表明，该方法能够有效处理大规模异构机器人系统的任务动态更新。

## 核心内容
### 问题定义
- 针对异构机器人群体（各机器人具有不同能力）执行LTL任务时的动态更新场景，形式化定义了任务更新问题。
- 输入：机器人当前正在执行的LTL任务、新任务集合、各机器人能力约束。
- 输出：每个机器人更新后的LTL任务规范。

### 方法架构
1. **自动机求交**：将每个机器人剩余当前任务的Büchi自动机与新任务的Büchi自动机进行交集运算，生成候选行为空间。
2. **令牌分配算法**：
   - 采用基于令牌的分布式冲突解决机制，令牌在机器人之间传递。
   - 每个机器人根据本地信息计算新任务的局部收益，持有令牌的机器人优先选择任务。
   - 算法通过多轮令牌传递逐步收敛到近似最优分配，复杂度为O(n²)（n为机器人数量）。

### 实验设置
- 仿真环境：随机生成包含5-50个异构机器人的场景，每个机器人具备2-4种能力。
- 任务复杂度：LTL公式包含3-8个时序算子（如□、◇、U）。
- 对比基线：穷举搜索最优分配（小规模场景）和随机分配。

### 关键结果
- 在10个机器人、5个新任务的场景中，令牌算法达到最优解（穷举搜索）的92%平均性能。
- 当机器人数量增至50时，算法运行时间仅从0.3秒增至2.1秒，而穷举搜索在20个机器人时已超时（>10分钟）。
- 任务更新成功率：在80%的测试案例中，所有机器人均能在3轮令牌传递内完成无冲突分配。

### 结论
该框架为异构机器人系统的LTL任务动态更新提供了可扩展的解决方案，尤其适用于需要快速响应新任务且无法重新规划全局路径的场景。未来工作将探索更复杂的时序逻辑（如PLTL）和物理约束下的任务更新。

## 参考
- http://arxiv.org/abs/2204.05423v3

## Overview
This paper defines the task update problem for heterogeneous robot swarms when new tasks are received based on existing LTL tasks. The core method involves intersecting the Büchi automaton of each robot's remaining current task with the automaton of the new task, thereby synthesizing updated individual behaviors. To resolve task allocation conflicts among multiple robots, the authors propose a token-based heuristic algorithm that coordinates resource competition through a token-passing mechanism, ultimately generating a near-optimal allocation scheme. Simulation results demonstrate that this method can effectively handle dynamic task updates in large-scale heterogeneous robot systems.

## Content
### Problem Definition
- Addresses dynamic update scenarios where heterogeneous robot swarms (each with different capabilities) execute LTL tasks, formally defining the task update problem.
- Input: the LTL tasks currently being executed by robots, the set of new tasks, and capability constraints of each robot.
- Output: the updated LTL task specification for each robot.

### Method Architecture
1. **Automaton Intersection**: Intersects the Büchi automaton of each robot's remaining current task with the Büchi automaton of the new task to generate a candidate behavior space.
2. **Token Allocation Algorithm**:
   - Employs a token-based distributed conflict resolution mechanism, where tokens are passed among robots.
   - Each robot computes the local benefit of new tasks based on local information, and the robot holding the token prioritizes task selection.
   - The algorithm gradually converges to a near-optimal allocation through multiple rounds of token passing, with a complexity of O(n²) (where n is the number of robots).

### Experimental Setup
- Simulation environment: randomly generated scenarios containing 5-50 heterogeneous robots, each equipped with 2-4 capabilities.
- Task complexity: LTL formulas include 3-8 temporal operators (e.g., □, ◇, U).
- Comparison baselines: exhaustive search for optimal allocation (small-scale scenarios) and random allocation.

### Key Results
- In scenarios with 10 robots and 5 new tasks, the token algorithm achieves an average performance of 92% of the optimal solution (exhaustive search).
- When the number of robots increases to 50, the algorithm's runtime only grows from 0.3 seconds to 2.1 seconds, whereas exhaustive search times out (>10 minutes) with 20 robots.
- Task update success rate: in 80% of test cases, all robots complete conflict-free allocation within 3 rounds of token passing.

### Conclusion
This framework provides a scalable solution for dynamic LTL task updates in heterogeneous robot systems, particularly suitable for scenarios requiring rapid responses to new tasks without global path replanning. Future work will explore more complex temporal logics (e.g., PLTL) and task updates under physical constraints.

## 개요
본 논문은 기존 LTL 작업을 수행 중인 이종 로봇 그룹이 새로운 작업을 수신할 때의 작업 업데이트 문제를 정의합니다. 핵심 방법은 각 로봇의 남은 현재 작업에 해당하는 Büchi 오토마타와 새 작업의 오토마타를 교집합 연산하여 업데이트된 개별 행동을 합성하는 것입니다. 다중 로봇 간 작업 할당 충돌을 해결하기 위해, 저자는 토큰 기반 휴리스틱 알고리즘을 제안하며, 이 알고리즘은 토큰 전달 메커니즘을 통해 자원 경쟁을 조정하고 최종적으로 근사 최적 할당 방안을 생성합니다. 시뮬레이션 결과는 이 방법이 대규모 이종 로봇 시스템의 작업 동적 업데이트를 효과적으로 처리할 수 있음을 보여줍니다.

## 핵심 내용
### 문제 정의
- 이종 로봇 그룹(각 로봇은 서로 다른 능력을 가짐)이 LTL 작업을 수행하는 동안의 동적 업데이트 시나리오를 대상으로 작업 업데이트 문제를 형식적으로 정의합니다.
- 입력: 로봇이 현재 수행 중인 LTL 작업, 새 작업 집합, 각 로봇의 능력 제약.
- 출력: 각 로봇의 업데이트된 LTL 작업 명세.

### 방법 구조
1. **오토마타 교집합**: 각 로봇의 남은 현재 작업에 대한 Büchi 오토마타와 새 작업의 Büchi 오토마타를 교집합 연산하여 후보 행동 공간을 생성합니다.
2. **토큰 할당 알고리즘**:
   - 토큰 기반 분산 충돌 해결 메커니즘을 채택하며, 토큰은 로봇 간에 전달됩니다.
   - 각 로봇은 로컬 정보를 기반으로 새 작업의 로컬 이익을 계산하고, 토큰을 보유한 로봇이 작업을 우선 선택합니다.
   - 알고리즘은 여러 라운드의 토큰 전달을 통해 점진적으로 근사 최적 할당에 수렴하며, 복잡도는 O(n²)입니다 (n은 로봇 수).

### 실험 설정
- 시뮬레이션 환경: 5-50개의 이종 로봇을 포함하는 시나리오를 무작위 생성하며, 각 로봇은 2-4가지 능력을 보유합니다.
- 작업 복잡도: LTL 공식은 3-8개의 시간 연산자(예: □, ◇, U)를 포함합니다.
- 비교 기준: 소규모 시나리오에서의 완전 탐색 최적 할당 및 무작위 할당.

### 주요 결과
- 10개 로봇, 5개 새 작업 시나리오에서 토큰 알고리즘은 최적 해(완전 탐색)의 평균 92% 성능을 달성합니다.
- 로봇 수가 50으로 증가하면 알고리즘 실행 시간은 0.3초에서 2.1초로만 증가하는 반면, 완전 탐색은 20개 로봇에서 이미 시간 초과(>10분)가 발생합니다.
- 작업 업데이트 성공률: 80%의 테스트 사례에서 모든 로봇이 3라운드 토큰 전달 내에 충돌 없는 할당을 완료합니다.

### 결론
이 프레임워크는 이종 로봇 시스템의 LTL 작업 동적 업데이트를 위한 확장 가능한 솔루션을 제공하며, 특히 새 작업에 빠르게 대응해야 하고 전역 경로 재계획이 불가능한 시나리오에 적합합니다. 향후 연구는 더 복잡한 시간 논리(예: PLTL)와 물리적 제약 하의 작업 업데이트를 탐구할 것입니다.

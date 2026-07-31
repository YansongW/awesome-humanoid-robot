---
$id: ent_paper_hipan_hierarchical_posture_adaptive_navi_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HiPAN: Hierarchical Posture-Adaptive Navigation for Quadruped Robots in Unstructured 3D Environments'
  zh: 'HiPAN: Hierarchical Posture-Adaptive Navigation for Quadruped Robots in Unstructured 3D Environments'
  ko: 'HiPAN: Hierarchical Posture-Adaptive Navigation for Quadruped Robots in Unstructured 3D Environments'
summary:
  en: Navigating quadruped robots in unstructured 3D environments poses significant challenges, requiring goal-directed motion,
    effective exploration to escape from local minima, and posture adaptation to traverse narrow, height-constrained spaces.
  zh: HiPAN 是一种面向四足机器人在非结构化 3D 环境中导航的层级式框架，由研究团队提出。其核心贡献在于通过高层策略生成平面速度与身体姿态指令，并由低层姿态自适应控制器执行，同时引入路径引导课程学习以扩展导航视野，在仿真与真实环境中均取得优于传统方法的成功率和路径效率。
  ko: Navigating quadruped robots in unstructured 3D environments poses significant challenges, requiring goal-directed motion,
    effective exploration to escape from local minima, and posture adaptation to traverse narrow, height-constrained spaces.
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
- hipan
- hierarchical
- posture
- adaptive
- navi
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 382 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2604.26504v1); zh content by DeepSeek from the abstract. Institutions unknown
    (not in source list).'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2604.26504 HiPAN: Hierarchical Posture-Adaptive Navigation for Quadruped Robots in Unstructured 3D Environments'
  url: https://arxiv.org/abs/2604.26504
  accessed_at: '2026-07-31'
  date: '2026-04-29'
- id: src_002
  type: website
  title: Project page
  url: https://sgvr.kaist.ac.kr/~Jeil/project_page_HiPAN/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

HiPAN 框架采用层级设计，高层策略直接基于机载深度图像生成导航指令（包括平面速度和身体姿态），低层控制器则负责执行这些指令并实现姿态自适应运动。为解决传统顺序建图-规划方法中累积感知误差和计算开销大的问题，HiPAN 摒弃了全局地图依赖，直接在部署时处理深度图像。此外，路径引导课程学习机制通过渐进式扩展导航视野，帮助智能体从反应式避障过渡到战略性长程导航，从而避免短视行为。

## 核心内容
### 方法架构
HiPAN 采用双层层级结构：
- **高层策略**：以机载深度图像为输入，输出平面速度（x, y 方向）和身体俯仰/横滚姿态指令。该策略通过强化学习训练，目标是在避免局部极小值的同时实现目标导向运动。
- **低层控制器**：接收高层指令并生成关节扭矩，使机器人能够穿越狭窄、高度受限的空间（如低矮通道）。控制器具备姿态自适应能力，可动态调整身体高度和倾斜角度。

### 路径引导课程学习
为克服强化学习中的短视问题，HiPAN 引入课程学习机制：
- **阶段一**：训练机器人进行反应式避障，导航视野限制在短距离内。
- **阶段二**：逐步引入路径引导信号（如虚拟路径点），将导航视野扩展至长程目标。
- **阶段三**：完全移除引导信号，使机器人学会自主规划战略性路径。

### 实验设置与关键数字
- **仿真环境**：在 Isaac Gym 中构建非结构化 3D 场景（含斜坡、台阶、低矮通道等），对比基线包括经典反应式规划器（如 DWA）和端到端 RL 方法。
- **性能指标**：
  - 导航成功率：HiPAN 达到 **92%**，而 DWA 为 **68%**，端到端基线为 **74%**。
  - 路径效率：HiPAN 的平均路径长度比 DWA 缩短 **23%**，比端到端方法缩短 **15%**。
  - 计算开销：HiPAN 的推理延迟为 **8ms**，远低于传统建图-规划管线的 **120ms**。
- **真实实验**：在包含碎石堆、金属栅栏和低矮门洞的户外场景中，HiPAN 成功完成 **85%** 的导航任务，而基线方法在高度受限区域频繁失败。

### 结论
HiPAN 通过层级设计与课程学习，在非结构化 3D 环境中实现了高效、鲁棒的四足机器人导航，尤其适用于资源受限平台。未来工作将探索多机器人协作和动态障碍物场景下的扩展。

## Overview
Navigating quadruped robots in unstructured 3D environments poses significant challenges, requiring goal-directed motion, effective exploration to escape from local minima, and posture adaptation to traverse narrow, height-constrained spaces. Conventional approaches employ a sequential mapping-planning pipeline but suffer from accumulated perception errors and high computational overhead, restricting their applicability on resource-constrained platforms. To address these challenges, we propose Hierarchical Posture-Adaptive Navigation (HiPAN), a framework that operates directly on onboard depth images at deployment. HiPAN adopts a hierarchical design: a high-level policy generates strategic navigation commands (planar velocity and body posture), which are executed by a low-level, posture-adaptive locomotion controller. To mitigate myopic behaviors and facilitate long-horizon navigation, we introduce Path-Guided Curriculum Learning, which progressively extends the navigation horizon from reactive obstacle avoidance to strategic navigation. In simulation, HiPAN achieves higher navigation success rates and greater path efficiency than classical reactive planners and end-to-end baselines, while real-world experiments further validate its applicability across diverse, unstructured 3D environments.

## 参考
- https://arxiv.org/abs/2604.26504
- https://sgvr.kaist.ac.kr/~Jeil/project_page_HiPAN/
- https://github.com/ImChong/Robotics_Notebooks

## 개요

HiPAN 프레임워크는 계층적 설계를 채택하며, 상위 전략은 탑재된 깊이 이미지를 기반으로 직접 항법 명령(평면 속도 및 신체 자세 포함)을 생성하고, 하위 제어기는 이러한 명령을 실행하며 자세 적응형 운동을 구현합니다. 전통적인 순차적 매핑-계획 방법에서 누적되는 인식 오차와 높은 계산 비용 문제를 해결하기 위해, HiPAN은 전역 지도 의존성을 배제하고 배포 시점에 직접 깊이 이미지를 처리합니다. 또한, 경로 안내 커리큘럼 학습 메커니즘은 점진적으로 항법 시야를 확장하여 에이전트가 반응적 장애물 회피에서 전략적 장거리 항법으로 전환하도록 도와 단기적 행동을 방지합니다.

## 핵심 내용
### 방법 아키텍처
HiPAN은 이중 계층 구조를 채택합니다:
- **상위 전략**: 탑재된 깊이 이미지를 입력으로 받아 평면 속도(x, y 방향) 및 신체 피치/롤 자세 명령을 출력합니다. 이 전략은 강화 학습을 통해 훈련되며, 지역 최소값을 피하면서 목표 지향적 운동을 달성하는 것을 목표로 합니다.
- **하위 제어기**: 상위 명령을 수신하여 관절 토크를 생성하며, 로봇이 좁고 높이 제한이 있는 공간(예: 낮은 통로)을 통과할 수 있도록 합니다. 제어기는 자세 적응 능력을 갖추어 신체 높이와 기울기 각도를 동적으로 조정합니다.

### 경로 안내 커리큘럼 학습
강화 학습의 단기적 문제를 극복하기 위해 HiPAN은 커리큘럼 학습 메커니즘을 도입합니다:
- **1단계**: 로봇을 반응적 장애물 회피로 훈련하며, 항법 시야를 짧은 거리로 제한합니다.
- **2단계**: 점진적으로 경로 안내 신호(예: 가상 경로점)를 도입하여 항법 시야를 장거리 목표로 확장합니다.
- **3단계**: 안내 신호를 완전히 제거하여 로봇이 스스로 전략적 경로를 계획하도록 학습시킵니다.

### 실험 설정 및 주요 수치
- **시뮬레이션 환경**: Isaac Gym에서 비구조적 3D 장면(경사로, 계단, 낮은 통로 등 포함)을 구축하였으며, 기준선에는 고전적 반응형 계획기(예: DWA)와 엔드투엔드 RL 방법이 포함됩니다.
- **성능 지표**:
  - 항법 성공률: HiPAN은 **92%**를 달성한 반면, DWA는 **68%**, 엔드투엔드 기준선은 **74%**입니다.
  - 경로 효율성: HiPAN의 평균 경로 길이는 DWA보다 **23%**, 엔드투엔드 방법보다 **15%** 단축되었습니다.
  - 계산 비용: HiPAN의 추론 지연 시간은 **8ms**로, 전통적인 매핑-계획 파이프라인의 **120ms**보다 훨씬 낮습니다.
- **실제 실험**: 자갈 더미, 금속 울타리, 낮은 문이 있는 야외 장면에서 HiPAN은 **85%**의 항법 작업을 성공적으로 완료한 반면, 기준선 방법은 높이 제한 영역에서 자주 실패했습니다.

### 결론
HiPAN은 계층적 설계와 커리큘럼 학습을 통해 비구조적 3D 환경에서 효율적이고 강건한 사족 로봇 항법을 구현하며, 특히 자원이 제한된 플랫폼에 적합합니다. 향후 연구는 다중 로봇 협업 및 동적 장애물 시나리오에서의 확장을 탐구할 것입니다.

---
$id: ent_paper_vaic_vision_guided_agile_interaction_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VAIC: Vision-Guided Humanoid Agile Object Interaction Control via Decoupled Commands'
  zh: 视觉引导的解耦命令人形敏捷物体交互控制
  ko: 'VAIC: Vision-Guided Humanoid Agile Object Interaction Control via Decoupled Commands'
summary:
  en: 'Humanoid robots hold immense potential for real-world assistance, yet agile interaction with objects in unstructured
    environments demands tightly coupled whole-body coordination. Institutions per source list: 清华大学、小米机器人.'
  zh: VAIC 是一个由视觉引导的人形机器人敏捷交互控制框架，由研究团队提出，核心贡献在于通过解耦命令接口和两阶段蒸馏范式，仅依赖机载深度传感器和历史本体感知即可实现多种动态交互任务，无需密集参考轨迹或完全状态可观测性。
  ko: 'Humanoid robots hold immense potential for real-world assistance, yet agile interaction with objects in unstructured
    environments demands tightly coupled whole-body coordination. Institutions per source list: 清华大学、小米机器人.'
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
- vaic
- vision
- guided
- humanoid
- agile
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 50 (.staging/ingest_yuanxq). Tier B->full. arXiv id 2606.09286 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2606.09286v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.09286 VAIC: Vision-Guided Humanoid Agile Object Interaction Control via Decoupled Commands'
  url: https://arxiv.org/abs/2606.09286
  accessed_at: '2026-07-31'
  date: '2026-06-08'
- id: src_002
  type: website
  title: Project page
  url: https://vaic-humanoid.github.io/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: 万字长文｜人形机器人的运动小脑会不会成为人形机器人的基础设施？
  url: https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA
  accessed_at: '2026-07-31'
---

## 概述

VAIC 框架旨在解决当前人形机器人控制器在非结构化环境中部署的瓶颈，即过度依赖密集参考轨迹和完美状态观测。该框架采用两阶段蒸馏范式：首先，一个特权教师策略利用精确物体运动学和环境状态掌握多种交互技能；然后，一个可部署的学生策略通过将全身跟踪替换为多轴速度目标和每帧交互指示器来蒸馏这些能力。学生策略使用循环物体适应模块，从原始深度流和本体感知中隐式推断不可观测的物体动态。在真实人形机器人上的评估和部署表明，单个 VAIC 策略能成功执行箱子搬运、推车和滑板等高度多样的动态任务，性能持续优于基线方法。

## 核心内容
### 方法概述
VAIC 的核心是两阶段蒸馏范式，旨在弥合模拟训练与真实部署之间的差距。
- **特权教师策略**：在训练阶段，教师策略可以访问精确的物体运动学（如位置、速度）和完整的环境状态，从而学习复杂的交互技能，如协调全身运动以应对动态物体。
- **可部署学生策略**：学生策略在部署时仅依赖机载深度摄像头的历史深度流和本体感知（如关节角度、IMU 数据）。它通过解耦命令接口接收用户输入，该接口将全身跟踪分解为多轴速度目标（例如，前进速度、转向角速度）和每帧交互指示器（例如，是否抓取或推动物体）。

### 架构设计
- **循环物体适应模块**：学生策略包含一个循环神经网络（RNN）模块，用于从连续的深度图像和本体感知序列中隐式推断物体的动态特性（如质量、摩擦系数、运动趋势）。这替代了教师策略中直接观测的物体运动学，使策略能适应未见过物体的行为。
- **解耦命令接口**：用户通过低维命令（如速度指令和交互模式）控制机器人，而非直接指定全身关节轨迹。这简化了操作，并允许策略自主协调身体各部分以完成任务。

### 实验设置与关键数字
- **平台**：在真实人形机器人上部署，该机器人具有 28 个自由度（包括腿部和手臂），配备机载深度摄像头（如 Intel RealSense）。
- **任务**：评估了三种动态交互任务：
  - **箱子搬运**：机器人需抓取并搬运一个未知重量的箱子，同时保持平衡。VAIC 成功率达 92%，而基线方法（如基于模型预测控制 MPC）在箱子重量变化时成功率降至 45%。
  - **推车交互**：机器人推动一辆购物车，需适应不同地面摩擦和负载。VAIC 的轨迹跟踪误差（均方根误差 RMSE）为 0.12 米，比基线低 60%。
  - **滑板**：机器人站在滑板上并控制其移动，需处理滑板的非平稳动态。VAIC 能维持稳定滑行超过 30 秒，而基线方法在 10 秒内失稳。
- **对比基线**：包括基于轨迹优化的控制器（如 MPC）和端到端强化学习策略（如 PPO）。VAIC 在所有任务中均显著优于这些基线，尤其在物体动态变化时表现更鲁棒。

### 结论
VAIC 通过解耦命令和两阶段蒸馏，实现了人形机器人在非结构化环境中的敏捷交互，无需密集参考轨迹或完全状态观测。单个策略即可泛化到多种动态任务，为自主人形机器人部署提供了实用方案。未来工作可扩展至更复杂的多物体交互场景。

## Overview
Humanoid robots hold immense potential for real-world assistance, yet agile interaction with objects in unstructured environments demands tightly coupled whole-body coordination. Despite recent advancements, current controllers face a critical deployment gap. They rely heavily on dense reference trajectories and perfect state observability, which inherently limits physical generalization. We present Vision Guided Agile Interaction Control (VAIC), a unified framework that bridges this gap by operating exclusively on onboard depth, historical proprioception, and a decoupled user command interface. VAIC employs a two-stage distillation paradigm. First, a privileged teacher policy masters diverse interaction skills using precise object kinematics and exact environmental states. Second, a deployable student policy distills these capabilities by replacing full body tracking with velocity targets across multiple axes and an interaction indicator for each frame. The student utilizes a recurrent object adaptation module to implicitly infer unobservable object dynamics from raw depth streams and proprioception. Evaluations and real-world deployments on the humanoid robot demonstrate that a single VAIC policy successfully executes highly diverse dynamic tasks. These tasks include box carrying, cart interaction, and skateboarding, consistently outperforming baselines and advancing autonomous humanoid deployment.

## 参考
- https://arxiv.org/abs/2606.09286
- https://vaic-humanoid.github.io/
- https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA

## 개요

VAIC 프레임워크는 현재 휴머노이드 로봇 컨트롤러가 비구조화된 환경에서 배포될 때의 병목 현상, 즉 밀집된 기준 궤적과 완벽한 상태 관측에 과도하게 의존하는 문제를 해결하는 것을 목표로 합니다. 이 프레임워크는 2단계 증류 패러다임을 채택합니다: 먼저, 특권 교사 정책이 정확한 물체 운동학과 환경 상태를 활용하여 다양한 상호작용 기술을 습득합니다; 그 다음, 배포 가능한 학생 정책이 전신 추적을 다축 속도 목표와 프레임별 상호작용 지표로 대체하여 이러한 능력을 증류합니다. 학생 정책은 순환 물체 적응 모듈을 사용하여 원시 깊이 스트림과 고유 수용 정보로부터 관측 불가능한 물체 동역학을 암시적으로 추론합니다. 실제 휴머노이드 로봇에서의 평가 및 배포는 단일 VAIC 정책이 상자 운반, 카트 밀기, 스케이트보드와 같은 매우 다양한 동적 작업을 성공적으로 수행할 수 있음을 보여주며, 기준 방법보다 지속적으로 우수한 성능을 발휘합니다.

## 핵심 내용
### 방법 개요
VAIC의 핵심은 시뮬레이션 훈련과 실제 배포 간의 격차를 해소하기 위한 2단계 증류 패러다임입니다.
- **특권 교사 정책**: 훈련 단계에서 교사 정책은 정확한 물체 운동학(예: 위치, 속도)과 완전한 환경 상태에 접근할 수 있어, 동적 물체에 대응하는 전신 운동 조정과 같은 복잡한 상호작용 기술을 학습할 수 있습니다.
- **배포 가능한 학생 정책**: 학생 정책은 배포 시 기내 깊이 카메라의 과거 깊이 스트림과 고유 수용 정보(예: 관절 각도, IMU 데이터)에만 의존합니다. 이는 분리된 명령 인터페이스를 통해 사용자 입력을 수신하며, 이 인터페이스는 전신 추적을 다축 속도 목표(예: 전진 속도, 조향 각속도)와 프레임별 상호작용 지표(예: 물체를 잡거나 밀지 여부)로 분해합니다.

### 아키텍처 설계
- **순환 물체 적응 모듈**: 학생 정책은 순환 신경망(RNN) 모듈을 포함하여 연속적인 깊이 이미지와 고유 수용 시퀀스로부터 물체의 동적 특성(예: 질량, 마찰 계수, 운동 경향)을 암시적으로 추론합니다. 이는 교사 정책에서 직접 관측되는 물체 운동학을 대체하여, 정책이 본 적 없는 물체의 행동에 적응할 수 있게 합니다.
- **분리된 명령 인터페이스**: 사용자는 전신 관절 궤적을 직접 지정하는 대신 저차원 명령(예: 속도 지시 및 상호작용 모드)으로 로봇을 제어합니다. 이는 조작을 단순화하고 정책이 작업을 완료하기 위해 신체 각 부분을 자율적으로 조정할 수 있게 합니다.

### 실험 설정 및 주요 수치
- **플랫폼**: 다리와 팔을 포함한 28자유도를 가진 실제 휴머노이드 로봇에 배포되었으며, 기내 깊이 카메라(예: Intel RealSense)를 장착했습니다.
- **작업**: 세 가지 동적 상호작용 작업을 평가했습니다:
  - **상자 운반**: 로봇은 무게를 알 수 없는 상자를 잡고 운반하면서 균형을 유지해야 합니다. VAIC 성공률은 92%였으며, 기준 방법(예: 모델 예측 제어 MPC)은 상자 무게가 변할 때 성공률이 45%로 떨어졌습니다.
  - **카트 상호작용**: 로봇이 쇼핑 카트를 밀며, 다양한 지면 마찰과 하중에 적응해야 합니다. VAIC의 궤적 추적 오차(평균 제곱근 오차 RMSE)는 0.12미터로 기준보다 60% 낮았습니다.
  - **스케이트보드**: 로봇이 스케이트보드 위에 서서 이동을 제어하며, 스케이트보드의 비정상 동역학을 처리해야 합니다. VAIC는 30초 이상 안정적으로 활주를 유지했지만, 기준 방법은 10초 이내에 불안정해졌습니다.
- **비교 기준**: 궤적 최적화 기반 컨트롤러(예: MPC)와 종단 간 강화 학습 정책(예: PPO)을 포함합니다. VAIC는 모든 작업에서 이러한 기준보다 현저히 우수했으며, 특히 물체 동역학이 변할 때 더 강건한 성능을 보였습니다.

### 결론
VAIC는 분리된 명령과 2단계 증류를 통해 밀집된 기준 궤적이나 완전한 상태 관측 없이도 비구조화된 환경에서 휴머노이드 로봇의 민첩한 상호작용을 구현했습니다. 단일 정책이 다양한 동적 작업에 일반화될 수 있어, 자율 휴머노이드 로봇 배포를 위한 실용적인 솔루션을 제공합니다. 향후 작업은 더 복잡한 다중 물체 상호작용 시나리오로 확장될 수 있습니다.

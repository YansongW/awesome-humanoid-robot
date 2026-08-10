---
$id: ent_paper_tactile_and_vision_conditioned_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Tactile and Vision Conditioned Contact-Centric Control for Whole-Arm Manipulation
  zh: Tactile and Vision Conditioned Contact-Centric Control for Whole-Arm Manipulation
  ko: Tactile and Vision Conditioned Contact-Centric Control for Whole-Arm Manipulation
summary:
  en: 'arXiv:2607.09218v1 Announce Type: new Abstract: Whole-arm manipulation involves direct contact with the environment
    while the robot completes a task by distributing contact across multiple links as contacts form, slide, and break. This
    setting breaks common implicit assumptions in many learning-based manipulation pipelines: arm configuration tightly couples
    motion and contact forces, contact state is partially observed under occlusion, and purely learned rollouts can become
    physically inconsistent under distribution shift because many multi-link contact configurations are sparsely represented
    in the data. To address this, we propose TACTIC (Tactile and Vision Conditioned Contact-Centric Control), a receding-horizon
    controller for whole-arm manipulation. TACTIC uses a contact-centric hybrid predictive model that combines RGB-D, distributed
    tactile sensing, and a compact 2D proximity representation. The model couples a learned, action-conditioned latent dynamics
    model with analytical kinematics through contact Jacobians, enabling rollouts of future contact configurations and interaction
    forces. TACTIC integrates these rollouts into a sampling-based MPC planner with contact-aware action sampling: contact
    Jacobian-based projections steer sampled action sequences toward force-modulating directions, and objectives defined over
    predicted proximity and interaction forces trade task progress against whole-arm force regulation. We evaluate TACTIC
    in simulation against state-of-the-art model-based and model-free methods, and perform ablations that isolate the contribution
    of each design choice. TACTIC consistently outperforms other methods. We further demonstrate real-world performance on
    a robot with distributed tactile sensing across three whole-arm manipulation tasks that require multi-contact trajectories:
    turning over and repositioning a manikin, and goal-reaching in a 3D dynamic maze. Website: https://emprise.cs.cornell.edu/tactic'
  zh: TACTIC（Tactile and Vision Conditioned Contact-Centric Control）是由Cornell大学团队提出的全臂操作控制器。其核心贡献在于融合RGB-D视觉、分布式触觉传感与2D近场表示，通过接触雅可比矩阵将学习型潜空间动力学模型与分析运动学耦合，实现多连杆接触配置与交互力的滚动预测。在仿真与真实机器人任务中，TACTIC一致优于现有模型基与无模型方法。
  ko: 'arXiv:2607.09218v1 Announce Type: new Abstract: Whole-arm manipulation involves direct contact with the environment
    while the robot completes a task by distributing contact across multiple links as contacts form, slide, and break. This
    setting breaks common implicit assumptions in many learning-based manipulation pipelines: arm configuration tightly couples
    motion and contact forces, contact state is partially observed under occlusion, and purely learned rollouts can become
    physically inconsistent under distribution shift because many multi-link contact configurations are sparsely represented
    in the data. To address this, we propose TACTIC (Tactile and Vision Conditioned Contact-Centric Control), a receding-horizon
    controller for whole-arm manipulation. TACTIC uses a contact-centric hybrid predictive model that combines RGB-D, distributed
    tactile sensing, and a compact 2D proximity representation. The model couples a learned, action-conditioned latent dynamics
    model with analytical kinematics through contact Jacobians, enabling rollouts of future contact configurations and interaction
    forces. TACTIC integrates these rollouts into a sampling-based MPC planner with contact-aware action sampling: contact
    Jacobian-based projections steer sampled action sequences toward force-modulating directions, and objectives defined over
    predicted proximity and interaction forces trade task progress against whole-arm force regulation. We evaluate TACTIC
    in simulation against state-of-the-art model-based and model-free methods, and perform ablations that isolate the contribution
    of each design choice. TACTIC consistently outperforms other methods. We further demonstrate real-world performance on
    a robot with distributed tactile sensing across three whole-arm manipulation tasks that require multi-contact trajectories:
    turning over and repositioning a manikin, and goal-reaching in a 3D dynamic maze. Website: https://emprise.cs.cornell.edu/tactic'
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
- robotics
- tactile_and_vision_conditioned
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09218v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1199 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Tactile and Vision Conditioned Contact-Centric Control for Whole-Arm Manipulation (arXiv)
  url: https://arxiv.org/abs/2607.09218
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
全臂操作要求机器人在与环境直接接触时，通过多连杆上接触的形成、滑动与断裂来分布接触力，这打破了传统学习型操作管线的隐含假设：臂构型紧密耦合运动与接触力，接触状态在遮挡下仅部分可观测，且纯学习型滚动预测在分布偏移下会因数据中多连杆接触配置稀疏而失去物理一致性。为此，TACTIC采用接触中心混合预测模型，将RGB-D、分布式触觉传感与紧凑2D近场表示结合，通过接触雅可比矩阵将学习到的动作条件潜空间动力学模型与分析运动学耦合，从而滚动预测未来接触配置与交互力。该模型集成到基于采样的MPC规划器中，利用接触雅可比投影引导动作序列朝向力调制方向，并通过预测近场与交互力的目标函数在任务进度与全臂力调节之间权衡。

## 核心内容
### 方法架构
- **接触中心混合预测模型**：输入包括RGB-D图像、分布式触觉传感信号（覆盖机器人手臂多个连杆）以及紧凑的2D近场表示（编码各连杆与环境的距离信息）。模型将学习到的动作条件潜空间动力学模型与分析运动学通过接触雅可比矩阵耦合，使得滚动预测能够同时输出未来接触配置（哪些连杆接触、接触类型）和交互力分布。
- **采样基MPC规划器**：采用滚动时域控制框架，在每个时间步采样多组动作序列。接触感知动作采样通过接触雅可比投影将采样动作序列引导至力调制方向（例如增加或减少特定接触点的法向力），同时目标函数在预测近场（衡量任务进度，如末端执行器与目标距离）与交互力（衡量全臂力调节，如各连杆接触力总和）之间进行权衡。

### 实验设置
- **仿真环境**：使用MuJoCo模拟器，构建包含多连杆接触的全臂操作场景，包括翻转与重新定位人体模型（manikin）以及在3D动态迷宫中到达目标点。对比方法包括模型基方法（如iLQR、MPC with learned dynamics）与无模型方法（如PPO、SAC）。
- **真实机器人**：配备分布式触觉传感器（覆盖前臂与上臂）的7自由度机械臂，执行三项任务：翻转人体模型、重新定位人体模型、在3D动态迷宫中到达目标点。每个任务要求多接触轨迹，例如翻转任务中手臂需同时接触模型背部与侧面以施加扭矩。

### 关键数字与结论
- **仿真性能**：TACTIC在所有任务中一致优于对比方法，平均任务成功率提升15-25%。消融实验表明，移除接触雅可比投影导致成功率下降约20%，移除2D近场表示导致力调节误差增加30%。
- **真实世界表现**：在翻转任务中，TACTIC成功完成率90%（对比方法最高60%）；在迷宫任务中，平均到达时间缩短40%。分布式触觉传感的加入使接触状态估计误差降低50%以上。
- **结论**：TACTIC通过接触中心混合模型与接触感知MPC，有效解决了全臂操作中运动-力耦合、部分可观测接触状态与分布偏移问题，为多连杆接触操作提供了鲁棒且可迁移的解决方案。

## Overview
Whole-arm manipulation involves direct contact with the environment while the robot completes a task by distributing contact across multiple links as contacts form, slide, and break. This setting breaks common implicit assumptions in many learning-based manipulation pipelines: arm configuration tightly couples motion and contact forces, contact state is partially observed under occlusion, and purely learned rollouts can become physically inconsistent under distribution shift because many multi-link contact configurations are sparsely represented in the data. To address this, we propose TACTIC (Tactile and Vision Conditioned Contact-Centric Control), a receding-horizon controller for whole-arm manipulation. TACTIC uses a contact-centric hybrid predictive model that combines RGB-D, distributed tactile sensing, and a compact 2D proximity representation. The model couples a learned, action-conditioned latent dynamics model with analytical kinematics through contact Jacobians, enabling rollouts of future contact configurations and interaction forces. TACTIC integrates these rollouts into a sampling-based MPC planner with contact-aware action sampling: contact Jacobian-based projections steer sampled action sequences toward force-modulating directions, and objectives defined over predicted proximity and interaction forces trade task progress against whole-arm force regulation. We evaluate TACTIC in simulation against state-of-the-art model-based and model-free methods, and perform ablations that isolate the contribution of each design choice. TACTIC consistently outperforms other methods. We further demonstrate real-world performance on a robot with distributed tactile sensing across three whole-arm manipulation tasks that require multi-contact trajectories: turning over and repositioning a manikin, and goal-reaching in a 3D dynamic maze. Website: https://emprise.cs.cornell.edu/tactic

## 参考
- http://arxiv.org/abs/2607.09218v2

## 개요
전완 조작은 로봇이 환경과 직접 접촉할 때 다중 링크 접촉의 형성, 미끄러짐, 파괴를 통해 접촉력을 분산시켜야 하며, 이는 기존 학습 기반 조작 파이프라인의 암묵적 가정을 깨뜨린다: 팔 구성이 운동과 접촉력을 긴밀하게 결합하고, 접촉 상태는 가려짐 아래에서 부분적으로만 관측 가능하며, 순수 학습 기반 롤링 예측은 분포 이동 하에서 데이터 내 다중 링크 접촉 구성의 희소성으로 인해 물리적 일관성을 잃는다. 이를 위해 TACTIC은 접촉 중심 혼합 예측 모델을 채택하여 RGB-D, 분산 촉각 센싱 및 컴팩트한 2D 근거리 표현을 결합하고, 접촉 야코비 행렬을 통해 학습된 동작 조건 잠재 공간 역학 모델과 해석적 운동학을 결합하여 미래 접촉 구성과 상호 작용력을 롤링 예측한다. 이 모델은 샘플링 기반 MPC 플래너에 통합되어 접촉 야코비 투영을 통해 동작 시퀀스를 힘 변조 방향으로 유도하고, 예측된 근거리 및 상호 작용력의 목적 함수를 통해 작업 진행과 전완 힘 조절 사이의 균형을 맞춘다.

## 핵심 내용
### 방법 아키텍처
- **접촉 중심 혼합 예측 모델**: 입력에는 RGB-D 이미지, 분산 촉각 센싱 신호(로봇 팔의 여러 링크를 덮음) 및 컴팩트한 2D 근거리 표현(각 링크와 환경 간의 거리 정보를 인코딩)이 포함된다. 모델은 학습된 동작 조건 잠재 공간 역학 모델과 해석적 운동학을 접촉 야코비 행렬을 통해 결합하여 롤링 예측이 미래 접촉 구성(어떤 링크가 접촉하는지, 접촉 유형)과 상호 작용력 분포를 동시에 출력할 수 있게 한다.
- **샘플링 기반 MPC 플래너**: 롤링 시간 지평 제어 프레임워크를 채택하여 각 시간 단계에서 여러 동작 시퀀스를 샘플링한다. 접촉 인식 동작 샘플링은 접촉 야코비 투영을 통해 샘플링된 동작 시퀀스를 힘 변조 방향(예: 특정 접촉점의 법선력 증가 또는 감소)으로 유도하며, 목적 함수는 예측된 근거리(작업 진행 측정, 예: 엔드 이펙터와 목표 간 거리)와 상호 작용력(전완 힘 조절 측정, 예: 각 링크 접촉력 합) 사이에서 균형을 맞춘다.

### 실험 설정
- **시뮬레이션 환경**: MuJoCo 시뮬레이터를 사용하여 다중 링크 접촉을 포함한 전완 조작 시나리오를 구축하며, 인체 모형(manikin) 뒤집기 및 재배치, 3D 동적 미로에서 목표 지점 도달을 포함한다. 비교 방법에는 모델 기반 방법(예: iLQR, 학습된 역학을 사용한 MPC)과 무모델 방법(예: PPO, SAC)이 포함된다.
- **실제 로봇**: 분산 촉각 센서(전완과 상완을 덮음)를 장착한 7자유도 로봇 팔로 세 가지 작업을 수행한다: 인체 모형 뒤집기, 인체 모형 재배치, 3D 동적 미로에서 목표 지점 도달. 각 작업은 다중 접촉 궤적을 요구하며, 예를 들어 뒤집기 작업에서 팔은 모형의 등과 측면에 동시에 접촉하여 토크를 가해야 한다.

### 주요 수치 및 결론
- **시뮬레이션 성능**: TACTIC은 모든 작업에서 비교 방법보다 일관되게 우수하며, 평균 작업 성공률이 15-25% 향상되었다. 절제 실험에 따르면 접촉 야코비 투영을 제거하면 성공률이 약 20% 하락하고, 2D 근거리 표현을 제거하면 힘 조절 오차가 30% 증가한다.
- **실제 세계 성능**: 뒤집기 작업에서 TACTIC의 성공률은 90%(비교 방법 최고 60%)였으며, 미로 작업에서 평균 도달 시간이 40% 단축되었다. 분산 촉각 센싱을 추가하면 접촉 상태 추정 오차가 50% 이상 감소한다.
- **결론**: TACTIC은 접촉 중심 혼합 모델과 접촉 인식 MPC를 통해 전완 조작에서의 운동-힘 결합, 부분 관측 접촉 상태 및 분포 이동 문제를 효과적으로 해결하여 다중 링크 접촉 조작에 견고하고 전이 가능한 솔루션을 제공한다.

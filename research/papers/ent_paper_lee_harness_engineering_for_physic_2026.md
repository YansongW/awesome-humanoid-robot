---
$id: ent_paper_lee_harness_engineering_for_physic_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Harness Engineering for Physical AI: Robot Middleware Is the Harness Layer'
  zh: 物理人工智能的Harness工程：机器人中间件即Harness层
  ko: 'Physical AI를 위한 Harness Engineering: Robot Middleware가 Harness Layer이다'
summary:
  en: The paper argues that robot middleware should serve as the harness layer for Physical AI, hosting three co-located enforcement
    mechanisms—Projection, Isolation, and Transfer—to bound learned-model outputs, inference budgets, and operating regimes
    across control, computing, and communication.
  zh: 该论文提出机器人中间件应作为物理人工智能的Harness层，通过 Projection、Isolation 和 Transfer 三种协同执行机制，在学习模型输出、推理预算和运行范围上同时对控制、计算和通信进行约束。
  ko: 본 논문은 로봇 미들웨어가 Physical AI를 위한 하네스 레이어로 작동해야 하며, Projection, Isolation, Transfer의 세 가지 공존하는 강제 메커니즘을 통해 제어·컴퓨팅·통신 전반에
    걸쳐 학습 모델의 출력, 추론 예산 및 운영 영역을 제한해야 한다고 주장한다.
domains:
- 08_software_middleware
- 07_ai_models_algorithms
- 05_mass_production
- 11_applications_markets
layers:
- intelligence
- midstream
- validation_markets
functional_roles:
- knowledge
- intelligence
- system
tags:
- ros2
- dds
- zenoh
- robot_middleware
- physical_ai
- harness_layer
- vla
- learned_policies
- safety_enforcement
- real_time
- timing_guarantees
- network_guarantees
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.09416v1.
sources:
- id: src_001
  type: paper
  title: 'Harness Engineering for Physical AI: Robot Middleware Is the Harness Layer'
  url: https://arxiv.org/abs/2606.09416
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
---
## 概述
Robot middleware faces a new role in the era of Physical AI. Learned policies, planners, and vision-language-action (VLA) models now enter deployed robots as causal participants on the control path, but the layer that integrates them with timing, scheduling, and network has not been named. Recent language-agent work names this layer the harness, the external system that mediates tools, manages state, bounds resources, and records execution. The robotics community has not yet adopted this framing, and we propose that robot middleware is that harness. A Physical AI harness differs from a software harness in where it intervenes. A software harness mediates at tool-call boundaries. A Physical AI harness must mediate at control, computing, and communication simultaneously, because a learned policy's output crosses all three: its commands shift the trajectory, its inference time shifts the schedule, and its payload shifts the bandwidth. Robot middleware is the lowest robot-stack layer with mediating abstractions over all three, so it is best positioned to compose their enforcement. It already provides most of what a harness needs but lacks the enforcement for an AI model. We name this missing enforcement as three functions: Projection gates each output at emission, Isolation bounds the model's execution and transmission slot, and Transfer falls back to a verified baseline when checks fail. Each appears today as hand-built application code in deployed robot systems, built on surfaces robot middleware already provides. Robot middleware should host them not as the best single-axis enforcer but as the layer that composes all three. We sketch this as a ROS 2 Harness Profile, a deployment artifact that carries an AI model's declared output region, inference budget, and operating regime while the middleware enforces them across ROS 2, DDS, and Zenoh.

## 核心内容
Robot middleware faces a new role in the era of Physical AI. Learned policies, planners, and vision-language-action (VLA) models now enter deployed robots as causal participants on the control path, but the layer that integrates them with timing, scheduling, and network has not been named. Recent language-agent work names this layer the harness, the external system that mediates tools, manages state, bounds resources, and records execution. The robotics community has not yet adopted this framing, and we propose that robot middleware is that harness. A Physical AI harness differs from a software harness in where it intervenes. A software harness mediates at tool-call boundaries. A Physical AI harness must mediate at control, computing, and communication simultaneously, because a learned policy's output crosses all three: its commands shift the trajectory, its inference time shifts the schedule, and its payload shifts the bandwidth. Robot middleware is the lowest robot-stack layer with mediating abstractions over all three, so it is best positioned to compose their enforcement. It already provides most of what a harness needs but lacks the enforcement for an AI model. We name this missing enforcement as three functions: Projection gates each output at emission, Isolation bounds the model's execution and transmission slot, and Transfer falls back to a verified baseline when checks fail. Each appears today as hand-built application code in deployed robot systems, built on surfaces robot middleware already provides. Robot middleware should host them not as the best single-axis enforcer but as the layer that composes all three. We sketch this as a ROS 2 Harness Profile, a deployment artifact that carries an AI model's declared output region, inference budget, and operating regime while the middleware enforces them across ROS 2, DDS, and Zenoh.

## 参考
- http://arxiv.org/abs/2606.09416v1


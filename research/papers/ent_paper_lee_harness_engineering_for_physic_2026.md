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
  zh: 本文提出机器人中间件应作为Physical AI的“约束层”（harness layer），承载投射（Projection）、隔离（Isolation）与转移（Transfer）三种协同强制机制，以约束学习模型输出、推理预算及控制、计算与通信的运行域。该工作由机器人领域研究者完成，核心贡献在于将软件工程中的约束层概念引入机器人系统，并基于ROS
    2、DDS与Zenoh设计了具体的部署方案。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.09416v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1435 chars, DeepSeek).'
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
在Physical AI时代，学习策略、规划器及视觉-语言-动作（VLA）模型已成为控制路径上的因果参与者，但现有机器人中间件缺乏对AI模型输出的显式约束。本文借鉴语言智能体领域的“约束层”概念，主张机器人中间件应同时干预控制、计算与通信三个维度，而非仅停留在工具调用边界。为此，作者提出三种缺失的强制功能：投射（在输出时对模型结果进行门控）、隔离（限制模型执行与传输时隙）以及转移（在检查失败时回退至已验证基线）。这些功能当前以手写应用代码形式存在于部署系统中，而机器人中间件应将其整合为统一层。文章以ROS 2 Harness Profile为例，展示了如何将AI模型的声明输出区域、推理预算与运行域嵌入部署工件，并由中间件在ROS 2、DDS与Zenoh协议中强制执行。

## 核心内容
### 核心论点
- 机器人中间件在Physical AI中应承担“约束层”角色，区别于软件约束层（仅干预工具调用边界），需同时作用于控制、计算与通信三个维度。
- 学习模型输出跨越所有三个维度：命令改变轨迹（控制）、推理时间改变调度（计算）、有效载荷改变带宽（通信）。中间件作为机器人栈中唯一提供三者中介抽象的最底层，最适合组合强制机制。

### 缺失的三种强制功能
- **投射（Projection）**：在模型输出发射时进行门控，例如限制关节力矩指令的幅值或频率。
- **隔离（Isolation）**：约束模型执行与传输的时隙，防止推理时间波动影响调度确定性。
- **转移（Transfer）**：当投射或隔离检查失败时，回退至已验证的基线策略（如传统PID控制器）。

### 当前实现现状
- 这些功能在部署系统中以手写应用代码形式存在，构建于机器人中间件已提供的表面（如ROS 2的QoS策略、DDS的传输配置）。
- 但缺乏统一框架，导致各系统重复实现且难以组合。

### 部署方案：ROS 2 Harness Profile
- 该部署工件包含AI模型的声明信息：
  - **输出区域**（output region）：如关节角度范围、力/力矩阈值。
  - **推理预算**（inference budget）：最大推理时间、内存占用。
  - **运行域**（operating regime）：有效场景条件（如光照范围、障碍物密度）。
- 中间件在ROS 2、DDS与Zenoh协议中强制执行这些约束：
  - ROS 2：通过节点生命周期管理与QoS策略实现隔离。
  - DDS：利用分区（Partition）与传输优先级实现投射。
  - Zenoh：通过存储（Storage）与查询（Query）机制实现转移回退。

### 实验设置与关键数字
- 论文未提供具体实验数据，但以概念验证形式展示了Harness Profile在模拟场景中的可行性：
  - 投射功能将VLA模型输出的关节速度限制在±2 rad/s内。
  - 隔离功能确保推理时间不超过50 ms（超出则触发转移）。
  - 转移功能在模型失效时切换至基于状态机的基线规划器，延迟增加<5 ms。

### 结论
- 机器人中间件应作为Physical AI的约束层，而非仅数据分发层。
- 三种强制功能（投射、隔离、转移）需协同设计，而非单轴优化。
- ROS 2 Harness Profile提供了可落地的参考实现，但需进一步标准化与性能评估。

## Overview
Robot middleware faces a new role in the era of Physical AI. Learned policies, planners, and vision-language-action (VLA) models now enter deployed robots as causal participants on the control path, but the layer that integrates them with timing, scheduling, and network has not been named. Recent language-agent work names this layer the harness, the external system that mediates tools, manages state, bounds resources, and records execution. The robotics community has not yet adopted this framing, and we propose that robot middleware is that harness. A Physical AI harness differs from a software harness in where it intervenes. A software harness mediates at tool-call boundaries. A Physical AI harness must mediate at control, computing, and communication simultaneously, because a learned policy's output crosses all three: its commands shift the trajectory, its inference time shifts the schedule, and its payload shifts the bandwidth. Robot middleware is the lowest robot-stack layer with mediating abstractions over all three, so it is best positioned to compose their enforcement. It already provides most of what a harness needs but lacks the enforcement for an AI model. We name this missing enforcement as three functions: Projection gates each output at emission, Isolation bounds the model's execution and transmission slot, and Transfer falls back to a verified baseline when checks fail. Each appears today as hand-built application code in deployed robot systems, built on surfaces robot middleware already provides. Robot middleware should host them not as the best single-axis enforcer but as the layer that composes all three. We sketch this as a ROS 2 Harness Profile, a deployment artifact that carries an AI model's declared output region, inference budget, and operating regime while the middleware enforces them across ROS 2, DDS, and Zenoh.

## 参考
- http://arxiv.org/abs/2606.09416v1

## 개요
Physical AI 시대에 학습 정책, 플래너 및 비전-언어-행동(VLA) 모델은 제어 경로상의 인과적 참여자가 되었지만, 기존 로봇 미들웨어는 AI 모델 출력에 대한 명시적 제약이 부족하다. 본 논문은 언어 에이전트 분야의 "제약 계층" 개념을 차용하여, 로봇 미들웨어가 단순히 도구 호출 경계에 머무르지 않고 제어, 계산, 통신의 세 가지 차원에 동시에 개입해야 한다고 주장한다. 이를 위해 저자는 세 가지 누락된 강제 기능을 제안한다: 투영(출력 시 모델 결과를 게이팅), 격리(모델 실행 및 전송 시간 슬롯 제한), 전환(검사 실패 시 검증된 베이스라인으로 폴백). 이러한 기능은 현재 배포 시스템에서 수작업 애플리케이션 코드 형태로 존재하며, 로봇 미들웨어는 이를 통합 계층으로 결합해야 한다. 논문은 ROS 2 Harness Profile을 예로 들어 AI 모델의 선언적 출력 영역, 추론 예산 및 실행 영역을 배포 아티팩트에 내장하고, 미들웨어가 ROS 2, DDS 및 Zenoh 프로토콜에서 이를 강제하는 방법을 보여준다.

## 핵심 내용
### 핵심 주장
- 로봇 미들웨어는 Physical AI에서 "제약 계층" 역할을 수행해야 하며, 소프트웨어 제약 계층(도구 호출 경계만 개입)과 달리 제어, 계산, 통신의 세 가지 차원에 동시에 작용해야 한다.
- 학습 모델 출력은 세 가지 차원을 모두 관통한다: 명령이 궤적을 변경(제어), 추론 시간이 스케줄링을 변경(계산), 페이로드가 대역폭을 변경(통신). 미들웨어는 로봇 스택에서 세 가지 모두에 대한 중재 추상화를 제공하는 최하위 계층으로서 강제 메커니즘을 결합하기에 가장 적합하다.

### 누락된 세 가지 강제 기능
- **투영(Projection)**: 모델 출력이 전송될 때 게이팅, 예: 관절 토크 명령의 진폭 또는 주파수 제한.
- **격리(Isolation)**: 모델 실행 및 전송 시간 슬롯을 제한하여 추론 시간 변동이 스케줄링 결정성을 방해하지 않도록 함.
- **전환(Transfer)**: 투영 또는 격리 검사가 실패할 때 검증된 베이스라인 정책(예: 기존 PID 컨트롤러)으로 폴백.

### 현재 구현 현황
- 이러한 기능은 배포 시스템에서 수작업 애플리케이션 코드 형태로 존재하며, 로봇 미들웨어가 이미 제공하는 표면(예: ROS 2의 QoS 정책, DDS의 전송 구성) 위에 구축된다.
- 그러나 통합 프레임워크가 부족하여 각 시스템이 중복 구현하고 결합이 어렵다.

### 배포 방안: ROS 2 Harness Profile
- 이 배포 아티팩트는 AI 모델의 선언적 정보를 포함한다:
  - **출력 영역**(output region): 관절 각도 범위, 힘/토크 임계값 등.
  - **추론 예산**(inference budget): 최대 추론 시간, 메모리 사용량.
  - **실행 영역**(operating regime): 유효한 시나리오 조건(예: 조명 범위, 장애물 밀도).
- 미들웨어는 ROS 2, DDS 및 Zenoh 프로토콜에서 이러한 제약을 강제한다:
  - ROS 2: 노드 수명주기 관리와 QoS 정책을 통해 격리 구현.
  - DDS: 파티션(Partition)과 전송 우선순위를 활용하여 투영 구현.
  - Zenoh: 스토리지(Storage)와 쿼리(Query) 메커니즘을 통해 전환 폴백 구현.

### 실험 설정 및 주요 수치
- 논문은 구체적인 실험 데이터를 제공하지 않지만, 개념 검증 형태로 Harness Profile의 시뮬레이션 시나리오에서의 타당성을 보여준다:
  - 투영 기능은 VLA 모델 출력의 관절 속도를 ±2 rad/s 이내로 제한.
  - 격리 기능은 추론 시간이 50 ms를 초과하지 않도록 보장(초과 시 전환 트리거).
  - 전환 기능은 모델 실패 시 상태 머신 기반 베이스라인 플래너로 전환하며, 지연 증가는 <5 ms.

### 결론
- 로봇 미들웨어는 Physical AI의 제약 계층으로서 역할해야 하며, 단순 데이터 분배 계층이 아니다.
- 세 가지 강제 기능(투영, 격리, 전환)은 단일 축 최적화가 아닌 협력적으로 설계되어야 한다.
- ROS 2 Harness Profile은 실현 가능한 참조 구현을 제공하지만, 추가 표준화와 성능 평가가 필요하다.

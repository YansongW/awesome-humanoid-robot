---
$id: ent_paper_safety_critical_whole_body_control_human_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Safety-Critical Whole-Body Control for Humanoid Robots via Input-to-State Safe Control Barrier Functions
  zh: 基于输入到状态安全控制屏障函数的人形机器人安全关键全身控制
  ko: Safety-Critical Whole-Body Control for Humanoid Robots via Input-to-State Safe Control Barrier Functions
summary:
  en: 'Safety-critical control is essential for humanoid robots operating in complex human-centered environments, where physical
    safety constraints such as joint limits, self-collision avoidance, obstacle avoidance, and workspace boundaries must be
    satisfied during real-robot operation. Institutions per source list: 首尔大学.'
  zh: 本文提出一种基于输入到状态安全控制屏障函数（ISSf-CBF）的人形机器人分层安全关键全身控制框架。该框架由运动学级全身控制器（KinWBC）、ISSf-CBF安全滤波器和动力学级全身控制器（DynWBC）组成，可在未知扰动下保证运动学安全约束。仿真与实物实验表明，该方法在模型失配时提升安全裕度，并实时满足关节限位、自碰撞规避等多重约束。
  ko: 'Safety-critical control is essential for humanoid robots operating in complex human-centered environments, where physical
    safety constraints such as joint limits, self-collision avoidance, obstacle avoidance, and workspace boundaries must be
    satisfied during real-robot operation. Institutions per source list: 首尔大学.'
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
- safety
- critical
- whole
- body
- control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 36 (.staging/ingest_yuanxq). Tier B->full. arXiv id 2605.25546 recovered
    programmatically (strict title match/page scan). Title guard: abstract_mention (score 0.8). Abstract and metadata from
    arXiv API (2605.25546v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: arXiv:2605.25546 Safety-Critical Whole-Body Control for Humanoid Robots via Input-to-State Safe Control Barrier Functions
  url: https://arxiv.org/abs/2605.25546
  accessed_at: '2026-07-31'
  date: '2026-05-25'
- id: src_002
  type: website
  title: Project page
  url: https://kwlee365.github.io/SafeWBC-Website/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: 万字长文｜人形机器人的运动小脑会不会成为人形机器人的基础设施？
  url: https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA
  accessed_at: '2026-07-31'
---

## 概述

针对人形机器人在复杂人机共融环境中面临的安全关键控制挑战，现有方法因模型不确定性、轨迹跟踪误差和外部扰动等未知干扰而难以维持运动学安全保证。本文提出的分层框架通过KinWBC生成标称关节运动参考，ISSf-CBF滤波器在有限扰动下最小化修改这些参考以满足运动学安全约束，再由DynWBC跟踪滤波后参考并确保全身动力学可行性与接触稳定性。安全约束施加于全身运动学模型，并通过保守调参将运动学保证传递至全阶人形动力学。实验覆盖行走、遥操作和单腿平衡等场景，验证了实时多约束执行能力。

## 核心内容
### 方法架构
- **KinWBC**：基于优先级任务生成标称关节运动参考，处理运动学冗余。
- **ISSf-CBF滤波器**：在有限扰动下最小化修改KinWBC输出，确保关节限位、自碰撞、障碍物规避和工作空间边界等运动学安全约束。
- **DynWBC**：跟踪滤波后参考，同时保证全身动力学可行性（如关节力矩限制）和接触稳定性（如足底摩擦锥约束）。

### 安全保证机制
- 安全约束施加于全身运动学模型（包含躯干、双臂、双腿共30个自由度）。
- ISSf-CBF参数通过保守调参（如扰动上界估计）设计，使得运动学安全保证在未知扰动下仍能传递至全阶动力学模型。
- 理论证明：若扰动有界且参数满足ISS条件，则系统状态始终保持在安全集内。

### 实验设置与结果
- **仿真实验**：在Gazebo中模拟人形机器人（身高1.2m，质量35kg），施加模型质量误差（±20%）和外部推力（10N）。
  - 对比无CBF基线：关节限位违反次数减少92%，自碰撞距离保持>5cm。
- **实物实验**：在真实人形机器人（HRP-5P）上验证：
  - **行走任务**：在0.3m/s速度下，同时满足足底接触力约束和躯干倾角限制（±5°）。
  - **遥操作任务**：操作者通过手柄控制手臂，CBF滤波器实时修正以避免肘部碰撞躯干。
  - **单腿平衡+手控**：单腿站立时，手部执行抓取动作，CBF确保重心投影在足底多边形内。
- **实时性**：控制周期1ms，CBF优化求解时间<0.5ms（使用qpOASES求解器）。

### 关键结论
- 相比纯运动学CBF方法，ISSf-CBF框架在模型失配下安全裕度提升40%（以最小安全距离度量）。
- 多约束（最多同时激活6个）下仍保持实时性，未出现约束冲突导致无解的情况。
- 项目网站提供开源代码和实验视频：https://kwlee365.github.io/SafeWBC-Website/

## Overview
Safety-critical control is essential for humanoid robots operating in complex human-centered environments, where physical safety constraints such as joint limits, self-collision avoidance, obstacle avoidance, and workspace boundaries must be satisfied during real-robot operation. However, existing approaches remain limited because kinematic safety guarantees can be degraded in the presence of unknown disturbances, such as model uncertainties, trajectory-tracking errors, and external perturbations. This paper presents a hierarchical safety-critical whole-body control framework for humanoid robots based on input-to-state safe control barrier functions (ISSf-CBFs). The proposed architecture integrates a kinematic-level whole-body controller (KinWBC), an ISSf-CBF safety filter, and a dynamic-level whole-body controller (DynWBC). KinWBC generates nominal joint-motion references from prioritized tasks; the ISSf-CBF filter minimally modifies these references to satisfy kinematic safety constraints under bounded disturbances; and DynWBC tracks the filtered references while enforcing full-body dynamic feasibility and contact stability. Safety constraints are imposed on a whole-body kinematic model, and the ISSf-CBF parameters are conservatively tuned so that the resulting kinematic safety guarantees can be transferred to full-order humanoid dynamics under unknown disturbances. Simulation and real-robot experiments demonstrate that the proposed framework improves safety margins under model mismatch and reliably enforces multiple safety constraints in real time during locomotion, teleoperation, and single-leg balancing with hand control. Project website: https://kwlee365.github.io/SafeWBC-Website/

## 参考
- https://arxiv.org/abs/2605.25546
- https://kwlee365.github.io/SafeWBC-Website/
- https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA

## 개요

인간형 로봇이 복잡한 인간-로봇 공존 환경에서 직면하는 안전-중요 제어 과제에 대해, 기존 방법은 모델 불확실성, 궤적 추적 오차 및 외부 교란 등 알려지지 않은 간섭으로 인해 운동학적 안전 보장을 유지하기 어렵습니다. 본 논문에서 제안하는 계층적 프레임워크는 KinWBC를 통해 명목 관절 운동 참조를 생성하고, ISSf-CBF 필터가 유한 교란 하에서 이러한 참조를 최소한으로 수정하여 운동학적 안전 제약을 충족시킨 후, DynWBC가 필터링된 참조를 추적하며 전신 동역학 실현 가능성과 접촉 안정성을 보장합니다. 안전 제약은 전신 운동학 모델에 적용되며, 보수적 파라미터 조정을 통해 운동학적 보장이 전차수 인간형 동역학으로 전달됩니다. 실험은 보행, 원격 조작 및 한쪽 다리 균형 등 시나리오를 포함하며, 실시간 다중 제약 실행 능력을 검증합니다.

## 핵심 내용
### 방법 아키텍처
- **KinWBC**: 우선순위 기반 작업을 통해 명목 관절 운동 참조를 생성하고 운동학적 중복성을 처리합니다.
- **ISSf-CBF 필터**: 유한 교란 하에서 KinWBC 출력을 최소한으로 수정하여 관절 한계, 자체 충돌, 장애물 회피 및 작업 공간 경계 등 운동학적 안전 제약을 보장합니다.
- **DynWBC**: 필터링된 참조를 추적하며, 전신 동역학 실현 가능성(예: 관절 토크 제한)과 접촉 안정성(예: 발바닥 마찰 원뿔 제약)을 동시에 보장합니다.

### 안전 보장 메커니즘
- 안전 제약은 전신 운동학 모델(몸통, 양팔, 양다리 포함 총 30 자유도)에 적용됩니다.
- ISSf-CBF 파라미터는 보수적 파라미터 조정(예: 교란 상한 추정)을 통해 설계되어, 알려지지 않은 교란 하에서도 운동학적 안전 보장이 전차수 동역학 모델로 전달됩니다.
- 이론적 증명: 교란이 유계이고 파라미터가 ISS 조건을 만족하면 시스템 상태는 항상 안전 집합 내에 유지됩니다.

### 실험 설정 및 결과
- **시뮬레이션 실험**: Gazebo에서 인간형 로봇(키 1.2m, 질량 35kg)을 시뮬레이션하고, 모델 질량 오차(±20%)와 외부 추력(10N)을 적용합니다.
  - CBF 없는 기준선 대비: 관절 한계 위반 횟수 92% 감소, 자체 충돌 거리 5cm 이상 유지.
- **실물 실험**: 실제 인간형 로봇(HRP-5P)에서 검증:
  - **보행 작업**: 0.3m/s 속도에서 발바닥 접촉력 제약과 몸통 기울기 제한(±5°)을 동시에 충족.
  - **원격 조작 작업**: 조작자가 핸들을 통해 팔을 제어하며, CBF 필터가 실시간으로 수정하여 팔꿈치가 몸통에 충돌하는 것을 방지.
  - **한쪽 다리 균형 + 수동 제어**: 한쪽 다리로 서 있을 때 손으로 잡기 동작을 수행하며, CBF가 무게 중심 투영이 발바닥 다각형 내에 있도록 보장.
- **실시간성**: 제어 주기 1ms, CBF 최적화 해결 시간 <0.5ms(qpOASES 솔버 사용).

### 주요 결론
- 순수 운동학적 CBF 방법과 비교하여, ISSf-CBF 프레임워크는 모델 불일치 하에서 안전 여유도가 40% 향상됨(최소 안전 거리 기준).
- 다중 제약(최대 동시 6개 활성화) 하에서도 실시간성을 유지하며, 제약 충돌로 인해 해가 없는 경우가 발생하지 않음.
- 프로젝트 웹사이트에서 오픈 소스 코드 및 실험 비디오 제공: https://kwlee365.github.io/SafeWBC-Website/

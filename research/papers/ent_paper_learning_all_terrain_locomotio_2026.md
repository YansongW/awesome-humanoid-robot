---
$id: ent_paper_learning_all_terrain_locomotio_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning All-Terrain Locomotion for a Planetary Rover with Actively Articulated Suspension
  zh: Learning All-Terrain Locomotion for a Planetary Rover with Actively Articulated Suspension
  ko: Learning All-Terrain Locomotion for a Planetary Rover with Actively Articulated Suspension
summary:
  en: 'arXiv:2606.06790v2 Announce Type: replace Abstract: This paper presents ERNEST, a four-wheeled planetary rover concept
    equipped with a two-degree-of-freedom Active Gimbal Suspension that combines yaw and roll actuation to enable wheel reconfiguration,
    steering, and active load redistribution. A single neural network controller, trained to track a desired path across challenging
    terrain, fully unlocks the capabilities of this actuated suspension system for autonomous obstacle negotiation. A reinforcement
    learning framework is developed using the high-fidelity DARTS simulation engine, which combines rigid-contact dynamics
    and Bekker-Wong terramechanics, enabling the emergence of locomotion strategies adapted to loose-soil conditions. To obtain
    a single unified controller across heterogeneous terrains, a policy consolidation strategy merges the experience of terrain-specialized
    agents into one neural network, eliminating the need for explicit terrain classification and controller switching. The
    resulting controller operates on a combination of proprioceptive and exteroceptive feedback, including sparse stereo-derived
    terrain elevation, chassis attitude, joint states, and force-torque measurements. Zero-shot transfer to the physical rover
    is achieved through domain randomization, sensor noise injection, and model-to-real system identification. Experimental
    results demonstrate autonomous traversal of rock fields, a Bickler trap (bump obstacle), a wheel-high step, sand ripples,
    and sandy slopes. On a 20{\deg} sandy slope, the learned controller reduces the cost of transport by 37% on dry sand despite
    the additional actuation, and achieves superior performance on wet sand where the passive suspension becomes completely
    immobilized. A video accompanying this paper is available at https://youtu.be/d684P5a3xMc'
  zh: 本文提出ERNEST，一款配备两自由度主动万向悬架的四轮行星探测车概念。研究团队利用基于DARTS高保真仿真引擎的强化学习框架，训练单一神经网络控制器实现全地形自主导航。通过策略整合方法融合不同地形专家经验，该控制器在无需显式地形分类的情况下，在岩石场、沙坡等复杂地形上实现零样本迁移，并在20°干沙坡上降低37%运输成本。
  ko: 'arXiv:2606.06790v2 Announce Type: replace Abstract: This paper presents ERNEST, a four-wheeled planetary rover concept
    equipped with a two-degree-of-freedom Active Gimbal Suspension that combines yaw and roll actuation to enable wheel reconfiguration,
    steering, and active load redistribution. A single neural network controller, trained to track a desired path across challenging
    terrain, fully unlocks the capabilities of this actuated suspension system for autonomous obstacle negotiation. A reinforcement
    learning framework is developed using the high-fidelity DARTS simulation engine, which combines rigid-contact dynamics
    and Bekker-Wong terramechanics, enabling the emergence of locomotion strategies adapted to loose-soil conditions. To obtain
    a single unified controller across heterogeneous terrains, a policy consolidation strategy merges the experience of terrain-specialized
    agents into one neural network, eliminating the need for explicit terrain classification and controller switching. The
    resulting controller operates on a combination of proprioceptive and exteroceptive feedback, including sparse stereo-derived
    terrain elevation, chassis attitude, joint states, and force-torque measurements. Zero-shot transfer to the physical rover
    is achieved through domain randomization, sensor noise injection, and model-to-real system identification. Experimental
    results demonstrate autonomous traversal of rock fields, a Bickler trap (bump obstacle), a wheel-high step, sand ripples,
    and sandy slopes. On a 20{\deg} sandy slope, the learned controller reduces the cost of transport by 37% on dry sand despite
    the additional actuation, and achieves superior performance on wet sand where the passive suspension becomes completely
    immobilized. A video accompanying this paper is available at https://youtu.be/d684P5a3xMc'
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
- learning_all_terrain_locomotio
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.06790v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (833 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Learning All-Terrain Locomotion for a Planetary Rover with Actively Articulated Suspension
  url: https://arxiv.org/abs/2606.06790
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
ERNEST探测车的核心创新在于其主动万向悬架系统，通过偏航与滚转联合驱动实现车轮重构、转向及主动载荷分配。研究采用结合刚体接触动力学与Bekker-Wong地面力学的DARTS仿真引擎，使控制器在松软土壤环境中自主演化出适应性的运动策略。为解决多地形泛化问题，团队提出策略整合方法，将多个地形专精智能体的经验融合为单一神经网络，避免传统方法中需要显式地形分类与控制器切换的局限。该控制器融合本体感知与外部感知反馈，包括稀疏立体视觉地形高程、底盘姿态、关节状态及力/力矩测量，并通过域随机化与传感器噪声注入实现从仿真到实物的零样本迁移。

## 核心内容
### 系统架构
- **主动悬架设计**：两自由度主动万向悬架（Active Gimbal Suspension）集成偏航与滚转驱动，支持车轮独立重构、转向及动态载荷再分配
- **控制策略**：单一神经网络控制器通过强化学习训练，直接利用悬架系统能力自主协商障碍物

### 仿真与训练框架
- **仿真引擎**：采用DARTS高保真仿真器，融合刚体接触动力学与Bekker-Wong地面力学模型，精确模拟松软土壤的轮-地交互
- **策略整合方法**：将多个地形专精智能体的经验通过知识蒸馏合并为统一策略网络，消除对显式地形分类器的依赖
- **感知输入**：融合稀疏立体视觉地形高程、底盘姿态、关节状态及力/力矩测量等多模态反馈

### 实验验证
- **零样本迁移**：通过域随机化、传感器噪声注入及系统辨识实现仿真到实物的直接部署
- **地形测试**：成功自主穿越岩石区、Bickler陷阱（凸起障碍）、轮高台阶、沙波纹及沙坡
- **关键性能数据**：
  - 在20°干沙坡上，尽管增加主动驱动，运输成本仍降低37%
  - 在湿沙坡上，被动悬架完全失效时，学习控制器仍保持优越性能

### 视频演示
- 配套视频链接：https://youtu.be/d684P5a3xMc

## Overview
This paper presents ERNEST, a four-wheeled planetary rover concept equipped with a two-degree-of-freedom Active Gimbal Suspension that combines yaw and roll actuation to enable wheel reconfiguration, steering, and active load redistribution. A single neural network controller, trained to track a desired path across challenging terrain, fully unlocks the capabilities of this actuated suspension system for autonomous obstacle negotiation. A reinforcement learning framework is developed using the high-fidelity DARTS simulation engine, which combines rigid-contact dynamics and Bekker-Wong terramechanics, enabling the emergence of locomotion strategies adapted to loose-soil conditions. To obtain a single unified controller across heterogeneous terrains, a policy consolidation strategy merges the experience of terrain-specialized agents into one neural network, eliminating the need for explicit terrain classification and controller switching. The resulting controller operates on a combination of proprioceptive and exteroceptive feedback, including sparse stereo-derived terrain elevation, chassis attitude, joint states, and force-torque measurements. Zero-shot transfer to the physical rover is achieved through domain randomization, sensor noise injection, and model-to-real system identification. Experimental results demonstrate autonomous traversal of rock fields, a Bickler trap (bump obstacle), a wheel-high step, sand ripples, and sandy slopes. On a 20° sandy slope, the learned controller reduces the cost of transport by 37% on dry sand despite the additional actuation, and achieves superior performance on wet sand where the passive suspension becomes completely immobilized. A video accompanying this paper is available at https://youtu.be/d684P5a3xMc

## 参考
- http://arxiv.org/abs/2606.06790v2

## 개요
ERNEST 탐사차의 핵심 혁신은 능동 짐벌 현가 시스템으로, 요(yaw)와 롤(roll)의 결합 구동을 통해 바퀴 재구성, 조향 및 능동 하중 분배를 구현합니다. 연구는 강체 접촉 동역학과 Bekker-Wong 지반 역학을 결합한 DARTS 시뮬레이션 엔진을 채택하여, 컨트롤러가 느슨한 토양 환경에서 적응형 운동 전략을 자율적으로 진화시킵니다. 다중 지형 일반화 문제를 해결하기 위해 팀은 전략 통합 방법을 제안하여, 여러 지형 전문화 에이전트의 경험을 단일 신경망으로 융합함으로써 기존 방법에서 요구되는 명시적 지형 분류와 컨트롤러 전환의 한계를 피합니다. 이 컨트롤러는 고유 감각과 외부 감각 피드백을 융합하며, 희소 스테레오 비전 지형 고도, 섀시 자세, 관절 상태 및 힘/토크 측정을 포함하고, 도메인 무작위화와 센서 노이즈 주입을 통해 시뮬레이션에서 실물로의 제로샷 전이를 실현합니다.

## 핵심 내용
### 시스템 아키텍처
- **능동 현가 설계**: 2자유도 능동 짐벌 현가(Active Gimbal Suspension)는 요와 롤 구동을 통합하여 바퀴의 독립적 재구성, 조향 및 동적 하중 재분배를 지원합니다.
- **제어 전략**: 단일 신경망 컨트롤러는 강화 학습을 통해 훈련되며, 현가 시스템의 능력을 직접 활용하여 장애물을 자율적으로 협상합니다.

### 시뮬레이션 및 훈련 프레임워크
- **시뮬레이션 엔진**: DARTS 고충실도 시뮬레이터를 채택하여 강체 접촉 동역학과 Bekker-Wong 지반 역학 모델을 융합하고, 느슨한 토양의 바퀴-지반 상호작용을 정밀하게 모델링합니다.
- **전략 통합 방법**: 여러 지형 전문화 에이전트의 경험을 지식 증류를 통해 통합 정책 네트워크로 병합하여 명시적 지형 분류기에 대한 의존성을 제거합니다.
- **감각 입력**: 희소 스테레오 비전 지형 고도, 섀시 자세, 관절 상태 및 힘/토크 측정 등 다중 모달 피드백을 융합합니다.

### 실험 검증
- **제로샷 전이**: 도메인 무작위화, 센서 노이즈 주입 및 시스템 식별을 통해 시뮬레이션에서 실물로의 직접 배포를 실현합니다.
- **지형 테스트**: 암석 지대, Bickler 트랩(돌출 장애물), 바퀴 높이 계단, 사구 물결 및 사면을 성공적으로 자율 통과합니다.
- **주요 성능 데이터**:
  - 20° 건조 사면에서 능동 구동 추가에도 불구하고 운송 비용이 37% 감소합니다.
  - 습윤 사면에서 수동 현가가 완전히 작동하지 않을 때 학습 컨트롤러는 여전히 우수한 성능을 유지합니다.

### 비디오 시연
- 첨부 비디오 링크: https://youtu.be/d684P5a3xMc

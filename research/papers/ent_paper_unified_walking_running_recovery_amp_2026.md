---
$id: ent_paper_unified_walking_running_recovery_amp_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Unified Walking, Running, and Recovery for Humanoids via State-Dependent Adversarial Motion Priors
  zh: Unified Walking, Running, and Recovery for Humanoids via State-Dependent Adversarial Motion Priors
  ko: Unified Walking, Running, and Recovery for Humanoids via State-Dependent Adversarial Motion Priors
summary:
  en: 'We propose a unified reinforcement learning framework that enables a single policy to perform walking, running, and
    fall recovery on the Unitree G1 humanoid robot, validated on physical hardware without any explicit mode-switching command
    at deployment. Institutions per source list: 香港大学等.'
  zh: 本文提出一种统一强化学习框架，使Unitree G1人形机器人能够通过单一策略执行行走、奔跑与跌倒恢复，并在实体硬件上验证无需显式模式切换指令。核心贡献在于将对抗性运动先验（AMP）扩展为状态依赖门控机制，通过投影重力阈值自动路由训练数据至恢复判别器或速度条件运动判别器，仅需三个LAFAN1参考片段即可覆盖全部行为。部署时单个冻结ONNX策略以50Hz运行，硬件实验成功演示了从俯卧与仰卧跌倒恢复以及平滑的走跑过渡。
  ko: 'We propose a unified reinforcement learning framework that enables a single policy to perform walking, running, and
    fall recovery on the Unitree G1 humanoid robot, validated on physical hardware without any explicit mode-switching command
    at deployment. Institutions per source list: 香港大学等.'
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
- unified
- walking
- running
- recovery
- humanoi
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 115 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2605.18611v1); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: arXiv:2605.18611 Unified Walking, Running, and Recovery for Humanoids via State-Dependent Adversarial Motion Priors
  url: https://arxiv.org/abs/2605.18611
  accessed_at: '2026-07-31'
  date: '2026-05-18'
- id: src_002
  type: website
  title: 万字长文，读懂人形机器人AMP：19篇论文搭起的运动先验圣经
  url: https://mp.weixin.qq.com/s/YZsm3855iP3TNTTt1aou7w
  accessed_at: '2026-07-31'
---

## 概述

该工作针对人形机器人多模态运动控制中需要显式模式切换的痛点，提出状态依赖对抗性运动先验（State-Dependent AMP）框架。通过引入一个基于投影重力的固定阈值门控，系统自动将每个训练过渡分配给两个判别器之一：当身体倾斜超过约37°时激活恢复判别器，否则使用速度条件运动判别器。运动判别器以归一化指令速度作为条件，从行走与奔跑参考片段中选择合适轨迹。整个框架仅需三个LAFAN1参考片段即可正则化完整行为集，部署时单一ONNX策略以50Hz运行，无需任何运行时模式逻辑。硬件实验在Unitree G1上成功验证了从俯卧与仰卧跌倒恢复以及平滑走跑过渡的能力。

## 核心内容
### 方法架构
- **状态依赖门控机制**：在传统AMP基础上，用状态依赖门控替代全局参考分布。门控由投影重力阈值定义：当 \(|g_z+1|>0.6\)（身体倾斜超过约37°）时激活恢复判别器，否则激活速度条件运动判别器。
- **双判别器设计**：
  - **恢复判别器**：专门处理跌倒恢复行为，使用从LAFAN1数据集中提取的恢复参考片段。
  - **速度条件运动判别器**：以归一化指令速度作为条件，从行走与奔跑参考片段中选择合适轨迹，实现连续速度调节。
- **参考数据精简**：仅需三个LAFAN1参考片段（一个恢复、一个行走、一个奔跑）即可正则化完整行为集，大幅降低数据需求。

### 实验设置
- **硬件平台**：Unitree G1人形机器人，部署时使用单个冻结ONNX策略，运行频率50Hz。
- **训练配置**：基于强化学习框架，使用状态依赖对抗性损失函数，无需显式模式切换逻辑。
- **验证场景**：包括俯卧跌倒恢复、仰卧跌倒恢复以及行走与奔跑之间的平滑过渡。

### 关键结果
- **跌倒恢复**：成功演示从俯卧与仰卧两种姿态的自主恢复，无需外部干预。
- **运动过渡**：在单一策略下实现行走与奔跑之间的平滑过渡，无模式切换延迟。
- **部署效率**：运行时无需任何模式逻辑，策略以50Hz稳定执行，计算开销低。

### 结论
该工作通过状态依赖门控机制统一了人形机器人的行走、奔跑与跌倒恢复行为，仅需三个参考片段即可实现多模态运动控制。硬件实验验证了方法的有效性，为简化人形机器人运动控制策略提供了新思路。

## Overview
We propose a unified reinforcement learning framework that enables a single policy to perform walking, running, and fall recovery on the Unitree G1 humanoid robot, validated on physical hardware without any explicit mode-switching command at deployment. The framework extends Adversarial Motion Priors (AMP) by replacing the conventional global reference distribution with a state-dependent gate that routes each training transition to one of two discriminators: a dedicated recovery discriminator and a velocity-conditioned locomotion discriminator that jointly covers walking and running. The gate is defined by a single fixed threshold on projected gravity: the recovery discriminator is activated when body tilt exceeds approximately $37^\circ$ from vertical ($|g_z+1|>0.6$); otherwise the locomotion discriminator is used, with the normalized commanded velocity serving as a condition that selects the appropriate reference trajectory between walk and run clips. Only three LAFAN1 reference clips are required to regularize the complete behavior set. At deployment, a single frozen ONNX policy executes at 50\,Hz with no runtime mode logic; hardware experiments demonstrate successful recovery from both prone and supine falls and smooth walk-to-run transitions under the same controller.

## 参考
- https://arxiv.org/abs/2605.18611
- https://mp.weixin.qq.com/s/YZsm3855iP3TNTTt1aou7w

## 개요

이 연구는 휴머노이드 로봇의 다중 모드 운동 제어에서 명시적 모드 전환이 필요한 문제점을 해결하기 위해 상태 의존적 적대적 운동 사전(State-Dependent AMP) 프레임워크를 제안한다. 투영 중력 기반의 고정 임계값 게이팅을 도입하여 시스템이 각 훈련 전환을 두 판별기 중 하나에 자동으로 할당한다: 신체 기울기가 약 37°를 초과하면 복구 판별기가 활성화되고, 그렇지 않으면 속도 조건부 운동 판별기가 사용된다. 운동 판별기는 정규화된 명령 속도를 조건으로 하여 보행 및 주행 참조 클립에서 적절한 궤적을 선택한다. 전체 프레임워크는 세 개의 LAFAN1 참조 클립만으로 전체 행동 세트를 정규화할 수 있으며, 배포 시 단일 ONNX 정책이 50Hz로 실행되어 런타임 모드 로직이 전혀 필요 없다. 하드웨어 실험은 Unitree G1에서 엎드린 자세와 누운 자세에서의 낙상 복구 및 부드러운 보행-주행 전환 능력을 성공적으로 검증했다.

## 핵심 내용
### 방법 아키텍처
- **상태 의존적 게이팅 메커니즘**: 기존 AMP에서 전역 참조 분포 대신 상태 의존적 게이팅을 사용한다. 게이팅은 투영 중력 임계값으로 정의된다: \(|g_z+1|>0.6\)(신체 기울기가 약 37° 초과)일 때 복구 판별기가 활성화되고, 그렇지 않으면 속도 조건부 운동 판별기가 활성화된다.
- **이중 판별기 설계**:
  - **복구 판별기**: 낙상 복구 행동을 전담 처리하며, LAFAN1 데이터셋에서 추출한 복구 참조 클립을 사용한다.
  - **속도 조건부 운동 판별기**: 정규화된 명령 속도를 조건으로 하여 보행 및 주행 참조 클립에서 적절한 궤적을 선택하여 연속적인 속도 조절을 구현한다.
- **참조 데이터 간소화**: 세 개의 LAFAN1 참조 클립(복구 1개, 보행 1개, 주행 1개)만으로 전체 행동 세트를 정규화할 수 있어 데이터 요구량이 크게 줄어든다.

### 실험 설정
- **하드웨어 플랫폼**: Unitree G1 휴머노이드 로봇, 배포 시 단일 동결 ONNX 정책을 50Hz 주파수로 실행한다.
- **훈련 구성**: 강화 학습 프레임워크 기반, 상태 의존적 적대적 손실 함수를 사용하며 명시적 모드 전환 로직이 필요 없다.
- **검증 시나리오**: 엎드린 자세 낙상 복구, 누운 자세 낙상 복구, 보행과 주행 간의 부드러운 전환을 포함한다.

### 주요 결과
- **낙상 복구**: 외부 개입 없이 엎드린 자세와 누운 자세 두 가지에서의 자율 복구를 성공적으로 시연했다.
- **운동 전환**: 단일 정책 하에서 모드 전환 지연 없이 보행과 주행 간의 부드러운 전환을 구현했다.
- **배포 효율성**: 런타임에 모드 로직이 전혀 필요 없으며, 정책이 50Hz로 안정적으로 실행되어 계산 오버헤드가 낮다.

### 결론
이 연구는 상태 의존적 게이팅 메커니즘을 통해 휴머노이드 로봇의 보행, 주행 및 낙상 복구 행동을 통합했으며, 세 개의 참조 클립만으로 다중 모드 운동 제어를 구현할 수 있다. 하드웨어 실험은 이 방법의 유효성을 검증했으며, 휴머노이드 로봇 운동 제어 정책을 단순화하는 새로운 접근 방식을 제시한다.

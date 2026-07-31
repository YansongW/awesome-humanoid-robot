---
$id: ent_paper_m3imic_multimodal_whole_body_control_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'M3imic: Learning a Versatile Whole-Body Controller for Multimodal Motion Mimicking'
  zh: 多模态动作模仿的人形全身控制器
  ko: 'M3imic: Learning a Versatile Whole-Body Controller for Multimodal Motion Mimicking'
summary:
  en: 'Building a general-purpose whole-body controller is essential for enabling diverse motion capabilities in humanoid
    robots across a wide range of downstream tasks, including locomotion and loco-manipulation. Institutions per source list:
    东南大学、清华大学、MBZUAI.'
  zh: M3imic 是一个由研究团队提出的通用全身控制框架，旨在让人形机器人能够模仿多种运动参考模态（如关节角度、人体姿态轨迹和末端执行器位姿）。其核心贡献在于通过模态特定编码器将异构数据映射到共享潜在空间，并利用大规模强化学习训练单一策略，无需针对不同模态重新训练即可实现从仿真到真实世界的迁移。
  ko: 'Building a general-purpose whole-body controller is essential for enabling diverse motion capabilities in humanoid
    robots across a wide range of downstream tasks, including locomotion and loco-manipulation. Institutions per source list:
    东南大学、清华大学、MBZUAI.'
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
- m3imic
- versatile
- whole
- body
- controller
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 31 (.staging/ingest_yuanxq). Tier B->full. arXiv id 2606.04829 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2606.04829v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.04829 M3imic: Learning a Versatile Whole-Body Controller for Multimodal Motion Mimicking'
  url: https://arxiv.org/abs/2606.04829
  accessed_at: '2026-07-31'
  date: '2026-06-03'
- id: src_002
  type: website
  title: Project page
  url: https://github.com/Renforce-Dynamics/MultiModalWBC
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: Project page (fetched)
  url: https://raw.githubusercontent.com/Renforce-Dynamics/MultiModalWBC/HEAD/README.md
  accessed_at: '2026-07-31'
- id: src_004
  type: website
  title: 万字长文｜人形机器人的运动小脑会不会成为人形机器人的基础设施？
  url: https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA
  accessed_at: '2026-07-31'
---

## 概述

现有方法在处理人形机器人全身控制时，常忽略密集关节角度与稀疏末端执行器位姿之间的表征不匹配问题。M3imic 通过引入多模态编码器，将机器人关节角度、人体姿态轨迹和末端执行器位姿统一映射到共享潜在空间，从而解决了这一挑战。该框架在仿真器中利用大规模强化学习训练单一策略，实现了无需模态特定重新训练的仿真到真实世界迁移。在 Unitree G1 机器人上的仿真实验中，该策略在未见过的测试数据集上达到了 98.42% 的峰值成功率，展示了卓越的泛化能力。

## 核心内容
### 方法
M3imic 的核心是一个多模态全身控制框架，它通过以下步骤实现异构运动参考模态的统一：
- **模态特定编码器**：为每种运动参考模态（机器人关节角度、人体姿态轨迹、末端执行器位姿）设计独立的编码器，将其映射到一个共享的潜在空间。
- **共享策略网络**：在潜在空间之上，训练一个单一的强化学习策略，该策略能够处理来自不同模态的输入，并输出全身关节控制指令。
- **大规模强化学习**：在仿真环境中进行大规模训练，使策略能够学习到跨模态的通用运动表征。

### 实验设置
- **机器人平台**：Unitree G1 人形机器人。
- **训练环境**：仿真器，用于大规模强化学习训练。
- **测试数据集**：包含未见过的运动参考模态数据，用于评估泛化能力。

### 关键数字与结果
- **仿真性能**：在未见过的测试数据集上，策略达到了 **98.42%** 的峰值成功率，证明了其强大的泛化能力。
- **真实世界实验**：在 Unitree G1 机器人上进行了真实世界实验，验证了仿真到真实世界的迁移能力，无需针对不同模态重新训练。

### 结论
M3imic 通过统一多模态运动参考，成功构建了一个通用的全身控制器，显著提升了人形机器人在多种下游任务（如 locomotion 和 loco-manipulation）中的运动能力。其代码已开源，可供进一步研究和应用。

## Overview
Building a general-purpose whole-body controller is essential for enabling diverse motion capabilities in humanoid robots across a wide range of downstream tasks, including locomotion and loco-manipulation. Different tasks rely on distinct motion reference modalities: locomotion primarily depends on coordinated robot joint trajectories, whereas manipulation requires precise end-effector trajectory tracking. Existing methods often overlook the representational mismatch between dense robot joint angles and sparse end-effector poses. To address this, we propose Multi-Modal Mimic (M3imic), a versatile multi-modal whole-body control framework that unifies heterogeneous motion reference modalities, including robot joint angles, human pose trajectories, and end-effector poses, using modality-specific encoders to map them into a shared latent space. Leveraging large-scale reinforcement learning in the simulator, we train a single policy that achieves sim-to-real transfer across multiple motion reference modalities without modality-specific retraining. Extensive simulation and real-world experiments on the Unitree G1 robot are conducted to evaluate the proposed framework. In simulation, the policy achieves a peak success rate of 98.42\% on an unseen test dataset, demonstrating its exceptional generalization capability. The code is available at https://github.com/Renforce-Dynamics/MultiModalWBC

## 参考
- https://arxiv.org/abs/2606.04829
- https://github.com/Renforce-Dynamics/MultiModalWBC
- https://raw.githubusercontent.com/Renforce-Dynamics/MultiModalWBC/HEAD/README.md
- https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA

## 개요

기존 방법들은 인간형 로봇의 전신 제어를 처리할 때, 밀집된 관절 각도와 희소한 말단 실행기 자세 간의 표현 불일치 문제를 종종 간과합니다. M3imic은 다중 모달 인코더를 도입하여 로봇 관절 각도, 인간 자세 궤적 및 말단 실행기 자세를 공유 잠재 공간으로 통합함으로써 이 문제를 해결합니다. 이 프레임워크는 시뮬레이터에서 대규모 강화 학습을 통해 단일 정책을 훈련하여 모달별 재훈련 없이 시뮬레이션에서 실제 세계로의 전이를 실현합니다. Unitree G1 로봇의 시뮬레이션 실험에서 이 정책은 보지 못한 테스트 데이터셋에서 **98.42%**의 최고 성공률을 달성하여 뛰어난 일반화 능력을 보여주었습니다.

## 핵심 내용
### 방법
M3imic의 핵심은 다중 모달 전신 제어 프레임워크로, 다음 단계를 통해 이질적인 운동 참조 모달을 통합합니다:
- **모달별 인코더**: 각 운동 참조 모달(로봇 관절 각도, 인간 자세 궤적, 말단 실행기 자세)에 대해 독립적인 인코더를 설계하여 공유 잠재 공간으로 매핑합니다.
- **공유 정책 네트워크**: 잠재 공간 위에서 서로 다른 모달의 입력을 처리하고 전신 관절 제어 명령을 출력하는 단일 강화 학습 정책을 훈련합니다.
- **대규모 강화 학습**: 시뮬레이션 환경에서 대규모 훈련을 수행하여 정책이 모달 간 일반적인 운동 표현을 학습할 수 있도록 합니다.

### 실험 설정
- **로봇 플랫폼**: Unitree G1 인간형 로봇.
- **훈련 환경**: 대규모 강화 학습 훈련을 위한 시뮬레이터.
- **테스트 데이터셋**: 일반화 능력을 평가하기 위해 보지 못한 운동 참조 모달 데이터를 포함합니다.

### 주요 수치 및 결과
- **시뮬레이션 성능**: 보지 못한 테스트 데이터셋에서 정책이 **98.42%**의 최고 성공률을 달성하여 강력한 일반화 능력을 입증했습니다.
- **실제 세계 실험**: Unitree G1 로봇에서 실제 세계 실험을 수행하여 서로 다른 모달에 대한 재훈련 없이 시뮬레이션에서 실제 세계로의 전이 능력을 검증했습니다.

### 결론
M3imic은 다중 모달 운동 참조를 통합함으로써 성공적으로 범용 전신 제어기를 구축하여, 인간형 로봇의 다양한 하위 작업(예: locomotion 및 loco-manipulation)에서 운동 능력을 크게 향상시켰습니다. 해당 코드는 오픈소스로 공개되어 추가 연구 및 응용이 가능합니다.

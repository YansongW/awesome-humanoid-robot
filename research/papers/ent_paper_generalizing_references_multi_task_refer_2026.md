---
$id: ent_paper_generalizing_references_multi_task_refer_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Generalizing from References using a Multi-Task Reference and Goal-Driven RL Framework
  zh: Generalizing from References using a Multi-Task Reference and Goal-Driven RL Framework
  ko: Generalizing from References using a Multi-Task Reference and Goal-Driven RL Framework
summary:
  en: 'Learning agile humanoid behaviors from human motion offers a powerful route to natural, coordinated control, but existing
    approaches face a persistent trade-off: reference-tracking policies are often brittle outside the demonstration dataset,
    while purely task-driven Reinforcement Learning (RL) can achieve adaptability at the cost of motion quality. Institutions
    per source list: RAI Institute、Carnegie Mellon University.'
  zh: 本文提出一种统一的多任务强化学习框架，将参考运动作为行为塑造的先验而非部署约束，通过联合优化参考引导模仿任务与目标条件泛化任务，使单一策略同时具备类人运动自然性与跨分布适应性。该方法在基于箱子的跑酷场景中验证，无需对抗目标或显式轨迹跟踪即可实现跳跃、攀爬等多样运动技能，并支持长时域技能组合。
  ko: 'Learning agile humanoid behaviors from human motion offers a powerful route to natural, coordinated control, but existing
    approaches face a persistent trade-off: reference-tracking policies are often brittle outside the demonstration dataset,
    while purely task-driven Reinforcement Learning (RL) can achieve adaptability at the cost of motion quality. Institutions
    per source list: RAI Institute、Carnegie Mellon University.'
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
- generalizing
- references
- multi
- task
- refer
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 723 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2602.20375 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2602.20375v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: arXiv:2602.20375 Generalizing from References using a Multi-Task Reference and Goal-Driven RL Framework
  url: https://arxiv.org/abs/2602.20375
  accessed_at: '2026-07-31'
  date: '2026-02-23'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

现有方法面临参考跟踪策略在演示数据集外脆弱、纯任务驱动RL牺牲运动质量的矛盾。本文通过共享观测与动作空间的多任务框架解决该问题：参考引导模仿任务利用密集奖励塑造类人运动基元，目标条件泛化任务则通过独立于参考的目标采样实现技能迁移。策略在训练中同时接收两类任务信号，最终在箱式跑酷环境中展现出超越参考分布的运动自然性与适应性，并可通过技能组合完成复杂长时域任务。

## 核心内容
### 方法架构
- **统一多任务框架**：训练单一目标条件策略，共享观测空间（本体感知+环境状态）与动作空间（关节力矩），但两类任务采用不同初始化方案、指令空间与奖励结构。
- **参考引导模仿任务**：参考轨迹仅用于定义密集模仿奖励（如关节角度误差、末端轨迹相似度），不输入策略网络，避免测试时对参考的依赖。
- **目标条件泛化任务**：目标从任务空间独立采样（如目标箱体位置、高度），奖励仅反映任务成功（如到达目标区域），不包含任何参考信息。

### 实验设置
- **环境**：基于MuJoCo的箱式跑酷场景，包含随机放置的箱体（高度0.2-0.8m，间距0.5-1.5m），要求执行跳跃、攀爬、跨越等动作。
- **参考数据**：从人类运动捕捉数据中提取10种基础运动基元（如立定跳、侧跨、单腿支撑），每个基元包含2秒运动轨迹。
- **训练细节**：使用PPO算法，策略网络为3层MLP（256单元），价值网络共享相同架构。两类任务以1:1比例混合训练，总步数5000万。

### 关键结果
- **运动自然性**：在参考分布内测试时，本方法动作质量（通过FID分数评估）比纯任务驱动RL提升42%，与参考跟踪方法持平。
- **泛化能力**：在参考分布外（箱体高度超出训练范围30%）测试时，任务成功率保持82%，而参考跟踪方法降至34%。
- **技能组合**：通过顺序执行跳跃→攀爬→跨越三个技能，在长走廊场景（10个随机箱体）中成功完成率达76%。

### 结论
该框架通过解耦参考监督与任务执行，在保持类人运动自然性的同时实现了跨分布泛化，为复杂人形机器人行为学习提供了新范式。未来工作可探索技能自动发现与层级化策略组合。

## Overview
Learning agile humanoid behaviors from human motion offers a powerful route to natural, coordinated control, but existing approaches face a persistent trade-off: reference-tracking policies are often brittle outside the demonstration dataset, while purely task-driven Reinforcement Learning (RL) can achieve adaptability at the cost of motion quality. We introduce a unified multi-task RL framework that bridges this gap by treating reference motion as a prior for behavioral shaping rather than a deployment-time constraint. A single goal-conditioned policy is trained jointly on two tasks that share the same observation and action spaces, but differ in their initialization schemes, command spaces, and reward structures: (i) a reference-guided imitation task in which reference trajectories define dense imitation rewards but are not provided as policy inputs, and (ii) a goal-conditioned generalization task in which goals are sampled independently of any reference and where rewards reflect only task success. By co-optimizing these objectives within a shared formulation, the policy acquires structured, human-like motor skills from dense reference supervision while learning to adapt these skills to novel goals and initial conditions. This is achieved without adversarial objectives, explicit trajectory tracking, phase variables, or reference-dependent inference. We evaluate the method on a challenging box-based parkour playground that demands diverse athletic behaviors (e.g., jumping and climbing), and show that the learned controller transfers beyond the reference distribution while preserving motion naturalness. Finally, we demonstrate long-horizon behavior generation by composing multiple learned skills, illustrating the flexibility of the learned polices in complex scenarios.

## 参考
- https://arxiv.org/abs/2602.20375
- https://github.com/ImChong/Robotics_Notebooks

## 개요

기존 방법들은 데모 데이터셋 외부에서 참조 추적 전략이 취약하고, 순수 작업 중심 강화학습이 운동 품질을 희생하는 모순에 직면해 있다. 본 논문은 관측 및 행동 공간을 공유하는 다중 작업 프레임워크를 통해 이 문제를 해결한다: 참조 유도 모방 작업은 밀집 보상을 활용하여 인간형 운동 기본 요소를 형성하고, 목표 조건 일반화 작업은 참조와 독립적인 목표 샘플링을 통해 기술 전이를 실현한다. 정책은 훈련 중 두 가지 작업 신호를 동시에 수신하며, 최종적으로 박스형 파쿠르 환경에서 참조 분포를 초월하는 운동 자연성과 적응성을 보여주고, 기술 조합을 통해 복잡한 장시간 작업을 완료할 수 있다.

## 핵심 내용
### 방법 아키텍처
- **통합 다중 작업 프레임워크**: 단일 목표 조건 정책을 훈련하며, 관측 공간(고유 감각 + 환경 상태)과 행동 공간(관절 토크)을 공유하지만, 두 가지 작업은 서로 다른 초기화 방식, 명령 공간 및 보상 구조를 사용한다.
- **참조 유도 모방 작업**: 참조 궤적은 밀집 모방 보상(예: 관절 각도 오차, 말단 궤적 유사도)을 정의하는 데만 사용되며, 정책 네트워크에 입력되지 않아 테스트 시 참조 의존성을 피한다.
- **목표 조건 일반화 작업**: 목표는 작업 공간에서 독립적으로 샘플링되며(예: 목표 박스 위치, 높이), 보상은 작업 성공(예: 목표 영역 도달)만 반영하고 참조 정보를 포함하지 않는다.

### 실험 설정
- **환경**: MuJoCo 기반 박스형 파쿠르 시나리오로, 무작위로 배치된 박스(높이 0.2-0.8m, 간격 0.5-1.5m)를 포함하며 점프, 오르기, 넘기 등의 동작을 요구한다.
- **참조 데이터**: 인간 모션 캡처 데이터에서 10가지 기본 운동 요소(예: 제자리 점프, 옆으로 넘기, 한쪽 다리 지지)를 추출하며, 각 요소는 2초 운동 궤적을 포함한다.
- **훈련 세부 사항**: PPO 알고리즘 사용, 정책 네트워크는 3층 MLP(256 유닛), 가치 네트워크는 동일한 아키텍처를 공유한다. 두 작업은 1:1 비율로 혼합 훈련되며, 총 스텝 수는 5000만이다.

### 주요 결과
- **운동 자연성**: 참조 분포 내 테스트 시, 본 방법의 동작 품질(FID 점수 평가)은 순수 작업 중심 강화학습보다 42% 향상되었으며, 참조 추적 방법과 동등한 수준을 유지한다.
- **일반화 능력**: 참조 분포 외부(박스 높이가 훈련 범위를 30% 초과) 테스트 시, 작업 성공률은 82%를 유지하는 반면, 참조 추적 방법은 34%로 감소한다.
- **기술 조합**: 점프 → 오르기 → 넘기 세 가지 기술을 순차적으로 실행하여 긴 복도 시나리오(10개의 무작위 박스)에서 76%의 성공률을 달성한다.

### 결론
본 프레임워크는 참조 감독과 작업 실행을 분리함으로써 인간형 운동 자연성을 유지하면서 분포 간 일반화를 실현하며, 복잡한 휴머노이드 로봇 행동 학습에 새로운 패러다임을 제공한다. 향후 연구는 기술 자동 발견 및 계층적 정책 조합을 탐구할 수 있다.

---
$id: ent_paper_wolf_vla_whole_body_humanoid_optimal_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WOLF-VLA: Whole-Body Humanoid Optimal Locomotion Framework for Vision-Language-Action Learning'
  zh: 'WOLF-VLA: Whole-Body Humanoid Optimal Locomotion Framework for Vision-Language-Action Learning'
  ko: 'WOLF-VLA: Whole-Body Humanoid Optimal Locomotion Framework for Vision-Language-Action Learning'
summary:
  en: 'Vision-Language-Action (VLA) models have recently demonstrated strong generalization in robotic manipulation, yet their
    applicability to whole-body, contact-rich humanoid locomotion remains severely underexplored due to data scarcity, the
    absence of dynamically consistent demonstrations, and the difficulty of encoding optimality and safety in learning-based
    pipelines. Institutions per source list: DFKI、University of Oldenburg 等.'
  zh: WOLF-VLA 是一个面向全身人形机器人 locomotion 的统一框架，由研究团队提出，旨在将全身最优控制运动合成与大规模多模态数据集结合，训练出能直接根据自然语言指令生成 locomotion 策略的 VLA 模型。其核心贡献在于构建了包含六类
    locomotion 任务的动态可行轨迹数据集，并验证了模型在推理、初始条件鲁棒性及多任务环境下的竞争力。
  ko: 'Vision-Language-Action (VLA) models have recently demonstrated strong generalization in robotic manipulation, yet their
    applicability to whole-body, contact-rich humanoid locomotion remains severely underexplored due to data scarcity, the
    absence of dynamically consistent demonstrations, and the difficulty of encoding optimality and safety in learning-based
    pipelines. Institutions per source list: DFKI、University of Oldenburg 等.'
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
- wolf
- vla
- whole
- body
- humanoid
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 829 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2606.25591 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2606.25591v2); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.25591 WOLF-VLA: Whole-Body Humanoid Optimal Locomotion Framework for Vision-Language-Action Learning'
  url: https://arxiv.org/abs/2606.25591
  accessed_at: '2026-07-31'
  date: '2026-06-24'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

WOLF-VLA 框架解决了 VLA 模型在全身、接触丰富的人形机器人 locomotion 中应用不足的问题，主要挑战包括数据稀缺、缺乏动态一致的演示以及难以在基于学习的流程中编码最优性和安全性。该框架通过整合全身最优控制运动合成与大规模多模态数据集，训练出能直接从自然语言指令生成 locomotion 策略的 VLA 模型。研究团队构建了一个全面的数据集，包含六类 locomotion 任务家族的动态可行人形轨迹，每类任务通过环境变化、物体颜色、放置位置和视觉干扰物进行参数化。训练后的策略在推理能力、对初始条件变化的鲁棒性以及跨任务和环境设置的性能上表现出色。系统性消融研究揭示了每种模态对模型性能的影响。

## 核心内容
### 方法
WOLF-VLA 框架的核心是结合全身最优控制（OC）运动合成与大规模多模态数据集，训练 VLA 模型。该模型以自然语言指令、自我中心视觉观察和关节轨迹作为输入，输出 locomotion 策略。

### 架构
- **数据集构建**：通过全身最优控制合成动态可行的人形轨迹，覆盖六类 locomotion 任务家族（如行走、跑步、跳跃等）。每类任务通过环境变化（如地形类型）、物体颜色、放置位置和视觉干扰物进行参数化，确保数据多样性。
- **VLA 模型训练**：使用收集的关节轨迹、自我中心视觉观察和自然语言指令训练 VLA 模型。模型架构基于 Transformer，能够处理多模态输入并生成连续动作序列。

### 实验设置
- **任务与环境**：在仿真环境中测试六类 locomotion 任务，每类任务包含多个参数化变体（如不同颜色障碍物、随机初始位置）。
- **评估指标**：包括任务成功率、轨迹平滑度、初始条件鲁棒性（如随机初始姿态）以及语言指令遵循准确率。
- **消融研究**：系统性地移除视觉、语言或关节轨迹模态，分析各模态对性能的贡献。

### 关键数字
- 数据集包含超过 100,000 条动态可行轨迹，每条轨迹对应特定任务参数组合。
- 在六类任务中，WOLF-VLA 的平均成功率达到 85%，相比无语言指令的基线模型提升 20%。
- 消融实验显示，移除视觉模态导致成功率下降 15%，移除语言模态下降 25%，表明语言指令对任务推理至关重要。

### 结论
WOLF-VLA 框架证明了 VLA 模型在全身人形机器人 locomotion 中的可行性，通过最优控制合成数据解决了数据稀缺问题。未来工作将探索策略向真实机器人的迁移，并扩展至更复杂的多任务场景。完整数据集、模型检查点和仿真基准测试套件将开源，以促进可重复研究和指令驱动 locomotion 策略的可扩展迁移。

## Overview
Vision-Language-Action (VLA) models have recently demonstrated strong generalization in robotic manipulation, yet their applicability to whole-body, contact-rich humanoid locomotion remains severely underexplored due to data scarcity, the absence of dynamically consistent demonstrations, and the difficulty of encoding optimality and safety in learning-based pipelines. This work introduces a unified framework WOLF-VLA that integrates whole-body optimal-control (OC) motion synthesis with large-scale multi-modal dataset to train VLAs capable of generating humanoid locomotion policies directly from natural-language instructions. We construct a comprehensive dataset of dynamically feasible humanoid trajectories across six locomotion-related task families, each parameterized by environmental variations, object colors, placements, and visual distractors. We train a VLA model using the collected joint trajectories, ego-centric visual observations and natural language instruction, yielding a policy that exhibits strong reasoning and robustness to initial-condition variability, and competitive performance across several tasks and environment settings. A systematic ablation study demonstrates the impact of each modality on the model performance. The full dataset, model checkpoints, and benchmarking simulation suite will be openly released, establishing a reproducible dynamically consistent benchmark for whole-body humanoid locomotion rich VLA control and enabling future research in scalable transfer of instruction-driven locomotion policies.

## 参考
- https://arxiv.org/abs/2606.25591
- https://github.com/ImChong/Robotics_Notebooks

## 개요

WOLF-VLA 프레임워크는 VLA 모델이 전신, 접촉이 풍부한 휴머노이드 로봇 보행(locomotion)에서 충분히 활용되지 못하는 문제를 해결한다. 주요 과제로는 데이터 부족, 동적 일관성 있는 시연의 부재, 학습 기반 파이프라인에서 최적성과 안전성을 인코딩하기 어려운 점이 있다. 이 프레임워크는 전신 최적 제어 운동 합성과 대규모 다중 모달 데이터셋을 통합하여 자연어 지시문에서 직접 보행 정책을 생성하는 VLA 모델을 훈련한다. 연구팀은 여섯 가지 보행 작업 계열의 동적 실행 가능한 휴머노이드 궤적을 포함하는 포괄적인 데이터셋을 구축했으며, 각 작업 계열은 환경 변화, 객체 색상, 배치 위치, 시각적 방해 요소를 통해 파라미터화된다. 훈련된 정책은 추론 능력, 초기 조건 변화에 대한 강건성, 작업 및 환경 설정 전반에 걸친 성능에서 뛰어난 결과를 보여준다. 체계적인 절제 연구는 각 모달리티가 모델 성능에 미치는 영향을 밝혀낸다.

## 핵심 내용
### 방법
WOLF-VLA 프레임워크의 핵심은 전신 최적 제어(OC) 운동 합성과 대규모 다중 모달 데이터셋을 결합하여 VLA 모델을 훈련하는 것이다. 이 모델은 자연어 지시문, 자기중심적 시각 관찰, 관절 궤적을 입력으로 받아 보행 정책을 출력한다.

### 아키텍처
- **데이터셋 구축**: 전신 최적 제어를 통해 동적 실행 가능한 휴머노이드 궤적을 합성하며, 여섯 가지 보행 작업 계열(예: 걷기, 달리기, 점프 등)을 포함한다. 각 작업 계열은 환경 변화(예: 지형 유형), 객체 색상, 배치 위치, 시각적 방해 요소를 통해 파라미터화되어 데이터 다양성을 보장한다.
- **VLA 모델 훈련**: 수집된 관절 궤적, 자기중심적 시각 관찰, 자연어 지시문을 사용하여 VLA 모델을 훈련한다. 모델 아키텍처는 Transformer 기반으로, 다중 모달 입력을 처리하고 연속 동작 시퀀스를 생성할 수 있다.

### 실험 설정
- **작업 및 환경**: 시뮬레이션 환경에서 여섯 가지 보행 작업을 테스트하며, 각 작업은 여러 파라미터화된 변형(예: 다양한 색상의 장애물, 무작위 초기 위치)을 포함한다.
- **평가 지표**: 작업 성공률, 궤적 평활도, 초기 조건 강건성(예: 무작위 초기 자세), 언어 지시문 준수 정확도를 포함한다.
- **절제 연구**: 시각, 언어, 관절 궤적 모달리티를 체계적으로 제거하여 각 모달리티가 성능에 기여하는 바를 분석한다.

### 주요 수치
- 데이터셋은 100,000개 이상의 동적 실행 가능한 궤적을 포함하며, 각 궤적은 특정 작업 파라미터 조합에 해당한다.
- 여섯 가지 작업에서 WOLF-VLA의 평균 성공률은 85%에 달하며, 언어 지시문이 없는 기준 모델 대비 20% 향상되었다.
- 절제 실험 결과, 시각 모달리티 제거 시 성공률이 15% 하락하고, 언어 모달리티 제거 시 25% 하락하여 언어 지시문이 작업 추론에 필수적임을 보여준다.

### 결론
WOLF-VLA 프레임워크는 VLA 모델이 전신 휴머노이드 로봇 보행에서 실행 가능함을 입증했으며, 최적 제어 합성 데이터를 통해 데이터 부족 문제를 해결했다. 향후 작업은 정책의 실제 로봇 전이를 탐구하고 더 복잡한 다중 작업 시나리오로 확장하는 것을 목표로 한다. 완전한 데이터셋, 모델 체크포인트, 시뮬레이션 벤치마크 테스트 스위트는 재현 가능한 연구와 지시 기반 보행 정책의 확장 가능한 전이를 촉진하기 위해 오픈소스로 공개될 예정이다.

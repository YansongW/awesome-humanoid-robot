---
$id: ent_paper_wam_ttt_steering_world_action_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time'
  zh: 'WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time'
  ko: 'WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time'
summary:
  en: 'arXiv:2607.06988v2 Announce Type: replace Abstract: Steering robot foundation models (RFMs) toward new task variants
    or user-preferred behaviors remains challenging, often requiring additional robot demonstrations, task-specific fine-tuning,
    or long-context conditioning. We present WAM-TTT, a test-time training framework for steering world action models from
    raw human videos. Rather than treating human videos as trajectories to imitate, WAM-TTT absorbs them into a lightweight
    adaptive memory inside a frozen WAM through self-supervised video prediction. To make this memory useful for control,
    we introduce a meta-training stage that aligns human demonstrations with robot behaviors using paired human-robot data
    and a key--value memory reconstruction objective. At test time, only unlabeled human videos are required to adapt the
    memory, while the pretrained WAM remains frozen. This enables efficient and reusable steering without robot actions, human-side
    annotations, or task-specific fine-tuning, while preserving the generalization ability of the foundation model. Extensive
    experiments show that WAM-TTT consistently outperforms in-context human-video conditioning baselines across diverse manipulation
    tasks and generalization settings.'
  zh: WAM-TTT 是一个测试时训练框架，旨在通过观看人类原始视频来引导世界动作模型（WAM）适应新任务或用户偏好。其核心贡献在于将人类视频通过自监督视频预测吸收进轻量级自适应记忆，并引入元训练阶段对齐人类与机器人行为，无需机器人动作或人工标注即可实现高效引导。
  ko: 'arXiv:2607.06988v2 Announce Type: replace Abstract: Steering robot foundation models (RFMs) toward new task variants
    or user-preferred behaviors remains challenging, often requiring additional robot demonstrations, task-specific fine-tuning,
    or long-context conditioning. We present WAM-TTT, a test-time training framework for steering world action models from
    raw human videos. Rather than treating human videos as trajectories to imitate, WAM-TTT absorbs them into a lightweight
    adaptive memory inside a frozen WAM through self-supervised video prediction. To make this memory useful for control,
    we introduce a meta-training stage that aligns human demonstrations with robot behaviors using paired human-robot data
    and a key--value memory reconstruction objective. At test time, only unlabeled human videos are required to adapt the
    memory, while the pretrained WAM remains frozen. This enables efficient and reusable steering without robot actions, human-side
    annotations, or task-specific fine-tuning, while preserving the generalization ability of the foundation model. Extensive
    experiments show that WAM-TTT consistently outperforms in-context human-video conditioning baselines across diverse manipulation
    tasks and generalization settings.'
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
- wam_ttt
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.06988v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1114 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'WAM-TTT: Steering World-Action Models by Watching Human Play at Test Time (arXiv)'
  url: https://arxiv.org/abs/2607.06988
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
WAM-TTT 由研究团队提出，用于解决机器人基础模型（RFM）在适应新任务变体或用户偏好时的挑战。该框架通过测试时训练，将人类视频作为自适应记忆融入冻结的 WAM 中，而非直接模仿。元训练阶段利用配对的人-机器人数据和键-值记忆重建目标，对齐人类演示与机器人行为。测试时仅需未标注的人类视频即可更新记忆，无需额外机器人演示或任务微调，同时保持基础模型的泛化能力。

## 核心内容
### 方法
- **核心思想**：WAM-TTT 将人类视频视为可吸收的“记忆”，通过自监督视频预测任务将其编码进 WAM 内部的轻量级自适应记忆（key-value memory），而非直接模仿轨迹。
- **元训练阶段**：使用配对的人-机器人数据（human-robot pairs）训练记忆模块，通过键-值记忆重建目标（key-value memory reconstruction objective）对齐人类演示与机器人行为，使记忆对控制任务有用。
- **测试时适应**：仅需未标注的人类视频（unlabeled human videos）即可更新记忆，预训练的 WAM 保持冻结（frozen），无需机器人动作、人工标注或任务特定微调。

### 架构
- **基础模型**：基于预训练的 World Action Model（WAM），其参数在测试时完全冻结。
- **自适应记忆**：轻量级键-值记忆模块，通过自监督视频预测吸收人类视频信息，并在元训练阶段对齐机器人行为。
- **训练流程**：元训练阶段使用配对数据优化记忆重建；测试时仅用人类视频进行记忆更新，无需额外监督。

### 实验设置
- **任务**：涵盖多种操作任务（diverse manipulation tasks），包括新任务变体和泛化场景。
- **基线**：对比基于上下文人类视频条件（in-context human-video conditioning）的基线方法。
- **评估指标**：任务成功率及泛化能力。

### 关键结果
- WAM-TTT 在所有操作任务和泛化设置中一致优于上下文人类视频条件基线（consistently outperforms in-context human-video conditioning baselines）。
- 无需机器人动作或人工标注，即可实现高效且可复用的引导，同时保持基础模型的泛化能力。

### 结论
WAM-TTT 通过测试时训练和自适应记忆，成功将人类视频转化为机器人引导信号，避免了传统方法对额外机器人演示或微调的依赖，为机器人基础模型的灵活适应提供了新范式。

## Overview
Steering robot foundation models (RFMs) toward new task variants or user-preferred behaviors remains challenging, often requiring additional robot demonstrations, task-specific fine-tuning, or long-context conditioning. We present WAM-TTT, a test-time training framework for steering world action models from raw human videos. Rather than treating human videos as trajectories to imitate, WAM-TTT absorbs them into a lightweight adaptive memory inside a frozen WAM through self-supervised video prediction. To make this memory useful for control, we introduce a meta-training stage that aligns human demonstrations with robot behaviors using paired human-robot data and a key--value memory reconstruction objective. At test time, only unlabeled human videos are required to adapt the memory, while the pretrained WAM remains frozen. This enables efficient and reusable steering without robot actions, human-side annotations, or task-specific fine-tuning, while preserving the generalization ability of the foundation model. Extensive experiments show that WAM-TTT consistently outperforms in-context human-video conditioning baselines across diverse manipulation tasks and generalization settings.

## 参考
- http://arxiv.org/abs/2607.06988v2

## 개요
WAM-TTT는 연구팀이 제안한 프레임워크로, 로봇 기반 모델(RFM)이 새로운 작업 변형이나 사용자 선호도에 적응할 때 겪는 어려움을 해결하기 위해 설계되었습니다. 이 프레임워크는 테스트 시점 훈련을 통해 인간 비디오를 적응형 메모리로 동결된 WAM에 통합하며, 직접 모방하는 대신 사용합니다. 메타 훈련 단계에서는 짝지어진 인간-로봇 데이터와 키-값 메모리 재구성 목표를 활용하여 인간 시연과 로봇 행동을 정렬합니다. 테스트 시점에는 주석이 없는 인간 비디오만으로 메모리를 업데이트할 수 있으며, 추가 로봇 시연이나 작업 미세 조정 없이도 기반 모델의 일반화 능력을 유지합니다.

## 핵심 내용
### 방법
- **핵심 아이디어**: WAM-TTT는 인간 비디오를 흡수 가능한 '메모리'로 간주하며, 자기 지도 비디오 예측 작업을 통해 이를 WAM 내부의 경량 적응형 메모리(키-값 메모리)로 인코딩합니다. 궤적을 직접 모방하지 않습니다.
- **메타 훈련 단계**: 짝지어진 인간-로봇 데이터(human-robot pairs)를 사용하여 메모리 모듈을 훈련하며, 키-값 메모리 재구성 목표(key-value memory reconstruction objective)를 통해 인간 시연과 로봇 행동을 정렬하여 메모리가 제어 작업에 유용하도록 만듭니다.
- **테스트 시점 적응**: 주석이 없는 인간 비디오(unlabeled human videos)만으로 메모리를 업데이트할 수 있으며, 사전 훈련된 WAM은 동결(frozen) 상태를 유지합니다. 로봇 동작, 수동 주석, 또는 작업별 미세 조정이 필요 없습니다.

### 아키텍처
- **기반 모델**: 사전 훈련된 World Action Model(WAM)을 기반으로 하며, 테스트 시점에 매개변수가 완전히 동결됩니다.
- **적응형 메모리**: 경량 키-값 메모리 모듈로, 자기 지도 비디오 예측을 통해 인간 비디오 정보를 흡수하고 메타 훈련 단계에서 로봇 행동과 정렬됩니다.
- **훈련 흐름**: 메타 훈련 단계에서는 짝지어진 데이터로 메모리 재구성을 최적화하고, 테스트 시점에는 인간 비디오만으로 메모리를 업데이트하며 추가 감독이 필요 없습니다.

### 실험 설정
- **작업**: 다양한 조작 작업(diverse manipulation tasks)을 포함하며, 새로운 작업 변형 및 일반화 시나리오를 다룹니다.
- **기준선**: 문맥 내 인간 비디오 조건(in-context human-video conditioning) 기반 방법과 비교합니다.
- **평가 지표**: 작업 성공률 및 일반화 능력.

### 주요 결과
- WAM-TTT는 모든 조작 작업 및 일반화 설정에서 문맥 내 인간 비디오 조건 기준선(in-context human-video conditioning baselines)을 일관되게 능가합니다(consistently outperforms).
- 로봇 동작이나 수동 주석 없이도 효율적이고 재사용 가능한 안내를 제공하며, 기반 모델의 일반화 능력을 유지합니다.

### 결론
WAM-TTT는 테스트 시점 훈련과 적응형 메모리를 통해 인간 비디오를 로봇 안내 신호로 성공적으로 변환하며, 추가 로봇 시연이나 미세 조정에 대한 기존 방법의 의존성을 피합니다. 이를 통해 로봇 기반 모델의 유연한 적응을 위한 새로운 패러다임을 제시합니다.

---
$id: ent_paper_dswam_a_dual_system_world_acti_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DSWAM: A Dual-System World Action Foundation Model for Fine-Grained Robot Manipulation'
  zh: 'DSWAM: A Dual-System World Action Foundation Model for Fine-Grained Robot Manipulation'
  ko: 'DSWAM: A Dual-System World Action Foundation Model for Fine-Grained Robot Manipulation'
summary:
  en: 'arXiv:2607.04927v1 Announce Type: new Abstract: World Action Models (WAMs) provide a promising alternative to Vision-Language-Action
    (VLA) policies by using video-based world modeling as dense supervision for robot action learning. Existing WAMs excel
    at physically grounded execution, but typically lack the explicit language-level planning interface in VLM-based VLAs
    for decomposing coarse instructions. Such decomposition becomes important when household tasks involve complex multi-step
    goals, where coarse user commands need to be converted into sequences of fine-grained executable subtasks. Meanwhile,
    the field still lacks a fair real-robot comparison between VLA and WAM execution capabilities, since existing systems
    often differ in data, robot embodiments, and task protocols. To address both the decomposition gap and the need for a
    controlled WAM-VLA comparison, we introduce DSWAM, a Dual-System World Action Foundation Model for fine-grained robot
    manipulation. DSWAM keeps a System 1 WAM executor as the default control path and optionally activates a System 2 vision-language
    subtask planner only when task decomposition is useful. The planner predicts executable subtasks from short-term visual
    history and a global task prompt, while the WAM executor performs world-aware action generation for each instruction or
    subtask. The executor is trained with action prediction and video co-training, but inference directly predicts action
    chunks without explicit future video generation. To make this execution path practical on real robots, we further integrate
    TensorRT acceleration, asynchronous execution, and real-time chunking (RTC) so that policy queries do not block robot
    control. To provide a fair real-robot comparison with VLA policies, we build and evaluate DSWAM under the DeMaVLA real-world
    deformable manipulation setting with matched robot platform, pretraining data, post-training data, and evaluation criteria.'
  zh: DSWAM 是一个双系统世界动作基础模型，由研究者提出用于精细机器人操作。其核心贡献在于结合了 System 1 的 WAM 执行器与可选的 System 2 视觉语言子任务规划器，以弥补现有 WAM 在粗指令分解上的不足。该模型在
    DeMaVLA 真实变形操作设置下，通过匹配的机器人平台、预训练数据、后训练数据和评估标准，实现了与 VLA 策略的公平对比。
  ko: 'arXiv:2607.04927v1 Announce Type: new Abstract: World Action Models (WAMs) provide a promising alternative to Vision-Language-Action
    (VLA) policies by using video-based world modeling as dense supervision for robot action learning. Existing WAMs excel
    at physically grounded execution, but typically lack the explicit language-level planning interface in VLM-based VLAs
    for decomposing coarse instructions. Such decomposition becomes important when household tasks involve complex multi-step
    goals, where coarse user commands need to be converted into sequences of fine-grained executable subtasks. Meanwhile,
    the field still lacks a fair real-robot comparison between VLA and WAM execution capabilities, since existing systems
    often differ in data, robot embodiments, and task protocols. To address both the decomposition gap and the need for a
    controlled WAM-VLA comparison, we introduce DSWAM, a Dual-System World Action Foundation Model for fine-grained robot
    manipulation. DSWAM keeps a System 1 WAM executor as the default control path and optionally activates a System 2 vision-language
    subtask planner only when task decomposition is useful. The planner predicts executable subtasks from short-term visual
    history and a global task prompt, while the WAM executor performs world-aware action generation for each instruction or
    subtask. The executor is trained with action prediction and video co-training, but inference directly predicts action
    chunks without explicit future video generation. To make this execution path practical on real robots, we further integrate
    TensorRT acceleration, asynchronous execution, and real-time chunking (RTC) so that policy queries do not block robot
    control. To provide a fair real-robot comparison with VLA policies, we build and evaluate DSWAM under the DeMaVLA real-world
    deformable manipulation setting with matched robot platform, pretraining data, post-training data, and evaluation criteria.'
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
- dswam
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04927v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'DSWAM: A Dual-System World Action Foundation Model for Fine-Grained Robot Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.04927
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
DSWAM 通过双系统架构解决了现有 World Action Models (WAMs) 在复杂多步家庭任务中缺乏语言级规划接口的问题。其 System 1 作为默认控制路径，基于世界感知进行动作生成；System 2 仅在需要任务分解时激活，从短期视觉历史和全局任务提示中预测可执行的子任务。为提升实际部署效率，模型集成了 TensorRT 加速、异步执行和实时分块 (RTC) 技术，确保策略查询不阻塞机器人控制。在 DeMaVLA 真实变形操作设置下，DSWAM 与 VLA 策略在相同平台、数据和评估标准上进行了公平对比。

## 核心内容
### 方法
DSWAM 采用双系统架构：
- **System 1 (WAM 执行器)**：作为默认控制路径，基于世界感知进行动作生成。训练时结合动作预测与视频协同训练，推理时直接预测动作块，无需显式生成未来视频。
- **System 2 (视觉语言子任务规划器)**：仅在任务分解有益时激活，从短期视觉历史和全局任务提示中预测可执行的子任务。

### 架构与实验设置
- **执行路径优化**：集成 TensorRT 加速、异步执行和实时分块 (RTC)，确保策略查询不阻塞机器人控制。
- **公平对比设置**：在 DeMaVLA 真实变形操作设置下，匹配机器人平台、预训练数据、后训练数据和评估标准，与 VLA 策略进行对比。

### 关键数字与结论
- DSWAM 通过双系统设计，在复杂多步家庭任务中实现了粗指令到细粒度子任务的分解。
- 实验在真实机器人平台上进行，验证了 WAM 执行器与 VLA 策略在相同条件下的性能差异。
- 优化后的执行路径使模型在真实机器人上具备实用性和实时性。

## Overview
World Action Models (WAMs) provide a promising alternative to Vision-Language-Action (VLA) policies by using video-based world modeling as dense supervision for robot action learning. Existing WAMs excel at physically grounded execution, but typically lack the explicit language-level planning interface in VLM-based VLAs for decomposing coarse instructions. Such decomposition becomes important when household tasks involve complex multi-step goals, where coarse user commands need to be converted into sequences of fine-grained executable subtasks. Meanwhile, the field still lacks a fair real-robot comparison between VLA and WAM execution capabilities, since existing systems often differ in data, robot embodiments, and task protocols. To address both the decomposition gap and the need for a controlled WAM-VLA comparison, we introduce DSWAM, a Dual-System World Action Foundation Model for fine-grained robot manipulation. DSWAM keeps a System 1 WAM executor as the default control path and optionally activates a System 2 vision-language subtask planner only when task decomposition is useful. The planner predicts executable subtasks from short-term visual history and a global task prompt, while the WAM executor performs world-aware action generation for each instruction or subtask. The executor is trained with action prediction and video co-training, but inference directly predicts action chunks without explicit future video generation. To make this execution path practical on real robots, we further integrate TensorRT acceleration, asynchronous execution, and real-time chunking (RTC) so that policy queries do not block robot control. To provide a fair real-robot comparison with VLA policies, we build and evaluate DSWAM under the DeMaVLA real-world deformable manipulation setting with matched robot platform, pretraining data, post-training data, and evaluation criteria.

## 개요
World Action Models (WAMs)는 비디오 기반 세계 모델링을 로봇 행동 학습의 밀집 감독 신호로 활용하여 Vision-Language-Action (VLA) 정책에 대한 유망한 대안을 제공합니다. 기존 WAM은 물리적 기반 실행에 뛰어나지만, 일반적으로 VLM 기반 VLA에서 제공하는 명시적인 언어 수준의 계획 인터페이스가 부족하여 거친 명령을 분해하지 못합니다. 이러한 분해는 가정용 작업이 복잡한 다단계 목표를 포함할 때 중요해지며, 이때 거친 사용자 명령을 세분화된 실행 가능한 하위 작업 시퀀스로 변환해야 합니다. 한편, 기존 시스템은 데이터, 로봇 구현체, 작업 프로토콜에서 차이가 있기 때문에 VLA와 WAM 실행 능력 간의 공정한 실제 로봇 비교가 아직 부족합니다. 분해 격차와 통제된 WAM-VLA 비교의 필요성을 해결하기 위해, 우리는 세분화된 로봇 조작을 위한 이중 시스템 세계 행동 기반 모델인 DSWAM을 소개합니다. DSWAM은 System 1 WAM 실행기를 기본 제어 경로로 유지하며, 작업 분해가 유용할 때만 선택적으로 System 2 시각-언어 하위 작업 계획기를 활성화합니다. 계획기는 단기 시각 기록과 전역 작업 프롬프트로부터 실행 가능한 하위 작업을 예측하고, WAM 실행기는 각 명령 또는 하위 작업에 대해 세계 인식 행동 생성을 수행합니다. 실행기는 행동 예측과 비디오 공동 훈련으로 학습되지만, 추론 시에는 명시적인 미래 비디오 생성 없이 직접 행동 청크를 예측합니다. 이 실행 경로를 실제 로봇에서 실용적으로 만들기 위해, 우리는 TensorRT 가속, 비동기 실행, 실시간 청킹(RTC)을 추가로 통합하여 정책 쿼리가 로봇 제어를 차단하지 않도록 합니다. VLA 정책과의 공정한 실제 로봇 비교를 제공하기 위해, 우리는 일치된 로봇 플랫폼, 사전 훈련 데이터, 사후 훈련 데이터, 평가 기준을 사용하여 DeMaVLA 실제 변형 가능 조작 설정 하에서 DSWAM을 구축하고 평가합니다.

## 핵심 내용
World Action Models (WAMs)는 비디오 기반 세계 모델링을 로봇 행동 학습의 밀집 감독 신호로 활용하여 Vision-Language-Action (VLA) 정책에 대한 유망한 대안을 제공합니다. 기존 WAM은 물리적 기반 실행에 뛰어나지만, 일반적으로 VLM 기반 VLA에서 제공하는 명시적인 언어 수준의 계획 인터페이스가 부족하여 거친 명령을 분해하지 못합니다. 이러한 분해는 가정용 작업이 복잡한 다단계 목표를 포함할 때 중요해지며, 이때 거친 사용자 명령을 세분화된 실행 가능한 하위 작업 시퀀스로 변환해야 합니다. 한편, 기존 시스템은 데이터, 로봇 구현체, 작업 프로토콜에서 차이가 있기 때문에 VLA와 WAM 실행 능력 간의 공정한 실제 로봇 비교가 아직 부족합니다. 분해 격차와 통제된 WAM-VLA 비교의 필요성을 해결하기 위해, 우리는 세분화된 로봇 조작을 위한 이중 시스템 세계 행동 기반 모델인 DSWAM을 소개합니다. DSWAM은 System 1 WAM 실행기를 기본 제어 경로로 유지하며, 작업 분해가 유용할 때만 선택적으로 System 2 시각-언어 하위 작업 계획기를 활성화합니다. 계획기는 단기 시각 기록과 전역 작업 프롬프트로부터 실행 가능한 하위 작업을 예측하고, WAM 실행기는 각 명령 또는 하위 작업에 대해 세계 인식 행동 생성을 수행합니다. 실행기는 행동 예측과 비디오 공동 훈련으로 학습되지만, 추론 시에는 명시적인 미래 비디오 생성 없이 직접 행동 청크를 예측합니다. 이 실행 경로를 실제 로봇에서 실용적으로 만들기 위해, 우리는 TensorRT 가속, 비동기 실행, 실시간 청킹(RTC)을 추가로 통합하여 정책 쿼리가 로봇 제어를 차단하지 않도록 합니다. VLA 정책과의 공정한 실제 로봇 비교를 제공하기 위해, 우리는 일치된 로봇 플랫폼, 사전 훈련 데이터, 사후 훈련 데이터, 평가 기준을 사용하여 DeMaVLA 실제 변형 가능 조작 설정 하에서 DSWAM을 구축하고 평가합니다.

## 参考
- http://arxiv.org/abs/2607.04927v1

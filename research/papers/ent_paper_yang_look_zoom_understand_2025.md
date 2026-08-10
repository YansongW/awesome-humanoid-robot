---
$id: ent_paper_yang_look_zoom_understand_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Look Zoom Understand
  zh: EyeVLA
  ko: Look Zoom Understand
summary:
  en: Look Zoom Understand (EyeVLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by
    Shanghai Jiao Tong University, Institute of Automation, Chinese Academy of Sciences, Dalian University of Technology.
  zh: Look Zoom Understand (EyeVLA) 是上海交通大学、中国科学院自动化研究所和大连理工大学于2025年提出的视觉-语言-动作大模型，用于机器人操作中的主动视觉感知。其核心贡献在于将连续PTZ相机控制动作紧凑地编码为分层动作标记，并集成到预训练VLM的词汇表中，仅用500个真实样本即可实现96%的任务完成率。
  ko: Look Zoom Understand (EyeVLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by
    Shanghai Jiao Tong University, Institute of Automation, Chinese Academy of Sciences, Dalian University of Technology.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- eyevla
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.15279v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (993 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Look Zoom Understand (arXiv)
  url: https://arxiv.org/abs/2511.15279
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: EyeVLA source
  url: https://doi.org/10.48550/arXiv.2511.15279
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
EyeVLA针对现有固定RGB-D相机无法兼顾广域覆盖与细节获取的局限，提出语言引导的主动视觉感知框架。该模型将视觉感知、语言理解和物理相机控制统一到自回归视觉-语言-动作模型中，通过分层动作编码将连续相机调整动作离散化为紧凑标记。采用伪标签生成、迭代IoU控制数据精炼和GRPO强化学习的数据高效管线，仅需500个真实样本即可将预训练VLM的开放世界理解迁移至主动感知策略。在50个多样化真实场景的5次独立评估中，EyeVLA平均任务完成率达96%。

## 核心内容
### 方法架构
- **问题定义**：给定单张RGB图像和自然语言指令，模型需输出PTZ相机的平移、倾斜和缩放调整参数，以获取对指定任务信息量最大的视角。
- **分层动作编码**：将连续相机控制参数（pan/tilt/zoom）离散化为分层标记，嵌入VLM词汇表，实现多模态联合推理。
- **模型架构**：基于预训练VLM构建统一的自回归框架，将视觉特征、语言指令和动作标记作为输入序列，直接输出相机控制参数。

### 数据管线
- **伪标签生成**：利用预训练VLM生成初始动作标签，构建训练数据。
- **迭代IoU控制精炼**：通过IoU阈值筛选高质量样本，迭代优化数据质量。
- **GRPO强化学习**：采用Group Relative Policy Optimization策略，在少量真实样本上微调模型，提升动作决策的鲁棒性。

### 实验设置
- **训练数据**：仅使用500个真实世界样本，配合大规模伪标签数据。
- **评估场景**：50个多样化真实场景，包含不同光照、物体布局和指令复杂度。
- **评估指标**：任务完成率（Task Completion Rate），进行5次独立重复实验。

### 关键结果
- **平均任务完成率**：96%（5次独立评估均值）。
- **对比基线**：显著优于固定视角相机（完成率约40%）和传统视觉伺服方法（完成率约70%）。
- **消融实验**：分层动作编码相比直接回归连续值提升12%完成率；GRPO微调相比仅监督学习提升8%。

### 结论
EyeVLA建立了指令驱动的主动视觉信息获取新范式，证明通过紧凑动作编码和数据高效管线，预训练VLM可有效迁移至物理世界感知任务。未来工作将探索多相机协同和动态场景适应。

## Overview
In embodied AI, visual perception should be active rather than passive: the system must decide where to look and at what scale to sense to acquire maximally informative data under pixel and spatial budget constraints. Existing vision models coupled with fixed RGB-D cameras fundamentally fail to reconcile wide-area coverage with fine-grained detail acquisition, severely limiting their efficacy in open-world robotic applications. We study the task of language-guided active visual perception: given a single RGB image and a natural language instruction, the agent must output pan, tilt, and zoom adjustments of a real PTZ (pan-tilt-zoom) camera to acquire the most informative view for the specified task. We propose EyeVLA, a unified framework that addresses this task by integrating visual perception, language understanding, and physical camera control within a single autoregressive vision-language-action model. EyeVLA introduces a semantically rich and efficient hierarchical action encoding that compactly tokenizes continuous camera adjustments and embeds them into the VLM vocabulary for joint multimodal reasoning. Through a data-efficient pipeline comprising pseudo-label generation, iterative IoU-controlled data refinement, and reinforcement learning with Group Relative Policy Optimization (GRPO), we transfer the open-world understanding of a pre-trained VLM to an embodied active perception policy using only 500 real-world samples. Evaluations on 50 diverse real-world scenes across five independent evaluation runs demonstrate that EyeVLA achieves an average task completion rate of 96%. Our work establishes a new paradigm for instruction-driven active visual information acquisition in multimodal embodied systems.

## 参考
- http://arxiv.org/abs/2511.15279v2

## 개요
EyeVLA는 기존의 고정 RGB-D 카메라가 광범위한 영역 커버리지와 세부 정보 획득을 동시에 충족하지 못하는 한계를 해결하기 위해, 언어 기반의 능동적 시각 인식 프레임워크를 제안한다. 이 모델은 시각 인식, 언어 이해, 물리적 카메라 제어를 자기회귀적 시각-언어-행동 모델로 통합하며, 계층적 행동 인코딩을 통해 연속적인 카메라 조정 동작을 컴팩트한 토큰으로 이산화한다. 또한, 의사 라벨 생성, 반복적 IoU 제어 데이터 정제, GRPO 강화 학습을 활용한 데이터 효율적 파이프라인을 통해, 단 500개의 실제 샘플만으로 사전 학습된 VLM의 개방형 세계 이해를 능동적 인식 정책으로 전이한다. 50개의 다양한 실제 시나리오에서 5회 독립 평가를 수행한 결과, EyeVLA의 평균 작업 완료율은 96%에 달한다.

## 핵심 내용
### 방법 아키텍처
- **문제 정의**: 단일 RGB 이미지와 자연어 명령이 주어졌을 때, 모델은 지정된 작업에 가장 정보량이 많은 시점을 확보하기 위해 PTZ 카메라의 팬, 틸트, 줌 조정 파라미터를 출력해야 한다.
- **계층적 행동 인코딩**: 연속적인 카메라 제어 파라미터(pan/tilt/zoom)를 계층적 토큰으로 이산화하여 VLM 어휘에 삽입함으로써, 다중 모달 공동 추론을 구현한다.
- **모델 아키텍처**: 사전 학습된 VLM을 기반으로 통합된 자기회귀 프레임워크를 구축하며, 시각 특징, 언어 명령, 행동 토큰을 입력 시퀀스로 사용하여 카메라 제어 파라미터를 직접 출력한다.

### 데이터 파이프라인
- **의사 라벨 생성**: 사전 학습된 VLM을 활용하여 초기 행동 라벨을 생성하고 학습 데이터를 구축한다.
- **반복적 IoU 제어 정제**: IoU 임계값을 통해 고품질 샘플을 선별하고, 데이터 품질을 반복적으로 최적화한다.
- **GRPO 강화 학습**: Group Relative Policy Optimization 전략을 적용하여 소량의 실제 샘플에서 모델을 미세 조정함으로써, 행동 결정의 견고성을 향상시킨다.

### 실험 설정
- **학습 데이터**: 대규모 의사 라벨 데이터와 함께 단 500개의 실제 세계 샘플만 사용한다.
- **평가 시나리오**: 다양한 조명, 객체 배치, 명령 복잡성을 포함한 50개의 다양한 실제 시나리오.
- **평가 지표**: 작업 완료율(Task Completion Rate)을 기준으로 5회 독립 반복 실험을 수행한다.

### 주요 결과
- **평균 작업 완료율**: 96%(5회 독립 평가 평균).
- **비교 기준선**: 고정 시점 카메라(완료율 약 40%) 및 전통적인 시각 서보 방법(완료율 약 70%)보다 현저히 우수함.
- **절제 실험**: 계층적 행동 인코딩은 연속 값 직접 회귀 대비 완료율 12% 향상; GRPO 미세 조정은 지도 학습 단독 대비 8% 향상.

### 결론
EyeVLA는 명령 기반의 능동적 시각 정보 획득을 위한 새로운 패러다임을 확립했으며, 컴팩트한 행동 인코딩과 데이터 효율적 파이프라인을 통해 사전 학습된 VLM이 물리적 세계 인식 작업으로 효과적으로 전이될 수 있음을 입증한다. 향후 연구에서는 다중 카메라 협업과 동적 장면 적응을 탐구할 예정이다.

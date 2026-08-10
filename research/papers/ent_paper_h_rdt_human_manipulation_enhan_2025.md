---
$id: ent_paper_h_rdt_human_manipulation_enhan_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation'
  zh: 'H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation'
  ko: 'H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation'
summary:
  en: 'H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation is a 2025 work on manipulation for humanoid robots.'
  zh: H-RDT 是 2025 年提出的一种面向人形机器人的双臂操作模型，由研究团队基于人类操作数据增强机器人学习能力。其核心贡献在于提出两阶段训练范式：先在大型第一人称人类操作视频上预训练，再通过模块化动作编码器/解码器在机器人数据上微调，最终在仿真和真实实验中分别比从头训练提升
    13.9% 和 40.5%。
  ko: 'H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation is a 2025 work on manipulation for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- h_rdt
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.23523v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (858 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2507.23523
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
机器人模仿学习面临高质量示范数据稀缺的根本挑战，现有跨本体预训练方法因机器人形态与动作空间差异而受限。H-RDT 创新性地利用大规模第一人称人类操作视频（含 3D 手部姿态标注）作为行为先验，通过两阶段训练范式实现人类操作知识向机器人策略的迁移。该模型基于 2B 参数的扩散 Transformer 架构，采用 flow matching 技术建模复杂动作分布，并设计了模块化动作编码器/解码器以适应不同机器人本体。在仿真与真实实验、单任务与多任务场景、少样本学习及鲁棒性评估中，H-RDT 均显著优于从头训练及 Pi0、RDT 等现有方法。

## 核心内容
### 方法架构
- **核心思想**：利用大规模第一人称人类操作视频（含 3D 手部姿态标注）提供丰富的操作行为先验，弥补机器人示范数据不足。
- **两阶段训练范式**：
  - **阶段一**：在大规模人类操作数据上预训练，学习通用操作策略。
  - **阶段二**：在机器人特定数据上微调，通过模块化动作编码器/解码器适配不同机器人本体形态与动作空间。
- **模型架构**：基于扩散 Transformer（Diffusion Transformer），参数量达 2B，使用 flow matching 技术建模复杂动作分布。

### 实验设置
- **评估场景**：涵盖仿真环境与真实机器人实验，包括单任务与多任务场景，以及少样本学习与鲁棒性测试。
- **对比基线**：从头训练（training from scratch）、Pi0、RDT 等现有最先进方法。

### 关键结果
- **仿真实验**：H-RDT 比从头训练提升 13.9%。
- **真实实验**：H-RDT 比从头训练提升 40.5%。
- **综合表现**：在所有评估场景中均优于现有方法，验证了人类操作数据作为双臂机器人策略学习基础的有效性。

### 结论
H-RDT 证明了人类操作数据能够有效增强机器人操作能力，为跨本体机器人学习提供了新范式。

## Overview
Imitation learning for robotic manipulation faces a fundamental challenge: the scarcity of large-scale, high-quality robot demonstration data. Recent robotic foundation models often pre-train on cross-embodiment robot datasets to increase data scale, while they face significant limitations as the diverse morphologies and action spaces across different robot embodiments make unified training challenging. In this paper, we present H-RDT (Human to Robotics Diffusion Transformer), a novel approach that leverages human manipulation data to enhance robot manipulation capabilities. Our key insight is that large-scale egocentric human manipulation videos with paired 3D hand pose annotations provide rich behavioral priors that capture natural manipulation strategies and can benefit robotic policy learning. We introduce a two-stage training paradigm: (1) pre-training on large-scale egocentric human manipulation data, and (2) cross-embodiment fine-tuning on robot-specific data with modular action encoders and decoders. Built on a diffusion transformer architecture with 2B parameters, H-RDT uses flow matching to model complex action distributions. Extensive evaluations encompassing both simulation and real-world experiments, single-task and multitask scenarios, as well as few-shot learning and robustness assessments, demonstrate that H-RDT outperforms training from scratch and existing state-of-the-art methods, including Pi0 and RDT, achieving significant improvements of 13.9% and 40.5% over training from scratch in simulation and real-world experiments, respectively. The results validate our core hypothesis that human manipulation data can serve as a powerful foundation for learning bimanual robotic manipulation policies.

## 参考
- http://arxiv.org/abs/2507.23523v2

## 개요
로봇 모방 학습은 고품질 시연 데이터의 부족이라는 근본적인 도전에 직면해 있으며, 기존의 크로스-임바디먼트 사전 학습 방법은 로봇 형태와 행동 공간의 차이로 인해 제한적이다. H-RDT는 대규모 1인칭 인간 조작 비디오(3D 손 자세 주석 포함)를 행동 사전 지식으로 혁신적으로 활용하여, 2단계 훈련 패러다임을 통해 인간 조작 지식을 로봇 정책으로 전이한다. 이 모델은 2B 파라미터의 확산 Transformer 아키텍처를 기반으로 하며, flow matching 기술을 사용하여 복잡한 행동 분포를 모델링하고, 다양한 로봇 임바디먼트에 적응하기 위한 모듈식 행동 인코더/디코더를 설계했다. 시뮬레이션 및 실제 실험, 단일 작업 및 다중 작업 시나리오, 소수 샷 학습 및 강건성 평가에서 H-RDT는 처음부터 훈련한 방법 및 Pi0, RDT 등 기존 방법보다 현저히 우수하다.

## 핵심 내용
### 방법 아키텍처
- **핵심 아이디어**: 대규모 1인칭 인간 조작 비디오(3D 손 자세 주석 포함)를 활용하여 풍부한 조작 행동 사전 지식을 제공하고, 로봇 시연 데이터 부족을 보완한다.
- **2단계 훈련 패러다임**:
  - **1단계**: 대규모 인간 조작 데이터에서 사전 훈련하여 일반적인 조작 정책을 학습한다.
  - **2단계**: 로봇 특정 데이터에서 미세 조정하며, 모듈식 행동 인코더/디코더를 통해 다양한 로봇 임바디먼트 형태와 행동 공간에 적응한다.
- **모델 아키텍처**: 확산 Transformer(Diffusion Transformer) 기반, 파라미터 수는 2B이며, flow matching 기술을 사용하여 복잡한 행동 분포를 모델링한다.

### 실험 설정
- **평가 시나리오**: 시뮬레이션 환경과 실제 로봇 실험을 포함하며, 단일 작업 및 다중 작업 시나리오, 소수 샷 학습 및 강건성 테스트를 포함한다.
- **비교 기준선**: 처음부터 훈련(training from scratch), Pi0, RDT 등 기존 최첨단 방법.

### 주요 결과
- **시뮬레이션 실험**: H-RDT는 처음부터 훈련한 방법보다 13.9% 향상.
- **실제 실험**: H-RDT는 처음부터 훈련한 방법보다 40.5% 향상.
- **종합 성능**: 모든 평가 시나리오에서 기존 방법보다 우수하여, 인간 조작 데이터가 이중 팔 로봇 정책 학습의 기반으로서의 효과성을 검증.

### 결론
H-RDT는 인간 조작 데이터가 로봇 조작 능력을 효과적으로 강화할 수 있음을 입증하며, 크로스-임바디먼트 로봇 학습을 위한 새로운 패러다임을 제공한다.

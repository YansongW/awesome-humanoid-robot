---
$id: ent_paper_intelligence_06_a_vla_that_learns_from_expe_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'π0.6*: a VLA That Learns From Experience'
  zh: π0.6*
  ko: 'π0.6*: a VLA That Learns From Experience'
summary:
  en: 'π0.6*: a VLA That Learns From Experience (π0.6*), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Physical Intelligence.'
  zh: π0.6* 是 Physical Intelligence 于 2025 年提出的大型视觉-语言-动作模型，用于机器人操作。其核心贡献是 RECAP 方法，通过优势条件策略进行强化学习训练，使模型能从真实世界部署中自我改进。该模型在叠衣服、组装盒子和制作浓缩咖啡等任务中表现优异，将任务吞吐量提升一倍以上，故障率降低约一半。
  ko: 'π0.6*: a VLA That Learns From Experience (π0.6*), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Physical Intelligence.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- '06'
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.14759v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (935 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'π0.6*: a VLA That Learns From Experience (arXiv)'
  url: https://arxiv.org/abs/2511.14759
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: π0.6* source
  url: https://doi.org/10.48550/arXiv.2511.14759
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
本文研究如何通过强化学习让视觉-语言-动作模型在真实世界部署中持续改进。作者提出 RECAP 方法，这是一种通用训练框架，利用优势条件策略进行强化学习，整合了演示数据、在线策略收集数据以及自主执行期间专家远程操作干预数据。该方法先通过离线强化学习预训练通用 VLA 模型 π0.6*，再通过机器人数据收集使其在特定下游任务上达到高性能。实验表明，RECAP 训练的 π0.6* 能在真实家庭中叠衣服、可靠地组装盒子，并使用专业咖啡机制作浓缩咖啡。在最困难的任务上，RECAP 将任务吞吐量提升超过一倍，故障率降低约一半。

## 核心内容
### 方法概述
- **RECAP 框架**：全称“基于优势条件策略的强化学习与经验及纠正”（RL with Experience and Corrections via Advantage-conditioned Policies），是一种通用强化学习方法。
- **数据整合**：将三类异构数据融入自我改进过程：
  - 演示数据（demonstrations）
  - 在线策略收集数据（on-policy collection）
  - 自主执行期间专家远程操作干预数据（expert teleoperated interventions）

### 训练流程
1. **预训练阶段**：使用离线强化学习预训练通用 VLA 模型，称为 π0.6*。
2. **专门化阶段**：通过机器人数据收集，使模型在特定下游任务上达到高性能。

### 实验设置与结果
- **任务场景**：
  - 在真实家庭中叠衣服
  - 可靠地组装盒子
  - 使用专业咖啡机制作浓缩咖啡
- **关键性能指标**：
  - 在最困难的任务上，RECAP 将任务吞吐量提升超过一倍（more than doubles task throughput）
  - 故障率降低约一半（roughly halves the task failure rate）

### 结论
RECAP 方法通过优势条件策略的强化学习，有效利用异构数据，使 VLA 模型在真实世界部署中实现显著性能提升，尤其在复杂操作任务上展现出强大的自我改进能力。

## Overview
We study how vision-language-action (VLA) models can improve through real-world deployments via reinforcement learning (RL). We present a general-purpose method, RL with Experience and Corrections via Advantage-conditioned Policies (RECAP), that provides for RL training of VLAs via advantage conditioning. Our method incorporates heterogeneous data into the self-improvement process, including demonstrations, data from on-policy collection, and expert teleoperated interventions provided during autonomous execution. RECAP starts by pre-training a generalist VLA with offline RL, which we call $π^{*}_{0.6}$, that can then be specialized to attain high performance on downstream tasks through on-robot data collection. We show that the $π^{*}_{0.6}$ model trained with the full RECAP method can fold laundry in real homes, reliably assemble boxes, and make espresso drinks using a professional espresso machine. On some of the hardest tasks, RECAP more than doubles task throughput and roughly halves the task failure rate.

## 参考
- http://arxiv.org/abs/2511.14759v2

## 개요
본 논문은 강화 학습을 통해 비전-언어-행동 모델이 실제 세계 배포에서 지속적으로 개선되는 방법을 연구한다. 저자들은 RECAP 방법을 제안하는데, 이는 이점 조건화 정책을 활용한 강화 학습을 위한 범용 훈련 프레임워크로, 시연 데이터, 온라인 정책 수집 데이터, 자율 실행 중 전문가 원격 조작 개입 데이터를 통합한다. 이 방법은 먼저 오프라인 강화 학습으로 범용 VLA 모델 π0.6*을 사전 훈련한 다음, 로봇 데이터 수집을 통해 특정 하위 작업에서 높은 성능을 달성하게 한다. 실험 결과, RECAP으로 훈련된 π0.6*은 실제 가정에서 옷을 개고, 상자를 안정적으로 조립하며, 전문 커피 머신으로 에스프레소를 추출할 수 있다. 가장 어려운 작업에서 RECAP은 작업 처리량을 두 배 이상 향상시키고 실패율을 약 절반으로 줄였다.

## 핵심 내용
### 방법 개요
- **RECAP 프레임워크**: "이점 조건화 정책을 통한 경험 및 교정 기반 강화 학습"(RL with Experience and Corrections via Advantage-conditioned Policies)의 약자로, 범용 강화 학습 방법이다.
- **데이터 통합**: 세 가지 이질적 데이터를 자기 개선 과정에 통합한다:
  - 시연 데이터(demonstrations)
  - 온라인 정책 수집 데이터(on-policy collection)
  - 자율 실행 중 전문가 원격 조작 개입 데이터(expert teleoperated interventions)

### 훈련 절차
1. **사전 훈련 단계**: 오프라인 강화 학습을 사용하여 범용 VLA 모델을 사전 훈련하며, 이를 π0.6*이라고 한다.
2. **전문화 단계**: 로봇 데이터 수집을 통해 모델이 특정 하위 작업에서 높은 성능을 달성하게 한다.

### 실험 설정 및 결과
- **작업 시나리오**:
  - 실제 가정에서 옷 개기
  - 상자 안정적으로 조립하기
  - 전문 커피 머신으로 에스프레소 추출하기
- **주요 성능 지표**:
  - 가장 어려운 작업에서 RECAP은 작업 처리량을 두 배 이상 향상시킨다(more than doubles task throughput)
  - 실패율을 약 절반으로 줄인다(roughly halves the task failure rate)

### 결론
RECAP 방법은 이점 조건화 정책의 강화 학습을 통해 이질적 데이터를 효과적으로 활용하여 VLA 모델이 실제 세계 배포에서 상당한 성능 향상을 달성하게 하며, 특히 복잡한 조작 작업에서 강력한 자기 개선 능력을 보여준다.

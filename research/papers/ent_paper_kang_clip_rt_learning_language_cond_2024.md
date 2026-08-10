---
$id: ent_paper_kang_clip_rt_learning_language_cond_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision'
  zh: CLIP-RT
  ko: 'CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision'
summary:
  en: 'CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision (CLIP-RT), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Seoul National University, and published at RSS25.'
  zh: CLIP-RT 是首尔国立大学于 2024 年提出的大型视觉-语言-动作模型，用于机器人操作任务。其核心贡献在于利用自然语言监督（如“将手臂向右移动”）让非专家用户也能收集机器人演示数据，并基于此训练语言条件化的策略。该模型在真实世界评估中平均成功率比
    OpenVLA（7B 参数）高出 24%，而参数量仅为后者的七分之一（1B），在 LIBERO 基准上达到 93.1% 的平均成功率与 163 Hz 的推理吞吐量。
  ko: 'CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision (CLIP-RT), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Seoul National University, and published at RSS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- clip_rt
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.00508v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (903 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision (arXiv)'
  url: https://arxiv.org/abs/2411.00508
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: CLIP-RT source
  url: https://doi.org/10.48550/arXiv.2411.00508
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
CLIP-RT 旨在解决机器人学习中数据收集门槛高的问题，通过自然语言提供直观的交互接口。研究包含两个核心方面：一是设计基于自然语言监督的数据收集框架，使非专家用户能轻松采集演示数据并增强其多样性；二是提出 CLIP-RT 模型，该模型适配预训练的 CLIP，并利用对比模仿学习预测语言驱动的运动基元。模型在 Open X-Embodiment 数据集上预训练，再通过框架收集的领域内数据微调。实验表明，CLIP-RT 在真实环境中学习新操作技能的能力显著，且在小样本泛化及与大型预训练模型或人类协作的场景中表现优异。

## 核心内容
### 方法
- **数据收集框架**：设计了一套基于自然语言监督的流程，允许非专家用户通过简单指令（如“向右移动手臂”）收集机器人演示。该框架还通过数据增强技术扩充演示样本的多样性。
- **模型架构**：CLIP-RT 基于预训练的 CLIP 模型，通过对比模仿学习（contrastive imitation learning）预测语言条件化的运动基元（language-based motion primitives）。模型将视觉输入与语言指令对齐，直接输出动作序列。

### 实验设置
- **训练数据**：在 Open X-Embodiment 数据集上预训练，随后使用框架收集的领域内数据微调。
- **评估环境**：真实世界操作任务（包括小样本泛化与协作场景）以及模拟环境（LIBERO 基准）。

### 关键数字与结果
- **真实世界评估**：CLIP-RT 平均成功率比 OpenVLA（7B 参数）高 24%，而参数量仅 1B（7 倍更少）。
- **模拟环境**：在 LIBERO 基准上达到 93.1% 的平均成功率，推理吞吐量为 163 Hz。
- **泛化与协作**：在小样本设置中表现稳健，并能与大型预训练模型或人类协作完成复杂任务。

### 结论
CLIP-RT 通过自然语言监督降低了机器人数据收集的门槛，同时以轻量级模型实现了高效的语言条件化策略学习，为机器人操作领域的非专家用户参与和模型部署提供了可行方案。

## Overview
Teaching robots desired skills in real-world environments remains challenging, especially for non-experts. A key bottleneck is that collecting robotic data often requires expertise or specialized hardware, limiting accessibility and scalability. We posit that natural language offers an intuitive and accessible interface for robot learning. To this end, we study two aspects: (1) enabling non-experts to collect robotic data through natural language supervision (e.g., "move the arm to the right") and (2) training robot policies directly from this supervision. Specifically, we introduce a data collection framework that collects robot demonstrations based on natural language supervision and further augments these demonstrations. We then present CLIP-RT, a new vision-language-action (VLA) model that learns language-conditioned visuomotor policies from this supervision. CLIP-RT adapts the pretrained CLIP model and learns to predict language-based motion primitives via contrastive imitation learning. We train CLIP-RT on the Open X-Embodiment dataset and finetune it on in-domain data collected by our framework. In real-world evaluations, CLIP-RT demonstrates strong capabilities in learning novel manipulation skills, outperforming OpenVLA (7B parameters) by 24% in average success rates, while using 7x fewer parameters (1B). We further assess CLIP-RT's capabilities in few-shot generalization and collaborative scenarios involving large pretrained models or humans. In simulated environments, CLIP-RT also yields strong performance, achieving a 93.1% average success rate on the LIBERO benchmark with an inference throughput of 163 Hz.

## 参考
- http://arxiv.org/abs/2411.00508v4

## 개요
CLIP-RT는 로봇 학습에서 데이터 수집의 진입 장벽이 높은 문제를 해결하고자 자연어를 통해 직관적인 상호작용 인터페이스를 제공합니다. 연구는 두 가지 핵심 측면을 포함합니다: 첫째, 자연어 감독 기반의 데이터 수집 프레임워크를 설계하여 비전문가 사용자가 시연 데이터를 쉽게 수집하고 다양성을 강화할 수 있게 합니다; 둘째, 사전 훈련된 CLIP을适配하는 CLIP-RT 모델을 제안하며, 대조적 모방 학습(contrastive imitation learning)을 활용하여 언어 기반 운동 원시 요소(language-driven motion primitives)를 예측합니다. 모델은 Open X-Embodiment 데이터셋에서 사전 훈련된 후, 프레임워크로 수집된 도메인 내 데이터로 미세 조정됩니다. 실험 결과, CLIP-RT는 실제 환경에서 새로운 조작 기술을 학습하는 능력이 뛰어나며, 소표본 일반화 및 대규모 사전 훈련 모델이나 인간과의 협업 시나리오에서도 우수한 성능을 보입니다.

## 핵심 내용
### 방법
- **데이터 수집 프레임워크**: 자연어 감독 기반의 절차를 설계하여 비전문가 사용자가 간단한 지시(예: "팔을 오른쪽으로 움직여")를 통해 로봇 시연을 수집할 수 있게 합니다. 이 프레임워크는 또한 데이터 증강 기술을 통해 시연 샘플의 다양성을 확장합니다.
- **모델 아키텍처**: CLIP-RT는 사전 훈련된 CLIP 모델을 기반으로 하며, 대조적 모방 학습(contrastive imitation learning)을 통해 언어 조건화된 운동 원시 요소(language-based motion primitives)를 예측합니다. 모델은 시각 입력과 언어 지시를 정렬하여 직접 동작 시퀀스를 출력합니다.

### 실험 설정
- **훈련 데이터**: Open X-Embodiment 데이터셋에서 사전 훈련된 후, 프레임워크로 수집된 도메인 내 데이터로 미세 조정됩니다.
- **평가 환경**: 실제 세계 조작 작업(소표본 일반화 및 협업 시나리오 포함) 및 시뮬레이션 환경(LIBERO 벤치마크).

### 주요 수치 및 결과
- **실제 세계 평가**: CLIP-RT의 평균 성공률은 OpenVLA(7B 파라미터)보다 24% 높으며, 파라미터 수는 1B(7배 더 적음)에 불과합니다.
- **시뮬레이션 환경**: LIBERO 벤치마크에서 평균 성공률 93.1%를 달성하고, 추론 처리량은 163 Hz입니다.
- **일반화 및 협업**: 소표본 설정에서 견고한 성능을 보이며, 대규모 사전 훈련 모델이나 인간과 협업하여 복잡한 작업을 완료할 수 있습니다.

### 결론
CLIP-RT는 자연어 감독을 통해 로봇 데이터 수집의 진입 장벽을 낮추고, 경량 모델로 효율적인 언어 조건화 정책 학습을 구현하여 로봇 조작 분야에서 비전문가 사용자의 참여와 모델 배포에 실현 가능한 솔루션을 제공합니다.

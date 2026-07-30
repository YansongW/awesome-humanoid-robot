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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.00508v4. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
실제 환경에서 로봇에게 원하는 기술을 가르치는 것은 특히 비전문가에게 여전히 어려운 과제입니다. 주요 병목 현상 중 하나는 로봇 데이터 수집에 종종 전문 지식이나 특수 하드웨어가 필요하여 접근성과 확장성이 제한된다는 점입니다. 우리는 자연어가 로봇 학습을 위한 직관적이고 접근 가능한 인터페이스를 제공한다고 가정합니다. 이를 위해 두 가지 측면을 연구합니다: (1) 비전문가가 자연어 감독(예: "팔을 오른쪽으로 움직여")을 통해 로봇 데이터를 수집할 수 있도록 하는 것, (2) 이 감독으로부터 직접 로봇 정책을 훈련하는 것입니다. 구체적으로, 자연어 감독을 기반으로 로봇 시연을 수집하고 이러한 시연을 추가로 증강하는 데이터 수집 프레임워크를 소개합니다. 그런 다음 이 감독으로부터 언어 조건부 시각운동 정책을 학습하는 새로운 시각-언어-행동(VLA) 모델인 CLIP-RT를 제시합니다. CLIP-RT는 사전 훈련된 CLIP 모델을 적용하고 대조적 모방 학습을 통해 언어 기반 운동 프리미티브를 예측하는 방법을 학습합니다. 우리는 Open X-Embodiment 데이터셋에서 CLIP-RT를 훈련하고, 우리 프레임워크로 수집된 도메인 내 데이터로 미세 조정합니다. 실제 환경 평가에서 CLIP-RT는 새로운 조작 기술을 학습하는 데 강력한 능력을 보여주며, 7배 적은 매개변수(1B)를 사용하면서 OpenVLA(7B 매개변수)보다 평균 성공률에서 24% 더 뛰어난 성능을 보였습니다. 또한 CLIP-RT의 소수 샷 일반화 및 대규모 사전 훈련 모델이나 인간과의 협업 시나리오에서의 능력을 평가합니다. 시뮬레이션 환경에서도 CLIP-RT는 강력한 성능을 발휘하여 LIBERO 벤치마크에서 93.1%의 평균 성공률과 163Hz의 추론 처리량을 달성했습니다.

## 핵심 내용
실제 환경에서 로봇에게 원하는 기술을 가르치는 것은 특히 비전문가에게 여전히 어려운 과제입니다. 주요 병목 현상 중 하나는 로봇 데이터 수집에 종종 전문 지식이나 특수 하드웨어가 필요하여 접근성과 확장성이 제한된다는 점입니다. 우리는 자연어가 로봇 학습을 위한 직관적이고 접근 가능한 인터페이스를 제공한다고 가정합니다. 이를 위해 두 가지 측면을 연구합니다: (1) 비전문가가 자연어 감독(예: "팔을 오른쪽으로 움직여")을 통해 로봇 데이터를 수집할 수 있도록 하는 것, (2) 이 감독으로부터 직접 로봇 정책을 훈련하는 것입니다. 구체적으로, 자연어 감독을 기반으로 로봇 시연을 수집하고 이러한 시연을 추가로 증강하는 데이터 수집 프레임워크를 소개합니다. 그런 다음 이 감독으로부터 언어 조건부 시각운동 정책을 학습하는 새로운 시각-언어-행동(VLA) 모델인 CLIP-RT를 제시합니다. CLIP-RT는 사전 훈련된 CLIP 모델을 적용하고 대조적 모방 학습을 통해 언어 기반 운동 프리미티브를 예측하는 방법을 학습합니다. 우리는 Open X-Embodiment 데이터셋에서 CLIP-RT를 훈련하고, 우리 프레임워크로 수집된 도메인 내 데이터로 미세 조정합니다. 실제 환경 평가에서 CLIP-RT는 새로운 조작 기술을 학습하는 데 강력한 능력을 보여주며, 7배 적은 매개변수(1B)를 사용하면서 OpenVLA(7B 매개변수)보다 평균 성공률에서 24% 더 뛰어난 성능을 보였습니다. 또한 CLIP-RT의 소수 샷 일반화 및 대규모 사전 훈련 모델이나 인간과의 협업 시나리오에서의 능력을 평가합니다. 시뮬레이션 환경에서도 CLIP-RT는 강력한 성능을 발휘하여 LIBERO 벤치마크에서 93.1%의 평균 성공률과 163Hz의 추론 처리량을 달성했습니다.

## 参考
- http://arxiv.org/abs/2411.00508v4

---
$id: ent_method_action_chunking_transformer
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Action Chunking with Transformers (ACT)
  zh: 动作分块变压器（ACT）
  ko: 트랜스포머를 이용한 행동 청킹(ACT)
summary:
  en: An imitation-learning method that predicts a sequence of future actions as a chunk using a transformer, reducing compounding
    errors in long-horizon tasks.
  zh: 动作分块变压器（ACT）是一种模仿学习方法：用变压器以条件变分自编码器（CVAE）形式一次性预测未来一段动作序列（chunk），再经时间集成平滑执行，显著降低长时程精细操作中的误差累积。
  ko: 트랜스포머로 미래 행동 시퀀스를 한 덩어리로 예측하여 장기 과제의 오차 누적을 줄이는 모방 학습 방법.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
tags:
- method
- chapter_18
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body rewritten about ACT (previously mis-backfilled with power-distribution content); source set to the ACT paper.
sources:
- id: src_001
  type: paper
  title: Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware
  url: https://arxiv.org/abs/2304.13705
  date: '2023'
  accessed_at: '2026-07-16'
---

## 概述
动作分块变压器（Action Chunking Transformer, ACT）是 Zhao 等人在 ALOHA 低成本双臂遥操作平台上提出的模仿学习方法。它把策略建模为条件变分自编码器（CVAE），由变压器编码器-解码器一次性预测未来 k 步动作序列（action chunk），执行时通过时间集成（temporal ensemble）对重叠预测加权平均，从而抑制长时程精细操作中的误差累积。

## 核心内容
- **动作分块（Action Chunking）**：策略不是逐步回归单帧动作，而是一次预测长度为 k（如 100 步）的动作块，相当于对短期"意图"建模，显著缓解模仿学习的复合误差问题。
- **CVAE 建模**：以当前关节状态与多视角图像为条件，CVAE 编码器在训练时压缩演示动作块到风格变量 z，解码器（变压器）根据条件观测和 z 重建动作块；推理时 z 直接置为先验均值。
- **时间集成（Temporal Ensemble）**：执行阶段每个时刻对多个重叠预测按指数权重平均，得到平滑、抗抖动的控制输出。
- **低成本硬件配套**：与 ALOHA 平台结合，用约 2 万美元级双臂遥操作系统采集演示数据，在拉链、开盖、插槽等精细双臂任务上达到 80%–90% 成功率。
- **影响**：ACT 成为后续 VLA（视觉-语言-动作）模型与扩散策略等方法的重要基线，"动作分块"也已成为机器人基础模型动作头的主流设计之一。
- **局限与后续方向**：原始 ACT 只支持单任务、单场景演示分布，对语言指令与开放物体的泛化能力有限；后续的扩散策略、OpenVLA、π0 等工作在动作头设计、预训练规模与多任务指令条件化上对其进行了扩展。

## 参考
- https://arxiv.org/abs/2304.13705
- https://tonyzhaozh.github.io/aloha/

## Overview
Action Chunking Transformer (ACT) is an imitation learning method proposed by Zhao et al. on the ALOHA low-cost dual-arm teleoperation platform. It models the policy as a Conditional Variational Autoencoder (CVAE), where a Transformer encoder-decoder predicts a sequence of future k-step actions (action chunk) in one shot. During execution, temporal ensemble is used to compute a weighted average of overlapping predictions, thereby suppressing error accumulation in long-horizon fine-grained manipulation tasks.

## Content
- **Action Chunking**: Instead of regressing single-frame actions step by step, the policy predicts an action chunk of length k (e.g., 100 steps) at once, effectively modeling short-term "intent" and significantly alleviating the compounding error problem in imitation learning.
- **CVAE Modeling**: Conditioned on the current joint state and multi-view images, the CVAE encoder compresses the demonstration action chunk into a style variable z during training, while the decoder (Transformer) reconstructs the action chunk based on the conditioned observations and z. During inference, z is directly set to the prior mean.
- **Temporal Ensemble**: During execution, multiple overlapping predictions at each timestep are averaged with exponential weights, yielding smooth and jitter-resistant control outputs.
- **Low-Cost Hardware Integration**: Combined with the ALOHA platform, demonstration data is collected using a dual-arm teleoperation system costing approximately $20,000. It achieves 80%–90% success rates on fine-grained dual-arm tasks such as zipping, opening lids, and inserting slots.
- **Impact**: ACT has become an important baseline for subsequent methods such as VLA (Vision-Language-Action) models and diffusion policies. "Action chunking" has also become one of the mainstream designs for action heads in robot foundation models.
- **Limitations and Future Directions**: The original ACT only supports single-task, single-scenario demonstration distributions, with limited generalization to language instructions and open objects. Subsequent works such as diffusion policies, OpenVLA, and π0 have extended it in terms of action head design, pre-training scale, and multi-task instruction conditioning.

## 개요
Action Chunking Transformer(ACT)는 Zhao 등이 ALOHA 저비용 양팔 원격 조작 플랫폼에서 제안한 모방 학습 방법입니다. 이 방법은 정책을 조건부 변분 오토인코더(CVAE)로 모델링하며, 트랜스포머 인코더-디코더가 미래 k단계 동작 시퀀스(action chunk)를 한 번에 예측합니다. 실행 시 시간적 앙상블(temporal ensemble)을 통해 중첩된 예측을 가중 평균하여 장시간 정밀 작업에서의 오류 누적을 억제합니다.

## 핵심 내용
- **동작 청킹(Action Chunking)**: 정책이 단일 프레임 동작을 단계별로 회귀하는 대신, 길이가 k(예: 100단계)인 동작 블록을 한 번에 예측합니다. 이는 단기 '의도'를 모델링하는 것과 같으며, 모방 학습의 복합 오류 문제를 크게 완화합니다.
- **CVAE 모델링**: 현재 관절 상태와 다중 시점 이미지를 조건으로 하여, CVAE 인코더는 훈련 시 데모 동작 블록을 스타일 변수 z로 압축하고, 디코더(트랜스포머)는 조건 관측값과 z를 기반으로 동작 블록을 재구성합니다. 추론 시 z는 직접 사전 평균으로 설정됩니다.
- **시간적 앙상블(Temporal Ensemble)**: 실행 단계에서 각 시점마다 여러 중첩 예측을 지수 가중치로 평균하여 부드럽고 떨림에 강한 제어 출력을 얻습니다.
- **저비용 하드웨어 연계**: ALOHA 플랫폼과 결합하여 약 2만 달러 수준의 양팔 원격 조작 시스템으로 데모 데이터를 수집하며, 지퍼 잠금, 뚜껑 열기, 슬롯 삽입 등 정밀 양팔 작업에서 80%~90%의 성공률을 달성합니다.
- **영향**: ACT는 이후 VLA(비전-언어-행동) 모델 및 확산 정책 등의 방법론에서 중요한 기준선이 되었으며, '동작 청킹'은 로봇 기초 모델의 동작 헤드 설계에서 주요 방식 중 하나로 자리 잡았습니다.
- **한계 및 후속 방향**: 원본 ACT는 단일 작업, 단일 장면 데모 분포만 지원하며, 언어 명령과 개방형 객체에 대한 일반화 능력이 제한적입니다. 이후 확산 정책, OpenVLA, π0 등의 연구는 동작 헤드 설계, 사전 훈련 규모 및 다중 작업 명령 조건화 측면에서 이를 확장했습니다.

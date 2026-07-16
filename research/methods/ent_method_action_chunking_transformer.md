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

---
$id: ent_paper_syed_expres_vla_specializing_vision_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval'
  zh: ExpReS-VLA
  ko: 'ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval'
summary:
  en: 'ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval (ExpReS-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Carnegie Mellon University.'
  zh: ExpReS-VLA 是卡内基梅隆大学于 2025 年提出的大型视觉-语言-动作模型，专为机器人操作任务设计。其核心贡献在于通过压缩经验回放与检索增强生成，在防止灾难性遗忘的同时，实现预训练 VLA 模型对特定部署环境的快速设备端适配。该方法将存储需求降低
    97%，并在 LIBERO 基准测试中将空间推理任务成功率从 82.6% 提升至 93.1%。
  ko: 'ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval (ExpReS-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Carnegie Mellon University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- expres_vla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.06202v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (921 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval (arXiv)'
  url: https://arxiv.org/abs/2511.06202
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ExpReS-VLA source
  url: https://doi.org/10.48550/arXiv.2511.06202
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
ExpReS-VLA 旨在解决现有 VLA 模型（如 OpenVLA）在零样本泛化后难以适应特定任务环境的问题。该方法通过维护一个内存高效的缓冲区，仅存储来自 OpenVLA 冻结视觉骨干的嵌入向量，从而将存储需求削减 97%。在部署时，系统利用余弦相似度检索最相似的过往经验来增强训练批次，并采用优先经验回放缓冲区保留近期成功轨迹。此外，引入的阈值混合对比损失（THCL）使模型能够同时从成功和失败的演示中学习，从而提升整体性能。

## 核心内容
### 方法架构
- **压缩经验回放**：ExpReS-VLA 不存储原始图像-动作对，而是从 OpenVLA 的冻结视觉骨干中提取并存储嵌入向量，将存储需求降低 97%。
- **检索增强生成**：在部署阶段，系统通过余弦相似度检索与当前任务最相似的 k 个过往经验，用于增强训练批次。
- **优先经验回放**：维护一个优先回放缓冲区，专门保留近期成功的轨迹，以强化有效策略。
- **阈值混合对比损失 (THCL)**：该损失函数允许模型从成功和失败的演示中学习，通过设置阈值来区分有效与无效经验，从而提升学习效率。

### 实验设置与关键数字
- **基准测试**：在 LIBERO 基准上，ExpReS-VLA 将空间推理任务成功率从 82.6% 提升至 93.1%，长时域任务从 61% 提升至 72.3%。
- **跨架构泛化**：该方法在其他架构上也表现出色，包括 π₀（+3.2 个百分点）和 OpenVLA-OFT（+1.7 个百分点）。
- **物理机器人实验**：在五项任务中，ExpReS-VLA 在分布内和分布外条件下均达到 98% 的成功率，而朴素微调的成功率分别为 84.7% 和 32%。
- **适配速度**：使用 12 个演示样本，在单张 RTX 5090 上仅需 31 秒即可完成适配。

### 结论
ExpReS-VLA 通过结合压缩经验回放与检索增强生成，有效解决了 VLA 模型在特定环境下的适配问题，同时防止灾难性遗忘。其显著降低的存储需求、快速的适配速度以及跨架构的泛化能力，使其成为机器人操作任务中高效且实用的解决方案。

## Overview
Vision-Language-Action (VLA) models like OpenVLA demonstrate impressive zero-shot generalization across robotic manipulation tasks but struggle to adapt to specific deployment environments where consistent high performance on a limited set of tasks is more valuable than broad generalization. We present EXPierence replayed, REtrieval augmented, Specialized VLA (ExpReS-VLA), a method that enables rapid on-device adaptation of pre-trained VLAs to target domains while preventing catastrophic forgetting through compressed experience replay and retrieval-augmented generation. Our approach maintains a memory-efficient buffer by storing extracted embeddings from OpenVLA's frozen vision backbone, reducing storage requirements by 97% compared to raw image-action pairs. During deployment, ExpReS-VLA retrieves the $k$ most similar past experiences using cosine similarity to augment training batches, while a prioritized experience replay buffer preserves recently successful trajectories. To leverage failed attempts, we introduce Thresholded Hybrid Contrastive Loss (THCL), enabling the model to learn from both successful and unsuccessful demonstrations. Experiments on the LIBERO benchmark show improvements from 82.6% to 93.1% on spatial reasoning and 61% to 72.3% on long-horizon tasks over base OpenVLA, with gains across architectures including $π_0$ (+3.2 points) and OpenVLA-OFT (+1.7 points). Physical robot experiments across five tasks demonstrate 98% success on both in-distribution and out-of-distribution conditions, improving from 84.7% and 32% respectively for naive fine-tuning. Adaptation completes in 31 seconds using 12 demonstrations on a single RTX 5090.

## Overview
Vision-Language-Action (VLA) models like OpenVLA demonstrate impressive zero-shot generalization across robotic manipulation tasks but struggle to adapt to specific deployment environments where consistent high performance on a limited set of tasks is more valuable than broad generalization. We present EXPierence replayed, REtrieval augmented, Specialized VLA (ExpReS-VLA), a method that enables rapid on-device adaptation of pre-trained VLAs to target domains while preventing catastrophic forgetting through compressed experience replay and retrieval-augmented generation. Our approach maintains a memory-efficient buffer by storing extracted embeddings from OpenVLA's frozen vision backbone, reducing storage requirements by 97% compared to raw image-action pairs. During deployment, ExpReS-VLA retrieves the \(k\) most similar past experiences using cosine similarity to augment training batches, while a prioritized experience replay buffer preserves recently successful trajectories. To leverage failed attempts, we introduce Thresholded Hybrid Contrastive Loss (THCL), enabling the model to learn from both successful and unsuccessful demonstrations. Experiments on the LIBERO benchmark show improvements from 82.6% to 93.1% on spatial reasoning and 61% to 72.3% on long-horizon tasks over base OpenVLA, with gains across architectures including \(\pi_0\) (+3.2 points) and OpenVLA-OFT (+1.7 points). Physical robot experiments across five tasks demonstrate 98% success on both in-distribution and out-of-distribution conditions, improving from 84.7% and 32% respectively for naive fine-tuning. Adaptation completes in 31 seconds using 12 demonstrations on a single RTX 5090.

## Content
Vision-Language-Action (VLA) models like OpenVLA demonstrate impressive zero-shot generalization across robotic manipulation tasks but struggle to adapt to specific deployment environments where consistent high performance on a limited set of tasks is more valuable than broad generalization. We present EXPierence replayed, REtrieval augmented, Specialized VLA (ExpReS-VLA), a method that enables rapid on-device adaptation of pre-trained VLAs to target domains while preventing catastrophic forgetting through compressed experience replay and retrieval-augmented generation. Our approach maintains a memory-efficient buffer by storing extracted embeddings from OpenVLA's frozen vision backbone, reducing storage requirements by 97% compared to raw image-action pairs. During deployment, ExpReS-VLA retrieves the \(k\) most similar past experiences using cosine similarity to augment training batches, while a prioritized experience replay buffer preserves recently successful trajectories. To leverage failed attempts, we introduce Thresholded Hybrid Contrastive Loss (THCL), enabling the model to learn from both successful and unsuccessful demonstrations. Experiments on the LIBERO benchmark show improvements from 82.6% to 93.1% on spatial reasoning and 61% to 72.3% on long-horizon tasks over base OpenVLA, with gains across architectures including \(\pi_0\) (+3.2 points) and OpenVLA-OFT (+1.7 points). Physical robot experiments across five tasks demonstrate 98% success on both in-distribution and out-of-distribution conditions, improving from 84.7% and 32% respectively for naive fine-tuning. Adaptation completes in 31 seconds using 12 demonstrations on a single RTX 5090.

## 参考
- http://arxiv.org/abs/2511.06202v2

## 개요
ExpReS-VLA는 기존 VLA 모델(예: OpenVLA)이 제로샷 일반화 후 특정 작업 환경에 적응하기 어려운 문제를 해결하기 위해 설계되었습니다. 이 방법은 메모리 효율적인 버퍼를 유지하여 OpenVLA의 고정된 시각 백본에서 추출된 임베딩 벡터만 저장함으로써 저장 요구량을 97% 절감합니다. 배포 시 시스템은 코사인 유사도를 활용하여 가장 유사한 과거 경험을 검색해 훈련 배치를 강화하며, 우선 경험 재생 버퍼를 사용해 최근 성공 궤적을 보존합니다. 또한, 도입된 임계값 혼합 대비 손실(THCL)은 모델이 성공 및 실패 데모에서 동시에 학습할 수 있게 하여 전반적인 성능을 향상시킵니다.

## 핵심 내용
### 방법 아키텍처
- **압축 경험 재생**: ExpReS-VLA는 원본 이미지-행동 쌍을 저장하지 않고 OpenVLA의 고정된 시각 백본에서 추출된 임베딩 벡터를 저장하여 저장 요구량을 97% 절감합니다.
- **검색 증강 생성**: 배포 단계에서 시스템은 코사인 유사도를 통해 현재 작업과 가장 유사한 k개의 과거 경험을 검색하여 훈련 배치를 강화합니다.
- **우선 경험 재생**: 최근 성공 궤적을 전용으로 보존하는 우선 재생 버퍼를 유지하여 효과적인 정책을 강화합니다.
- **임계값 혼합 대비 손실 (THCL)**: 이 손실 함수는 모델이 성공 및 실패 데모에서 학습할 수 있게 하며, 임계값을 설정해 유효한 경험과 무효한 경험을 구분함으로써 학습 효율을 높입니다.

### 실험 설정 및 주요 수치
- **벤치마크**: LIBERO 벤치마크에서 ExpReS-VLA는 공간 추론 작업 성공률을 82.6%에서 93.1%로, 장기 시간 도메인 작업을 61%에서 72.3%로 향상시켰습니다.
- **교차 아키텍처 일반화**: 이 방법은 π₀(+3.2퍼센트 포인트) 및 OpenVLA-OFT(+1.7퍼센트 포인트)를 포함한 다른 아키텍처에서도 우수한 성능을 보였습니다.
- **물리 로봇 실험**: 다섯 가지 작업에서 ExpReS-VLA는 분포 내 및 분포 외 조건 모두에서 98%의 성공률을 달성했으며, 단순 미세 조정은 각각 84.7% 및 32%의 성공률을 보였습니다.
- **적응 속도**: 12개의 데모 샘플을 사용하여 단일 RTX 5090에서 단 31초 만에 적응을 완료합니다.

### 결론
ExpReS-VLA는 압축 경험 재생과 검색 증강 생성을 결합하여 특정 환경에서 VLA 모델의 적응 문제를 효과적으로 해결하면서도 파괴적 망각을 방지합니다. 현저히 낮아진 저장 요구량, 빠른 적응 속도, 그리고 교차 아키텍처 일반화 능력은 로봇 조작 작업에서 효율적이고 실용적인 솔루션으로 만듭니다.

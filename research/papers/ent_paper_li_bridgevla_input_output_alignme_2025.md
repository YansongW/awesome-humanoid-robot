---
$id: ent_paper_li_bridgevla_input_output_alignme_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models'
  zh: BridgeVLA
  ko: 'BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models'
summary:
  en: 'BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models (BridgeVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by ByteDance Seed, School of Artificial
    Intelligence, University of Chinese Academy of Sciences, Institute of Automation, Chinese Academy of Sciences, FiveAges,
    Nanjing University, and published at NIPS25.'
  zh: BridgeVLA 是字节跳动 Seed、中国科学院大学、中国科学院自动化研究所、FiveAges、南京大学等机构在 NIPS25 上提出的 3D 视觉-语言-动作模型。其核心贡献在于通过将 3D 输入投影为多张 2D 图像并与 VLM
    骨干对齐，同时利用 2D 热图预测动作，实现了输入输出空间在 2D 图像空间中的统一。该模型在 RLBench、COLOSSEUM、GemBench 等仿真基准和真实机器人实验中均显著超越现有方法，展现出极高的样本效率。
  ko: 'BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models (BridgeVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by ByteDance Seed, School of Artificial
    Intelligence, University of Chinese Academy of Sciences, Institute of Automation, Chinese Academy of Sciences, FiveAges,
    Nanjing University, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- bridgevla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.07961v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1153 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models (arXiv)'
  url: https://arxiv.org/abs/2506.07961
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: BridgeVLA source
  url: https://doi.org/10.48550/arXiv.2506.07961
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
BridgeVLA 针对现有 VLA 模型在利用 3D 信号时样本效率低下的问题，提出了一种新颖的 3D VLA 架构。该方法首先将 3D 输入投影为多个 2D 视图，确保与预训练 VLM 骨干的输入对齐；然后使用 2D 热图作为动作预测的表示，从而将输入和输出空间统一在一致的 2D 图像空间中。此外，作者还提出了一种可扩展的预训练方法，使 VLM 骨干在下游策略学习前就具备预测 2D 热图的能力。大量实验表明，BridgeVLA 能够高效且有效地学习 3D 操作任务。

## 核心内容
### 方法架构
BridgeVLA 的核心设计围绕输入-输出对齐展开：
- **输入对齐**：将 3D 点云或 RGB-D 数据投影到多个预设的 2D 视角（如前、上、侧视图），生成多张 2D 图像。这些图像直接输入到预训练的 VLM 骨干（如 CLIP 或类似架构）中，避免了 3D 数据与 2D 预训练模型之间的模态鸿沟。
- **输出对齐**：动作预测被建模为 2D 热图回归问题。模型输出多个 2D 热图，每个热图对应动作空间中的一个维度（如末端执行器的位置、方向或抓取状态）。通过从热图中解码出关键点坐标，得到最终的动作指令。这使得输出空间与输入空间同属 2D 图像域，简化了学习难度。
- **可扩展预训练**：在正式的策略学习之前，作者设计了一个预训练阶段，让 VLM 骨干学习预测 2D 热图。该阶段使用大规模无标签或弱标签数据，使模型掌握从视觉特征到空间位置映射的基本能力，从而加速下游策略的收敛。

### 实验设置与关键结果
- **仿真基准**：在三个标准基准上评估：
  - **RLBench**：BridgeVLA 将平均成功率从 81.4% 提升至 88.2%。
  - **COLOSSEUM**：在更具挑战性的泛化设置中，平均成功率从 56.7% 提升至 64.0%。
  - **GemBench**：在所有对比基线中取得最高平均成功率。
- **真实机器人实验**：在真实场景中，BridgeVLA 比最先进的基线方法平均高出 32%。在多种分布外设置（如视觉干扰、未见指令）下表现出稳健的泛化能力。
- **样本效率**：在 10 个以上任务中，每个任务仅使用 3 条轨迹进行训练，即可达到 96.8% 的成功率，凸显了其极高的样本效率。

### 结论
BridgeVLA 通过输入-输出对齐策略，成功将 3D 操作学习与预训练 VLM 的能力相结合，在多个基准和真实场景中实现了高效、鲁棒的操控性能。其统一的 2D 图像空间表示和可扩展预训练方法为未来 VLA 模型的设计提供了新思路。项目网站：https://bridgevla.github.io/

## Overview
Recently, leveraging pre-trained vision-language models (VLMs) for building vision-language-action (VLA) models has emerged as a promising approach to effective robot manipulation learning. However, only few methods incorporate 3D signals into VLMs for action prediction, and they do not fully leverage the spatial structure inherent in 3D data, leading to low sample efficiency. In this paper, we introduce BridgeVLA, a novel 3D VLA model that (1) projects 3D inputs to multiple 2D images, ensuring input alignment with the VLM backbone, and (2) utilizes 2D heatmaps for action prediction, unifying the input and output spaces within a consistent 2D image space. In addition, we propose a scalable pre-training method that equips the VLM backbone with the capability to predict 2D heatmaps before downstream policy learning. Extensive experiments show the proposed method is able to learn 3D manipulation efficiently and effectively. BridgeVLA outperforms state-of-the-art baseline methods across three simulation benchmarks. In RLBench, it improves the average success rate from 81.4% to 88.2%. In COLOSSEUM, it demonstrates significantly better performance in challenging generalization settings, boosting the average success rate from 56.7% to 64.0%. In GemBench, it surpasses all the comparing baseline methods in terms of average success rate. In real-robot experiments, BridgeVLA outperforms a state-of-the-art baseline method by 32% on average. It generalizes robustly in multiple out-of-distribution settings, including visual disturbances and unseen instructions. Remarkably, it is able to achieve a success rate of 96.8% on 10+ tasks with only 3 trajectories per task, highlighting its extraordinary sample efficiency. Project Website:https://bridgevla.github.io/

## Overview
Recently, leveraging pre-trained vision-language models (VLMs) for building vision-language-action (VLA) models has emerged as a promising approach to effective robot manipulation learning. However, only few methods incorporate 3D signals into VLMs for action prediction, and they do not fully leverage the spatial structure inherent in 3D data, leading to low sample efficiency. In this paper, we introduce BridgeVLA, a novel 3D VLA model that (1) projects 3D inputs to multiple 2D images, ensuring input alignment with the VLM backbone, and (2) utilizes 2D heatmaps for action prediction, unifying the input and output spaces within a consistent 2D image space. In addition, we propose a scalable pre-training method that equips the VLM backbone with the capability to predict 2D heatmaps before downstream policy learning. Extensive experiments show the proposed method is able to learn 3D manipulation efficiently and effectively. BridgeVLA outperforms state-of-the-art baseline methods across three simulation benchmarks. In RLBench, it improves the average success rate from 81.4% to 88.2%. In COLOSSEUM, it demonstrates significantly better performance in challenging generalization settings, boosting the average success rate from 56.7% to 64.0%. In GemBench, it surpasses all the comparing baseline methods in terms of average success rate. In real-robot experiments, BridgeVLA outperforms a state-of-the-art baseline method by 32% on average. It generalizes robustly in multiple out-of-distribution settings, including visual disturbances and unseen instructions. Remarkably, it is able to achieve a success rate of 96.8% on 10+ tasks with only 3 trajectories per task, highlighting its extraordinary sample efficiency. Project Website: https://bridgevla.github.io/

## Content
Recently, leveraging pre-trained vision-language models (VLMs) for building vision-language-action (VLA) models has emerged as a promising approach to effective robot manipulation learning. However, only few methods incorporate 3D signals into VLMs for action prediction, and they do not fully leverage the spatial structure inherent in 3D data, leading to low sample efficiency. In this paper, we introduce BridgeVLA, a novel 3D VLA model that (1) projects 3D inputs to multiple 2D images, ensuring input alignment with the VLM backbone, and (2) utilizes 2D heatmaps for action prediction, unifying the input and output spaces within a consistent 2D image space. In addition, we propose a scalable pre-training method that equips the VLM backbone with the capability to predict 2D heatmaps before downstream policy learning. Extensive experiments show the proposed method is able to learn 3D manipulation efficiently and effectively. BridgeVLA outperforms state-of-the-art baseline methods across three simulation benchmarks. In RLBench, it improves the average success rate from 81.4% to 88.2%. In COLOSSEUM, it demonstrates significantly better performance in challenging generalization settings, boosting the average success rate from 56.7% to 64.0%. In GemBench, it surpasses all the comparing baseline methods in terms of average success rate. In real-robot experiments, BridgeVLA outperforms a state-of-the-art baseline method by 32% on average. It generalizes robustly in multiple out-of-distribution settings, including visual disturbances and unseen instructions. Remarkably, it is able to achieve a success rate of 96.8% on 10+ tasks with only 3 trajectories per task, highlighting its extraordinary sample efficiency. Project Website: https://bridgevla.github.io/

## 参考
- http://arxiv.org/abs/2506.07961v2

## 개요
BridgeVLA는 기존 VLA 모델이 3D 신호를 활용할 때 샘플 효율이 낮은 문제를 해결하기 위해 새로운 3D VLA 아키텍처를 제안한다. 이 방법은 먼저 3D 입력을 여러 2D 뷰로 투영하여 사전 학습된 VLM 백본의 입력과 정렬되도록 보장한다. 그런 다음 2D 히트맵을 동작 예측의 표현으로 사용하여 입력 및 출력 공간을 일관된 2D 이미지 공간으로 통합한다. 또한, 저자는 다운스트림 정책 학습 전에 VLM 백본이 2D 히트맵을 예측할 수 있도록 하는 확장 가능한 사전 학습 방법을 제안한다. 광범위한 실험을 통해 BridgeVLA가 3D 조작 작업을 효율적이고 효과적으로 학습할 수 있음을 보여준다.

## 핵심 내용
### 방법 아키텍처
BridgeVLA의 핵심 설계는 입력-출력 정렬을 중심으로 이루어진다:
- **입력 정렬**: 3D 포인트 클라우드 또는 RGB-D 데이터를 여러 사전 설정된 2D 시점(예: 전면, 상면, 측면 뷰)으로 투영하여 여러 2D 이미지를 생성한다. 이러한 이미지는 사전 학습된 VLM 백본(예: CLIP 또는 유사 아키텍처)에 직접 입력되어 3D 데이터와 2D 사전 학습 모델 간의 모달리티 격차를 방지한다.
- **출력 정렬**: 동작 예측은 2D 히트맵 회귀 문제로 모델링된다. 모델은 여러 2D 히트맵을 출력하며, 각 히트맵은 동작 공간의 한 차원(예: 엔드 이펙터의 위치, 방향 또는 그립 상태)에 해당한다. 히트맵에서 키포인트 좌표를 디코딩하여 최종 동작 명령을 얻는다. 이를 통해 출력 공간과 입력 공간이 동일한 2D 이미지 도메인에 속하게 되어 학습 난이도가 단순화된다.
- **확장 가능한 사전 학습**: 공식적인 정책 학습 전에, 저자는 VLM 백본이 2D 히트맵을 예측하도록 학습시키는 사전 학습 단계를 설계한다. 이 단계는 대규모의 라벨이 없거나 약한 라벨이 있는 데이터를 사용하여 모델이 시각적 특징에서 공간 위치 매핑까지의 기본 능력을 습득하게 하여 다운스트림 정책의 수렴을 가속화한다.

### 실험 설정 및 주요 결과
- **시뮬레이션 벤치마크**: 세 가지 표준 벤치마크에서 평가:
  - **RLBench**: BridgeVLA는 평균 성공률을 81.4%에서 88.2%로 향상시켰다.
  - **COLOSSEUM**: 더 도전적인 일반화 설정에서 평균 성공률이 56.7%에서 64.0%로 향상되었다.
  - **GemBench**: 모든 비교 기준선 중 가장 높은 평균 성공률을 달성했다.
- **실제 로봇 실험**: 실제 시나리오에서 BridgeVLA는 최첨단 기준선 방법보다 평균 32% 더 높은 성능을 보였다. 다양한 분포 외 설정(예: 시각적 방해, 보지 못한 명령)에서 강건한 일반화 능력을 입증했다.
- **샘플 효율**: 10개 이상의 작업에서 각 작업당 3개의 궤적만 사용하여 훈련했음에도 96.8%의 성공률을 달성하여 매우 높은 샘플 효율을 강조한다.

### 결론
BridgeVLA는 입력-출력 정렬 전략을 통해 3D 조작 학습과 사전 학습된 VLM의 능력을 성공적으로 결합하여 여러 벤치마크와 실제 시나리오에서 효율적이고 강건한 조작 성능을 구현했다. 통합된 2D 이미지 공간 표현과 확장 가능한 사전 학습 방법은 향후 VLA 모델 설계에 새로운 통찰력을 제공한다. 프로젝트 웹사이트: https://bridgevla.github.io/

---
$id: ent_paper_cao_fastdrivevla_efficient_end_to_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FastDriveVLA: Efficient End-to-End Driving via Plug-and-Play Reconstruction-based Token Pruning'
  zh: FastDriveVLA
  ko: 'FastDriveVLA: Efficient End-to-End Driving via Plug-and-Play Reconstruction-based Token Pruning'
summary:
  en: 'FastDriveVLA: Efficient End-to-End Driving via Plug-and-Play Reconstruction-based Token Pruning (FastDriveVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Peking University, XPeng Motors.'
  zh: FastDriveVLA 是北京大学与小鹏汽车于 2025 年提出的高效端到端驾驶大模型，其核心贡献在于一种即插即用的视觉令牌剪枝框架 ReconPruner。该方法通过基于 MAE 风格的前景-背景对抗重建策略，在保留关键前景信息的同时大幅降低计算成本，在
    nuScenes 开环规划基准上取得了最优结果。
  ko: 'FastDriveVLA: Efficient End-to-End Driving via Plug-and-Play Reconstruction-based Token Pruning (FastDriveVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Peking University, XPeng Motors.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- fastdrivevla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.23318v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (759 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'FastDriveVLA: Efficient End-to-End Driving via Plug-and-Play Reconstruction-based Token Pruning (arXiv)'
  url: https://arxiv.org/abs/2507.23318
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: FastDriveVLA source
  url: https://doi.org/10.48550/arXiv.2507.23318
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
针对 VLA 模型在自动驾驶中因长视觉令牌导致的高计算成本问题，FastDriveVLA 提出了一种名为 ReconPruner 的即插即用视觉令牌剪枝器。该剪枝器受人类驾驶员关注前景区域的启发，采用 MAE 风格的像素重建策略，并通过新颖的前景-背景对抗重建训练方法，使模型能优先保留包含前景信息的视觉令牌。ReconPruner 训练完成后，可无缝应用于具有相同视觉编码器的不同 VLA 模型，无需重新训练。为支持训练，团队还构建了包含 24.1 万对图像-掩码的大规模数据集 nuScenes-FG。

## 核心内容
### 方法架构
- **核心问题**：VLA 模型的长视觉令牌导致计算成本过高，现有基于视觉令牌相似性或视觉-文本注意力的剪枝方法在自动驾驶场景中表现不佳。
- **ReconPruner 设计**：采用 MAE 风格的像素重建任务，通过对抗式前景-背景重建策略训练，使剪枝器学会优先保留包含关键前景信息的视觉令牌。
- **即插即用特性**：训练完成后，ReconPruner 可无缝应用于具有相同视觉编码器的不同 VLA 模型，无需重新训练或调整。

### 数据集与实验设置
- **nuScenes-FG 数据集**：包含 241K 图像-掩码对，标注了前景区域，专门用于训练 ReconPruner。
- **基准测试**：在 nuScenes 开环规划基准上进行评估，测试不同剪枝比例下的性能。

### 关键结果
- 在不同剪枝比例下，FastDriveVLA 均取得了最优结果（state-of-the-art），在保持高规划精度的同时显著降低了计算开销。
- 实验验证了前景信息保留对自动驾驶决策的有效性，证明了 ReconPruner 在复杂场景中的鲁棒性。

## Overview
Vision-Language-Action (VLA) models have demonstrated significant potential in complex scene understanding and action reasoning, leading to their increasing adoption in end-to-end autonomous driving systems. However, the long visual tokens of VLA models greatly increase computational costs. Current visual token pruning methods in Vision-Language Models (VLM) rely on either visual token similarity or visual-text attention, but both have shown poor performance in autonomous driving scenarios. Given that human drivers concentrate on relevant foreground areas while driving, we assert that retaining visual tokens containing this foreground information is essential for effective decision-making. Inspired by this, we propose FastDriveVLA, a novel reconstruction-based vision token pruning framework designed specifically for autonomous driving. FastDriveVLA includes a plug-and-play visual token pruner called ReconPruner, which prioritizes foreground information through MAE-style pixel reconstruction. A novel adversarial foreground-background reconstruction strategy is designed to train ReconPruner for the visual encoder of VLA models. Once trained, ReconPruner can be seamlessly applied to different VLA models with the same visual encoder without retraining. To train ReconPruner, we also introduce a large-scale dataset called nuScenes-FG, consisting of 241K image-mask pairs with annotated foreground regions. Our approach achieves state-of-the-art results on the nuScenes open-loop planning benchmark across different pruning ratios.

## 参考
- http://arxiv.org/abs/2507.23318v4

## 개요
VLA 모델이 자율주행에서 긴 시각적 토큰으로 인해 발생하는 높은 계산 비용 문제를 해결하기 위해, FastDriveVLA는 ReconPruner라는 플러그 앤 플레이 시각적 토큰 프루너를 제안합니다. 이 프루너는 인간 운전자가 전경 영역에 주의를 기울이는 점에서 영감을 받아, MAE 스타일의 픽셀 재구성 전략을 채택하고, 새로운 전경-배경 적대적 재구성 훈련 방법을 통해 모델이 전경 정보를 포함한 시각적 토큰을 우선적으로 보존하도록 합니다. ReconPruner 훈련이 완료되면, 동일한 시각적 인코더를 가진 다른 VLA 모델에 재훈련 없이 원활하게 적용할 수 있습니다. 훈련을 지원하기 위해, 팀은 24.1만 쌍의 이미지-마스크 대규모 데이터셋인 nuScenes-FG도 구축했습니다.

## 핵심 내용
### 방법 아키텍처
- **핵심 문제**: VLA 모델의 긴 시각적 토큰으로 인해 계산 비용이 과도하게 높아지며, 기존의 시각적 토큰 유사성 또는 시각-텍스트 주의 기반 프루닝 방법은 자율주행 시나리오에서 성능이 저조합니다.
- **ReconPruner 설계**: MAE 스타일의 픽셀 재구성 작업을 채택하고, 적대적 전경-배경 재구성 전략을 통해 훈련하여, 프루너가 핵심 전경 정보를 포함한 시각적 토큰을 우선적으로 보존하도록 학습합니다.
- **플러그 앤 플레이 특성**: 훈련이 완료되면, ReconPruner는 동일한 시각적 인코더를 가진 다른 VLA 모델에 재훈련이나 조정 없이 원활하게 적용할 수 있습니다.

### 데이터셋 및 실험 설정
- **nuScenes-FG 데이터셋**: 전경 영역이 주석 처리된 241K 이미지-마스크 쌍을 포함하며, ReconPruner 훈련에 특화되어 있습니다.
- **벤치마크 테스트**: nuScenes 개방 루프 계획 벤치마크에서 평가하며, 다양한 프루닝 비율에서의 성능을 테스트합니다.

### 주요 결과
- 다양한 프루닝 비율에서 FastDriveVLA는 모두 최적의 결과(state-of-the-art)를 달성했으며, 높은 계획 정확도를 유지하면서 계산 오버헤드를 크게 줄였습니다.
- 실험을 통해 전경 정보 보존이 자율주행 의사결정에 미치는 효과를 검증했으며, 복잡한 시나리오에서 ReconPruner의 견고성을 입증했습니다.

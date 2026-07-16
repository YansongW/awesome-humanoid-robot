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
  zh: 'FastDriveVLA: Efficient End-to-End Driving via Plug-and-Play Reconstruction-based Token Pruning (FastDriveVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Peking University, XPeng Motors.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.23318v4.
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
Vision-Language-Action (VLA) models have demonstrated significant potential in complex scene understanding and action reasoning, leading to their increasing adoption in end-to-end autonomous driving systems. However, the long visual tokens of VLA models greatly increase computational costs. Current visual token pruning methods in Vision-Language Models (VLM) rely on either visual token similarity or visual-text attention, but both have shown poor performance in autonomous driving scenarios. Given that human drivers concentrate on relevant foreground areas while driving, we assert that retaining visual tokens containing this foreground information is essential for effective decision-making. Inspired by this, we propose FastDriveVLA, a novel reconstruction-based vision token pruning framework designed specifically for autonomous driving. FastDriveVLA includes a plug-and-play visual token pruner called ReconPruner, which prioritizes foreground information through MAE-style pixel reconstruction. A novel adversarial foreground-background reconstruction strategy is designed to train ReconPruner for the visual encoder of VLA models. Once trained, ReconPruner can be seamlessly applied to different VLA models with the same visual encoder without retraining. To train ReconPruner, we also introduce a large-scale dataset called nuScenes-FG, consisting of 241K image-mask pairs with annotated foreground regions. Our approach achieves state-of-the-art results on the nuScenes open-loop planning benchmark across different pruning ratios.

## 核心内容
Vision-Language-Action (VLA) models have demonstrated significant potential in complex scene understanding and action reasoning, leading to their increasing adoption in end-to-end autonomous driving systems. However, the long visual tokens of VLA models greatly increase computational costs. Current visual token pruning methods in Vision-Language Models (VLM) rely on either visual token similarity or visual-text attention, but both have shown poor performance in autonomous driving scenarios. Given that human drivers concentrate on relevant foreground areas while driving, we assert that retaining visual tokens containing this foreground information is essential for effective decision-making. Inspired by this, we propose FastDriveVLA, a novel reconstruction-based vision token pruning framework designed specifically for autonomous driving. FastDriveVLA includes a plug-and-play visual token pruner called ReconPruner, which prioritizes foreground information through MAE-style pixel reconstruction. A novel adversarial foreground-background reconstruction strategy is designed to train ReconPruner for the visual encoder of VLA models. Once trained, ReconPruner can be seamlessly applied to different VLA models with the same visual encoder without retraining. To train ReconPruner, we also introduce a large-scale dataset called nuScenes-FG, consisting of 241K image-mask pairs with annotated foreground regions. Our approach achieves state-of-the-art results on the nuScenes open-loop planning benchmark across different pruning ratios.

## 参考
- http://arxiv.org/abs/2507.23318v4

## Overview
Vision-Language-Action (VLA) models have demonstrated significant potential in complex scene understanding and action reasoning, leading to their increasing adoption in end-to-end autonomous driving systems. However, the long visual tokens of VLA models greatly increase computational costs. Current visual token pruning methods in Vision-Language Models (VLM) rely on either visual token similarity or visual-text attention, but both have shown poor performance in autonomous driving scenarios. Given that human drivers concentrate on relevant foreground areas while driving, we assert that retaining visual tokens containing this foreground information is essential for effective decision-making. Inspired by this, we propose FastDriveVLA, a novel reconstruction-based vision token pruning framework designed specifically for autonomous driving. FastDriveVLA includes a plug-and-play visual token pruner called ReconPruner, which prioritizes foreground information through MAE-style pixel reconstruction. A novel adversarial foreground-background reconstruction strategy is designed to train ReconPruner for the visual encoder of VLA models. Once trained, ReconPruner can be seamlessly applied to different VLA models with the same visual encoder without retraining. To train ReconPruner, we also introduce a large-scale dataset called nuScenes-FG, consisting of 241K image-mask pairs with annotated foreground regions. Our approach achieves state-of-the-art results on the nuScenes open-loop planning benchmark across different pruning ratios.

## Content
Vision-Language-Action (VLA) models have demonstrated significant potential in complex scene understanding and action reasoning, leading to their increasing adoption in end-to-end autonomous driving systems. However, the long visual tokens of VLA models greatly increase computational costs. Current visual token pruning methods in Vision-Language Models (VLM) rely on either visual token similarity or visual-text attention, but both have shown poor performance in autonomous driving scenarios. Given that human drivers concentrate on relevant foreground areas while driving, we assert that retaining visual tokens containing this foreground information is essential for effective decision-making. Inspired by this, we propose FastDriveVLA, a novel reconstruction-based vision token pruning framework designed specifically for autonomous driving. FastDriveVLA includes a plug-and-play visual token pruner called ReconPruner, which prioritizes foreground information through MAE-style pixel reconstruction. A novel adversarial foreground-background reconstruction strategy is designed to train ReconPruner for the visual encoder of VLA models. Once trained, ReconPruner can be seamlessly applied to different VLA models with the same visual encoder without retraining. To train ReconPruner, we also introduce a large-scale dataset called nuScenes-FG, consisting of 241K image-mask pairs with annotated foreground regions. Our approach achieves state-of-the-art results on the nuScenes open-loop planning benchmark across different pruning ratios.

## 개요
Vision-Language-Action (VLA) 모델은 복잡한 장면 이해와 행동 추론에서 상당한 잠재력을 입증하며, 엔드투엔드 자율주행 시스템에 점점 더 많이 채택되고 있습니다. 그러나 VLA 모델의 긴 시각적 토큰은 계산 비용을 크게 증가시킵니다. 현재 Vision-Language Models (VLM)의 시각적 토큰 프루닝 방법은 시각적 토큰 유사성 또는 시각-텍스트 주의(attention)에 의존하지만, 두 방법 모두 자율주행 시나리오에서 성능이 낮은 것으로 나타났습니다. 인간 운전자가 운전 중 관련 전경 영역에 집중한다는 점을 고려하여, 우리는 효과적인 의사 결정을 위해 이 전경 정보를 포함하는 시각적 토큰을 유지하는 것이 필수적이라고 주장합니다. 이에 영감을 받아, 우리는 자율주행을 위해 특별히 설계된 새로운 재구성 기반 시각 토큰 프루닝 프레임워크인 FastDriveVLA를 제안합니다. FastDriveVLA는 ReconPruner라는 플러그 앤 플레이 시각 토큰 프루너를 포함하며, 이는 MAE 스타일의 픽셀 재구성을 통해 전경 정보를 우선시합니다. VLA 모델의 시각적 인코더를 위해 ReconPruner를 훈련시키기 위해 새로운 적대적 전경-배경 재구성 전략이 설계되었습니다. 훈련이 완료되면 ReconPruner는 재훈련 없이 동일한 시각적 인코더를 가진 다른 VLA 모델에 원활하게 적용될 수 있습니다. ReconPruner를 훈련시키기 위해, 우리는 주석이 달린 전경 영역을 포함하는 241K 이미지-마스크 쌍으로 구성된 대규모 데이터셋인 nuScenes-FG도 소개합니다. 우리의 접근 방식은 다양한 프루닝 비율에서 nuScenes 개방 루프 계획 벤치마크에서 최첨단 결과를 달성합니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 복잡한 장면 이해와 행동 추론에서 상당한 잠재력을 입증하며, 엔드투엔드 자율주행 시스템에 점점 더 많이 채택되고 있습니다. 그러나 VLA 모델의 긴 시각적 토큰은 계산 비용을 크게 증가시킵니다. 현재 Vision-Language Models (VLM)의 시각적 토큰 프루닝 방법은 시각적 토큰 유사성 또는 시각-텍스트 주의(attention)에 의존하지만, 두 방법 모두 자율주행 시나리오에서 성능이 낮은 것으로 나타났습니다. 인간 운전자가 운전 중 관련 전경 영역에 집중한다는 점을 고려하여, 우리는 효과적인 의사 결정을 위해 이 전경 정보를 포함하는 시각적 토큰을 유지하는 것이 필수적이라고 주장합니다. 이에 영감을 받아, 우리는 자율주행을 위해 특별히 설계된 새로운 재구성 기반 시각 토큰 프루닝 프레임워크인 FastDriveVLA를 제안합니다. FastDriveVLA는 ReconPruner라는 플러그 앤 플레이 시각 토큰 프루너를 포함하며, 이는 MAE 스타일의 픽셀 재구성을 통해 전경 정보를 우선시합니다. VLA 모델의 시각적 인코더를 위해 ReconPruner를 훈련시키기 위해 새로운 적대적 전경-배경 재구성 전략이 설계되었습니다. 훈련이 완료되면 ReconPruner는 재훈련 없이 동일한 시각적 인코더를 가진 다른 VLA 모델에 원활하게 적용될 수 있습니다. ReconPruner를 훈련시키기 위해, 우리는 주석이 달린 전경 영역을 포함하는 241K 이미지-마스크 쌍으로 구성된 대규모 데이터셋인 nuScenes-FG도 소개합니다. 우리의 접근 방식은 다양한 프루닝 비율에서 nuScenes 개방 루프 계획 벤치마크에서 최첨단 결과를 달성합니다.

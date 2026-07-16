---
$id: ent_paper_zhang_4d_vla_spatiotemporal_vision_l_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '4D-VLA: Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration'
  zh: 4D-VLA
  ko: '4D-VLA: Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration'
summary:
  en: '4D-VLA: Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration (4D-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Fudan University, HUAWEI Noah''s Ark Lab, and published at NIPS25.'
  zh: '4D-VLA: Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration (4D-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Fudan University, HUAWEI Noah''s Ark Lab, and published at NIPS25.'
  ko: '4D-VLA: Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration (4D-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Fudan University, HUAWEI Noah''s Ark Lab, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- 4d_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.22242v2.
sources:
- id: src_001
  type: paper
  title: '4D-VLA: Spatiotemporal Vision-Language-Action Pretraining with Cross-Scene Calibration (arXiv)'
  url: https://arxiv.org/abs/2506.22242
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 4D-VLA source
  url: https://doi.org/10.48550/arXiv.2506.22242
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Leveraging diverse robotic data for pretraining remains a critical challenge. Existing methods typically model the dataset's action distribution using simple observations as inputs. However, these inputs are often incomplete, resulting in a dispersed conditional action distribution-an issue we refer to as coordinate system chaos and state chaos. This inconsistency significantly hampers pretraining efficiency. To address this, we propose 4D-VLA, a novel approach that effectively integrates 4D information into the input to mitigate these sources of chaos. Our model introduces depth and temporal information into visual features with sequential RGB-D inputs, aligning the coordinate systems of the robot and the scene. This alignment endows the model with strong spatiotemporal reasoning capabilities while minimizing training overhead. Additionally, we introduce memory bank sampling, a frame sampling strategy designed to extract informative frames from historical images, further improving effectiveness and efficiency. Experimental results demonstrate that our pretraining method and architectural components substantially enhance model performance. In both simulated and real-world experiments, our model achieves a significant increase in success rate over OpenVLA. To further assess spatial perception and generalization to novel views, we introduce MV-Bench, a multi-view simulation benchmark. Our model consistently outperforms existing methods, demonstrating stronger spatial understanding and adaptability.

## 核心内容
Leveraging diverse robotic data for pretraining remains a critical challenge. Existing methods typically model the dataset's action distribution using simple observations as inputs. However, these inputs are often incomplete, resulting in a dispersed conditional action distribution-an issue we refer to as coordinate system chaos and state chaos. This inconsistency significantly hampers pretraining efficiency. To address this, we propose 4D-VLA, a novel approach that effectively integrates 4D information into the input to mitigate these sources of chaos. Our model introduces depth and temporal information into visual features with sequential RGB-D inputs, aligning the coordinate systems of the robot and the scene. This alignment endows the model with strong spatiotemporal reasoning capabilities while minimizing training overhead. Additionally, we introduce memory bank sampling, a frame sampling strategy designed to extract informative frames from historical images, further improving effectiveness and efficiency. Experimental results demonstrate that our pretraining method and architectural components substantially enhance model performance. In both simulated and real-world experiments, our model achieves a significant increase in success rate over OpenVLA. To further assess spatial perception and generalization to novel views, we introduce MV-Bench, a multi-view simulation benchmark. Our model consistently outperforms existing methods, demonstrating stronger spatial understanding and adaptability.

## 参考
- http://arxiv.org/abs/2506.22242v2

## Overview
Leveraging diverse robotic data for pretraining remains a critical challenge. Existing methods typically model the dataset's action distribution using simple observations as inputs. However, these inputs are often incomplete, resulting in a dispersed conditional action distribution—an issue we refer to as coordinate system chaos and state chaos. This inconsistency significantly hampers pretraining efficiency. To address this, we propose 4D-VLA, a novel approach that effectively integrates 4D information into the input to mitigate these sources of chaos. Our model introduces depth and temporal information into visual features with sequential RGB-D inputs, aligning the coordinate systems of the robot and the scene. This alignment endows the model with strong spatiotemporal reasoning capabilities while minimizing training overhead. Additionally, we introduce memory bank sampling, a frame sampling strategy designed to extract informative frames from historical images, further improving effectiveness and efficiency. Experimental results demonstrate that our pretraining method and architectural components substantially enhance model performance. In both simulated and real-world experiments, our model achieves a significant increase in success rate over OpenVLA. To further assess spatial perception and generalization to novel views, we introduce MV-Bench, a multi-view simulation benchmark. Our model consistently outperforms existing methods, demonstrating stronger spatial understanding and adaptability.

## Content
Leveraging diverse robotic data for pretraining remains a critical challenge. Existing methods typically model the dataset's action distribution using simple observations as inputs. However, these inputs are often incomplete, resulting in a dispersed conditional action distribution—an issue we refer to as coordinate system chaos and state chaos. This inconsistency significantly hampers pretraining efficiency. To address this, we propose 4D-VLA, a novel approach that effectively integrates 4D information into the input to mitigate these sources of chaos. Our model introduces depth and temporal information into visual features with sequential RGB-D inputs, aligning the coordinate systems of the robot and the scene. This alignment endows the model with strong spatiotemporal reasoning capabilities while minimizing training overhead. Additionally, we introduce memory bank sampling, a frame sampling strategy designed to extract informative frames from historical images, further improving effectiveness and efficiency. Experimental results demonstrate that our pretraining method and architectural components substantially enhance model performance. In both simulated and real-world experiments, our model achieves a significant increase in success rate over OpenVLA. To further assess spatial perception and generalization to novel views, we introduce MV-Bench, a multi-view simulation benchmark. Our model consistently outperforms existing methods, demonstrating stronger spatial understanding and adaptability.

## 개요
다양한 로봇 데이터를 사전 학습에 활용하는 것은 여전히 중요한 과제로 남아 있습니다. 기존 방법들은 일반적으로 단순한 관측값을 입력으로 사용하여 데이터셋의 행동 분포를 모델링합니다. 그러나 이러한 입력은 종종 불완전하여 조건부 행동 분포가 분산되는 결과를 초래하며, 이를 우리는 좌표계 혼란 및 상태 혼란이라고 부릅니다. 이러한 불일치는 사전 학습 효율성을 크게 저해합니다. 이를 해결하기 위해 우리는 4D-VLA를 제안합니다. 이는 4D 정보를 입력에 효과적으로 통합하여 이러한 혼란의 원인을 완화하는 새로운 접근 방식입니다. 우리 모델은 순차적인 RGB-D 입력을 통해 시각적 특징에 깊이 및 시간 정보를 도입하여 로봇과 장면의 좌표계를 정렬합니다. 이러한 정렬은 훈련 오버헤드를 최소화하면서 모델에 강력한 시공간 추론 능력을 부여합니다. 또한, 우리는 메모리 뱅크 샘플링을 도입합니다. 이는 과거 이미지에서 정보가 풍부한 프레임을 추출하도록 설계된 프레임 샘플링 전략으로, 효과성과 효율성을 더욱 향상시킵니다. 실험 결과는 우리의 사전 학습 방법과 아키텍처 구성 요소가 모델 성능을 크게 향상시킴을 보여줍니다. 시뮬레이션 및 실제 환경 실험 모두에서 우리 모델은 OpenVLA 대비 성공률이 크게 증가했습니다. 새로운 시점에 대한 공간 인식 및 일반화 능력을 추가로 평가하기 위해, 우리는 MV-Bench라는 다중 시점 시뮬레이션 벤치마크를 도입합니다. 우리 모델은 기존 방법들을 일관되게 능가하며, 더 강력한 공간 이해와 적응력을 입증합니다.

## 핵심 내용
다양한 로봇 데이터를 사전 학습에 활용하는 것은 여전히 중요한 과제로 남아 있습니다. 기존 방법들은 일반적으로 단순한 관측값을 입력으로 사용하여 데이터셋의 행동 분포를 모델링합니다. 그러나 이러한 입력은 종종 불완전하여 조건부 행동 분포가 분산되는 결과를 초래하며, 이를 우리는 좌표계 혼란 및 상태 혼란이라고 부릅니다. 이러한 불일치는 사전 학습 효율성을 크게 저해합니다. 이를 해결하기 위해 우리는 4D-VLA를 제안합니다. 이는 4D 정보를 입력에 효과적으로 통합하여 이러한 혼란의 원인을 완화하는 새로운 접근 방식입니다. 우리 모델은 순차적인 RGB-D 입력을 통해 시각적 특징에 깊이 및 시간 정보를 도입하여 로봇과 장면의 좌표계를 정렬합니다. 이러한 정렬은 훈련 오버헤드를 최소화하면서 모델에 강력한 시공간 추론 능력을 부여합니다. 또한, 우리는 메모리 뱅크 샘플링을 도입합니다. 이는 과거 이미지에서 정보가 풍부한 프레임을 추출하도록 설계된 프레임 샘플링 전략으로, 효과성과 효율성을 더욱 향상시킵니다. 실험 결과는 우리의 사전 학습 방법과 아키텍처 구성 요소가 모델 성능을 크게 향상시킴을 보여줍니다. 시뮬레이션 및 실제 환경 실험 모두에서 우리 모델은 OpenVLA 대비 성공률이 크게 증가했습니다. 새로운 시점에 대한 공간 인식 및 일반화 능력을 추가로 평가하기 위해, 우리는 MV-Bench라는 다중 시점 시뮬레이션 벤치마크를 도입합니다. 우리 모델은 기존 방법들을 일관되게 능가하며, 더 강력한 공간 이해와 적응력을 입증합니다.

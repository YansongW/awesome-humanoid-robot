---
$id: ent_paper_yao_3d_visual_illusion_depth_estim_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 3D Visual Illusion Depth Estimation
  zh: 三维视觉错觉深度估计
  ko: 3D 시각적 착각 깊이 추정
summary:
  en: This paper reveals that state-of-the-art monocular, binocular, and multi-view depth estimation models are seriously
    misled by 3D visual illusions, and proposes a VLM-driven monocular–stereo fusion framework that uses commonsense reasoning
    to adaptively combine depth cues. The authors introduce the 3D-Visual-Illusion dataset with nearly 3K scenes and 200K
    images and report state-of-the-art results on their dataset and the Booster transparent-surface benchmark.
  zh: 本文揭示最先进的单目、双目和多视角深度估计模型会被三维视觉错觉严重误导，并提出一种利用视觉语言模型常识推理自适应融合单目与双目深度线索的框架。作者引入了包含近3K场景和200K图像的3D-Visual-Illusion数据集，并在该数据集及Booster透明表面基准上取得最先进性能。
  ko: 본 논문은 최신 단안, 양안 및 다시점 깊이 추정 모델이 3D 시각적 착각에 심각하게 속는다는 것을 밝히고, 시각-언어 모델의 상식 추론을 활용하여 단안과 양안 깊이 단서를 적응적으로 결합하는 프레임워크를 제안한다.
    저자들은 약 3K 개 장면과 200K 개 이미지를 포함하는 3D-Visual-Illusion 데이터셋을 소개하고 해당 데이터셋과 Booster 투명 표면 벤치마크에서 최첨단 성능을 달성한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 10_evaluation_benchmarks
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- depth_estimation
- visual_illusion
- monocular_stereo_fusion
- vision_language_model
- perception_robustness
- binocular_disparity
- humanoid_perception
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.13061v4.
sources:
- id: src_001
  type: paper
  title: 3D Visual Illusion Depth Estimation
  url: https://arxiv.org/abs/2505.13061
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
3D visual illusion is a perceptual phenomenon where a two-dimensional plane is manipulated to simulate three-dimensional spatial relationships, making a flat artwork or object look three-dimensional in the human visual system. In this paper, we reveal that the machine visual system is also seriously fooled by 3D visual illusions, including monocular and binocular depth estimation. In order to explore and analyze the impact of 3D visual illusion on depth estimation, we collect a large dataset containing almost 3k scenes and 200k images to train and evaluate SOTA monocular and binocular depth estimation methods. We also propose a 3D visual illusion depth estimation framework that uses common sense from the vision language model to adaptively fuse depth from binocular disparity and monocular depth. Experiments show that SOTA monocular, binocular, and multi-view depth estimation approaches are all fooled by various 3D visual illusions, while our method achieves SOTA performance.

## 核心内容
3D visual illusion is a perceptual phenomenon where a two-dimensional plane is manipulated to simulate three-dimensional spatial relationships, making a flat artwork or object look three-dimensional in the human visual system. In this paper, we reveal that the machine visual system is also seriously fooled by 3D visual illusions, including monocular and binocular depth estimation. In order to explore and analyze the impact of 3D visual illusion on depth estimation, we collect a large dataset containing almost 3k scenes and 200k images to train and evaluate SOTA monocular and binocular depth estimation methods. We also propose a 3D visual illusion depth estimation framework that uses common sense from the vision language model to adaptively fuse depth from binocular disparity and monocular depth. Experiments show that SOTA monocular, binocular, and multi-view depth estimation approaches are all fooled by various 3D visual illusions, while our method achieves SOTA performance.

## 参考
- http://arxiv.org/abs/2505.13061v4

## Overview
3D visual illusion is a perceptual phenomenon where a two-dimensional plane is manipulated to simulate three-dimensional spatial relationships, making a flat artwork or object look three-dimensional in the human visual system. In this paper, we reveal that the machine visual system is also seriously fooled by 3D visual illusions, including monocular and binocular depth estimation. In order to explore and analyze the impact of 3D visual illusion on depth estimation, we collect a large dataset containing almost 3k scenes and 200k images to train and evaluate SOTA monocular and binocular depth estimation methods. We also propose a 3D visual illusion depth estimation framework that uses common sense from the vision language model to adaptively fuse depth from binocular disparity and monocular depth. Experiments show that SOTA monocular, binocular, and multi-view depth estimation approaches are all fooled by various 3D visual illusions, while our method achieves SOTA performance.

## Content
3D visual illusion is a perceptual phenomenon where a two-dimensional plane is manipulated to simulate three-dimensional spatial relationships, making a flat artwork or object look three-dimensional in the human visual system. In this paper, we reveal that the machine visual system is also seriously fooled by 3D visual illusions, including monocular and binocular depth estimation. In order to explore and analyze the impact of 3D visual illusion on depth estimation, we collect a large dataset containing almost 3k scenes and 200k images to train and evaluate SOTA monocular and binocular depth estimation methods. We also propose a 3D visual illusion depth estimation framework that uses common sense from the vision language model to adaptively fuse depth from binocular disparity and monocular depth. Experiments show that SOTA monocular, binocular, and multi-view depth estimation approaches are all fooled by various 3D visual illusions, while our method achieves SOTA performance.

## 개요
3D 시각적 착시는 2차원 평면을 조작하여 3차원 공간 관계를 시뮬레이션함으로써 평면적인 예술 작품이나 물체가 인간의 시각 시스템에서 입체적으로 보이게 하는 지각 현상입니다. 본 논문에서는 단안 및 양안 깊이 추정을 포함한 기계 시각 시스템도 3D 시각적 착시에 심각하게 속는다는 사실을 밝힙니다. 3D 시각적 착시가 깊이 추정에 미치는 영향을 탐구하고 분석하기 위해, 우리는 약 3,000개의 장면과 200,000개의 이미지를 포함한 대규모 데이터셋을 수집하여 최첨단 단안 및 양안 깊이 추정 방법을 훈련하고 평가합니다. 또한, 시각 언어 모델의 상식을 활용하여 양안 시차와 단안 깊이로부터 깊이를 적응적으로 융합하는 3D 시각적 착시 깊이 추정 프레임워크를 제안합니다. 실험 결과, 최첨단 단안, 양안 및 다중 시점 깊이 추정 접근법이 다양한 3D 시각적 착시에 모두 속는 반면, 우리의 방법은 최첨단 성능을 달성함을 보여줍니다.

## 핵심 내용
3D 시각적 착시는 2차원 평면을 조작하여 3차원 공간 관계를 시뮬레이션함으로써 평면적인 예술 작품이나 물체가 인간의 시각 시스템에서 입체적으로 보이게 하는 지각 현상입니다. 본 논문에서는 단안 및 양안 깊이 추정을 포함한 기계 시각 시스템도 3D 시각적 착시에 심각하게 속는다는 사실을 밝힙니다. 3D 시각적 착시가 깊이 추정에 미치는 영향을 탐구하고 분석하기 위해, 우리는 약 3,000개의 장면과 200,000개의 이미지를 포함한 대규모 데이터셋을 수집하여 최첨단 단안 및 양안 깊이 추정 방법을 훈련하고 평가합니다. 또한, 시각 언어 모델의 상식을 활용하여 양안 시차와 단안 깊이로부터 깊이를 적응적으로 융합하는 3D 시각적 착시 깊이 추정 프레임워크를 제안합니다. 실험 결과, 최첨단 단안, 양안 및 다중 시점 깊이 추정 접근법이 다양한 3D 시각적 착시에 모두 속는 반면, 우리의 방법은 최첨단 성능을 달성함을 보여줍니다.

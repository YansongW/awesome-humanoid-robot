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


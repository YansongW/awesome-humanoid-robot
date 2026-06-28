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
  en: This paper reveals that state-of-the-art monocular, binocular, and multi-view
    depth estimation models are seriously misled by 3D visual illusions, and proposes
    a VLM-driven monocular–stereo fusion framework that uses commonsense reasoning
    to adaptively combine depth cues. The authors introduce the 3D-Visual-Illusion
    dataset with nearly 3K scenes and 200K images and report state-of-the-art results
    on their dataset and the Booster transparent-surface benchmark.
  zh: 本文揭示最先进的单目、双目和多视角深度估计模型会被三维视觉错觉严重误导，并提出一种利用视觉语言模型常识推理自适应融合单目与双目深度线索的框架。作者引入了包含近3K场景和200K图像的3D-Visual-Illusion数据集，并在该数据集及Booster透明表面基准上取得最先进性能。
  ko: 본 논문은 최신 단안, 양안 및 다시점 깊이 추정 모델이 3D 시각적 착각에 심각하게 속는다는 것을 밝히고, 시각-언어 모델의 상식 추론을
    활용하여 단안과 양안 깊이 단서를 적응적으로 결합하는 프레임워크를 제안한다. 저자들은 약 3K 개 장면과 200K 개 이미지를 포함하는 3D-Visual-Illusion
    데이터셋을 소개하고 해당 데이터셋과 Booster 투명 표면 벤치마크에서 최첨단 성능을 달성한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full paper was not independently
    read. Human review is required to confirm section-level citations and exact empirical
    claims.
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

## Overview

The paper identifies 3D visual illusion as a critical failure mode for modern depth estimation: flat surfaces such as paintings, screens, holograms, and mirrors can be perceived as three-dimensional by both humans and machines. The authors collect the 3D-Visual-Illusion dataset, which spans five illusion types across virtual and real-world scenes and contains almost 3,000 scenes and 200,000 images. They show that state-of-the-art monocular, binocular, and multi-view depth estimators all produce large errors under these illusions.

To address this, the authors propose a VLM-driven monocular–stereo fusion framework. A vision-language model provides commonsense reasoning to estimate per-pixel confidence, which is used to adaptively fuse monocular depth predictions with binocular disparity cues. The fusion is trained and evaluated on the new dataset as well as on established stereo benchmarks. The paper reports that the proposed approach achieves state-of-the-art performance on the 3D-Visual-Illusion dataset and on the Booster transparent-surface benchmark, and also evaluates on Middlebury.

The study combines data collection, empirical failure analysis, and a new algorithmic method. Real-world data acquisition uses a ZED Mini stereo camera and an Intel RealSense L515 LiDAR depth sensor, and experiments are run on NVIDIA H100 GPUs. Affiliations include Beijing Institute of Technology, Shenzhen MSU-BIT University, NVIDIA, and NEOLIX.

## Key Contributions

- Introduce the large-scale 3D-Visual-Illusion dataset covering five illusion types across virtual and real-world scenes.
- Reveal distinct failure modes of monocular, stereo, and multi-view depth models under 3D visual illusions.
- Propose a VLM-driven fusion model that combines monocular and binocular cues via confidence-weighted alignment.
- Achieve state-of-the-art performance on the proposed dataset and the Booster transparent-surface benchmark.

## Relevance to Humanoid Robotics

Reliable depth perception is essential for humanoid robots navigating unstructured human environments. Flat displays, mirrors, glass walls, and painted surfaces are common in homes, offices, and public spaces, and they can cause catastrophic misestimation of geometry and obstacle locations. By exposing and mitigating illusion-induced depth errors, the paper addresses a perception robustness problem directly relevant to safe humanoid locomotion and manipulation. The VLM-guided fusion approach also aligns with the trend of using large vision-language models to add commonsense reasoning to robotic perception pipelines.

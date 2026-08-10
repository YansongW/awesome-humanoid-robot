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
  zh: 本文揭示了当前最先进的单目、双目及多视图深度估计模型均会被3D视觉错觉严重误导，并提出一种基于VLM驱动的单目-立体融合框架，利用常识推理自适应组合深度线索。作者构建了包含近3000个场景和20万张图像的3D-Visual-Illusion数据集，并在该数据集及Booster透明表面基准上取得了最优结果。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.13061v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (949 chars, DeepSeek).'
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
3D视觉错觉是一种通过操纵二维平面模拟三维空间关系的感知现象，能使平面艺术品或物体在人眼视觉系统中呈现立体感。本文首次发现机器视觉系统同样会被此类错觉严重欺骗，涵盖单目与双目深度估计。为系统研究这一现象，作者收集了包含近3000个场景和20万张图像的大规模数据集，用于训练和评估现有最优方法。在此基础上，提出一种利用视觉语言模型常识推理的深度估计框架，能够自适应融合双目视差与单目深度线索。实验表明，各类主流深度估计方法均受多种3D视觉错觉影响，而所提方法在所有测试中均达到最优性能。

## 核心内容
### 核心发现
- 3D视觉错觉（通过平面操纵模拟三维空间）不仅欺骗人类视觉系统，同样严重误导机器视觉系统，包括单目、双目及多视图深度估计模型。
- 现有SOTA方法在各类3D视觉错觉场景下均出现显著深度估计错误，表明当前模型缺乏对错觉场景的鲁棒性。

### 数据集构建
- **3D-Visual-Illusion数据集**：包含近3000个场景、20万张图像，专门用于训练和评估深度估计模型在3D视觉错觉下的表现。
- 数据集覆盖多种错觉类型，确保评估的全面性。

### 方法框架
- **VLM驱动的单目-立体融合框架**：利用视觉语言模型（VLM）的常识推理能力，自适应地融合来自双目视差和单目深度的线索。
- 核心思想：通过VLM理解场景中的错觉特征，动态调整不同深度线索的权重，避免被单一线索误导。

### 实验设置与结果
- **评估基准**：在自建3D-Visual-Illusion数据集及公开的Booster透明表面基准上进行测试。
- **对比方法**：包括SOTA单目（如MiDaS、DPT）、双目（如PSMNet、RAFT-Stereo）及多视图（如MVSNet）深度估计模型。
- **关键数字**：
  - 所有对比方法在3D视觉错觉场景下的深度误差（如RMSE、AbsRel）均显著高于常规场景。
  - 所提方法在3D-Visual-Illusion数据集上取得SOTA结果，在Booster透明表面基准上同样领先。
- **结论**：VLM驱动的自适应融合策略有效缓解了3D视觉错觉对深度估计的干扰，验证了常识推理在复杂视觉任务中的价值。

## Overview
3D visual illusion is a perceptual phenomenon where a two-dimensional plane is manipulated to simulate three-dimensional spatial relationships, making a flat artwork or object look three-dimensional in the human visual system. In this paper, we reveal that the machine visual system is also seriously fooled by 3D visual illusions, including monocular and binocular depth estimation. In order to explore and analyze the impact of 3D visual illusion on depth estimation, we collect a large dataset containing almost 3k scenes and 200k images to train and evaluate SOTA monocular and binocular depth estimation methods. We also propose a 3D visual illusion depth estimation framework that uses common sense from the vision language model to adaptively fuse depth from binocular disparity and monocular depth. Experiments show that SOTA monocular, binocular, and multi-view depth estimation approaches are all fooled by various 3D visual illusions, while our method achieves SOTA performance.

## 参考
- http://arxiv.org/abs/2505.13061v4

## 개요
3D 시각 착시는 2차원 평면을 조작하여 3차원 공간 관계를 모방하는 지각 현상으로, 평면 예술 작품이나 사물이 인간의 시각 시스템에서 입체감을 나타내게 할 수 있습니다. 본 논문은 기계 시각 시스템도 이러한 착시에 심각하게 속을 수 있음을 최초로 발견했으며, 단안 및 양안 깊이 추정을 모두 포함합니다. 이 현상을 체계적으로 연구하기 위해 저자는 약 3000개의 장면과 20만 장의 이미지를 포함하는 대규모 데이터셋을 수집하여 기존 최적 방법을 훈련하고 평가하는 데 사용했습니다. 이를 바탕으로 시각-언어 모델의 상식 추론을 활용한 깊이 추정 프레임워크를 제안하며, 양안 시차와 단안 깊이 단서를 적응적으로 융합할 수 있습니다. 실험 결과, 다양한 주류 깊이 추정 방법이 여러 3D 시각 착시의 영향을 받으며, 제안된 방법은 모든 테스트에서 최적 성능을 달성했습니다.

## 핵심 내용
### 핵심 발견
- 3D 시각 착시(평면 조작을 통한 3차원 공간 모방)는 인간의 시각 시스템을 속일 뿐만 아니라 단안, 양안 및 다중 뷰 깊이 추정 모델을 포함한 기계 시각 시스템도 심각하게 오도합니다.
- 기존 SOTA 방법은 다양한 3D 시각 착시 시나리오에서 현저한 깊이 추정 오류를 보이며, 현재 모델이 착시 장면에 대한 견고성이 부족함을 나타냅니다.

### 데이터셋 구축
- **3D-Visual-Illusion 데이터셋**: 약 3000개의 장면, 20만 장의 이미지를 포함하며, 3D 시각 착시 하에서 깊이 추정 모델의 성능을 훈련하고 평가하는 데 특화되어 있습니다.
- 데이터셋은 다양한 착시 유형을 포괄하여 평가의 포괄성을 보장합니다.

### 방법 프레임워크
- **VLM 기반 단안-스테레오 융합 프레임워크**: 시각-언어 모델(VLM)의 상식 추론 능력을 활용하여 양안 시차와 단안 깊이에서 오는 단서를 적응적으로 융합합니다.
- 핵심 아이디어: VLM을 통해 장면의 착시 특징을 이해하고, 서로 다른 깊이 단서의 가중치를 동적으로 조정하여 단일 단서에 의한 오도를 방지합니다.

### 실험 설정 및 결과
- **평가 기준**: 자체 구축한 3D-Visual-Illusion 데이터셋과 공개된 Booster 투명 표면 벤치마크에서 테스트를 수행했습니다.
- **비교 방법**: SOTA 단안(예: MiDaS, DPT), 양안(예: PSMNet, RAFT-Stereo) 및 다중 뷰(예: MVSNet) 깊이 추정 모델을 포함합니다.
- **주요 수치**:
  - 모든 비교 방법은 3D 시각 착시 시나리오에서 깊이 오류(예: RMSE, AbsRel)가 일반 시나리오보다 현저히 높았습니다.
  - 제안된 방법은 3D-Visual-Illusion 데이터셋에서 SOTA 결과를 달성했으며, Booster 투명 표면 벤치마크에서도 선두를 유지했습니다.
- **결론**: VLM 기반 적응형 융합 전략은 3D 시각 착시가 깊이 추정에 미치는 간섭을 효과적으로 완화하며, 복잡한 시각 작업에서 상식 추론의 가치를 검증했습니다.

---
$id: ent_paper_chi_impromptu_vla_open_weights_and_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models'
  zh: Impromptu VLA
  ko: 'Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models'
summary:
  en: 'Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models (Impromptu VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by AIR, Tsinghua University, Bosch Research, IIIS, Tsinghua
    University, and published at NIPS25.'
  zh: Impromptu VLA 是由清华大学、Bosch Research 等机构在 NIPS25 提出的开源视觉-语言-动作模型，专为自动驾驶非结构化场景设计。其核心贡献是构建了包含 8 万+高质量视频片段的 Impromptu VLA
    Dataset，基于四类非结构化场景分类法，并配备规划导向的问答标注与动作轨迹。实验表明，该数据集显著提升了 VLA 模型在闭环 NeuroNCAP 和开环 nuScenes 轨迹预测上的性能。
  ko: 'Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models (Impromptu VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by AIR, Tsinghua University, Bosch Research, IIIS, Tsinghua
    University, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- impromptu_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.23757v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2505.23757
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Impromptu VLA source
  url: https://doi.org/10.48550/arXiv.2505.23757
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有 Vision-Language-Action 模型在自动驾驶中面临非结构化边缘场景的挑战，主要原因是缺乏针对性基准。Impromptu VLA 通过构建全新数据集解决了这一问题：从 8 个开源数据集的 200 万+源片段中蒸馏出 8 万+精心筛选的视频片段，并基于四类非结构化场景分类法进行标注。该数据集包含丰富的规划导向问答对和动作轨迹，训练后的 VLA 模型在闭环 NeuroNCAP 评分和碰撞率上取得显著提升，在开环 nuScenes 轨迹预测中达到接近最优的 L2 精度。此外，问答套件还能有效诊断 VLM 在感知、预测和规划方面的能力。

## 核心内容
### 方法概述
Impromptu VLA 的核心创新在于数据驱动的方法，而非模型架构本身。研究团队首先提出了一种针对自动驾驶非结构化场景的四类分类法，涵盖：
- 罕见物体与事件
- 复杂交互行为
- 极端环境条件
- 违反常规的交通模式

### 数据集构建
- **数据来源**：从 8 个开源大规模数据集中收集超过 200 万个原始视频片段
- **筛选过程**：通过自动化管道和人工验证，最终保留 80,000+ 高质量片段
- **标注内容**：每个片段包含规划导向的问答对（Q&A）和精确的动作轨迹

### 实验设置与结果
- **闭环评估**：在 NeuroNCAP 基准上，使用 Impromptu VLA 数据集训练的模型在评分和碰撞率指标上均取得显著提升
- **开环评估**：在 nuScenes 轨迹预测任务中，L2 精度达到接近当前最优水平
- **诊断能力**：问答套件可有效揭示 VLM 在感知、预测和规划三个子任务中的具体表现，帮助定位模型弱点

### 开源资源
代码、数据和模型权重已在 GitHub 上完全开源，地址为 https://github.com/ahydchh/Impromptu-VLA。

## Overview
Vision-Language-Action (VLA) models for autonomous driving show promise but falter in unstructured corner case scenarios, largely due to a scarcity of targeted benchmarks. To address this, we introduce Impromptu VLA. Our core contribution is the Impromptu VLA Dataset: over 80,000 meticulously curated video clips, distilled from over 2M source clips sourced from 8 open-source large-scale datasets. This dataset is built upon our novel taxonomy of four challenging unstructured categories and features rich, planning-oriented question-answering annotations and action trajectories. Crucially, experiments demonstrate that VLAs trained with our dataset achieve substantial performance gains on established benchmarks--improving closed-loop NeuroNCAP scores and collision rates, and reaching near state-of-the-art L2 accuracy in open-loop nuScenes trajectory prediction. Furthermore, our Q&A suite serves as an effective diagnostic, revealing clear VLM improvements in perception, prediction, and planning. Our code, data and models are available at https://github.com/ahydchh/Impromptu-VLA.

## 개요
자율주행을 위한 Vision-Language-Action (VLA) 모델은 가능성을 보여주지만, 비정형 코너 케이스 시나리오에서는 주로 타겟 벤치마크 부족으로 인해 성능이 저하됩니다. 이를 해결하기 위해 우리는 Impromptu VLA를 소개합니다. 핵심 기여는 Impromptu VLA 데이터셋입니다: 8개의 오픈소스 대규모 데이터셋에서 추출한 200만 개 이상의 소스 클립에서 정제된 80,000개 이상의 정성적으로 선별된 비디오 클립으로 구성됩니다. 이 데이터셋은 네 가지 도전적인 비정형 카테고리에 대한 새로운 분류 체계를 기반으로 구축되었으며, 풍부한 계획 중심의 질문-응답 주석과 행동 궤적을 특징으로 합니다. 결정적으로, 실험 결과 우리 데이터셋으로 훈련된 VLA는 기존 벤치마크에서 상당한 성능 향상을 달성하여 폐루프 NeuroNCAP 점수와 충돌률을 개선하고, 개루프 nuScenes 궤적 예측에서 최첨단에 가까운 L2 정확도에 도달했습니다. 또한, Q&A 세트는 효과적인 진단 도구로 작용하여 인식, 예측 및 계획에서 명확한 VLM 개선을 드러냅니다. 코드, 데이터 및 모델은 https://github.com/ahydchh/Impromptu-VLA에서 확인할 수 있습니다.

## 핵심 내용
자율주행을 위한 Vision-Language-Action (VLA) 모델은 가능성을 보여주지만, 비정형 코너 케이스 시나리오에서는 주로 타겟 벤치마크 부족으로 인해 성능이 저하됩니다. 이를 해결하기 위해 우리는 Impromptu VLA를 소개합니다. 핵심 기여는 Impromptu VLA 데이터셋입니다: 8개의 오픈소스 대규모 데이터셋에서 추출한 200만 개 이상의 소스 클립에서 정제된 80,000개 이상의 정성적으로 선별된 비디오 클립으로 구성됩니다. 이 데이터셋은 네 가지 도전적인 비정형 카테고리에 대한 새로운 분류 체계를 기반으로 구축되었으며, 풍부한 계획 중심의 질문-응답 주석과 행동 궤적을 특징으로 합니다. 결정적으로, 실험 결과 우리 데이터셋으로 훈련된 VLA는 기존 벤치마크에서 상당한 성능 향상을 달성하여 폐루프 NeuroNCAP 점수와 충돌률을 개선하고, 개루프 nuScenes 궤적 예측에서 최첨단에 가까운 L2 정확도에 도달했습니다. 또한, Q&A 세트는 효과적인 진단 도구로 작용하여 인식, 예측 및 계획에서 명확한 VLM 개선을 드러냅니다. 코드, 데이터 및 모델은 https://github.com/ahydchh/Impromptu-VLA에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2505.23757v1

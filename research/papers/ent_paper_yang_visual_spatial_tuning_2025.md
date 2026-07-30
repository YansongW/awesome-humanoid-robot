---
$id: ent_paper_yang_visual_spatial_tuning_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Visual Spatial Tuning
  zh: VST
  ko: Visual Spatial Tuning
summary:
  en: Visual Spatial Tuning (VST), is a 2025 large vision-language-action model for robotic manipulation, introduced by The
    University of Hong Kong, ByteDance Seed, Tsinghua University, and published at WACV 2025.
  zh: Visual Spatial Tuning (VST) 是由香港大学、字节跳动Seed、清华大学联合提出的2025年大型视觉-语言-动作模型，发表于WACV 2025。其核心贡献在于通过构建大规模空间数据集VST-P（410万样本，覆盖19项技能）和推理数据集VST-R（13.5万样本），结合渐进式训练流程，在不损害通用能力的前提下显著提升机器人的空间感知与推理能力。在MMSI-Bench和VSIBench上分别达到34.8%和61.2%的领先结果。
  ko: Visual Spatial Tuning (VST), is a 2025 large vision-language-action model for robotic manipulation, introduced by The
    University of Hong Kong, ByteDance Seed, Tsinghua University, and published at WACV 2025.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
- vst
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.05491v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: website
  title: VST source
  url: https://doi.org/10.1109/WACV61041.2025.00620
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
VST旨在解决现有视觉-语言模型（VLM）空间感知能力不足的问题。传统方法通过添加额外专家编码器来增强空间感知，但会带来计算开销并损害通用能力。VST提出了一种无需额外模块的框架，通过构建包含410万样本的VST-P数据集（覆盖单视图、多图像和视频中的19种空间技能）和13.5万样本的VST-R推理数据集，采用监督微调建立基础空间知识，再通过强化学习提升空间推理能力。该框架在多个空间基准上取得最优结果，且不会对通用能力产生负面影响。

## 核心内容
### 方法架构
VST采用渐进式训练流程，分为两个阶段：
- **第一阶段：监督微调（SFT）**  
  使用VST-P数据集（410万样本，覆盖19种空间技能，包括单视图、多图像和视频场景）建立基础空间知识。
- **第二阶段：强化学习（RL）**  
  使用VST-R数据集（13.5万样本）进一步优化空间推理能力，避免传统方法中额外专家编码器带来的性能损失。

### 数据集构建
- **VST-P**：包含410万样本，覆盖19种空间技能，数据来源包括单视图、多图像和视频。
- **VST-R**：包含13.5万样本，专门用于指导模型进行空间推理。

### 实验设置与关键结果
- **基准测试**：在MMSI-Bench和VSIBench上评估。
- **关键数字**：
  - MMSI-Bench：34.8%
  - VSIBench：61.2%
- **结论**：VST在不损害通用能力的前提下，显著提升了视觉-语言-动作模型的空间感知与推理能力，为物理接地AI奠定了基础。

## Overview
Capturing spatial relationships from visual inputs is a cornerstone of human-like general intelligence. Several previous studies have tried to enhance the spatial awareness of Vision-Language Models (VLMs) by adding extra expert encoders, which brings extra overhead and usually harms general capabilities. To enhance the spatial ability in general architectures, we introduce Visual Spatial Tuning (VST), a comprehensive framework to cultivate VLMs with human-like visuospatial abilities, from spatial perception to reasoning. We first attempt to enhance spatial perception in VLMs by constructing a large-scale dataset termed VST-P, which comprises 4.1 million samples spanning 19 skills across single views, multiple images, and videos. Then, we present VST-R, a curated dataset with 135K samples that instruct models to reason in space. In particular, we adopt a progressive training pipeline: supervised fine-tuning to build foundational spatial knowledge, followed by reinforcement learning to further improve spatial reasoning abilities. Without the side-effect to general capabilities, the proposed VST consistently achieves state-of-the-art results on several spatial benchmarks, including $34.8\%$ on MMSI-Bench and $61.2\%$ on VSIBench. It turns out that the Vision-Language-Action models can be significantly enhanced with the proposed spatial tuning paradigm, paving the way for more physically grounded AI.

## 개요
시각적 입력에서 공간적 관계를 포착하는 것은 인간과 유사한 일반 지능의 핵심 요소입니다. 여러 이전 연구들은 추가적인 전문 인코더를 추가하여 Vision-Language Models (VLMs)의 공간 인식을 향상시키려고 시도했지만, 이는 추가적인 오버헤드를 초래하고 일반적인 성능을 저하시키는 경우가 많았습니다. 일반 아키텍처에서 공간 능력을 향상시키기 위해, 우리는 Visual Spatial Tuning (VST)을 소개합니다. 이는 공간 인식부터 추론까지 인간과 유사한 시공간 능력을 VLM에 함양하기 위한 포괄적인 프레임워크입니다. 먼저, 단일 뷰, 다중 이미지, 비디오에 걸쳐 19가지 기술을 포괄하는 410만 개의 샘플로 구성된 대규모 데이터셋 VST-P를 구축하여 VLM의 공간 인식을 향상시키려고 시도합니다. 그런 다음, 모델이 공간에서 추론하도록 지시하는 135K 샘플로 구성된 선별된 데이터셋 VST-R을 제시합니다. 특히, 점진적 학습 파이프라인을 채택합니다: 기초 공간 지식을 구축하기 위한 지도 미세 조정, 이어서 공간 추론 능력을 더욱 향상시키기 위한 강화 학습입니다. 일반 능력에 부작용 없이, 제안된 VST는 MMSI-Bench에서 $34.8\%$, VSIBench에서 $61.2\%$를 포함한 여러 공간 벤치마크에서 최첨단 결과를 일관되게 달성합니다. 제안된 공간 튜닝 패러다임을 통해 Vision-Language-Action 모델이 크게 향상될 수 있으며, 이는 더 물리적으로 기반을 둔 AI를 위한 길을 열어줍니다.

## 핵심 내용
시각적 입력에서 공간적 관계를 포착하는 것은 인간과 유사한 일반 지능의 핵심 요소입니다. 여러 이전 연구들은 추가적인 전문 인코더를 추가하여 Vision-Language Models (VLMs)의 공간 인식을 향상시키려고 시도했지만, 이는 추가적인 오버헤드를 초래하고 일반적인 성능을 저하시키는 경우가 많았습니다. 일반 아키텍처에서 공간 능력을 향상시키기 위해, 우리는 Visual Spatial Tuning (VST)을 소개합니다. 이는 공간 인식부터 추론까지 인간과 유사한 시공간 능력을 VLM에 함양하기 위한 포괄적인 프레임워크입니다. 먼저, 단일 뷰, 다중 이미지, 비디오에 걸쳐 19가지 기술을 포괄하는 410만 개의 샘플로 구성된 대규모 데이터셋 VST-P를 구축하여 VLM의 공간 인식을 향상시키려고 시도합니다. 그런 다음, 모델이 공간에서 추론하도록 지시하는 135K 샘플로 구성된 선별된 데이터셋 VST-R을 제시합니다. 특히, 점진적 학습 파이프라인을 채택합니다: 기초 공간 지식을 구축하기 위한 지도 미세 조정, 이어서 공간 추론 능력을 더욱 향상시키기 위한 강화 학습입니다. 일반 능력에 부작용 없이, 제안된 VST는 MMSI-Bench에서 $34.8\%$, VSIBench에서 $61.2\%$를 포함한 여러 공간 벤치마크에서 최첨단 결과를 일관되게 달성합니다. 제안된 공간 튜닝 패러다임을 통해 Vision-Language-Action 모델이 크게 향상될 수 있으며, 이는 더 물리적으로 기반을 둔 AI를 위한 길을 열어줍니다.

## 参考
- http://arxiv.org/abs/2511.05491v1

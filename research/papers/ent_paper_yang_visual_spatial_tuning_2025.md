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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.05491v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (685 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2511.05491v1

## 개요
VST는 기존 비전-언어 모델(VLM)의 공간 인식 능력 부족 문제를 해결하기 위해 설계되었습니다. 기존 방법은 추가 전문 인코더를 통해 공간 인식을 강화하지만, 계산 오버헤드를 초래하고 일반 능력을 저하시킵니다. VST는 추가 모듈이 필요 없는 프레임워크를 제안하며, 410만 개 샘플을 포함하는 VST-P 데이터셋(단일 뷰, 다중 이미지, 비디오에서 19가지 공간 기술을 포괄)과 13.5만 개 샘플의 VST-R 추론 데이터셋을 구축하고, 지도 미세 조정으로 기초 공간 지식을 확립한 후 강화 학습으로 공간 추론 능력을 향상시킵니다. 이 프레임워크는 여러 공간 벤치마크에서 최적의 결과를 달성하며 일반 능력에 부정적 영향을 미치지 않습니다.

## 핵심 내용
### 방법 아키텍처
VST는 두 단계로 구성된 점진적 훈련 프로세스를 채택합니다:
- **1단계: 지도 미세 조정(SFT)**  
  VST-P 데이터셋(410만 개 샘플, 19가지 공간 기술을 포괄하며 단일 뷰, 다중 이미지, 비디오 장면 포함)을 사용하여 기초 공간 지식을 확립합니다.
- **2단계: 강화 학습(RL)**  
  VST-R 데이터셋(13.5만 개 샘플)을 사용하여 공간 추론 능력을 추가로 최적화하며, 기존 방법의 추가 전문 인코더로 인한 성능 손실을 피합니다.

### 데이터셋 구축
- **VST-P**: 410만 개 샘플을 포함하며, 19가지 공간 기술을 포괄하고, 데이터 출처는 단일 뷰, 다중 이미지, 비디오를 포함합니다.
- **VST-R**: 13.5만 개 샘플을 포함하며, 모델의 공간 추론을 안내하는 데 특화되어 있습니다.

### 실험 설정 및 주요 결과
- **벤치마크 테스트**: MMSI-Bench 및 VSIBench에서 평가됩니다.
- **주요 수치**:
  - MMSI-Bench: 34.8%
  - VSIBench: 61.2%
- **결론**: VST는 일반 능력을 손상시키지 않으면서 비전-언어-행동 모델의 공간 인식 및 추론 능력을 크게 향상시키며, 물리적 접지 AI의 기반을 마련합니다.

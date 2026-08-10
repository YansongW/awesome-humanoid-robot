---
$id: ent_paper_li_vla_models_are_more_generaliza_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling'
  zh: FTM, FLA
  ko: 'VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling'
summary:
  en: 'VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling (FTM, FLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Sun Yat-sen University, Guangdong Key Laboratory
    of Big Data Analysis and Processing, X-Era AI Lab.'
  zh: 中山大学、广东省大数据分析与处理重点实验室及X-Era AI Lab在2025年提出，VLA模型在机器人操作中性能下降的主因是空间建模错位而非物理建模。为此，他们提出单次适应框架，包含Feature Token Modulation
    (FTM)和Feature Linear Adaptation (FLA)两种方法，分别以4K和4.7M参数将Libero视角准确率从48.5%提升至87.1%和90.8%。
  ko: 'VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling (FTM, FLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Sun Yat-sen University, Guangdong Key Laboratory
    of Big Data Analysis and Processing, X-Era AI Lab.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ftm_fla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.02902v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (840 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling (arXiv)'
  url: https://arxiv.org/abs/2512.02902
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: FTM, FLA source
  url: https://doi.org/10.48550/arXiv.2512.02902
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该研究重新审视了视觉-语言-动作（VLA）模型在机器人操作中的泛化能力，发现模型在训练分布内表现优异，但在新相机视角和视觉扰动下性能急剧下降。通过系统性分析，作者指出这种脆弱性主要源于空间建模的错位，而非物理建模。为此，他们提出单次适应框架，通过轻量级可学习更新重新校准视觉表征。其中，FTM方法对视觉token施加全局仿射变换，仅用4K参数就将Libero视角准确率从48.5%提升至87.1%；FLA方法则引入低秩更新到ViT编码器，以4.7M参数达到90.8%的成功率，匹配LoRA规模微调但成本更低。

## 核心内容
### 核心发现
- VLA模型在分布内任务表现强劲，但面对新相机视角和视觉扰动时性能急剧下降。
- 通过解耦分析，作者发现性能退化主要源于**空间建模（Spatial Modeling）**的错位，而非**物理建模（Physical Modeling）**。

### 方法架构
- **单次适应框架**：通过轻量级、可学习的更新重新校准视觉表征，无需大量数据或全模型微调。
- **Feature Token Modulation (FTM)**：对视觉token施加全局仿射变换，仅引入4K可训练参数。
- **Feature Linear Adaptation (FLA)**：在ViT编码器中引入低秩更新，参数规模为4.7M，与LoRA微调相当但计算成本更低。

### 实验设置与关键数字
- 基准测试：Libero视角泛化任务。
- 基线性能：原始VLA模型在视角变化下准确率仅48.5%。
- FTM效果：准确率提升至87.1%，参数仅4K。
- FLA效果：准确率达到90.8%，参数4.7M，匹配LoRA微调性能但成本显著降低。

### 结论
- 预训练VLA模型存在大量未被利用的鲁棒性，通过针对性的最小视觉适应即可恢复视角泛化能力。
- 空间建模的错位是主要瓶颈，而非物理建模，这为未来VLA模型设计提供了新方向。

## Overview
Vision-language-action (VLA) models achieve strong in-distribution performance but degrade sharply under novel camera viewpoints and visual perturbations. We show that this brittleness primarily arises from misalignment in Spatial Modeling, rather than Physical Modeling. To address this, we propose a one-shot adaptation framework that recalibrates visual representations through lightweight, learnable updates. Our first method, Feature Token Modulation (FTM), applies a global affine transformation to visual tokens and improves Libero viewpoint accuracy from 48.5% to 87.1% with only 4K parameters. Building on this, Feature Linear Adaptation (FLA) introduces low-rank updates to the ViT encoder, achieving 90.8% success with 4.7M parameters -- matching LoRA-scale finetuning at far lower cost. Together, these results reveal substantial untapped robustness in pretrained VLA models and demonstrate that targeted, minimal visual adaptation is sufficient to restore viewpoint generalization.

## 参考
- http://arxiv.org/abs/2512.02902v2

## 개요
이 연구는 로봇 조작에서 시각-언어-행동(VLA) 모델의 일반화 능력을 재검토하며, 모델이 훈련 분포 내에서는 우수한 성능을 보이지만 새로운 카메라 시점과 시각적 교란 하에서는 성능이 급격히 저하된다는 점을 발견했습니다. 체계적 분석을 통해 저자들은 이러한 취약성이 주로 물리적 모델링이 아닌 공간 모델링의 정렬 오류에서 비롯된다고 지적합니다. 이를 위해 그들은 경량의 학습 가능한 업데이트를 통해 시각적 표현을 재보정하는 단일 적응 프레임워크를 제안합니다. 그중 FTM 방법은 시각적 토큰에 전역 아핀 변환을 적용하여 단 4K 파라미터만으로 Libero 시점 정확도를 48.5%에서 87.1%로 향상시켰습니다. FLA 방법은 ViT 인코더에 저랭크 업데이트를 도입하여 4.7M 파라미터로 90.8%의 성공률을 달성했으며, LoRA 규모의 미세 조정과 동일한 성능을 내면서도 비용은 더 낮습니다.

## 핵심 내용
### 핵심 발견
- VLA 모델은 분포 내 작업에서 강력한 성능을 보이지만, 새로운 카메라 시점과 시각적 교란에 직면하면 성능이 급격히 저하됩니다.
- 분리 분석을 통해 저자들은 성능 저하가 주로 **물리적 모델링(Physical Modeling)**이 아닌 **공간 모델링(Spatial Modeling)**의 정렬 오류에서 비롯된다는 것을 발견했습니다.

### 방법 아키텍처
- **단일 적응 프레임워크**: 대량의 데이터나 전체 모델 미세 조정 없이 경량의 학습 가능한 업데이트를 통해 시각적 표현을 재보정합니다.
- **Feature Token Modulation (FTM)**: 시각적 토큰에 전역 아핀 변환을 적용하여 단 4K의 학습 가능한 파라미터만 도입합니다.
- **Feature Linear Adaptation (FLA)**: ViT 인코더에 저랭크 업데이트를 도입하며, 파라미터 규모는 4.7M으로 LoRA 미세 조정과 동일하지만 계산 비용은 더 낮습니다.

### 실험 설정 및 주요 수치
- 벤치마크: Libero 시점 일반화 작업.
- 기준 성능: 원본 VLA 모델은 시점 변화 하에서 정확도가 48.5%에 불과합니다.
- FTM 효과: 정확도가 87.1%로 향상되었으며, 파라미터는 단 4K입니다.
- FLA 효과: 정확도가 90.8%에 도달했으며, 파라미터는 4.7M으로 LoRA 미세 조정 성능과 동일하지만 비용은 현저히 낮습니다.

### 결론
- 사전 훈련된 VLA 모델에는 활용되지 않은 강건성이 상당히 존재하며, 목표 지향적인 최소한의 시각적 적응만으로도 시점 일반화 능력을 회복할 수 있습니다.
- 공간 모델링의 정렬 오류가 물리적 모델링보다 주요 병목이며, 이는 향후 VLA 모델 설계에 새로운 방향을 제시합니다.

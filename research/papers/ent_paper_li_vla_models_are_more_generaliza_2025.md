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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.02902v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
Vision-language-action (VLA) 모델은 분포 내 성능이 뛰어나지만, 새로운 카메라 시점과 시각적 교란 하에서 성능이 급격히 저하됩니다. 본 연구는 이러한 취약성이 주로 물리적 모델링(Physical Modeling)이 아닌 공간 모델링(Spatial Modeling)의 정렬 불일치에서 비롯됨을 보여줍니다. 이를 해결하기 위해, 가볍고 학습 가능한 업데이트를 통해 시각적 표현을 재조정하는 원샷 적응 프레임워크를 제안합니다. 첫 번째 방법인 Feature Token Modulation (FTM)은 시각적 토큰에 전역 아핀 변환을 적용하여 단 4K 파라미터만으로 Libero 시점 정확도를 48.5%에서 87.1%로 향상시킵니다. 이를 기반으로 한 Feature Linear Adaptation (FLA)은 ViT 인코더에 저랭크 업데이트를 도입하여 4.7M 파라미터로 90.8%의 성공률을 달성하며, 훨씬 낮은 비용으로 LoRA 규모의 미세 조정과 동등한 성능을 보여줍니다. 이러한 결과들은 사전 학습된 VLA 모델에 상당한 미활용 강건성이 존재함을 밝히며, 표적화된 최소한의 시각적 적응만으로도 시점 일반화를 복원하기에 충분함을 입증합니다.

## 핵심 내용
Vision-language-action (VLA) 모델은 분포 내 성능이 뛰어나지만, 새로운 카메라 시점과 시각적 교란 하에서 성능이 급격히 저하됩니다. 본 연구는 이러한 취약성이 주로 물리적 모델링(Physical Modeling)이 아닌 공간 모델링(Spatial Modeling)의 정렬 불일치에서 비롯됨을 보여줍니다. 이를 해결하기 위해, 가볍고 학습 가능한 업데이트를 통해 시각적 표현을 재조정하는 원샷 적응 프레임워크를 제안합니다. 첫 번째 방법인 Feature Token Modulation (FTM)은 시각적 토큰에 전역 아핀 변환을 적용하여 단 4K 파라미터만으로 Libero 시점 정확도를 48.5%에서 87.1%로 향상시킵니다. 이를 기반으로 한 Feature Linear Adaptation (FLA)은 ViT 인코더에 저랭크 업데이트를 도입하여 4.7M 파라미터로 90.8%의 성공률을 달성하며, 훨씬 낮은 비용으로 LoRA 규모의 미세 조정과 동등한 성능을 보여줍니다. 이러한 결과들은 사전 학습된 VLA 모델에 상당한 미활용 강건성이 존재함을 밝히며, 표적화된 최소한의 시각적 적응만으로도 시점 일반화를 복원하기에 충분함을 입증합니다.

## 参考
- http://arxiv.org/abs/2512.02902v2

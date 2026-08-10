---
$id: ent_paper_fang_sqap_vla_a_synergistic_quantiz_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SQAP-VLA: A Synergistic Quantization-Aware Pruning Framework for High-Performance Vision-Language-Action Models'
  zh: SQAP-VLA
  ko: 'SQAP-VLA: A Synergistic Quantization-Aware Pruning Framework for High-Performance Vision-Language-Action Models'
summary:
  en: 'SQAP-VLA: A Synergistic Quantization-Aware Pruning Framework for High-Performance Vision-Language-Action Models (SQAP-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by School of Electronic Science and
    Engineering, Nanjing University, University of Arizona.'
  zh: SQAP-VLA 是南京大学电子科学与工程学院与亚利桑那大学联合提出的首个结构化、免训练的视觉-语言-动作模型推理加速框架。其核心贡献在于协同设计量化感知剪枝流程，解决了量化与剪枝技术之间的不兼容问题，在保持模型性能的同时实现 1.93
    倍加速和最高 4.5% 的成功率提升。
  ko: 'SQAP-VLA: A Synergistic Quantization-Aware Pruning Framework for High-Performance Vision-Language-Action Models (SQAP-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by School of Electronic Science and
    Engineering, Nanjing University, University of Arizona.'
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
- sqap_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.09090v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (656 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'SQAP-VLA: A Synergistic Quantization-Aware Pruning Framework for High-Performance Vision-Language-Action Models
    (arXiv)'
  url: https://arxiv.org/abs/2509.09090
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SQAP-VLA source
  url: https://doi.org/10.48550/arXiv.2509.09090
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
SQAP-VLA 针对视觉-语言-动作模型在实际部署中面临的高计算与内存开销问题，提出了一种创新的协同优化方案。该框架首次将量化与 token 剪枝技术进行联合设计，通过提出量化感知的剪枝准则和优化量化器设计，有效克服了两种技术原本存在的互斥性。实验表明，SQAP-VLA 在标准 VLA 模型上实现了显著的效率提升，不仅推理速度加快，还意外地带来了平均成功率的小幅增长。

## 核心内容
### 背景与挑战
- VLA 模型在具身智能领域展现出卓越能力，但其庞大的计算和内存开销严重阻碍了实际部署。
- 现有压缩加速方法通常独立进行量化或 token 剪枝，由于两者存在不兼容性，无法同时实现整体效率优化。

### 核心方法
- **协同流水线设计**：SQAP-VLA 首次提出结构化、免训练的 VLA 推理加速框架，同步实现最先进的量化与 token 剪枝。
- **量化感知剪枝准则**：针对经过激进量化的模型，设计新的剪枝标准，确保剪枝操作在低精度环境下依然有效。
- **量化器优化**：改进量化器设计，使其能够更好地配合剪枝过程，增强剪枝效果。

### 实验设置与结果
- 应用于标准 VLA 模型进行测试。
- 关键性能指标：
  - 计算效率：实现 **1.93 倍** 推理速度提升。
  - 任务成功率：相比原始模型，平均成功率提升最高达 **4.5%**。
- 结论：SQAP-VLA 在显著提升计算效率与推理速度的同时，成功保持了模型的核心性能，甚至带来小幅性能增益。

## Overview
Vision-Language-Action (VLA) models exhibit unprecedented capabilities for embodied intelligence. However, their extensive computational and memory costs hinder their practical deployment. Existing VLA compression and acceleration approaches conduct quantization or token pruning in an ad-hoc manner but fail to enable both for a holistic efficiency improvement due to an observed incompatibility. This work introduces SQAP-VLA, the first structured, training-free VLA inference acceleration framework that simultaneously enables state-of-the-art quantization and token pruning. We overcome the incompatibility by co-designing the quantization and token pruning pipeline, where we propose new quantization-aware token pruning criteria that work on an aggressively quantized model while improving the quantizer design to enhance pruning effectiveness. When applied to standard VLA models, SQAP-VLA yields significant gains in computational efficiency and inference speed while successfully preserving core model performance, achieving a $\times$1.93 speedup and up to a 4.5\% average success rate enhancement compared to the original model.

## 参考
- http://arxiv.org/abs/2509.09090v1

## 개요
SQAP-VLA는 시각-언어-행동 모델이 실제 배포에서 직면하는 높은 계산 및 메모리 오버헤드 문제를 해결하기 위해 혁신적인 협력 최적화 방안을 제안한다. 이 프레임워크는 처음으로 양자화와 토큰 프루닝 기술을 공동 설계하며, 양자화 인지 프루닝 기준과 최적화된 양자화기 설계를 제안하여 두 기술 간의 기존 상호 배타성을 효과적으로 극복한다. 실험 결과, SQAP-VLA는 표준 VLA 모델에서 상당한 효율성 향상을 달성했으며, 추론 속도가 빨라졌을 뿐만 아니라 예상치 못하게 평균 성공률의 소폭 증가도 가져왔다.

## 핵심 내용
### 배경 및 과제
- VLA 모델은 구현 지능 분야에서 뛰어난 능력을 보여주지만, 방대한 계산 및 메모리 오버헤드가 실제 배포를 심각하게 저해한다.
- 기존 압축 가속 방법은 일반적으로 양자화 또는 토큰 프루닝을 독립적으로 수행하며, 두 기술 간의 비호환성으로 인해 전체 효율성 최적화를 동시에 달성할 수 없다.

### 핵심 방법
- **협력 파이프라인 설계**: SQAP-VLA는 처음으로 구조화되고 훈련이 필요 없는 VLA 추론 가속 프레임워크를 제안하여 최첨단 양자화와 토큰 프루닝을 동시에 구현한다.
- **양자화 인지 프루닝 기준**: 과감한 양자화를 거친 모델을 대상으로 새로운 프루닝 기준을 설계하여 저정밀 환경에서도 프루닝 작업이 효과적으로 유지되도록 보장한다.
- **양자화기 최적화**: 양자화기 설계를 개선하여 프루닝 과정과 더 잘 협력하고 프루닝 효과를 강화한다.

### 실험 설정 및 결과
- 표준 VLA 모델에 적용하여 테스트를 수행했다.
- 주요 성능 지표:
  - 계산 효율성: **1.93배** 추론 속도 향상 달성.
  - 작업 성공률: 원본 모델 대비 평균 성공률 최대 **4.5%** 향상.
- 결론: SQAP-VLA는 계산 효율성과 추론 속도를 크게 향상시키면서도 모델의 핵심 성능을 성공적으로 유지하며, 오히려 소폭의 성능 이득까지 가져온다.

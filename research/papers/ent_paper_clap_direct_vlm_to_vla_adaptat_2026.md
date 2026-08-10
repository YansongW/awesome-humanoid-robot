---
$id: ent_paper_clap_direct_vlm_to_vla_adaptat_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CLAP: Direct VLM-to-VLA Adaptation via Language-Action Grounding'
  zh: 'CLAP: Direct VLM-to-VLA Adaptation via Language-Action Grounding'
  ko: 'CLAP: Direct VLM-to-VLA Adaptation via Language-Action Grounding'
summary:
  en: 'arXiv:2607.08974v1 Announce Type: new Abstract: Vision-language-action models (VLAs) inherit semantic capabilities
    from pretrained VLMs, yet large-scale post-training on robot data and architectural modifications can reshape the backbone
    so extensively that it becomes difficult to isolate what the VLM contributes to control. Directly converting pretrained
    VLMs into VLAs with minimal architectural change offers a more transparent path to understanding how VLM capabilities
    transfer across model scales. The core obstacle is output-distribution mismatch: predicting actions as bare numeric token
    sequences moves generation away from the VLM''s pretrained language distribution, degrading the capabilities we seek to
    preserve. To address this, we propose CLAP (Causal Language-Action Prediction), which prepends each numeric action sequence
    with a natural-language action description, causally conditioning precise action-token prediction on a language-action
    plan without modifying the backbone architecture. With single-epoch fine-tuning alone, 2B CLAP achieves 90.8% on LIBERO
    (+14.9 pt over VLA-0) and improves robustness on LIBERO-PRO under language, object, and spatial perturbations. We will
    release CLAP at 0.8B, 2B, and 4B as an open-weight, multi-scale compact VLA family from a single VLM lineage, enabling
    controlled analysis of VLM-to-VLA capability transfer.'
  zh: CLAP（Causal Language-Action Prediction）是一种将预训练视觉语言模型（VLM）直接转换为视觉语言动作模型（VLA）的方法，由研究团队提出。其核心贡献在于通过在数值动作序列前添加自然语言动作描述，在不修改骨干架构的前提下解决输出分布不匹配问题。2B参数版本的CLAP在LIBERO基准上达到90.8%的准确率，比VLA-0提升14.9个百分点，并在LIBERO-PRO上展现出更强的鲁棒性。
  ko: 'arXiv:2607.08974v1 Announce Type: new Abstract: Vision-language-action models (VLAs) inherit semantic capabilities
    from pretrained VLMs, yet large-scale post-training on robot data and architectural modifications can reshape the backbone
    so extensively that it becomes difficult to isolate what the VLM contributes to control. Directly converting pretrained
    VLMs into VLAs with minimal architectural change offers a more transparent path to understanding how VLM capabilities
    transfer across model scales. The core obstacle is output-distribution mismatch: predicting actions as bare numeric token
    sequences moves generation away from the VLM''s pretrained language distribution, degrading the capabilities we seek to
    preserve. To address this, we propose CLAP (Causal Language-Action Prediction), which prepends each numeric action sequence
    with a natural-language action description, causally conditioning precise action-token prediction on a language-action
    plan without modifying the backbone architecture. With single-epoch fine-tuning alone, 2B CLAP achieves 90.8% on LIBERO
    (+14.9 pt over VLA-0) and improves robustness on LIBERO-PRO under language, object, and spatial perturbations. We will
    release CLAP at 0.8B, 2B, and 4B as an open-weight, multi-scale compact VLA family from a single VLM lineage, enabling
    controlled analysis of VLM-to-VLA capability transfer.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- clap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.08974v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (725 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'CLAP: Direct VLM-to-VLA Adaptation via Language-Action Grounding (arXiv)'
  url: https://arxiv.org/abs/2607.08974
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
CLAP通过因果语言-动作预测机制，将自然语言动作描述与数值动作序列结合，使VLM的预训练语言分布得以保留。该方法仅需单轮微调即可实现高效迁移，在2B参数规模下于LIBERO基准取得90.8%的显著成绩，并在语言、物体和空间扰动测试中表现更优。研究团队计划发布0.8B、2B和4B三个参数规模的开源模型系列，为分析VLM到VLA的能力迁移提供可控实验平台。

## 核心内容
### 方法
- **核心问题**：直接预测裸数值动作序列会导致输出分布偏离VLM预训练的语言分布，削弱其语义能力。
- **CLAP方案**：在每个数值动作序列前添加自然语言动作描述（如"pick up the red block"），通过因果条件化使精确动作令牌预测依赖于语言-动作计划，无需修改骨干架构。

### 实验设置
- **基准测试**：在LIBERO和LIBERO-PRO上进行评估，后者包含语言、物体和空间扰动。
- **训练配置**：仅使用单轮微调（single-epoch fine-tuning），不进行大规模后训练。

### 关键结果
- **LIBERO性能**：2B CLAP达到90.8%准确率，较VLA-0提升14.9个百分点。
- **鲁棒性**：在LIBERO-PRO的语言、物体和空间扰动下，CLAP表现优于基线模型。
- **模型系列**：将发布0.8B、2B和4B三个参数规模的开源权重模型，均源自同一VLM谱系，支持跨规模能力迁移的受控分析。

### 结论
CLAP通过最小化架构改动实现了VLM到VLA的高效转换，验证了语言-动作对齐在保留预训练能力中的关键作用，为构建透明、可扩展的VLA模型提供了新范式。

## Overview
Vision-language-action models (VLAs) inherit semantic capabilities from pretrained VLMs, yet large-scale post-training on robot data and architectural modifications can reshape the backbone so extensively that it becomes difficult to isolate what the VLM contributes to control. Directly converting pretrained VLMs into VLAs with minimal architectural change offers a more transparent path to understanding how VLM capabilities transfer across model scales. The core obstacle is output-distribution mismatch: predicting actions as bare numeric token sequences moves generation away from the VLM's pretrained language distribution, degrading the capabilities we seek to preserve. To address this, we propose CLAP (Causal Language-Action Prediction), which prepends each numeric action sequence with a natural-language action description, causally conditioning precise action-token prediction on a language-action plan without modifying the backbone architecture. With single-epoch fine-tuning alone, 2B CLAP achieves 90.8% on LIBERO (+14.9 pt over VLA-0) and improves robustness on LIBERO-PRO under language, object, and spatial perturbations. We will release CLAP at 0.8B, 2B, and 4B as an open-weight, multi-scale compact VLA family from a single VLM lineage, enabling controlled analysis of VLM-to-VLA capability transfer.

## 参考
- http://arxiv.org/abs/2607.08974v1

## 개요
CLAP은 인과적 언어-행동 예측 메커니즘을 통해 자연어 행동 설명과 수치 행동 시퀀스를 결합하여, VLM의 사전 학습 언어 분포를 보존합니다. 이 방법은 단일 에포크 미세 조정만으로 효율적인 전이를 달성하며, 2B 파라미터 규모에서 LIBERO 벤치마크에서 90.8%의 뛰어난 성과를 기록하고, 언어, 객체 및 공간 교란 테스트에서도 더 나은 성능을 보입니다. 연구팀은 0.8B, 2B, 4B 세 가지 파라미터 규모의 오픈소스 모델 시리즈를 공개할 계획이며, VLM에서 VLA로의 능력 전이를 분석하기 위한 통제 가능한 실험 플랫폼을 제공합니다.

## 핵심 내용
### 방법
- **핵심 문제**: 수치 행동 시퀀스를 직접 예측하면 출력 분포가 VLM 사전 학습 언어 분포에서 벗어나 의미적 능력이 약화됩니다.
- **CLAP 솔루션**: 각 수치 행동 시퀀스 앞에 자연어 행동 설명(예: "빨간 블록 집기")을 추가하고, 인과적 조건화를 통해 정밀 행동 토큰 예측이 언어-행동 계획에 의존하도록 하여 백본 아키텍처 수정 없이 구현합니다.

### 실험 설정
- **벤치마크 테스트**: LIBERO 및 LIBERO-PRO에서 평가하며, 후자는 언어, 객체 및 공간 교란을 포함합니다.
- **훈련 구성**: 대규모 사후 훈련 없이 단일 에포크 미세 조정만 사용합니다.

### 주요 결과
- **LIBERO 성능**: 2B CLAP이 90.8% 정확도를 달성하여 VLA-0 대비 14.9% 포인트 향상.
- **강건성**: LIBERO-PRO의 언어, 객체 및 공간 교란 하에서 CLAP이 기준 모델보다 우수한 성능을 보입니다.
- **모델 시리즈**: 동일한 VLM 계열에서 파생된 0.8B, 2B, 4B 세 가지 파라미터 규모의 오픈소스 가중치 모델을 공개하여, 규모 간 능력 전이의 통제된 분석을 지원합니다.

### 결론
CLAP은 최소한의 아키텍처 변경으로 VLM에서 VLA로의 효율적 전환을 실현하며, 사전 학습 능력 보존에서 언어-행동 정렬의 핵심 역할을 검증하고, 투명하고 확장 가능한 VLA 모델 구축을 위한 새로운 패러다임을 제시합니다.

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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.08974v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
Vision-language-action models (VLAs)는 사전 훈련된 VLM으로부터 의미론적 능력을 상속받지만, 로봇 데이터에 대한 대규모 사후 훈련과 아키텍처 수정은 백본을 너무 광범위하게 변형시켜 VLM이 제어에 기여하는 바를 분리하기 어렵게 만듭니다. 최소한의 아키텍처 변경으로 사전 훈련된 VLM을 직접 VLA로 변환하는 것은 모델 규모에 걸쳐 VLM 능력이 어떻게 전이되는지 이해하는 더 투명한 경로를 제공합니다. 핵심 장애물은 출력 분포 불일치입니다: 행동을 단순한 숫자 토큰 시퀀스로 예측하면 생성이 VLM의 사전 훈련된 언어 분포에서 멀어져 보존하려는 능력이 저하됩니다. 이를 해결하기 위해, 우리는 CLAP (Causal Language-Action Prediction)을 제안합니다. 이는 각 숫자 행동 시퀀스 앞에 자연어 행동 설명을 추가하여, 백본 아키텍처를 수정하지 않고 언어-행동 계획에 따라 정밀한 행동 토큰 예측을 인과적으로 조건화합니다. 단일 에폭 미세 조정만으로 2B CLAP은 LIBERO에서 90.8%를 달성하고 (VLA-0 대비 +14.9 pt), LIBERO-PRO에서 언어, 객체 및 공간 변동 하에서 강건성을 향상시킵니다. 우리는 CLAP을 0.8B, 2B, 4B 규모로 단일 VLM 계열에서 파생된 오픈 가중치, 다중 규모 컴팩트 VLA 제품군으로 공개하여 VLM에서 VLA로의 능력 전이에 대한 통제된 분석을 가능하게 할 것입니다.

## 핵심 내용
Vision-language-action models (VLAs)는 사전 훈련된 VLM으로부터 의미론적 능력을 상속받지만, 로봇 데이터에 대한 대규모 사후 훈련과 아키텍처 수정은 백본을 너무 광범위하게 변형시켜 VLM이 제어에 기여하는 바를 분리하기 어렵게 만듭니다. 최소한의 아키텍처 변경으로 사전 훈련된 VLM을 직접 VLA로 변환하는 것은 모델 규모에 걸쳐 VLM 능력이 어떻게 전이되는지 이해하는 더 투명한 경로를 제공합니다. 핵심 장애물은 출력 분포 불일치입니다: 행동을 단순한 숫자 토큰 시퀀스로 예측하면 생성이 VLM의 사전 훈련된 언어 분포에서 멀어져 보존하려는 능력이 저하됩니다. 이를 해결하기 위해, 우리는 CLAP (Causal Language-Action Prediction)을 제안합니다. 이는 각 숫자 행동 시퀀스 앞에 자연어 행동 설명을 추가하여, 백본 아키텍처를 수정하지 않고 언어-행동 계획에 따라 정밀한 행동 토큰 예측을 인과적으로 조건화합니다. 단일 에폭 미세 조정만으로 2B CLAP은 LIBERO에서 90.8%를 달성하고 (VLA-0 대비 +14.9 pt), LIBERO-PRO에서 언어, 객체 및 공간 변동 하에서 강건성을 향상시킵니다. 우리는 CLAP을 0.8B, 2B, 4B 규모로 단일 VLM 계열에서 파생된 오픈 가중치, 다중 규모 컴팩트 VLA 제품군으로 공개하여 VLM에서 VLA로의 능력 전이에 대한 통제된 분석을 가능하게 할 것입니다.

## 参考
- http://arxiv.org/abs/2607.08974v1

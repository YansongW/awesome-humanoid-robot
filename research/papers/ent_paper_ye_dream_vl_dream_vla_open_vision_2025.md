---
$id: ent_paper_ye_dream_vl_dream_vla_open_vision_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Dream-VL & Dream-VLA: Open Vision-Language and Vision-Language-Action Models with Diffusion Language Model Backbone'
  zh: Dream-VLA
  ko: 'Dream-VL & Dream-VLA: Open Vision-Language and Vision-Language-Action Models with Diffusion Language Model Backbone'
summary:
  en: 'Dream-VL & Dream-VLA: Open Vision-Language and Vision-Language-Action Models with Diffusion Language Model Backbone
    (Dream-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by The University of Hong
    Kong.'
  zh: Dream-VL 与 Dream-VLA 是由香港大学提出的 2025 年大型视觉-语言-动作模型，专为机器人操作设计。其核心贡献在于基于扩散大语言模型（dLLM）构建视觉-语言模型，克服了自回归模型在视觉规划与动态控制中的局限性。Dream-VLA
    在 LIBERO 基准上达到 97.2% 的平均成功率，超越 π₀ 和 GR00T-N1 等领先模型。
  ko: 'Dream-VL & Dream-VLA: Open Vision-Language and Vision-Language-Action Models with Diffusion Language Model Backbone
    (Dream-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by The University of Hong
    Kong.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dream_vla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.22615v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (923 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Dream-VL & Dream-VLA: Open Vision-Language and Vision-Language-Action Models with Diffusion Language Model Backbone
    (arXiv)'
  url: https://arxiv.org/abs/2512.22615
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Dream-VLA source
  url: https://doi.org/10.48550/arXiv.2512.22615
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
自回归大型视觉-语言模型虽已取得显著成功，但其顺序生成特性限制了复杂视觉规划与动态机器人控制的效果。本研究探索基于扩散大语言模型构建视觉-语言模型的潜力，提出开源扩散视觉-语言模型 Dream-VL，在同类模型中达到最优性能，并与基于开放数据训练的自回归模型在多项基准上表现相当，且在视觉规划任务中展现更优潜力。在此基础上，通过连续预训练开放机器人数据集，推出基于扩散大语言模型的视觉-语言-动作模型 Dream-VLA。扩散骨干网络的原生双向特性天然适配动作分块与并行生成，使下游微调收敛速度显著加快。Dream-VLA 在 LIBERO 上取得 97.2% 的平均成功率，在 SimplerEnv-Bridge 上达 71.4%，在 SimplerEnv-Fractal 上达 60.5%，超越 π₀ 与 GR00T-N1 等领先模型。

## 核心内容
### 方法架构
- **Dream-VL**：基于扩散大语言模型（dLLM）构建的开源视觉-语言模型，采用双向扩散机制替代传统自回归顺序生成，提升复杂视觉规划任务的适应性。
- **Dream-VLA**：在 Dream-VL 基础上，通过连续预训练开放机器人数据集（如 LIBERO、SimplerEnv）得到的视觉-语言-动作模型。其扩散骨干网络原生支持双向上下文建模，天然适配动作分块（action chunking）与并行生成，显著加速下游微调收敛。

### 实验设置与关键结果
- **LIBERO 基准**：Dream-VLA 平均成功率达 97.2%，超越 π₀ 与 GR00T-N1 等模型。
- **SimplerEnv-Bridge**：整体平均成功率 71.4%。
- **SimplerEnv-Fractal**：整体平均成功率 60.5%。
- **对比验证**：在不同训练目标下，扩散视觉-语言模型（dVLMs）在下游任务中均优于自回归基线模型。

### 结论
Dream-VL 与 Dream-VLA 证明了扩散大语言模型作为视觉-语言-动作模型骨干的优越性，尤其在动作分块与并行生成方面。研究团队已开源这两个模型，以推动社区进一步研究。

## Overview
While autoregressive Large Vision-Language Models (VLMs) have achieved remarkable success, their sequential generation often limits their efficacy in complex visual planning and dynamic robotic control. In this work, we investigate the potential of constructing Vision-Language Models upon diffusion-based large language models (dLLMs) to overcome these limitations. We introduce Dream-VL, an open diffusion-based VLM (dVLM) that achieves state-of-the-art performance among previous dVLMs. Dream-VL is comparable to top-tier AR-based VLMs trained on open data on various benchmarks but exhibits superior potential when applied to visual planning tasks. Building upon Dream-VL, we introduce Dream-VLA, a dLLM-based Vision-Language-Action model (dVLA) developed through continuous pre-training on open robotic datasets. We demonstrate that the natively bidirectional nature of this diffusion backbone serves as a superior foundation for VLA tasks, inherently suited for action chunking and parallel generation, leading to significantly faster convergence in downstream fine-tuning. Dream-VLA achieves top-tier performance of 97.2% average success rate on LIBERO, 71.4% overall average on SimplerEnv-Bridge, and 60.5% overall average on SimplerEnv-Fractal, surpassing leading models such as $π_0$ and GR00T-N1. We also validate that dVLMs surpass AR baselines on downstream tasks across different training objectives. We release both Dream-VL and Dream-VLA to facilitate further research in the community.

## 参考
- http://arxiv.org/abs/2512.22615v2

## 개요
자동회귀 대규모 시각-언어 모델은 상당한 성공을 거두었지만, 순차 생성 특성으로 인해 복잡한 시각 계획 및 동적 로봇 제어에는 한계가 있습니다. 본 연구는 확산 대규모 언어 모델 기반의 시각-언어 모델 구축 가능성을 탐구하며, 오픈소스 확산 시각-언어 모델 Dream-VL을 제안합니다. 이 모델은 동급 모델 중 최고 성능을 달성하고, 공개 데이터로 학습된 자동회귀 모델과 여러 벤치마크에서 비슷한 성능을 보이며, 시각 계획 작업에서 더 우수한 잠재력을 입증합니다. 이를 바탕으로 공개 로봇 데이터셋을 연속 사전 학습하여, 확산 대규모 언어 모델 기반의 시각-언어-행동 모델 Dream-VLA를 출시합니다. 확산 백본 네트워크의 고유한 양방향 특성은 액션 청킹 및 병렬 생성에 자연스럽게 적합하여, 하류 미세 조정 수렴 속도를 크게 향상시킵니다. Dream-VLA는 LIBERO에서 97.2%의 평균 성공률, SimplerEnv-Bridge에서 71.4%, SimplerEnv-Fractal에서 60.5%를 달성하며, π₀ 및 GR00T-N1과 같은 선도 모델을 능가합니다.

## 핵심 내용
### 방법 아키텍처
- **Dream-VL**: 확산 대규모 언어 모델(dLLM) 기반의 오픈소스 시각-언어 모델로, 기존 자동회귀 순차 생성을 대체하는 양방향 확산 메커니즘을 채택하여 복잡한 시각 계획 작업에 대한 적응성을 향상시킵니다.
- **Dream-VLA**: Dream-VL을 기반으로 공개 로봇 데이터셋(예: LIBERO, SimplerEnv)을 연속 사전 학습하여 얻은 시각-언어-행동 모델입니다. 확산 백본 네트워크는 양방향 컨텍스트 모델링을 기본 지원하여 액션 청킹 및 병렬 생성에 자연스럽게 적합하며, 하류 미세 조정 수렴을 크게 가속화합니다.

### 실험 설정 및 주요 결과
- **LIBERO 벤치마크**: Dream-VLA의 평균 성공률은 97.2%로, π₀ 및 GR00T-N1과 같은 모델을 능가합니다.
- **SimplerEnv-Bridge**: 전체 평균 성공률 71.4%.
- **SimplerEnv-Fractal**: 전체 평균 성공률 60.5%.
- **비교 검증**: 다양한 학습 목표에서 확산 시각-언어 모델(dVLMs)은 하류 작업에서 자동회귀 기준 모델보다 모두 우수합니다.

### 결론
Dream-VL과 Dream-VLA는 확산 대규모 언어 모델이 시각-언어-행동 모델의 백본으로서 우수함을 입증하며, 특히 액션 청킹 및 병렬 생성 측면에서 두드러집니다. 연구팀은 커뮤니티의 추가 연구를 촉진하기 위해 두 모델을 오픈소스로 공개했습니다.

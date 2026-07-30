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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.22615v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
자기회귀적 대규모 시각-언어 모델(VLM)은 놀라운 성공을 거두었지만, 순차적 생성 방식은 복잡한 시각적 계획 및 동적 로봇 제어에서 그 효용성을 종종 제한합니다. 본 연구에서는 이러한 한계를 극복하기 위해 확산 기반 대규모 언어 모델(dLLM) 위에 시각-언어 모델을 구축할 가능성을 탐구합니다. 우리는 이전 dVLM 중 최첨단 성능을 달성한 오픈 확산 기반 VLM(dVLM)인 Dream-VL을 소개합니다. Dream-VL은 공개 데이터로 학습된 최고 수준의 AR 기반 VLM과 다양한 벤치마크에서 견줄 만하지만, 시각적 계획 작업에 적용될 때 우수한 잠재력을 보여줍니다. Dream-VL을 기반으로, 우리는 공개 로봇 데이터셋에 대한 지속적인 사전 학습을 통해 개발된 dLLM 기반 시각-언어-행동 모델(dVLA)인 Dream-VLA를 소개합니다. 우리는 이 확산 백본의 본질적으로 양방향적인 특성이 VLA 작업에 탁월한 기반을 제공하며, 액션 청킹 및 병렬 생성에 본질적으로 적합하여 하위 작업 미세 조정에서 훨씬 빠른 수렴을 이끌어낸다는 것을 입증합니다. Dream-VLA는 LIBERO에서 97.2%의 평균 성공률, SimplerEnv-Bridge에서 71.4%의 전체 평균, SimplerEnv-Fractal에서 60.5%의 전체 평균을 달성하여 $π_0$ 및 GR00T-N1과 같은 선도 모델을 능가합니다. 또한 dVLM이 다양한 학습 목표에 걸쳐 하위 작업에서 AR 기준선을 능가한다는 것을 검증합니다. 우리는 커뮤니티의 추가 연구를 촉진하기 위해 Dream-VL과 Dream-VLA를 모두 공개합니다.

## 핵심 내용
자기회귀적 대규모 시각-언어 모델(VLM)은 놀라운 성공을 거두었지만, 순차적 생성 방식은 복잡한 시각적 계획 및 동적 로봇 제어에서 그 효용성을 종종 제한합니다. 본 연구에서는 이러한 한계를 극복하기 위해 확산 기반 대규모 언어 모델(dLLM) 위에 시각-언어 모델을 구축할 가능성을 탐구합니다. 우리는 이전 dVLM 중 최첨단 성능을 달성한 오픈 확산 기반 VLM(dVLM)인 Dream-VL을 소개합니다. Dream-VL은 공개 데이터로 학습된 최고 수준의 AR 기반 VLM과 다양한 벤치마크에서 견줄 만하지만, 시각적 계획 작업에 적용될 때 우수한 잠재력을 보여줍니다. Dream-VL을 기반으로, 우리는 공개 로봇 데이터셋에 대한 지속적인 사전 학습을 통해 개발된 dLLM 기반 시각-언어-행동 모델(dVLA)인 Dream-VLA를 소개합니다. 우리는 이 확산 백본의 본질적으로 양방향적인 특성이 VLA 작업에 탁월한 기반을 제공하며, 액션 청킹 및 병렬 생성에 본질적으로 적합하여 하위 작업 미세 조정에서 훨씬 빠른 수렴을 이끌어낸다는 것을 입증합니다. Dream-VLA는 LIBERO에서 97.2%의 평균 성공률, SimplerEnv-Bridge에서 71.4%의 전체 평균, SimplerEnv-Fractal에서 60.5%의 전체 평균을 달성하여 $π_0$ 및 GR00T-N1과 같은 선도 모델을 능가합니다. 또한 dVLM이 다양한 학습 목표에 걸쳐 하위 작업에서 AR 기준선을 능가한다는 것을 검증합니다. 우리는 커뮤니티의 추가 연구를 촉진하기 위해 Dream-VL과 Dream-VLA를 모두 공개합니다.

## 参考
- http://arxiv.org/abs/2512.22615v2

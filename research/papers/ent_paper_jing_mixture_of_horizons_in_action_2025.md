---
$id: ent_paper_jing_mixture_of_horizons_in_action_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Mixture of Horizons in Action Chunking
  zh: MoH
  ko: Mixture of Horizons in Action Chunking
summary:
  en: Mixture of Horizons in Action Chunking (MoH), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by RUC, UNC, CUHK.
  zh: Mixture of Horizons in Action Chunking (MoH) 是2025年由中国人民大学、北卡罗来纳大学教堂山分校和香港中文大学联合提出的大型视觉-语言-动作模型。其核心贡献在于通过混合不同长度的动作块（horizons）来平衡全局规划与局部精度，并实现动态推理，在LIBERO基准上以99%的平均成功率达到新最优水平。
  ko: Mixture of Horizons in Action Chunking (MoH), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by RUC, UNC, CUHK.
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
- moh
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.19433v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (885 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Mixture of Horizons in Action Chunking (arXiv)
  url: https://arxiv.org/abs/2511.19433
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MoH source
  url: https://doi.org/10.48550/arXiv.2511.19433
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该研究揭示了视觉-语言-动作模型中动作块长度（horizon）的关键权衡：长horizon提供全局预见性但牺牲细粒度精度，短horizon增强局部控制却难以处理长期任务。为此，MoH将动作块拆分为多个不同horizon的片段，通过共享动作变换器并行处理，并用轻量线性门控融合输出。该方法兼具长期与短期优势，可作为即插即用模块集成到现有全注意力动作模块中，同时通过跨horizon共识实现自适应推理，吞吐量提升2.5倍。

## 核心内容
### 方法架构
- **核心问题**：固定horizon训练导致全局与局部性能的固有矛盾，单horizon选择始终次优。
- **MoH策略**：
  - 将原始动作块重新排列为多个不同horizon的片段（如短、中、长片段）。
  - 所有片段通过共享的action transformer并行处理，保持参数效率。
  - 使用轻量线性门控（linear gate）融合各片段输出，实现自适应权重分配。
- **动态推理**：通过跨horizon共识机制选择稳定动作，无需额外训练即可在推理时动态调整horizon。

### 实验设置
- **基础模型**：基于流策略的 $π_0$、$π_{0.5}$ 以及单步回归策略 $π_{\text{reg}}$。
- **训练配置**：在LIBERO基准上仅需30k次训练迭代。
- **对比基线**：固定horizon的原始模型、不同horizon长度的消融实验。

### 关键结果
- **性能提升**：
  - 在LIBERO混合任务设置下，$π_{0.5}$ + MoH达到99%平均成功率，刷新最优水平。
  - 在仿真和真实世界任务中，MoH在所有基础模型上均取得一致且显著的增益。
- **效率优势**：
  - 动态推理模式下，吞吐量比基线高2.5倍，同时保持优越性能。
  - 作为即插即用模块，训练和推理开销极小（仅增加线性门控参数）。
- **消融分析**：验证了多horizon并行处理优于任何单horizon选择，且门控融合比简单平均更有效。

## Overview
Vision-language-action (VLA) models have shown remarkable capabilities in robotic manipulation, but their performance is sensitive to the $\textbf{action chunk length}$ used during training, termed $\textbf{horizon}$. Our empirical study reveals an inherent trade-off: longer horizons provide stronger global foresight but degrade fine-grained accuracy, while shorter ones sharpen local control yet struggle on long-term tasks, implying fixed choice of single horizons being suboptimal. To mitigate the trade-off, we propose a $\textbf{mixture of horizons (MoH)}$ strategy. MoH rearranges the action chunk into several segments with different horizons, processes them in parallel with a shared action transformer, and fuses outputs with a light linear gate. It has three appealing benefits. 1) MoH exploits long-term foresight and short-term precision jointly within a single model, improving both performance and generalizability to complex tasks. 2) MoH is plug-and-play for full-attention action modules with minimal training or inference overhead. 3) MoH enables dynamic inference with adaptive horizons, which selects stable actions through cross-horizon consensus, achieving 2.5$\times$ higher throughput than baselines while preserving superior performance. Extensive experiments over flow-based policies $π_0$, $π_{0.5}$, and one-step regression policy $π_{\text{reg}}$ demonstrate that MoH yields consistent and significant gains on both simulations and real-world tasks. Notably, under mixed-task setting, $π_{0.5}$ with MoH reaches a new state-of-the-art with 99$\%$ average success rate on LIBERO after only $30k$ training iterations. Project page: https://timsty1.github.io/moh/

## 参考
- http://arxiv.org/abs/2511.19433v2

## 개요
이 연구는 비전-언어-행동 모델에서 행동 블록 길이(horizon)의 핵심적인 트레이드오프를 밝혀냅니다: 긴 horizon은 전역적 예측력을 제공하지만 세밀한 정밀도를 희생하고, 짧은 horizon은 국소적 제어를 강화하지만 장기 과제를 처리하기 어렵습니다. 이를 위해 MoH는 행동 블록을 여러 다른 horizon의 세그먼트로 분할하고, 공유된 행동 트랜스포머를 통해 병렬로 처리하며, 경량 선형 게이팅을 사용해 출력을 융합합니다. 이 방법은 장기 및 단기 이점을 모두 갖추며, 기존의 전체 주의(action attention) 행동 모듈에 플러그 앤 플레이 모듈로 통합될 수 있고, 동시에 교차 horizon 합의를 통해 적응형 추론을 구현하여 처리량을 2.5배 향상시킵니다.

## 핵심 내용
### 방법 아키텍처
- **핵심 문제**: 고정된 horizon 훈련은 전역적 및 국소적 성능 간의 본질적인 모순을 초래하며, 단일 horizon 선택은 항상 차선입니다.
- **MoH 전략**:
  - 원래 행동 블록을 여러 다른 horizon의 세그먼트(예: 짧은, 중간, 긴 세그먼트)로 재배열합니다.
  - 모든 세그먼트는 공유된 행동 트랜스포머를 통해 병렬로 처리되어 매개변수 효율성을 유지합니다.
  - 경량 선형 게이팅을 사용해 각 세그먼트의 출력을 융합하여 적응형 가중치 할당을 구현합니다.
- **동적 추론**: 교차 horizon 합의 메커니즘을 통해 안정적인 행동을 선택하며, 추가 훈련 없이 추론 시 horizon을 동적으로 조정할 수 있습니다.

### 실험 설정
- **기본 모델**: 흐름 정책 기반의 $π_0$, $π_{0.5}$ 및 단일 단계 회귀 정책 $π_{\text{reg}}$입니다.
- **훈련 구성**: LIBERO 벤치마크에서 30k 훈련 반복만 필요합니다.
- **비교 기준선**: 고정된 horizon의 원본 모델, 다양한 horizon 길이의 절제 실험입니다.

### 주요 결과
- **성능 향상**:
  - LIBERO 혼합 작업 설정에서 $π_{0.5}$ + MoH는 99% 평균 성공률을 달성하여 최고 수준을 갱신했습니다.
  - 시뮬레이션 및 실제 세계 작업에서 MoH는 모든 기본 모델에서 일관되고 유의미한 이득을 보였습니다.
- **효율성 이점**:
  - 동적 추론 모드에서 처리량이 기준선보다 2.5배 높으며 우수한 성능을 유지합니다.
  - 플러그 앤 플레이 모듈로서 훈련 및 추론 오버헤드가 매우 낮습니다(선형 게이팅 매개변수만 추가).
- **절제 분석**: 다중 horizon 병렬 처리가 단일 horizon 선택보다 우수하며, 게이팅 융합이 단순 평균보다 더 효과적임을 검증했습니다.

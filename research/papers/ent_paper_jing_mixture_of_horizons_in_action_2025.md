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
  zh: Mixture of Horizons in Action Chunking (MoH), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by RUC, UNC, CUHK.
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.19433v2.
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
Vision-language-action (VLA) models have shown remarkable capabilities in robotic manipulation, but their performance is sensitive to the $\textbf{action chunk length}$ used during training, termed $\textbf{horizon}$. Our empirical study reveals an inherent trade-off: longer horizons provide stronger global foresight but degrade fine-grained accuracy, while shorter ones sharpen local control yet struggle on long-term tasks, implying fixed choice of single horizons being suboptimal. To mitigate the trade-off, we propose a $\textbf{mixture of horizons (MoH)}$ strategy. MoH rearranges the action chunk into several segments with different horizons, processes them in parallel with a shared action transformer, and fuses outputs with a light linear gate. It has three appealing benefits. 1) MoH exploits long-term foresight and short-term precision jointly within a single model, improving both performance and generalizability to complex tasks. 2) MoH is plug-and-play for full-attention action modules with minimal training or inference overhead. 3) MoH enables dynamic inference with adaptive horizons, which selects stable actions through cross-horizon consensus, achieving 2.5$\times$ higher throughput than baselines while preserving superior performance. Extensive experiments over flow-based policies $π_0$, $π_{0.5}$, and one-step regression policy $π_{\text{reg}}$ demonstrate that MoH yields consistent and significant gains on both simulations and real-world tasks. Notably, under mixed-task setting, $π_{0.5}$ with MoH reaches a new state-of-the-art with 99$\%$ average success rate on LIBERO after only $30k$ training iterations. Project page: https://timsty1.github.io/moh/

## 核心内容
Vision-language-action (VLA) models have shown remarkable capabilities in robotic manipulation, but their performance is sensitive to the $\textbf{action chunk length}$ used during training, termed $\textbf{horizon}$. Our empirical study reveals an inherent trade-off: longer horizons provide stronger global foresight but degrade fine-grained accuracy, while shorter ones sharpen local control yet struggle on long-term tasks, implying fixed choice of single horizons being suboptimal. To mitigate the trade-off, we propose a $\textbf{mixture of horizons (MoH)}$ strategy. MoH rearranges the action chunk into several segments with different horizons, processes them in parallel with a shared action transformer, and fuses outputs with a light linear gate. It has three appealing benefits. 1) MoH exploits long-term foresight and short-term precision jointly within a single model, improving both performance and generalizability to complex tasks. 2) MoH is plug-and-play for full-attention action modules with minimal training or inference overhead. 3) MoH enables dynamic inference with adaptive horizons, which selects stable actions through cross-horizon consensus, achieving 2.5$\times$ higher throughput than baselines while preserving superior performance. Extensive experiments over flow-based policies $π_0$, $π_{0.5}$, and one-step regression policy $π_{\text{reg}}$ demonstrate that MoH yields consistent and significant gains on both simulations and real-world tasks. Notably, under mixed-task setting, $π_{0.5}$ with MoH reaches a new state-of-the-art with 99$\%$ average success rate on LIBERO after only $30k$ training iterations. Project page: https://timsty1.github.io/moh/

## 参考
- http://arxiv.org/abs/2511.19433v2

## Overview
Vision-language-action (VLA) models have shown remarkable capabilities in robotic manipulation, but their performance is sensitive to the $\textbf{action chunk length}$ used during training, termed $\textbf{horizon}$. Our empirical study reveals an inherent trade-off: longer horizons provide stronger global foresight but degrade fine-grained accuracy, while shorter ones sharpen local control yet struggle on long-term tasks, implying fixed choice of single horizons being suboptimal. To mitigate the trade-off, we propose a $\textbf{mixture of horizons (MoH)}$ strategy. MoH rearranges the action chunk into several segments with different horizons, processes them in parallel with a shared action transformer, and fuses outputs with a light linear gate. It has three appealing benefits. 1) MoH exploits long-term foresight and short-term precision jointly within a single model, improving both performance and generalizability to complex tasks. 2) MoH is plug-and-play for full-attention action modules with minimal training or inference overhead. 3) MoH enables dynamic inference with adaptive horizons, which selects stable actions through cross-horizon consensus, achieving 2.5$\times$ higher throughput than baselines while preserving superior performance. Extensive experiments over flow-based policies $π_0$, $π_{0.5}$, and one-step regression policy $π_{\text{reg}}$ demonstrate that MoH yields consistent and significant gains on both simulations and real-world tasks. Notably, under mixed-task setting, $π_{0.5}$ with MoH reaches a new state-of-the-art with 99$\%$ average success rate on LIBERO after only $30k$ training iterations. Project page: https://timsty1.github.io/moh/

## Content
Vision-language-action (VLA) models have shown remarkable capabilities in robotic manipulation, but their performance is sensitive to the $\textbf{action chunk length}$ used during training, termed $\textbf{horizon}$. Our empirical study reveals an inherent trade-off: longer horizons provide stronger global foresight but degrade fine-grained accuracy, while shorter ones sharpen local control yet struggle on long-term tasks, implying fixed choice of single horizons being suboptimal. To mitigate the trade-off, we propose a $\textbf{mixture of horizons (MoH)}$ strategy. MoH rearranges the action chunk into several segments with different horizons, processes them in parallel with a shared action transformer, and fuses outputs with a light linear gate. It has three appealing benefits. 1) MoH exploits long-term foresight and short-term precision jointly within a single model, improving both performance and generalizability to complex tasks. 2) MoH is plug-and-play for full-attention action modules with minimal training or inference overhead. 3) MoH enables dynamic inference with adaptive horizons, which selects stable actions through cross-horizon consensus, achieving 2.5$\times$ higher throughput than baselines while preserving superior performance. Extensive experiments over flow-based policies $π_0$, $π_{0.5}$, and one-step regression policy $π_{\text{reg}}$ demonstrate that MoH yields consistent and significant gains on both simulations and real-world tasks. Notably, under mixed-task setting, $π_{0.5}$ with MoH reaches a new state-of-the-art with 99$\%$ average success rate on LIBERO after only $30k$ training iterations. Project page: https://timsty1.github.io/moh/

## 개요
Vision-language-action (VLA) 모델은 로봇 조작에서 놀라운 성능을 보여주었지만, 그 성능은 훈련 중 사용되는 $\textbf{액션 청크 길이}$(이하 $\textbf{horizon}$)에 민감합니다. 실증 연구 결과, 장기 horizon은 더 강력한 전역적 예측 능력을 제공하지만 세밀한 정확도가 저하되고, 단기 horizon은 국소적 제어를 강화하지만 장기 과제에서 어려움을 겪는 고유한 트레이드오프가 존재함을 밝혔습니다. 이는 단일 horizon의 고정된 선택이 최적이 아님을 시사합니다. 이러한 트레이드오프를 완화하기 위해, 우리는 $\textbf{mixture of horizons (MoH)}$ 전략을 제안합니다. MoH는 액션 청크를 서로 다른 horizon을 가진 여러 세그먼트로 재구성하고, 공유된 액션 트랜스포머로 병렬 처리한 후, 가벼운 선형 게이트로 출력을 융합합니다. 이는 세 가지 장점을 제공합니다. 1) MoH는 단일 모델 내에서 장기 예측과 단기 정밀도를 동시에 활용하여 복잡한 과제에 대한 성능과 일반화 능력을 모두 향상시킵니다. 2) MoH는 전체 주의 액션 모듈에 대해 최소한의 훈련 또는 추론 오버헤드로 플러그 앤 플레이 방식으로 작동합니다. 3) MoH는 적응형 horizon을 통한 동적 추론을 가능하게 하여, 교차 horizon 합의를 통해 안정적인 액션을 선택함으로써 기준 모델 대비 2.5배 높은 처리량을 달성하면서도 우수한 성능을 유지합니다. 흐름 기반 정책 $π_0$, $π_{0.5}$ 및 단일 회귀 정책 $π_{\text{reg}}$에 대한 광범위한 실험을 통해 MoH가 시뮬레이션과 실제 작업 모두에서 일관되고 유의미한 성능 향상을 제공함을 입증했습니다. 특히, 혼합 과제 설정에서 MoH를 적용한 $π_{0.5}$는 단 $30k$ 훈련 반복 후 LIBERO에서 99$\%$의 평균 성공률로 새로운 최첨단 성능을 달성했습니다. 프로젝트 페이지: https://timsty1.github.io/moh/

## 핵심 내용
Vision-language-action (VLA) 모델은 로봇 조작에서 놀라운 성능을 보여주었지만, 그 성능은 훈련 중 사용되는 $\textbf{액션 청크 길이}$(이하 $\textbf{horizon}$)에 민감합니다. 실증 연구 결과, 장기 horizon은 더 강력한 전역적 예측 능력을 제공하지만 세밀한 정확도가 저하되고, 단기 horizon은 국소적 제어를 강화하지만 장기 과제에서 어려움을 겪는 고유한 트레이드오프가 존재함을 밝혔습니다. 이는 단일 horizon의 고정된 선택이 최적이 아님을 시사합니다. 이러한 트레이드오프를 완화하기 위해, 우리는 $\textbf{mixture of horizons (MoH)}$ 전략을 제안합니다. MoH는 액션 청크를 서로 다른 horizon을 가진 여러 세그먼트로 재구성하고, 공유된 액션 트랜스포머로 병렬 처리한 후, 가벼운 선형 게이트로 출력을 융합합니다. 이는 세 가지 장점을 제공합니다. 1) MoH는 단일 모델 내에서 장기 예측과 단기 정밀도를 동시에 활용하여 복잡한 과제에 대한 성능과 일반화 능력을 모두 향상시킵니다. 2) MoH는 전체 주의 액션 모듈에 대해 최소한의 훈련 또는 추론 오버헤드로 플러그 앤 플레이 방식으로 작동합니다. 3) MoH는 적응형 horizon을 통한 동적 추론을 가능하게 하여, 교차 horizon 합의를 통해 안정적인 액션을 선택함으로써 기준 모델 대비 2.5배 높은 처리량을 달성하면서도 우수한 성능을 유지합니다. 흐름 기반 정책 $π_0$, $π_{0.5}$ 및 단일 회귀 정책 $π_{\text{reg}}$에 대한 광범위한 실험을 통해 MoH가 시뮬레이션과 실제 작업 모두에서 일관되고 유의미한 성능 향상을 제공함을 입증했습니다. 특히, 혼합 과제 설정에서 MoH를 적용한 $π_{0.5}$는 단 $30k$ 훈련 반복 후 LIBERO에서 99$\%$의 평균 성공률로 새로운 최첨단 성능을 달성했습니다. 프로젝트 페이지: https://timsty1.github.io/moh/

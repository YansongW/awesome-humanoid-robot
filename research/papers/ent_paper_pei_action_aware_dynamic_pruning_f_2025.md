---
$id: ent_paper_pei_action_aware_dynamic_pruning_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation
  zh: ADP
  ko: Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation
summary:
  en: Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation (ADP), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by School of Computer Science, The University of Sydney.
  zh: Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation (ADP), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by School of Computer Science, The University of Sydney.
  ko: Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation (ADP), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by School of Computer Science, The University of Sydney.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- adp
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.22093v1.
sources:
- id: src_001
  type: paper
  title: Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation (arXiv)
  url: https://arxiv.org/abs/2509.22093
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ADP source
  url: https://doi.org/10.48550/arXiv.2509.22093
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Robotic manipulation with Vision-Language-Action models requires efficient inference over long-horizon multi-modal context, where attention to dense visual tokens dominates computational cost. Existing methods optimize inference speed by reducing visual redundancy within VLA models, but they overlook the varying redundancy across robotic manipulation stages. We observe that the visual token redundancy is higher in coarse manipulation phase than in fine-grained operations, and is strongly correlated with the action dynamic. Motivated by this observation, we propose \textbf{A}ction-aware \textbf{D}ynamic \textbf{P}runing (\textbf{ADP}), a multi-modal pruning framework that integrates text-driven token selection with action-aware trajectory gating. Our method introduces a gating mechanism that conditions the pruning signal on recent action trajectories, using past motion windows to adaptively adjust token retention ratios in accordance with dynamics, thereby balancing computational efficiency and perceptual precision across different manipulation stages. Extensive experiments on the LIBERO suites and diverse real-world scenarios demonstrate that our method significantly reduces FLOPs and action inference latency (\textit{e.g.} $1.35 \times$ speed up on OpenVLA-OFT) while maintaining competitive success rates (\textit{e.g.} 25.8\% improvements with OpenVLA) compared to baselines, thereby providing a simple plug-in path to efficient robot policies that advances the efficiency and performance frontier of robotic manipulation. Our project website is: \href{https://vla-adp.github.io/}{ADP.com}.

## 核心内容
Robotic manipulation with Vision-Language-Action models requires efficient inference over long-horizon multi-modal context, where attention to dense visual tokens dominates computational cost. Existing methods optimize inference speed by reducing visual redundancy within VLA models, but they overlook the varying redundancy across robotic manipulation stages. We observe that the visual token redundancy is higher in coarse manipulation phase than in fine-grained operations, and is strongly correlated with the action dynamic. Motivated by this observation, we propose \textbf{A}ction-aware \textbf{D}ynamic \textbf{P}runing (\textbf{ADP}), a multi-modal pruning framework that integrates text-driven token selection with action-aware trajectory gating. Our method introduces a gating mechanism that conditions the pruning signal on recent action trajectories, using past motion windows to adaptively adjust token retention ratios in accordance with dynamics, thereby balancing computational efficiency and perceptual precision across different manipulation stages. Extensive experiments on the LIBERO suites and diverse real-world scenarios demonstrate that our method significantly reduces FLOPs and action inference latency (\textit{e.g.} $1.35 \times$ speed up on OpenVLA-OFT) while maintaining competitive success rates (\textit{e.g.} 25.8\% improvements with OpenVLA) compared to baselines, thereby providing a simple plug-in path to efficient robot policies that advances the efficiency and performance frontier of robotic manipulation. Our project website is: \href{https://vla-adp.github.io/}{ADP.com}.

## 参考
- http://arxiv.org/abs/2509.22093v1

## Overview
Robotic manipulation with Vision-Language-Action models requires efficient inference over long-horizon multi-modal context, where attention to dense visual tokens dominates computational cost. Existing methods optimize inference speed by reducing visual redundancy within VLA models, but they overlook the varying redundancy across robotic manipulation stages. We observe that the visual token redundancy is higher in coarse manipulation phase than in fine-grained operations, and is strongly correlated with the action dynamic. Motivated by this observation, we propose \textbf{A}ction-aware \textbf{D}ynamic \textbf{P}runing (\textbf{ADP}), a multi-modal pruning framework that integrates text-driven token selection with action-aware trajectory gating. Our method introduces a gating mechanism that conditions the pruning signal on recent action trajectories, using past motion windows to adaptively adjust token retention ratios in accordance with dynamics, thereby balancing computational efficiency and perceptual precision across different manipulation stages. Extensive experiments on the LIBERO suites and diverse real-world scenarios demonstrate that our method significantly reduces FLOPs and action inference latency (\textit{e.g.} $1.35 \times$ speed up on OpenVLA-OFT) while maintaining competitive success rates (\textit{e.g.} 25.8\% improvements with OpenVLA) compared to baselines, thereby providing a simple plug-in path to efficient robot policies that advances the efficiency and performance frontier of robotic manipulation. Our project website is: \href{https://vla-adp.github.io/}{ADP.com}.

## Content
Robotic manipulation with Vision-Language-Action models requires efficient inference over long-horizon multi-modal context, where attention to dense visual tokens dominates computational cost. Existing methods optimize inference speed by reducing visual redundancy within VLA models, but they overlook the varying redundancy across robotic manipulation stages. We observe that the visual token redundancy is higher in coarse manipulation phase than in fine-grained operations, and is strongly correlated with the action dynamic. Motivated by this observation, we propose \textbf{A}ction-aware \textbf{D}ynamic \textbf{P}runing (\textbf{ADP}), a multi-modal pruning framework that integrates text-driven token selection with action-aware trajectory gating. Our method introduces a gating mechanism that conditions the pruning signal on recent action trajectories, using past motion windows to adaptively adjust token retention ratios in accordance with dynamics, thereby balancing computational efficiency and perceptual precision across different manipulation stages. Extensive experiments on the LIBERO suites and diverse real-world scenarios demonstrate that our method significantly reduces FLOPs and action inference latency (\textit{e.g.} $1.35 \times$ speed up on OpenVLA-OFT) while maintaining competitive success rates (\textit{e.g.} 25.8\% improvements with OpenVLA) compared to baselines, thereby providing a simple plug-in path to efficient robot policies that advances the efficiency and performance frontier of robotic manipulation. Our project website is: \href{https://vla-adp.github.io/}{ADP.com}.

## 개요
Vision-Language-Action 모델을 활용한 로봇 조작은 장기적인 다중 모달 컨텍스트에 대한 효율적인 추론을 필요로 하며, 이때 밀집된 시각적 토큰에 대한 어텐션이 계산 비용을 지배합니다. 기존 방법은 VLA 모델 내 시각적 중복성을 줄여 추론 속도를 최적화하지만, 로봇 조작 단계에 따라 달라지는 중복성을 간과합니다. 우리는 조잡한 조작 단계에서 미세한 작업보다 시각적 토큰 중복성이 더 높으며, 이는 동작 역학과 강한 상관관계가 있음을 관찰했습니다. 이러한 관찰에 기반하여, 우리는 텍스트 기반 토큰 선택과 동작 인식 궤적 게이팅을 통합하는 다중 모달 프루닝 프레임워크인 **동작 인식 동적 프루닝(ADP)**을 제안합니다. 우리의 방법은 최근 동작 궤적에 프루닝 신호를 조건화하는 게이팅 메커니즘을 도입하여, 과거 모션 윈도우를 사용해 동역학에 따라 토큰 유지 비율을 적응적으로 조정함으로써 다양한 조작 단계에서 계산 효율성과 인식 정밀도의 균형을 맞춥니다. LIBERO 스위트 및 다양한 실제 시나리오에 대한 광범위한 실험을 통해, 우리의 방법이 기준선과 비교하여 FLOPs 및 동작 추론 지연 시간을 크게 줄이고(예: OpenVLA-OFT에서 $1.35 \times$ 속도 향상), 경쟁력 있는 성공률을 유지(예: OpenVLA에서 25.8% 개선)함으로써, 로봇 조작의 효율성 및 성능 경계를 발전시키는 효율적인 로봇 정책을 위한 간단한 플러그인 경로를 제공함을 입증합니다. 프로젝트 웹사이트는 \href{https://vla-adp.github.io/}{ADP.com}입니다.

## 핵심 내용
Vision-Language-Action 모델을 활용한 로봇 조작은 장기적인 다중 모달 컨텍스트에 대한 효율적인 추론을 필요로 하며, 이때 밀집된 시각적 토큰에 대한 어텐션이 계산 비용을 지배합니다. 기존 방법은 VLA 모델 내 시각적 중복성을 줄여 추론 속도를 최적화하지만, 로봇 조작 단계에 따라 달라지는 중복성을 간과합니다. 우리는 조잡한 조작 단계에서 미세한 작업보다 시각적 토큰 중복성이 더 높으며, 이는 동작 역학과 강한 상관관계가 있음을 관찰했습니다. 이러한 관찰에 기반하여, 우리는 텍스트 기반 토큰 선택과 동작 인식 궤적 게이팅을 통합하는 다중 모달 프루닝 프레임워크인 **동작 인식 동적 프루닝(ADP)**을 제안합니다. 우리의 방법은 최근 동작 궤적에 프루닝 신호를 조건화하는 게이팅 메커니즘을 도입하여, 과거 모션 윈도우를 사용해 동역학에 따라 토큰 유지 비율을 적응적으로 조정함으로써 다양한 조작 단계에서 계산 효율성과 인식 정밀도의 균형을 맞춥니다. LIBERO 스위트 및 다양한 실제 시나리오에 대한 광범위한 실험을 통해, 우리의 방법이 기준선과 비교하여 FLOPs 및 동작 추론 지연 시간을 크게 줄이고(예: OpenVLA-OFT에서 $1.35 \times$ 속도 향상), 경쟁력 있는 성공률을 유지(예: OpenVLA에서 25.8% 개선)함으로써, 로봇 조작의 효율성 및 성능 경계를 발전시키는 효율적인 로봇 정책을 위한 간단한 플러그인 경로를 제공함을 입증합니다. 프로젝트 웹사이트는 \href{https://vla-adp.github.io/}{ADP.com}입니다.

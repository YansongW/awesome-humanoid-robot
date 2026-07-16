---
$id: ent_paper_cai_seeing_space_and_motion_enhanc_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Seeing Space and Motion: Enhancing Latent Actions with Spatial and Dynamic Awareness for VLA'
  zh: SSM-VLA
  ko: 'Seeing Space and Motion: Enhancing Latent Actions with Spatial and Dynamic Awareness for VLA'
summary:
  en: 'Seeing Space and Motion: Enhancing Latent Actions with Spatial and Dynamic Awareness for VLA (SSM-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Tsinghua Shenzhen International Graduate School,
    Tsinghua University, Amap, Alibaba Group, School of Software Engineering, Xi’an Jiaotong University, Xi’an Jiaotong University..'
  zh: 'Seeing Space and Motion: Enhancing Latent Actions with Spatial and Dynamic Awareness for VLA (SSM-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Tsinghua Shenzhen International Graduate School,
    Tsinghua University, Amap, Alibaba Group, School of Software Engineering, Xi’an Jiaotong University, Xi’an Jiaotong University..'
  ko: 'Seeing Space and Motion: Enhancing Latent Actions with Spatial and Dynamic Awareness for VLA (SSM-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Tsinghua Shenzhen International Graduate School,
    Tsinghua University, Amap, Alibaba Group, School of Software Engineering, Xi’an Jiaotong University, Xi’an Jiaotong University..'
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
- ssm_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.26251v2.
sources:
- id: src_001
  type: paper
  title: 'Seeing Space and Motion: Enhancing Latent Actions with Spatial and Dynamic Awareness for VLA (arXiv)'
  url: https://arxiv.org/abs/2509.26251
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SSM-VLA source
  url: https://doi.org/10.48550/arXiv.2509.26251
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Latent Action Models (LAMs) enable Vision- Language-Action (VLA) systems to learn semantic action representations from large-scale unannotated data. Yet, we identify two bottlenecks of LAMs: 1) the commonly adopted end-to-end trained image encoder suffers from poor spatial understanding; 2) LAMs can be fragile when input frames are temporally distant, leading to limited temporal percep- tion. Such factors inevitably hinder stable and clear action modeling. To this end, we propose Farsighted-LAM, a latent action framework with geometry-aware spatial encoding and multi-scale temporal modeling, capturing structural priors and dynamic motion patterns from consecutive frames. We further propose SSM-VLA, an end-to-end VLA framework built upon Farsighted-LAM, which integrates structured perception with a visual Chain-of-Thought module to explicitly reason about environmental dynamics, enhancing decision consistency and interpretability. We validate SSM-VLA on multiple VLA tasks in both simulation and real-world settings, and achieve state-of- the-art performance. Our results demonstrate that our strategy of combining geometry-aware modeling, temporal coherence, and explicit reasoning is effective in enhancing the robustness and generalizability of embodied intelligence.

## 核心内容
Latent Action Models (LAMs) enable Vision- Language-Action (VLA) systems to learn semantic action representations from large-scale unannotated data. Yet, we identify two bottlenecks of LAMs: 1) the commonly adopted end-to-end trained image encoder suffers from poor spatial understanding; 2) LAMs can be fragile when input frames are temporally distant, leading to limited temporal percep- tion. Such factors inevitably hinder stable and clear action modeling. To this end, we propose Farsighted-LAM, a latent action framework with geometry-aware spatial encoding and multi-scale temporal modeling, capturing structural priors and dynamic motion patterns from consecutive frames. We further propose SSM-VLA, an end-to-end VLA framework built upon Farsighted-LAM, which integrates structured perception with a visual Chain-of-Thought module to explicitly reason about environmental dynamics, enhancing decision consistency and interpretability. We validate SSM-VLA on multiple VLA tasks in both simulation and real-world settings, and achieve state-of- the-art performance. Our results demonstrate that our strategy of combining geometry-aware modeling, temporal coherence, and explicit reasoning is effective in enhancing the robustness and generalizability of embodied intelligence.

## 参考
- http://arxiv.org/abs/2509.26251v2

## Overview
Latent Action Models (LAMs) enable Vision-Language-Action (VLA) systems to learn semantic action representations from large-scale unannotated data. Yet, we identify two bottlenecks of LAMs: 1) the commonly adopted end-to-end trained image encoder suffers from poor spatial understanding; 2) LAMs can be fragile when input frames are temporally distant, leading to limited temporal perception. Such factors inevitably hinder stable and clear action modeling. To this end, we propose Farsighted-LAM, a latent action framework with geometry-aware spatial encoding and multi-scale temporal modeling, capturing structural priors and dynamic motion patterns from consecutive frames. We further propose SSM-VLA, an end-to-end VLA framework built upon Farsighted-LAM, which integrates structured perception with a visual Chain-of-Thought module to explicitly reason about environmental dynamics, enhancing decision consistency and interpretability. We validate SSM-VLA on multiple VLA tasks in both simulation and real-world settings, and achieve state-of-the-art performance. Our results demonstrate that our strategy of combining geometry-aware modeling, temporal coherence, and explicit reasoning is effective in enhancing the robustness and generalizability of embodied intelligence.

## Content
Latent Action Models (LAMs) enable Vision-Language-Action (VLA) systems to learn semantic action representations from large-scale unannotated data. Yet, we identify two bottlenecks of LAMs: 1) the commonly adopted end-to-end trained image encoder suffers from poor spatial understanding; 2) LAMs can be fragile when input frames are temporally distant, leading to limited temporal perception. Such factors inevitably hinder stable and clear action modeling. To this end, we propose Farsighted-LAM, a latent action framework with geometry-aware spatial encoding and multi-scale temporal modeling, capturing structural priors and dynamic motion patterns from consecutive frames. We further propose SSM-VLA, an end-to-end VLA framework built upon Farsighted-LAM, which integrates structured perception with a visual Chain-of-Thought module to explicitly reason about environmental dynamics, enhancing decision consistency and interpretability. We validate SSM-VLA on multiple VLA tasks in both simulation and real-world settings, and achieve state-of-the-art performance. Our results demonstrate that our strategy of combining geometry-aware modeling, temporal coherence, and explicit reasoning is effective in enhancing the robustness and generalizability of embodied intelligence.

## 개요
Latent Action Models (LAMs)는 대규모 비주석 데이터로부터 시각-언어-행동(VLA) 시스템이 의미론적 행동 표현을 학습할 수 있게 합니다. 그러나 우리는 LAM의 두 가지 병목 현상을 식별했습니다: 1) 일반적으로 사용되는 종단 간 학습된 이미지 인코더는 공간 이해 능력이 부족하며; 2) LAM은 입력 프레임이 시간적으로 멀리 떨어져 있을 때 취약해져 시간적 인식이 제한됩니다. 이러한 요인들은 필연적으로 안정적이고 명확한 행동 모델링을 방해합니다. 이를 해결하기 위해 우리는 기하학 인식 공간 인코딩과 다중 스케일 시간 모델링을 갖춘 잠재 행동 프레임워크인 Farsighted-LAM을 제안하며, 연속 프레임으로부터 구조적 사전 지식과 동적 움직임 패턴을 포착합니다. 또한 Farsighted-LAM을 기반으로 구축된 종단 간 VLA 프레임워크인 SSM-VLA를 제안하며, 이는 구조적 인식과 시각적 사고 사슬 모듈을 통합하여 환경 역학을 명시적으로 추론함으로써 결정 일관성과 해석 가능성을 향상시킵니다. 우리는 SSM-VLA를 시뮬레이션 및 실제 환경 모두에서 여러 VLA 작업에 대해 검증하고 최첨단 성능을 달성했습니다. 우리의 결과는 기하학 인식 모델링, 시간적 일관성, 명시적 추론을 결합한 전략이 구현된 지능의 견고성과 일반화 능력을 향상시키는 데 효과적임을 보여줍니다.

## 핵심 내용
Latent Action Models (LAMs)는 대규모 비주석 데이터로부터 시각-언어-행동(VLA) 시스템이 의미론적 행동 표현을 학습할 수 있게 합니다. 그러나 우리는 LAM의 두 가지 병목 현상을 식별했습니다: 1) 일반적으로 사용되는 종단 간 학습된 이미지 인코더는 공간 이해 능력이 부족하며; 2) LAM은 입력 프레임이 시간적으로 멀리 떨어져 있을 때 취약해져 시간적 인식이 제한됩니다. 이러한 요인들은 필연적으로 안정적이고 명확한 행동 모델링을 방해합니다. 이를 해결하기 위해 우리는 기하학 인식 공간 인코딩과 다중 스케일 시간 모델링을 갖춘 잠재 행동 프레임워크인 Farsighted-LAM을 제안하며, 연속 프레임으로부터 구조적 사전 지식과 동적 움직임 패턴을 포착합니다. 또한 Farsighted-LAM을 기반으로 구축된 종단 간 VLA 프레임워크인 SSM-VLA를 제안하며, 이는 구조적 인식과 시각적 사고 사슬 모듈을 통합하여 환경 역학을 명시적으로 추론함으로써 결정 일관성과 해석 가능성을 향상시킵니다. 우리는 SSM-VLA를 시뮬레이션 및 실제 환경 모두에서 여러 VLA 작업에 대해 검증하고 최첨단 성능을 달성했습니다. 우리의 결과는 기하학 인식 모델링, 시간적 일관성, 명시적 추론을 결합한 전략이 구현된 지능의 견고성과 일반화 능력을 향상시키는 데 효과적임을 보여줍니다.

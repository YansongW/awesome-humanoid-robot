---
$id: ent_paper_architecture_is_all_you_need_d_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Architecture Is All You Need: Diversity-Enabled Sweet Spots for Robust Humanoid Locomotion'
  zh: 'Architecture Is All You Need: Diversity-Enabled Sweet Spots for Robust Humanoid Locomotion'
  ko: 'Architecture Is All You Need: Diversity-Enabled Sweet Spots for Robust Humanoid Locomotion'
summary:
  en: 'Architecture Is All You Need: Diversity-Enabled Sweet Spots for Robust Humanoid Locomotion is a 2025 work on locomotion
    for humanoid robots.'
  zh: 'Architecture Is All You Need: Diversity-Enabled Sweet Spots for Robust Humanoid Locomotion is a 2025 work on locomotion
    for humanoid robots.'
  ko: 'Architecture Is All You Need: Diversity-Enabled Sweet Spots for Robust Humanoid Locomotion is a 2025 work on locomotion
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- architecture_is_all_you_need
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.14947v2.
sources:
- id: src_001
  type: paper
  title: 'Architecture Is All You Need: Diversity-Enabled Sweet Spots for Robust Humanoid Locomotion (arXiv)'
  url: https://arxiv.org/abs/2510.14947
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Robust humanoid locomotion in unstructured environments requires architectures that balance fast low-level stabilization with slower perceptual decision-making. We show that a simple layered control architecture (LCA), a proprioceptive stabilizer running at high rate, coupled with a compact low-rate perceptual policy, enables substantially more robust performance than monolithic end-to-end designs, even when using minimal perception encoders. Through a two-stage training curriculum (blind stabilizer pretraining followed by perceptual fine-tuning), we demonstrate that layered policies consistently outperform one-stage alternatives in both simulation and hardware. On a Unitree G1 humanoid, our approach succeeds across stair and ledge tasks where one-stage perceptual policies fail. These results highlight that architectural separation of timescales, rather than network scale or complexity, is the key enabler for robust perception-conditioned locomotion.

## 核心内容
Robust humanoid locomotion in unstructured environments requires architectures that balance fast low-level stabilization with slower perceptual decision-making. We show that a simple layered control architecture (LCA), a proprioceptive stabilizer running at high rate, coupled with a compact low-rate perceptual policy, enables substantially more robust performance than monolithic end-to-end designs, even when using minimal perception encoders. Through a two-stage training curriculum (blind stabilizer pretraining followed by perceptual fine-tuning), we demonstrate that layered policies consistently outperform one-stage alternatives in both simulation and hardware. On a Unitree G1 humanoid, our approach succeeds across stair and ledge tasks where one-stage perceptual policies fail. These results highlight that architectural separation of timescales, rather than network scale or complexity, is the key enabler for robust perception-conditioned locomotion.

## 参考
- http://arxiv.org/abs/2510.14947v2

## Overview
Robust humanoid locomotion in unstructured environments requires architectures that balance fast low-level stabilization with slower perceptual decision-making. We show that a simple layered control architecture (LCA), a proprioceptive stabilizer running at high rate, coupled with a compact low-rate perceptual policy, enables substantially more robust performance than monolithic end-to-end designs, even when using minimal perception encoders. Through a two-stage training curriculum (blind stabilizer pretraining followed by perceptual fine-tuning), we demonstrate that layered policies consistently outperform one-stage alternatives in both simulation and hardware. On a Unitree G1 humanoid, our approach succeeds across stair and ledge tasks where one-stage perceptual policies fail. These results highlight that architectural separation of timescales, rather than network scale or complexity, is the key enabler for robust perception-conditioned locomotion.

## Content
Robust humanoid locomotion in unstructured environments requires architectures that balance fast low-level stabilization with slower perceptual decision-making. We show that a simple layered control architecture (LCA), a proprioceptive stabilizer running at high rate, coupled with a compact low-rate perceptual policy, enables substantially more robust performance than monolithic end-to-end designs, even when using minimal perception encoders. Through a two-stage training curriculum (blind stabilizer pretraining followed by perceptual fine-tuning), we demonstrate that layered policies consistently outperform one-stage alternatives in both simulation and hardware. On a Unitree G1 humanoid, our approach succeeds across stair and ledge tasks where one-stage perceptual policies fail. These results highlight that architectural separation of timescales, rather than network scale or complexity, is the key enabler for robust perception-conditioned locomotion.

## 개요
비정형 환경에서의 강건한 휴머노이드 보행을 위해서는 빠른 저수준 안정화와 느린 지각적 의사 결정의 균형을 맞추는 아키텍처가 필요합니다. 본 연구는 고속으로 작동하는 고유수용성 안정화기와 소형 저속 지각 정책을 결합한 단순한 계층적 제어 아키텍처(LCA)가, 최소한의 지각 인코더를 사용하더라도 모놀리식 엔드투엔드 설계보다 훨씬 더 강건한 성능을 제공함을 보여줍니다. 2단계 훈련 커리큘럼(블라인드 안정화기 사전 훈련 후 지각 미세 조정)을 통해, 계층적 정책이 시뮬레이션과 하드웨어 모두에서 단일 단계 대안보다 일관되게 우수함을 입증했습니다. Unitree G1 휴머노이드에서 본 접근법은 단일 단계 지각 정책이 실패하는 계단 및 선반 작업에서 성공합니다. 이러한 결과는 네트워크 규모나 복잡성보다 시간 척도의 아키텍처적 분리가 강건한 지각 조건부 보행의 핵심 요소임을 강조합니다.

## 핵심 내용
비정형 환경에서의 강건한 휴머노이드 보행을 위해서는 빠른 저수준 안정화와 느린 지각적 의사 결정의 균형을 맞추는 아키텍처가 필요합니다. 본 연구는 고속으로 작동하는 고유수용성 안정화기와 소형 저속 지각 정책을 결합한 단순한 계층적 제어 아키텍처(LCA)가, 최소한의 지각 인코더를 사용하더라도 모놀리식 엔드투엔드 설계보다 훨씬 더 강건한 성능을 제공함을 보여줍니다. 2단계 훈련 커리큘럼(블라인드 안정화기 사전 훈련 후 지각 미세 조정)을 통해, 계층적 정책이 시뮬레이션과 하드웨어 모두에서 단일 단계 대안보다 일관되게 우수함을 입증했습니다. Unitree G1 휴머노이드에서 본 접근법은 단일 단계 지각 정책이 실패하는 계단 및 선반 작업에서 성공합니다. 이러한 결과는 네트워크 규모나 복잡성보다 시간 척도의 아키텍처적 분리가 강건한 지각 조건부 보행의 핵심 요소임을 강조합니다.

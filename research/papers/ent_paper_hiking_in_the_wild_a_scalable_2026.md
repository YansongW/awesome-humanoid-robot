---
$id: ent_paper_hiking_in_the_wild_a_scalable_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Hiking in the Wild: A Scalable Perceptive Parkour Framework for Humanoids'
  zh: 脚落在哪里，比走得多快更重要
  ko: 'Hiking in the Wild: A Scalable Perceptive Parkour Framework for Humanoids'
summary:
  en: 'Hiking in the Wild: A Scalable Perceptive Parkour Framework for Humanoids is a knowledge node related to paper in the
    humanoid robot value chain.'
  zh: 'Achieving robust humanoid hiking in complex, unstructured environments requires transitioning from reactive proprioception
    to proactive perception. However, integrating exteroception remains a significant challenge: mapping-based methods suffer
    from state estimation drift; for instance, LiDAR-based methods do not handle torso jitter well. Existing end-to-end approaches
    often struggle with scalability and training complexity; specifically, some previous works using virtual obstacles are
    implemented case-by-case. In this work, we present \textit{Hiking in the Wild}, a scalable, end-to-end parkour perceptive
    framework designed for robust humanoid hiking. To ensure safety and training stability, we introduce two key mechanisms:
    a foothold safety mechanism combining scalable \textit{Terrain Edg'
  ko: 'Hiking in the Wild: A Scalable Perceptive Parkour Framework for Humanoids is a knowledge node related to paper in the
    humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- high_dynamic_motion
- locomotion
- parkour
- perception
- vision_guided_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.07718v1.
sources:
- id: src_001
  type: paper
  title: 'Hiking in the Wild: A Scalable Perceptive Parkour Framework for Humanoids (arXiv)'
  url: https://arxiv.org/abs/2601.07718
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 脚落在哪里，比走得多快更重要 project page
  url: https://project-instinct.github.io/hiking-in-the-wild
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
Achieving robust humanoid hiking in complex, unstructured environments requires transitioning from reactive proprioception to proactive perception. However, integrating exteroception remains a significant challenge: mapping-based methods suffer from state estimation drift; for instance, LiDAR-based methods do not handle torso jitter well. Existing end-to-end approaches often struggle with scalability and training complexity; specifically, some previous works using virtual obstacles are implemented case-by-case. In this work, we present \textit{Hiking in the Wild}, a scalable, end-to-end parkour perceptive framework designed for robust humanoid hiking. To ensure safety and training stability, we introduce two key mechanisms: a foothold safety mechanism combining scalable \textit{Terrain Edge Detection} with \textit{Foot Volume Points} to prevent catastrophic slippage on edges, and a \textit{Flat Patch Sampling} strategy that mitigates reward hacking by generating feasible navigation targets. Our approach utilizes a single-stage reinforcement learning scheme, mapping raw depth inputs and proprioception directly to joint actions, without relying on external state estimation. Extensive field experiments on a full-size humanoid demonstrate that our policy enables robust traversal of complex terrains at speeds up to 2.5 m/s. The training and deployment code is open-sourced to facilitate reproducible research and deployment on real robots with minimal hardware modifications.

## 核心内容
Achieving robust humanoid hiking in complex, unstructured environments requires transitioning from reactive proprioception to proactive perception. However, integrating exteroception remains a significant challenge: mapping-based methods suffer from state estimation drift; for instance, LiDAR-based methods do not handle torso jitter well. Existing end-to-end approaches often struggle with scalability and training complexity; specifically, some previous works using virtual obstacles are implemented case-by-case. In this work, we present \textit{Hiking in the Wild}, a scalable, end-to-end parkour perceptive framework designed for robust humanoid hiking. To ensure safety and training stability, we introduce two key mechanisms: a foothold safety mechanism combining scalable \textit{Terrain Edge Detection} with \textit{Foot Volume Points} to prevent catastrophic slippage on edges, and a \textit{Flat Patch Sampling} strategy that mitigates reward hacking by generating feasible navigation targets. Our approach utilizes a single-stage reinforcement learning scheme, mapping raw depth inputs and proprioception directly to joint actions, without relying on external state estimation. Extensive field experiments on a full-size humanoid demonstrate that our policy enables robust traversal of complex terrains at speeds up to 2.5 m/s. The training and deployment code is open-sourced to facilitate reproducible research and deployment on real robots with minimal hardware modifications.

## 参考
- http://arxiv.org/abs/2601.07718v1

## Overview
Achieving robust humanoid hiking in complex, unstructured environments requires transitioning from reactive proprioception to proactive perception. However, integrating exteroception remains a significant challenge: mapping-based methods suffer from state estimation drift; for instance, LiDAR-based methods do not handle torso jitter well. Existing end-to-end approaches often struggle with scalability and training complexity; specifically, some previous works using virtual obstacles are implemented case-by-case. In this work, we present \textit{Hiking in the Wild}, a scalable, end-to-end parkour perceptive framework designed for robust humanoid hiking. To ensure safety and training stability, we introduce two key mechanisms: a foothold safety mechanism combining scalable \textit{Terrain Edge Detection} with \textit{Foot Volume Points} to prevent catastrophic slippage on edges, and a \textit{Flat Patch Sampling} strategy that mitigates reward hacking by generating feasible navigation targets. Our approach utilizes a single-stage reinforcement learning scheme, mapping raw depth inputs and proprioception directly to joint actions, without relying on external state estimation. Extensive field experiments on a full-size humanoid demonstrate that our policy enables robust traversal of complex terrains at speeds up to 2.5 m/s. The training and deployment code is open-sourced to facilitate reproducible research and deployment on real robots with minimal hardware modifications.

## Content
Achieving robust humanoid hiking in complex, unstructured environments requires transitioning from reactive proprioception to proactive perception. However, integrating exteroception remains a significant challenge: mapping-based methods suffer from state estimation drift; for instance, LiDAR-based methods do not handle torso jitter well. Existing end-to-end approaches often struggle with scalability and training complexity; specifically, some previous works using virtual obstacles are implemented case-by-case. In this work, we present \textit{Hiking in the Wild}, a scalable, end-to-end parkour perceptive framework designed for robust humanoid hiking. To ensure safety and training stability, we introduce two key mechanisms: a foothold safety mechanism combining scalable \textit{Terrain Edge Detection} with \textit{Foot Volume Points} to prevent catastrophic slippage on edges, and a \textit{Flat Patch Sampling} strategy that mitigates reward hacking by generating feasible navigation targets. Our approach utilizes a single-stage reinforcement learning scheme, mapping raw depth inputs and proprioception directly to joint actions, without relying on external state estimation. Extensive field experiments on a full-size humanoid demonstrate that our policy enables robust traversal of complex terrains at speeds up to 2.5 m/s. The training and deployment code is open-sourced to facilitate reproducible research and deployment on real robots with minimal hardware modifications.

## 개요
복잡하고 비정형적인 환경에서 강건한 휴머노이드 하이킹을 달성하려면 반응적 고유수용성 감각에서 능동적 외부 감각으로 전환해야 합니다. 그러나 외부 감각 통합은 여전히 중요한 과제로 남아 있습니다. 지도 기반 방법은 상태 추정 드리프트 문제를 겪으며, 예를 들어 LiDAR 기반 방법은 몸통 흔들림을 잘 처리하지 못합니다. 기존의 종단 간 접근 방식은 확장성과 훈련 복잡성에 어려움을 겪는 경우가 많으며, 특히 가상 장애물을 사용한 일부 이전 연구는 사례별로 구현되었습니다. 본 연구에서는 강건한 휴머노이드 하이킹을 위해 설계된 확장 가능한 종단 간 파쿠르 인지 프레임워크인 \textit{Hiking in the Wild}를 제시합니다. 안전성과 훈련 안정성을 보장하기 위해 두 가지 핵심 메커니즘을 도입합니다. 확장 가능한 \textit{지형 가장자리 감지}와 \textit{발 볼륨 포인트}를 결합하여 가장자리에서의 치명적인 미끄러짐을 방지하는 발판 안전 메커니즘과, 실행 가능한 내비게이션 목표를 생성하여 보상 해킹을 완화하는 \textit{평평한 패치 샘플링} 전략입니다. 우리의 접근 방식은 단일 단계 강화 학습 방식을 사용하여 외부 상태 추정에 의존하지 않고 원시 깊이 입력과 고유수용성 감각을 관절 동작에 직접 매핑합니다. 실제 크기 휴머노이드에서의 광범위한 현장 실험을 통해 우리의 정책이 최대 2.5m/s의 속도로 복잡한 지형을 강건하게 횡단할 수 있음을 입증했습니다. 훈련 및 배포 코드는 오픈소스로 공개되어 최소한의 하드웨어 수정으로 실제 로봇에서 재현 가능한 연구와 배포를 용이하게 합니다.

## 핵심 내용
복잡하고 비정형적인 환경에서 강건한 휴머노이드 하이킹을 달성하려면 반응적 고유수용성 감각에서 능동적 외부 감각으로 전환해야 합니다. 그러나 외부 감각 통합은 여전히 중요한 과제로 남아 있습니다. 지도 기반 방법은 상태 추정 드리프트 문제를 겪으며, 예를 들어 LiDAR 기반 방법은 몸통 흔들림을 잘 처리하지 못합니다. 기존의 종단 간 접근 방식은 확장성과 훈련 복잡성에 어려움을 겪는 경우가 많으며, 특히 가상 장애물을 사용한 일부 이전 연구는 사례별로 구현되었습니다. 본 연구에서는 강건한 휴머노이드 하이킹을 위해 설계된 확장 가능한 종단 간 파쿠르 인지 프레임워크인 \textit{Hiking in the Wild}를 제시합니다. 안전성과 훈련 안정성을 보장하기 위해 두 가지 핵심 메커니즘을 도입합니다. 확장 가능한 \textit{지형 가장자리 감지}와 \textit{발 볼륨 포인트}를 결합하여 가장자리에서의 치명적인 미끄러짐을 방지하는 발판 안전 메커니즘과, 실행 가능한 내비게이션 목표를 생성하여 보상 해킹을 완화하는 \textit{평평한 패치 샘플링} 전략입니다. 우리의 접근 방식은 단일 단계 강화 학습 방식을 사용하여 외부 상태 추정에 의존하지 않고 원시 깊이 입력과 고유수용성 감각을 관절 동작에 직접 매핑합니다. 실제 크기 휴머노이드에서의 광범위한 현장 실험을 통해 우리의 정책이 최대 2.5m/s의 속도로 복잡한 지형을 강건하게 횡단할 수 있음을 입증했습니다. 훈련 및 배포 코드는 오픈소스로 공개되어 최소한의 하드웨어 수정으로 실제 로봇에서 재현 가능한 연구와 배포를 용이하게 합니다.

---
$id: ent_paper_phuma_physically_grounded_huma_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PHUMA: Physically-Grounded Humanoid Locomotion Dataset'
  zh: 'PHUMA: Physically-Grounded Humanoid Locomotion Dataset'
  ko: 'PHUMA: Physically-Grounded Humanoid Locomotion Dataset'
summary:
  en: 'PHUMA: Physically-Grounded Humanoid Locomotion Dataset is a 2025 work on locomotion for humanoid robots.'
  zh: 'PHUMA: Physically-Grounded Humanoid Locomotion Dataset is a 2025 work on locomotion for humanoid robots.'
  ko: 'PHUMA: Physically-Grounded Humanoid Locomotion Dataset is a 2025 work on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- phuma
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.26236v2.
sources:
- id: src_001
  type: paper
  title: 'PHUMA: Physically-Grounded Humanoid Locomotion Dataset (arXiv)'
  url: https://arxiv.org/abs/2510.26236
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Motion imitation is a promising approach for humanoid locomotion, enabling agents to acquire humanlike behaviors. Existing methods typically rely on high-quality motion capture datasets such as AMASS, but these are scarce and expensive, limiting scalability and diversity. Recent studies attempt to scale data collection by converting large-scale internet videos, exemplified by Humanoid-X. However, they often suffer from physical artifacts such as floating, penetration, and foot skating, which hinder stable imitation. To address this, we introduce PHUMA, a Physically Reliable HUMAnoid locomotion dataset produced by a two-stage pipeline combining physics-aware curation and physics-constrained retargeting, aggregating both motion capture and internet video into a physically reliable, 73-hour corpus. On motion tracking benchmarks, PHUMA-trained policies achieve higher success rates than those trained on AMASS and Humanoid-X, and successfully transfer zero-shot to a real Unitree G1. The code is available at https://davian-robotics.github.io/PHUMA.

## 核心内容
Motion imitation is a promising approach for humanoid locomotion, enabling agents to acquire humanlike behaviors. Existing methods typically rely on high-quality motion capture datasets such as AMASS, but these are scarce and expensive, limiting scalability and diversity. Recent studies attempt to scale data collection by converting large-scale internet videos, exemplified by Humanoid-X. However, they often suffer from physical artifacts such as floating, penetration, and foot skating, which hinder stable imitation. To address this, we introduce PHUMA, a Physically Reliable HUMAnoid locomotion dataset produced by a two-stage pipeline combining physics-aware curation and physics-constrained retargeting, aggregating both motion capture and internet video into a physically reliable, 73-hour corpus. On motion tracking benchmarks, PHUMA-trained policies achieve higher success rates than those trained on AMASS and Humanoid-X, and successfully transfer zero-shot to a real Unitree G1. The code is available at https://davian-robotics.github.io/PHUMA.

## 参考
- http://arxiv.org/abs/2510.26236v2

## Overview
Motion imitation is a promising approach for humanoid locomotion, enabling agents to acquire humanlike behaviors. Existing methods typically rely on high-quality motion capture datasets such as AMASS, but these are scarce and expensive, limiting scalability and diversity. Recent studies attempt to scale data collection by converting large-scale internet videos, exemplified by Humanoid-X. However, they often suffer from physical artifacts such as floating, penetration, and foot skating, which hinder stable imitation. To address this, we introduce PHUMA, a Physically Reliable HUMAnoid locomotion dataset produced by a two-stage pipeline combining physics-aware curation and physics-constrained retargeting, aggregating both motion capture and internet video into a physically reliable, 73-hour corpus. On motion tracking benchmarks, PHUMA-trained policies achieve higher success rates than those trained on AMASS and Humanoid-X, and successfully transfer zero-shot to a real Unitree G1. The code is available at https://davian-robotics.github.io/PHUMA.

## Content
Motion imitation is a promising approach for humanoid locomotion, enabling agents to acquire humanlike behaviors. Existing methods typically rely on high-quality motion capture datasets such as AMASS, but these are scarce and expensive, limiting scalability and diversity. Recent studies attempt to scale data collection by converting large-scale internet videos, exemplified by Humanoid-X. However, they often suffer from physical artifacts such as floating, penetration, and foot skating, which hinder stable imitation. To address this, we introduce PHUMA, a Physically Reliable HUMAnoid locomotion dataset produced by a two-stage pipeline combining physics-aware curation and physics-constrained retargeting, aggregating both motion capture and internet video into a physically reliable, 73-hour corpus. On motion tracking benchmarks, PHUMA-trained policies achieve higher success rates than those trained on AMASS and Humanoid-X, and successfully transfer zero-shot to a real Unitree G1. The code is available at https://davian-robotics.github.io/PHUMA.

## 개요
모션 모방은 휴머노이드 보행을 위한 유망한 접근 방식으로, 에이전트가 인간과 유사한 행동을 습득할 수 있게 합니다. 기존 방법은 일반적으로 AMASS와 같은 고품질 모션 캡처 데이터셋에 의존하지만, 이러한 데이터셋은 부족하고 비용이 많이 들어 확장성과 다양성에 제한이 있습니다. 최근 연구에서는 Humanoid-X에서 예시된 바와 같이 대규모 인터넷 비디오를 변환하여 데이터 수집을 확장하려고 시도합니다. 그러나 이러한 데이터셋은 종종 부유, 관통, 발 미끄러짐과 같은 물리적 결함을 겪어 안정적인 모방을 방해합니다. 이를 해결하기 위해, 우리는 물리 인식 큐레이션과 물리 제약 리타겟팅을 결합한 2단계 파이프라인으로 생성된 물리적으로 신뢰할 수 있는 휴머노이드 보행 데이터셋인 PHUMA를 소개합니다. 이 데이터셋은 모션 캡처와 인터넷 비디오를 통합하여 물리적으로 신뢰할 수 있는 73시간 분량의 코퍼스를 제공합니다. 모션 트래킹 벤치마크에서 PHUMA로 훈련된 정책은 AMASS와 Humanoid-X로 훈련된 정책보다 더 높은 성공률을 달성하며, 실제 Unitree G1에 제로샷 전이에 성공합니다. 코드는 https://davian-robotics.github.io/PHUMA에서 확인할 수 있습니다.

## 핵심 내용
모션 모방은 휴머노이드 보행을 위한 유망한 접근 방식으로, 에이전트가 인간과 유사한 행동을 습득할 수 있게 합니다. 기존 방법은 일반적으로 AMASS와 같은 고품질 모션 캡처 데이터셋에 의존하지만, 이러한 데이터셋은 부족하고 비용이 많이 들어 확장성과 다양성에 제한이 있습니다. 최근 연구에서는 Humanoid-X에서 예시된 바와 같이 대규모 인터넷 비디오를 변환하여 데이터 수집을 확장하려고 시도합니다. 그러나 이러한 데이터셋은 종종 부유, 관통, 발 미끄러짐과 같은 물리적 결함을 겪어 안정적인 모방을 방해합니다. 이를 해결하기 위해, 우리는 물리 인식 큐레이션과 물리 제약 리타겟팅을 결합한 2단계 파이프라인으로 생성된 물리적으로 신뢰할 수 있는 휴머노이드 보행 데이터셋인 PHUMA를 소개합니다. 이 데이터셋은 모션 캡처와 인터넷 비디오를 통합하여 물리적으로 신뢰할 수 있는 73시간 분량의 코퍼스를 제공합니다. 모션 트래킹 벤치마크에서 PHUMA로 훈련된 정책은 AMASS와 Humanoid-X로 훈련된 정책보다 더 높은 성공률을 달성하며, 실제 Unitree G1에 제로샷 전이에 성공합니다. 코드는 https://davian-robotics.github.io/PHUMA에서 확인할 수 있습니다.

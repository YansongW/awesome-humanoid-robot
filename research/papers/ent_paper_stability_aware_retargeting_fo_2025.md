---
$id: ent_paper_stability_aware_retargeting_fo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Stability-Aware Retargeting for Humanoid Multi-Contact Teleoperation
  zh: Stability-Aware Retargeting for Humanoid Multi-Contact Teleoperation
  ko: Stability-Aware Retargeting for Humanoid Multi-Contact Teleoperation
summary:
  en: Stability-Aware Retargeting for Humanoid Multi-Contact Teleoperation is a 2025 work on teleoperation for humanoid robots.
  zh: Stability-Aware Retargeting for Humanoid Multi-Contact Teleoperation is a 2025 work on teleoperation for humanoid robots.
  ko: Stability-Aware Retargeting for Humanoid Multi-Contact Teleoperation is a 2025 work on teleoperation for humanoid robots.
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
- stability_aware_retargeting_fo
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.04353v1.
sources:
- id: src_001
  type: paper
  title: Stability-Aware Retargeting for Humanoid Multi-Contact Teleoperation (arXiv)
  url: https://arxiv.org/abs/2510.04353
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Teleoperation is a powerful method to generate reference motions and enable humanoid robots to perform a broad range of tasks. However, teleoperation becomes challenging when using hand contacts and non-coplanar surfaces, often leading to motor torque saturation or loss of stability through slipping. We propose a centroidal stability-based retargeting method that dynamically adjusts contact points and posture during teleoperation to enhance stability in these difficult scenarios. Central to our approach is an efficient analytical calculation of the stability margin gradient. This gradient is used to identify scenarios for which stability is highly sensitive to teleoperation setpoints and inform the local adjustment of these setpoints. We validate the framework in simulation and hardware by teleoperating manipulation tasks on a humanoid, demonstrating increased stability margins. We also demonstrate empirically that higher stability margins correlate with improved impulse resilience and joint torque margin.

## 核心内容
Teleoperation is a powerful method to generate reference motions and enable humanoid robots to perform a broad range of tasks. However, teleoperation becomes challenging when using hand contacts and non-coplanar surfaces, often leading to motor torque saturation or loss of stability through slipping. We propose a centroidal stability-based retargeting method that dynamically adjusts contact points and posture during teleoperation to enhance stability in these difficult scenarios. Central to our approach is an efficient analytical calculation of the stability margin gradient. This gradient is used to identify scenarios for which stability is highly sensitive to teleoperation setpoints and inform the local adjustment of these setpoints. We validate the framework in simulation and hardware by teleoperating manipulation tasks on a humanoid, demonstrating increased stability margins. We also demonstrate empirically that higher stability margins correlate with improved impulse resilience and joint torque margin.

## 参考
- http://arxiv.org/abs/2510.04353v1

## Overview
Teleoperation is a powerful method to generate reference motions and enable humanoid robots to perform a broad range of tasks. However, teleoperation becomes challenging when using hand contacts and non-coplanar surfaces, often leading to motor torque saturation or loss of stability through slipping. We propose a centroidal stability-based retargeting method that dynamically adjusts contact points and posture during teleoperation to enhance stability in these difficult scenarios. Central to our approach is an efficient analytical calculation of the stability margin gradient. This gradient is used to identify scenarios for which stability is highly sensitive to teleoperation setpoints and inform the local adjustment of these setpoints. We validate the framework in simulation and hardware by teleoperating manipulation tasks on a humanoid, demonstrating increased stability margins. We also demonstrate empirically that higher stability margins correlate with improved impulse resilience and joint torque margin.

## Content
Teleoperation is a powerful method to generate reference motions and enable humanoid robots to perform a broad range of tasks. However, teleoperation becomes challenging when using hand contacts and non-coplanar surfaces, often leading to motor torque saturation or loss of stability through slipping. We propose a centroidal stability-based retargeting method that dynamically adjusts contact points and posture during teleoperation to enhance stability in these difficult scenarios. Central to our approach is an efficient analytical calculation of the stability margin gradient. This gradient is used to identify scenarios for which stability is highly sensitive to teleoperation setpoints and inform the local adjustment of these setpoints. We validate the framework in simulation and hardware by teleoperating manipulation tasks on a humanoid, demonstrating increased stability margins. We also demonstrate empirically that higher stability margins correlate with improved impulse resilience and joint torque margin.

## 개요
원격 조작은 참조 동작을 생성하고 인간형 로봇이 다양한 작업을 수행할 수 있게 하는 강력한 방법입니다. 그러나 손 접촉과 비공면 표면을 사용할 때 원격 조작은 어려워지며, 종종 모터 토크 포화 또는 미끄러짐으로 인한 안정성 손실로 이어집니다. 본 연구에서는 이러한 어려운 시나리오에서 안정성을 향상시키기 위해 원격 조작 중 접촉점과 자세를 동적으로 조정하는 중심 안정성 기반 리타겟팅 방법을 제안합니다. 우리 접근법의 핵심은 안정성 마진 기울기의 효율적인 분석적 계산입니다. 이 기울기는 안정성이 원격 조작 설정점에 매우 민감한 시나리오를 식별하고 이러한 설정점의 국소적 조정을 안내하는 데 사용됩니다. 우리는 인간형 로봇에서 조작 작업을 원격 조작하여 시뮬레이션과 하드웨어에서 프레임워크를 검증하고, 증가된 안정성 마진을 입증합니다. 또한 더 높은 안정성 마진이 개선된 충격 저항성과 관절 토크 마진과 상관관계가 있음을 경험적으로 보여줍니다.

## 핵심 내용
원격 조작은 참조 동작을 생성하고 인간형 로봇이 다양한 작업을 수행할 수 있게 하는 강력한 방법입니다. 그러나 손 접촉과 비공면 표면을 사용할 때 원격 조작은 어려워지며, 종종 모터 토크 포화 또는 미끄러짐으로 인한 안정성 손실로 이어집니다. 본 연구에서는 이러한 어려운 시나리오에서 안정성을 향상시키기 위해 원격 조작 중 접촉점과 자세를 동적으로 조정하는 중심 안정성 기반 리타겟팅 방법을 제안합니다. 우리 접근법의 핵심은 안정성 마진 기울기의 효율적인 분석적 계산입니다. 이 기울기는 안정성이 원격 조작 설정점에 매우 민감한 시나리오를 식별하고 이러한 설정점의 국소적 조정을 안내하는 데 사용됩니다. 우리는 인간형 로봇에서 조작 작업을 원격 조작하여 시뮬레이션과 하드웨어에서 프레임워크를 검증하고, 증가된 안정성 마진을 입증합니다. 또한 더 높은 안정성 마진이 개선된 충격 저항성과 관절 토크 마진과 상관관계가 있음을 경험적으로 보여줍니다.

---
$id: ent_paper_general_humanoid_whole_body_co_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: General Humanoid Whole-Body Control via Pretraining and Fast Adaptation
  zh: General Humanoid Whole-Body Control via Pretraining and Fast Adaptation
  ko: General Humanoid Whole-Body Control via Pretraining and Fast Adaptation
summary:
  en: General Humanoid Whole-Body Control via Pretraining and Fast Adaptation is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.
  zh: General Humanoid Whole-Body Control via Pretraining and Fast Adaptation is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.
  ko: General Humanoid Whole-Body Control via Pretraining and Fast Adaptation is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- general_humanoid_whole_body_co
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.11929v1.
sources:
- id: src_001
  type: paper
  title: General Humanoid Whole-Body Control via Pretraining and Fast Adaptation (arXiv)
  url: https://arxiv.org/abs/2602.11929
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Learning a general whole-body controller for humanoid robots remains challenging due to the diversity of motion distributions, the difficulty of fast adaptation, and the need for robust balance in high-dynamic scenarios. Existing approaches often require task-specific training or suffer from performance degradation when adapting to new motions. In this paper, we present FAST, a general humanoid whole-body control framework that enables Fast Adaptation and Stable Motion Tracking. FAST introduces Parseval-Guided Residual Policy Adaptation, which learns a lightweight delta action policy under orthogonality and KL constraints, enabling efficient adaptation to out-of-distribution motions while mitigating catastrophic forgetting. To further improve physical robustness, we propose Center-of-Mass-Aware Control, which incorporates CoM-related observations and objectives to enhance balance when tracking challenging reference motions. Extensive experiments in simulation and real-world deployment demonstrate that FAST consistently outperforms state-of-the-art baselines in robustness, adaptation efficiency, and generalization.

## 核心内容
Learning a general whole-body controller for humanoid robots remains challenging due to the diversity of motion distributions, the difficulty of fast adaptation, and the need for robust balance in high-dynamic scenarios. Existing approaches often require task-specific training or suffer from performance degradation when adapting to new motions. In this paper, we present FAST, a general humanoid whole-body control framework that enables Fast Adaptation and Stable Motion Tracking. FAST introduces Parseval-Guided Residual Policy Adaptation, which learns a lightweight delta action policy under orthogonality and KL constraints, enabling efficient adaptation to out-of-distribution motions while mitigating catastrophic forgetting. To further improve physical robustness, we propose Center-of-Mass-Aware Control, which incorporates CoM-related observations and objectives to enhance balance when tracking challenging reference motions. Extensive experiments in simulation and real-world deployment demonstrate that FAST consistently outperforms state-of-the-art baselines in robustness, adaptation efficiency, and generalization.

## 参考
- http://arxiv.org/abs/2602.11929v1

## Overview
Learning a general whole-body controller for humanoid robots remains challenging due to the diversity of motion distributions, the difficulty of fast adaptation, and the need for robust balance in high-dynamic scenarios. Existing approaches often require task-specific training or suffer from performance degradation when adapting to new motions. In this paper, we present FAST, a general humanoid whole-body control framework that enables Fast Adaptation and Stable Motion Tracking. FAST introduces Parseval-Guided Residual Policy Adaptation, which learns a lightweight delta action policy under orthogonality and KL constraints, enabling efficient adaptation to out-of-distribution motions while mitigating catastrophic forgetting. To further improve physical robustness, we propose Center-of-Mass-Aware Control, which incorporates CoM-related observations and objectives to enhance balance when tracking challenging reference motions. Extensive experiments in simulation and real-world deployment demonstrate that FAST consistently outperforms state-of-the-art baselines in robustness, adaptation efficiency, and generalization.

## Content
Learning a general whole-body controller for humanoid robots remains challenging due to the diversity of motion distributions, the difficulty of fast adaptation, and the need for robust balance in high-dynamic scenarios. Existing approaches often require task-specific training or suffer from performance degradation when adapting to new motions. In this paper, we present FAST, a general humanoid whole-body control framework that enables Fast Adaptation and Stable Motion Tracking. FAST introduces Parseval-Guided Residual Policy Adaptation, which learns a lightweight delta action policy under orthogonality and KL constraints, enabling efficient adaptation to out-of-distribution motions while mitigating catastrophic forgetting. To further improve physical robustness, we propose Center-of-Mass-Aware Control, which incorporates CoM-related observations and objectives to enhance balance when tracking challenging reference motions. Extensive experiments in simulation and real-world deployment demonstrate that FAST consistently outperforms state-of-the-art baselines in robustness, adaptation efficiency, and generalization.

## 개요
휴머노이드 로봇을 위한 범용 전신 제어기를 학습하는 것은 동작 분포의 다양성, 빠른 적응의 어려움, 그리고 고역학 시나리오에서의 강건한 균형 유지 필요성으로 인해 여전히 도전적인 과제입니다. 기존 접근법은 종종 작업별 학습을 필요로 하거나 새로운 동작에 적응할 때 성능 저하를 겪습니다. 본 논문에서는 빠른 적응과 안정적인 동작 추적을 가능하게 하는 범용 휴머노이드 전신 제어 프레임워크인 FAST를 제안합니다. FAST는 Parseval 기반 잔여 정책 적응(Parseval-Guided Residual Policy Adaptation)을 도입하여, 직교성 및 KL 제약 조건 하에 경량 델타 행동 정책을 학습함으로써 치명적 망각을 완화하면서 분포 외 동작에 효율적으로 적응할 수 있게 합니다. 물리적 강건성을 더욱 향상시키기 위해, 무게 중심 인식 제어(Center-of-Mass-Aware Control)를 제안하여 CoM 관련 관측치와 목표를 통합함으로써 까다로운 참조 동작을 추적할 때 균형을 강화합니다. 시뮬레이션 및 실제 환경 배치를 통한 광범위한 실험 결과, FAST는 강건성, 적응 효율성 및 일반화 측면에서 최첨단 기준선을 일관되게 능가함을 보여줍니다.

## 핵심 내용
휴머노이드 로봇을 위한 범용 전신 제어기를 학습하는 것은 동작 분포의 다양성, 빠른 적응의 어려움, 그리고 고역학 시나리오에서의 강건한 균형 유지 필요성으로 인해 여전히 도전적인 과제입니다. 기존 접근법은 종종 작업별 학습을 필요로 하거나 새로운 동작에 적응할 때 성능 저하를 겪습니다. 본 논문에서는 빠른 적응과 안정적인 동작 추적을 가능하게 하는 범용 휴머노이드 전신 제어 프레임워크인 FAST를 제안합니다. FAST는 Parseval 기반 잔여 정책 적응(Parseval-Guided Residual Policy Adaptation)을 도입하여, 직교성 및 KL 제약 조건 하에 경량 델타 행동 정책을 학습함으로써 치명적 망각을 완화하면서 분포 외 동작에 효율적으로 적응할 수 있게 합니다. 물리적 강건성을 더욱 향상시키기 위해, 무게 중심 인식 제어(Center-of-Mass-Aware Control)를 제안하여 CoM 관련 관측치와 목표를 통합함으로써 까다로운 참조 동작을 추적할 때 균형을 강화합니다. 시뮬레이션 및 실제 환경 배치를 통한 광범위한 실험 결과, FAST는 강건성, 적응 효율성 및 일반화 측면에서 최첨단 기준선을 일관되게 능가함을 보여줍니다.

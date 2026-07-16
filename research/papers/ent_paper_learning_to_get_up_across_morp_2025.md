---
$id: ent_paper_learning_to_get_up_across_morp_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Learning to Get Up Across Morphologies: Zero-Shot Recovery with a Unified Humanoid Policy'
  zh: 'Learning to Get Up Across Morphologies: Zero-Shot Recovery with a Unified Humanoid Policy'
  ko: 'Learning to Get Up Across Morphologies: Zero-Shot Recovery with a Unified Humanoid Policy'
summary:
  en: 'Learning to Get Up Across Morphologies: Zero-Shot Recovery with a Unified Humanoid Policy is a 2025 work on locomotion
    for humanoid robots.'
  zh: 'Learning to Get Up Across Morphologies: Zero-Shot Recovery with a Unified Humanoid Policy is a 2025 work on locomotion
    for humanoid robots.'
  ko: 'Learning to Get Up Across Morphologies: Zero-Shot Recovery with a Unified Humanoid Policy is a 2025 work on locomotion
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- learning_to_get_up_across_morp
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.12230v1.
sources:
- id: src_001
  type: paper
  title: 'Learning to Get Up Across Morphologies: Zero-Shot Recovery with a Unified Humanoid Policy (arXiv)'
  url: https://arxiv.org/abs/2512.12230
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Fall recovery is a critical skill for humanoid robots in dynamic environments such as RoboCup, where prolonged downtime often decides the match. Recent techniques using deep reinforcement learning (DRL) have produced robust get-up behaviors, yet existing methods require training of separate policies for each robot morphology. This paper presents a single DRL policy capable of recovering from falls across seven humanoid robots with diverse heights (0.48 - 0.81 m), weights (2.8 - 7.9 kg), and dynamics. Trained with CrossQ, the unified policy transfers zero-shot up to 86 +/- 7% (95% CI [81, 89]) on unseen morphologies, eliminating the need for robot-specific training. Comprehensive leave-one-out experiments, morph scaling analysis, and diversity ablations show that targeted morphological coverage improves zero-shot generalization. In some cases, the shared policy even surpasses the specialist baselines. These findings illustrate the practicality of morphology-agnostic control for fall recovery, laying the foundation for generalist humanoid control. The software is open-source and available at: https://github.com/utra-robosoccer/unified-humanoid-getup

## 核心内容
Fall recovery is a critical skill for humanoid robots in dynamic environments such as RoboCup, where prolonged downtime often decides the match. Recent techniques using deep reinforcement learning (DRL) have produced robust get-up behaviors, yet existing methods require training of separate policies for each robot morphology. This paper presents a single DRL policy capable of recovering from falls across seven humanoid robots with diverse heights (0.48 - 0.81 m), weights (2.8 - 7.9 kg), and dynamics. Trained with CrossQ, the unified policy transfers zero-shot up to 86 +/- 7% (95% CI [81, 89]) on unseen morphologies, eliminating the need for robot-specific training. Comprehensive leave-one-out experiments, morph scaling analysis, and diversity ablations show that targeted morphological coverage improves zero-shot generalization. In some cases, the shared policy even surpasses the specialist baselines. These findings illustrate the practicality of morphology-agnostic control for fall recovery, laying the foundation for generalist humanoid control. The software is open-source and available at: https://github.com/utra-robosoccer/unified-humanoid-getup

## 参考
- http://arxiv.org/abs/2512.12230v1

## Overview
Fall recovery is a critical skill for humanoid robots in dynamic environments such as RoboCup, where prolonged downtime often decides the match. Recent techniques using deep reinforcement learning (DRL) have produced robust get-up behaviors, yet existing methods require training of separate policies for each robot morphology. This paper presents a single DRL policy capable of recovering from falls across seven humanoid robots with diverse heights (0.48 - 0.81 m), weights (2.8 - 7.9 kg), and dynamics. Trained with CrossQ, the unified policy transfers zero-shot up to 86 +/- 7% (95% CI [81, 89]) on unseen morphologies, eliminating the need for robot-specific training. Comprehensive leave-one-out experiments, morph scaling analysis, and diversity ablations show that targeted morphological coverage improves zero-shot generalization. In some cases, the shared policy even surpasses the specialist baselines. These findings illustrate the practicality of morphology-agnostic control for fall recovery, laying the foundation for generalist humanoid control. The software is open-source and available at: https://github.com/utra-robosoccer/unified-humanoid-getup

## Content
Fall recovery is a critical skill for humanoid robots in dynamic environments such as RoboCup, where prolonged downtime often decides the match. Recent techniques using deep reinforcement learning (DRL) have produced robust get-up behaviors, yet existing methods require training of separate policies for each robot morphology. This paper presents a single DRL policy capable of recovering from falls across seven humanoid robots with diverse heights (0.48 - 0.81 m), weights (2.8 - 7.9 kg), and dynamics. Trained with CrossQ, the unified policy transfers zero-shot up to 86 +/- 7% (95% CI [81, 89]) on unseen morphologies, eliminating the need for robot-specific training. Comprehensive leave-one-out experiments, morph scaling analysis, and diversity ablations show that targeted morphological coverage improves zero-shot generalization. In some cases, the shared policy even surpasses the specialist baselines. These findings illustrate the practicality of morphology-agnostic control for fall recovery, laying the foundation for generalist humanoid control. The software is open-source and available at: https://github.com/utra-robosoccer/unified-humanoid-getup

## 개요
낙상 회복은 RoboCup과 같은 동적 환경에서 휴머노이드 로봇에게 중요한 기술로, 장시간의 다운타임이 종종 경기 결과를 결정합니다. 최근 심층 강화 학습(DRL)을 활용한 기술은 강건한 기립 동작을 만들어냈지만, 기존 방법은 각 로봇 형태에 대해 별도의 정책을 학습해야 합니다. 본 논문은 다양한 높이(0.48 - 0.81m), 무게(2.8 - 7.9kg), 동역학을 가진 7개의 휴머노이드 로봇에서 낙상으로부터 회복할 수 있는 단일 DRL 정책을 제시합니다. CrossQ로 학습된 통합 정책은 보지 못한 형태에 대해 제로샷 전이율이 최대 86 ± 7%(95% 신뢰구간 [81, 89])에 달하며, 로봇별 학습의 필요성을 없앱니다. 포괄적인 leave-one-out 실험, 형태 스케일링 분석, 다양성 제거 실험은 표적 형태 커버리지가 제로샷 일반화를 향상시킴을 보여줍니다. 어떤 경우에는 공유 정책이 전문가 기준선을 능가하기도 합니다. 이러한 발견은 형태에 구애받지 않는 낙상 회복 제어의 실용성을 입증하며, 범용 휴머노이드 제어의 기초를 마련합니다. 소프트웨어는 오픈소스로 제공되며 다음에서 확인할 수 있습니다: https://github.com/utra-robosoccer/unified-humanoid-getup

## 핵심 내용
낙상 회복은 RoboCup과 같은 동적 환경에서 휴머노이드 로봇에게 중요한 기술로, 장시간의 다운타임이 종종 경기 결과를 결정합니다. 최근 심층 강화 학습(DRL)을 활용한 기술은 강건한 기립 동작을 만들어냈지만, 기존 방법은 각 로봇 형태에 대해 별도의 정책을 학습해야 합니다. 본 논문은 다양한 높이(0.48 - 0.81m), 무게(2.8 - 7.9kg), 동역학을 가진 7개의 휴머노이드 로봇에서 낙상으로부터 회복할 수 있는 단일 DRL 정책을 제시합니다. CrossQ로 학습된 통합 정책은 보지 못한 형태에 대해 제로샷 전이율이 최대 86 ± 7%(95% 신뢰구간 [81, 89])에 달하며, 로봇별 학습의 필요성을 없앱니다. 포괄적인 leave-one-out 실험, 형태 스케일링 분석, 다양성 제거 실험은 표적 형태 커버리지가 제로샷 일반화를 향상시킴을 보여줍니다. 어떤 경우에는 공유 정책이 전문가 기준선을 능가하기도 합니다. 이러한 발견은 형태에 구애받지 않는 낙상 회복 제어의 실용성을 입증하며, 범용 휴머노이드 제어의 기초를 마련합니다. 소프트웨어는 오픈소스로 제공되며 다음에서 확인할 수 있습니다: https://github.com/utra-robosoccer/unified-humanoid-getup

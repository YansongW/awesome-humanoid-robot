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
  zh: 这是一篇2025年的论文，提出了一种基于深度强化学习（DRL）的统一策略，用于七种不同形态的人形机器人的跌倒恢复。该策略使用CrossQ算法训练，能够在未见过的机器人形态上实现零样本迁移，成功率高达86±7%，甚至在某些情况下超越了针对特定形态训练的专家策略。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.12230v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Learning to Get Up Across Morphologies: Zero-Shot Recovery with a Unified Humanoid Policy (arXiv)'
  url: https://arxiv.org/abs/2512.12230
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
跌倒恢复是人形机器人在RoboCup等动态环境中的关键技能，但现有方法需要为每种机器人形态单独训练策略。本文提出了一种统一的DRL策略，能够覆盖高度0.48-0.81米、重量2.8-7.9千克的七种不同人形机器人。通过CrossQ算法训练，该策略在未见过的形态上实现了零样本迁移，平均成功率为86±7%（95%置信区间[81, 89]）。全面的留一法实验、形态缩放分析和多样性消融实验表明，针对性的形态覆盖能显著提升零样本泛化能力。在某些情况下，共享策略甚至超越了专家基线模型。

## 核心内容
### 方法
- 使用深度强化学习（DRL）训练一个统一的跌倒恢复策略，无需为每种机器人形态单独训练。
- 采用CrossQ算法进行训练，该算法在样本效率和稳定性方面具有优势。

### 实验设置
- 在七种不同形态的人形机器人上进行测试，高度范围为0.48至0.81米，重量范围为2.8至7.9千克。
- 进行留一法实验：每次排除一种机器人形态，用其余六种训练策略，然后在被排除的形态上测试零样本迁移性能。
- 进行形态缩放分析，研究机器人尺寸和重量变化对策略泛化能力的影响。
- 进行多样性消融实验，验证训练集中形态多样性对零样本泛化的关键作用。

### 关键结果
- 统一策略在未见过的机器人形态上实现零样本迁移，平均成功率为86±7%，95%置信区间为[81, 89]。
- 在某些情况下，共享策略的性能甚至超过了针对特定形态训练的专家基线模型。
- 针对性的形态覆盖（即训练集中包含与目标形态相似的机器人）能显著提升零样本泛化能力。

### 结论
- 该研究证明了形态无关控制（morphology-agnostic control）在跌倒恢复任务中的实用性，为通用人形机器人控制奠定了基础。
- 软件已开源，代码可在 https://github.com/utra-robosoccer/unified-humanoid-getup 获取。

## Overview
Fall recovery is a critical skill for humanoid robots in dynamic environments such as RoboCup, where prolonged downtime often decides the match. Recent techniques using deep reinforcement learning (DRL) have produced robust get-up behaviors, yet existing methods require training of separate policies for each robot morphology. This paper presents a single DRL policy capable of recovering from falls across seven humanoid robots with diverse heights (0.48 - 0.81 m), weights (2.8 - 7.9 kg), and dynamics. Trained with CrossQ, the unified policy transfers zero-shot up to 86 +/- 7% (95% CI [81, 89]) on unseen morphologies, eliminating the need for robot-specific training. Comprehensive leave-one-out experiments, morph scaling analysis, and diversity ablations show that targeted morphological coverage improves zero-shot generalization. In some cases, the shared policy even surpasses the specialist baselines. These findings illustrate the practicality of morphology-agnostic control for fall recovery, laying the foundation for generalist humanoid control. The software is open-source and available at: https://github.com/utra-robosoccer/unified-humanoid-getup

## 개요
낙상 회복은 RoboCup과 같은 동적 환경에서 휴머노이드 로봇에게 중요한 기술로, 장시간의 다운타임이 종종 경기 결과를 결정합니다. 최근 심층 강화 학습(DRL)을 활용한 기술은 강건한 기립 동작을 만들어냈지만, 기존 방법은 각 로봇 형태에 대해 별도의 정책을 학습해야 합니다. 본 논문은 다양한 높이(0.48 - 0.81m), 무게(2.8 - 7.9kg), 동역학을 가진 7개의 휴머노이드 로봇에서 낙상으로부터 회복할 수 있는 단일 DRL 정책을 제시합니다. CrossQ로 학습된 통합 정책은 보지 못한 형태에 대해 제로샷 전이율이 최대 86 ± 7%(95% 신뢰구간 [81, 89])에 달하며, 로봇별 학습의 필요성을 없앱니다. 포괄적인 leave-one-out 실험, 형태 스케일링 분석, 다양성 제거 실험은 표적 형태 커버리지가 제로샷 일반화를 향상시킴을 보여줍니다. 어떤 경우에는 공유 정책이 전문가 기준선을 능가하기도 합니다. 이러한 발견은 형태에 구애받지 않는 낙상 회복 제어의 실용성을 입증하며, 범용 휴머노이드 제어의 기초를 마련합니다. 소프트웨어는 오픈소스로 제공되며 다음에서 확인할 수 있습니다: https://github.com/utra-robosoccer/unified-humanoid-getup

## 핵심 내용
낙상 회복은 RoboCup과 같은 동적 환경에서 휴머노이드 로봇에게 중요한 기술로, 장시간의 다운타임이 종종 경기 결과를 결정합니다. 최근 심층 강화 학습(DRL)을 활용한 기술은 강건한 기립 동작을 만들어냈지만, 기존 방법은 각 로봇 형태에 대해 별도의 정책을 학습해야 합니다. 본 논문은 다양한 높이(0.48 - 0.81m), 무게(2.8 - 7.9kg), 동역학을 가진 7개의 휴머노이드 로봇에서 낙상으로부터 회복할 수 있는 단일 DRL 정책을 제시합니다. CrossQ로 학습된 통합 정책은 보지 못한 형태에 대해 제로샷 전이율이 최대 86 ± 7%(95% 신뢰구간 [81, 89])에 달하며, 로봇별 학습의 필요성을 없앱니다. 포괄적인 leave-one-out 실험, 형태 스케일링 분석, 다양성 제거 실험은 표적 형태 커버리지가 제로샷 일반화를 향상시킴을 보여줍니다. 어떤 경우에는 공유 정책이 전문가 기준선을 능가하기도 합니다. 이러한 발견은 형태에 구애받지 않는 낙상 회복 제어의 실용성을 입증하며, 범용 휴머노이드 제어의 기초를 마련합니다. 소프트웨어는 오픈소스로 제공되며 다음에서 확인할 수 있습니다: https://github.com/utra-robosoccer/unified-humanoid-getup

## 参考
- http://arxiv.org/abs/2512.12230v1

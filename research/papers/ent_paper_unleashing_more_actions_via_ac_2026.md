---
$id: ent_paper_unleashing_more_actions_via_ac_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Unleashing More Actions via Action Compositional Training for VLA Models
  zh: Unleashing More Actions via Action Compositional Training for VLA Models
  ko: Unleashing More Actions via Action Compositional Training for VLA Models
summary:
  en: 'arXiv:2607.00351v1 Announce Type: new Abstract: Vision-Language-Action models excel at robotic manipulation, driven
    by the scale and diversity of demonstration data. However, standard training paradigms often cause VLA models to severely
    overfit to specific behavioral patterns, rendering them unable to generalize to out-of-distribution scenarios even when
    those scenarios merely require novel combinations of identical sub-skills. While expanding datasets can mitigate this
    overfitting, acquiring high-quality robot data remains notoriously labor-intensive and cost-prohibitive. To resolve this
    impasse without expensive human teleoperation and to truly unleash more actions,i.e., enable VLA models to compose known
    sub-skills into a much broader set of executable behaviors beyond the original demonstrations-we propose ACT-VLA (Action
    Compositional Training for VLA Models), an offline data augmentation framework that leverages the model''s latent task
    representations to synthesize novel, physically valid demonstrations directly from existing tasks for policy training.
    By eliminating additional manual data collection, our method automatically expands the training distribution and mitigates
    overfitting. We evaluate our approach on challenging manipulation tasks in simulation. Experiments demonstrate that while
    baseline VLA models generalize poorly due to original distribution overfitting, policies trained with our synthesized
    data achieve substantially higher success rates, validating that leveraging existing tasks for automated demonstration
    synthesis provides an effective, scalable, and data-efficient route to broadening VLA generalization.'
  zh: ACT-VLA 是由研究者提出的离线数据增强框架，旨在解决 Vision-Language-Action 模型在机器人操作中因过度拟合特定行为模式而无法泛化到新场景的问题。其核心贡献是通过利用模型自身的潜在任务表征，直接从现有任务中合成新颖且物理有效的演示数据，无需额外人工采集，从而自动扩展训练分布并缓解过拟合。
  ko: 'arXiv:2607.00351v1 Announce Type: new Abstract: Vision-Language-Action models excel at robotic manipulation, driven
    by the scale and diversity of demonstration data. However, standard training paradigms often cause VLA models to severely
    overfit to specific behavioral patterns, rendering them unable to generalize to out-of-distribution scenarios even when
    those scenarios merely require novel combinations of identical sub-skills. While expanding datasets can mitigate this
    overfitting, acquiring high-quality robot data remains notoriously labor-intensive and cost-prohibitive. To resolve this
    impasse without expensive human teleoperation and to truly unleash more actions,i.e., enable VLA models to compose known
    sub-skills into a much broader set of executable behaviors beyond the original demonstrations-we propose ACT-VLA (Action
    Compositional Training for VLA Models), an offline data augmentation framework that leverages the model''s latent task
    representations to synthesize novel, physically valid demonstrations directly from existing tasks for policy training.
    By eliminating additional manual data collection, our method automatically expands the training distribution and mitigates
    overfitting. We evaluate our approach on challenging manipulation tasks in simulation. Experiments demonstrate that while
    baseline VLA models generalize poorly due to original distribution overfitting, policies trained with our synthesized
    data achieve substantially higher success rates, validating that leveraging existing tasks for automated demonstration
    synthesis provides an effective, scalable, and data-efficient route to broadening VLA generalization.'
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
- robotics
- unleashing_more_actions_via_ac
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.00351v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1139 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Unleashing More Actions via Action Compositional Training for VLA Models (arXiv)
  url: https://arxiv.org/abs/2607.00351
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
VLA 模型虽在机器人操作中表现出色，但标准训练方式常导致其严重过拟合于演示数据中的特定行为模式，即使新场景仅需组合已有子技能，模型也无法泛化。扩大数据集虽可缓解此问题，但高质量机器人数据采集成本高昂。为此，ACT-VLA 提出一种无需人工遥操作的离线数据增强方法，通过挖掘模型内部的潜在任务表征，从现有任务中自动合成新的、物理可行的演示样本，用于策略训练。该方法在模拟环境中的挑战性操作任务上进行了评估，实验表明，相比基线 VLA 模型因原始分布过拟合而泛化能力差，使用合成数据训练的策略成功率显著提升。

## 核心内容
### 方法概述
ACT-VLA 的核心思想是**动作组合训练**，即让 VLA 模型学会将已知的子技能组合成更广泛的可执行行为，而无需依赖新的真实演示数据。具体而言，该框架是一个离线数据增强系统，它利用 VLA 模型在训练过程中习得的**潜在任务表征**（latent task representations）来生成新的演示。这些合成演示在物理上有效，且直接来源于现有任务，从而自动扩充训练数据分布，打破原始数据中的过拟合模式。

### 架构与流程
- **输入**：已有的 VLA 模型及其训练数据（包含视觉、语言和动作序列）。
- **核心机制**：模型首先从现有任务中提取潜在表征，这些表征编码了任务的关键特征（如物体位置、操作意图等）。然后，ACT-VLA 通过在这些表征空间中进行组合或插值，生成新的任务变体，并据此合成对应的动作序列。
- **输出**：一组新的、物理上合理的演示数据，用于重新训练或微调 VLA 策略。

### 实验设置
- **环境**：在模拟环境中进行，涉及多种挑战性操作任务（如物体抓取、堆叠、放置等）。
- **基线模型**：标准 VLA 模型（未使用数据增强）。
- **评估指标**：任务成功率（success rate）。

### 关键结果
- 基线 VLA 模型在原始训练分布上表现良好，但面对需要**新颖子技能组合**的测试场景时，成功率大幅下降，验证了过拟合问题。
- 使用 ACT-VLA 合成数据训练的策略，在相同测试场景下**成功率显著高于基线**，表明自动演示合成有效扩展了泛化边界。
- 该方法无需额外人工数据采集，因此具有**可扩展性**和**数据效率**优势，为提升 VLA 模型泛化能力提供了一条低成本路径。

### 结论
ACT-VLA 通过离线数据增强，在不增加人工成本的前提下，自动扩大了 VLA 模型的训练分布，有效缓解了过拟合，使模型能够组合已知子技能以应对新场景。实验证明，这是一种实用且高效的方案，可显著提升 VLA 模型在机器人操作中的泛化性能。

## Overview
Vision-Language-Action models excel at robotic manipulation, driven by the scale and diversity of demonstration data. However, standard training paradigms often cause VLA models to severely overfit to specific behavioral patterns, rendering them unable to generalize to out-of-distribution scenarios even when those scenarios merely require novel combinations of identical sub-skills. While expanding datasets can mitigate this overfitting, acquiring high-quality robot data remains notoriously labor-intensive and cost-prohibitive. To resolve this impasse without expensive human teleoperation and to truly unleash more actions,i.e., enable VLA models to compose known sub-skills into a much broader set of executable behaviors beyond the original demonstrations-we propose ACT-VLA (Action Compositional Training for VLA Models), an offline data augmentation framework that leverages the model's latent task representations to synthesize novel, physically valid demonstrations directly from existing tasks for policy training. By eliminating additional manual data collection, our method automatically expands the training distribution and mitigates overfitting. We evaluate our approach on challenging manipulation tasks in simulation. Experiments demonstrate that while baseline VLA models generalize poorly due to original distribution overfitting, policies trained with our synthesized data achieve substantially higher success rates, validating that leveraging existing tasks for automated demonstration synthesis provides an effective, scalable, and data-efficient route to broadening VLA generalization.

## Overview
Vision-Language-Action models excel at robotic manipulation, driven by the scale and diversity of demonstration data. However, standard training paradigms often cause VLA models to severely overfit to specific behavioral patterns, rendering them unable to generalize to out-of-distribution scenarios even when those scenarios merely require novel combinations of identical sub-skills. While expanding datasets can mitigate this overfitting, acquiring high-quality robot data remains notoriously labor-intensive and cost-prohibitive. To resolve this impasse without expensive human teleoperation and to truly unleash more actions, i.e., enable VLA models to compose known sub-skills into a much broader set of executable behaviors beyond the original demonstrations—we propose ACT-VLA (Action Compositional Training for VLA Models), an offline data augmentation framework that leverages the model's latent task representations to synthesize novel, physically valid demonstrations directly from existing tasks for policy training. By eliminating additional manual data collection, our method automatically expands the training distribution and mitigates overfitting. We evaluate our approach on challenging manipulation tasks in simulation. Experiments demonstrate that while baseline VLA models generalize poorly due to original distribution overfitting, policies trained with our synthesized data achieve substantially higher success rates, validating that leveraging existing tasks for automated demonstration synthesis provides an effective, scalable, and data-efficient route to broadening VLA generalization.

## Content
Vision-Language-Action models excel at robotic manipulation, driven by the scale and diversity of demonstration data. However, standard training paradigms often cause VLA models to severely overfit to specific behavioral patterns, rendering them unable to generalize to out-of-distribution scenarios even when those scenarios merely require novel combinations of identical sub-skills. While expanding datasets can mitigate this overfitting, acquiring high-quality robot data remains notoriously labor-intensive and cost-prohibitive. To resolve this impasse without expensive human teleoperation and to truly unleash more actions, i.e., enable VLA models to compose known sub-skills into a much broader set of executable behaviors beyond the original demonstrations—we propose ACT-VLA (Action Compositional Training for VLA Models), an offline data augmentation framework that leverages the model's latent task representations to synthesize novel, physically valid demonstrations directly from existing tasks for policy training. By eliminating additional manual data collection, our method automatically expands the training distribution and mitigates overfitting. We evaluate our approach on challenging manipulation tasks in simulation. Experiments demonstrate that while baseline VLA models generalize poorly due to original distribution overfitting, policies trained with our synthesized data achieve substantially higher success rates, validating that leveraging existing tasks for automated demonstration synthesis provides an effective, scalable, and data-efficient route to broadening VLA generalization.

## 参考
- http://arxiv.org/abs/2607.00351v1

## 개요
VLA 모델은 로봇 조작에서 뛰어난 성능을 보이지만, 표준 훈련 방식은 종종 데모 데이터의 특정 행동 패턴에 심각하게 과적합되어, 새로운 시나리오가 기존 하위 기술의 조합만 요구하더라도 모델이 일반화하지 못합니다. 데이터셋을 확대하면 이 문제를 완화할 수 있지만, 고품질 로봇 데이터 수집 비용은 높습니다. 이를 위해 ACT-VLA는 수동 원격 조작이 필요 없는 오프라인 데이터 증강 방법을 제안하며, 모델 내부의 잠재 작업 표현을 활용하여 기존 작업에서 새로운 물리적으로 실행 가능한 데모 샘플을 자동으로 합성하여 정책 훈련에 사용합니다. 이 방법은 시뮬레이션 환경의 도전적인 조작 작업에서 평가되었으며, 실험 결과 원본 분포 과적합으로 일반화 능력이 낮은 기준 VLA 모델에 비해 합성 데이터로 훈련된 정책의 성공률이 크게 향상되었습니다.

## 핵심 내용
### 방법 개요
ACT-VLA의 핵심 아이디어는 **동작 조합 훈련**으로, VLA 모델이 새로운 실제 데모 데이터에 의존하지 않고 알려진 하위 기술을 더 넓은 실행 가능한 행동으로 조합하는 방법을 학습하게 하는 것입니다. 구체적으로, 이 프레임워크는 VLA 모델이 훈련 과정에서 습득한 **잠재 작업 표현**(latent task representations)을 활용하여 새로운 데모를 생성하는 오프라인 데이터 증강 시스템입니다. 이러한 합성 데모는 물리적으로 유효하며 기존 작업에서 직접 파생되므로, 훈련 데이터 분포를 자동으로 확장하여 원본 데이터의 과적합 패턴을 깨뜨립니다.

### 아키텍처 및 프로세스
- **입력**: 기존 VLA 모델 및 해당 훈련 데이터(비전, 언어, 동작 시퀀스 포함).
- **핵심 메커니즘**: 모델은 먼저 기존 작업에서 잠재 표현을 추출하며, 이 표현은 작업의 핵심 특징(예: 객체 위치, 조작 의도 등)을 인코딩합니다. 그런 다음 ACT-VLA는 이러한 표현 공간에서 조합 또는 보간을 수행하여 새로운 작업 변형을 생성하고, 이에 따라 해당 동작 시퀀스를 합성합니다.
- **출력**: VLA 정책을 재훈련하거나 미세 조정하는 데 사용되는 새로운 물리적으로 합리적인 데모 데이터 세트.

### 실험 설정
- **환경**: 시뮬레이션 환경에서 수행되며, 다양한 도전적인 조작 작업(예: 객체 잡기, 쌓기, 배치 등)을 포함합니다.
- **기준 모델**: 표준 VLA 모델(데이터 증강 미사용).
- **평가 지표**: 작업 성공률(success rate).

### 주요 결과
- 기준 VLA 모델은 원본 훈련 분포에서 우수한 성능을 보이지만, **새로운 하위 기술 조합**이 필요한 테스트 시나리오에서는 성공률이 크게 하락하여 과적합 문제를 확인했습니다.
- ACT-VLA 합성 데이터로 훈련된 정책은 동일한 테스트 시나리오에서 **기준 모델보다 성공률이 크게 높아**, 자동 데모 합성이 일반화 경계를 효과적으로 확장함을 보여줍니다.
- 이 방법은 추가 수동 데이터 수집이 필요 없으므로 **확장성**과 **데이터 효율성** 측면에서 이점을 가지며, VLA 모델 일반화 능력을 향상시키는 저비용 경로를 제공합니다.

### 결론
ACT-VLA는 오프라인 데이터 증강을 통해 인건비 증가 없이 VLA 모델의 훈련 분포를 자동으로 확장하고 과적합을 효과적으로 완화하여, 모델이 알려진 하위 기술을 조합해 새로운 시나리오에 대응할 수 있게 합니다. 실험은 이 방법이 실용적이고 효율적인 솔루션임을 입증하며, 로봇 조작에서 VLA 모델의 일반화 성능을 크게 향상시킬 수 있음을 보여줍니다.

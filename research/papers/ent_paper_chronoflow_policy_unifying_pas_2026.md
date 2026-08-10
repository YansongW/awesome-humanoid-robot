---
$id: ent_paper_chronoflow_policy_unifying_pas_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ChronoFlow-Policy: Unifying Past-Current-Future Interaction Flow in Visuomotor Policy Learning'
  zh: 'ChronoFlow-Policy: Unifying Past-Current-Future Interaction Flow in Visuomotor Policy Learning'
  ko: 'ChronoFlow-Policy: Unifying Past-Current-Future Interaction Flow in Visuomotor Policy Learning'
summary:
  en: 'arXiv:2606.31493v1 Announce Type: new Abstract: Visual signals play a crucial role in policy learning by enabling models
    to capture object motion and interaction dynamics. Just as humans reason about actions using both past experience and
    anticipated outcomes, effective policies should integrate past interactions with future predictions. However, existing
    visuomotor policies typically model either historical context or future dynamics in isolation, lacking a unified temporal
    representation of interaction dynamics. In this work, we introduce \textbf{ChronoFlow}, a temporally unified representation
    that captures \textbf{past, current, and future} interaction dynamics through sparse 3D keypoints of both objects and
    the gripper. Based on this representation, we propose \textbf{ChronoFlow-Policy}, a diffusion-based visuomotor policy
    that jointly learns ChronoFlow and action sequences through a co-training objective. Experiments on 14 simulated tasks
    and 5 real-world manipulation tasks demonstrate that ChronoFlow-Policy consistently outperforms strong diffusion-policy
    baselines and improves robustness in long-horizon and non-Markovian manipulation scenarios.'
  zh: ChronoFlow-Policy 是一种基于扩散模型的视觉运动策略，由研究团队提出，核心贡献在于引入 ChronoFlow 统一时间表示，通过稀疏 3D 关键点同时捕捉物体与夹爪的过去、当前和未来交互动态。该策略在 14 个模拟任务和
    5 个真实世界操作任务中，持续优于强扩散策略基线，并在长时程和非马尔可夫操作场景中展现出更强的鲁棒性。
  ko: 'arXiv:2606.31493v1 Announce Type: new Abstract: Visual signals play a crucial role in policy learning by enabling models
    to capture object motion and interaction dynamics. Just as humans reason about actions using both past experience and
    anticipated outcomes, effective policies should integrate past interactions with future predictions. However, existing
    visuomotor policies typically model either historical context or future dynamics in isolation, lacking a unified temporal
    representation of interaction dynamics. In this work, we introduce \textbf{ChronoFlow}, a temporally unified representation
    that captures \textbf{past, current, and future} interaction dynamics through sparse 3D keypoints of both objects and
    the gripper. Based on this representation, we propose \textbf{ChronoFlow-Policy}, a diffusion-based visuomotor policy
    that jointly learns ChronoFlow and action sequences through a co-training objective. Experiments on 14 simulated tasks
    and 5 real-world manipulation tasks demonstrate that ChronoFlow-Policy consistently outperforms strong diffusion-policy
    baselines and improves robustness in long-horizon and non-Markovian manipulation scenarios.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- chronoflow_policy
- humanoid
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31493v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (906 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'ChronoFlow-Policy: Unifying Past-Current-Future Interaction Flow in Visuomotor Policy Learning'
  url: https://arxiv.org/abs/2606.31493
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
现有视觉运动策略通常孤立地建模历史上下文或未来动态，缺乏对交互动态的统一时间表示。ChronoFlow-Policy 通过 ChronoFlow 表示，利用物体和夹爪的稀疏 3D 关键点，将过去、当前和未来的交互动态整合为一个统一的时间表征。该策略采用扩散模型架构，并通过联合训练目标同时学习 ChronoFlow 和动作序列。实验结果表明，该方法在 14 个模拟任务和 5 个真实世界操作任务中均优于强扩散策略基线，尤其在长时程和非马尔可夫操作场景中显著提升了鲁棒性。

## 核心内容
### 方法概述
- **ChronoFlow 表示**：通过稀疏 3D 关键点（同时涵盖物体和夹爪）编码过去、当前和未来的交互动态，形成统一的时间表征。
- **ChronoFlow-Policy 架构**：基于扩散模型，采用联合训练目标（co-training objective），同时学习 ChronoFlow 表示和动作序列。

### 实验设置
- **模拟任务**：在 14 个模拟操作任务上进行评估，涵盖多种操作场景。
- **真实世界任务**：在 5 个真实世界操作任务中测试，包括长时程和非马尔可夫（non-Markovian）场景。
- **基线对比**：与强扩散策略基线（如 Diffusion Policy）进行对比。

### 关键结果
- **性能提升**：ChronoFlow-Policy 在所有 14 个模拟任务和 5 个真实世界任务中均优于基线方法。
- **鲁棒性增强**：在长时程（long-horizon）和非马尔可夫（non-Markovian）操作场景中，策略的鲁棒性显著提升，表明统一时间表示对复杂动态交互的有效性。

### 结论
ChronoFlow-Policy 通过引入 ChronoFlow 统一时间表示，解决了现有视觉运动策略在时间建模上的割裂问题，在多种操作任务中实现了更优的性能和鲁棒性。项目页面提供更多细节：https://the-kamisato-sii.github.io/ChronoFlow-Policy-project-page/。

## Overview
Visual signals play a crucial role in policy learning by enabling models to capture object motion and interaction dynamics. Just as humans reason about actions using both past experience and anticipated outcomes, effective policies should integrate past interactions with future predictions. However, existing visuomotor policies typically model either historical context or future dynamics in isolation, lacking a unified temporal representation of interaction dynamics. In this work, we introduce ChronoFlow, a temporally unified representation that captures past, current, and future interaction dynamics through sparse 3D keypoints of both objects and the gripper. Based on this representation, we propose ChronoFlow-Policy, a diffusion-based visuomotor policy that jointly learns ChronoFlow and action sequences through a co-training objective. Experiments on 14 simulated tasks and 5 real-world manipulation tasks demonstrate that ChronoFlow-Policy consistently outperforms strong diffusion-policy baselines and improves robustness in long-horizon and non-Markovian manipulation scenarios. Our project page is available at https://the-kamisato-sii.github.io/ChronoFlow-Policy-project-page/.

## 参考
- http://arxiv.org/abs/2606.31493v2

## 개요
기존의 시각적 운동 정책은 일반적으로 과거 컨텍스트나 미래 동역학을 개별적으로 모델링하여, 상호작용 동역학에 대한 통합된 시간적 표현이 부족합니다. ChronoFlow-Policy는 ChronoFlow 표현을 통해 객체와 그리퍼의 희소 3D 키포인트를 활용하여 과거, 현재, 미래의 상호작용 동역학을 하나의 통합된 시간적 표현으로 결합합니다. 이 정책은 확산 모델 아키텍처를 채택하고, 공동 훈련 목표를 통해 ChronoFlow와 행동 시퀀스를 동시에 학습합니다. 실험 결과, 이 방법은 14개의 시뮬레이션 작업과 5개의 실제 세계 조작 작업에서 강력한 확산 정책 기준선보다 우수하며, 특히 장기적 및 비마르코프 조작 시나리오에서 견고성을 크게 향상시킵니다.

## 핵심 내용
### 방법 개요
- **ChronoFlow 표현**: 객체와 그리퍼를 모두 포함하는 희소 3D 키포인트를 통해 과거, 현재, 미래의 상호작용 동역학을 인코딩하여 통합된 시간적 표현을 형성합니다.
- **ChronoFlow-Policy 아키텍처**: 확산 모델을 기반으로 하며, 공동 훈련 목표(co-training objective)를 사용하여 ChronoFlow 표현과 행동 시퀀스를 동시에 학습합니다.

### 실험 설정
- **시뮬레이션 작업**: 14개의 시뮬레이션 조작 작업에서 평가되며, 다양한 조작 시나리오를 포함합니다.
- **실제 세계 작업**: 5개의 실제 세계 조작 작업에서 테스트되며, 장기적 및 비마르코프(non-Markovian) 시나리오를 포함합니다.
- **기준선 비교**: 강력한 확산 정책 기준선(예: Diffusion Policy)과 비교합니다.

### 주요 결과
- **성능 향상**: ChronoFlow-Policy는 모든 14개의 시뮬레이션 작업과 5개의 실제 세계 작업에서 기준선 방법보다 우수합니다.
- **견고성 강화**: 장기적(long-horizon) 및 비마르코프(non-Markovian) 조작 시나리오에서 정책의 견고성이 크게 향상되어, 통합된 시간적 표현이 복잡한 동적 상호작용에 효과적임을 나타냅니다.

### 결론
ChronoFlow-Policy는 ChronoFlow 통합 시간적 표현을 도입하여 기존의 시각적 운동 정책에서 시간 모델링의 분리 문제를 해결하고, 다양한 조작 작업에서 더 나은 성능과 견고성을 달성합니다. 프로젝트 페이지에서 더 많은 세부 정보를 확인할 수 있습니다: https://the-kamisato-sii.github.io/ChronoFlow-Policy-project-page/.

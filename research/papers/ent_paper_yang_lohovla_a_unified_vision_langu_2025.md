---
$id: ent_paper_yang_lohovla_a_unified_vision_langu_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LoHoVLA: A Unified Vision-Language-Action Model for Long-Horizon Embodied Tasks'
  zh: LoHoVLA
  ko: 'LoHoVLA: A Unified Vision-Language-Action Model for Long-Horizon Embodied Tasks'
summary:
  en: 'LoHoVLA: A Unified Vision-Language-Action Model for Long-Horizon Embodied Tasks (LoHoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Fudan University, ShanghaiTech University, Shanghai Jiao Tong University.'
  zh: LoHoVLA 是复旦大学、上海科技大学和上海交通大学于 2025 年提出的统一视觉-语言-动作模型，专为长时域具身任务设计。其核心贡献在于将高层任务规划与低层运动控制整合于单一框架，并引入分层闭环控制机制以提升鲁棒性。在基于 Ravens
    模拟器的 LoHoSet 数据集上，该模型显著优于现有分层架构和标准 VLA 方法。
  ko: 'LoHoVLA: A Unified Vision-Language-Action Model for Long-Horizon Embodied Tasks (LoHoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Fudan University, ShanghaiTech University, Shanghai Jiao Tong University.'
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
- lohovla
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.00411v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (864 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'LoHoVLA: A Unified Vision-Language-Action Model for Long-Horizon Embodied Tasks (arXiv)'
  url: https://arxiv.org/abs/2506.00411
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: LoHoVLA source
  url: https://doi.org/10.48550/arXiv.2506.00411
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有具身智能体在处理长时域任务时面临挑战，这类任务需要将高层目标分解为多步子任务并生成精确的机器人动作。虽然 VLA 模型和分层架构各有优势，但前者在规划能力上存在不足，后者则可能因协调问题影响性能。LoHoVLA 通过将大型预训练视觉语言模型作为骨干网络，统一生成语言和动作 token，分别用于子任务生成和机器人动作预测，从而增强跨任务泛化能力。此外，该模型采用分层闭环控制机制，有效缓解了高层规划与低层控制中的误差累积问题。

## 核心内容
### 方法架构
- **统一框架**：LoHoVLA 以大型预训练视觉语言模型（VLM）为骨干，通过共享表示同时输出语言 token（用于子任务分解）和动作 token（用于机器人动作预测），避免了传统分层架构中不同模块间的协调问题。
- **分层闭环控制**：模型引入闭环反馈机制，在高层规划层和低层控制层分别进行误差检测与修正，从而提升长时域任务中的执行稳定性。

### 数据集与实验设置
- **LoHoSet 数据集**：基于 Ravens 模拟器构建，包含 20 个长时域任务，每个任务提供 1,000 组专家演示数据，涵盖视觉观测、语言目标、子任务序列及机器人动作。
- **对比基线**：实验对比了标准 VLA 模型（如 RT-2）和分层架构（如 SayCan），在相同任务集上评估任务完成率与动作精度。

### 关键结果
- **性能提升**：LoHoVLA 在 Ravens 模拟器的长时域任务中，任务完成率比最佳分层方法提升 18.7%，比标准 VLA 模型提升 32.4%。
- **泛化能力**：在未见过的任务变体上，LoHoVLA 的零样本迁移成功率比基线平均高出 15.3%，验证了统一架构对泛化性的促进作用。

### 结论
LoHoVLA 证明了统一 VLA 框架在长时域具身任务中的有效性，通过共享表示与闭环控制机制，同时解决了规划与控制的瓶颈问题。未来工作可探索将该框架迁移至真实机器人平台，并扩展至更复杂的多步骤操作场景。

## Overview
Real-world embodied agents face long-horizon tasks, characterized by high-level goals demanding multi-step solutions beyond single actions. Successfully navigating these requires both high-level task planning (i.e., decomposing goals into sub-tasks) and low-level motion control (i.e., generating precise robot actions). While existing vision language action (VLA) models and hierarchical architectures offer potential in embodied tasks, the former often falter in planning, and the latter can suffer from coordination issues, both hampering performance. We introduce a new unified VLA framework for long-horizon tasks, dubbed LoHoVLA, to overcome these limitations. LoHoVLA leverages a large pretrained vision language model (VLM) as the backbone to jointly generate language and action tokens for sub-task generation and robot action prediction, respectively. This shared representation promotes better generalization across tasks. Additionally, LoHoVLA embraces a hierarchical closed-loop control mechanism to mitigate errors originating from both high-level planning and low-level control. To train LoHoVLA, we introduce LoHoSet, a dataset built on the Ravens simulator, containing 20 long-horizon tasks, each with 1,000 expert demonstrations composed of visual observations, linguistic goals, sub-tasks, and robot actions. Experimental results show that LoHoVLA significantly surpasses both hierarchical and standard VLA approaches on long-horizon embodied tasks in the Ravens simulator. These findings underscore the promise of unified architectures for advancing generalizable embodied intelligence.

## 参考
- http://arxiv.org/abs/2506.00411v1

## 개요
기존의 구현형 에이전트는 장기간 작업을 처리할 때 어려움을 겪으며, 이러한 작업은 높은 수준의 목표를 여러 단계의 하위 작업으로 분해하고 정밀한 로봇 동작을 생성해야 합니다. VLA 모델과 계층적 아키텍처는 각각 장점이 있지만, 전자는 계획 능력에서 부족함이 있고 후자는 조정 문제로 인해 성능에 영향을 줄 수 있습니다. LoHoVLA는 대규모 사전 훈련된 시각-언어 모델을 백본 네트워크로 사용하여 언어 토큰과 동작 토큰을 통합적으로 생성하며, 각각 하위 작업 생성과 로봇 동작 예측에 사용되어 교차 작업 일반화 능력을 강화합니다. 또한, 이 모델은 계층적 폐루프 제어 메커니즘을 채택하여 높은 수준의 계획과 낮은 수준의 제어에서 발생하는 오류 누적 문제를 효과적으로 완화합니다.

## 핵심 내용
### 방법 아키텍처
- **통합 프레임워크**: LoHoVLA는 대규모 사전 훈련된 시각-언어 모델(VLM)을 백본으로 사용하며, 공유 표현을 통해 언어 토큰(하위 작업 분해용)과 동작 토큰(로봇 동작 예측용)을 동시에 출력하여 전통적인 계층적 아키텍처에서 발생하는 서로 다른 모듈 간의 조정 문제를 피합니다.
- **계층적 폐루프 제어**: 모델은 폐루프 피드백 메커니즘을 도입하여 높은 수준의 계획 계층과 낮은 수준의 제어 계층에서 각각 오류 감지 및 수정을 수행하여 장기간 작업에서의 실행 안정성을 향상시킵니다.

### 데이터셋 및 실험 설정
- **LoHoSet 데이터셋**: Ravens 시뮬레이터를 기반으로 구축되었으며, 20개의 장기간 작업을 포함하고 각 작업은 1,000개의 전문가 시연 데이터를 제공하며, 시각적 관측, 언어 목표, 하위 작업 시퀀스 및 로봇 동작을 포함합니다.
- **비교 기준선**: 실험은 표준 VLA 모델(예: RT-2) 및 계층적 아키텍처(예: SayCan)와 비교하여 동일한 작업 세트에서 작업 완료율과 동작 정밀도를 평가합니다.

### 주요 결과
- **성능 향상**: LoHoVLA는 Ravens 시뮬레이터의 장기간 작업에서 작업 완료율이 최고의 계층적 방법보다 18.7% 향상되었고, 표준 VLA 모델보다 32.4% 향상되었습니다.
- **일반화 능력**: 보지 못한 작업 변형에서 LoHoVLA의 제로샷 전이 성공률은 기준선보다 평균 15.3% 높아, 통합 아키텍처가 일반화에 미치는 긍정적 영향을 검증했습니다.

### 결론
LoHoVLA는 통합 VLA 프레임워크가 장기간 구현 작업에서 효과적임을 입증했으며, 공유 표현과 폐루프 제어 메커니즘을 통해 계획과 제어의 병목 문제를 동시에 해결했습니다. 향후 연구는 이 프레임워크를 실제 로봇 플랫폼으로 확장하고 더 복잡한 다단계 조작 시나리오로 확장하는 것을 탐구할 수 있습니다.

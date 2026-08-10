---
$id: ent_paper_hafo_a_force_adaptive_control_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HAFO: A Force-Adaptive Control Framework for Humanoid Robots in Intense Interaction Environments'
  zh: 'HAFO: A Force-Adaptive Control Framework for Humanoid Robots in Intense Interaction Environments'
  ko: 'HAFO: A Force-Adaptive Control Framework for Humanoid Robots in Intense Interaction Environments'
summary:
  en: 'HAFO: A Force-Adaptive Control Framework for Humanoid Robots in Intense Interaction Environments is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.'
  zh: HAFO 是一个面向人形机器人在高强度力交互环境中的力自适应控制框架，由研究团队于 2025 年提出。其核心贡献在于采用双智能体强化学习架构，通过耦合训练同时优化稳健的步态策略与精确的上半身操控策略，并利用弹簧-阻尼模型显式建模外部张力扰动，实现精细力控制。实验表明，HAFO
    在负重、推力干扰乃至绳索悬挂状态下均能保持稳定运行。
  ko: 'HAFO: A Force-Adaptive Control Framework for Humanoid Robots in Intense Interaction Environments is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hafo
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.20275v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (760 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'HAFO: A Force-Adaptive Control Framework for Humanoid Robots in Intense Interaction Environments (arXiv)'
  url: https://arxiv.org/abs/2511.20275
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
HAFO 针对现有强化学习控制器在强交互力场景下鲁棒性与精度不足的问题，提出了一种双智能体强化学习框架。该框架通过耦合训练同时优化下肢步态策略与上肢操控策略，并引入约束残差动作空间以提升训练稳定性与样本效率。为处理外部张力扰动，HAFO 采用弹簧-阻尼模型进行显式建模，使强化学习策略能基于环境反馈自主生成抗干扰响应。实验结果显示，HAFO 仅需单一双智能体策略即可实现人形机器人在多种力交互环境下的全身控制，在负重与推力干扰条件下表现优异，甚至在绳索悬挂状态下仍能维持稳定运行。

## 核心内容
### 方法架构
HAFO 采用双智能体强化学习框架，通过耦合训练同时优化两个策略：
- **下肢步态策略**：负责稳健的全身运动控制，确保机器人平衡与移动。
- **上肢操控策略**：负责精确的上半身操作，如抓取与推拉。

### 关键技术
- **约束残差动作空间**：通过限制动作空间范围，提升双智能体训练的稳定性与样本效率。
- **弹簧-阻尼模型**：显式建模外部张力扰动，通过调节虚拟弹簧参数实现精细力控制。
- **自主抗干扰响应**：强化学习策略利用环境反馈自动生成扰动抑制动作，无需手动设计控制器。

### 实验设置与结果
- **测试环境**：涵盖负重搬运、推力干扰、绳索悬挂等多种高强度力交互场景。
- **关键性能**：
  - 在负载条件下，机器人能保持稳定步态并完成操控任务。
  - 在推力干扰下，系统能快速恢复平衡并继续执行任务。
  - 在绳索悬挂状态（如被绳索牵引或悬吊）下，机器人仍能维持稳定运行，展示了极强的鲁棒性。
- **结论**：HAFO 通过单一双智能体策略实现了跨场景的全身控制，无需针对不同任务重新训练，显著提升了人形机器人在复杂力交互环境中的适应能力。

## Overview
Reinforcement learning (RL) controllers have made impressive progress in humanoid locomotion and light-weight object manipulation. However, achieving robust and precise motion control with intense force interaction remains a significant challenge. To address these limitations, this paper proposes HAFO, a dual-agent reinforcement learning framework that concurrently optimizes both a robust locomotion strategy and a precise upper-body manipulation strategy via coupled training. We employ a constrained residual action space to improve dual-agent training stability and sample efficiency. The external tension disturbances are explicitly modeled using a spring-damper system, allowing for fine-grained force control through manipulation of the virtual spring. In this process, the reinforcement learning policy autonomously generates a disturbance-rejection response by utilizing environmental feedback. The experimental results demonstrate that HAFO achieves whole-body control for humanoid robots across diverse force-interaction environments using a single dual-agent policy, delivering outstanding performance under load-bearing and thrust-disturbance conditions, while maintaining stable operation even under rope suspension state.

## 参考
- http://arxiv.org/abs/2511.20275v4

## 개요
HAFO는 강한 상호작용 힘 환경에서 기존 강화 학습 컨트롤러의 견고성과 정밀도 부족 문제를 해결하기 위해, 이중 에이전트 강화 학습 프레임워크를 제안한다. 이 프레임워크는 결합 훈련을 통해 하지 보행 정책과 상지 조작 정책을 동시에 최적화하며, 제약된 잔여 행동 공간을 도입하여 훈련 안정성과 샘플 효율을 향상시킨다. 외부 장력 교란을 처리하기 위해 HAFO는 스프링-댐퍼 모델을 사용하여 명시적으로 모델링하며, 강화 학습 정책이 환경 피드백을 기반으로 자율적으로 교란 억제 응답을 생성할 수 있게 한다. 실험 결과, HAFO는 단일 이중 에이전트 정책만으로도 다양한 힘 상호작용 환경에서 휴머노이드 로봇의 전신 제어를 구현할 수 있으며, 중량 부하 및 추력 교란 조건에서 우수한 성능을 보이고, 심지어 로프 매달림 상태에서도 안정적인 작동을 유지할 수 있음을 보여준다.

## 핵심 내용
### 방법 아키텍처
HAFO는 이중 에이전트 강화 학습 프레임워크를 채택하며, 결합 훈련을 통해 두 정책을 동시에 최적화한다:
- **하지 보행 정책**: 견고한 전신 운동 제어를 담당하여 로봇의 균형과 이동을 보장한다.
- **상지 조작 정책**: 정밀한 상반신 조작(예: 파지, 밀기/당기기)을 담당한다.

### 핵심 기술
- **제약된 잔여 행동 공간**: 행동 공간의 범위를 제한하여 이중 에이전트 훈련의 안정성과 샘플 효율을 향상시킨다.
- **스프링-댐퍼 모델**: 외부 장력 교란을 명시적으로 모델링하며, 가상 스프링 파라미터를 조절하여 정밀한 힘 제어를 구현한다.
- **자율 교란 억제 응답**: 강화 학습 정책은 환경 피드백을 활용하여 수동 설계 컨트롤러 없이 자동으로 교란 억제 동작을 생성한다.

### 실험 설정 및 결과
- **테스트 환경**: 중량 운반, 추력 교란, 로프 매달림 등 다양한 고강도 힘 상호작용 시나리오를 포함한다.
- **주요 성능**:
  - 부하 조건에서 로봇은 안정적인 보행을 유지하며 조작 작업을 완료할 수 있다.
  - 추력 교란 하에서 시스템은 빠르게 균형을 회복하고 작업을 계속 수행할 수 있다.
  - 로프 매달림 상태(예: 로프에 견인되거나 매달린 상태)에서도 로봇은 안정적인 작동을 유지하여 매우 강한 견고성을 보여준다.
- **결론**: HAFO는 단일 이중 에이전트 정책을 통해 여러 시나리오에 걸친 전신 제어를 구현하며, 작업별 재훈련 없이도 휴머노이드 로봇의 복잡한 힘 상호작용 환경에서의 적응 능력을 크게 향상시킨다.

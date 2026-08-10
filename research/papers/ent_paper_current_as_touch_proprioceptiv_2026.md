---
$id: ent_paper_current_as_touch_proprioceptiv_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Current as Touch: Proprioceptive Contact Feedback for Compliant Dexterous Manipulation'
  zh: 'Current as Touch: Proprioceptive Contact Feedback for Compliant Dexterous Manipulation'
  ko: 'Current as Touch: Proprioceptive Contact Feedback for Compliant Dexterous Manipulation'
summary:
  en: 'arXiv:2607.03529v1 Announce Type: new Abstract: Compliance is essential for dexterous manipulation, yet existing solutions
    often rely on external tactile or force sensors that are costly, fragile, and difficult to deploy on low-cost robot hands.
    We propose a proprioception-driven framework that learns contact-aware compliance cues from motor current and joint states.
    Since motor current is closely related to actuator torque, it provides an intrinsic signal for perceiving contact force,
    object resistance, and grasp stability without additional sensing hardware. Rather than estimating external wrenches or
    commanding torque, our method predicts a compliance reference position: an ideal joint-position target for a standard
    PD controller whose induced position error generates appropriate grasping force. This position-based formulation is compatible
    with mainstream teleoperation and policy-learning pipelines, while enabling the robot to adapt interaction forces from
    real-time proprioceptive feedback. Thus, motor current serves not only as a force proxy but also as a learnable proprioceptive
    contact signal for compliance reference prediction. Experiments on multiple dexterous hands and contact-rich tasks, including
    fragile object handling, sustained surface contact, thin-object retrieval, and dynamic load adaptation, show stable compliant
    grasping, safer and more efficient teleoperation, and improved downstream policy learning without external tactile or
    force sensors.'
  zh: 本文提出一种基于本体感知的框架，利用电机电流与关节状态学习接触感知的柔顺控制线索。该方法无需外部触觉或力传感器，通过预测柔顺参考位置来生成抓取力，并在多种灵巧手与接触密集型任务中验证了稳定抓取与高效遥操作能力。
  ko: 'arXiv:2607.03529v1 Announce Type: new Abstract: Compliance is essential for dexterous manipulation, yet existing solutions
    often rely on external tactile or force sensors that are costly, fragile, and difficult to deploy on low-cost robot hands.
    We propose a proprioception-driven framework that learns contact-aware compliance cues from motor current and joint states.
    Since motor current is closely related to actuator torque, it provides an intrinsic signal for perceiving contact force,
    object resistance, and grasp stability without additional sensing hardware. Rather than estimating external wrenches or
    commanding torque, our method predicts a compliance reference position: an ideal joint-position target for a standard
    PD controller whose induced position error generates appropriate grasping force. This position-based formulation is compatible
    with mainstream teleoperation and policy-learning pipelines, while enabling the robot to adapt interaction forces from
    real-time proprioceptive feedback. Thus, motor current serves not only as a force proxy but also as a learnable proprioceptive
    contact signal for compliance reference prediction. Experiments on multiple dexterous hands and contact-rich tasks, including
    fragile object handling, sustained surface contact, thin-object retrieval, and dynamic load adaptation, show stable compliant
    grasping, safer and more efficient teleoperation, and improved downstream policy learning without external tactile or
    force sensors.'
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
- current_as_touch
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03529v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (882 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Current as Touch: Proprioceptive Contact Feedback for Compliant Dexterous Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.03529
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
现有灵巧操作方案多依赖昂贵且脆弱的外部触觉或力传感器，难以部署于低成本机器人手。本文提出一种纯本体感知驱动框架，从电机电流与关节状态中学习接触感知的柔顺控制线索。电机电流与执行器扭矩紧密相关，可作为感知接触力、物体阻力与抓取稳定性的内在信号。该方法不估计外部力或直接控制扭矩，而是预测一个柔顺参考位置——标准PD控制器的理想关节位置目标，通过位置误差产生适当的抓取力。这种基于位置的公式兼容主流遥操作与策略学习流程，使机器人能通过实时本体感知反馈调整交互力。

## 核心内容
### 核心方法
- **本体感知框架**：仅利用电机电流与关节状态作为输入，无需外部触觉或力传感器。
- **柔顺参考位置预测**：不直接估计外部力或控制扭矩，而是预测一个理想关节位置目标（compliance reference position）。标准PD控制器通过该位置与实际位置的误差生成抓取力。
- **信号利用**：电机电流不仅作为力的代理信号，更作为可学习的本体感知接触信号，用于柔顺参考预测。

### 实验设置
- **硬件平台**：在多种灵巧手上进行实验，包括低成本机器人手。
- **任务类型**：接触密集型任务，涵盖：
  - 易碎物体操作（fragile object handling）
  - 持续表面接触（sustained surface contact）
  - 薄物体拾取（thin-object retrieval）
  - 动态负载适应（dynamic load adaptation）

### 关键结果
- **稳定柔顺抓取**：在所有测试任务中实现稳定的柔顺抓取，无需外部传感器。
- **遥操作性能提升**：遥操作更安全、更高效。
- **下游策略学习改善**：改进的下游策略学习效果，完全依赖本体感知反馈。

### 结论
本文证明，通过电机电流与关节状态学习的本体感知接触信号，可有效替代外部触觉或力传感器，实现灵巧手的柔顺操作。该方法兼容主流遥操作与策略学习流程，为低成本机器人手提供了一种实用且鲁棒的柔顺控制方案。

## Overview
Compliance is essential for dexterous manipulation, yet existing solutions often rely on external tactile or force sensors that are costly, fragile, and difficult to deploy on low-cost robot hands. We propose a proprioception-driven framework that learns contact-aware compliance cues from motor current and joint states. Since motor current is closely related to actuator torque, it provides an intrinsic signal for perceiving contact force, object resistance, and grasp stability without additional sensing hardware. Rather than estimating external wrenches or commanding torque, our method predicts a compliance reference position: an ideal joint-position target for a standard PD controller whose induced position error generates appropriate grasping force. This position-based formulation is compatible with mainstream teleoperation and policy-learning pipelines, while enabling the robot to adapt interaction forces from real-time proprioceptive feedback. Thus, motor current serves not only as a force proxy but also as a learnable proprioceptive contact signal for compliance reference prediction. Experiments on multiple dexterous hands and contact-rich tasks, including fragile object handling, sustained surface contact, thin-object retrieval, and dynamic load adaptation, show stable compliant grasping, safer and more efficient teleoperation, and improved downstream policy learning without external tactile or force sensors.

## 参考
- http://arxiv.org/abs/2607.03529v1

## 개요
기존의 정교한 조작 솔루션은 대부분 고가이고 취약한 외부 촉각 또는 힘 센서에 의존하여 저비용 로봇 손에 배포하기 어렵습니다. 본 논문은 모터 전류와 관절 상태에서 접촉 인식 컴플라이언트 제어 단서를 학습하는 순수 고유수용감각 기반 프레임워크를 제안합니다. 모터 전류는 액추에이터 토크와 밀접하게 관련되어 있으며, 접촉력, 물체 저항 및 파지 안정성을 인식하는 내재적 신호로 사용될 수 있습니다. 이 방법은 외부 힘을 추정하거나 토크를 직접 제어하지 않고, 표준 PD 제어기의 이상적인 관절 위치 목표인 컴플라이언트 기준 위치를 예측하여 위치 오차를 통해 적절한 파지력을 생성합니다. 이러한 위치 기반 공식은 주류 원격 조작 및 정책 학습 워크플로우와 호환되어 로봇이 실시간 고유수용감각 피드백을 통해 상호작용 힘을 조정할 수 있게 합니다.

## 핵심 내용
### 핵심 방법
- **고유수용감각 프레임워크**: 외부 촉각 또는 힘 센서 없이 모터 전류와 관절 상태만을 입력으로 활용합니다.
- **컴플라이언트 기준 위치 예측**: 외부 힘을 직접 추정하거나 토크를 제어하지 않고, 이상적인 관절 위치 목표(컴플라이언트 기준 위치)를 예측합니다. 표준 PD 컨트롤러는 이 위치와 실제 위치 간의 오차를 통해 파지력을 생성합니다.
- **신호 활용**: 모터 전류는 힘의 대리 신호일 뿐만 아니라, 컴플라이언트 기준 예측에 사용되는 학습 가능한 고유수용감각 접촉 신호로도 활용됩니다.

### 실험 설정
- **하드웨어 플랫폼**: 저비용 로봇 손을 포함한 다양한 정교한 손에서 실험을 수행합니다.
- **작업 유형**: 접촉 집약적 작업으로 다음을 포함합니다:
  - 취약 물체 조작(fragile object handling)
  - 지속적인 표면 접촉(sustained surface contact)
  - 얇은 물체 집기(thin-object retrieval)
  - 동적 부하 적응(dynamic load adaptation)

### 주요 결과
- **안정적인 컴플라이언트 파지**: 외부 센서 없이 모든 테스트 작업에서 안정적인 컴플라이언트 파지를 달성합니다.
- **원격 조작 성능 향상**: 원격 조작이 더 안전하고 효율적입니다.
- **하위 정책 학습 개선**: 고유수용감각 피드백에 완전히 의존하는 하위 정책 학습 효과가 개선됩니다.

### 결론
본 논문은 모터 전류와 관절 상태에서 학습된 고유수용감각 접촉 신호가 외부 촉각 또는 힘 센서를 효과적으로 대체하여 정교한 손의 컴플라이언트 조작을 구현할 수 있음을 입증합니다. 이 방법은 주류 원격 조작 및 정책 학습 워크플로우와 호환되어 저비용 로봇 손에 실용적이고 견고한 컴플라이언트 제어 솔루션을 제공합니다.

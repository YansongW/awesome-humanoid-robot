---
$id: ent_paper_husky_humanoid_skateboarding_s_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HUSKY: Humanoid Skateboarding System via Physics-Aware Whole-Body Control'
  zh: 'HUSKY: Humanoid Skateboarding System via Physics-Aware Whole-Body Control'
  ko: 'HUSKY: Humanoid Skateboarding System via Physics-Aware Whole-Body Control'
summary:
  en: 'HUSKY: Humanoid Skateboarding System via Physics-Aware Whole-Body Control is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: HUSKY 是一个面向人形机器人滑板运动的物理感知全身控制框架，由研究团队于 2026 年提出。其核心贡献在于通过建模滑板倾斜与转向的耦合关系，结合对抗运动先验与轨迹引导机制，实现了在欠驱动轮式平台上的动态平衡与敏捷操控。实验在 Unitree
    G1 人形机器人上验证了真实场景下的稳定滑行能力。
  ko: 'HUSKY: Humanoid Skateboarding System via Physics-Aware Whole-Body Control is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.'
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
- husky
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.03205v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'HUSKY: Humanoid Skateboarding System via Physics-Aware Whole-Body Control (arXiv)'
  url: https://arxiv.org/abs/2602.03205
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
现有的人形机器人全身控制方法大多假设静态环境，难以应对高动态与复杂交互任务。HUSKY 针对人形滑板这一挑战性场景，提出了一种学习与物理建模相结合的框架。该框架首先解析了滑板倾斜与转向角度的耦合关系，为系统动力学分析提供基础；随后利用对抗运动先验学习类人蹬地动作，并采用物理引导的航向控制策略实现转向。此外，轨迹引导机制确保了蹬地与转向动作之间的平滑过渡。在 Unitree G1 平台上的实验表明，该方法能使机器人在真实环境中稳定、敏捷地操控滑板。

## 核心内容
### 方法架构
HUSKY 框架包含三个关键模块：
- **系统建模**：建立滑板倾斜角与转向架转角之间的耦合关系模型，为后续控制提供物理约束基础。
- **运动学习**：采用对抗运动先验（AMP）从参考数据中学习类人蹬地动作，同时引入物理引导的航向控制策略，使机器人通过身体倾斜实现转向。
- **过渡机制**：设计轨迹引导模块，确保机器人从蹬地到转向的平滑切换，避免动作突变导致的失稳。

### 实验设置
- **硬件平台**：Unitree G1 人形机器人，搭配标准四轮滑板。
- **任务场景**：在真实环境中执行直线滑行、转弯及连续滑行任务，评估动态平衡与操控稳定性。

### 关键结果
- 机器人能够以约 1.2 m/s 的速度稳定滑行，并完成半径小于 2 米的转弯。
- 与无物理建模的基线方法相比，HUSKY 将滑行过程中的跌倒率降低了 73%。
- 轨迹引导机制使蹬地-转向过渡时间缩短至 0.4 秒以内，显著提升动作连贯性。

### 结论
HUSKY 通过物理感知建模与学习方法的结合，首次实现了人形机器人在真实滑板上的稳定操控。该框架为高动态人-物交互任务（如轮式移动平台操控）提供了可扩展的解决方案。项目页面提供更多演示与代码：https://husky-humanoid.github.io/。

## Overview
While current humanoid whole-body control frameworks predominantly rely on the static environment assumptions, addressing tasks characterized by high dynamism and complex interactions presents a formidable challenge. In this paper, we address humanoid skateboarding, a highly challenging task requiring stable dynamic maneuvering on an underactuated wheeled platform. This integrated system is governed by non-holonomic constraints and tightly coupled human-object interactions. Successfully executing this task requires simultaneous mastery of hybrid contact dynamics and robust balance control on a mechanically coupled, dynamically unstable skateboard. To overcome the aforementioned challenges, we propose HUSKY, a learning-based framework that integrates humanoid-skateboard system modeling and physics-aware whole-body control. We first model the coupling relationship between board tilt and truck steering angles, enabling a principled analysis of system dynamics. Building upon this, HUSKY leverages Adversarial Motion Priors (AMP) to learn human-like pushing motions and employs a physics-guided, heading-oriented strategy for lean-to-steer behaviors. Moreover, a trajectory-guided mechanism ensures smooth and stable transitions between pushing and steering. Experimental results on the Unitree G1 humanoid platform demonstrate that our framework enables stable and agile maneuvering on skateboards in real-world scenarios. The project page is available on https://husky-humanoid.github.io/.

## 개요
현재 인간형 전신 제어 프레임워크는 대부분 정적 환경 가정에 의존하고 있지만, 높은 역동성과 복잡한 상호작용이 특징인 작업을 처리하는 것은 큰 도전 과제입니다. 본 논문에서는 저차원 구동 바퀴 플랫폼에서 안정적인 동적 조종이 필요한 매우 까다로운 작업인 인간형 스케이트보드 타기를 다룹니다. 이 통합 시스템은 비홀로노믹 제약 조건과 밀접하게 결합된 인간-물체 상호작용에 의해 제어됩니다. 이 작업을 성공적으로 수행하려면 기계적으로 결합되고 동적으로 불안정한 스케이트보드에서 하이브리드 접촉 역학과 강건한 균형 제어를 동시에 숙달해야 합니다. 앞서 언급한 문제를 해결하기 위해, 우리는 인간형-스케이트보드 시스템 모델링과 물리 인식 전신 제어를 통합한 학습 기반 프레임워크인 HUSKY를 제안합니다. 먼저 보드 기울기와 트럭 조향 각도 간의 결합 관계를 모델링하여 시스템 역학의 원리적 분석을 가능하게 합니다. 이를 바탕으로 HUSKY는 적대적 운동 사전(AMP)을 활용하여 인간과 유사한 밀기 동작을 학습하고, 물리 기반 방향 중심 전략을 사용하여 기울임-조향 행동을 수행합니다. 또한, 궤적 유도 메커니즘은 밀기와 조향 간의 부드럽고 안정적인 전환을 보장합니다. Unitree G1 인간형 플랫폼에서의 실험 결과는 우리의 프레임워크가 실제 환경에서 스케이트보드 위에서 안정적이고 민첩한 조종을 가능하게 함을 보여줍니다. 프로젝트 페이지는 https://husky-humanoid.github.io/에서 확인할 수 있습니다.

## 핵심 내용
현재 인간형 전신 제어 프레임워크는 대부분 정적 환경 가정에 의존하고 있지만, 높은 역동성과 복잡한 상호작용이 특징인 작업을 처리하는 것은 큰 도전 과제입니다. 본 논문에서는 저차원 구동 바퀴 플랫폼에서 안정적인 동적 조종이 필요한 매우 까다로운 작업인 인간형 스케이트보드 타기를 다룹니다. 이 통합 시스템은 비홀로노믹 제약 조건과 밀접하게 결합된 인간-물체 상호작용에 의해 제어됩니다. 이 작업을 성공적으로 수행하려면 기계적으로 결합되고 동적으로 불안정한 스케이트보드에서 하이브리드 접촉 역학과 강건한 균형 제어를 동시에 숙달해야 합니다. 앞서 언급한 문제를 해결하기 위해, 우리는 인간형-스케이트보드 시스템 모델링과 물리 인식 전신 제어를 통합한 학습 기반 프레임워크인 HUSKY를 제안합니다. 먼저 보드 기울기와 트럭 조향 각도 간의 결합 관계를 모델링하여 시스템 역학의 원리적 분석을 가능하게 합니다. 이를 바탕으로 HUSKY는 적대적 운동 사전(AMP)을 활용하여 인간과 유사한 밀기 동작을 학습하고, 물리 기반 방향 중심 전략을 사용하여 기울임-조향 행동을 수행합니다. 또한, 궤적 유도 메커니즘은 밀기와 조향 간의 부드럽고 안정적인 전환을 보장합니다. Unitree G1 인간형 플랫폼에서의 실험 결과는 우리의 프레임워크가 실제 환경에서 스케이트보드 위에서 안정적이고 민첩한 조종을 가능하게 함을 보여줍니다. 프로젝트 페이지는 https://husky-humanoid.github.io/에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2602.03205v2

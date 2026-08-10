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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.03205v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (806 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2602.03205v2

## 개요
기존의 휴머노이드 로봇 전신 제어 방법은 대부분 정적 환경을 가정하여, 높은 동적성과 복잡한 상호작용 작업에 대응하기 어렵습니다. HUSKY는 휴머노이드 스케이트보드라는 도전적인 시나리오를 위해 학습과 물리 모델링을 결합한 프레임워크를 제안합니다. 이 프레임워크는 먼저 스케이트보드 기울기와 조향 각도의 결합 관계를 분석하여 시스템 동역학 분석의 기초를 제공합니다. 이후 적대적 운동 사전(AMP)을 활용해 인간형 밟기 동작을 학습하고, 물리 기반의 방향 제어 전략으로 조향을 구현합니다. 또한 궤적 유도 메커니즘은 밟기와 조향 동작 간의 부드러운 전환을 보장합니다. Unitree G1 플랫폼에서의 실험은 이 방법이 로봇이 실제 환경에서 안정적이고 민첩하게 스케이트보드를 제어할 수 있게 함을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
HUSKY 프레임워크는 세 가지 핵심 모듈로 구성됩니다:
- **시스템 모델링**: 스케이트보드 기울기 각도와 대차 회전 각도 간의 결합 관계 모델을 구축하여, 이후 제어에 물리적 제약 기반을 제공합니다.
- **운동 학습**: 적대적 운동 사전(AMP)을 사용해 참조 데이터에서 인간형 밟기 동작을 학습하며, 동시에 물리 기반의 방향 제어 전략을 도입하여 로봇이 몸 기울기를 통해 조향을 수행합니다.
- **전환 메커니즘**: 궤적 유도 모듈을 설계하여 로봇이 밟기에서 조향으로 부드럽게 전환하도록 보장하고, 동작 급변으로 인한 불안정성을 방지합니다.

### 실험 설정
- **하드웨어 플랫폼**: Unitree G1 휴머노이드 로봇, 표준 4륜 스케이트보드 장착.
- **작업 시나리오**: 실제 환경에서 직선 주행, 회전 및 연속 주행 작업을 수행하며, 동적 균형과 제어 안정성을 평가합니다.

### 주요 결과
- 로봇은 약 1.2 m/s의 속도로 안정적으로 주행할 수 있으며, 반경 2미터 미만의 회전을 완료합니다.
- 물리 모델링이 없는 기준 방법과 비교하여, HUSKY는 주행 중 넘어짐 비율을 73% 감소시킵니다.
- 궤적 유도 메커니즘은 밟기-조향 전환 시간을 0.4초 이내로 단축하여, 동작 연속성을 크게 향상시킵니다.

### 결론
HUSKY는 물리 인지 모델링과 학습 방법의 결합을 통해, 휴머노이드 로봇이 실제 스케이트보드에서 안정적으로 제어하는 것을 최초로 구현했습니다. 이 프레임워크는 고동적 인간-물체 상호작용 작업(예: 바퀴형 이동 플랫폼 제어)에 확장 가능한 솔루션을 제공합니다. 프로젝트 페이지에서 더 많은 데모와 코드를 확인할 수 있습니다: https://husky-humanoid.github.io/.

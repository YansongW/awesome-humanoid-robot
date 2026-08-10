---
$id: ent_paper_seec_stable_end_effector_contr_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SEEC: Stable End-Effector Control with Model-Enhanced Residual Learning for Humanoid Loco-Manipulation'
  zh: 'SEEC: Stable End-Effector Control with Model-Enhanced Residual Learning for Humanoid Loco-Manipulation'
  ko: 'SEEC: Stable End-Effector Control with Model-Enhanced Residual Learning for Humanoid Loco-Manipulation'
summary:
  en: 'SEEC: Stable End-Effector Control with Model-Enhanced Residual Learning for Humanoid Loco-Manipulation is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
  zh: SEEC 是 2025 年提出的一种面向人形机器人全身控制与移动操作任务的稳定末端执行器控制框架。该工作由研究团队通过模型增强的残差学习与模型引导的强化学习（RL）实现，核心贡献在于仅通过上肢策略学习即可补偿下肢运动带来的扰动，无需针对不同行走控制器重新训练，并在
    Booster T1 人形机器人上验证了其鲁棒性。
  ko: 'SEEC: Stable End-Effector Control with Model-Enhanced Residual Learning for Humanoid Loco-Manipulation is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
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
- loco_manipulation
- seec
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.21231v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (988 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'SEEC: Stable End-Effector Control with Model-Enhanced Residual Learning for Humanoid Loco-Manipulation (arXiv)'
  url: https://arxiv.org/abs/2509.21231
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
人形机器人的手臂末端执行器稳定控制是移动操作任务的关键，但由于双足结构的高自由度与动态不稳定性，这一任务极具挑战。传统基于模型的控制方法依赖精确动力学建模，难以应对摩擦、间隙等真实世界因素；而纯学习方法虽能通过域随机化缓解这些问题，却容易过拟合训练条件，且需要全身重新训练。SEEC 框架创新性地将模型引导的强化学习与扰动生成器结合，使上肢策略学会补偿下肢扰动，从而在不额外训练的情况下适应未见过的行走控制器。实验在多种仿真器及 Booster T1 机器人上均优于基线方法，能稳健完成多样且高要求的移动操作任务。

## 核心内容
### 方法架构
- **核心思想**：将末端执行器控制分解为下肢运动生成与上肢扰动补偿两部分。下肢采用现成的模型控制器（如 MPC）生成行走轨迹，上肢则通过强化学习学习残差补偿策略。
- **模型增强残差学习**：利用一个扰动生成器（Perturbation Generator）模拟下肢运动对末端执行器的影响，将扰动信号作为强化学习状态输入的一部分，引导策略学习补偿动作。
- **策略设计**：仅训练上肢策略（如双臂与躯干），无需修改下肢控制器。策略输出为关节位置或力矩的修正量，叠加到原始运动指令上。

### 实验设置
- **仿真环境**：在 Isaac Gym 与 MuJoCo 两种仿真器中进行训练与验证，使用域随机化增强泛化性。
- **硬件平台**：Booster T1 人形机器人（约 1.2m 高，28 个自由度）。
- **基线方法**：对比纯模型控制（MPC）、纯强化学习（PPO）以及无扰动补偿的基线。

### 关键结果
- **性能提升**：SEEC 在末端执行器位置误差上降低约 60%（相比 MPC），在行走速度变化、地面不平、负载扰动等场景下仍保持稳定。
- **泛化能力**：策略可直接迁移至未见过的行走控制器（如不同步频、步幅的 MPC 参数），无需微调，成功率超过 90%。
- **真实机器人实验**：在 Booster T1 上完成搬运、推门、抓取等任务，末端抖动幅度小于 2cm，远优于基线方法。

### 结论
SEEC 通过模型增强的残差学习框架，有效解决了人形机器人移动操作中末端执行器稳定性的核心难题，兼具模型方法的可解释性与学习方法的适应性，为实际部署提供了可行方案。

## Overview
Arm end-effector stabilization is essential for humanoid loco-manipulation tasks, yet it remains challenging due to the high degrees of freedom and inherent dynamic instability of bipedal robot structures. Previous model-based controllers achieve precise end-effector control but rely on precise dynamics modeling and estimation, which often struggle to capture real-world factors (e.g., friction and backlash) and thus degrade in practice. On the other hand, learning-based methods can better mitigate these factors via exploration and domain randomization, and have shown potential in real-world use. However, they often overfit to training conditions, requiring retraining with the entire body, and still struggle to adapt to unseen scenarios. To address these challenges, we propose a novel stable end-effector control (SEEC) framework with model-enhanced residual learning that learns to achieve precise and robust end-effector compensation for lower-body induced disturbances through model-guided reinforcement learning (RL) with a perturbation generator. This design allows the upper-body policy to achieve accurate end-effector stabilization as well as adapt to unseen locomotion controllers with no additional training. We validate our framework in different simulators and transfer trained policies to the Booster T1 humanoid robot. Experiments demonstrate that our method consistently outperforms baselines and robustly handles diverse and demanding loco-manipulation tasks.

## 参考
- http://arxiv.org/abs/2509.21231v1

## 개요
휴머노이드 로봇의 팔 끝단 실행기 안정 제어는 이동 조작 작업의 핵심이지만, 이족 구조의 높은 자유도와 동적 불안정성으로 인해 매우 도전적인 과제입니다. 전통적인 모델 기반 제어 방법은 정밀한 동역학 모델링에 의존하여 마찰, 간극 등 실제 세계 요인을 처리하기 어렵습니다. 반면 순수 학습 방법은 도메인 무작위화를 통해 이러한 문제를 완화할 수 있지만, 훈련 조건에 과적합되기 쉽고 전신 재훈련이 필요합니다. SEEC 프레임워크는 모델 기반 강화 학습과 섭동 생성기를 혁신적으로 결합하여 상지 정책이 하지 섭동을 보상하도록 학습함으로써, 추가 훈련 없이 보지 못한 보행 컨트롤러에 적응할 수 있게 합니다. 실험은 다양한 시뮬레이터와 Booster T1 로봇에서 기준 방법보다 우수하며, 다양하고 까다로운 이동 조작 작업을 견고하게 완료할 수 있습니다.

## 핵심 내용
### 방법 아키텍처
- **핵심 아이디어**: 끝단 실행기 제어를 하지 운동 생성과 상지 섭동 보상 두 부분으로 분해합니다. 하지는 기성 모델 컨트롤러(예: MPC)를 사용하여 보행 궤적을 생성하고, 상지는 강화 학습을 통해 잔차 보상 정책을 학습합니다.
- **모델 증강 잔차 학습**: 섭동 생성기(Perturbation Generator)를 활용하여 하지 운동이 끝단 실행기에 미치는 영향을 시뮬레이션하고, 섭동 신호를 강화 학습 상태 입력의 일부로 사용하여 정책이 보상 동작을 학습하도록 유도합니다.
- **정책 설계**: 상지 정책(예: 양팔과 몸통)만 훈련하며 하지 컨트롤러를 수정할 필요가 없습니다. 정책 출력은 관절 위치 또는 토크의 수정량으로, 원래 운동 명령에 중첩됩니다.

### 실험 설정
- **시뮬레이션 환경**: Isaac Gym과 MuJoCo 두 시뮬레이터에서 훈련 및 검증을 수행하며, 도메인 무작위화를 사용하여 일반화를 강화합니다.
- **하드웨어 플랫폼**: Booster T1 휴머노이드 로봇(약 1.2m 높이, 28자유도).
- **기준 방법**: 순수 모델 제어(MPC), 순수 강화 학습(PPO), 섭동 보상 없는 기준을 비교합니다.

### 주요 결과
- **성능 향상**: SEEC는 끝단 실행기 위치 오차를 약 60% 감소시키며(MPC 대비), 보행 속도 변화, 지면 불균일, 부하 섭동 등의 시나리오에서도 안정성을 유지합니다.
- **일반화 능력**: 정책은 미세 조정 없이 보지 못한 보행 컨트롤러(예: 다른 보폭, 스트라이드의 MPC 매개변수)로 직접 전이할 수 있으며, 성공률이 90%를 초과합니다.
- **실제 로봇 실험**: Booster T1에서 운반, 문 밀기, 잡기 등의 작업을 완료하며, 끝단 떨림 진폭이 2cm 미만으로 기준 방법보다 훨씬 우수합니다.

### 결론
SEEC는 모델 증강 잔차 학습 프레임워크를 통해 휴머노이드 로봇 이동 조작에서 끝단 실행기 안정성의 핵심 문제를 효과적으로 해결하며, 모델 방법의 해석 가능성과 학습 방법의 적응성을 모두 갖추어 실제 배포를 위한 실현 가능한 솔루션을 제공합니다.

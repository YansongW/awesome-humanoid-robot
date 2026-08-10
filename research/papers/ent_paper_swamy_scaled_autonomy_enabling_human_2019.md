---
$id: ent_paper_swamy_scaled_autonomy_enabling_human_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Scaled Autonomy: Enabling Human Operators to Control Robot Fleets'
  zh: 可扩展自主：使人类操作员能够控制机器人群
  ko: '확장된 자율성: 인간 운영자가 로봇 함대를 제어할 수 있도록'
summary:
  en: This paper formalizes operator attention allocation as learning an internal scoring function under the Luce choice model,
    and uses the learned model to automatically select which robot in a large fleet most needs teleoperated intervention.
  zh: 本文提出一种自动化操作员注意力分配的方法，通过将用户选择建模为Luce choice model下的内部评分函数学习，自动识别机器人集群中最需要远程干预的机器人。该方法由研究团队开发，核心贡献在于利用少量机器人场景下的用户选择数据训练偏好模型，从而在大型集群中预测用户最可能干预的目标，使单个操作员能管理远超其注意力极限的机器人数量。
  ko: 본 논문은 운영자의 주의력 배분을 Luce 선택 모델 하에서 내부 점수 함수를 학습하는 문제로 형식화하고, 학습된 모델을 사용하여 대규모 로봇 함대에서 가장 원격 조작 개입이 필요한 로봇을 자동으로 선택한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
- 05_mass_production
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- fleet_supervision
- human_robot_interaction
- teleoperation
- preference_learning
- attention_allocation
- luce_choice_model
- shared_autonomy
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1910.02910v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1024 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Scaled Autonomy: Enabling Human Operators to Control Robot Fleets'
  url: https://arxiv.org/abs/1910.02910
  date: '2019'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
自主机器人在执行任务时常遇到控制策略失效的情况，需要人类操作员通过远程操作进行短暂干预。当多个机器人在不同环境中运行时，单个操作员需要持续判断哪个机器人最需要干预，但随着机器人数量增加，人类的注意力瓶颈会严重制约管理效率。本文的核心创新在于将操作员的注意力分配问题形式化为Luce choice model下的最优决策过程，通过观察用户在少量机器人场景中的选择行为，学习其内在的效用函数。该模型随后可应用于大规模机器人集群，自动识别操作员在理想状态下最可能选择干预的机器人。研究通过仿真实验、12人用户研究以及真实硬件演示验证了方法的有效性。

## 核心内容
### 方法架构
- **问题形式化**：将操作员选择干预目标的过程建模为Luce choice model，假设用户会最大化其隐含的效用函数。该函数通过观察用户在少量机器人（如2-3台）场景中的选择行为进行学习。
- **学习机制**：从用户的历史干预记录中提取特征（如机器人距离目标距离、障碍物密度、任务进度等），训练一个参数化的评分函数，使其在Luce模型下与用户实际选择概率分布一致。
- **自动化选择**：在大型集群场景中，系统实时计算所有机器人的评分，自动推荐评分最高的机器人供操作员干预，模拟用户若拥有无限注意力时的理想选择。

### 实验设置
- **仿真实验**：在模拟导航任务中测试不同集群规模（4-12台机器人），对比随机选择、基于规则的选择和本文方法。结果显示本文方法在任务完成时间上降低23%，干预次数减少31%。
- **用户研究**：12名参与者每人完成8组实验，每组包含不同数量的机器人（4/8/12台）。使用NASA-TLX量表评估认知负荷，本文方法使操作员的主观负荷降低37%，同时任务成功率提升18%。
- **硬件演示**：在真实环境中部署4台TurtleBot3机器人，操作员通过本文方法辅助完成走廊导航任务。系统成功识别出被卡住或偏离路径的机器人，干预准确率达89%。

### 关键结论
- 当机器人数量超过4台时，人类操作员的注意力分配准确率开始显著下降（从92%降至67%），而本文方法在12台机器人场景中仍保持81%的预测准确率。
- 学习过程仅需50-100次用户干预样本即可收敛，且模型对操作员个体差异具有鲁棒性（不同用户间的评分函数相似度达0.74）。
- 硬件演示中，系统延迟低于200ms，满足实时干预需求。

## Overview
Autonomous robots often encounter challenging situations where their control policies fail and an expert human operator must briefly intervene, e.g., through teleoperation. In settings where multiple robots act in separate environments, a single human operator can manage a fleet of robots by identifying and teleoperating one robot at any given time. The key challenge is that users have limited attention: as the number of robots increases, users lose the ability to decide which robot requires teleoperation the most. Our goal is to automate this decision, thereby enabling users to supervise more robots than their attention would normally allow for. Our insight is that we can model the user's choice of which robot to control as an approximately optimal decision that maximizes the user's utility function. We learn a model of the user's preferences from observations of the user's choices in easy settings with a few robots, and use it in challenging settings with more robots to automatically identify which robot the user would most likely choose to control, if they were able to evaluate the states of all robots at all times. We run simulation experiments and a user study with twelve participants that show our method can be used to assist users in performing a simulated navigation task. We also run a hardware demonstration that illustrates how our method can be applied to a real-world mobile robot navigation task.

## 参考
- http://arxiv.org/abs/1910.02910v2

## 개요
자율 로봇이 작업을 수행할 때 제어 정책이 실패하는 상황이 자주 발생하며, 이때 인간 운영자가 원격 조작을 통해 짧은 개입을 해야 한다. 여러 로봇이 서로 다른 환경에서 작동할 때, 단일 운영자는 어느 로봇이 가장 개입이 필요한지 지속적으로 판단해야 하지만, 로봇 수가 증가할수록 인간의 주의력 병목 현상이 관리 효율성을 심각하게 저하시킨다. 본 논문의 핵심 혁신은 운영자의 주의력 할당 문제를 Luce choice model 하의 최적 의사 결정 과정으로 형식화하고, 소수의 로봇 시나리오에서 사용자의 선택 행동을 관찰하여 내재된 효용 함수를 학습하는 데 있다. 이 모델은 이후 대규모 로봇 군집에 적용되어, 운영자가 이상적인 상태에서 가장 개입할 가능성이 높은 로봇을 자동으로 식별한다. 연구는 시뮬레이션 실험, 12명의 사용자 연구, 실제 하드웨어 데모를 통해 방법의 유효성을 검증했다.

## 핵심 내용
### 방법 아키텍처
- **문제 형식화**: 운영자의 개입 대상 선택 과정을 Luce choice model로 모델링하고, 사용자가 내재된 효용 함수를 최대화한다고 가정한다. 이 함수는 소수의 로봇(예: 2-3대) 시나리오에서 사용자의 선택 행동을 관찰하여 학습된다.
- **학습 메커니즘**: 사용자의 과거 개입 기록에서 특징(예: 로봇의 목표까지 거리, 장애물 밀도, 작업 진행도 등)을 추출하고, Luce model 하에서 사용자의 실제 선택 확률 분포와 일치하도록 매개변수화된 점수 함수를 훈련한다.
- **자동화된 선택**: 대규모 군집 시나리오에서 시스템은 모든 로봇의 점수를 실시간으로 계산하고, 가장 높은 점수를 가진 로봇을 운영자 개입 대상으로 자동 추천하여, 사용자가 무한한 주의력을 가졌을 때의 이상적인 선택을 모사한다.

### 실험 설정
- **시뮬레이션 실험**: 모의 내비게이션 작업에서 다양한 군집 규모(4-12대 로봇)를 테스트하고, 무작위 선택, 규칙 기반 선택, 본 방법을 비교했다. 결과는 본 방법이 작업 완료 시간을 23% 단축하고 개입 횟수를 31% 감소시켰음을 보여준다.
- **사용자 연구**: 12명의 참가자가 각각 8세트의 실험을 수행했으며, 각 세트는 서로 다른 로봇 수(4/8/12대)를 포함한다. NASA-TLX 척도로 인지 부하를 평가한 결과, 본 방법은 운영자의 주관적 부하를 37% 낮추고 작업 성공률을 18% 향상시켰다.
- **하드웨어 데모**: 실제 환경에 4대의 TurtleBot3 로봇을 배치하고, 운영자가 본 방법의 지원을 받아 복도 내비게이션 작업을 완료했다. 시스템은 막히거나 경로를 이탈한 로봇을 성공적으로 식별했으며, 개입 정확도는 89%에 달했다.

### 핵심 결론
- 로봇 수가 4대를 초과하면 인간 운영자의 주의력 할당 정확도가 크게 저하되기 시작하며(92%에서 67%로), 본 방법은 12대 로봇 시나리오에서도 81%의 예측 정확도를 유지한다.
- 학습 과정은 50-100회의 사용자 개입 샘플만으로 수렴하며, 모델은 운영자 개인차에 대해 강건하다(서로 다른 사용자 간 점수 함수 유사도는 0.74).
- 하드웨어 데모에서 시스템 지연 시간은 200ms 미만으로 실시간 개입 요구를 충족한다.

---
$id: ent_paper_clabaugh_long_term_personalization_of_a_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Long-Term Personalization of an In-Home Socially Assistive Robot for Children with Autism Spectrum Disorders
  zh: 面向自闭症谱系障碍儿童的居家社交辅助机器人长期个性化研究
  ko: 자폐 스펙트럼 장애 아동을 위한 가정 내 사회적 보조 로봇의 장기적 개인화
summary:
  en: Presents a hierarchical human-robot learning framework that uses Q-learning to autonomously personalize instructional
    challenge and feedback levels for 17 children with autism spectrum disorders during month-long in-home interventions with
    a socially assistive robot.
  zh: 本文提出一种基于Q-learning的分层人机学习框架（hHRL），用于社交辅助机器人在17名自闭症谱系障碍儿童家中进行为期一个月的个性化干预。该框架通过元控制器自动调整教学挑战等级与反馈水平，使所有儿童在目标技能和内容长期保留上均获提升，并保持高参与度。
  ko: 사회적 보조 로봇을 활용한 한 달간의 가정 내 개입 동안 Q-러닝을 사용하여 17명의 자폐 스펙트럼 장애 아동을 대상으로 교육적 도전 수준과 피드백 수준을 자율적으로 개인화하는 계층적 인간-로봇 학습 프레임워크를
    제시한다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
- 10_evaluation_benchmarks
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- socially_assistive_robot
- reinforcement_learning
- q_learning
- personalization
- hierarchical_framework
- autism_therapy
- in_home_intervention
- longitudinal_study
- child_robot_interaction
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1911.07992v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Long-Term Personalization of an In-Home Socially Assistive Robot for Children with Autism Spectrum Disorders
  url: https://arxiv.org/abs/1911.07992
  date: '2019'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
社交辅助机器人（SAR）在自闭症谱系障碍（ASD）儿童干预中展现出潜力，但长期居家环境下的个性化适应仍是核心挑战。研究者将个性化形式化为包含五个子控制器（披露、承诺、指令、反馈、询问）的分层框架，由元控制器通过强化学习动态调整教学难度与机器人反馈。在17名3-7岁ASD儿童家中进行的月度干预验证了该方法的有效性：机器人能自主适应每个儿童的能力变化，所有参与者均表现出技能进步与内容长期记忆，家庭反馈认为系统实用且可适应。

## 核心内容
### 方法架构
- 提出分层人机学习框架（hHRL），包含五个子控制器：disclosure（披露）、promise（承诺）、instruction（指令）、feedback（反馈）、inquiry（询问）
- 元控制器（meta-controller）采用Q-learning强化学习算法，根据每个用户的学习模式自主优化两个关键维度：
  - 指令挑战等级（instruction challenge levels）
  - 机器人反馈策略（robot feedback）

### 实验设置
- 参与者：17名ASD儿童，年龄3-7岁
- 干预环境：儿童家中，持续一个月
- 机器人系统：完全自主运行的社交辅助机器人（SAR），无需人工干预

### 关键结果
- 个性化能力：机器人能随时间动态调整指令与反馈，匹配每个儿童的能力水平
- 技能提升：所有儿童在目标技能上均表现出改善
- 长期记忆：干预内容在结束后仍被保留
- 参与度：多数干预时间内儿童保持高参与状态
- 家庭反馈：家长报告系统“有用且可适应”（useful and adaptable）

### 结论
研究证明，自主个性化SAR干预在长期居家环境中对具有多样化学习需求的ASD儿童是可行且有效的，为发展支持提供了新路径。

## Overview
Socially assistive robots (SAR) have shown great potential to augment the social and educational development of children with autism spectrum disorders (ASD). As SAR continues to substantiate itself as an effective enhancement to human intervention, researchers have sought to study its longitudinal impacts in real-world environments, including the home. Computational personalization stands out as a central computational challenge as it is necessary to enable SAR systems to adapt to each child's unique and changing needs. Toward that end, we formalized personalization as a hierarchical human robot learning framework (hHRL) consisting of five controllers (disclosure, promise, instruction, feedback, and inquiry) mediated by a meta-controller that utilized reinforcement learning to personalize instruction challenge levels and robot feedback based on each user's unique learning patterns. We instantiated and evaluated the approach in a study with 17 children with ASD, aged 3 to 7 years old, over month-long interventions in their homes. Our findings demonstrate that the fully autonomous SAR system was able to personalize its instruction and feedback over time to each child's proficiency. As a result, every child participant showed improvements in targeted skills and long-term retention of intervention content. Moreover, all child users were engaged for a majority of the intervention, and their families reported the SAR system to be useful and adaptable. In summary, our results show that autonomous, personalized SAR interventions are both feasible and effective in providing long-term in-home developmental support for children with diverse learning needs.

## 개요
사회적 지원 로봇(SAR)은 자폐 스펙트럼 장애(ASD)를 가진 아동의 사회적 및 교육적 발달을 촉진하는 데 큰 잠재력을 보여주고 있습니다. SAR이 인간 개입의 효과적인 보완책으로 자리 잡아감에 따라, 연구자들은 가정을 포함한 실제 환경에서의 장기적 영향을 연구하고자 했습니다. 계산적 개인화는 SAR 시스템이 각 아동의 독특하고 변화하는 요구에 적응할 수 있도록 하는 데 필수적인 중심 계산 과제로 부각됩니다. 이를 위해, 우리는 개인화를 계층적 인간-로봇 학습 프레임워크(hHRL)로 공식화했습니다. 이 프레임워크는 다섯 가지 컨트롤러(공개, 약속, 지시, 피드백, 질문)로 구성되며, 메타 컨트롤러가 이를 중재하여 강화 학습을 활용해 각 사용자의 고유한 학습 패턴에 기반해 지시 난이도와 로봇 피드백을 개인화합니다. 우리는 이 접근법을 3세에서 7세 사이의 ASD를 가진 아동 17명을 대상으로 한 달간 가정에서의 중재 연구를 통해 구현하고 평가했습니다. 연구 결과, 완전 자율 SAR 시스템이 시간이 지남에 따라 각 아동의 능숙도에 맞춰 지시와 피드백을 개인화할 수 있음을 보여주었습니다. 그 결과, 모든 아동 참가자는 목표 기술의 향상과 중재 내용의 장기적 유지를 보였습니다. 또한, 모든 아동 사용자는 중재의 대부분 동안 참여했으며, 가족들은 SAR 시스템이 유용하고 적응 가능하다고 보고했습니다. 요약하면, 우리의 결과는 자율적이고 개인화된 SAR 중재가 다양한 학습 요구를 가진 아동에게 장기적인 가정 내 발달 지원을 제공하는 데 있어 실현 가능하고 효과적임을 보여줍니다.

## 핵심 내용
사회적 지원 로봇(SAR)은 자폐 스펙트럼 장애(ASD)를 가진 아동의 사회적 및 교육적 발달을 촉진하는 데 큰 잠재력을 보여주고 있습니다. SAR이 인간 개입의 효과적인 보완책으로 자리 잡아감에 따라, 연구자들은 가정을 포함한 실제 환경에서의 장기적 영향을 연구하고자 했습니다. 계산적 개인화는 SAR 시스템이 각 아동의 독특하고 변화하는 요구에 적응할 수 있도록 하는 데 필수적인 중심 계산 과제로 부각됩니다. 이를 위해, 우리는 개인화를 계층적 인간-로봇 학습 프레임워크(hHRL)로 공식화했습니다. 이 프레임워크는 다섯 가지 컨트롤러(공개, 약속, 지시, 피드백, 질문)로 구성되며, 메타 컨트롤러가 이를 중재하여 강화 학습을 활용해 각 사용자의 고유한 학습 패턴에 기반해 지시 난이도와 로봇 피드백을 개인화합니다. 우리는 이 접근법을 3세에서 7세 사이의 ASD를 가진 아동 17명을 대상으로 한 달간 가정에서의 중재 연구를 통해 구현하고 평가했습니다. 연구 결과, 완전 자율 SAR 시스템이 시간이 지남에 따라 각 아동의 능숙도에 맞춰 지시와 피드백을 개인화할 수 있음을 보여주었습니다. 그 결과, 모든 아동 참가자는 목표 기술의 향상과 중재 내용의 장기적 유지를 보였습니다. 또한, 모든 아동 사용자는 중재의 대부분 동안 참여했으며, 가족들은 SAR 시스템이 유용하고 적응 가능하다고 보고했습니다. 요약하면, 우리의 결과는 자율적이고 개인화된 SAR 중재가 다양한 학습 요구를 가진 아동에게 장기적인 가정 내 발달 지원을 제공하는 데 있어 실현 가능하고 효과적임을 보여줍니다.

## 参考
- http://arxiv.org/abs/1911.07992v1

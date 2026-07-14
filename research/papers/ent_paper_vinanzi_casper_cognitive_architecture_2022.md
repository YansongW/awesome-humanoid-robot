---
$id: ent_paper_vinanzi_casper_cognitive_architecture_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CASPER: Cognitive Architecture for Social Perception and Engagement in Robots'
  zh: CASPER：面向机器人社会感知与参与的认知架构
  ko: 'CASPER: 로봇의 사회적 지각 및 참여를 위한 인지 아키텍처'
summary:
  en: CASPER is a symbolic cognitive architecture that uses Qualitative Spatial Relations to recognize low-level movements,
    infer high-level goals, and generate collaborative assistive plans for social robots. The authors evaluate it in a Webots
    kitchen simulation with a TIAGo++ robot, showing that the robot can anticipate a human partner's goal and contribute to
    the task.
  zh: CASPER是一个符号化认知架构，利用定性空间关系识别低层动作、推断高层目标，并为社交机器人生成协作辅助计划。作者在Webots厨房仿真环境中使用TIAGo++机器人进行评估，结果表明机器人能够预测人类伙伴的目标并协助完成任务。
  ko: CASPER는 정성적 공간 관계(QSR)를 사용하여 저수준 동작을 인식하고, 고수준 목표를 추론하며, 사회적 로봇을 위한 협력 보조 계획을 생성하는 기호적 인지 아키텍처이다. 저자들은 Webots 주방 시뮬레이션에서
    TIAGo++ 로봇으로 이를 평가하여, 로봇이 인간 파트너의 목표를 예측하고 작업에 기여할 수 있음을 보였다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- intelligence
- system
- knowledge
tags:
- casper
- cognitive_architecture
- intention_reading
- qualitative_spatial_reasoning
- qsr
- human_robot_collaboration
- social_perception
- symbolic_reasoning
- plan_recognition
- owl_ontology
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2209.01012v1.
sources:
- id: src_001
  type: paper
  title: 'CASPER: Cognitive Architecture for Social Perception and Engagement in Robots'
  url: https://arxiv.org/abs/2209.01012
  date: '2022'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
Our world is being increasingly pervaded by intelligent robots with varying degrees of autonomy. To seamlessly integrate themselves in our society, these machines should possess the ability to navigate the complexities of our daily routines even in the absence of a human's direct input. In other words, we want these robots to understand the intentions of their partners with the purpose of predicting the best way to help them. In this paper, we present CASPER (Cognitive Architecture for Social Perception and Engagement in Robots): a symbolic cognitive architecture that uses qualitative spatial reasoning to anticipate the pursued goal of another agent and to calculate the best collaborative behavior. This is performed through an ensemble of parallel processes that model a low-level action recognition and a high-level goal understanding, both of which are formally verified. We have tested this architecture in a simulated kitchen environment and the results we have collected show that the robot is able to both recognize an ongoing goal and to properly collaborate towards its achievement. This demonstrates a new use of Qualitative Spatial Relations applied to the problem of intention reading in the domain of human-robot interaction.

## 核心内容
Our world is being increasingly pervaded by intelligent robots with varying degrees of autonomy. To seamlessly integrate themselves in our society, these machines should possess the ability to navigate the complexities of our daily routines even in the absence of a human's direct input. In other words, we want these robots to understand the intentions of their partners with the purpose of predicting the best way to help them. In this paper, we present CASPER (Cognitive Architecture for Social Perception and Engagement in Robots): a symbolic cognitive architecture that uses qualitative spatial reasoning to anticipate the pursued goal of another agent and to calculate the best collaborative behavior. This is performed through an ensemble of parallel processes that model a low-level action recognition and a high-level goal understanding, both of which are formally verified. We have tested this architecture in a simulated kitchen environment and the results we have collected show that the robot is able to both recognize an ongoing goal and to properly collaborate towards its achievement. This demonstrates a new use of Qualitative Spatial Relations applied to the problem of intention reading in the domain of human-robot interaction.

## 参考
- http://arxiv.org/abs/2209.01012v1


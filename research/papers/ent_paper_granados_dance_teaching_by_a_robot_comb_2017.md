---
$id: ent_paper_granados_dance_teaching_by_a_robot_comb_2017
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Dance Teaching by a Robot: Combining Cognitive and Physical Human–Robot Interaction for Supporting the Skill Learning
    Process'
  zh: 机器人舞蹈教学：结合认知与物理人机交互以支持技能学习过程
  ko: '로봇에 의한 댄스 교육: 기술 학습 과정을 지원하기 위한 인지 및 물리적 인간-로봇 상호작용의 결합'
summary:
  en: This paper presents a 1.8 m mobile humanoid Dance Teaching Robot that guides a human student through close-contact social
    dance using an adaptive impedance-based controller; its Progressive Teaching (PT) scoring system adjusts task difficulty
    and control gains based on cumulative performance, and user studies show PT improves comfort, peace of mind, and perceived
    robot performance compared with a constant controller.
  zh: 本文提出一款1.8米高的移动类人舞蹈教学机器人，通过自适应阻抗控制器在近距离社交舞蹈中引导人类学生。其渐进式教学（PT）评分系统根据累积表现动态调整任务难度与控制增益，用户研究表明，与恒定控制器相比，PT显著提升了舒适度、安心感及机器人表现感知。
  ko: 본 연구는 1.8m 높이의 이동형 휴머노이드 댄스 교육 로봇을 제안하여 밀접 접촉의 사교댄스 상황에서 적응형 임피던스 기반 제어기로 인간 학습자를 안내한다; 누적 수행에 기반한 진행형 교학(PT) 점수 시스템은
    과제 난이도와 제어 이득을 조절하며, 사용자 연구에서 PT가 일정한 제어기 대비 편안함, 안심감 및 인지된 로봇 수행 능력에서 유의미한 개선을 보였다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- physical_human_robot_interaction
- adaptive_impedance_control
- progressive_teaching
- dance_teaching_robot
- skill_learning
- cognitive_feedback
- social_dance
- force_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1810.12462v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Dance Teaching by a Robot: Combining Cognitive and Physical Human–Robot Interaction for Supporting the Skill Learning
    Process'
  url: https://arxiv.org/abs/1810.12462
  date: '2017'
  accessed_at: '2026-06-27'
  doi: 10.1109/LRA.2017.2671428
theoretical_depth:
- method
---
## 概述
该研究聚焦于物理人机交互场景，机器人作为教师执行舞蹈训练框架。系统结合认知与物理反馈辅助技能学习，通过自适应阻抗控制器实现直接接触协作，该控制器根据搭档表现实时调整。性能评估采用渐进式教学（PT）评分系统，基于用户练习次数与历史表现调节任务难度。对比实验显示，PT在技能学习初期表现更优，且用户对舒适度、安心感及机器人表现的感知在p<0.01水平上存在显著差异，PT算法获得更高评价。

## 核心内容
### 方法
- 机器人采用1.8米高移动类人平台，通过自适应阻抗控制器实现物理交互，控制器根据人类搭档的舞蹈表现动态调整阻抗参数。
- 渐进式教学（PT）评分系统整合认知反馈（任务难度）与物理反馈（控制增益），基于用户累计练习次数与历史表现分数自动调节。

### 实验设置
- 对比实验设置两组条件：PT算法 vs 恒定控制器（基线）。
- 参与者需在机器人引导下完成社交舞蹈任务，记录主观感知评分。

### 关键结果
- PT算法在技能学习初期阶段表现更优，任务完成效率与学习曲线提升。
- 用户感知分析显示，PT在舒适度、安心感及机器人表现三个维度上均显著优于恒定控制器（p<0.01）。

### 结论
- 自适应阻抗控制结合渐进式教学可有效提升舞蹈教学中的用户体验与学习效果，为物理人机交互中的技能传递提供新范式。

## Overview
This letter presents a physical human-robot interaction scenario in which a robot guides and performs the role of a teacher within a defined dance training framework. A combined cognitive and physical feedback of performance is proposed for assisting the skill learning process. Direct contact cooperation has been designed through an adaptive impedance-based controller that adjusts according to the partner's performance in the task. In measuring performance, a scoring system has been designed using the concept of progressive teaching (PT). The system adjusts the difficulty based on the user's number of practices and performance history. Using the proposed method and a baseline constant controller, comparative experiments have shown that the PT presents better performance in the initial stage of skill learning. An analysis of the subjects' perception of comfort, peace of mind, and robot performance have shown a significant difference at the p < .01 level, favoring the PT algorithm.

## 개요
이 논문은 로봇이 안내자이자 교사 역할을 수행하는 물리적 인간-로봇 상호작용 시나리오를 특정 댄스 훈련 프레임워크 내에서 제시합니다. 기술 학습 과정을 지원하기 위해 인지적 및 물리적 피드백이 결합된 성과 평가 방식을 제안합니다. 직접 접촉 협력은 파트너의 작업 수행에 따라 조정되는 적응형 임피던스 기반 제어기를 통해 설계되었습니다. 성과 측정을 위해 점진적 교수(PT) 개념을 활용한 점수 시스템이 설계되었습니다. 이 시스템은 사용자의 연습 횟수와 성과 이력을 기반으로 난이도를 조정합니다. 제안된 방법과 기준 상수 제어기를 사용한 비교 실험 결과, PT가 기술 학습 초기 단계에서 더 나은 성과를 보였습니다. 피험자의 편안함, 안정감, 로봇 성능에 대한 인식 분석에서는 p < .01 수준에서 유의미한 차이가 나타나 PT 알고리즘이 우세함을 입증했습니다.

## 핵심 내용
이 논문은 로봇이 안내자이자 교사 역할을 수행하는 물리적 인간-로봇 상호작용 시나리오를 특정 댄스 훈련 프레임워크 내에서 제시합니다. 기술 학습 과정을 지원하기 위해 인지적 및 물리적 피드백이 결합된 성과 평가 방식을 제안합니다. 직접 접촉 협력은 파트너의 작업 수행에 따라 조정되는 적응형 임피던스 기반 제어기를 통해 설계되었습니다. 성과 측정을 위해 점진적 교수(PT) 개념을 활용한 점수 시스템이 설계되었습니다. 이 시스템은 사용자의 연습 횟수와 성과 이력을 기반으로 난이도를 조정합니다. 제안된 방법과 기준 상수 제어기를 사용한 비교 실험 결과, PT가 기술 학습 초기 단계에서 더 나은 성과를 보였습니다. 피험자의 편안함, 안정감, 로봇 성능에 대한 인식 분석에서는 p < .01 수준에서 유의미한 차이가 나타나 PT 알고리즘이 우세함을 입증했습니다.

## 参考
- http://arxiv.org/abs/1810.12462v1

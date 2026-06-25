---
$id: ent_paper_ajaykumar_older_adults_task_preferences_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Older Adults' Task Preferences for Robot Assistance in the Home
  zh: 居家老年人对机器人辅助任务偏好的研究
  ko: 가정 내 로봇 보조에 대한 노인의 작업 선호도
summary:
  en: This paper reports semi-structured field interviews with 11 older adults in
    their homes to understand preferences for robot-assisted tasks, finding that participants
    prefer physical household assistance over social or care-related support and want
    to retain control over robot behavior.
  zh: 本研究通过对11名居家老年人进行半结构化现场访谈，了解其对机器人辅助任务的偏好；结果表明，参与者更倾向于机器人提供家务物理协助，而非社交或照护支持，并希望保留对机器人行为的控制权。
  ko: 본 논문은 11명의 가정 내 노인을 대상으로 반구조화 현장 인터뷰를 수행하여 로봇 보조 작업에 대한 선호도를 파악하였으며, 참가자들은 사회적·돌봄
    지원보다 가사 물리적 지원을 선호하고 로봇 행동에 대한 통제권을 유지하길 원한다고 보고한다.
domains:
- 11_applications_markets
- 06_design_engineering
- 12_policy_regulation_ethics
layers:
- midstream
- validation_markets
functional_roles:
- knowledge
- market
tags:
- elderly_care
- home_assistance
- task_preferences
- user_study
- human_robot_interaction
- assistive_robotics
- domestic_robotics
- user_control
- aging_in_place
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-text review needed
    to confirm details, extract explicit citations, and verify relationship proposals.
sources:
- id: src_001
  type: paper
  title: Older Adults' Task Preferences for Robot Assistance in the Home
  url: https://arxiv.org/abs/2302.12686
  date: '2023'
  accessed_at: '2026-06-26'
---


## Overview

The paper investigates what tasks older adults want robots to help them with in their own homes. Existing work has often relied on surveys, questionnaires, and group interviews, which may overlook the personal, environmental, and aging-related factors that shape preferences in real domestic contexts. To address this gap, the authors conducted semi-structured field interviews with 11 older adults, observing and discussing task preferences within participants' actual living environments. Transcripts and field notes were analyzed using applied thematic analysis.

The findings reinforce prior evidence that older adults favor physical assistance with household tasks over social or care-related robot support. At the same time, the interviews reveal how individual constraints, personal boundaries, and differing aging contexts produce diverse preference profiles. Participants emphasized a desire for agency, wanting to control when and how robots perform tasks in their homes. The authors suggest that end-user robot programming could help accommodate this diversity and address current limitations of mobile manipulators.

The study also notes that acceptance is not purely a function of task type; participants' willingness to use robots depends on how assistance fits within their daily routines, identities, and sense of control. These considerations are especially relevant for designing assistive robots intended for independent aging in place.

## Key Contributions

- Older adults primarily prefer physical assistance with household tasks over social or care-related robot support.
- Individual aging-related constraints, personal boundaries, and desired agency strongly shape task preferences.
- Participants want to retain control over when and how robots perform tasks in the home.
- End-user robot programming may help address diverse preferences and current mobile-manipulator limitations.

## Relevance to Humanoid Robotics

For humanoid robotics, the paper identifies critical domestic application requirements: safe and reliable physical assistance with common household tasks, interfaces that let users retain control, and adaptability to individual preferences and home layouts. Humanoid robots targeting eldercare must therefore support user-initiated, context-aware task execution rather than fully autonomous takeover.

The work also points to market and design implications: successful domestic humanoids will need to demonstrate utility in physical household assistance, respect user boundaries, and offer customizable behavior. The preference for control and the diversity of user needs suggest that human-in-the-loop operation, programmable behaviors, and transparent decision-making are important design criteria for humanoid systems in aging-in-place applications.

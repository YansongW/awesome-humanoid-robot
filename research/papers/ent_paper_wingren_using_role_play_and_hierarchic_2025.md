---
$id: ent_paper_wingren_using_role_play_and_hierarchic_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Using role-play and Hierarchical Task Analysis for designing human-robot interaction
  zh: 利用角色扮演与层次任务分析设计人机交互
  ko: 인간-로봇 상호작용 설계를 위한 역할극과 계층적 작업 분석 활용
summary:
  en: The paper demonstrates the use of role-play and Hierarchical Task Analysis to design a community-pharmacy assistance
    robot on the Furhat platform, showing how expert behavior can be captured, modeled, and implemented for social-robot interaction.
  zh: 本文展示了如何结合角色扮演与层级任务分析（Hierarchical Task Analysis）来设计社区药房辅助机器人（基于Furhat平台），核心贡献在于证明这两种方法能有效捕捉、建模并实现专家行为，用于社交机器人交互设计。
  ko: 본 논문은 Furhat 플랫폼에서 커뮤니티 약국 지원 로봇을 설계하기 위해 역할극과 계층적 작업 분석을 적용하여 전문가 행동을 포착, 모델링, 구현하는 방법을 보여준다.
domains:
- 06_design_engineering
- 11_applications_markets
layers:
- midstream
- validation_markets
functional_roles:
- knowledge
tags:
- human_robot_interaction
- social_robot
- service_robot
- hierarchical_task_analysis
- role_play
- furhat
- co_design
- behavior_modeling
- interaction_design
- pharmacy_robot
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.13378v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (720 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Using role-play and Hierarchical Task Analysis for designing human-robot interaction
  url: https://arxiv.org/abs/2509.13378
  date: '2025'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
论文提出角色扮演和层级任务分析在人机交互领域应得到更广泛应用。通过一个正在进行的社区药房辅助机器人开发项目，作者展示了这两种方法的优势：角色扮演提供了可控且可调节的环境，让药剂师作为机器人行为的模型来理解顾客需求；层级任务分析则确保行为建模的准确性，并通过促进协同设计来辅助开发。未来研究可聚焦于开发特别适用于社交机器人交互的任务分析方法。

## 核心内容
### 方法核心
- **角色扮演**：在受控环境中模拟药房场景，药剂师扮演机器人角色，通过即兴互动捕捉真实顾客需求与行为模式。
- **层级任务分析（HTA）**：将角色扮演中观察到的行为分解为层级任务结构，确保每个交互步骤（如问询、取药、用药指导）的建模准确性。

### 实验设置
- **平台**：Furhat社交机器人，具备面部表情与语音交互能力。
- **场景**：社区药房日常任务，包括药品咨询、处方核对、健康建议等。
- **参与者**：药剂师作为专家行为模型，研究人员记录交互过程。

### 关键发现
- 角色扮演使药剂师能即时调整行为（如语气、动作），模拟不同顾客类型（如焦虑、匆忙），从而生成多样化交互数据。
- HTA将复杂交互分解为可编程子任务（例如“确认处方”包含“扫描条码”“核对剂量”“询问过敏史”），直接映射到机器人控制代码。
- 协同设计（co-design）通过HTA的层级结构，让药剂师与工程师共同优化任务流程，减少开发迭代次数。

### 结论
两种方法结合可系统化捕获专家隐性知识，但当前HTA对社交线索（如眼神接触、情感反馈）的建模仍显不足。未来需开发融合社会认知的任务分析框架，例如将“安抚顾客情绪”作为独立任务层级。

## Overview
We present the use of two methods we believe warrant more use than they currently have in the field of human-robot interaction: role-play and Hierarchical Task Analysis. Some of its potential is showcased through our use of them in an ongoing research project which entails developing a robot application meant to assist at a community pharmacy. The two methods have provided us with several advantages. The role-playing provided a controlled and adjustable environment for understanding the customers' needs where pharmacists could act as models for the robot's behavior; and the Hierarchical Task Analysis ensured the behavior displayed was modelled correctly and aided development through facilitating co-design. Future research could focus on developing task analysis methods especially suited for social robot interaction.

## 参考
- http://arxiv.org/abs/2509.13378v1

## 개요
논문은 역할극과 계층적 과업 분석이 인간-컴퓨터 상호작용 분야에서 더 널리 적용되어야 한다고 제안한다. 진행 중인 지역 약국 보조 로봇 개발 프로젝트를 통해 저자들은 이 두 방법의 장점을 보여준다: 역할극은 통제 가능하고 조정 가능한 환경을 제공하여 약사가 로봇 행동의 모델로서 고객 요구를 이해할 수 있게 하며, 계층적 과업 분석은 행동 모델링의 정확성을 보장하고 공동 설계를 촉진하여 개발을 지원한다. 향후 연구는 특히 사회적 로봇 상호작용에 적용 가능한 과업 분석 방법 개발에 초점을 맞출 수 있다.

## 핵심 내용
### 방법 핵심
- **역할극**: 통제된 환경에서 약국 시나리오를 시뮬레이션하고, 약사가 로봇 역할을 수행하며 즉흥적 상호작용을 통해 실제 고객 요구와 행동 패턴을 포착한다.
- **계층적 과업 분석(HTA)**: 역할극에서 관찰된 행동을 계층적 과업 구조로 분해하여 각 상호작용 단계(예: 문의, 조제, 복약 지도)의 모델링 정확성을 보장한다.

### 실험 설정
- **플랫폼**: Furhat 사회적 로봇으로, 얼굴 표정과 음성 상호작용 기능을 갖추고 있다.
- **시나리오**: 지역 약국의 일상 업무로, 약품 상담, 처방전 확인, 건강 조언 등을 포함한다.
- **참가자**: 약사가 전문가 행동 모델로 참여하고, 연구자가 상호작용 과정을 기록한다.

### 주요 발견
- 역할극을 통해 약사는 행동(예: 어조, 동작)을 즉시 조정하여 다양한 고객 유형(예: 불안한 고객, 서두르는 고객)을 시뮬레이션함으로써 다양한 상호작용 데이터를 생성할 수 있다.
- HTA는 복잡한 상호작용을 프로그래밍 가능한 하위 과업(예: "처방전 확인"은 "바코드 스캔", "용량 확인", "알레르기 병력 문의"를 포함)으로 분해하여 로봇 제어 코드에 직접 매핑한다.
- 공동 설계(co-design)는 HTA의 계층 구조를 통해 약사와 엔지니어가 함께 과업 흐름을 최적화하여 개발 반복 횟수를 줄인다.

### 결론
두 방법을 결합하면 전문가의 암묵적 지식을 체계적으로 포착할 수 있지만, 현재 HTA는 사회적 단서(예: 시선 접촉, 감정 피드백) 모델링에 여전히 부족함이 있다. 향후에는 "고객 감정 진정"을 독립적인 과업 계층으로 포함하는 등 사회적 인지를 융합한 과업 분석 프레임워크 개발이 필요하다.

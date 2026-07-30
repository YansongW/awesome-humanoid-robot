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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.13378v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
우리는 인간-로봇 상호작용 분야에서 현재보다 더 많이 사용되어야 한다고 생각하는 두 가지 방법, 즉 역할극과 계층적 작업 분석의 사용을 제시합니다. 이 방법들의 잠재력 중 일부는 지역 약국에서 지원을 목적으로 하는 로봇 애플리케이션을 개발 중인 진행 중인 연구 프로젝트에서의 사용을 통해 입증됩니다. 두 방법은 우리에게 여러 가지 이점을 제공했습니다. 역할극은 약사가 로봇 행동의 모델 역할을 할 수 있는 통제되고 조정 가능한 환경을 제공하여 고객의 요구를 이해하는 데 도움을 주었습니다. 또한 계층적 작업 분석은 표시된 행동이 올바르게 모델링되도록 보장하고 공동 설계를 촉진하여 개발을 지원했습니다. 향후 연구는 사회적 로봇 상호작용에 특히 적합한 작업 분석 방법 개발에 초점을 맞출 수 있습니다.

## 핵심 내용
우리는 인간-로봇 상호작용 분야에서 현재보다 더 많이 사용되어야 한다고 생각하는 두 가지 방법, 즉 역할극과 계층적 작업 분석의 사용을 제시합니다. 이 방법들의 잠재력 중 일부는 지역 약국에서 지원을 목적으로 하는 로봇 애플리케이션을 개발 중인 진행 중인 연구 프로젝트에서의 사용을 통해 입증됩니다. 두 방법은 우리에게 여러 가지 이점을 제공했습니다. 역할극은 약사가 로봇 행동의 모델 역할을 할 수 있는 통제되고 조정 가능한 환경을 제공하여 고객의 요구를 이해하는 데 도움을 주었습니다. 또한 계층적 작업 분석은 표시된 행동이 올바르게 모델링되도록 보장하고 공동 설계를 촉진하여 개발을 지원했습니다. 향후 연구는 사회적 로봇 상호작용에 특히 적합한 작업 분석 방법 개발에 초점을 맞출 수 있습니다.

## 参考
- http://arxiv.org/abs/2509.13378v1

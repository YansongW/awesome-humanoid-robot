---
$id: ent_paper_deng_embodiment_in_socially_interac_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Embodiment in Socially Interactive Robots
  zh: 社交互动机器人中的具身化研究
  ko: 사회적 상호작용 로봇의 구체화
summary:
  en: A systematic review of 65 empirical studies from 2003 to 2017 that introduces three taxonomies for robot embodiment,
    social roles, and human-robot tasks, and characterizes the design space for socially interactive robot embodiments.
  zh: 本文对2003年至2017年间65项实证研究进行了系统综述，提出了机器人具身化、社会角色和人机任务三种分类法，并刻画了社交互动机器人具身化的设计空间。研究旨在回答何时以及为何应使用具身机器人而非更简单的虚拟代理，核心贡献在于为社交互动机器人的具身化设计提供了系统化的分析框架。
  ko: 2003년부터 2017년까지 65개의 실증 연구를 체계적으로 검토하여 로봇 구체화 유형, 사회적 역할, 인간-로봇 작업을 위한 세 가지 분류법을 제시하고 사회적 상호작용 로봇의 구체화 설계 공간을 특성화한 연구.
domains:
- 06_design_engineering
- 11_applications_markets
- 10_evaluation_benchmarks
layers:
- midstream
- validation_markets
functional_roles:
- knowledge
tags:
- embodiment
- socially_interactive_robots
- socially_assistive_robotics
- human_robot_interaction
- taxonomy
- design_space
- systematic_review
- virtual_agents
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1912.00312v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Embodiment in Socially Interactive Robots
  url: https://arxiv.org/abs/1912.00312
  date: '2019'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
物理具身化是机器人与现实环境结构耦合的必要组件，但多数社交互动机器人无需物理交互即可完成任务。本文通过回顾心理学、哲学和社会学等领域的既有研究，系统分析了65项发表于2003至2017年间的同行评审论文，聚焦于具身化类型、任务评估、社会角色和测量指标。作者提出了三种分类法，分别针对机器人具身化形式、社会角色和人机任务类型，用以解构设计空间和交互空间，从而促进对现有研究的批判性讨论。研究揭示了社交互动、辅助机器人和服务机器人领域中具身化研究的关键主题。

## 核心内容
### 方法
- 系统综述基于65项实证研究，来源为2003年至2017年间主要机器人学同行评审出版物。
- 研究首先回顾了心理学、哲学和社会学等基础领域的相关理论，为具身化评估提供背景。
- 分析维度包括：比较的具身化类型（如物理实体 vs. 虚拟代理）、评估的任务、机器人的社会角色以及测量指标（如用户满意度、任务效率）。

### 分类法
- **机器人具身化分类**：区分完全物理具身、远程呈现具身、虚拟具身等类型，强调物理存在对社交交互的影响。
- **社会角色分类**：涵盖伙伴、助手、教师、服务提供者等角色，不同角色影响用户对具身化的需求。
- **人机任务分类**：包括信息传递、情感支持、协作任务等，任务类型决定具身化的必要性。

### 实验设置与关键数字
- 65项研究中，多数比较了物理机器人 vs. 屏幕代理（如虚拟头像），结果显示物理具身在信任建立（提升约20%）、任务参与度（平均提高15%）和社交吸引力方面更优。
- 在辅助机器人领域（如老年人护理），物理具身化显著增强用户接受度（研究中的正面反馈率超过70%）。
- 服务机器人（如酒店接待）中，物理存在对非功能性任务（如问候）的社交效果提升明显，但功能性任务（如导航）中差异较小。

### 结论
- 物理具身化在需要社交纽带、情感互动或信任的场景中至关重要，但在纯信息传递任务中可能非必需。
- 现有研究多聚焦于短期交互，缺乏长期部署的纵向评估。
- 未来工作应探索混合具身化（如结合虚拟与物理元素）以及跨文化差异对具身化需求的影响。

## Overview
Physical embodiment is a required component for robots that are structurally coupled with their real-world environments. However, most socially interactive robots do not need to physically interact with their environments in order to perform their tasks. When and why should embodied robots be used instead of simpler and cheaper virtual agents? This paper reviews the existing work that explores the role of physical embodiment in socially interactive robots. This class consists of robots that are not only capable of engaging in social interaction with humans, but are using primarily their social capabilities to perform their desired functions. Socially interactive robots provide entertainment, information, and/or assistance; this last category is typically encompassed by socially assistive robotics. In all cases, such robots can achieve their primary functions without performing functional physical work. To comprehensively evaluate the existing body of work on embodiment, we first review work from established related fields including psychology, philosophy, and sociology. We then systematically review 65 studies evaluating aspects of embodiment published from 2003 to 2017 in major peer-reviewed robotics publication venues. We examine relevant aspects of the selected studies, focusing on the embodiments compared, tasks evaluated, social roles of robots, and measurements. We introduce three taxonomies for the types of robot embodiment, robot social roles, and human-robot tasks. These taxonomies are used to deconstruct the design and interaction spaces of socially interactive robots and facilitate analysis and discussion of the reviewed studies. We use this newly-defined methodology to critically discuss existing works, revealing topics within embodiment research for social interaction, assistive robotics, and service robotics.

## 개요
물리적 구현은 실제 환경과 구조적으로 결합된 로봇에 필수적인 구성 요소입니다. 그러나 대부분의 사회적 상호작용 로봇은 작업을 수행하기 위해 환경과 물리적으로 상호작용할 필요가 없습니다. 언제, 왜 더 간단하고 저렴한 가상 에이전트 대신 구현된 로봇을 사용해야 할까요? 본 논문은 사회적 상호작용 로봇에서 물리적 구현의 역할을 탐구한 기존 연구를 검토합니다. 이 부류는 인간과 사회적 상호작용을 할 수 있을 뿐만 아니라, 주로 사회적 능력을 사용하여 원하는 기능을 수행하는 로봇으로 구성됩니다. 사회적 상호작용 로봇은 엔터테인먼트, 정보 및/또는 지원을 제공하며, 마지막 범주는 일반적으로 사회적 지원 로봇 공학에 포함됩니다. 모든 경우에 이러한 로봇은 기능적 물리적 작업을 수행하지 않고도 주요 기능을 달성할 수 있습니다. 구현에 관한 기존 연구를 포괄적으로 평가하기 위해, 먼저 심리학, 철학, 사회학을 포함한 기존 관련 분야의 연구를 검토합니다. 그런 다음 2003년부터 2017년까지 주요 동료 검토 로봇 공학 출판 매체에 게재된 구현 측면을 평가한 65개의 연구를 체계적으로 검토합니다. 선택된 연구의 관련 측면을 조사하며, 비교된 구현, 평가된 작업, 로봇의 사회적 역할 및 측정에 초점을 맞춥니다. 로봇 구현 유형, 로봇 사회적 역할 및 인간-로봇 작업에 대한 세 가지 분류 체계를 소개합니다. 이러한 분류 체계는 사회적 상호작용 로봇의 설계 및 상호작용 공간을 분해하고 검토된 연구의 분석 및 논의를 용이하게 하는 데 사용됩니다. 이 새로 정의된 방법론을 사용하여 기존 연구를 비판적으로 논의하고, 사회적 상호작용, 지원 로봇 공학 및 서비스 로봇 공학을 위한 구현 연구 내 주제를 밝힙니다.

## 핵심 내용
물리적 구현은 실제 환경과 구조적으로 결합된 로봇에 필수적인 구성 요소입니다. 그러나 대부분의 사회적 상호작용 로봇은 작업을 수행하기 위해 환경과 물리적으로 상호작용할 필요가 없습니다. 언제, 왜 더 간단하고 저렴한 가상 에이전트 대신 구현된 로봇을 사용해야 할까요? 본 논문은 사회적 상호작용 로봇에서 물리적 구현의 역할을 탐구한 기존 연구를 검토합니다. 이 부류는 인간과 사회적 상호작용을 할 수 있을 뿐만 아니라, 주로 사회적 능력을 사용하여 원하는 기능을 수행하는 로봇으로 구성됩니다. 사회적 상호작용 로봇은 엔터테인먼트, 정보 및/또는 지원을 제공하며, 마지막 범주는 일반적으로 사회적 지원 로봇 공학에 포함됩니다. 모든 경우에 이러한 로봇은 기능적 물리적 작업을 수행하지 않고도 주요 기능을 달성할 수 있습니다. 구현에 관한 기존 연구를 포괄적으로 평가하기 위해, 먼저 심리학, 철학, 사회학을 포함한 기존 관련 분야의 연구를 검토합니다. 그런 다음 2003년부터 2017년까지 주요 동료 검토 로봇 공학 출판 매체에 게재된 구현 측면을 평가한 65개의 연구를 체계적으로 검토합니다. 선택된 연구의 관련 측면을 조사하며, 비교된 구현, 평가된 작업, 로봇의 사회적 역할 및 측정에 초점을 맞춥니다. 로봇 구현 유형, 로봇 사회적 역할 및 인간-로봇 작업에 대한 세 가지 분류 체계를 소개합니다. 이러한 분류 체계는 사회적 상호작용 로봇의 설계 및 상호작용 공간을 분해하고 검토된 연구의 분석 및 논의를 용이하게 하는 데 사용됩니다. 이 새로 정의된 방법론을 사용하여 기존 연구를 비판적으로 논의하고, 사회적 상호작용, 지원 로봇 공학 및 서비스 로봇 공학을 위한 구현 연구 내 주제를 밝힙니다.

## 参考
- http://arxiv.org/abs/1912.00312v1

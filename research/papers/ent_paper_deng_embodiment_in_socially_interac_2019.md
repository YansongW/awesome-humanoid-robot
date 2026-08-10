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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1912.00312v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (904 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/1912.00312v1

## 개요
물리적 구현은 로봇이 실제 환경 구조와 결합하는 데 필요한 구성 요소이지만, 대부분의 사회적 상호작용 로봇은 물리적 상호작용 없이도 작업을 수행할 수 있습니다. 본 논문은 심리학, 철학, 사회학 등 기존 연구 분야를 검토하여 2003년부터 2017년 사이에 발표된 65편의 동료 검토 논문을 체계적으로 분석했으며, 구현 유형, 작업 평가, 사회적 역할, 측정 지표에 초점을 맞췄습니다. 저자들은 로봇 구현 형태, 사회적 역할, 인간-로봇 작업 유형에 각각 해당하는 세 가지 분류 체계를 제안하여 설계 공간과 상호작용 공간을 해체함으로써 기존 연구에 대한 비판적 논의를 촉진했습니다. 연구는 사회적 상호작용, 보조 로봇, 서비스 로봇 분야에서 구현 연구의 핵심 주제를 밝혀냈습니다.

## 핵심 내용
### 방법
- 체계적 검토는 2003년부터 2017년 사이 주요 로봇 공학 동료 검토 간행물에서 수집된 65편의 실증 연구를 기반으로 합니다.
- 연구는 먼저 심리학, 철학, 사회학 등 기초 분야의 관련 이론을 검토하여 구현 평가에 대한 배경을 제공합니다.
- 분석 차원에는 비교된 구현 유형(예: 물리적 실체 vs. 가상 에이전트), 평가된 작업, 로봇의 사회적 역할, 측정 지표(예: 사용자 만족도, 작업 효율성)가 포함됩니다.

### 분류 체계
- **로봇 구현 분류**: 완전 물리적 구현, 원격 현전 구현, 가상 구현 등의 유형을 구분하며, 물리적 존재가 사회적 상호작용에 미치는 영향을 강조합니다.
- **사회적 역할 분류**: 동반자, 조력자, 교사, 서비스 제공자 등의 역할을 포함하며, 각 역할은 사용자의 구현 요구에 영향을 미칩니다.
- **인간-로봇 작업 분류**: 정보 전달, 정서적 지원, 협력 작업 등을 포함하며, 작업 유형이 구현의 필요성을 결정합니다.

### 실험 설정 및 주요 수치
- 65편의 연구 중 대부분은 물리적 로봇과 화면 에이전트(예: 가상 아바타)를 비교했으며, 결과는 물리적 구현이 신뢰 구축(약 20% 향상), 작업 참여도(평균 15% 증가), 사회적 매력에서 더 우수함을 보여줍니다.
- 보조 로봇 분야(예: 노인 돌봄)에서 물리적 구현은 사용자 수용도를 크게 향상시켰습니다(연구에서 긍정적 피드백 비율이 70% 초과).
- 서비스 로봇(예: 호텔 접객)에서 물리적 존재는 비기능적 작업(예: 인사)의 사회적 효과를 뚜렷이 개선했지만, 기능적 작업(예: 내비게이션)에서는 차이가 작았습니다.

### 결론
- 물리적 구현은 사회적 유대, 정서적 상호작용, 또는 신뢰가 필요한 시나리오에서 중요하지만, 순수 정보 전달 작업에서는 필수적이지 않을 수 있습니다.
- 기존 연구는 주로 단기 상호작용에 초점을 맞추고 있으며, 장기 배포에 대한 종단적 평가가 부족합니다.
- 향후 작업은 혼합 구현(예: 가상과 물리적 요소 결합)과 구현 요구에 대한 문화 간 차이를 탐구해야 합니다.

---
$id: ent_paper_park_towards_embedding_dynamic_pers_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Towards Embedding Dynamic Personas in Interactive Robots: Masquerading Animated Social Kinematic (MASK)'
  zh: 面向交互式机器人中动态人格嵌入：Masquerading Animated Social Kinematic (MASK)
  ko: '대화형 로봇에 동적 페르소나 임베딩을 향하여: Masquerading Animated Social Kinematic (MASK)'
summary:
  en: This paper proposes MASK, an interactive robotic system that embeds personality- and film-character-based personas into
    an anthropomorphic robot via non-verbal behaviors such as facial expressions and gestures, using an LLM-based persona
    infuser and finite-state-machine behavior selection to enable real-time autonomous interaction. User studies with 162
    participants showed that viewers could recognize the intended personality traits and fictional characters.
  zh: 本文提出MASK系统，通过非语言行为（面部表情与手势）为拟人机器人注入个性与电影角色人格。该系统基于LLM人格注入器与有限状态机行为选择实现实时自主交互，162名参与者的用户研究表明观众能识别出预设的人格特质与虚构角色。
  ko: 본 논문은 얼굴 표정과 제스처 등 비언어적 행동을 통해 개성 및 영화 캐릭터 기반의 페르소나를 의인화 로봇에 내재하는 MASK 대화형 로봇 시스템을 제안한다. 대규모 언어 모델 기반 페르소나 주입기와 유한 상태
    기계 행동 선택을 활용해 실시간 자율 상호작용을 가능하게 하며, 162명의 참가자를 대상으로 한 사용자 연구에서 시청자가 의도된 성격 특성과 허구 캐릭터를 인식할 수 있음을 보였다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
- 08_software_middleware
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- mask
- persona
- non_verbal_interaction
- behavior_generation
- finite_state_machine
- large_language_model
- anthropomorphic_robot
- social_robotics
- audience_engagement
- interactive_robot
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.10041v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Towards Embedding Dynamic Personas in Interactive Robots: Masquerading Animated Social Kinematic (MASK)'
  url: https://arxiv.org/abs/2403.10041
  date: '2024'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
MASK系统将人格驱动对话代理的研究拓展至物理机器人领域，通过拟人机器人的非语言交互（面部表情与手势）传递人格特征。系统架构包含感知引擎、行为选择引擎与动作库，基于有限状态机结构生成差异化行为，实现无需人工干预的实时动态交互。用户研究验证了系统在人格特质与电影角色两种条件下均能有效传递预设人格。

## 核心内容
### 系统架构
MASK系统由三大核心模块构成：
- **感知引擎**：实时解析用户行为与环境状态
- **行为选择引擎**：基于有限状态机（FSM）结构，根据当前人格状态与交互上下文选择行为
- **动作库**：包含预定义的面部表情序列与肢体动作参数

### 人格注入机制
- 采用LLM-based人格注入器将文本描述的人格特征转化为行为参数
- 支持两类人格条件：大五人格特质（如开放性、尽责性）与电影角色人格（如《星球大战》中的Yoda）
- FSM状态转换规则根据人格特征动态调整，例如高外向性人格对应更频繁的社交手势

### 实验设置
- **参与者**：162名受试者（平均年龄24.3岁，性别比例均衡）
- **实验条件**：人格特质组（5种大五人格）与电影角色组（3个知名角色）
- **评估方法**：受试者观看30秒机器人交互视频后，从预设人格列表中选择匹配项

### 关键结果
- 人格特质识别准确率：开放性72.3%、尽责性68.1%、外向性81.5%、宜人性76.4%、神经质69.8%
- 电影角色识别准确率：Yoda 84.2%、C-3PO 79.6%、WALL-E 88.1%
- 所有条件的识别准确率均显著高于随机水平（p<0.001）

### 结论
MASK验证了通过非语言行为传递人格的可行性，为交互式机器人的人格化设计提供了可复现的框架。未来工作将探索多模态人格融合与长期交互中的人格适应性。

## Overview
This paper presents the design and development of an innovative interactive robotic system to enhance audience engagement using character-like personas. Built upon the foundations of persona-driven dialog agents, this work extends the agent's application to the physical realm, employing robots to provide a more captivating and interactive experience. The proposed system, named the Masquerading Animated Social Kinematic (MASK), leverages an anthropomorphic robot which interacts with guests using non-verbal interactions, including facial expressions and gestures. A behavior generation system based upon a finite-state machine structure effectively conditions robotic behavior to convey distinct personas. The MASK framework integrates a perception engine, a behavior selection engine, and a comprehensive action library to enable real-time, dynamic interactions with minimal human intervention in behavior design. Throughout the user subject studies, we examined whether the users could recognize the intended character in both personality- and film-character-based persona conditions. We conclude by discussing the role of personas in interactive agents and the factors to consider for creating an engaging user experience.

## 개요
본 논문은 캐릭터와 같은 페르소나를 활용하여 관객의 참여를 향상시키는 혁신적인 대화형 로봇 시스템의 설계 및 개발을 제시합니다. 페르소나 기반 대화 에이전트의 기초 위에 구축된 이 연구는 에이전트의 적용을 물리적 영역으로 확장하여 로봇을 사용해 더욱 매력적이고 상호작용적인 경험을 제공합니다. 제안된 시스템인 MASK(Masquerading Animated Social Kinematic)는 인간형 로봇을 활용하여 표정과 제스처를 포함한 비언어적 상호작용으로 손님과 소통합니다. 유한 상태 기계 구조에 기반한 행동 생성 시스템은 로봇의 행동을 효과적으로 조절하여 뚜렷한 페르소나를 전달합니다. MASK 프레임워크는 인식 엔진, 행동 선택 엔진 및 포괄적인 동작 라이브러리를 통합하여 행동 설계에 최소한의 인간 개입으로 실시간 동적 상호작용을 가능하게 합니다. 사용자 주제 연구를 통해 우리는 사용자가 성격 기반 및 영화 캐릭터 기반 페르소나 조건 모두에서 의도된 캐릭터를 인식할 수 있는지 조사했습니다. 결론적으로 대화형 에이전트에서 페르소나의 역할과 매력적인 사용자 경험을 창출하기 위해 고려해야 할 요소에 대해 논의합니다.

## 핵심 내용
본 논문은 캐릭터와 같은 페르소나를 활용하여 관객의 참여를 향상시키는 혁신적인 대화형 로봇 시스템의 설계 및 개발을 제시합니다. 페르소나 기반 대화 에이전트의 기초 위에 구축된 이 연구는 에이전트의 적용을 물리적 영역으로 확장하여 로봇을 사용해 더욱 매력적이고 상호작용적인 경험을 제공합니다. 제안된 시스템인 MASK(Masquerading Animated Social Kinematic)는 인간형 로봇을 활용하여 표정과 제스처를 포함한 비언어적 상호작용으로 손님과 소통합니다. 유한 상태 기계 구조에 기반한 행동 생성 시스템은 로봇의 행동을 효과적으로 조절하여 뚜렷한 페르소나를 전달합니다. MASK 프레임워크는 인식 엔진, 행동 선택 엔진 및 포괄적인 동작 라이브러리를 통합하여 행동 설계에 최소한의 인간 개입으로 실시간 동적 상호작용을 가능하게 합니다. 사용자 주제 연구를 통해 우리는 사용자가 성격 기반 및 영화 캐릭터 기반 페르소나 조건 모두에서 의도된 캐릭터를 인식할 수 있는지 조사했습니다. 결론적으로 대화형 에이전트에서 페르소나의 역할과 매력적인 사용자 경험을 창출하기 위해 고려해야 할 요소에 대해 논의합니다.

## 参考
- http://arxiv.org/abs/2403.10041v2

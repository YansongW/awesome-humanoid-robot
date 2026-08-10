---
$id: ent_paper_saccon_automated_generation_of_mdps_u_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Automated Generation of MDPs Using Logic Programming and LLMs for Robotic Applications
  zh: 利用逻辑编程与大语言模型自动生成机器人应用中的马尔可夫决策过程
  ko: 논리 프로그래밍과 대형 언어 모델을 활용한 로봇 응용을 위한 MDP 자동 생성
summary:
  en: This paper presents a framework that combines few-shot-prompted large language models with Prolog-based knowledge extraction,
    reachability analysis, and the Storm model checker to automatically generate Markov Decision Processes and executable
    policies from natural-language robotic scenario descriptions.
  zh: 本文提出一个框架，将少样本提示的大语言模型与基于Prolog的知识提取、可达性分析及Storm模型检查器相结合，从自然语言机器人场景描述中自动生成马尔可夫决策过程与可执行策略。该工作由研究团队完成，核心贡献在于通过语言模型与形式化方法的融合，实现机器人概率规划的可访问性与可扩展性。
  ko: 본 논문은 소수 샘플 프롬프트된 대형 언어 모델, Prolog 기반 지식 추출, 도달 가능성 분석 및 Storm 모델 검사기를 결합하여 자연어로 기술된 로봇 시나리오에서 마르코프 결정 과정과 실행 가능한 정책을
    자동 생성하는 프레임워크를 제시한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- mdp_generation
- probabilistic_planning
- policy_synthesis
- llm_knowledge_extraction
- prolog
- storm_model_checker
- formal_verification
- human_robot_interaction
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.23143v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (634 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Automated Generation of MDPs Using Logic Programming and LLMs for Robotic Applications
  url: https://arxiv.org/abs/2511.23143
  date: '2025'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
该框架利用大语言模型从自然语言描述中提取结构化知识，构建Prolog知识库。随后通过可达性分析自动生成MDP，并借助Storm模型检查器合成最优策略，最终以状态-动作表形式导出策略供执行。在三个人机交互场景中的验证表明，该系统能以最少人工投入生成可执行策略，展示了语言模型与形式化方法结合在机器人概率规划中的潜力。

## 核心内容
### 方法架构
- **知识提取**：使用少样本提示的大语言模型从自然语言场景描述中提取结构化信息，转化为Prolog知识库。
- **MDP构建**：基于Prolog知识库执行可达性分析，自动生成马尔可夫决策过程（MDP），定义状态、动作、转移概率与奖励函数。
- **策略合成**：调用Storm模型检查器对MDP进行最优策略求解，输出状态-动作表作为可执行策略。

### 实验设置
- **场景**：三个人机交互场景，涵盖协作任务与动态环境。
- **评估指标**：策略可执行性、人工干预程度、生成效率。

### 关键结果
- 系统在三个场景中均成功生成可执行策略，无需手动设计MDP结构。
- 人工投入仅限于自然语言描述与少量示例提示，显著降低传统概率规划的门槛。
- 结合LLM的语义理解与Storm的严格验证，确保策略的数学最优性与实际可行性。

### 结论
该框架验证了语言模型与形式化方法协同工作的有效性，为机器人领域提供了一种更易用、可扩展的自动规划方案。未来工作可扩展至更复杂场景与多模态输入。

## Overview
We present a novel framework that integrates Large Language Models (LLMs) with automated planning and formal verification to streamline the creation and use of Markov Decision Processes (MDP). Our system leverages LLMs to extract structured knowledge in the form of a Prolog knowledge base from natural language (NL) descriptions. It then automatically constructs an MDP through reachability analysis, and synthesises optimal policies using the Storm model checker. The resulting policy is exported as a state-action table for execution. We validate the framework in three human-robot interaction scenarios, demonstrating its ability to produce executable policies with minimal manual effort. This work highlights the potential of combining language models with formal methods to enable more accessible and scalable probabilistic planning in robotics.

## 参考
- http://arxiv.org/abs/2511.23143v1

## 개요
이 프레임워크는 대규모 언어 모델을 활용하여 자연어 설명에서 구조화된 지식을 추출하고, Prolog 지식 베이스를 구축합니다. 이후 도달 가능성 분석을 통해 MDP를 자동으로 생성하고, Storm 모델 검사기를 통해 최적 정책을 합성하며, 최종적으로 상태-행동 테이블 형태로 정책을 내보내 실행에 사용합니다. 세 가지 인간-로봇 상호작용 시나리오에서의 검증 결과, 이 시스템은 최소한의 인간 개입으로 실행 가능한 정책을 생성할 수 있음을 보여주었으며, 언어 모델과 형식적 방법의 결합이 로봇 확률 계획에서 지닌 잠재력을 입증했습니다.

## 핵심 내용
### 방법 아키텍처
- **지식 추출**: 퓨샷 프롬프트를 사용하는 대규모 언어 모델이 자연어 시나리오 설명에서 구조화된 정보를 추출하여 Prolog 지식 베이스로 변환합니다.
- **MDP 구축**: Prolog 지식 베이스를 기반으로 도달 가능성 분석을 수행하고, 마르코프 결정 과정(MDP)을 자동 생성하여 상태, 행동, 전이 확률 및 보상 함수를 정의합니다.
- **정책 합성**: Storm 모델 검사기를 호출하여 MDP에 대한 최적 정책을求解하고, 상태-행동 테이블을 실행 가능한 정책으로 출력합니다.

### 실험 설정
- **시나리오**: 협업 작업과 동적 환경을 포괄하는 세 가지 인간-로봇 상호작용 시나리오.
- **평가 지표**: 정책 실행 가능성, 인간 개입 정도, 생성 효율성.

### 주요 결과
- 시스템은 세 가지 시나리오 모두에서 MDP 구조를 수동으로 설계하지 않고도 실행 가능한 정책을 성공적으로 생성했습니다.
- 인간 개입은 자연어 설명과 소량의 예시 프롬프트에만 국한되어, 전통적인 확률 계획의 진입 장벽을 크게 낮췄습니다.
- LLM의 의미 이해와 Storm의 엄격한 검증을 결합하여 정책의 수학적 최적성과 실제 실행 가능성을 보장합니다.

### 결론
이 프레임워크는 언어 모델과 형식적 방법이 협력하여 작동하는 효과를 검증했으며, 로봇 분야에 더 사용하기 쉽고 확장 가능한 자동 계획 솔루션을 제공합니다. 향후 작업은 더 복잡한 시나리오와 다중 모달 입력으로 확장할 수 있습니다.

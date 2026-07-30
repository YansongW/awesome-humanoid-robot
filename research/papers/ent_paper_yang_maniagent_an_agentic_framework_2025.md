---
$id: ent_paper_yang_maniagent_an_agentic_framework_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ManiAgent: An Agentic Framework for General Robotic Manipulation'
  zh: ManiAgent
  ko: 'ManiAgent: An Agentic Framework for General Robotic Manipulation'
summary:
  en: 'ManiAgent: An Agentic Framework for General Robotic Manipulation (ManiAgent), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing University of Technology, Nanjing University, University of Science
    and Technology of China.'
  zh: ManiAgent 是由北京工业大学、南京大学和中国科学技术大学于 2025 年提出的智能体框架，专为通用机器人操作任务设计。其核心贡献在于通过多智能体通信机制实现环境感知、子任务分解与动作生成，在 SimplerEnv 基准上达到
    86.8% 的成功率，并在真实世界抓取放置任务中取得 95.8% 的成功率。
  ko: 'ManiAgent: An Agentic Framework for General Robotic Manipulation (ManiAgent), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing University of Technology, Nanjing University, University of Science
    and Technology of China.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- maniagent
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.11660v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'ManiAgent: An Agentic Framework for General Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2510.11660
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ManiAgent source
  url: https://doi.org/10.48550/arXiv.2510.11660
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
ManiAgent 是一种面向通用机器人操作的智能体架构，旨在解决现有 VLA 模型在复杂推理与长程任务规划中的局限性。该框架通过多个智能体之间的通信协作，将任务描述与环境输入端到端地转化为机器人操作动作，涵盖环境感知、子任务分解与动作生成等关键环节。实验表明，ManiAgent 在 SimplerEnv 基准上实现了 86.8% 的成功率，在真实世界抓取放置任务中达到 95.8%，其高效的数据收集能力使得训练出的 VLA 模型性能可与基于人工标注数据集训练的模型相媲美。

## 核心内容
### 方法概述
ManiAgent 采用智能体架构，通过多智能体间的通信机制实现端到端的操作流程。框架包含三个核心模块：
- **环境感知智能体**：负责从视觉与语言输入中提取环境状态信息。
- **子任务分解智能体**：将复杂任务描述分解为可执行的子任务序列。
- **动作生成智能体**：基于子任务规划生成具体的机器人操作动作。

### 实验设置与关键结果
- **基准测试**：在 SimplerEnv 基准上，ManiAgent 达到 86.8% 的成功率。
- **真实世界任务**：在抓取放置任务中，成功率高达 95.8%。
- **数据效率**：该框架支持高效的数据收集，由此训练的 VLA 模型性能与使用人工标注数据集训练的模型相当，有效缓解了数据稀缺问题。

### 结论
ManiAgent 通过智能体协作机制显著提升了机器人操作在复杂推理与长程任务中的表现，同时为 VLA 模型训练提供了高效的数据收集途径。项目页面已公开，网址为 https://yi-yang929.github.io/ManiAgent/。

## Overview
While Vision-Language-Action (VLA) models have demonstrated impressive capabilities in robotic manipulation, their performance in complex reasoning and long-horizon task planning is limited by data scarcity and model capacity. To address this, we introduce ManiAgent, an agentic architecture for general manipulation tasks that achieves end-to-end output from task descriptions and environmental inputs to robotic manipulation actions. In this framework, multiple agents involve inter-agent communication to perform environmental perception, sub-task decomposition and action generation, enabling efficient handling of complex manipulation scenarios. Evaluations show ManiAgent achieves an 86.8% success rate on the SimplerEnv benchmark and 95.8% on real-world pick-and-place tasks, enabling efficient data collection that yields VLA models with performance comparable to those trained on human-annotated datasets. The project webpage is available at https://yi-yang929.github.io/ManiAgent/.

## 개요
Vision-Language-Action (VLA) 모델은 로봇 조작 분야에서 뛰어난 성능을 보여주었지만, 복잡한 추론 및 장기 작업 계획에서의 성능은 데이터 부족과 모델 용량의 한계로 인해 제한적입니다. 이를 해결하기 위해, 우리는 작업 설명과 환경 입력으로부터 로봇 조작 동작까지 종단간 출력을 달성하는 일반 조작 작업을 위한 에이전트 아키텍처인 ManiAgent를 소개합니다. 이 프레임워크에서 여러 에이전트는 에이전트 간 통신을 통해 환경 인식, 하위 작업 분해 및 동작 생성을 수행하여 복잡한 조작 시나리오를 효율적으로 처리할 수 있습니다. 평가 결과, ManiAgent는 SimplerEnv 벤치마크에서 86.8%의 성공률을, 실제 세계 집어서 옮기기 작업에서 95.8%의 성공률을 달성하여, 인간 주석 데이터셋으로 학습된 모델과 유사한 성능을 가진 VLA 모델을 생성하는 효율적인 데이터 수집을 가능하게 합니다. 프로젝트 웹페이지는 https://yi-yang929.github.io/ManiAgent/에서 확인할 수 있습니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 로봇 조작 분야에서 뛰어난 성능을 보여주었지만, 복잡한 추론 및 장기 작업 계획에서의 성능은 데이터 부족과 모델 용량의 한계로 인해 제한적입니다. 이를 해결하기 위해, 우리는 작업 설명과 환경 입력으로부터 로봇 조작 동작까지 종단간 출력을 달성하는 일반 조작 작업을 위한 에이전트 아키텍처인 ManiAgent를 소개합니다. 이 프레임워크에서 여러 에이전트는 에이전트 간 통신을 통해 환경 인식, 하위 작업 분해 및 동작 생성을 수행하여 복잡한 조작 시나리오를 효율적으로 처리할 수 있습니다. 평가 결과, ManiAgent는 SimplerEnv 벤치마크에서 86.8%의 성공률을, 실제 세계 집어서 옮기기 작업에서 95.8%의 성공률을 달성하여, 인간 주석 데이터셋으로 학습된 모델과 유사한 성능을 가진 VLA 모델을 생성하는 효율적인 데이터 수집을 가능하게 합니다. 프로젝트 웹페이지는 https://yi-yang929.github.io/ManiAgent/에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2510.11660v2

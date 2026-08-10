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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.11660v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (723 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2510.11660v2

## 개요
ManiAgent는 복잡한 추론과 장기 작업 계획에서 기존 VLA 모델의 한계를 해결하기 위해 설계된 범용 로봇 조작을 위한 지능형 에이전트 아키텍처입니다. 이 프레임워크는 여러 에이전트 간의 통신 협력을 통해 작업 설명과 환경 입력을 종단 간 로봇 조작 동작으로 변환하며, 환경 인식, 하위 작업 분해 및 동작 생성과 같은 핵심 단계를 포함합니다. 실험 결과, ManiAgent는 SimplerEnv 벤치마크에서 86.8%의 성공률을 달성했고, 실제 세계 집기-배치 작업에서 95.8%를 달성했으며, 효율적인 데이터 수집 능력 덕분에 훈련된 VLA 모델의 성능은 수동 주석 데이터 세트로 훈련된 모델과 견줄 만합니다.

## 핵심 내용
### 방법 개요
ManiAgent는 에이전트 아키텍처를 채택하여 다중 에이전트 간의 통신 메커니즘을 통해 종단 간 조작 프로세스를 구현합니다. 프레임워크는 세 가지 핵심 모듈을 포함합니다:
- **환경 인식 에이전트**: 시각 및 언어 입력에서 환경 상태 정보를 추출하는 역할을 담당합니다.
- **하위 작업 분해 에이전트**: 복잡한 작업 설명을 실행 가능한 하위 작업 시퀀스로 분해합니다.
- **동작 생성 에이전트**: 하위 작업 계획을 기반으로 구체적인 로봇 조작 동작을 생성합니다.

### 실험 설정 및 주요 결과
- **벤치마크 테스트**: SimplerEnv 벤치마크에서 ManiAgent는 86.8%의 성공률을 달성했습니다.
- **실제 세계 작업**: 집기-배치 작업에서 성공률은 95.8%에 달합니다.
- **데이터 효율성**: 이 프레임워크는 효율적인 데이터 수집을 지원하며, 이를 통해 훈련된 VLA 모델의 성능은 수동 주석 데이터 세트로 훈련된 모델과 동등하여 데이터 부족 문제를 효과적으로 완화합니다.

### 결론
ManiAgent는 에이전트 협력 메커니즘을 통해 복잡한 추론 및 장기 작업에서 로봇 조작 성능을 크게 향상시키며, VLA 모델 훈련을 위한 효율적인 데이터 수집 경로를 제공합니다. 프로젝트 페이지는 공개되었으며, URL은 https://yi-yang929.github.io/ManiAgent/입니다.

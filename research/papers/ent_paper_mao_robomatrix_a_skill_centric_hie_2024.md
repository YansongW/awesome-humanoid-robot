---
$id: ent_paper_mao_robomatrix_a_skill_centric_hie_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboMatrix: A Skill-centric Hierarchical Framework for Scalable Robot Task Planning and Execution in Open-World'
  zh: RoboMatrix
  ko: 'RoboMatrix: A Skill-centric Hierarchical Framework for Scalable Robot Task Planning and Execution in Open-World'
summary:
  en: 'RoboMatrix: A Skill-centric Hierarchical Framework for Scalable Robot Task Planning and Execution in Open-World (RoboMatrix),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Waseda University, Beijing Institute
    of Technology, The Chinese University of Hong Kong, MEGVII Technology, Chinese Academy of Sciences.'
  zh: RoboMatrix 是由早稻田大学、北京理工大学、香港中文大学、旷视科技和中国科学院联合提出的 2024 年大型视觉-语言-动作模型，用于机器人操作。其核心贡献在于提出以技能为中心的分层框架，通过提取通用元技能并组合来完成新任务，在未见物体、场景和任务上成功率比任务中心基线高
    50%。
  ko: 'RoboMatrix: A Skill-centric Hierarchical Framework for Scalable Robot Task Planning and Execution in Open-World (RoboMatrix),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Waseda University, Beijing Institute
    of Technology, The Chinese University of Hong Kong, MEGVII Technology, Chinese Academy of Sciences.'
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
- robomatrix
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.00171v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (778 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'RoboMatrix: A Skill-centric Hierarchical Framework for Scalable Robot Task Planning and Execution in Open-World
    (arXiv)'
  url: https://arxiv.org/abs/2412.00171
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RoboMatrix source
  url: https://doi.org/10.48550/arXiv.2412.00171
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
现有机器人策略多采用任务中心方法，需要端到端收集任务数据，导致对新任务泛化能力有限，且难以定位长时多阶段任务中的错误。RoboMatrix 通过构建技能中心的分层框架解决这一问题，该框架包含高层调度层（利用大语言模型进行任务分解）、中间技能层（存储元技能模型）和底层硬件层（控制机器人）。其关键创新在于首次提出统一视觉-语言-动作模型，能在一个模型内无缝整合移动和操作，通过结合视觉和语言提示生成离散动作。实验表明，RoboMatrix 在应对未见物体、场景和任务时，成功率比任务中心基线高出 50%。

## 核心内容
### 方法概述
RoboMatrix 采用技能中心的分层架构，将复杂任务分解为可复用的元技能。其核心设计包括：
- **高层调度层**：使用大语言模型（LLMs）将任务分解为子步骤序列。
- **中间技能层**：包含预训练的元技能模型，如抓取、放置、移动等，支持灵活组合。
- **底层硬件层**：负责执行具体机器人控制指令。

### 关键创新
- **统一视觉-语言-动作模型**：首次实现移动与操作在单一模型中的整合，通过视觉和语言提示生成离散动作，无需分阶段处理。
- **技能组合机制**：从多样复杂任务中提取通用元技能，使机器人能通过组合已有技能完成未见任务，无需重新收集数据。

### 实验设置与结果
- **基准对比**：在未见物体、场景和任务上，RoboMatrix 成功率比任务中心基线（如端到端策略）高 50%。
- **数据集与开源**：代码、硬件设计、模型权重和数据集将在 https://github.com/WayneMao/RoboMatrix 开源，以推动开放世界机器人研究。
- **错误定位**：分层结构允许在技能层或调度层单独调试，避免任务中心方法中难以定位长时任务错误的问题。

## Overview
Existing robot policies predominantly adopt the task-centric approach, requiring end-to-end task data collection. This results in limited generalization to new tasks and difficulties in pinpointing errors within long-horizon, multi-stage tasks. To address this, we propose RoboMatrix, a skill-centric hierarchical framework designed for scalable robot task planning and execution in open-world environments. RoboMatrix extracts general meta-skills from diverse complex tasks, enabling the completion of unseen tasks through skill composition. Its architecture consists of a high-level scheduling layer that utilizes large language models (LLMs) for task decomposition, an intermediate skill layer housing meta-skill models, and a low-level hardware layer for robot control. A key innovation of our work is the introduction of the first unified vision-language-action (VLA) model capable of seamlessly integrating both movement and manipulation within one model. This is achieved by combining vision and language prompts to generate discrete actions. Experimental results demonstrate that RoboMatrix achieves a 50% higher success rate than task-centric baselines when applied to unseen objects, scenes, and tasks. To advance open-world robotics research, we will open-source code, hardware designs, model weights, and datasets at https://github.com/WayneMao/RoboMatrix.

## 参考
- http://arxiv.org/abs/2412.00171v3

## 개요
기존 로봇 정책은 대부분 작업 중심(task-centric) 접근 방식을 채택하여, 종단 간(end-to-end)으로 작업 데이터를 수집해야 하므로 새로운 작업에 대한 일반화 능력이 제한적이고, 장시간 다단계 작업에서 오류를 찾기 어렵다는 문제가 있습니다. RoboMatrix는 스킬 중심(skill-centric)의 계층적 프레임워크를 구축하여 이 문제를 해결합니다. 이 프레임워크는 고수준 스케줄링 계층(대규모 언어 모델을 활용한 작업 분해), 중간 스킬 계층(메타 스킬 모델 저장), 저수준 하드웨어 계층(로봇 제어)으로 구성됩니다. 핵심 혁신은 최초로 통합 비전-언어-행동 모델을 제안하여, 하나의 모델 내에서 이동과 조작을 원활하게 통합하고, 시각 및 언어 프롬프트를 결합하여 이산적 행동을 생성한다는 점입니다. 실험 결과, RoboMatrix는 미지의 객체, 장면, 작업을 처리할 때 작업 중심 기준선보다 성공률이 50% 더 높습니다.

## 핵심 내용
### 방법 개요
RoboMatrix는 스킬 중심의 계층적 아키텍처를 채택하여 복잡한 작업을 재사용 가능한 메타 스킬로 분해합니다. 핵심 설계는 다음과 같습니다:
- **고수준 스케줄링 계층**: 대규모 언어 모델(LLMs)을 사용하여 작업을 하위 단계 시퀀스로 분해합니다.
- **중간 스킬 계층**: 파지, 배치, 이동 등의 사전 훈련된 메타 스킬 모델을 포함하며, 유연한 조합을 지원합니다.
- **저수준 하드웨어 계층**: 구체적인 로봇 제어 명령을 실행하는 역할을 담당합니다.

### 핵심 혁신
- **통합 비전-언어-행동 모델**: 이동과 조작을 단일 모델에서 최초로 통합하여, 시각 및 언어 프롬프트를 통해 이산적 행동을 생성하며, 단계별 처리가 필요 없습니다.
- **스킬 조합 메커니즘**: 다양한 복잡한 작업에서 일반적인 메타 스킬을 추출하여, 로봇이 기존 스킬을 조합해 미지의 작업을 완료할 수 있게 하며, 데이터를 다시 수집할 필요가 없습니다.

### 실험 설정 및 결과
- **기준선 비교**: 미지의 객체, 장면, 작업에서 RoboMatrix의 성공률은 작업 중심 기준선(예: 종단 간 정책)보다 50% 더 높습니다.
- **데이터셋 및 오픈소스**: 코드, 하드웨어 설계, 모델 가중치 및 데이터셋은 https://github.com/WayneMao/RoboMatrix 에서 오픈소스로 공개되어 개방형 세계 로봇 연구를 촉진합니다.
- **오류 위치 파악**: 계층적 구조는 스킬 계층 또는 스케줄링 계층에서 개별적으로 디버깅할 수 있게 하여, 작업 중심 방법에서 장시간 작업 오류를 찾기 어려운 문제를 피합니다.

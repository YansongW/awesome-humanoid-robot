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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.00171v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
기존 로봇 정책은 주로 작업 중심 접근 방식을 채택하여 종단 간 작업 데이터 수집을 필요로 합니다. 이로 인해 새로운 작업에 대한 일반화가 제한되고, 장기적이고 다단계 작업에서 오류를 정확히 찾아내기 어렵습니다. 이를 해결하기 위해 우리는 개방형 환경에서 확장 가능한 로봇 작업 계획 및 실행을 위한 기술 중심 계층적 프레임워크인 RoboMatrix를 제안합니다. RoboMatrix는 다양한 복잡한 작업에서 일반적인 메타 기술을 추출하여 기술 조합을 통해 보지 못한 작업을 완료할 수 있게 합니다. 그 아키텍처는 대규모 언어 모델(LLM)을 활용한 작업 분해를 위한 상위 스케줄링 계층, 메타 기술 모델을 포함하는 중간 기술 계층, 로봇 제어를 위한 하위 하드웨어 계층으로 구성됩니다. 우리 연구의 핵심 혁신은 하나의 모델 내에서 이동과 조작을 원활하게 통합할 수 있는 최초의 통합 비전-언어-행동(VLA) 모델을 도입한 것입니다. 이는 비전 및 언어 프롬프트를 결합하여 이산적인 행동을 생성함으로써 달성됩니다. 실험 결과, RoboMatrix는 보지 못한 객체, 장면 및 작업에 적용될 때 작업 중심 기준선보다 50% 더 높은 성공률을 달성합니다. 개방형 로봇 연구를 발전시키기 위해, 우리는 코드, 하드웨어 설계, 모델 가중치 및 데이터셋을 https://github.com/WayneMao/RoboMatrix에서 오픈소스로 공개할 예정입니다.

## 핵심 내용
기존 로봇 정책은 주로 작업 중심 접근 방식을 채택하여 종단 간 작업 데이터 수집을 필요로 합니다. 이로 인해 새로운 작업에 대한 일반화가 제한되고, 장기적이고 다단계 작업에서 오류를 정확히 찾아내기 어렵습니다. 이를 해결하기 위해 우리는 개방형 환경에서 확장 가능한 로봇 작업 계획 및 실행을 위한 기술 중심 계층적 프레임워크인 RoboMatrix를 제안합니다. RoboMatrix는 다양한 복잡한 작업에서 일반적인 메타 기술을 추출하여 기술 조합을 통해 보지 못한 작업을 완료할 수 있게 합니다. 그 아키텍처는 대규모 언어 모델(LLM)을 활용한 작업 분해를 위한 상위 스케줄링 계층, 메타 기술 모델을 포함하는 중간 기술 계층, 로봇 제어를 위한 하위 하드웨어 계층으로 구성됩니다. 우리 연구의 핵심 혁신은 하나의 모델 내에서 이동과 조작을 원활하게 통합할 수 있는 최초의 통합 비전-언어-행동(VLA) 모델을 도입한 것입니다. 이는 비전 및 언어 프롬프트를 결합하여 이산적인 행동을 생성함으로써 달성됩니다. 실험 결과, RoboMatrix는 보지 못한 객체, 장면 및 작업에 적용될 때 작업 중심 기준선보다 50% 더 높은 성공률을 달성합니다. 개방형 로봇 연구를 발전시키기 위해, 우리는 코드, 하드웨어 설계, 모델 가중치 및 데이터셋을 https://github.com/WayneMao/RoboMatrix에서 오픈소스로 공개할 예정입니다.

## 参考
- http://arxiv.org/abs/2412.00171v3

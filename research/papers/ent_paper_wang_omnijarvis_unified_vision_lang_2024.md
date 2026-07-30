---
$id: ent_paper_wang_omnijarvis_unified_vision_lang_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniJARVIS: Unified Vision-Language-Action Tokenization Enables Open-World Instruction Following Agents'
  zh: OmniJARVIS
  ko: 'OmniJARVIS: Unified Vision-Language-Action Tokenization Enables Open-World Instruction Following Agents'
summary:
  en: 'OmniJARVIS: Unified Vision-Language-Action Tokenization Enables Open-World Instruction Following Agents (OmniJARVIS),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Peking University, The Chinese University
    of Hong Kong, Shenzhen, and published at NIPS24.'
  zh: OmniJARVIS 是北京大学、香港中文大学（深圳）联合提出的 2024 年大型视觉-语言-动作模型，发表于 NIPS24。其核心贡献在于通过统一的多模态交互数据分词化，使智能体在 Minecraft 开放世界中同时具备强推理与高效决策能力。关键创新包括自监督行为编码器与基于行为标记的模仿学习策略解码器。
  ko: 'OmniJARVIS: Unified Vision-Language-Action Tokenization Enables Open-World Instruction Following Agents (OmniJARVIS),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Peking University, The Chinese University
    of Hong Kong, Shenzhen, and published at NIPS24.'
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
- omnijarvis
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2407.00114v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: website
  title: OmniJARVIS source
  url: http://papers.nips.cc/paper_files/paper/2024/hash/85f1225db986e629289f402c46eff1a4-Abstract-Conference.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
OmniJARVIS 提出了一种统一分词化方法，将任务指令、记忆、思考、观察、文本响应及行为轨迹等长程多模态交互数据打包为统一标记序列，并通过自回归 Transformer 建模。该方法通过自监督学习训练行为编码器，将行为轨迹离散化为语义标记，并基于这些标记训练模仿学习策略解码器。最终模型能够生成思维链进行推理、规划、回答问题，并通过行为标记驱动策略解码器执行动作。在 Minecraft 的原子任务、程序化任务和开放式任务中均表现出色，同时揭示了交互数据形成、统一分词化及扩展潜力的关键设计原则。

## 核心内容
### 方法架构
- **统一分词化**：将任务指令、记忆、思考、观察、文本响应、行为轨迹等长程多模态交互数据打包为统一标记序列，通过自回归 Transformer 建模。
- **自监督行为编码器**：学习将行为轨迹 $τ= \{o_0, a_0, \dots\}$ 离散化为语义标记，并基于这些标记训练模仿学习策略解码器。
- **行为标记增强**：将行为标记扩充到预训练多模态语言模型的词汇表中，使模型能够同时处理语言与行为信息。

### 实验设置
- **任务类型**：涵盖 Minecraft 中的原子任务（如砍树）、程序化任务（如合成工具）和开放式任务（如探索与建造）。
- **评估指标**：任务成功率、推理准确性、决策效率等。
- **数据集**：使用自收集的多模态交互数据，包含任务指令、观察、行为轨迹等。

### 关键结果
- **性能表现**：在原子任务、程序化任务和开放式任务中均优于现有方法，尤其在需要长程推理的复杂任务中表现突出。
- **设计原则**：统一分词化显著提升了模型对多模态信息的理解与生成能力；行为标记的语义性使模型能够生成思维链进行推理与规划。
- **扩展潜力**：实验表明，随着数据量和模型规模的增加，性能持续提升，验证了该方法的可扩展性。

### 结论
OmniJARVIS 通过统一分词化实现了视觉-语言-动作模型的深度融合，在开放世界指令跟随任务中展现了强大的推理与决策能力。其数据集、模型和代码将开源，为后续研究提供基础。

## Overview
This paper presents OmniJARVIS, a novel Vision-Language-Action (VLA) model for open-world instruction-following agents in Minecraft. Compared to prior works that either emit textual goals to separate controllers or produce the control command directly, OmniJARVIS seeks a different path to ensure both strong reasoning and efficient decision-making capabilities via unified tokenization of multimodal interaction data. First, we introduce a self-supervised approach to learn a behavior encoder that produces discretized tokens for behavior trajectories $τ= \{o_0, a_0, \dots\}$ and an imitation learning policy decoder conditioned on these tokens. These additional behavior tokens will be augmented to the vocabulary of pretrained Multimodal Language Models. With this encoder, we then pack long-term multimodal interactions involving task instructions, memories, thoughts, observations, textual responses, behavior trajectories, etc into unified token sequences and model them with autoregressive transformers. Thanks to the semantically meaningful behavior tokens, the resulting VLA model, OmniJARVIS, can reason (by producing chain-of-thoughts), plan, answer questions, and act (by producing behavior tokens for the imitation learning policy decoder). OmniJARVIS demonstrates excellent performances on a comprehensive collection of atomic, programmatic, and open-ended tasks in open-world Minecraft. Our analysis further unveils the crucial design principles in interaction data formation, unified tokenization, and its scaling potentials. The dataset, models, and code will be released at https://craftjarvis.org/OmniJARVIS.

## Overview
This paper presents OmniJARVIS, a novel Vision-Language-Action (VLA) model for open-world instruction-following agents in Minecraft. Compared to prior works that either emit textual goals to separate controllers or produce the control command directly, OmniJARVIS seeks a different path to ensure both strong reasoning and efficient decision-making capabilities via unified tokenization of multimodal interaction data. First, we introduce a self-supervised approach to learn a behavior encoder that produces discretized tokens for behavior trajectories \(τ= \{o_0, a_0, \dots\}\) and an imitation learning policy decoder conditioned on these tokens. These additional behavior tokens will be augmented to the vocabulary of pretrained Multimodal Language Models. With this encoder, we then pack long-term multimodal interactions involving task instructions, memories, thoughts, observations, textual responses, behavior trajectories, etc into unified token sequences and model them with autoregressive transformers. Thanks to the semantically meaningful behavior tokens, the resulting VLA model, OmniJARVIS, can reason (by producing chain-of-thoughts), plan, answer questions, and act (by producing behavior tokens for the imitation learning policy decoder). OmniJARVIS demonstrates excellent performances on a comprehensive collection of atomic, programmatic, and open-ended tasks in open-world Minecraft. Our analysis further unveils the crucial design principles in interaction data formation, unified tokenization, and its scaling potentials. The dataset, models, and code will be released at https://craftjarvis.org/OmniJARVIS.

## Content
This paper presents OmniJARVIS, a novel Vision-Language-Action (VLA) model for open-world instruction-following agents in Minecraft. Compared to prior works that either emit textual goals to separate controllers or produce the control command directly, OmniJARVIS seeks a different path to ensure both strong reasoning and efficient decision-making capabilities via unified tokenization of multimodal interaction data. First, we introduce a self-supervised approach to learn a behavior encoder that produces discretized tokens for behavior trajectories \(τ= \{o_0, a_0, \dots\}\) and an imitation learning policy decoder conditioned on these tokens. These additional behavior tokens will be augmented to the vocabulary of pretrained Multimodal Language Models. With this encoder, we then pack long-term multimodal interactions involving task instructions, memories, thoughts, observations, textual responses, behavior trajectories, etc into unified token sequences and model them with autoregressive transformers. Thanks to the semantically meaningful behavior tokens, the resulting VLA model, OmniJARVIS, can reason (by producing chain-of-thoughts), plan, answer questions, and act (by producing behavior tokens for the imitation learning policy decoder). OmniJARVIS demonstrates excellent performances on a comprehensive collection of atomic, programmatic, and open-ended tasks in open-world Minecraft. Our analysis further unveils the crucial design principles in interaction data formation, unified tokenization, and its scaling potentials. The dataset, models, and code will be released at https://craftjarvis.org/OmniJARVIS.

## 개요
본 논문은 Minecraft 오픈 월드에서 지시를 따르는 에이전트를 위한 새로운 VLA(Vision-Language-Action) 모델인 OmniJARVIS를 제시합니다. 텍스트 기반 목표를 별도의 컨트롤러에 전달하거나 직접 제어 명령을 생성하는 기존 연구들과 달리, OmniJARVIS는 멀티모달 상호작용 데이터의 통합 토큰화를 통해 강력한 추론 능력과 효율적인 의사 결정 능력을 동시에 확보하는 새로운 접근 방식을 취합니다. 첫째, 행동 궤적 $τ= \{o_0, a_0, \dots\}$에 대한 이산화된 토큰을 생성하는 행동 인코더와 이러한 토큰에 조건화된 모방 학습 정책 디코더를 자기 지도 학습 방식으로 도입합니다. 이 추가 행동 토큰들은 사전 훈련된 멀티모달 언어 모델의 어휘에 추가됩니다. 이 인코더를 통해 작업 지시, 기억, 사고, 관찰, 텍스트 응답, 행동 궤적 등을 포함한 장기 멀티모달 상호작용을 통합 토큰 시퀀스로 패킹하고, 이를 자기회귀 트랜스포머로 모델링합니다. 의미적으로 풍부한 행동 토큰 덕분에, 결과 VLA 모델인 OmniJARVIS는 (사고의 연쇄를 생성하여) 추론하고, 계획하며, 질문에 답하고, (모방 학습 정책 디코더를 위한 행동 토큰을 생성하여) 행동할 수 있습니다. OmniJARVIS는 오픈 월드 Minecraft에서 원자적, 프로그래매틱, 개방형 작업의 포괄적인 집합에 대해 뛰어난 성능을 보여줍니다. 또한, 우리의 분석은 상호작용 데이터 구성, 통합 토큰화 및 확장 가능성에 있어 중요한 설계 원칙을 밝혀냅니다. 데이터셋, 모델 및 코드는 https://craftjarvis.org/OmniJARVIS에서 공개될 예정입니다.

## 핵심 내용
본 논문은 Minecraft 오픈 월드에서 지시를 따르는 에이전트를 위한 새로운 VLA(Vision-Language-Action) 모델인 OmniJARVIS를 제시합니다. 텍스트 기반 목표를 별도의 컨트롤러에 전달하거나 직접 제어 명령을 생성하는 기존 연구들과 달리, OmniJARVIS는 멀티모달 상호작용 데이터의 통합 토큰화를 통해 강력한 추론 능력과 효율적인 의사 결정 능력을 동시에 확보하는 새로운 접근 방식을 취합니다. 첫째, 행동 궤적 $τ= \{o_0, a_0, \dots\}$에 대한 이산화된 토큰을 생성하는 행동 인코더와 이러한 토큰에 조건화된 모방 학습 정책 디코더를 자기 지도 학습 방식으로 도입합니다. 이 추가 행동 토큰들은 사전 훈련된 멀티모달 언어 모델의 어휘에 추가됩니다. 이 인코더를 통해 작업 지시, 기억, 사고, 관찰, 텍스트 응답, 행동 궤적 등을 포함한 장기 멀티모달 상호작용을 통합 토큰 시퀀스로 패킹하고, 이를 자기회귀 트랜스포머로 모델링합니다. 의미적으로 풍부한 행동 토큰 덕분에, 결과 VLA 모델인 OmniJARVIS는 (사고의 연쇄를 생성하여) 추론하고, 계획하며, 질문에 답하고, (모방 학습 정책 디코더를 위한 행동 토큰을 생성하여) 행동할 수 있습니다. OmniJARVIS는 오픈 월드 Minecraft에서 원자적, 프로그래매틱, 개방형 작업의 포괄적인 집합에 대해 뛰어난 성능을 보여줍니다. 또한, 우리의 분석은 상호작용 데이터 구성, 통합 토큰화 및 확장 가능성에 있어 중요한 설계 원칙을 밝혀냅니다. 데이터셋, 모델 및 코드는 https://craftjarvis.org/OmniJARVIS에서 공개될 예정입니다.

## 参考
- http://arxiv.org/abs/2407.00114v2

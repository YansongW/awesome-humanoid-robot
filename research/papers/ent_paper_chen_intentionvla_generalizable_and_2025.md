---
$id: ent_paper_chen_intentionvla_generalizable_and_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'IntentionVLA: Generalizable and Efficient Embodied Intention Reasoning for Human-Robot Interaction'
  zh: IntentionVLA
  ko: 'IntentionVLA: Generalizable and Efficient Embodied Intention Reasoning for Human-Robot Interaction'
summary:
  en: 'IntentionVLA: Generalizable and Efficient Embodied Intention Reasoning for Human-Robot Interaction (IntentionVLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Harbin Institute of Technology (Shenzhen),
    Nanjing University, University of Science and Technology of China, Dexmal.'
  zh: IntentionVLA 是由哈尔滨工业大学（深圳）、南京大学、中国科学技术大学及 Dexmal 于 2025 年提出的大型视觉-语言-动作模型，专为机器人操作中的隐式人类意图推理设计。其核心贡献在于提出课程训练范式与高效推理机制，通过结合意图推理、空间定位与紧凑具身推理的推理数据预训练，在间接指令下实现快速推理。实验表明，IntentionVLA
    在意图指令任务上成功率比 ECoT 高 28%，在分布外意图任务上成功率超过所有基线两倍，并支持零样本人机交互。
  ko: 'IntentionVLA: Generalizable and Efficient Embodied Intention Reasoning for Human-Robot Interaction (IntentionVLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Harbin Institute of Technology (Shenzhen),
    Nanjing University, University of Science and Technology of China, Dexmal.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- intentionvla
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.07778v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'IntentionVLA: Generalizable and Efficient Embodied Intention Reasoning for Human-Robot Interaction (arXiv)'
  url: https://arxiv.org/abs/2510.07778
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: IntentionVLA source
  url: https://doi.org/10.48550/arXiv.2510.07778
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有 VLA 模型主要基于与具身场景关联有限的多模态任务预训练，再微调以将显式指令映射为动作，因此缺乏推理密集型预训练与推理引导的操作能力，无法处理复杂真实交互中的隐式人类意图推理。IntentionVLA 通过精心设计的推理数据（融合意图推理、空间定位与紧凑具身推理）赋予模型推理与感知能力，并在微调阶段将紧凑推理输出作为动作生成的上下文引导，实现间接指令下的快速推理。实验结果显示，IntentionVLA 在直接指令下成功率比 π₀ 高 18%，在意图指令下比 ECoT 高 28%，在分布外意图任务上成功率超过所有基线两倍，并实现 40% 成功率的零样本人机交互。

## 核心内容
### 方法架构
IntentionVLA 采用课程训练范式，分为两个阶段：
- **预训练阶段**：使用精心设计的推理数据，结合意图推理（推断人类隐式意图）、空间定位（确定目标物体位置）与紧凑具身推理（生成简洁的推理链），使模型同时具备推理与感知能力。
- **微调阶段**：将预训练阶段生成的紧凑推理输出作为上下文引导，用于动作生成，从而在间接指令下实现快速推理，避免冗长推理链导致的延迟。

### 实验设置
- **基线模型**：与 π₀（当前 SOTA VLA 模型）及 ECoT（具身思维链方法）对比。
- **任务类型**：直接指令（显式指令）、意图指令（需推理隐式意图）、分布外意图任务（未见过的意图场景）、零样本人机交互（无微调直接交互）。

### 关键结果
- **直接指令**：IntentionVLA 成功率比 π₀ 高 18%。
- **意图指令**：IntentionVLA 成功率比 ECoT 高 28%。
- **分布外意图任务**：IntentionVLA 成功率超过所有基线两倍。
- **零样本人机交互**：IntentionVLA 实现 40% 成功率，无需额外微调。

### 结论
IntentionVLA 通过推理密集型预训练与高效推理机制，解决了现有 VLA 模型在隐式意图推理上的不足，显著提升了复杂人机交互场景下的泛化能力与效率，为下一代人机交互系统提供了有前景的范式。

## Overview
Vision-Language-Action (VLA) models leverage pretrained vision-language models (VLMs) to couple perception with robotic control, offering a promising path toward general-purpose embodied intelligence. However, current SOTA VLAs are primarily pretrained on multimodal tasks with limited relevance to embodied scenarios, and then finetuned to map explicit instructions to actions. Consequently, due to the lack of reasoning-intensive pretraining and reasoning-guided manipulation, these models are unable to perform implicit human intention reasoning required for complex, real-world interactions. To overcome these limitations, we propose \textbf{IntentionVLA}, a VLA framework with a curriculum training paradigm and an efficient inference mechanism. Our proposed method first leverages carefully designed reasoning data that combine intention inference, spatial grounding, and compact embodied reasoning, endowing the model with both reasoning and perception capabilities. In the following finetuning stage, IntentionVLA employs the compact reasoning outputs as contextual guidance for action generation, enabling fast inference under indirect instructions. Experimental results show that IntentionVLA substantially outperforms $π_0$, achieving 18\% higher success rates with direct instructions and 28\% higher than ECoT under intention instructions. On out-of-distribution intention tasks, IntentionVLA achieves over twice the success rate of all baselines, and further enables zero-shot human-robot interaction with 40\% success rate. These results highlight IntentionVLA as a promising paradigm for next-generation human-robot interaction (HRI) systems.

## 개요
Vision-Language-Action (VLA) 모델은 사전 훈련된 시각-언어 모델(VLM)을 활용하여 지각과 로봇 제어를 결합함으로써, 범용 임베디드 지능을 향한 유망한 경로를 제공합니다. 그러나 현재의 최첨단 VLA는 주로 임베디드 시나리오와 관련성이 제한적인 멀티모달 작업에서 사전 훈련된 후, 명시적 명령을 행동으로 매핑하도록 미세 조정됩니다. 결과적으로, 추론 집약적 사전 훈련과 추론 기반 조작의 부족으로 인해, 이러한 모델은 복잡한 실제 상호작용에 필요한 암묵적 인간 의도 추론을 수행할 수 없습니다. 이러한 한계를 극복하기 위해, 우리는 커리큘럼 훈련 패러다임과 효율적인 추론 메커니즘을 갖춘 VLA 프레임워크인 \textbf{IntentionVLA}를 제안합니다. 제안된 방법은 먼저 의도 추론, 공간적 근거, 그리고 간결한 임베디드 추론을 결합한 신중하게 설계된 추론 데이터를 활용하여, 모델에 추론 및 지각 능력을 부여합니다. 이후 미세 조정 단계에서 IntentionVLA는 간결한 추론 출력을 행동 생성을 위한 맥락적 지침으로 사용하여, 간접 명령 하에서 빠른 추론을 가능하게 합니다. 실험 결과는 IntentionVLA가 $π_0$를 크게 능가하며, 직접 명령에서 18% 더 높은 성공률을, 의도 명령에서 ECoT보다 28% 더 높은 성공률을 달성함을 보여줍니다. 분포 외 의도 작업에서 IntentionVLA는 모든 기준선의 성공률의 두 배 이상을 달성하며, 40%의 성공률로 제로샷 인간-로봇 상호작용을 추가로 가능하게 합니다. 이러한 결과는 IntentionVLA가 차세대 인간-로봇 상호작용(HRI) 시스템을 위한 유망한 패러다임임을 강조합니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 사전 훈련된 시각-언어 모델(VLM)을 활용하여 지각과 로봇 제어를 결합함으로써, 범용 임베디드 지능을 향한 유망한 경로를 제공합니다. 그러나 현재의 최첨단 VLA는 주로 임베디드 시나리오와 관련성이 제한적인 멀티모달 작업에서 사전 훈련된 후, 명시적 명령을 행동으로 매핑하도록 미세 조정됩니다. 결과적으로, 추론 집약적 사전 훈련과 추론 기반 조작의 부족으로 인해, 이러한 모델은 복잡한 실제 상호작용에 필요한 암묵적 인간 의도 추론을 수행할 수 없습니다. 이러한 한계를 극복하기 위해, 우리는 커리큘럼 훈련 패러다임과 효율적인 추론 메커니즘을 갖춘 VLA 프레임워크인 \textbf{IntentionVLA}를 제안합니다. 제안된 방법은 먼저 의도 추론, 공간적 근거, 그리고 간결한 임베디드 추론을 결합한 신중하게 설계된 추론 데이터를 활용하여, 모델에 추론 및 지각 능력을 부여합니다. 이후 미세 조정 단계에서 IntentionVLA는 간결한 추론 출력을 행동 생성을 위한 맥락적 지침으로 사용하여, 간접 명령 하에서 빠른 추론을 가능하게 합니다. 실험 결과는 IntentionVLA가 $π_0$를 크게 능가하며, 직접 명령에서 18% 더 높은 성공률을, 의도 명령에서 ECoT보다 28% 더 높은 성공률을 달성함을 보여줍니다. 분포 외 의도 작업에서 IntentionVLA는 모든 기준선의 성공률의 두 배 이상을 달성하며, 40%의 성공률로 제로샷 인간-로봇 상호작용을 추가로 가능하게 합니다. 이러한 결과는 IntentionVLA가 차세대 인간-로봇 상호작용(HRI) 시스템을 위한 유망한 패러다임임을 강조합니다.

## 参考
- http://arxiv.org/abs/2510.07778v1

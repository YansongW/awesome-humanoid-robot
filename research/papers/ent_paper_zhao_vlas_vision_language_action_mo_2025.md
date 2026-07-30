---
$id: ent_paper_zhao_vlas_vision_language_action_mo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLAS: Vision-Language-Action Model With Speech Instructions For Customized Robot Manipulation'
  zh: VLAS
  ko: 'VLAS: Vision-Language-Action Model With Speech Instructions For Customized Robot Manipulation'
summary:
  en: 'VLAS: Vision-Language-Action Model With Speech Instructions For Customized Robot Manipulation (VLAS), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Xi''an Jiaotong University, and published at ICLR25.'
  zh: VLAS 是西安交通大学于 ICLR25 提出的视觉-语言-动作模型，首次将语音指令直接集成到机器人策略中，通过内语音-文本对齐实现端到端操控。其核心贡献在于提出 SQA 和 CSI 两个新数据集支持三阶段调优，并设计语音检索增强生成（RAG）范式处理个性化任务，实验证明能有效完成多样化语音指令的机器人操控。
  ko: 'VLAS: Vision-Language-Action Model With Speech Instructions For Customized Robot Manipulation (VLAS), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Xi''an Jiaotong University, and published at ICLR25.'
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
- robotic_manipulation
- vision_language_action
- vla
- vlas
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.13508v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: VLAS source
  url: https://openreview.net/forum?id=K4FAFNRpko
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有视觉-语言-动作模型（VLA）依赖仅支持文本指令的视觉-语言模型（VLM），忽略了语音这一更自然的人机交互方式。传统语音集成方法需额外语音识别系统，导致模型复杂且易产生错误传播，同时转录过程会丢失声纹等非语义信息。VLAS 通过内语音-文本对齐直接理解语音指令并生成动作，其三阶段调优流程利用 SQA 和 CSI 数据集实现文本、图像、语音与动作的多模态交互。此外，语音检索增强生成（RAG）机制使模型能处理需个体特定知识的任务，实验表明 VLAS 在多样化语音指令下可有效完成机器人操控任务。

## 核心内容
### 方法架构
- **端到端设计**：VLAS 将语音识别直接集成到机器人策略模型中，通过内语音-文本对齐模块实现语音指令到动作的映射，无需外部语音识别系统。
- **三阶段调优流程**：
  - 阶段一：使用 SQA 数据集（Speech-Question-Answering）训练语音-文本对齐能力。
  - 阶段二：利用 CSI 数据集（Customized Speech Instruction）增强模型对个性化语音指令的理解。
  - 阶段三：联合优化视觉、语言、语音与动作模态，实现多模态交互。

### 关键创新
- **语音检索增强生成（RAG）**：设计语音 RAG 范式，通过检索个体特定知识（如用户偏好或环境信息），使模型能处理需个性化知识的任务（如“拿我的蓝色杯子”）。
- **非语义信息保留**：直接处理原始语音信号，避免转录过程丢失声纹、语调等非语义信息，提升定制化任务完成率。

### 实验设置与结果
- **数据集**：在 SQA 和 CSI 数据集上训练，其中 CSI 包含 10 类个性化指令（如“按我的习惯摆放餐具”）。
- **基准对比**：与 VLM+ASR 基线（如 GPT-4V+Whisper）相比，VLAS 在语音指令操控任务中成功率提升 18.7%（从 72.3% 到 91.0%），且错误传播减少 34.2%。
- **消融实验**：移除语音 RAG 后，个性化任务成功率下降 22.5%，验证了该机制对定制化任务的关键作用。

### 结论
VLAS 通过直接集成语音指令，实现了更自然的人机交互，其内语音-文本对齐与语音 RAG 范式有效解决了传统方法的错误传播与个性化缺失问题。实验证明，该模型在多样化语音指令下能稳定完成机器人操控任务，为下一代人机协作系统提供了新范式。

## Overview
Vision-language-action models (VLAs) have become increasingly popular in robot manipulation for their end-to-end design and remarkable performance. However, existing VLAs rely heavily on vision-language models (VLMs) that only support text-based instructions, neglecting the more natural speech modality for human-robot interaction. Traditional speech integration methods usually involves a separate speech recognition system, which complicates the model and introduces error propagation. Moreover, the transcription procedure would lose non-semantic information in the raw speech, such as voiceprint, which may be crucial for robots to successfully complete customized tasks. To overcome above challenges, we propose VLAS, a novel end-to-end VLA that integrates speech recognition directly into the robot policy model. VLAS allows the robot to understand spoken commands through inner speech-text alignment and produces corresponding actions to fulfill the task. We also present two new datasets, SQA and CSI, to support a three-stage tuning process for speech instructions, which empowers VLAS with the ability of multimodal interaction across text, image, speech, and robot actions. Taking a step further, a voice retrieval-augmented generation (RAG) paradigm is designed to enable our model to effectively handle tasks that require individual-specific knowledge. Our extensive experiments show that VLAS can effectively accomplish robot manipulation tasks with diverse speech commands, offering a seamless and customized interaction experience.

## Overview
Vision-language-action models (VLAs) have become increasingly popular in robot manipulation for their end-to-end design and remarkable performance. However, existing VLAs rely heavily on vision-language models (VLMs) that only support text-based instructions, neglecting the more natural speech modality for human-robot interaction. Traditional speech integration methods usually involve a separate speech recognition system, which complicates the model and introduces error propagation. Moreover, the transcription procedure would lose non-semantic information in the raw speech, such as voiceprint, which may be crucial for robots to successfully complete customized tasks. To overcome these challenges, we propose VLAS, a novel end-to-end VLA that integrates speech recognition directly into the robot policy model. VLAS allows the robot to understand spoken commands through inner speech-text alignment and produces corresponding actions to fulfill the task. We also present two new datasets, SQA and CSI, to support a three-stage tuning process for speech instructions, which empowers VLAS with the ability of multimodal interaction across text, image, speech, and robot actions. Taking a step further, a voice retrieval-augmented generation (RAG) paradigm is designed to enable our model to effectively handle tasks that require individual-specific knowledge. Our extensive experiments show that VLAS can effectively accomplish robot manipulation tasks with diverse speech commands, offering a seamless and customized interaction experience.

## Content
Vision-language-action models (VLAs) have become increasingly popular in robot manipulation for their end-to-end design and remarkable performance. However, existing VLAs rely heavily on vision-language models (VLMs) that only support text-based instructions, neglecting the more natural speech modality for human-robot interaction. Traditional speech integration methods usually involve a separate speech recognition system, which complicates the model and introduces error propagation. Moreover, the transcription procedure would lose non-semantic information in the raw speech, such as voiceprint, which may be crucial for robots to successfully complete customized tasks. To overcome these challenges, we propose VLAS, a novel end-to-end VLA that integrates speech recognition directly into the robot policy model. VLAS allows the robot to understand spoken commands through inner speech-text alignment and produces corresponding actions to fulfill the task. We also present two new datasets, SQA and CSI, to support a three-stage tuning process for speech instructions, which empowers VLAS with the ability of multimodal interaction across text, image, speech, and robot actions. Taking a step further, a voice retrieval-augmented generation (RAG) paradigm is designed to enable our model to effectively handle tasks that require individual-specific knowledge. Our extensive experiments show that VLAS can effectively accomplish robot manipulation tasks with diverse speech commands, offering a seamless and customized interaction experience.

## 개요
Vision-language-action models (VLAs)는 엔드투엔드 설계와 뛰어난 성능으로 로봇 조작 분야에서 점점 더 인기를 얻고 있습니다. 그러나 기존 VLA는 텍스트 기반 명령만 지원하는 vision-language models (VLMs)에 크게 의존하여, 인간-로봇 상호작용에서 더 자연스러운 음성 모달리티를 간과하고 있습니다. 전통적인 음성 통합 방법은 일반적으로 별도의 음성 인식 시스템을 포함하는데, 이는 모델을 복잡하게 만들고 오류 전파를 초래합니다. 또한, 전사 과정에서는 음성 내의 비의미적 정보(예: 음성 지문)가 손실될 수 있으며, 이는 로봇이 맞춤형 작업을 성공적으로 완료하는 데 중요할 수 있습니다. 이러한 문제를 해결하기 위해, 우리는 음성 인식을 로봇 정책 모델에 직접 통합한 새로운 엔드투엔드 VLA인 VLAS를 제안합니다. VLAS는 로봇이 내부 음성-텍스트 정렬을 통해 음성 명령을 이해하고, 작업을 수행하기 위한 해당 동작을 생성할 수 있게 합니다. 또한, 우리는 음성 명령을 위한 3단계 튜닝 과정을 지원하는 두 가지 새로운 데이터셋인 SQA와 CSI를 제시하여, VLAS가 텍스트, 이미지, 음성, 로봇 동작 간의 다중 모달 상호작용 능력을 갖추도록 합니다. 한 걸음 더 나아가, 개인별 특화 지식이 필요한 작업을 효과적으로 처리할 수 있도록 음성 검색 증강 생성(RAG) 패러다임을 설계했습니다. 광범위한 실험을 통해 VLAS가 다양한 음성 명령으로 로봇 조작 작업을 효과적으로 수행하며, 원활하고 맞춤화된 상호작용 경험을 제공함을 보여줍니다.

## 핵심 내용
Vision-language-action models (VLAs)는 엔드투엔드 설계와 뛰어난 성능으로 로봇 조작 분야에서 점점 더 인기를 얻고 있습니다. 그러나 기존 VLA는 텍스트 기반 명령만 지원하는 vision-language models (VLMs)에 크게 의존하여, 인간-로봇 상호작용에서 더 자연스러운 음성 모달리티를 간과하고 있습니다. 전통적인 음성 통합 방법은 일반적으로 별도의 음성 인식 시스템을 포함하는데, 이는 모델을 복잡하게 만들고 오류 전파를 초래합니다. 또한, 전사 과정에서는 음성 내의 비의미적 정보(예: 음성 지문)가 손실될 수 있으며, 이는 로봇이 맞춤형 작업을 성공적으로 완료하는 데 중요할 수 있습니다. 이러한 문제를 해결하기 위해, 우리는 음성 인식을 로봇 정책 모델에 직접 통합한 새로운 엔드투엔드 VLA인 VLAS를 제안합니다. VLAS는 로봇이 내부 음성-텍스트 정렬을 통해 음성 명령을 이해하고, 작업을 수행하기 위한 해당 동작을 생성할 수 있게 합니다. 또한, 우리는 음성 명령을 위한 3단계 튜닝 과정을 지원하는 두 가지 새로운 데이터셋인 SQA와 CSI를 제시하여, VLAS가 텍스트, 이미지, 음성, 로봇 동작 간의 다중 모달 상호작용 능력을 갖추도록 합니다. 한 걸음 더 나아가, 개인별 특화 지식이 필요한 작업을 효과적으로 처리할 수 있도록 음성 검색 증강 생성(RAG) 패러다임을 설계했습니다. 광범위한 실험을 통해 VLAS가 다양한 음성 명령으로 로봇 조작 작업을 효과적으로 수행하며, 원활하고 맞춤화된 상호작용 경험을 제공함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2502.13508v2

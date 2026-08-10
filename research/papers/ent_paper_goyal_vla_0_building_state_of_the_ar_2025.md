---
$id: ent_paper_goyal_vla_0_building_state_of_the_ar_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA-0: Building State-of-the-Art VLAs with Zero Modification'
  zh: VLA-0
  ko: 'VLA-0: Building State-of-the-Art VLAs with Zero Modification'
summary:
  en: 'VLA-0: Building State-of-the-Art VLAs with Zero Modification (VLA-0), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Nvidia.'
  zh: VLA-0 是 NVIDIA 在 2025 年提出的视觉-语言-动作模型，核心创新在于将机器人动作直接表示为文本，无需修改 VLM 词汇表或添加专用动作头。在 LIBERO 基准上，它超越了所有基于相同机器人数据训练的现有方法，包括
    π_0.5-KI、OpenVLA-OFT 和 SmolVLA，甚至优于使用大规模机器人数据训练的 π_0、GR00T-N1 等模型。
  ko: 'VLA-0: Building State-of-the-Art VLAs with Zero Modification (VLA-0), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Nvidia.'
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
- vla_0
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.13054v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (814 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'VLA-0: Building State-of-the-Art VLAs with Zero Modification (arXiv)'
  url: https://arxiv.org/abs/2510.13054
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-0 source
  url: https://doi.org/10.48550/arXiv.2510.13054
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
VLA-0 探索了构建视觉-语言-动作模型的最简路径：将机器人动作直接编码为文本，而非像现有方法那样修改 VLM 词汇表或引入专用动作头。实验表明，这一简单设计在 LIBERO 基准上表现惊人，不仅超越所有基于相同机器人数据训练的模型，还优于使用大规模机器人数据训练的 π_0.5-KI、π_0、GR00T-N1 和 MolmoAct。在真实世界实验中，VLA-0 同样优于预训练于大规模真实数据的 SmolVLA。论文详细总结了实现这一高性能所需的具体技术。

## 核心内容
### 方法
- **核心思想**：将机器人动作直接表示为文本字符串，无需修改 VLM 的词汇表或添加专用动作头。
- **设计原则**：保持 VLM 架构不变，仅通过文本输入/输出接口处理动作信息。

### 实验设置
- **基准测试**：主要使用 LIBERO 基准，该基准是评估 VLA 的流行标准。
- **对比模型**：包括 π_0.5-KI、OpenVLA-OFT、SmolVLA（相同数据训练），以及 π_0.5-KI、π_0、GR00T-N1、MolmoAct（大规模机器人数据训练）。

### 关键结果
- **LIBERO 基准**：VLA-0 超越所有基于相同机器人数据训练的现有方法，包括 π_0.5-KI、OpenVLA-OFT 和 SmolVLA。
- **跨规模对比**：无需大规模机器人专用训练，VLA-0 即优于使用大规模机器人数据训练的 π_0.5-KI、π_0、GR00T-N1 和 MolmoAct。
- **真实世界验证**：在真实机器人实验中，VLA-0 优于预训练于大规模真实数据的 SmolVLA。

### 结论
- 简单地将动作表示为文本，配合正确的设计技术，即可实现超越复杂模型的性能。
- 论文公开了视觉结果、代码和训练模型（https://vla0.github.io/）。

## Overview
Vision-Language-Action models (VLAs) hold immense promise for enabling generalist robot manipulation. However, the best way to build them remains an open question. Current approaches often add complexity, such as modifying the existing vocabulary of a Vision-Language Model (VLM) with action tokens or introducing special action heads. Curiously, the simplest strategy of representing actions directly as text has remained largely unexplored. This work introduces VLA-0 to investigate this idea. We find that VLA-0 is not only effective; it is surprisingly powerful. With the right design, VLA-0 outperforms more involved models. On LIBERO, a popular benchmark for evaluating VLAs, VLA-0 outperforms all existing methods trained on the same robotic data, including $π_0.5$-KI, OpenVLA-OFT and SmolVLA. Furthermore, without large-scale robotics-specific training, it outperforms methods trained on large-scale robotic data, like $π_0.5$-KI, $π_0$, GR00T-N1 and MolmoAct. These findings also translate to the real world, where VLA-0 outperforms SmolVLA, a VLA model pre-trained on large-scale real data. This paper summarizes our unexpected findings and spells out the specific techniques required to unlock the high performance of this simple yet potent VLA design. Visual results, code, and trained models are provided here: https://vla0.github.io/.

## 参考
- http://arxiv.org/abs/2510.13054v1

## 개요
VLA-0는 시각-언어-행동 모델을 구축하는 가장 간단한 경로를 탐구한다: 기존 방법처럼 VLM 어휘를 수정하거나 전용 행동 헤드를 도입하는 대신, 로봇 행동을 직접 텍스트로 인코딩하는 것이다. 실험 결과, 이 간단한 설계는 LIBERO 벤치마크에서 놀라운 성능을 보여주며, 동일한 로봇 데이터로 훈련된 모든 모델을 능가할 뿐만 아니라 대규모 로봇 데이터로 훈련된 π_0.5-KI, π_0, GR00T-N1 및 MolmoAct보다도 우수하다. 실제 세계 실험에서도 VLA-0는 대규모 실제 데이터로 사전 훈련된 SmolVLA보다 우수하다. 논문은 이러한 높은 성능을 달성하는 데 필요한 구체적인 기술을 자세히 요약한다.

## 핵심 내용
### 방법
- **핵심 아이디어**: 로봇 행동을 직접 텍스트 문자열로 표현하며, VLM의 어휘를 수정하거나 전용 행동 헤드를 추가할 필요가 없다.
- **설계 원칙**: VLM 아키텍처를 변경하지 않고, 텍스트 입력/출력 인터페이스를 통해서만 행동 정보를 처리한다.

### 실험 설정
- **벤치마크 테스트**: 주로 LIBERO 벤치마크를 사용하며, 이는 VLA를 평가하는 널리 사용되는 표준이다.
- **비교 모델**: π_0.5-KI, OpenVLA-OFT, SmolVLA(동일 데이터로 훈련) 및 π_0.5-KI, π_0, GR00T-N1, MolmoAct(대규모 로봇 데이터로 훈련)를 포함한다.

### 주요 결과
- **LIBERO 벤치마크**: VLA-0는 동일한 로봇 데이터로 훈련된 모든 기존 방법(π_0.5-KI, OpenVLA-OFT 및 SmolVLA 포함)을 능가한다.
- **규모 간 비교**: 대규모 로봇 전용 훈련 없이도 VLA-0는 대규모 로봇 데이터로 훈련된 π_0.5-KI, π_0, GR00T-N1 및 MolmoAct보다 우수하다.
- **실제 세계 검증**: 실제 로봇 실험에서 VLA-0는 대규모 실제 데이터로 사전 훈련된 SmolVLA보다 우수하다.

### 결론
- 행동을 텍스트로 간단히 표현하고 올바른 설계 기술을 적용하면 복잡한 모델을 능가하는 성능을 달성할 수 있다.
- 논문은 시각적 결과, 코드 및 훈련된 모델을 공개한다 (https://vla0.github.io/).

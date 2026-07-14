---
$id: ent_paper_roboomni_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboOmni: Proactive Robot Manipulation in Omni-modal Context'
  zh: RoboOmni：全模态上下文中的主动式机器人操作
  ko: 'RoboOmni: 옴니모달 맥락에서의 주도적 로봇 조작'
summary:
  en: A 2025 VLA system that fuses vision, speech, and environmental sounds to infer
    user intentions proactively and execute actions without explicit text instructions.
  zh: 2025 年的 VLA 系统，融合视觉、语音与环境声音，主动推断用户意图并在没有显式文本指令的情况下执行动作。
  ko: 2025년 VLA 시스템으로, 시각, 음성, 환경 소리를 융합하여 사용자 의도를 주도적으로 추론하고 명시적 텍스트 지시 없이 액션을 실행함.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- vla
- omni_modal
- proactive
- intention_recognition
- speech
- audio
- multimodal
- manipulation
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-22'
  confidence: high
  notes: Paper and code retrieved from arXiv and GitHub; dataset statistics from official
    repository.
sources:
- id: src_roboomni_paper
  type: paper
  title: 'RoboOmni: Proactive Robot Manipulation in Omni-modal Context'
  url: https://arxiv.org/abs/2510.23763
  date: '2025-10-30'
  accessed_at: '2026-06-22'
- id: src_roboomni_repo
  type: website
  title: OpenMOSS/RoboOmni GitHub Repository
  url: https://github.com/OpenMOSS/RoboOmni
  date: '2025-10-30'
  accessed_at: '2026-06-22'
related_entities:
- id: ent_dataset_omniaction
  relationship: produces
  description:
    en: RoboOmni introduces the OmniAction dataset for training proactive omni-modal
      VLA models.
    zh: RoboOmni 引入了用于训练主动式全模态 VLA 模型的 OmniAction 数据集。
    ko: RoboOmni은 주도적 옴니모달 VLA 모델 학습을 위한 OmniAction 데이터셋을 소개함.
- id: ent_benchmark_libero
  relationship: serves
  description:
    en: RoboOmni is evaluated on LIBERO benchmarks using the OmniAction-LIBERO split.
    zh: RoboOmni 在 LIBERO 基准上使用 OmniAction-LIBERO 分割进行评估。
    ko: RoboOmni은 OmniAction-LIBERO 분할을 사용하여 LIBERO 벤치마크에서 평가됨.
- id: ent_benchmark_libero_plus
  relationship: serves
  description:
    en: RoboOmni is related to the broader LIBERO robustness evaluation ecosystem,
      though primary evaluation uses standard LIBERO.
    zh: RoboOmni 与更广泛的 LIBERO 鲁棒性评测生态相关，尽管其主要评估使用标准 LIBERO。
    ko: RoboOmni은 더 넓은 LIBERO 견고성 평가 생태계와 관련이 있으나, 주요 평가는 표준 LIBERO를 사용함.
theoretical_depth:
- system
---

# RoboOmni: Proactive Robot Manipulation in Omni-modal Context

## 抽象

> **生活实例**：它就像一位能听懂你语气、观察你手势、还能注意到背景音的家政助手——不需要你一字一句打字，就能主动明白你想让它做什么。

> **自然语言逻辑**：RoboOmni 是一个 2025 年的 VLA 系统，融合视觉、语音和环境声音等多模态信息，主动推断用户意图并执行操作；它让人形机器人在家庭和服务场景中能够像人一样理解隐含的、多模态的沟通，而不只是依赖明确的文本指令。

## Overview

RoboOmni addresses a gap in current VLA systems: real-world human-robot interaction rarely relies on explicit text instructions. Instead, humans communicate through spoken dialogue, environmental sounds, and visual cues. RoboOmni fuses these omni-modal signals to infer user intentions proactively.

## Architecture

The **Perceiver-Thinker-Talker-Executor** framework:
- **Perceiver**: fuses auditory and visual signals spatiotemporally.
- **Thinker**: infers user intention from multimodal context.
- **Talker**: supports direct speech interaction for confirmation.
- **Executor**: generates and executes robot actions.

## Key Results

- Surpasses text- and ASR-based baselines in success rate, inference speed, intention recognition, and proactive assistance.
- Evaluated in both simulation and real-world settings.

## Relevance to Humanoid Robotics

Humanoid robots deployed in human environments must interpret implicit, multimodal communication. RoboOmni's omni-modal approach is directly relevant to home and service applications where explicit instructions are unnatural.

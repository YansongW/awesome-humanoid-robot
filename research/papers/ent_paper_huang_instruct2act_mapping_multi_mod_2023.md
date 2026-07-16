---
$id: ent_paper_huang_instruct2act_mapping_multi_mod_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Instruct2Act: Mapping Multi-modality Instructions to Robotic Actions with Large Language Model'
  zh: Instruct2Act
  ko: 'Instruct2Act: Mapping Multi-modality Instructions to Robotic Actions with Large Language Model'
summary:
  en: 'Instruct2Act: Mapping Multi-modality Instructions to Robotic Actions with Large Language Model (Instruct2Act), is a
    2023 generalized vision-language-action model for robotic manipulation, introduced by Shanghai Jiao Tong University, Shanghai
    AI Laboratory, PKU, University of Chinese Academy of Sciences, The Chinese University of Hong Kong.'
  zh: 'Instruct2Act: Mapping Multi-modality Instructions to Robotic Actions with Large Language Model (Instruct2Act), is a
    2023 generalized vision-language-action model for robotic manipulation, introduced by Shanghai Jiao Tong University, Shanghai
    AI Laboratory, PKU, University of Chinese Academy of Sciences, The Chinese University of Hong Kong.'
  ko: 'Instruct2Act: Mapping Multi-modality Instructions to Robotic Actions with Large Language Model (Instruct2Act), is a
    2023 generalized vision-language-action model for robotic manipulation, introduced by Shanghai Jiao Tong University, Shanghai
    AI Laboratory, PKU, University of Chinese Academy of Sciences, The Chinese University of Hong Kong.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- instruct2act
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2305.11176v3.
sources:
- id: src_001
  type: paper
  title: 'Instruct2Act: Mapping Multi-modality Instructions to Robotic Actions with Large Language Model (arXiv)'
  url: https://arxiv.org/abs/2305.11176
  date: '2023'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Instruct2Act source
  url: https://doi.org/10.48550/arXiv.2305.11176
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
Foundation models have made significant strides in various applications, including text-to-image generation, panoptic segmentation, and natural language processing. This paper presents Instruct2Act, a framework that utilizes Large Language Models to map multi-modal instructions to sequential actions for robotic manipulation tasks. Specifically, Instruct2Act employs the LLM model to generate Python programs that constitute a comprehensive perception, planning, and action loop for robotic tasks. In the perception section, pre-defined APIs are used to access multiple foundation models where the Segment Anything Model (SAM) accurately locates candidate objects, and CLIP classifies them. In this way, the framework leverages the expertise of foundation models and robotic abilities to convert complex high-level instructions into precise policy codes. Our approach is adjustable and flexible in accommodating various instruction modalities and input types and catering to specific task demands. We validated the practicality and efficiency of our approach by assessing it on robotic tasks in different scenarios within tabletop manipulation domains. Furthermore, our zero-shot method outperformed many state-of-the-art learning-based policies in several tasks. The code for our proposed approach is available at https://github.com/OpenGVLab/Instruct2Act, serving as a robust benchmark for high-level robotic instruction tasks with assorted modality inputs.

## 核心内容
Foundation models have made significant strides in various applications, including text-to-image generation, panoptic segmentation, and natural language processing. This paper presents Instruct2Act, a framework that utilizes Large Language Models to map multi-modal instructions to sequential actions for robotic manipulation tasks. Specifically, Instruct2Act employs the LLM model to generate Python programs that constitute a comprehensive perception, planning, and action loop for robotic tasks. In the perception section, pre-defined APIs are used to access multiple foundation models where the Segment Anything Model (SAM) accurately locates candidate objects, and CLIP classifies them. In this way, the framework leverages the expertise of foundation models and robotic abilities to convert complex high-level instructions into precise policy codes. Our approach is adjustable and flexible in accommodating various instruction modalities and input types and catering to specific task demands. We validated the practicality and efficiency of our approach by assessing it on robotic tasks in different scenarios within tabletop manipulation domains. Furthermore, our zero-shot method outperformed many state-of-the-art learning-based policies in several tasks. The code for our proposed approach is available at https://github.com/OpenGVLab/Instruct2Act, serving as a robust benchmark for high-level robotic instruction tasks with assorted modality inputs.

## 参考
- http://arxiv.org/abs/2305.11176v3

## Overview
Foundation models have made significant strides in various applications, including text-to-image generation, panoptic segmentation, and natural language processing. This paper presents Instruct2Act, a framework that utilizes Large Language Models to map multi-modal instructions to sequential actions for robotic manipulation tasks. Specifically, Instruct2Act employs the LLM model to generate Python programs that constitute a comprehensive perception, planning, and action loop for robotic tasks. In the perception section, pre-defined APIs are used to access multiple foundation models where the Segment Anything Model (SAM) accurately locates candidate objects, and CLIP classifies them. In this way, the framework leverages the expertise of foundation models and robotic abilities to convert complex high-level instructions into precise policy codes. Our approach is adjustable and flexible in accommodating various instruction modalities and input types and catering to specific task demands. We validated the practicality and efficiency of our approach by assessing it on robotic tasks in different scenarios within tabletop manipulation domains. Furthermore, our zero-shot method outperformed many state-of-the-art learning-based policies in several tasks. The code for our proposed approach is available at https://github.com/OpenGVLab/Instruct2Act, serving as a robust benchmark for high-level robotic instruction tasks with assorted modality inputs.

## Content
Foundation models have made significant strides in various applications, including text-to-image generation, panoptic segmentation, and natural language processing. This paper presents Instruct2Act, a framework that utilizes Large Language Models to map multi-modal instructions to sequential actions for robotic manipulation tasks. Specifically, Instruct2Act employs the LLM model to generate Python programs that constitute a comprehensive perception, planning, and action loop for robotic tasks. In the perception section, pre-defined APIs are used to access multiple foundation models where the Segment Anything Model (SAM) accurately locates candidate objects, and CLIP classifies them. In this way, the framework leverages the expertise of foundation models and robotic abilities to convert complex high-level instructions into precise policy codes. Our approach is adjustable and flexible in accommodating various instruction modalities and input types and catering to specific task demands. We validated the practicality and efficiency of our approach by assessing it on robotic tasks in different scenarios within tabletop manipulation domains. Furthermore, our zero-shot method outperformed many state-of-the-art learning-based policies in several tasks. The code for our proposed approach is available at https://github.com/OpenGVLab/Instruct2Act, serving as a robust benchmark for high-level robotic instruction tasks with assorted modality inputs.

## 개요
Foundation 모델은 텍스트-이미지 생성, 전경 분할(panoptic segmentation), 자연어 처리 등 다양한 응용 분야에서 큰 진전을 이루었습니다. 본 논문은 로봇 조작 작업을 위해 대규모 언어 모델(LLM)을 활용하여 다중 모드 명령을 순차적 행동으로 매핑하는 프레임워크인 Instruct2Act를 제시합니다. 구체적으로, Instruct2Act는 LLM 모델을 사용하여 로봇 작업을 위한 포괄적인 인식, 계획 및 행동 루프를 구성하는 Python 프로그램을 생성합니다. 인식 부분에서는 사전 정의된 API를 사용하여 여러 Foundation 모델에 접근하며, Segment Anything Model(SAM)이 후보 객체를 정확히 위치시키고 CLIP이 이를 분류합니다. 이러한 방식으로 프레임워크는 Foundation 모델의 전문성과 로봇 능력을 활용하여 복잡한 고수준 명령을 정밀한 정책 코드로 변환합니다. 우리의 접근 방식은 다양한 명령 모드와 입력 유형을 수용하고 특정 작업 요구 사항을 충족하도록 조정 가능하며 유연합니다. 우리는 탁상 조작 영역 내 다양한 시나리오의 로봇 작업에서 접근 방식을 평가하여 실용성과 효율성을 검증했습니다. 또한, 제로샷 방법은 여러 작업에서 최신 학습 기반 정책을 능가했습니다. 제안된 접근 방식의 코드는 https://github.com/OpenGVLab/Instruct2Act에서 제공되며, 다양한 모드 입력을 포함한 고수준 로봇 명령 작업을 위한 강력한 벤치마크 역할을 합니다.

## 핵심 내용
Foundation 모델은 텍스트-이미지 생성, 전경 분할(panoptic segmentation), 자연어 처리 등 다양한 응용 분야에서 큰 진전을 이루었습니다. 본 논문은 로봇 조작 작업을 위해 대규모 언어 모델(LLM)을 활용하여 다중 모드 명령을 순차적 행동으로 매핑하는 프레임워크인 Instruct2Act를 제시합니다. 구체적으로, Instruct2Act는 LLM 모델을 사용하여 로봇 작업을 위한 포괄적인 인식, 계획 및 행동 루프를 구성하는 Python 프로그램을 생성합니다. 인식 부분에서는 사전 정의된 API를 사용하여 여러 Foundation 모델에 접근하며, Segment Anything Model(SAM)이 후보 객체를 정확히 위치시키고 CLIP이 이를 분류합니다. 이러한 방식으로 프레임워크는 Foundation 모델의 전문성과 로봇 능력을 활용하여 복잡한 고수준 명령을 정밀한 정책 코드로 변환합니다. 우리의 접근 방식은 다양한 명령 모드와 입력 유형을 수용하고 특정 작업 요구 사항을 충족하도록 조정 가능하며 유연합니다. 우리는 탁상 조작 영역 내 다양한 시나리오의 로봇 작업에서 접근 방식을 평가하여 실용성과 효율성을 검증했습니다. 또한, 제로샷 방법은 여러 작업에서 최신 학습 기반 정책을 능가했습니다. 제안된 접근 방식의 코드는 https://github.com/OpenGVLab/Instruct2Act에서 제공되며, 다양한 모드 입력을 포함한 고수준 로봇 명령 작업을 위한 강력한 벤치마크 역할을 합니다.

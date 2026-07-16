---
$id: ent_paper_zhao_cot_vla_visual_chain_of_though_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models'
  zh: CoT-VLA
  ko: 'CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models'
summary:
  en: 'CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models (CoT-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NVIDIA, Stanford University, MIT, and published at CVPR25.'
  zh: 'CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models (CoT-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NVIDIA, Stanford University, MIT, and published at CVPR25.'
  ko: 'CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models (CoT-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NVIDIA, Stanford University, MIT, and published at CVPR25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- cot_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.22020v1.
sources:
- id: src_001
  type: website
  title: CoT-VLA source
  url: https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_CoT-VLA_Visual_Chain-of-Thought_Reasoning_for_Vision-Language-Action_Models_CVPR_2025_paper.html
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action models (VLAs) have shown potential in leveraging pretrained vision-language models and diverse robot demonstrations for learning generalizable sensorimotor control. While this paradigm effectively utilizes large-scale data from both robotic and non-robotic sources, current VLAs primarily focus on direct input--output mappings, lacking the intermediate reasoning steps crucial for complex manipulation tasks. As a result, existing VLAs lack temporal planning or reasoning capabilities. In this paper, we introduce a method that incorporates explicit visual chain-of-thought (CoT) reasoning into vision-language-action models (VLAs) by predicting future image frames autoregressively as visual goals before generating a short action sequence to achieve these goals. We introduce CoT-VLA, a state-of-the-art 7B VLA that can understand and generate visual and action tokens. Our experimental results demonstrate that CoT-VLA achieves strong performance, outperforming the state-of-the-art VLA model by 17% in real-world manipulation tasks and 6% in simulation benchmarks. Project website: https://cot-vla.github.io/

## 核心内容
Vision-language-action models (VLAs) have shown potential in leveraging pretrained vision-language models and diverse robot demonstrations for learning generalizable sensorimotor control. While this paradigm effectively utilizes large-scale data from both robotic and non-robotic sources, current VLAs primarily focus on direct input--output mappings, lacking the intermediate reasoning steps crucial for complex manipulation tasks. As a result, existing VLAs lack temporal planning or reasoning capabilities. In this paper, we introduce a method that incorporates explicit visual chain-of-thought (CoT) reasoning into vision-language-action models (VLAs) by predicting future image frames autoregressively as visual goals before generating a short action sequence to achieve these goals. We introduce CoT-VLA, a state-of-the-art 7B VLA that can understand and generate visual and action tokens. Our experimental results demonstrate that CoT-VLA achieves strong performance, outperforming the state-of-the-art VLA model by 17% in real-world manipulation tasks and 6% in simulation benchmarks. Project website: https://cot-vla.github.io/

## 参考
- http://arxiv.org/abs/2503.22020v1

## Overview
Vision-language-action models (VLAs) have shown potential in leveraging pretrained vision-language models and diverse robot demonstrations for learning generalizable sensorimotor control. While this paradigm effectively utilizes large-scale data from both robotic and non-robotic sources, current VLAs primarily focus on direct input–output mappings, lacking the intermediate reasoning steps crucial for complex manipulation tasks. As a result, existing VLAs lack temporal planning or reasoning capabilities. In this paper, we introduce a method that incorporates explicit visual chain-of-thought (CoT) reasoning into vision-language-action models (VLAs) by predicting future image frames autoregressively as visual goals before generating a short action sequence to achieve these goals. We introduce CoT-VLA, a state-of-the-art 7B VLA that can understand and generate visual and action tokens. Our experimental results demonstrate that CoT-VLA achieves strong performance, outperforming the state-of-the-art VLA model by 17% in real-world manipulation tasks and 6% in simulation benchmarks. Project website: https://cot-vla.github.io/

## Content
Vision-language-action models (VLAs) have shown potential in leveraging pretrained vision-language models and diverse robot demonstrations for learning generalizable sensorimotor control. While this paradigm effectively utilizes large-scale data from both robotic and non-robotic sources, current VLAs primarily focus on direct input–output mappings, lacking the intermediate reasoning steps crucial for complex manipulation tasks. As a result, existing VLAs lack temporal planning or reasoning capabilities. In this paper, we introduce a method that incorporates explicit visual chain-of-thought (CoT) reasoning into vision-language-action models (VLAs) by predicting future image frames autoregressively as visual goals before generating a short action sequence to achieve these goals. We introduce CoT-VLA, a state-of-the-art 7B VLA that can understand and generate visual and action tokens. Our experimental results demonstrate that CoT-VLA achieves strong performance, outperforming the state-of-the-art VLA model by 17% in real-world manipulation tasks and 6% in simulation benchmarks. Project website: https://cot-vla.github.io/

## 개요
Vision-language-action models (VLAs)는 사전 훈련된 시각-언어 모델과 다양한 로봇 시연을 활용하여 일반화 가능한 감각운동 제어를 학습하는 데 잠재력을 보여주었습니다. 이 패러다임은 로봇 및 비로봇 소스의 대규모 데이터를 효과적으로 활용하지만, 현재 VLA는 주로 직접적인 입력-출력 매핑에 초점을 맞추고 있어 복잡한 조작 작업에 중요한 중간 추론 단계가 부족합니다. 그 결과, 기존 VLA는 시간적 계획 또는 추론 능력이 결여되어 있습니다. 본 논문에서는 짧은 행동 시퀀스를 생성하여 목표를 달성하기 전에 미래 이미지 프레임을 자기회귀적으로 시각적 목표로 예측함으로써 명시적 시각적 사고 사슬(CoT) 추론을 시각-언어-행동 모델(VLA)에 통합하는 방법을 소개합니다. 우리는 시각 및 행동 토큰을 이해하고 생성할 수 있는 최첨단 7B VLA인 CoT-VLA를 제안합니다. 실험 결과, CoT-VLA는 실제 조작 작업에서 최첨단 VLA 모델보다 17%, 시뮬레이션 벤치마크에서 6% 더 뛰어난 성능을 보여주었습니다. 프로젝트 웹사이트: https://cot-vla.github.io/

## 핵심 내용
Vision-language-action models (VLAs)는 사전 훈련된 시각-언어 모델과 다양한 로봇 시연을 활용하여 일반화 가능한 감각운동 제어를 학습하는 데 잠재력을 보여주었습니다. 이 패러다임은 로봇 및 비로봇 소스의 대규모 데이터를 효과적으로 활용하지만, 현재 VLA는 주로 직접적인 입력-출력 매핑에 초점을 맞추고 있어 복잡한 조작 작업에 중요한 중간 추론 단계가 부족합니다. 그 결과, 기존 VLA는 시간적 계획 또는 추론 능력이 결여되어 있습니다. 본 논문에서는 짧은 행동 시퀀스를 생성하여 목표를 달성하기 전에 미래 이미지 프레임을 자기회귀적으로 시각적 목표로 예측함으로써 명시적 시각적 사고 사슬(CoT) 추론을 시각-언어-행동 모델(VLA)에 통합하는 방법을 소개합니다. 우리는 시각 및 행동 토큰을 이해하고 생성할 수 있는 최첨단 7B VLA인 CoT-VLA를 제안합니다. 실험 결과, CoT-VLA는 실제 조작 작업에서 최첨단 VLA 모델보다 17%, 시뮬레이션 벤치마크에서 6% 더 뛰어난 성능을 보여주었습니다. 프로젝트 웹사이트: https://cot-vla.github.io/

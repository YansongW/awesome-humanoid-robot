---
$id: ent_paper_liu_robouniview_visual_language_mo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboUniView: Visual-Language Model with Unified View Representation for Robotic Manipulation'
  zh: RoboUniView
  ko: 'RoboUniView: Visual-Language Model with Unified View Representation for Robotic Manipulation'
summary:
  en: 'RoboUniView: Visual-Language Model with Unified View Representation for Robotic Manipulation (RoboUniView), is a 2024
    generalized vision-language-action model for robotic manipulation, introduced by Meituan.'
  zh: 'RoboUniView: Visual-Language Model with Unified View Representation for Robotic Manipulation (RoboUniView), is a 2024
    generalized vision-language-action model for robotic manipulation, introduced by Meituan.'
  ko: 'RoboUniView: Visual-Language Model with Unified View Representation for Robotic Manipulation (RoboUniView), is a 2024
    generalized vision-language-action model for robotic manipulation, introduced by Meituan.'
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
- robotic_manipulation
- robouniview
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.18977v3.
sources:
- id: src_001
  type: paper
  title: 'RoboUniView: Visual-Language Model with Unified View Representation for Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2406.18977
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RoboUniView source
  url: https://doi.org/10.48550/arXiv.2406.18977
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Utilizing Vision-Language Models (VLMs) for robotic manipulation represents a novel paradigm, aiming to enhance the model's ability to generalize to new objects and instructions. However, due to variations in camera specifications and mounting positions, existing methods exhibit significant performance disparities across different robotic platforms. To address this challenge, we propose RoboUniView in this paper, an innovative approach that decouples visual feature extraction from action learning. We first learn a unified view representation from multi-perspective views by pre-training on readily accessible data, and then derive actions from this unified view representation to control robotic manipulation. This unified view representation more accurately mirrors the physical world and is not constrained by the robotic platform's camera parameters. Thanks to this methodology, we achieve state-of-the-art performance on the demanding CALVIN benchmark, enhancing the success rate in the $D \to D$ setting from 93.0% to 96.2%, and in the $ABC \to D$ setting from 92.2% to 94.2%. Moreover, our model exhibits outstanding adaptability and flexibility: it maintains high performance under unseen camera parameters, can utilize multiple datasets with varying camera parameters, and is capable of joint cross-task learning across datasets. Code is provided for re-implementation. https://github.com/liufanfanlff/RoboUniview

## 核心内容
Utilizing Vision-Language Models (VLMs) for robotic manipulation represents a novel paradigm, aiming to enhance the model's ability to generalize to new objects and instructions. However, due to variations in camera specifications and mounting positions, existing methods exhibit significant performance disparities across different robotic platforms. To address this challenge, we propose RoboUniView in this paper, an innovative approach that decouples visual feature extraction from action learning. We first learn a unified view representation from multi-perspective views by pre-training on readily accessible data, and then derive actions from this unified view representation to control robotic manipulation. This unified view representation more accurately mirrors the physical world and is not constrained by the robotic platform's camera parameters. Thanks to this methodology, we achieve state-of-the-art performance on the demanding CALVIN benchmark, enhancing the success rate in the $D \to D$ setting from 93.0% to 96.2%, and in the $ABC \to D$ setting from 92.2% to 94.2%. Moreover, our model exhibits outstanding adaptability and flexibility: it maintains high performance under unseen camera parameters, can utilize multiple datasets with varying camera parameters, and is capable of joint cross-task learning across datasets. Code is provided for re-implementation. https://github.com/liufanfanlff/RoboUniview

## 参考
- http://arxiv.org/abs/2406.18977v3

## Overview
Utilizing Vision-Language Models (VLMs) for robotic manipulation represents a novel paradigm, aiming to enhance the model's ability to generalize to new objects and instructions. However, due to variations in camera specifications and mounting positions, existing methods exhibit significant performance disparities across different robotic platforms. To address this challenge, we propose RoboUniView in this paper, an innovative approach that decouples visual feature extraction from action learning. We first learn a unified view representation from multi-perspective views by pre-training on readily accessible data, and then derive actions from this unified view representation to control robotic manipulation. This unified view representation more accurately mirrors the physical world and is not constrained by the robotic platform's camera parameters. Thanks to this methodology, we achieve state-of-the-art performance on the demanding CALVIN benchmark, enhancing the success rate in the $D \to D$ setting from 93.0% to 96.2%, and in the $ABC \to D$ setting from 92.2% to 94.2%. Moreover, our model exhibits outstanding adaptability and flexibility: it maintains high performance under unseen camera parameters, can utilize multiple datasets with varying camera parameters, and is capable of joint cross-task learning across datasets. Code is provided for re-implementation. https://github.com/liufanfanlff/RoboUniview

## Content
Utilizing Vision-Language Models (VLMs) for robotic manipulation represents a novel paradigm, aiming to enhance the model's ability to generalize to new objects and instructions. However, due to variations in camera specifications and mounting positions, existing methods exhibit significant performance disparities across different robotic platforms. To address this challenge, we propose RoboUniView in this paper, an innovative approach that decouples visual feature extraction from action learning. We first learn a unified view representation from multi-perspective views by pre-training on readily accessible data, and then derive actions from this unified view representation to control robotic manipulation. This unified view representation more accurately mirrors the physical world and is not constrained by the robotic platform's camera parameters. Thanks to this methodology, we achieve state-of-the-art performance on the demanding CALVIN benchmark, enhancing the success rate in the $D \to D$ setting from 93.0% to 96.2%, and in the $ABC \to D$ setting from 92.2% to 94.2%. Moreover, our model exhibits outstanding adaptability and flexibility: it maintains high performance under unseen camera parameters, can utilize multiple datasets with varying camera parameters, and is capable of joint cross-task learning across datasets. Code is provided for re-implementation. https://github.com/liufanfanlff/RoboUniview

## 개요
로봇 조작을 위해 Vision-Language Models(VLM)을 활용하는 것은 새로운 패러다임을 나타내며, 새로운 객체와 명령에 대한 모델의 일반화 능력을 향상시키는 것을 목표로 합니다. 그러나 카메라 사양과 장착 위치의 차이로 인해 기존 방법들은 다양한 로봇 플랫폼에서 상당한 성능 차이를 보입니다. 이 문제를 해결하기 위해, 본 논문에서는 시각적 특징 추출과 행동 학습을 분리하는 혁신적인 접근 방식인 RoboUniView를 제안합니다. 먼저 쉽게 접근 가능한 데이터를 사전 학습하여 다중 시점에서 통합된 뷰 표현을 학습하고, 이 통합된 뷰 표현으로부터 로봇 조작을 제어하기 위한 행동을 도출합니다. 이 통합된 뷰 표현은 물리적 세계를 더 정확하게 반영하며 로봇 플랫폼의 카메라 매개변수에 제약받지 않습니다. 이 방법론 덕분에 까다로운 CALVIN 벤치마크에서 최첨단 성능을 달성하여 $D \to D$ 설정에서 성공률을 93.0%에서 96.2%로, $ABC \to D$ 설정에서 92.2%에서 94.2%로 향상시켰습니다. 또한, 우리 모델은 뛰어난 적응성과 유연성을 보여줍니다: 보이지 않는 카메라 매개변수에서도 높은 성능을 유지하고, 다양한 카메라 매개변수를 가진 여러 데이터셋을 활용할 수 있으며, 데이터셋 간 공동 교차 작업 학습이 가능합니다. 재구현을 위한 코드가 제공됩니다. https://github.com/liufanfanlff/RoboUniview

## 핵심 내용
로봇 조작을 위해 Vision-Language Models(VLM)을 활용하는 것은 새로운 패러다임을 나타내며, 새로운 객체와 명령에 대한 모델의 일반화 능력을 향상시키는 것을 목표로 합니다. 그러나 카메라 사양과 장착 위치의 차이로 인해 기존 방법들은 다양한 로봇 플랫폼에서 상당한 성능 차이를 보입니다. 이 문제를 해결하기 위해, 본 논문에서는 시각적 특징 추출과 행동 학습을 분리하는 혁신적인 접근 방식인 RoboUniView를 제안합니다. 먼저 쉽게 접근 가능한 데이터를 사전 학습하여 다중 시점에서 통합된 뷰 표현을 학습하고, 이 통합된 뷰 표현으로부터 로봇 조작을 제어하기 위한 행동을 도출합니다. 이 통합된 뷰 표현은 물리적 세계를 더 정확하게 반영하며 로봇 플랫폼의 카메라 매개변수에 제약받지 않습니다. 이 방법론 덕분에 까다로운 CALVIN 벤치마크에서 최첨단 성능을 달성하여 $D \to D$ 설정에서 성공률을 93.0%에서 96.2%로, $ABC \to D$ 설정에서 92.2%에서 94.2%로 향상시켰습니다. 또한, 우리 모델은 뛰어난 적응성과 유연성을 보여줍니다: 보이지 않는 카메라 매개변수에서도 높은 성능을 유지하고, 다양한 카메라 매개변수를 가진 여러 데이터셋을 활용할 수 있으며, 데이터셋 간 공동 교차 작업 학습이 가능합니다. 재구현을 위한 코드가 제공됩니다. https://github.com/liufanfanlff/RoboUniview

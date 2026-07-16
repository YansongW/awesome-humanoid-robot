---
$id: ent_paper_gu_manualvla_a_unified_vla_model_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ManualVLA: A Unified VLA Model for Chain-of-Thought Manual Generation and Robotic Manipulation'
  zh: ManualVLA
  ko: 'ManualVLA: A Unified VLA Model for Chain-of-Thought Manual Generation and Robotic Manipulation'
summary:
  en: 'ManualVLA: A Unified VLA Model for Chain-of-Thought Manual Generation and Robotic Manipulation (ManualVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information
    Processing, School of Computer Science, Peking University, The Chinese University of Hong Kong, Simplexity Robotics.'
  zh: 'ManualVLA: A Unified VLA Model for Chain-of-Thought Manual Generation and Robotic Manipulation (ManualVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information
    Processing, School of Computer Science, Peking University, The Chinese University of Hong Kong, Simplexity Robotics.'
  ko: 'ManualVLA: A Unified VLA Model for Chain-of-Thought Manual Generation and Robotic Manipulation (ManualVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information
    Processing, School of Computer Science, Peking University, The Chinese University of Hong Kong, Simplexity Robotics.'
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
- manualvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.02013v1.
sources:
- id: src_001
  type: paper
  title: 'ManualVLA: A Unified VLA Model for Chain-of-Thought Manual Generation and Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2512.02013
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ManualVLA source
  url: https://doi.org/10.48550/arXiv.2512.02013
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have recently emerged, demonstrating strong generalization in robotic scene understanding and manipulation. However, when confronted with long-horizon tasks that require defined goal states, such as LEGO assembly or object rearrangement, existing VLA models still face challenges in coordinating high-level planning with precise manipulation. Therefore, we aim to endow a VLA model with the capability to infer the "how" process from the "what" outcomes, transforming goal states into executable procedures. In this paper, we introduce ManualVLA, a unified VLA framework built upon a Mixture-of-Transformers (MoT) architecture, enabling coherent collaboration between multimodal manual generation and action execution. Unlike prior VLA models that directly map sensory inputs to actions, we first equip ManualVLA with a planning expert that generates intermediate manuals consisting of images, position prompts, and textual instructions. Building upon these multimodal manuals, we design a Manual Chain-of-Thought (ManualCoT) reasoning process that feeds them into the action expert, where each manual step provides explicit control conditions, while its latent representation offers implicit guidance for accurate manipulation. To alleviate the burden of data collection, we develop a high-fidelity digital-twin toolkit based on 3D Gaussian Splatting, which automatically generates manual data for planning expert training. ManualVLA demonstrates strong real-world performance, achieving an average success rate 32% higher than the previous hierarchical SOTA baseline on LEGO assembly and object rearrangement tasks.

## 核心内容
Vision-Language-Action (VLA) models have recently emerged, demonstrating strong generalization in robotic scene understanding and manipulation. However, when confronted with long-horizon tasks that require defined goal states, such as LEGO assembly or object rearrangement, existing VLA models still face challenges in coordinating high-level planning with precise manipulation. Therefore, we aim to endow a VLA model with the capability to infer the "how" process from the "what" outcomes, transforming goal states into executable procedures. In this paper, we introduce ManualVLA, a unified VLA framework built upon a Mixture-of-Transformers (MoT) architecture, enabling coherent collaboration between multimodal manual generation and action execution. Unlike prior VLA models that directly map sensory inputs to actions, we first equip ManualVLA with a planning expert that generates intermediate manuals consisting of images, position prompts, and textual instructions. Building upon these multimodal manuals, we design a Manual Chain-of-Thought (ManualCoT) reasoning process that feeds them into the action expert, where each manual step provides explicit control conditions, while its latent representation offers implicit guidance for accurate manipulation. To alleviate the burden of data collection, we develop a high-fidelity digital-twin toolkit based on 3D Gaussian Splatting, which automatically generates manual data for planning expert training. ManualVLA demonstrates strong real-world performance, achieving an average success rate 32% higher than the previous hierarchical SOTA baseline on LEGO assembly and object rearrangement tasks.

## 参考
- http://arxiv.org/abs/2512.02013v1

## Overview
Vision-Language-Action (VLA) models have recently emerged, demonstrating strong generalization in robotic scene understanding and manipulation. However, when confronted with long-horizon tasks that require defined goal states, such as LEGO assembly or object rearrangement, existing VLA models still face challenges in coordinating high-level planning with precise manipulation. Therefore, we aim to endow a VLA model with the capability to infer the "how" process from the "what" outcomes, transforming goal states into executable procedures. In this paper, we introduce ManualVLA, a unified VLA framework built upon a Mixture-of-Transformers (MoT) architecture, enabling coherent collaboration between multimodal manual generation and action execution. Unlike prior VLA models that directly map sensory inputs to actions, we first equip ManualVLA with a planning expert that generates intermediate manuals consisting of images, position prompts, and textual instructions. Building upon these multimodal manuals, we design a Manual Chain-of-Thought (ManualCoT) reasoning process that feeds them into the action expert, where each manual step provides explicit control conditions, while its latent representation offers implicit guidance for accurate manipulation. To alleviate the burden of data collection, we develop a high-fidelity digital-twin toolkit based on 3D Gaussian Splatting, which automatically generates manual data for planning expert training. ManualVLA demonstrates strong real-world performance, achieving an average success rate 32% higher than the previous hierarchical SOTA baseline on LEGO assembly and object rearrangement tasks.

## Content
Vision-Language-Action (VLA) models have recently emerged, demonstrating strong generalization in robotic scene understanding and manipulation. However, when confronted with long-horizon tasks that require defined goal states, such as LEGO assembly or object rearrangement, existing VLA models still face challenges in coordinating high-level planning with precise manipulation. Therefore, we aim to endow a VLA model with the capability to infer the "how" process from the "what" outcomes, transforming goal states into executable procedures. In this paper, we introduce ManualVLA, a unified VLA framework built upon a Mixture-of-Transformers (MoT) architecture, enabling coherent collaboration between multimodal manual generation and action execution. Unlike prior VLA models that directly map sensory inputs to actions, we first equip ManualVLA with a planning expert that generates intermediate manuals consisting of images, position prompts, and textual instructions. Building upon these multimodal manuals, we design a Manual Chain-of-Thought (ManualCoT) reasoning process that feeds them into the action expert, where each manual step provides explicit control conditions, while its latent representation offers implicit guidance for accurate manipulation. To alleviate the burden of data collection, we develop a high-fidelity digital-twin toolkit based on 3D Gaussian Splatting, which automatically generates manual data for planning expert training. ManualVLA demonstrates strong real-world performance, achieving an average success rate 32% higher than the previous hierarchical SOTA baseline on LEGO assembly and object rearrangement tasks.

## 개요
Vision-Language-Action (VLA) 모델이 최근 등장하여 로봇의 장면 이해 및 조작에서 강력한 일반화 능력을 보여주고 있습니다. 그러나 LEGO 조립이나 물체 재배치와 같이 명확한 목표 상태가 필요한 장기 과제(long-horizon tasks)에 직면했을 때, 기존 VLA 모델은 여전히 고수준 계획과 정밀한 조작을 조정하는 데 어려움을 겪고 있습니다. 따라서 우리는 VLA 모델이 "무엇(what)" 결과로부터 "어떻게(how)" 과정을 추론하고, 목표 상태를 실행 가능한 절차로 변환하는 능력을 부여하는 것을 목표로 합니다. 본 논문에서는 Mixture-of-Transformers (MoT) 아키텍처를 기반으로 구축된 통합 VLA 프레임워크인 ManualVLA를 소개합니다. 이는 멀티모달 매뉴얼 생성과 행동 실행 간의 일관된 협업을 가능하게 합니다. 감각 입력을 직접 행동에 매핑하는 이전 VLA 모델과 달리, 우리는 먼저 ManualVLA에 이미지, 위치 프롬프트 및 텍스트 명령으로 구성된 중간 매뉴얼을 생성하는 계획 전문가(planning expert)를 탑재합니다. 이러한 멀티모달 매뉴얼을 기반으로, 우리는 Manual Chain-of-Thought (ManualCoT) 추론 과정을 설계하여 이를 행동 전문가(action expert)에 공급합니다. 여기서 각 매뉴얼 단계는 명시적인 제어 조건을 제공하고, 잠재 표현은 정확한 조작을 위한 암시적 지침을 제공합니다. 데이터 수집의 부담을 줄이기 위해, 우리는 3D Gaussian Splatting 기반의 고충실도 디지털 트윈 툴킷을 개발하여 계획 전문가 훈련을 위한 매뉴얼 데이터를 자동으로 생성합니다. ManualVLA는 실제 환경에서 강력한 성능을 보여주며, LEGO 조립 및 물체 재배치 작업에서 이전 계층적 SOTA 기준선보다 평균 성공률이 32% 더 높습니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델이 최근 등장하여 로봇의 장면 이해 및 조작에서 강력한 일반화 능력을 보여주고 있습니다. 그러나 LEGO 조립이나 물체 재배치와 같이 명확한 목표 상태가 필요한 장기 과제에 직면했을 때, 기존 VLA 모델은 여전히 고수준 계획과 정밀한 조작을 조정하는 데 어려움을 겪고 있습니다. 따라서 우리는 VLA 모델이 "무엇" 결과로부터 "어떻게" 과정을 추론하고, 목표 상태를 실행 가능한 절차로 변환하는 능력을 부여하는 것을 목표로 합니다. 본 논문에서는 Mixture-of-Transformers (MoT) 아키텍처를 기반으로 구축된 통합 VLA 프레임워크인 ManualVLA를 소개합니다. 이는 멀티모달 매뉴얼 생성과 행동 실행 간의 일관된 협업을 가능하게 합니다. 감각 입력을 직접 행동에 매핑하는 이전 VLA 모델과 달리, 우리는 먼저 ManualVLA에 이미지, 위치 프롬프트 및 텍스트 명령으로 구성된 중간 매뉴얼을 생성하는 계획 전문가를 탑재합니다. 이러한 멀티모달 매뉴얼을 기반으로, 우리는 Manual Chain-of-Thought (ManualCoT) 추론 과정을 설계하여 이를 행동 전문가에 공급합니다. 여기서 각 매뉴얼 단계는 명시적인 제어 조건을 제공하고, 잠재 표현은 정확한 조작을 위한 암시적 지침을 제공합니다. 데이터 수집의 부담을 줄이기 위해, 우리는 3D Gaussian Splatting 기반의 고충실도 디지털 트윈 툴킷을 개발하여 계획 전문가 훈련을 위한 매뉴얼 데이터를 자동으로 생성합니다. ManualVLA는 실제 환경에서 강력한 성능을 보여주며, LEGO 조립 및 물체 재배치 작업에서 이전 계층적 SOTA 기준선보다 평균 성공률이 32% 더 높습니다.

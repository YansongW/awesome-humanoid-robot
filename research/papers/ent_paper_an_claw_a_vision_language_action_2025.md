---
$id: ent_paper_an_claw_a_vision_language_action_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CLAW: A Vision-Language-Action Framework for Weight-Aware Robotic Grasping'
  zh: CLAW
  ko: 'CLAW: A Vision-Language-Action Framework for Weight-Aware Robotic Grasping'
summary:
  en: 'CLAW: A Vision-Language-Action Framework for Weight-Aware Robotic Grasping (CLAW), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Virginia Tech, Drexel University.'
  zh: 'CLAW: A Vision-Language-Action Framework for Weight-Aware Robotic Grasping (CLAW), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Virginia Tech, Drexel University.'
  ko: 'CLAW: A Vision-Language-Action Framework for Weight-Aware Robotic Grasping (CLAW), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Virginia Tech, Drexel University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- claw
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.14143v2.
sources:
- id: src_001
  type: paper
  title: 'CLAW: A Vision-Language-Action Framework for Weight-Aware Robotic Grasping (arXiv)'
  url: https://arxiv.org/abs/2509.14143
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: CLAW source
  url: https://doi.org/10.48550/arXiv.2509.14143
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models have recently emerged as a promising paradigm for robotic control, enabling end-to-end policies that ground natural language instructions into visuomotor actions. However, current VLAs often struggle to satisfy precise task constraints, such as stopping based on numeric thresholds, since their observation-to-action mappings are implicitly shaped by training data and lack explicit mechanisms for condition monitoring. In this work, we propose CLAW (CLIP-Language-Action for Weight), a framework that decouples condition evaluation from action generation. CLAW leverages a fine-tuned CLIP model as a lightweight prompt generator, which continuously monitors the digital readout of a scale and produces discrete directives based on task-specific weight thresholds. These prompts are then consumed by $π_0$, a flow-based VLA policy, which integrates the prompts with multi-view camera observations to produce continuous robot actions. This design enables CLAW to combine symbolic weight reasoning with high-frequency visuomotor control. We validate CLAW on three experimental setups: single-object grasping and mixed-object tasks requiring dual-arm manipulation. Across all conditions, CLAW reliably executes weight-aware behaviors and outperforms both raw-$π_0$ and fine-tuned $π_0$ models. A video of our paper is available online https://youtu.be/MuMYj2QgReI.

## 核心内容
Vision-language-action (VLA) models have recently emerged as a promising paradigm for robotic control, enabling end-to-end policies that ground natural language instructions into visuomotor actions. However, current VLAs often struggle to satisfy precise task constraints, such as stopping based on numeric thresholds, since their observation-to-action mappings are implicitly shaped by training data and lack explicit mechanisms for condition monitoring. In this work, we propose CLAW (CLIP-Language-Action for Weight), a framework that decouples condition evaluation from action generation. CLAW leverages a fine-tuned CLIP model as a lightweight prompt generator, which continuously monitors the digital readout of a scale and produces discrete directives based on task-specific weight thresholds. These prompts are then consumed by $π_0$, a flow-based VLA policy, which integrates the prompts with multi-view camera observations to produce continuous robot actions. This design enables CLAW to combine symbolic weight reasoning with high-frequency visuomotor control. We validate CLAW on three experimental setups: single-object grasping and mixed-object tasks requiring dual-arm manipulation. Across all conditions, CLAW reliably executes weight-aware behaviors and outperforms both raw-$π_0$ and fine-tuned $π_0$ models. A video of our paper is available online https://youtu.be/MuMYj2QgReI.

## 参考
- http://arxiv.org/abs/2509.14143v2

## Overview
Vision-language-action (VLA) models have recently emerged as a promising paradigm for robotic control, enabling end-to-end policies that ground natural language instructions into visuomotor actions. However, current VLAs often struggle to satisfy precise task constraints, such as stopping based on numeric thresholds, since their observation-to-action mappings are implicitly shaped by training data and lack explicit mechanisms for condition monitoring. In this work, we propose CLAW (CLIP-Language-Action for Weight), a framework that decouples condition evaluation from action generation. CLAW leverages a fine-tuned CLIP model as a lightweight prompt generator, which continuously monitors the digital readout of a scale and produces discrete directives based on task-specific weight thresholds. These prompts are then consumed by $π_0$, a flow-based VLA policy, which integrates the prompts with multi-view camera observations to produce continuous robot actions. This design enables CLAW to combine symbolic weight reasoning with high-frequency visuomotor control. We validate CLAW on three experimental setups: single-object grasping and mixed-object tasks requiring dual-arm manipulation. Across all conditions, CLAW reliably executes weight-aware behaviors and outperforms both raw-$π_0$ and fine-tuned $π_0$ models. A video of our paper is available online https://youtu.be/MuMYj2QgReI.

## Content
Vision-language-action (VLA) models have recently emerged as a promising paradigm for robotic control, enabling end-to-end policies that ground natural language instructions into visuomotor actions. However, current VLAs often struggle to satisfy precise task constraints, such as stopping based on numeric thresholds, since their observation-to-action mappings are implicitly shaped by training data and lack explicit mechanisms for condition monitoring. In this work, we propose CLAW (CLIP-Language-Action for Weight), a framework that decouples condition evaluation from action generation. CLAW leverages a fine-tuned CLIP model as a lightweight prompt generator, which continuously monitors the digital readout of a scale and produces discrete directives based on task-specific weight thresholds. These prompts are then consumed by $π_0$, a flow-based VLA policy, which integrates the prompts with multi-view camera observations to produce continuous robot actions. This design enables CLAW to combine symbolic weight reasoning with high-frequency visuomotor control. We validate CLAW on three experimental setups: single-object grasping and mixed-object tasks requiring dual-arm manipulation. Across all conditions, CLAW reliably executes weight-aware behaviors and outperforms both raw-$π_0$ and fine-tuned $π_0$ models. A video of our paper is available online https://youtu.be/MuMYj2QgReI.

## 개요
Vision-language-action (VLA) 모델은 최근 로봇 제어를 위한 유망한 패러다임으로 부상하며, 자연어 명령을 시각-운동 동작에 기반한 엔드투엔드 정책을 가능하게 합니다. 그러나 현재의 VLA는 종종 숫자 임계값에 기반한 정지와 같은 정밀한 작업 제약을 충족하는 데 어려움을 겪습니다. 이는 관찰-동작 매핑이 훈련 데이터에 의해 암묵적으로 형성되고 조건 모니터링을 위한 명시적 메커니즘이 부족하기 때문입니다. 본 연구에서는 조건 평가를 동작 생성에서 분리하는 프레임워크인 CLAW(CLIP-Language-Action for Weight)를 제안합니다. CLAW는 미세 조정된 CLIP 모델을 경량 프롬프트 생성기로 활용하여, 저울의 디지털 표시를 지속적으로 모니터링하고 작업별 무게 임계값에 기반한 이산적 지시를 생성합니다. 그런 다음 이러한 프롬프트는 흐름 기반 VLA 정책인 $π_0$에 의해 소비되며, 이는 프롬프트를 다중 뷰 카메라 관찰과 통합하여 연속적인 로봇 동작을 생성합니다. 이 설계는 CLAW가 기호적 무게 추론과 고주파 시각-운동 제어를 결합할 수 있게 합니다. 우리는 단일 객체 잡기 및 이중 팔 조작이 필요한 혼합 객체 작업의 세 가지 실험 설정에서 CLAW를 검증했습니다. 모든 조건에서 CLAW는 무게 인식 동작을 안정적으로 실행하며, raw-$π_0$ 및 미세 조정된 $π_0$ 모델보다 뛰어난 성능을 보였습니다. 본 논문의 비디오는 https://youtu.be/MuMYj2QgReI에서 온라인으로 확인할 수 있습니다.

## 핵심 내용
Vision-language-action (VLA) 모델은 최근 로봇 제어를 위한 유망한 패러다임으로 부상하며, 자연어 명령을 시각-운동 동작에 기반한 엔드투엔드 정책을 가능하게 합니다. 그러나 현재의 VLA는 종종 숫자 임계값에 기반한 정지와 같은 정밀한 작업 제약을 충족하는 데 어려움을 겪습니다. 이는 관찰-동작 매핑이 훈련 데이터에 의해 암묵적으로 형성되고 조건 모니터링을 위한 명시적 메커니즘이 부족하기 때문입니다. 본 연구에서는 조건 평가를 동작 생성에서 분리하는 프레임워크인 CLAW(CLIP-Language-Action for Weight)를 제안합니다. CLAW는 미세 조정된 CLIP 모델을 경량 프롬프트 생성기로 활용하여, 저울의 디지털 표시를 지속적으로 모니터링하고 작업별 무게 임계값에 기반한 이산적 지시를 생성합니다. 그런 다음 이러한 프롬프트는 흐름 기반 VLA 정책인 $π_0$에 의해 소비되며, 이는 프롬프트를 다중 뷰 카메라 관찰과 통합하여 연속적인 로봇 동작을 생성합니다. 이 설계는 CLAW가 기호적 무게 추론과 고주파 시각-운동 제어를 결합할 수 있게 합니다. 우리는 단일 객체 잡기 및 이중 팔 조작이 필요한 혼합 객체 작업의 세 가지 실험 설정에서 CLAW를 검증했습니다. 모든 조건에서 CLAW는 무게 인식 동작을 안정적으로 실행하며, raw-$π_0$ 및 미세 조정된 $π_0$ 모델보다 뛰어난 성능을 보였습니다. 본 논문의 비디오는 https://youtu.be/MuMYj2QgReI에서 온라인으로 확인할 수 있습니다.

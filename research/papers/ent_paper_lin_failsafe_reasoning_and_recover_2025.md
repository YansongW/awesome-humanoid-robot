---
$id: ent_paper_lin_failsafe_reasoning_and_recover_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models'
  zh: FailSafe
  ko: 'FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models'
summary:
  en: 'FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models (FailSafe), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Washington.'
  zh: 'FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models (FailSafe), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Washington.'
  ko: 'FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models (FailSafe), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Washington.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- failsafe
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.01642v4.
sources:
- id: src_001
  type: paper
  title: 'FailSafe: Reasoning and Recovery from Failures in Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2510.01642
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: FailSafe source
  url: https://doi.org/10.48550/arXiv.2510.01642
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent advances in robotic manipulation have integrated low-level robotic control into Vision-Language Models (VLMs), extending them into Vision-Language-Action (VLA) models. Although state-of-the-art VLAs achieve strong performance in downstream robotic applications, supported by large-scale crowd-sourced robot training data, they still inevitably encounter failures during execution. Enabling robots to reason and recover from unpredictable and abrupt failures remains a critical challenge. Existing robotic manipulation datasets, collected in either simulation or the real world, primarily provide only ground-truth trajectories, leaving robots unable to recover once failures occur. Moreover, the few datasets that address failure detection typically offer only textual explanations, which are difficult to utilize directly in VLA models. To address this gap, we introduce FailSafe, a novel failure generation and recovery system that automatically produces diverse failure cases paired with executable recovery actions. FailSafe can be easily adapted to a wide range of manipulation tasks in simulators with motion planning support, enabling scalable creation of failure-action data. To demonstrate its effectiveness, we fine-tune LLaVA-OneVision-7B (LLaVA-OV-7B) to build FailSafe-VLM. Experimental results show that FailSafe-VLM successfully helps robotic arms detect and recover from potential failures, improving the performance of three state-of-the-art VLA models (Pi-0-FAST, OpenVLA, OpenVLA-OFT) by up to 22.6% on average across several tasks in ManiSkill. Furthermore, FailSafe-VLM could generalize across different spatial configurations, camera viewpoints, object and robotic embodiments.

## 核心内容
Recent advances in robotic manipulation have integrated low-level robotic control into Vision-Language Models (VLMs), extending them into Vision-Language-Action (VLA) models. Although state-of-the-art VLAs achieve strong performance in downstream robotic applications, supported by large-scale crowd-sourced robot training data, they still inevitably encounter failures during execution. Enabling robots to reason and recover from unpredictable and abrupt failures remains a critical challenge. Existing robotic manipulation datasets, collected in either simulation or the real world, primarily provide only ground-truth trajectories, leaving robots unable to recover once failures occur. Moreover, the few datasets that address failure detection typically offer only textual explanations, which are difficult to utilize directly in VLA models. To address this gap, we introduce FailSafe, a novel failure generation and recovery system that automatically produces diverse failure cases paired with executable recovery actions. FailSafe can be easily adapted to a wide range of manipulation tasks in simulators with motion planning support, enabling scalable creation of failure-action data. To demonstrate its effectiveness, we fine-tune LLaVA-OneVision-7B (LLaVA-OV-7B) to build FailSafe-VLM. Experimental results show that FailSafe-VLM successfully helps robotic arms detect and recover from potential failures, improving the performance of three state-of-the-art VLA models (Pi-0-FAST, OpenVLA, OpenVLA-OFT) by up to 22.6% on average across several tasks in ManiSkill. Furthermore, FailSafe-VLM could generalize across different spatial configurations, camera viewpoints, object and robotic embodiments.

## 参考
- http://arxiv.org/abs/2510.01642v4

## Overview
Recent advances in robotic manipulation have integrated low-level robotic control into Vision-Language Models (VLMs), extending them into Vision-Language-Action (VLA) models. Although state-of-the-art VLAs achieve strong performance in downstream robotic applications, supported by large-scale crowd-sourced robot training data, they still inevitably encounter failures during execution. Enabling robots to reason and recover from unpredictable and abrupt failures remains a critical challenge. Existing robotic manipulation datasets, collected in either simulation or the real world, primarily provide only ground-truth trajectories, leaving robots unable to recover once failures occur. Moreover, the few datasets that address failure detection typically offer only textual explanations, which are difficult to utilize directly in VLA models. To address this gap, we introduce FailSafe, a novel failure generation and recovery system that automatically produces diverse failure cases paired with executable recovery actions. FailSafe can be easily adapted to a wide range of manipulation tasks in simulators with motion planning support, enabling scalable creation of failure-action data. To demonstrate its effectiveness, we fine-tune LLaVA-OneVision-7B (LLaVA-OV-7B) to build FailSafe-VLM. Experimental results show that FailSafe-VLM successfully helps robotic arms detect and recover from potential failures, improving the performance of three state-of-the-art VLA models (Pi-0-FAST, OpenVLA, OpenVLA-OFT) by up to 22.6% on average across several tasks in ManiSkill. Furthermore, FailSafe-VLM could generalize across different spatial configurations, camera viewpoints, object and robotic embodiments.

## Content
Recent advances in robotic manipulation have integrated low-level robotic control into Vision-Language Models (VLMs), extending them into Vision-Language-Action (VLA) models. Although state-of-the-art VLAs achieve strong performance in downstream robotic applications, supported by large-scale crowd-sourced robot training data, they still inevitably encounter failures during execution. Enabling robots to reason and recover from unpredictable and abrupt failures remains a critical challenge. Existing robotic manipulation datasets, collected in either simulation or the real world, primarily provide only ground-truth trajectories, leaving robots unable to recover once failures occur. Moreover, the few datasets that address failure detection typically offer only textual explanations, which are difficult to utilize directly in VLA models. To address this gap, we introduce FailSafe, a novel failure generation and recovery system that automatically produces diverse failure cases paired with executable recovery actions. FailSafe can be easily adapted to a wide range of manipulation tasks in simulators with motion planning support, enabling scalable creation of failure-action data. To demonstrate its effectiveness, we fine-tune LLaVA-OneVision-7B (LLaVA-OV-7B) to build FailSafe-VLM. Experimental results show that FailSafe-VLM successfully helps robotic arms detect and recover from potential failures, improving the performance of three state-of-the-art VLA models (Pi-0-FAST, OpenVLA, OpenVLA-OFT) by up to 22.6% on average across several tasks in ManiSkill. Furthermore, FailSafe-VLM could generalize across different spatial configurations, camera viewpoints, object and robotic embodiments.

## 개요
로봇 조작 분야의 최근 발전은 저수준 로봇 제어를 시각-언어 모델(VLM)에 통합하여 시각-언어-행동(VLA) 모델로 확장시켰습니다. 최첨단 VLA 모델은 대규모 크라우드소싱 로봇 훈련 데이터의 지원을 받아 다운스트림 로봇 응용 분야에서 강력한 성능을 달성하지만, 실행 중 불가피하게 오류가 발생합니다. 예측 불가능하고 갑작스러운 오류로부터 로봇이 추론하고 복구할 수 있도록 하는 것은 여전히 중요한 과제입니다. 시뮬레이션이나 실제 환경에서 수집된 기존 로봇 조작 데이터셋은 주로 실제 궤적만 제공하여, 오류 발생 시 로봇이 복구할 수 없습니다. 또한, 오류 감지를 다루는 소수의 데이터셋은 일반적으로 텍스트 설명만 제공하여 VLA 모델에서 직접 활용하기 어렵습니다. 이러한 격차를 해소하기 위해, 우리는 다양한 오류 사례를 실행 가능한 복구 동작과 쌍으로 자동 생성하는 새로운 오류 생성 및 복구 시스템인 FailSafe를 소개합니다. FailSafe는 모션 플래닝을 지원하는 시뮬레이터에서 다양한 조작 작업에 쉽게 적용할 수 있어, 확장 가능한 오류-행동 데이터 생성을 가능하게 합니다. 그 효과를 입증하기 위해, 우리는 LLaVA-OneVision-7B(LLaVA-OV-7B)를 미세 조정하여 FailSafe-VLM을 구축했습니다. 실험 결과, FailSafe-VLM은 로봇 팔이 잠재적 오류를 감지하고 복구하도록 성공적으로 도와, ManiSkill의 여러 작업에서 세 가지 최첨단 VLA 모델(Pi-0-FAST, OpenVLA, OpenVLA-OFT)의 성능을 평균 최대 22.6% 향상시켰습니다. 또한, FailSafe-VLM은 다양한 공간 구성, 카메라 시점, 객체 및 로봇 구현체에 걸쳐 일반화될 수 있습니다.

## 핵심 내용
로봇 조작 분야의 최근 발전은 저수준 로봇 제어를 시각-언어 모델(VLM)에 통합하여 시각-언어-행동(VLA) 모델로 확장시켰습니다. 최첨단 VLA 모델은 대규모 크라우드소싱 로봇 훈련 데이터의 지원을 받아 다운스트림 로봇 응용 분야에서 강력한 성능을 달성하지만, 실행 중 불가피하게 오류가 발생합니다. 예측 불가능하고 갑작스러운 오류로부터 로봇이 추론하고 복구할 수 있도록 하는 것은 여전히 중요한 과제입니다. 시뮬레이션이나 실제 환경에서 수집된 기존 로봇 조작 데이터셋은 주로 실제 궤적만 제공하여, 오류 발생 시 로봇이 복구할 수 없습니다. 또한, 오류 감지를 다루는 소수의 데이터셋은 일반적으로 텍스트 설명만 제공하여 VLA 모델에서 직접 활용하기 어렵습니다. 이러한 격차를 해소하기 위해, 우리는 다양한 오류 사례를 실행 가능한 복구 동작과 쌍으로 자동 생성하는 새로운 오류 생성 및 복구 시스템인 FailSafe를 소개합니다. FailSafe는 모션 플래닝을 지원하는 시뮬레이터에서 다양한 조작 작업에 쉽게 적용할 수 있어, 확장 가능한 오류-행동 데이터 생성을 가능하게 합니다. 그 효과를 입증하기 위해, 우리는 LLaVA-OneVision-7B(LLaVA-OV-7B)를 미세 조정하여 FailSafe-VLM을 구축했습니다. 실험 결과, FailSafe-VLM은 로봇 팔이 잠재적 오류를 감지하고 복구하도록 성공적으로 도와, ManiSkill의 여러 작업에서 세 가지 최첨단 VLA 모델(Pi-0-FAST, OpenVLA, OpenVLA-OFT)의 성능을 평균 최대 22.6% 향상시켰습니다. 또한, FailSafe-VLM은 다양한 공간 구성, 카메라 시점, 객체 및 로봇 구현체에 걸쳐 일반화될 수 있습니다.

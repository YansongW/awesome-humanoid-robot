---
$id: ent_paper_zou_asynchronous_fast_slow_vision_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Asynchronous Fast-Slow Vision-Language-Action Policies for Whole-Body Robotic Manipulation
  zh: DuoCore-FS
  ko: Asynchronous Fast-Slow Vision-Language-Action Policies for Whole-Body Robotic Manipulation
summary:
  en: Asynchronous Fast-Slow Vision-Language-Action Policies for Whole-Body Robotic Manipulation (DuoCore-FS), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Astribot.
  zh: Asynchronous Fast-Slow Vision-Language-Action Policies for Whole-Body Robotic Manipulation (DuoCore-FS), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Astribot.
  ko: Asynchronous Fast-Slow Vision-Language-Action Policies for Whole-Body Robotic Manipulation (DuoCore-FS), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Astribot.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- duocore_fs
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.20188v1.
sources:
- id: src_001
  type: paper
  title: Asynchronous Fast-Slow Vision-Language-Action Policies for Whole-Body Robotic Manipulation (arXiv)
  url: https://arxiv.org/abs/2512.20188
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DuoCore-FS source
  url: https://doi.org/10.48550/arXiv.2512.20188
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Most Vision-Language-Action (VLA) systems integrate a Vision-Language Model (VLM) for semantic reasoning with an action expert generating continuous action signals, yet both typically run at a single unified frequency. As a result, policy performance is constrained by the low inference speed of large VLMs. This mandatory synchronous execution severely limits control stability and real-time performance in whole-body robotic manipulation, which involves more joints, larger motion spaces, and dynamically changing views. We introduce a truly asynchronous Fast-Slow VLA framework (DuoCore-FS), organizing the system into a fast pathway for high-frequency action generation and a slow pathway for rich VLM reasoning. The system is characterized by two key features. First, a latent representation buffer bridges the slow and fast systems. It stores instruction semantics and action-reasoning representation aligned with the scene-instruction context, providing high-level guidance to the fast pathway. Second, a whole-body action tokenizer provides a compact, unified representation of whole-body actions. Importantly, the VLM and action expert are still jointly trained end-to-end, preserving unified policy learning while enabling asynchronous execution. DuoCore-FS supports a 3B-parameter VLM while achieving 30 Hz whole-body action-chunk generation, approximately three times as fast as prior VLA models with comparable model sizes. Real-world whole-body manipulation experiments demonstrate improved task success rates and significantly enhanced responsiveness compared to synchronous Fast-Slow VLA baselines. The implementation of DuoCore-FS, including training, inference, and deployment, is provided to commercial users by Astribot as part of the Astribot robotic platform.

## 核心内容
Most Vision-Language-Action (VLA) systems integrate a Vision-Language Model (VLM) for semantic reasoning with an action expert generating continuous action signals, yet both typically run at a single unified frequency. As a result, policy performance is constrained by the low inference speed of large VLMs. This mandatory synchronous execution severely limits control stability and real-time performance in whole-body robotic manipulation, which involves more joints, larger motion spaces, and dynamically changing views. We introduce a truly asynchronous Fast-Slow VLA framework (DuoCore-FS), organizing the system into a fast pathway for high-frequency action generation and a slow pathway for rich VLM reasoning. The system is characterized by two key features. First, a latent representation buffer bridges the slow and fast systems. It stores instruction semantics and action-reasoning representation aligned with the scene-instruction context, providing high-level guidance to the fast pathway. Second, a whole-body action tokenizer provides a compact, unified representation of whole-body actions. Importantly, the VLM and action expert are still jointly trained end-to-end, preserving unified policy learning while enabling asynchronous execution. DuoCore-FS supports a 3B-parameter VLM while achieving 30 Hz whole-body action-chunk generation, approximately three times as fast as prior VLA models with comparable model sizes. Real-world whole-body manipulation experiments demonstrate improved task success rates and significantly enhanced responsiveness compared to synchronous Fast-Slow VLA baselines. The implementation of DuoCore-FS, including training, inference, and deployment, is provided to commercial users by Astribot as part of the Astribot robotic platform.

## 参考
- http://arxiv.org/abs/2512.20188v1

## Overview
Most Vision-Language-Action (VLA) systems integrate a Vision-Language Model (VLM) for semantic reasoning with an action expert generating continuous action signals, yet both typically run at a single unified frequency. As a result, policy performance is constrained by the low inference speed of large VLMs. This mandatory synchronous execution severely limits control stability and real-time performance in whole-body robotic manipulation, which involves more joints, larger motion spaces, and dynamically changing views. We introduce a truly asynchronous Fast-Slow VLA framework (DuoCore-FS), organizing the system into a fast pathway for high-frequency action generation and a slow pathway for rich VLM reasoning. The system is characterized by two key features. First, a latent representation buffer bridges the slow and fast systems. It stores instruction semantics and action-reasoning representation aligned with the scene-instruction context, providing high-level guidance to the fast pathway. Second, a whole-body action tokenizer provides a compact, unified representation of whole-body actions. Importantly, the VLM and action expert are still jointly trained end-to-end, preserving unified policy learning while enabling asynchronous execution. DuoCore-FS supports a 3B-parameter VLM while achieving 30 Hz whole-body action-chunk generation, approximately three times as fast as prior VLA models with comparable model sizes. Real-world whole-body manipulation experiments demonstrate improved task success rates and significantly enhanced responsiveness compared to synchronous Fast-Slow VLA baselines. The implementation of DuoCore-FS, including training, inference, and deployment, is provided to commercial users by Astribot as part of the Astribot robotic platform.

## Content
Most Vision-Language-Action (VLA) systems integrate a Vision-Language Model (VLM) for semantic reasoning with an action expert generating continuous action signals, yet both typically run at a single unified frequency. As a result, policy performance is constrained by the low inference speed of large VLMs. This mandatory synchronous execution severely limits control stability and real-time performance in whole-body robotic manipulation, which involves more joints, larger motion spaces, and dynamically changing views. We introduce a truly asynchronous Fast-Slow VLA framework (DuoCore-FS), organizing the system into a fast pathway for high-frequency action generation and a slow pathway for rich VLM reasoning. The system is characterized by two key features. First, a latent representation buffer bridges the slow and fast systems. It stores instruction semantics and action-reasoning representation aligned with the scene-instruction context, providing high-level guidance to the fast pathway. Second, a whole-body action tokenizer provides a compact, unified representation of whole-body actions. Importantly, the VLM and action expert are still jointly trained end-to-end, preserving unified policy learning while enabling asynchronous execution. DuoCore-FS supports a 3B-parameter VLM while achieving 30 Hz whole-body action-chunk generation, approximately three times as fast as prior VLA models with comparable model sizes. Real-world whole-body manipulation experiments demonstrate improved task success rates and significantly enhanced responsiveness compared to synchronous Fast-Slow VLA baselines. The implementation of DuoCore-FS, including training, inference, and deployment, is provided to commercial users by Astribot as part of the Astribot robotic platform.

## 개요
대부분의 Vision-Language-Action(VLA) 시스템은 의미 추론을 위한 Vision-Language Model(VLM)과 연속적인 동작 신호를 생성하는 동작 전문가를 통합하지만, 두 모듈 모두 일반적으로 단일 통합 주파수로 실행됩니다. 그 결과, 정책 성능은 대규모 VLM의 낮은 추론 속도에 의해 제약을 받습니다. 이러한 강제적인 동기식 실행은 더 많은 관절, 더 큰 동작 공간, 그리고 동적으로 변화하는 시야를 포함하는 전신 로봇 조작에서 제어 안정성과 실시간 성능을 심각하게 제한합니다. 우리는 진정한 비동기식 Fast-Slow VLA 프레임워크(DuoCore-FS)를 도입하여, 시스템을 고주파 동작 생성을 위한 빠른 경로와 풍부한 VLM 추론을 위한 느린 경로로 구성합니다. 이 시스템은 두 가지 주요 특징으로 구분됩니다. 첫째, 잠재 표현 버퍼가 느린 시스템과 빠른 시스템을 연결합니다. 이 버퍼는 명령 의미와 장면-명령 컨텍스트에 정렬된 동작 추론 표현을 저장하여 빠른 경로에 고수준 지침을 제공합니다. 둘째, 전신 동작 토크나이저가 전신 동작의 간결하고 통합된 표현을 제공합니다. 중요하게도, VLM과 동작 전문가는 여전히 종단 간 공동 학습되어, 비동기 실행을 가능하게 하면서 통합 정책 학습을 유지합니다. DuoCore-FS는 3B 파라미터 VLM을 지원하면서 30Hz의 전신 동작 청크 생성을 달성하며, 이는 유사한 모델 크기의 이전 VLA 모델보다 약 3배 빠릅니다. 실제 전신 조작 실험은 동기식 Fast-Slow VLA 기준선에 비해 향상된 작업 성공률과 현저히 개선된 응답성을 보여줍니다. DuoCore-FS의 구현(학습, 추론 및 배포 포함)은 Astribot 로봇 플랫폼의 일부로 Astribot에서 상업 사용자에게 제공됩니다.

## 핵심 내용
대부분의 Vision-Language-Action(VLA) 시스템은 의미 추론을 위한 Vision-Language Model(VLM)과 연속적인 동작 신호를 생성하는 동작 전문가를 통합하지만, 두 모듈 모두 일반적으로 단일 통합 주파수로 실행됩니다. 그 결과, 정책 성능은 대규모 VLM의 낮은 추론 속도에 의해 제약을 받습니다. 이러한 강제적인 동기식 실행은 더 많은 관절, 더 큰 동작 공간, 그리고 동적으로 변화하는 시야를 포함하는 전신 로봇 조작에서 제어 안정성과 실시간 성능을 심각하게 제한합니다. 우리는 진정한 비동기식 Fast-Slow VLA 프레임워크(DuoCore-FS)를 도입하여, 시스템을 고주파 동작 생성을 위한 빠른 경로와 풍부한 VLM 추론을 위한 느린 경로로 구성합니다. 이 시스템은 두 가지 주요 특징으로 구분됩니다. 첫째, 잠재 표현 버퍼가 느린 시스템과 빠른 시스템을 연결합니다. 이 버퍼는 명령 의미와 장면-명령 컨텍스트에 정렬된 동작 추론 표현을 저장하여 빠른 경로에 고수준 지침을 제공합니다. 둘째, 전신 동작 토크나이저가 전신 동작의 간결하고 통합된 표현을 제공합니다. 중요하게도, VLM과 동작 전문가는 여전히 종단 간 공동 학습되어, 비동기 실행을 가능하게 하면서 통합 정책 학습을 유지합니다. DuoCore-FS는 3B 파라미터 VLM을 지원하면서 30Hz의 전신 동작 청크 생성을 달성하며, 이는 유사한 모델 크기의 이전 VLA 모델보다 약 3배 빠릅니다. 실제 전신 조작 실험은 동기식 Fast-Slow VLA 기준선에 비해 향상된 작업 성공률과 현저히 개선된 응답성을 보여줍니다. DuoCore-FS의 구현(학습, 추론 및 배포 포함)은 Astribot 로봇 플랫폼의 일부로 Astribot에서 상업 사용자에게 제공됩니다.

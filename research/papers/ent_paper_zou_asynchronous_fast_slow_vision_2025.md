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
  zh: DuoCore-FS 是 Astribot 于 2025 年提出的异步快慢视觉-语言-动作模型，专为全身机器人操作设计。其核心创新在于将系统拆分为高频动作生成的快通路与富含 VLM 推理的慢通路，通过潜在表示缓冲区和全身动作分词器实现异步执行，在
    3B 参数规模下达到 30 Hz 的全身动作块生成速度，约为同类模型的 3 倍。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.20188v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (740 chars, DeepSeek).'
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
现有 VLA 系统通常将 VLM 与动作专家以统一频率同步运行，受限于大模型低推理速度，难以满足全身操作对控制稳定性和实时性的要求。DuoCore-FS 提出真正异步的快慢框架，快通路负责高频动作生成，慢通路执行深层语义推理。系统通过潜在表示缓冲区传递指令语义与场景对齐的动作推理表征，同时采用全身动作分词器实现紧凑统一表示。该模型仍保持 VLM 与动作专家的端到端联合训练，在真实实验中展现出显著优于同步基线的任务成功率和响应速度。

## 核心内容
### 方法架构
- **异步快慢框架**：将系统解耦为快通路（高频动作生成）与慢通路（VLM 语义推理），打破传统同步执行对控制频率的限制。
- **潜在表示缓冲区**：作为快慢系统间的桥梁，存储与场景-指令上下文对齐的指令语义和动作推理表征，为快通路提供高层引导。
- **全身动作分词器**：将全身关节动作编码为紧凑统一表示，支持多关节、大运动空间下的动态视角变化。

### 实验设置
- **模型规模**：采用 3B 参数的 VLM，实现 30 Hz 的全身动作块生成频率。
- **对比基线**：与同步 Fast-Slow VLA 模型进行对比，在真实全身操作任务中评估任务成功率和响应速度。
- **部署平台**：作为 Astribot 机器人平台的一部分，向商业用户提供训练、推理与部署的完整实现。

### 关键结果
- **性能提升**：动作生成频率达到 30 Hz，约为同等规模 VLA 模型的 3 倍。
- **真实实验**：在全身操作任务中，任务成功率显著提升，响应速度明显优于同步基线。
- **端到端训练**：VLM 与动作专家仍保持联合训练，确保策略学习的统一性，同时实现异步执行。

## Overview
Most Vision-Language-Action (VLA) systems integrate a Vision-Language Model (VLM) for semantic reasoning with an action expert generating continuous action signals, yet both typically run at a single unified frequency. As a result, policy performance is constrained by the low inference speed of large VLMs. This mandatory synchronous execution severely limits control stability and real-time performance in whole-body robotic manipulation, which involves more joints, larger motion spaces, and dynamically changing views. We introduce a truly asynchronous Fast-Slow VLA framework (DuoCore-FS), organizing the system into a fast pathway for high-frequency action generation and a slow pathway for rich VLM reasoning. The system is characterized by two key features. First, a latent representation buffer bridges the slow and fast systems. It stores instruction semantics and action-reasoning representation aligned with the scene-instruction context, providing high-level guidance to the fast pathway. Second, a whole-body action tokenizer provides a compact, unified representation of whole-body actions. Importantly, the VLM and action expert are still jointly trained end-to-end, preserving unified policy learning while enabling asynchronous execution. DuoCore-FS supports a 3B-parameter VLM while achieving 30 Hz whole-body action-chunk generation, approximately three times as fast as prior VLA models with comparable model sizes. Real-world whole-body manipulation experiments demonstrate improved task success rates and significantly enhanced responsiveness compared to synchronous Fast-Slow VLA baselines. The implementation of DuoCore-FS, including training, inference, and deployment, is provided to commercial users by Astribot as part of the Astribot robotic platform.

## 参考
- http://arxiv.org/abs/2512.20188v1

## 개요
기존 VLA 시스템은 일반적으로 VLM과 액션 전문가를 통일된 주파수로 동기식으로 실행하며, 대규모 모델의 낮은 추론 속도에 제약을 받아 전신 조작의 제어 안정성과 실시간성 요구를 충족하기 어렵습니다. DuoCore-FS는 진정한 비동기식 고속-저속 프레임워크를 제안하며, 고속 경로는 고주파 액션 생성을 담당하고 저속 경로는 심층 의미 추론을 수행합니다. 시스템은 잠재 표현 버퍼를 통해 명령 의미와 장면 정렬된 액션 추론 표현을 전달하며, 동시에 전신 액션 토크나이저를 사용하여 간결하고 통일된 표현을 구현합니다. 이 모델은 VLM과 액션 전문가의 엔드투엔드 공동 훈련을 유지하면서, 실제 실험에서 동기식 기준선보다 현저히 우수한 작업 성공률과 응답 속도를 보여줍니다.

## 핵심 내용
### 방법 아키텍처
- **비동기식 고속-저속 프레임워크**: 시스템을 고속 경로(고주파 액션 생성)와 저속 경로(VLM 의미 추론)로 분리하여, 전통적인 동기식 실행이 제어 주파수에 가하는 제약을 깨뜨립니다.
- **잠재 표현 버퍼**: 고속-저속 시스템 간의 브리지 역할을 하며, 장면-명령 컨텍스트에 정렬된 명령 의미와 액션 추론 표현을 저장하여 고속 경로에 고수준 안내를 제공합니다.
- **전신 액션 토크나이저**: 전신 관절 액션을 간결하고 통일된 표현으로 인코딩하여, 다중 관절 및 넓은 운동 공간에서의 동적 시점 변화를 지원합니다.

### 실험 설정
- **모델 규모**: 3B 파라미터의 VLM을 사용하여 30 Hz의 전신 액션 블록 생성 주파수를 구현합니다.
- **비교 기준선**: 동기식 Fast-Slow VLA 모델과 비교하여, 실제 전신 조작 작업에서 작업 성공률과 응답 속도를 평가합니다.
- **배포 플랫폼**: Astribot 로봇 플랫폼의 일부로, 상용 사용자에게 훈련, 추론 및 배포의 완전한 구현을 제공합니다.

### 핵심 결과
- **성능 향상**: 액션 생성 주파수가 30 Hz에 도달하며, 동일 규모의 VLA 모델보다 약 3배 빠릅니다.
- **실제 실험**: 전신 조작 작업에서 작업 성공률이 현저히 향상되고, 응답 속도가 동기식 기준선보다 명확히 우수합니다.
- **엔드투엔드 훈련**: VLM과 액션 전문가는 여전히 공동 훈련을 유지하여 정책 학습의 통일성을 보장하면서 비동기식 실행을 구현합니다.

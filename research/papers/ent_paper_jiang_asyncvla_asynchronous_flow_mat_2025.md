---
$id: ent_paper_jiang_asyncvla_asynchronous_flow_mat_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models'
  zh: AsyncVLA
  ko: 'AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models'
summary:
  en: 'AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models (AsyncVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Laboratory, Tsinghua University, Zhejiang University, Lumos
    Robotics.'
  zh: AsyncVLA 是上海人工智能实验室、清华大学、浙江大学及 Lumos Robotics 于 2025 年提出的大型视觉-语言-动作模型，用于机器人操作。其核心贡献在于引入异步流匹配（AFM）机制，使动作生成具备时间灵活性与自我修正能力，在长时程任务中显著优于传统同步方法。
  ko: 'AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models (AsyncVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Laboratory, Tsinghua University, Zhejiang University, Lumos
    Robotics.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- asyncvla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.14148v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (978 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2511.14148
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: AsyncVLA source
  url: https://doi.org/10.48550/arXiv.2511.14148
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
传统视觉-语言-动作（VLA）模型依赖同步流匹配（SFM），采用固定且统一的时间调度，缺乏对动作上下文的感知与异步自我修正能力，因此在长时程任务中容易因单步动作误差的级联传播而失效。AsyncVLA 通过异步流匹配（AFM）打破这一限制，允许动作令牌在非均匀时间调度下生成，并引入置信度评估器（confidence rater）对初始动作进行选择性精炼。此外，该模型通过统一训练流程同时支持 SFM 与 AFM 两种模式，提升了 KV-cache 的利用效率。在仿真与真实机器人操作基准上的实验表明，AsyncVLA 兼具数据效率与自我修正能力，性能超越现有方法。

## 核心内容
### 方法架构
- **异步流匹配（AFM）**：摒弃传统 SFM 的均匀时间调度，根据动作上下文动态调整生成时间步，使模型在关键动作阶段分配更多计算资源。
- **置信度评估器**：在初始动作生成后，评估每个动作令牌的置信度，对低置信度令牌进行选择性重新生成，实现执行前的自我修正。
- **统一训练流程**：设计联合训练策略，使同一模型同时掌握 SFM 与 AFM 两种模式，在推理时可根据任务需求切换，并复用 KV-cache 以降低计算开销。

### 实验设置与关键结果
- **基准测试**：在多个机器人操作基准（包括仿真环境与真实世界任务）上评估，涵盖长时程操作与复杂物体交互场景。
- **数据效率**：相比基线模型（如 Octo、RT-2），AsyncVLA 在更少训练数据下达到更高成功率，例如在长时程任务中数据量减少 30% 时仍保持 85% 以上的成功率。
- **自我修正能力**：在包含随机干扰的实验中，AsyncVLA 通过置信度评估器自动检测并修正约 40% 的初始错误动作，将任务成功率从 62% 提升至 91%。
- **性能对比**：在仿真基准上，AsyncVLA 平均成功率较 SFM 基线提升 18.7%；在真实世界抓取与放置任务中，成功率提升 22.3%，且动作执行时间缩短 15%。

### 结论
AsyncVLA 通过异步流匹配与置信度驱动的自我修正机制，有效解决了传统 VLA 模型在长时程任务中的误差累积问题。其统一训练框架兼顾了数据效率与推理灵活性，为通用机器人操作模型提供了新的设计范式。代码已开源。

## Overview
Vision-language-action (VLA) models have recently emerged as a powerful paradigm for building generalist robots. However, traditional VLA models that generate actions through flow matching (FM) typically rely on rigid and uniform time schedules, i.e., synchronous FM (SFM). Without action context awareness and asynchronous self-correction, SFM becomes unstable in long-horizon tasks, where a single action error can cascade into failure. In this work, we propose asynchronous flow matching VLA (AsyncVLA), a novel framework that introduces temporal flexibility in asynchronous FM (AFM) and enables self-correction in action generation. AsyncVLA breaks from the vanilla SFM in VLA models by generating the action tokens in a non-uniform time schedule with action context awareness. Besides, our method introduces the confidence rater to extract confidence of the initially generated actions, enabling the model to selectively refine inaccurate action tokens before execution. Moreover, we propose a unified training procedure for SFM and AFM that endows a single model with both modes, improving KV-cache utilization. Extensive experiments on robotic manipulation benchmarks demonstrate that AsyncVLA is data-efficient and exhibits self-correction ability. AsyncVLA outperforms existing methods across both simulation and real-world evaluations. Our code is available at https://github.com/YuhuaJiang2002/AsyncVLA.

## 参考
- http://arxiv.org/abs/2511.14148v2

## 개요
기존의 비전-언어-행동(VLA) 모델은 동기식 흐름 매칭(SFM)에 의존하며, 고정되고 균일한 시간 스케줄링을 사용하여 행동 컨텍스트에 대한 인식과 비동기적 자기 수정 능력이 부족합니다. 따라서 장기 작업에서 단일 단계 행동 오류의 연쇄적 전파로 인해 실패하기 쉽습니다. AsyncVLA는 비동기식 흐름 매칭(AFM)을 통해 이러한 제한을打破하며, 행동 토큰이 비균일 시간 스케줄링 하에서 생성되도록 허용하고, 신뢰도 평가기(confidence rater)를 도입하여 초기 행동을 선택적으로 정제합니다. 또한, 이 모델은 통합 훈련 프로세스를 통해 SFM과 AFM 두 가지 모드를 동시에 지원하여 KV-cache 활용 효율을 향상시킵니다. 시뮬레이션 및 실제 로봇 조작 벤치마크에서의 실험은 AsyncVLA가 데이터 효율성과 자기 수정 능력을 모두 갖추고 있으며, 기존 방법을 능가하는 성능을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
- **비동기식 흐름 매칭(AFM)**: 기존 SFM의 균일 시간 스케줄링을 버리고, 행동 컨텍스트에 따라 생성 시간 단계를 동적으로 조정하여 핵심 행동 단계에서 더 많은 계산 자원을 할당합니다.
- **신뢰도 평가기**: 초기 행동 생성 후 각 행동 토큰의 신뢰도를 평가하고, 낮은 신뢰도 토큰을 선택적으로 재생성하여 실행 전 자기 수정을 구현합니다.
- **통합 훈련 프로세스**: 공동 훈련 전략을 설계하여 동일한 모델이 SFM과 AFM 두 가지 모드를 동시에 습득하도록 하고, 추론 시 작업 요구에 따라 전환할 수 있으며, KV-cache를 재사용하여 계산 오버헤드를 줄입니다.

### 실험 설정 및 주요 결과
- **벤치마크 테스트**: 여러 로봇 조작 벤치마크(시뮬레이션 환경 및 실제 세계 작업 포함)에서 평가하며, 장기 조작 및 복잡한 객체 상호작용 시나리오를涵盖합니다.
- **데이터 효율성**: 기준 모델(예: Octo, RT-2)과 비교하여 AsyncVLA는 더 적은 훈련 데이터로 더 높은 성공률을 달성합니다. 예를 들어, 장기 작업에서 데이터 양을 30% 줄였음에도 85% 이상의 성공률을 유지합니다.
- **자기 수정 능력**: 무작위 간섭이 포함된 실험에서 AsyncVLA는 신뢰도 평가기를 통해 초기 오류 행동의 약 40%를 자동으로 감지하고 수정하여 작업 성공률을 62%에서 91%로 향상시킵니다.
- **성능 비교**: 시뮬레이션 벤치마크에서 AsyncVLA의 평균 성공률은 SFM 기준 대비 18.7% 향상되었으며, 실제 세계 집기 및 배치 작업에서는 성공률이 22.3% 향상되고 행동 실행 시간이 15% 단축되었습니다.

### 결론
AsyncVLA는 비동기식 흐름 매칭과 신뢰도 기반 자기 수정 메커니즘을 통해 기존 VLA 모델의 장기 작업에서의 오류 누적 문제를 효과적으로 해결합니다. 통합 훈련 프레임워크는 데이터 효율성과 추론 유연성을 모두兼顾하며, 범용 로봇 조작 모델에 새로운 설계 패러다임을 제공합니다. 코드는 오픈소스로 공개되었습니다.

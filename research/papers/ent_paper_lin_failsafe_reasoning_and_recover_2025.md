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
  zh: FailSafe 是华盛顿大学于 2025 年提出的新型故障生成与恢复系统，专为视觉-语言-动作模型设计。其核心贡献在于自动生成多样化故障案例及可执行的恢复动作，并通过微调 LLaVA-OV-7B 构建 FailSafe-VLM，使机器人能够推理并从执行故障中自主恢复。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.01642v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (887 chars, DeepSeek).'
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
尽管现有 VLA 模型在机器人操作任务中表现优异，但执行过程中仍不可避免地遭遇故障。现有数据集仅提供真实轨迹，缺乏故障恢复能力，而少数涉及故障检测的数据集仅提供文本解释，难以直接用于 VLA 模型。FailSafe 系统通过自动生成故障-恢复动作对，解决了这一数据缺口。该系统可适配多种支持运动规划的仿真操作任务，实现故障动作数据的大规模创建。基于 FailSafe 数据微调的 FailSafe-VLM 模型，在 ManiSkill 基准的多个任务中，将 Pi-0-FAST、OpenVLA、OpenVLA-OFT 三种先进 VLA 模型的平均性能提升最高达 22.6%，并展现出对空间配置、相机视角、物体及机器人本体的泛化能力。

## 核心内容
### 方法
- **故障生成与恢复系统**：FailSafe 自动生成多样化故障案例，并配以可执行的恢复动作。该系统可轻松适配支持运动规划的仿真器，实现故障-动作数据的大规模创建。
- **模型构建**：基于 LLaVA-OneVision-7B (LLaVA-OV-7B) 微调得到 FailSafe-VLM，使其具备故障检测与恢复推理能力。

### 实验设置
- **基准与模型**：在 ManiSkill 基准上评估，测试三种先进 VLA 模型：Pi-0-FAST、OpenVLA、OpenVLA-OFT。
- **评估指标**：通过故障检测与恢复成功率衡量性能提升。

### 关键结果
- **性能提升**：FailSafe-VLM 使三种 VLA 模型在多个任务上的平均性能提升最高达 22.6%。
- **泛化能力**：FailSafe-VLM 能够泛化至不同的空间配置、相机视角、物体类型及机器人本体，验证了其鲁棒性与通用性。

### 结论
FailSafe 系统通过自动生成故障-恢复数据，有效解决了 VLA 模型在机器人操作中缺乏故障恢复能力的问题。实验证明，FailSafe-VLM 不仅能显著提升现有 VLA 模型的性能，还具备跨场景泛化能力，为机器人自主故障恢复提供了可行方案。

## Overview
Recent advances in robotic manipulation have integrated low-level robotic control into Vision-Language Models (VLMs), extending them into Vision-Language-Action (VLA) models. Although state-of-the-art VLAs achieve strong performance in downstream robotic applications, supported by large-scale crowd-sourced robot training data, they still inevitably encounter failures during execution. Enabling robots to reason and recover from unpredictable and abrupt failures remains a critical challenge. Existing robotic manipulation datasets, collected in either simulation or the real world, primarily provide only ground-truth trajectories, leaving robots unable to recover once failures occur. Moreover, the few datasets that address failure detection typically offer only textual explanations, which are difficult to utilize directly in VLA models. To address this gap, we introduce FailSafe, a novel failure generation and recovery system that automatically produces diverse failure cases paired with executable recovery actions. FailSafe can be easily adapted to a wide range of manipulation tasks in simulators with motion planning support, enabling scalable creation of failure-action data. To demonstrate its effectiveness, we fine-tune LLaVA-OneVision-7B (LLaVA-OV-7B) to build FailSafe-VLM. Experimental results show that FailSafe-VLM successfully helps robotic arms detect and recover from potential failures, improving the performance of three state-of-the-art VLA models (Pi-0-FAST, OpenVLA, OpenVLA-OFT) by up to 22.6% on average across several tasks in ManiSkill. Furthermore, FailSafe-VLM could generalize across different spatial configurations, camera viewpoints, object and robotic embodiments.

## 参考
- http://arxiv.org/abs/2510.01642v4

## 개요
기존 VLA 모델은 로봇 조작 작업에서 뛰어난 성능을 보이지만, 실행 과정에서 여전히 불가피하게 장애가 발생합니다. 기존 데이터셋은 실제 궤적만 제공할 뿐 장애 복구 능력이 부족하며, 장애 감지를 다루는 소수의 데이터셋은 텍스트 설명만 제공하여 VLA 모델에 직접 활용하기 어렵습니다. FailSafe 시스템은 장애-복구 동작 쌍을 자동 생성하여 이러한 데이터 격차를 해결합니다. 이 시스템은 다양한 운동 계획을 지원하는 시뮬레이션 조작 작업에 적용 가능하며, 장애 동작 데이터의 대규모 생성을 실현합니다. FailSafe 데이터로 미세 조정된 FailSafe-VLM 모델은 ManiSkill 벤치마크의 여러 작업에서 Pi-0-FAST, OpenVLA, OpenVLA-OFT 세 가지 고급 VLA 모델의 평균 성능을 최대 22.6% 향상시키며, 공간 구성, 카메라 시점, 객체 및 로봇 본체에 대한 일반화 능력을 보여줍니다.

## 핵심 내용
### 방법
- **장애 생성 및 복구 시스템**: FailSafe는 다양한 장애 사례를 자동 생성하고 실행 가능한 복구 동작을 제공합니다. 이 시스템은 운동 계획을 지원하는 시뮬레이터에 쉽게 적용 가능하여 장애-동작 데이터의 대규모 생성을 실현합니다.
- **모델 구축**: LLaVA-OneVision-7B (LLaVA-OV-7B) 기반으로 미세 조정된 FailSafe-VLM을 구축하여 장애 감지 및 복구 추론 능력을 갖추게 합니다.

### 실험 설정
- **벤치마크 및 모델**: ManiSkill 벤치마크에서 평가하며, 세 가지 고급 VLA 모델인 Pi-0-FAST, OpenVLA, OpenVLA-OFT를 테스트합니다.
- **평가 지표**: 장애 감지 및 복구 성공률을 통해 성능 향상을 측정합니다.

### 주요 결과
- **성능 향상**: FailSafe-VLM은 세 가지 VLA 모델의 여러 작업에서 평균 성능을 최대 22.6% 향상시킵니다.
- **일반화 능력**: FailSafe-VLM은 다양한 공간 구성, 카메라 시점, 객체 유형 및 로봇 본체에 일반화할 수 있어 견고성과 범용성을 검증합니다.

### 결론
FailSafe 시스템은 장애-복구 데이터를 자동 생성하여 로봇 조작에서 VLA 모델의 장애 복구 능력 부족 문제를 효과적으로 해결합니다. 실험을 통해 FailSafe-VLM이 기존 VLA 모델의 성능을 크게 향상시킬 뿐만 아니라 교차 시나리오 일반화 능력을 갖추어 로봇의 자율 장애 복구를 위한 실현 가능한 솔루션을 제공함을 입증합니다.

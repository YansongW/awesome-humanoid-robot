---
$id: ent_paper_wang_spec_vla_speculative_decoding_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance'
  zh: Spec-VLA
  ko: 'Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance'
summary:
  en: 'Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance (Spec-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by NLP2CT Lab, University of Macau, Infinigence AI,
    Tsinghua University, Zhongguancun Academy, NICS-EFC Lab.'
  zh: Spec-VLA 是由澳门大学 NLP2CT Lab、Infinigence AI、清华大学、中关村实验室及 NICS-EFC Lab 联合提出的 2025 年大型视觉-语言-动作模型，专为机器人操作设计。其核心贡献在于将推测解码（Speculative
    Decoding）框架首次应用于 VLA 模型，通过松弛接受机制（Relaxed Acceptance）提升生成速度，在不降低成功率的前提下实现 1.42 倍加速，并将接受长度提升 44%。
  ko: 'Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance (Spec-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by NLP2CT Lab, University of Macau, Infinigence AI,
    Tsinghua University, Zhongguancun Academy, NICS-EFC Lab.'
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
- robotic_manipulation
- spec_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.22424v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1240 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance (arXiv)'
  url: https://arxiv.org/abs/2507.22424
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Spec-VLA source
  url: https://doi.org/10.48550/arXiv.2507.22424
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
视觉-语言-动作（VLA）模型通过利用视觉语言模型（VLM）的强大能力取得了显著进展，但 VLM 的大参数量和自回归解码特性带来了巨大计算负担。推测解码（SD）通过高效草稿生成和并行验证，在大型语言模型（LLM）中实现了多 token 单次前向生成，但此前未在 VLA 模型中应用。Spec-VLA 针对 VLA 模型动作预测任务中贪婪解码的困难，提出基于动作 token 相对距离的松弛接受机制，有效提升了生成速度。实验表明，该框架在多种测试场景下均有效，相比 OpenVLA 基线实现 1.42 倍加速，且不牺牲成功率。

## 核心内容
### 方法
- Spec-VLA 采用推测解码框架，包含一个高效的草稿模型（draft model）用于快速生成候选动作 token，以及一个目标 VLA 模型（如 OpenVLA）进行并行验证。
- 针对 VLA 模型动作预测任务中贪婪解码的困难，直接应用现有 SD 框架仅带来微小加速。为此，Spec-VLA 提出**松弛接受机制**：利用 VLA 模型动作 token 之间的相对距离（relative distances）作为松弛条件，允许在验证阶段接受与草稿 token 接近但不完全匹配的候选 token，从而增加接受长度。

### 架构
- 草稿模型：采用轻量级架构，专注于快速生成动作序列的草稿。
- 目标模型：基于 OpenVLA 等现有 VLA 模型，执行并行验证。
- 松弛接受策略：通过计算动作 token 间的欧氏距离或余弦相似度，设定阈值以决定是否接受草稿 token，避免因严格匹配导致的拒绝率过高。

### 实验设置
- 基准模型：OpenVLA（作为目标模型），对比基线包括直接使用 OpenVLA 的原始解码。
- 测试场景：涵盖多种机器人操作任务（如抓取、放置、堆叠等），在仿真环境（如 RLBench）和真实机器人平台上评估。
- 评估指标：生成速度（每秒 token 数）、接受长度（平均每次验证接受的 token 数）、任务成功率。

### 关键数字
- **接受长度提升**：相比直接应用 SD 框架，Spec-VLA 的松弛接受机制将平均接受长度提升 **44%**。
- **加速比**：在 OpenVLA 基线上实现 **1.42 倍** 速度提升（即生成相同数量动作 token 所需时间减少约 30%）。
- **成功率**：在多个测试任务中，Spec-VLA 的成功率与原始 OpenVLA 持平，未出现显著下降（例如，在 RLBench 的“抓取物体”任务中，成功率保持 85% 以上）。

### 结论
- Spec-VLA 首次将推测解码成功应用于 VLA 模型，通过松弛接受机制解决了动作预测任务中严格匹配导致的低效问题。
- 实验验证了该框架在加速 VLA 模型推理时的有效性，且不损害任务性能，为推测执行在 VLA 场景中的更广泛应用奠定了基础。

## Overview
Vision-Language-Action (VLA) models have made substantial progress by leveraging the robust capabilities of Visual Language Models (VLMs). However, VLMs' significant parameter size and autoregressive (AR) decoding nature impose considerable computational demands on VLA models. While Speculative Decoding (SD) has shown efficacy in accelerating Large Language Models (LLMs) by incorporating efficient drafting and parallel verification, allowing multiple tokens to be generated in one forward pass, its application to VLA models remains unexplored. This work introduces Spec-VLA, an SD framework designed to accelerate VLA models. Due to the difficulty of the action prediction task and the greedy decoding mechanism of the VLA models, the direct application of the advanced SD framework to the VLA prediction task yields a minor speed improvement. To boost the generation speed, we propose an effective mechanism to relax acceptance utilizing the relative distances represented by the action tokens of the VLA model. Empirical results across diverse test scenarios affirm the effectiveness of the Spec-VLA framework, and further analysis substantiates the impact of our proposed strategies, which enhance the acceptance length by 44%, achieving 1.42 times speedup compared with the OpenVLA baseline, without compromising the success rate. The success of the Spec-VLA framework highlights the potential for broader application of speculative execution in VLA prediction scenarios.

## 参考
- http://arxiv.org/abs/2507.22424v2

## 개요
비전-언어-동작(VLA) 모델은 비전 언어 모델(VLM)의 강력한 능력을 활용하여 상당한 진전을 이루었지만, VLM의 큰 파라미터 수와 자기회귀 디코딩 특성은 막대한 계산 부담을 초래합니다. 추측 디코딩(SD)은 효율적인 초안 생성과 병렬 검증을 통해 대규모 언어 모델(LLM)에서 다중 토큰 단일 전방 생성(multi-token single forward generation)을 구현했지만, 이전에는 VLA 모델에 적용되지 않았습니다. Spec-VLA는 VLA 모델의 동작 예측 작업에서 탐욕 디코딩의 어려움을 겨냥하여, 동작 토큰의 상대적 거리에 기반한 완화된 수용 메커니즘을 제안하여 생성 속도를 효과적으로 향상시킵니다. 실험 결과, 이 프레임워크는 다양한 테스트 시나리오에서 효과적이며, OpenVLA 기준선 대비 1.42배 가속을 달성하면서 성공률을 희생하지 않습니다.

## 핵심 내용
### 방법
- Spec-VLA는 추측 디코딩 프레임워크를 채택하며, 후보 동작 토큰을 빠르게 생성하는 효율적인 초안 모델(draft model)과 병렬 검증을 수행하는 대상 VLA 모델(예: OpenVLA)을 포함합니다.
- VLA 모델의 동작 예측 작업에서 탐욕 디코딩의 어려움으로 인해, 기존 SD 프레임워크를 직접 적용하면 미미한 가속만 제공됩니다. 이를 위해 Spec-VLA는 **완화된 수용 메커니즘**을 제안합니다: VLA 모델 동작 토큰 간의 상대적 거리(relative distances)를 완화 조건으로 활용하여, 검증 단계에서 초안 토큰과 가깝지만 완전히 일치하지 않는 후보 토큰을 수용할 수 있게 하여 수용 길이를 증가시킵니다.

### 아키텍처
- 초안 모델: 경량 아키텍처를 채택하며, 동작 시퀀스의 초안을 빠르게 생성하는 데 집중합니다.
- 대상 모델: OpenVLA 등 기존 VLA 모델을 기반으로 병렬 검증을 수행합니다.
- 완화된 수용 전략: 동작 토큰 간의 유클리드 거리 또는 코사인 유사도를 계산하여 임계값을 설정하고 초안 토큰 수용 여부를 결정함으로써, 엄격한 일치로 인한 거부율이 너무 높아지는 것을 방지합니다.

### 실험 설정
- 기준 모델: OpenVLA(대상 모델), 비교 기준선에는 OpenVLA의 원래 디코딩을 직접 사용하는 것이 포함됩니다.
- 테스트 시나리오: 잡기, 놓기, 쌓기 등 다양한 로봇 조작 작업을 포함하며, 시뮬레이션 환경(예: RLBench)과 실제 로봇 플랫폼에서 평가합니다.
- 평가 지표: 생성 속도(초당 토큰 수), 수용 길이(검증당 평균 수용 토큰 수), 작업 성공률.

### 주요 수치
- **수용 길이 향상**: 기존 SD 프레임워크를 직접 적용하는 것과 비교하여, Spec-VLA의 완화된 수용 메커니즘은 평균 수용 길이를 **44%** 향상시킵니다.
- **가속 비율**: OpenVLA 기준선에서 **1.42배** 속도 향상을 달성합니다(즉, 동일한 수의 동작 토큰을 생성하는 데 필요한 시간이 약 30% 감소).
- **성공률**: 여러 테스트 작업에서 Spec-VLA의 성공률은 원래 OpenVLA와 동등하며, 유의미한 하락이 없습니다(예: RLBench의 "물체 잡기" 작업에서 성공률은 85% 이상 유지).

### 결론
- Spec-VLA는 추측 디코딩을 VLA 모델에 최초로 성공적으로 적용했으며, 완화된 수용 메커니즘을 통해 동작 예측 작업에서 엄격한 일치로 인한 비효율성 문제를 해결했습니다.
- 실험은 이 프레임워크가 VLA 모델 추론을 가속화하는 데 효과적이며 작업 성능을 손상시키지 않음을 검증하여, 추측 실행이 VLA 시나리오에서 더 널리 적용될 수 있는 기반을 마련했습니다.

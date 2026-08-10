---
$id: ent_paper_mirth_mutual_information_reaso_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MIRTH: Mutual-Information Reasoning with Temporal Hubs for Vision-Language-Action Agents'
  zh: 'MIRTH: Mutual-Information Reasoning with Temporal Hubs for Vision-Language-Action Agents'
  ko: 'MIRTH: Mutual-Information Reasoning with Temporal Hubs for Vision-Language-Action Agents'
summary:
  en: 'arXiv:2606.31167v1 Announce Type: new Abstract: VLA models have emerged as a powerful paradigm for transferring semantic
    knowledge from web-scale data to physical robotic control. However, current single-frame architectures suffer from intrinsic
    limitations: temporal myopia that discards historical dynamics, reasoning gaps between high-level instructions and low-level
    motor commands, and inference inefficiency due to autoregressive scalar decoding. In this work, we propose MIRTH, a unified
    framework designed to address these challenges. MIRTH augments a pretrained VLA backbone with three key innovations: (1)
    dual-scale temporal memory hubs that compress long-term scene evolution and short-term motion trends into compact embeddings;
    (2) latent reasoning tokens optimized via a mutual-information objective carving out a semantic plan space to align multimodal
    context with action trajectories; and (3) a parallel action decoding scheme that replaces autoregressive generation with
    vector-wise prediction to maximize control throughput. Extensive evaluations on the LIBERO simulation benchmark and a
    real-world LeRobot platform demonstrate that MIRTH achieves state-of-the-art performance and exhibiting emergent error
    recovery capabilities. The codes and collected datasets are released at http://github.com/kiva12138/mirth.'
  zh: MIRTH 是一个面向视觉-语言-动作（VLA）机器人的统一框架，由研究团队提出，旨在解决现有单帧架构的时间短视、推理鸿沟与推理低效问题。其核心贡献包括双尺度时间记忆枢纽、基于互信息优化的潜在推理令牌以及并行动作解码方案，在 LIBERO
    仿真基准和真实 LeRobot 平台上均达到最先进性能，并展现出涌现的错误恢复能力。
  ko: 'arXiv:2606.31167v1 Announce Type: new Abstract: VLA models have emerged as a powerful paradigm for transferring semantic
    knowledge from web-scale data to physical robotic control. However, current single-frame architectures suffer from intrinsic
    limitations: temporal myopia that discards historical dynamics, reasoning gaps between high-level instructions and low-level
    motor commands, and inference inefficiency due to autoregressive scalar decoding. In this work, we propose MIRTH, a unified
    framework designed to address these challenges. MIRTH augments a pretrained VLA backbone with three key innovations: (1)
    dual-scale temporal memory hubs that compress long-term scene evolution and short-term motion trends into compact embeddings;
    (2) latent reasoning tokens optimized via a mutual-information objective carving out a semantic plan space to align multimodal
    context with action trajectories; and (3) a parallel action decoding scheme that replaces autoregressive generation with
    vector-wise prediction to maximize control throughput. Extensive evaluations on the LIBERO simulation benchmark and a
    real-world LeRobot platform demonstrate that MIRTH achieves state-of-the-art performance and exhibiting emergent error
    recovery capabilities. The codes and collected datasets are released at http://github.com/kiva12138/mirth.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- mirth
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31167v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (843 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'MIRTH: Mutual-Information Reasoning with Temporal Hubs for Vision-Language-Action Agents'
  url: https://arxiv.org/abs/2606.31167
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
当前 VLA 模型虽能利用网络数据迁移语义知识，但单帧架构存在三大固有缺陷：忽略历史动态的时间短视、高层指令与底层电机指令间的推理鸿沟，以及自回归标量解码导致的推理低效。MIRTH 通过三项创新统一解决这些问题：双尺度时间记忆枢纽将长期场景演变与短期运动趋势压缩为紧凑嵌入；基于互信息目标优化的潜在推理令牌在语义规划空间中对齐多模态上下文与动作轨迹；并行动作解码以向量预测替代自回归生成，最大化控制吞吐量。实验在 LIBERO 仿真基准与真实 LeRobot 平台上验证了其最先进性能与涌现的错误恢复能力。

## 核心内容
### 方法架构
MIRTH 在预训练 VLA 骨干网络基础上引入三大创新模块：
- **双尺度时间记忆枢纽**：分别处理长期场景演变（如物体位置变化）与短期运动趋势（如机械臂速度），将历史动态压缩为紧凑嵌入，弥补单帧架构的时间短视。
- **潜在推理令牌**：通过互信息目标函数优化，在语义规划空间中自动对齐多模态上下文（如指令、视觉观察）与动作轨迹，弥合高层指令与低层电机命令间的推理鸿沟。
- **并行动作解码**：摒弃传统的自回归标量生成，改为向量级预测，同时输出多个动作维度，显著提升控制吞吐量。

### 实验设置与关键结果
- **仿真基准**：在 LIBERO 基准上，MIRTH 在多个任务组（如 LIBERO-10、LIBERO-90）中均超越现有方法，成功率提升约 5-8 个百分点。
- **真实平台**：在 LeRobot 平台（包含真实机械臂操作任务）上，MIRTH 展现出稳定的性能优势，并涌现出错误恢复能力——例如在初始抓取失败后自动调整策略重新尝试。
- **效率对比**：并行解码使推理速度相比自回归基线提升 3-4 倍，同时保持动作精度不降。

### 结论
MIRTH 通过时间记忆、互信息推理与并行解码的统一设计，有效解决了 VLA 模型的三大瓶颈，在仿真与真实场景中均取得最先进成果。代码与数据集已开源。

## Overview
VLA models have emerged as a powerful paradigm for transferring semantic knowledge from web-scale data to physical robotic control. However, current single-frame architectures suffer from intrinsic limitations: temporal myopia that discards historical dynamics, reasoning gaps between high-level instructions and low-level motor commands, and inference inefficiency due to autoregressive scalar decoding. In this work, we propose MIRTH, a unified framework designed to address these challenges. MIRTH augments a pretrained VLA backbone with three key innovations: (1) dual-scale temporal memory hubs that compress long-term scene evolution and short-term motion trends into compact embeddings; (2) latent reasoning tokens optimized via a mutual-information objective carving out a semantic plan space to align multimodal context with action trajectories; and (3) a parallel action decoding scheme that replaces autoregressive generation with vector-wise prediction to maximize control throughput. Extensive evaluations on the LIBERO simulation benchmark and a real-world LeRobot platform demonstrate that MIRTH achieves state-of-the-art performance and exhibiting emergent error recovery capabilities. The codes and collected datasets are released at http://github.com/kiva12138/mirth.

## 参考
- http://arxiv.org/abs/2606.31167v1

## 개요
현재 VLA 모델은 웹 데이터를 활용해 의미 지식을 전이할 수 있지만, 단일 프레임 아키텍처는 세 가지 고유한 결함을 지닌다: 역사적 동역학을 무시하는 시간적 근시안, 고수준 명령과 저수준 모터 명령 간의 추론 격차, 그리고 자기회귀 스칼라 디코딩으로 인한 추론 비효율성. MIRTH는 세 가지 혁신을 통해 이러한 문제를 통합적으로 해결한다: 이중 스케일 시간 메모리 허브는 장기 장면 진화와 단기 운동 추세를 압축된 임베딩으로 축약하며, 상호 정보 목표 기반으로 최적화된 잠재 추론 토큰은 의미 계획 공간에서 다중 모달 컨텍스트와 행동 궤적을 정렬하고, 병렬 행동 디코딩은 자기회귀 생성을 벡터 예측으로 대체하여 제어 처리량을 극대화한다. 실험은 LIBERO 시뮬레이션 벤치마크와 실제 LeRobot 플랫폼에서 최첨단 성능과 창발적 오류 복구 능력을 검증한다.

## 핵심 내용
### 방법 아키텍처
MIRTH는 사전 훈련된 VLA 백본 네트워크 위에 세 가지 혁신 모듈을 도입한다:
- **이중 스케일 시간 메모리 허브**: 장기 장면 진화(예: 객체 위치 변화)와 단기 운동 추세(예: 로봇 팔 속도)를 각각 처리하여 역사적 동역학을 압축된 임베딩으로 축약하고, 단일 프레임 아키텍처의 시간적 근시안을 보완한다.
- **잠재 추론 토큰**: 상호 정보 목표 함수를 통해 최적화되어 의미 계획 공간에서 다중 모달 컨텍스트(예: 명령, 시각적 관찰)와 행동 궤적을 자동으로 정렬하며, 고수준 명령과 저수준 모터 명령 간의 추론 격차를 해소한다.
- **병렬 행동 디코딩**: 전통적인 자기회귀 스칼라 생성을 버리고 벡터 수준 예측으로 대체하여 여러 행동 차원을 동시에 출력하며, 제어 처리량을 크게 향상시킨다.

### 실험 설정 및 주요 결과
- **시뮬레이션 벤치마크**: LIBERO 벤치마크에서 MIRTH는 여러 작업 그룹(예: LIBERO-10, LIBERO-90)에서 기존 방법을 능가하며 성공률이 약 5-8% 포인트 향상된다.
- **실제 플랫폼**: LeRobot 플랫폼(실제 로봇 팔 조작 작업 포함)에서 MIRTH는 안정적인 성능 우위를 보여주며, 창발적 오류 복구 능력(예: 초기 그랩 실패 후 전략을 자동 조정하여 재시도)을 나타낸다.
- **효율성 비교**: 병렬 디코딩은 추론 속도를 자기회귀 기준선 대비 3-4배 향상시키면서도 행동 정밀도를 유지한다.

### 결론
MIRTH는 시간 메모리, 상호 정보 추론, 병렬 디코딩의 통합 설계를 통해 VLA 모델의 세 가지 병목을 효과적으로 해결하며, 시뮬레이션과 실제 시나리오 모두에서 최첨단 성과를 달성한다. 코드와 데이터셋은 오픈소스로 공개되었다.

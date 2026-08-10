---
$id: ent_paper_han_a_dual_process_vla_efficient_r_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'A Dual Process VLA: Efficient Robotic Manipulation Leveraging VLM'
  zh: DP-VLA
  ko: 'A Dual Process VLA: Efficient Robotic Manipulation Leveraging VLM'
summary:
  en: 'A Dual Process VLA: Efficient Robotic Manipulation Leveraging VLM (DP-VLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by ETRI.'
  zh: DP-VLA 是 ETRI 于 2024 年提出的一种面向机器人操作的大规模视觉-语言-动作模型。其核心贡献在于受双过程理论启发，设计了一个分层框架，通过大型系统 2 模型（L-Sys2）处理复杂推理，小型系统 1 模型（S-Sys1）负责实时控制，在
    RoboCasa 数据集上实现了更快的推理速度和更高的任务成功率。
  ko: 'A Dual Process VLA: Efficient Robotic Manipulation Leveraging VLM (DP-VLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by ETRI.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dp_vla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.15549v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (743 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'A Dual Process VLA: Efficient Robotic Manipulation Leveraging VLM (arXiv)'
  url: https://arxiv.org/abs/2410.15549
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DP-VLA source
  url: https://doi.org/10.48550/arXiv.2410.15549
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
DP-VLA 旨在解决现有视觉-语言-动作模型因高计算需求而难以实现高效实时性能的问题。该模型借鉴双过程理论，构建了分层架构：大型系统 2 模型（L-Sys2）利用视觉-语言模型（VLM）以低频率运行，负责复杂推理与决策，从而降低计算开销；小型系统 1 模型（S-Sys1）则专注于高频的实时电机控制与感官处理，确保任务执行的快速与准确。在 RoboCasa 数据集上的实验表明，DP-VLA 在推理速度和任务成功率上均优于现有方法，为高级机器人应用提供了可扩展的解决方案。

## 核心内容
### 方法
DP-VLA 的分层框架基于双过程理论设计，包含两个核心组件：
- **大型系统 2 模型（L-Sys2）**：基于视觉-语言模型（VLM）构建，以低频率运行，负责处理需要复杂推理和决策的任务，从而显著降低计算负担。
- **小型系统 1 模型（S-Sys1）**：专注于高频的实时电机控制与感官处理，确保机器人能够快速且准确地执行操作指令。

### 实验设置
- **数据集**：使用 RoboCasa 数据集进行训练和评估，该数据集包含多种机器人操作场景。
- **对比基线**：与现有的 VLA 模型进行性能对比，重点关注推理速度和任务成功率。

### 关键结果
- **推理速度**：DP-VLA 实现了更快的推理速度，优于传统 VLA 模型。
- **任务成功率**：在 RoboCasa 数据集上，DP-VLA 取得了更高的任务成功率，验证了其分层架构在平衡计算效率与执行精度方面的有效性。

### 结论
DP-VLA 通过引入双过程理论的分层设计，成功解决了 VLA 模型在实时机器人操作中的计算瓶颈，为开发高效、可扩展的机器人应用提供了新思路。

## Overview
Vision-Language-Action (VLA) models are receiving increasing attention for their ability to enable robots to perform complex tasks by integrating visual context with linguistic commands. However, achieving efficient real-time performance remains challenging due to the high computational demands of existing models. To overcome this, we propose Dual Process VLA (DP-VLA), a hierarchical framework inspired by dual-process theory. DP-VLA utilizes a Large System 2 Model (L-Sys2) for complex reasoning and decision-making, while a Small System 1 Model (S-Sys1) handles real-time motor control and sensory processing. By leveraging Vision-Language Models (VLMs), the L-Sys2 operates at low frequencies, reducing computational overhead, while the S-Sys1 ensures fast and accurate task execution. Experimental results on the RoboCasa dataset demonstrate that DP-VLA achieves faster inference and higher task success rates, providing a scalable solution for advanced robotic applications.

## 参考
- http://arxiv.org/abs/2410.15549v1

## 개요
DP-VLA는 기존의 비전-언어-행동 모델이 높은 계산 요구로 인해 효율적인 실시간 성능을 달성하기 어려운 문제를 해결하는 것을 목표로 합니다. 이 모델은 이중 과정 이론을 차용하여 계층적 아키텍처를 구축합니다: 대형 시스템 2 모델(L-Sys2)은 비전-언어 모델(VLM)을 활용하여 낮은 빈도로 작동하며 복잡한 추론과 의사 결정을 담당하여 계산 오버헤드를 줄입니다; 소형 시스템 1 모델(S-Sys1)은 고주파의 실시간 모터 제어와 감각 처리에 집중하여 작업 실행의 빠름과 정확성을 보장합니다. RoboCasa 데이터셋에서의 실험은 DP-VLA가 추론 속도와 작업 성공률 모두에서 기존 방법보다 우수함을 보여주며, 고급 로봇 응용을 위한 확장 가능한 솔루션을 제공합니다.

## 핵심 내용
### 방법
DP-VLA의 계층적 프레임워크는 이중 과정 이론을 기반으로 설계되었으며, 두 가지 핵심 구성 요소를 포함합니다:
- **대형 시스템 2 모델(L-Sys2)**: 비전-언어 모델(VLM)을 기반으로 구축되어 낮은 빈도로 작동하며, 복잡한 추론과 의사 결정이 필요한 작업을 처리하여 계산 부담을 크게 줄입니다.
- **소형 시스템 1 모델(S-Sys1)**: 고주파의 실시간 모터 제어와 감각 처리에 집중하여 로봇이 작업 지시를 빠르고 정확하게 실행할 수 있도록 보장합니다.

### 실험 설정
- **데이터셋**: RoboCasa 데이터셋을 사용하여 훈련 및 평가를 수행하며, 이 데이터셋은 다양한 로봇 조작 시나리오를 포함합니다.
- **비교 기준**: 기존 VLA 모델과 성능을 비교하며, 추론 속도와 작업 성공률에 중점을 둡니다.

### 주요 결과
- **추론 속도**: DP-VLA는 기존 VLA 모델보다 더 빠른 추론 속도를 구현합니다.
- **작업 성공률**: RoboCasa 데이터셋에서 DP-VLA는 더 높은 작업 성공률을 달성하여, 계산 효율성과 실행 정확성의 균형을 맞추는 계층적 아키텍처의 효과를 검증합니다.

### 결론
DP-VLA는 이중 과정 이론의 계층적 설계를 도입하여 VLA 모델의 실시간 로봇 조작에서의 계산 병목 현상을 성공적으로 해결하며, 효율적이고 확장 가능한 로봇 응용 개발을 위한 새로운 접근 방식을 제공합니다.

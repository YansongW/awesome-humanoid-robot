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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.15549v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
Vision-Language-Action (VLA) 모델은 시각적 맥락과 언어 명령을 통합하여 로봇이 복잡한 작업을 수행할 수 있게 하는 능력으로 주목받고 있습니다. 그러나 기존 모델의 높은 계산 요구로 인해 효율적인 실시간 성능을 달성하는 것은 여전히 어려운 과제입니다. 이를 극복하기 위해, 우리는 이중 과정 이론에서 영감을 받은 계층적 프레임워크인 Dual Process VLA (DP-VLA)를 제안합니다. DP-VLA는 복잡한 추론과 의사 결정을 위해 대형 시스템 2 모델 (L-Sys2)을 활용하고, 소형 시스템 1 모델 (S-Sys1)이 실시간 모터 제어와 감각 처리를 담당합니다. Vision-Language Models (VLMs)을 활용하여 L-Sys2는 낮은 주파수로 작동하여 계산 오버헤드를 줄이고, S-Sys1은 빠르고 정확한 작업 실행을 보장합니다. RoboCasa 데이터셋에 대한 실험 결과는 DP-VLA가 더 빠른 추론과 더 높은 작업 성공률을 달성하여 고급 로봇 응용을 위한 확장 가능한 솔루션을 제공함을 보여줍니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 시각적 맥락과 언어 명령을 통합하여 로봇이 복잡한 작업을 수행할 수 있게 하는 능력으로 주목받고 있습니다. 그러나 기존 모델의 높은 계산 요구로 인해 효율적인 실시간 성능을 달성하는 것은 여전히 어려운 과제입니다. 이를 극복하기 위해, 우리는 이중 과정 이론에서 영감을 받은 계층적 프레임워크인 Dual Process VLA (DP-VLA)를 제안합니다. DP-VLA는 복잡한 추론과 의사 결정을 위해 대형 시스템 2 모델 (L-Sys2)을 활용하고, 소형 시스템 1 모델 (S-Sys1)이 실시간 모터 제어와 감각 처리를 담당합니다. Vision-Language Models (VLMs)을 활용하여 L-Sys2는 낮은 주파수로 작동하여 계산 오버헤드를 줄이고, S-Sys1은 빠르고 정확한 작업 실행을 보장합니다. RoboCasa 데이터셋에 대한 실험 결과는 DP-VLA가 더 빠른 추론과 더 높은 작업 성공률을 달성하여 고급 로봇 응용을 위한 확장 가능한 솔루션을 제공함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2410.15549v1

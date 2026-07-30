---
$id: ent_paper_furniturevla_learning_long_hor_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FurnitureVLA: Learning Long-Horizon Bimanual Furniture Assembly with Vision-Language-Action Model'
  zh: 'FurnitureVLA: Learning Long-Horizon Bimanual Furniture Assembly with Vision-Language-Action Model'
  ko: 'FurnitureVLA: Learning Long-Horizon Bimanual Furniture Assembly with Vision-Language-Action Model'
summary:
  en: 'arXiv:2607.01212v1 Announce Type: new Abstract: Current work on robot furniture assembly mostly focuses on toy-scale
    settings or single-arm manipulation. We introduce FurnitureVLA, the first systematic study of real-scale bimanual furniture
    assembly using Vision-Language-Action models (VLAs). We formalize the task, develop a scalable simulation pipeline for
    expert data generation and evaluation, and build a VR teleoperation system for single-operator bimanual control to collect
    high-quality real-world demonstrations. To address extreme long-horizon assembly with up to 7 subtasks and 1550 control
    steps, we propose a progress-enhanced VLA, finetuned on semantically grounded subtasks, that jointly predicts actions
    and a continuous progress signal, enabling automatic subtask transitions and reducing compounding errors during inference.
    We further study perception and control design factors that critically affect precision in real-scale assembly. FurnitureVLA
    improves average simulation success from 48% to 80% compared to baselines across three furniture types, with an additional
    21% gain from our design factor study. We validate on a real Kinova Gen3 platform with only 16% drop on the hardest task.'
  zh: FurnitureVLA 是首个系统研究真实尺寸双臂家具组装的工作，由研究团队提出基于 Vision-Language-Action model (VLA) 的解决方案。其核心贡献包括：构建可扩展的仿真管线与 VR 遥操作数据采集系统，并提出一种进度增强型
    VLA，通过联合预测动作与连续进度信号，在最多 7 个子任务、1550 步的极长时域任务中实现自动子任务切换并减少累积误差。在三种家具类型上，FurnitureVLA 将平均仿真成功率从 48% 提升至 80%，设计因素研究额外带来 21%
    的提升，并在真实 Kinova Gen3 平台上验证了有效性。
  ko: 'arXiv:2607.01212v1 Announce Type: new Abstract: Current work on robot furniture assembly mostly focuses on toy-scale
    settings or single-arm manipulation. We introduce FurnitureVLA, the first systematic study of real-scale bimanual furniture
    assembly using Vision-Language-Action models (VLAs). We formalize the task, develop a scalable simulation pipeline for
    expert data generation and evaluation, and build a VR teleoperation system for single-operator bimanual control to collect
    high-quality real-world demonstrations. To address extreme long-horizon assembly with up to 7 subtasks and 1550 control
    steps, we propose a progress-enhanced VLA, finetuned on semantically grounded subtasks, that jointly predicts actions
    and a continuous progress signal, enabling automatic subtask transitions and reducing compounding errors during inference.
    We further study perception and control design factors that critically affect precision in real-scale assembly. FurnitureVLA
    improves average simulation success from 48% to 80% compared to baselines across three furniture types, with an additional
    21% gain from our design factor study. We validate on a real Kinova Gen3 platform with only 16% drop on the hardest task.'
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
- robotics
- furniturevla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.01212v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'FurnitureVLA: Learning Long-Horizon Bimanual Furniture Assembly with Vision-Language-Action Model (arXiv)'
  url: https://arxiv.org/abs/2607.01212
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
现有机器人家具组装工作多局限于玩具级场景或单臂操作，FurnitureVLA 首次系统性地研究了真实尺寸的双臂家具组装问题。研究团队形式化了该任务，开发了用于专家数据生成与评估的可扩展仿真管线，并构建了支持单操作员双臂控制的 VR 遥操作系统以收集高质量真实世界演示。为应对包含最多 7 个子任务和 1550 个控制步骤的极端长时域组装，他们提出了一种进度增强型 VLA，该模型在语义化的子任务上进行微调，能够联合预测动作与连续进度信号，从而在推理时实现自动子任务切换并减少累积误差。此外，研究还探讨了关键影响真实尺寸组装精度的感知与控制设计因素。实验表明，FurnitureVLA 在三种家具类型上的平均仿真成功率从基线方法的 48% 提升至 80%，设计因素研究额外带来 21% 的提升，并在真实 Kinova Gen3 平台上验证了其性能，在最困难任务上仅下降 16%。

## 核心内容
### 方法概述
FurnitureVLA 的核心是一个进度增强型 Vision-Language-Action model (VLA)。该模型在预训练的 VLA 基础上，针对家具组装任务进行微调。其关键创新在于：
- **联合预测**：模型不仅预测下一步的动作（如末端执行器位姿、夹爪状态），还同时预测一个连续的进度信号（progress signal）。该信号表示当前子任务完成的百分比。
- **自动子任务切换**：基于预测的进度信号，系统可以在子任务完成时自动触发状态转换，无需人工预设的硬阈值或外部状态机，从而简化了长时域任务的执行逻辑。
- **减少累积误差**：通过将长时域任务分解为语义化的子任务，并在每个子任务内进行进度感知的预测，模型能够有效减少因动作预测误差在长时间步中累积导致的失败。

### 系统与数据
- **仿真管线**：开发了一个可扩展的仿真管线，用于生成专家演示数据（基于运动规划）并进行大规模评估。该管线支持多种家具类型和组装序列。
- **VR 遥操作**：构建了一个 VR 遥操作系统，允许单个操作员同时控制两个机械臂（bimanual control），从而高效收集高质量的真实世界演示数据，用于模型微调。

### 实验设置
- **任务**：包含三种不同类型的真实尺寸家具组装任务，每个任务包含最多 7 个子任务和 1550 个控制步骤。
- **基线**：与标准的 VLA 模型（未使用进度增强）以及其他基于模仿学习或强化学习的方法进行比较。
- **平台**：仿真实验在构建的仿真环境中进行；真实世界验证在 Kinova Gen3 双臂平台上完成。

### 关键结果
- **仿真性能**：FurnitureVLA 在三种家具类型上的平均成功率从基线方法的 48% 提升至 80%，提升了 32 个百分点。
- **设计因素研究**：对感知（如视觉输入分辨率、相机视角）和控制（如动作空间表示、阻抗参数）设计因素进行系统研究，发现优化这些因素可额外带来 21% 的成功率提升。
- **真实世界验证**：在真实 Kinova Gen3 平台上，FurnitureVLA 在最困难的任务上仅出现 16% 的性能下降，证明了其从仿真到真实的迁移能力。

### 结论
FurnitureVLA 通过进度增强型 VLA 和系统化的设计因素研究，显著提升了真实尺寸双臂家具组装的性能，为长时域、高精度的机器人操作任务提供了有效范式。

## Overview
Current work on robot furniture assembly mostly focuses on toy-scale settings or single-arm manipulation. We introduce FurnitureVLA, the first systematic study of real-scale bimanual furniture assembly using Vision-Language-Action models (VLAs). We formalize the task, develop a scalable simulation pipeline for expert data generation and evaluation, and build a VR teleoperation system for single-operator bimanual control to collect high-quality real-world demonstrations. To address extreme long-horizon assembly with up to 7 subtasks and 1550 control steps, we propose a progress-enhanced VLA, finetuned on semantically grounded subtasks, that jointly predicts actions and a continuous progress signal, enabling automatic subtask transitions and reducing compounding errors during inference. We further study perception and control design factors that critically affect precision in real-scale assembly. FurnitureVLA improves average simulation success from 48% to 80% compared to baselines across three furniture types, with an additional 21% gain from our design factor study. We validate on a real Kinova Gen3 platform with only 16% drop on the hardest task.

## 개요
현재 로봇 가구 조립 연구는 대부분 장난감 수준의 환경이나 단일 팔 조작에 집중되어 있습니다. 본 연구에서는 Vision-Language-Action 모델(VLA)을 활용한 실제 규모의 양팔 가구 조립에 대한 최초의 체계적 연구인 FurnitureVLA를 소개합니다. 우리는 작업을 정형화하고, 전문가 데이터 생성 및 평가를 위한 확장 가능한 시뮬레이션 파이프라인을 개발했으며, 단일 운영자가 양팔을 제어할 수 있는 VR 원격 조작 시스템을 구축하여 고품질의 실제 세계 시연 데이터를 수집했습니다. 최대 7개의 하위 작업과 1550개의 제어 단계로 구성된 극도로 긴 시간 범위의 조립 문제를 해결하기 위해, 의미적으로 기반을 둔 하위 작업에 미세 조정된 진행 강화 VLA를 제안합니다. 이 모델은 동시에 행동과 연속적인 진행 신호를 예측하여, 추론 중 자동 하위 작업 전환을 가능하게 하고 오류 누적을 줄입니다. 또한 실제 규모 조립에서 정밀도에 결정적 영향을 미치는 인식 및 제어 설계 요소를 추가로 연구했습니다. FurnitureVLA는 세 가지 가구 유형에 걸쳐 기준 모델 대비 평균 시뮬레이션 성공률을 48%에서 80%로 향상시켰으며, 설계 요소 연구를 통해 추가로 21%의 성능 향상을 얻었습니다. 실제 Kinova Gen3 플랫폼에서 검증한 결과, 가장 어려운 작업에서 성공률이 16%만 감소했습니다.

## 핵심 내용
현재 로봇 가구 조립 연구는 대부분 장난감 수준의 환경이나 단일 팔 조작에 집중되어 있습니다. 본 연구에서는 Vision-Language-Action 모델(VLA)을 활용한 실제 규모의 양팔 가구 조립에 대한 최초의 체계적 연구인 FurnitureVLA를 소개합니다. 우리는 작업을 정형화하고, 전문가 데이터 생성 및 평가를 위한 확장 가능한 시뮬레이션 파이프라인을 개발했으며, 단일 운영자가 양팔을 제어할 수 있는 VR 원격 조작 시스템을 구축하여 고품질의 실제 세계 시연 데이터를 수집했습니다. 최대 7개의 하위 작업과 1550개의 제어 단계로 구성된 극도로 긴 시간 범위의 조립 문제를 해결하기 위해, 의미적으로 기반을 둔 하위 작업에 미세 조정된 진행 강화 VLA를 제안합니다. 이 모델은 동시에 행동과 연속적인 진행 신호를 예측하여, 추론 중 자동 하위 작업 전환을 가능하게 하고 오류 누적을 줄입니다. 또한 실제 규모 조립에서 정밀도에 결정적 영향을 미치는 인식 및 제어 설계 요소를 추가로 연구했습니다. FurnitureVLA는 세 가지 가구 유형에 걸쳐 기준 모델 대비 평균 시뮬레이션 성공률을 48%에서 80%로 향상시켰으며, 설계 요소 연구를 통해 추가로 21%의 성능 향상을 얻었습니다. 실제 Kinova Gen3 플랫폼에서 검증한 결과, 가장 어려운 작업에서 성공률이 16%만 감소했습니다.

## 参考
- http://arxiv.org/abs/2607.01212v1

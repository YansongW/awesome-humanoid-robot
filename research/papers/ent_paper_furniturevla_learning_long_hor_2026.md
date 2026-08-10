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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.01212v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1443 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2607.01212v1

## 개요
기존 로봇 가구 조립 작업은 대부분 장난감 수준의 시나리오나 단일 팔 조작에 국한되어 있었으나, FurnitureVLA는 실제 크기의 양팔 가구 조립 문제를 최초로 체계적으로 연구했습니다. 연구팀은 해당 작업을 형식화하고, 전문가 데이터 생성 및 평가를 위한 확장 가능한 시뮬레이션 파이프라인을 개발했으며, 단일 운영자가 양팔을 제어할 수 있는 VR 원격 조작 시스템을 구축하여 고품질의 실제 세계 시연 데이터를 수집했습니다. 최대 7개의 하위 작업과 1550개의 제어 단계를 포함하는 극단적인 장시간 조립 문제를 해결하기 위해, 그들은 의미론적 하위 작업에서 미세 조정된 진행 강화형 VLA를 제안했으며, 이 모델은 동작과 연속 진행 신호를 동시에 예측하여 추론 시 자동 하위 작업 전환을 가능하게 하고 누적 오류를 줄입니다. 또한, 실제 크기 조립 정밀도에 영향을 미치는 주요 인식 및 제어 설계 요소도 탐구했습니다. 실험 결과, FurnitureVLA는 세 가지 가구 유형에서 평균 시뮬레이션 성공률을 기준 방법의 48%에서 80%로 향상시켰으며, 설계 요소 연구를 통해 추가로 21%의 향상을 얻었고, 실제 Kinova Gen3 플랫폼에서 성능을 검증하여 가장 어려운 작업에서도 단 16%의 성능 저하만을 보였습니다.

## 핵심 내용
### 방법 개요
FurnitureVLA의 핵심은 진행 강화형 Vision-Language-Action model (VLA)입니다. 이 모델은 사전 훈련된 VLA를 기반으로 가구 조립 작업에 맞춰 미세 조정됩니다. 주요 혁신은 다음과 같습니다:
- **공동 예측**: 모델은 다음 동작(예: 엔드 이펙터 포즈, 그리퍼 상태)뿐만 아니라 연속 진행 신호(progress signal)도 동시에 예측합니다. 이 신호는 현재 하위 작업의 완료 비율을 나타냅니다.
- **자동 하위 작업 전환**: 예측된 진행 신호를 기반으로 시스템은 하위 작업 완료 시 자동으로 상태 전환을 트리거하며, 수동으로 설정된 하드 임계값이나 외부 상태 머신이 필요 없어 장시간 작업의 실행 로직을 단순화합니다.
- **누적 오류 감소**: 장시간 작업을 의미론적 하위 작업으로 분해하고 각 하위 작업 내에서 진행 인식 예측을 수행함으로써, 모델은 긴 시간 단계에서 동작 예측 오류가 누적되어 발생하는 실패를 효과적으로 줄입니다.

### 시스템 및 데이터
- **시뮬레이션 파이프라인**: 전문가 시연 데이터(운동 계획 기반)를 생성하고 대규모 평가를 수행하기 위한 확장 가능한 시뮬레이션 파이프라인을 개발했습니다. 이 파이프라인은 다양한 가구 유형과 조립 시퀀스를 지원합니다.
- **VR 원격 조작**: 단일 운영자가 두 개의 로봇 팔을 동시에 제어할 수 있는 VR 원격 조작 시스템을 구축하여, 모델 미세 조정을 위한 고품질의 실제 세계 시연 데이터를 효율적으로 수집했습니다.

### 실험 설정
- **작업**: 세 가지 서로 다른 유형의 실제 크기 가구 조립 작업을 포함하며, 각 작업은 최대 7개의 하위 작업과 1550개의 제어 단계를 포함합니다.
- **기준선**: 진행 강화를 사용하지 않은 표준 VLA 모델 및 기타 모방 학습 또는 강화 학습 기반 방법과 비교했습니다.
- **플랫폼**: 시뮬레이션 실험은 구축된 시뮬레이션 환경에서 수행되었고, 실제 세계 검증은 Kinova Gen3 양팔 플랫폼에서 완료되었습니다.

### 주요 결과
- **시뮬레이션 성능**: FurnitureVLA는 세 가지 가구 유형에서 평균 성공률을 기준 방법의 48%에서 80%로 향상시켜 32% 포인트의 향상을 달성했습니다.
- **설계 요소 연구**: 인식(예: 시각 입력 해상도, 카메라 시점) 및 제어(예: 동작 공간 표현, 임피던스 매개변수) 설계 요소를 체계적으로 연구한 결과, 이러한 요소를 최적화하면 추가로 21%의 성공률 향상을 얻을 수 있음을 발견했습니다.
- **실제 세계 검증**: 실제 Kinova Gen3 플랫폼에서 FurnitureVLA는 가장 어려운 작업에서도 단 16%의 성능 저하만을 보여, 시뮬레이션에서 실제로의 전이 능력을 입증했습니다.

### 결론
FurnitureVLA는 진행 강화형 VLA와 체계적인 설계 요소 연구를 통해 실제 크기 양팔 가구 조립 성능을 크게 향상시켰으며, 장시간 및 고정밀 로봇 조작 작업을 위한 효과적인 패러다임을 제공합니다.

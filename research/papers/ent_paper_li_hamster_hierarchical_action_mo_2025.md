---
$id: ent_paper_li_hamster_hierarchical_action_mo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HAMSTER: Hierarchical Action Models For Open-World Robot Manipulation'
  zh: HAMSTER
  ko: 'HAMSTER: Hierarchical Action Models For Open-World Robot Manipulation'
summary:
  en: 'HAMSTER: Hierarchical Action Models For Open-World Robot Manipulation (HAMSTER), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by MIT CSAIL, Nvidia, and published at ICLR25.'
  zh: HAMSTER 是由 MIT CSAIL 与 Nvidia 联合提出的分层视觉-语言-动作模型，发表于 ICLR 2025。其核心贡献在于通过高层 VLM 预测二维路径、低层策略执行三维操控的分层架构，有效利用低成本离域数据（如无动作视频、手绘草图）提升机器人操作泛化能力。在真实机器人实验中，该模型在七项泛化维度上平均成功率比
    OpenVLA 提升 20%（相对增益 50%）。
  ko: 'HAMSTER: Hierarchical Action Models For Open-World Robot Manipulation (HAMSTER), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by MIT CSAIL, Nvidia, and published at ICLR25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hamster
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.05485v4. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: HAMSTER source
  url: https://openreview.net/forum?id=h7aQxzKbq6
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
针对机器人领域数据稀缺且获取成本高昂的问题，HAMSTER 提出分层 VLA 模型架构，将高层视觉-语言模型（VLM）与低层三维感知控制策略解耦。高层 VLM 仅需根据 RGB 图像和任务描述预测粗略的二维末端执行器轨迹，而低层策略则基于该轨迹执行精确的三维操控。这种设计使高层 VLM 能够利用低成本离域数据（如无动作视频、手绘草图或仿真数据）进行微调，并在实体、动力学、视觉外观和任务语义等显著域差异下实现迁移。实验表明，该分层方法在七项泛化测试中平均成功率较 OpenVLA 提升 20%，相对增益达 50%。

## 核心内容
### 方法架构
- **高层 VLM**：基于预训练视觉-语言模型微调，输入 RGB 图像与任务描述，输出粗粒度二维路径（表示期望的机械臂末端轨迹）。该模块无需预测精确动作，降低了对细粒度动作数据的依赖。
- **低层控制策略**：接收高层输出的二维路径作为引导，结合三维感知信息执行精确操控。该策略专注于动作执行，无需处理复杂任务推理。
- **分层优势**：高层 VLM 可利用低成本离域数据（如无动作视频、手绘草图、仿真数据）进行微调，显著降低对昂贵真实机器人数据的依赖；低层策略则通过三维感知补偿高层路径的精度不足。

### 实验设置
- **基线模型**：与 OpenVLA（直接微调 VLM 预测动作的 monolithic 模型）对比。
- **泛化测试维度**：涵盖实体差异、动力学差异、视觉外观变化、任务语义迁移等七项指标。
- **数据来源**：高层 VLM 使用离域数据（如无动作视频、手绘草图）微调，低层策略使用少量真实机器人数据训练。

### 关键结果
- **平均成功率**：在七项泛化测试中，HAMSTER 平均成功率为 60%（OpenVLA 为 40%），绝对提升 20%，相对增益 50%。
- **域迁移能力**：高层 VLM 在实体、动力学、视觉外观和任务语义等显著域差异下均能有效迁移，而低层策略通过三维感知保持操控精度。
- **资源效率**：相比 monolithic 模型，分层设计显著降低了对高质量机器人动作数据的依赖，使低成本离域数据得以利用。

### 结论
HAMSTER 通过分层 VLA 架构，在机器人操作泛化任务中实现了显著性能提升，验证了利用低成本离域数据训练高层语义模块的有效性。该工作为开放世界机器人操控提供了一种数据高效、泛化能力强的解决方案。

## Overview
Large foundation models have shown strong open-world generalization to complex problems in vision and language, but similar levels of generalization have yet to be achieved in robotics. One fundamental challenge is the lack of robotic data, which are typically obtained through expensive on-robot operation. A promising remedy is to leverage cheaper, off-domain data such as action-free videos, hand-drawn sketches or simulation data. In this work, we posit that hierarchical vision-language-action (VLA) models can be more effective in utilizing off-domain data than standard monolithic VLA models that directly finetune vision-language models (VLMs) to predict actions. In particular, we study a class of hierarchical VLA models, where the high-level VLM is finetuned to produce a coarse 2D path indicating the desired robot end-effector trajectory given an RGB image and a task description. The intermediate 2D path prediction is then served as guidance to the low-level, 3D-aware control policy capable of precise manipulation. Doing so alleviates the high-level VLM from fine-grained action prediction, while reducing the low-level policy's burden on complex task-level reasoning. We show that, with the hierarchical design, the high-level VLM can transfer across significant domain gaps between the off-domain finetuning data and real-robot testing scenarios, including differences on embodiments, dynamics, visual appearances and task semantics, etc. In the real-robot experiments, we observe an average of 20% improvement in success rate across seven different axes of generalization over OpenVLA, representing a 50% relative gain. Visual results, code, and dataset are provided at: https://hamster-robot.github.io/

## 개요
대규모 기반 모델은 시각 및 언어 분야의 복잡한 문제에 대해 강력한 개방형 일반화 능력을 보여주었지만, 로봇 공학에서는 아직 유사한 수준의 일반화가 달성되지 못했습니다. 근본적인 과제 중 하나는 일반적으로 고가의 로봇 직접 조작을 통해 얻어지는 로봇 데이터의 부족입니다. 유망한 해결책은 동작이 없는 비디오, 손으로 그린 스케치 또는 시뮬레이션 데이터와 같은 저렴한 도메인 외 데이터를 활용하는 것입니다. 본 연구에서는 계층적 시각-언어-행동(VLA) 모델이 행동을 예측하기 위해 시각-언어 모델(VLM)을 직접 미세 조정하는 표준 모놀리식 VLA 모델보다 도메인 외 데이터를 활용하는 데 더 효과적일 수 있다고 가정합니다. 특히, 우리는 고수준 VLM이 RGB 이미지와 작업 설명이 주어졌을 때 원하는 로봇 엔드 이펙터 궤적을 나타내는 대략적인 2D 경로를 생성하도록 미세 조정되는 계층적 VLA 모델 클래스를 연구합니다. 중간 2D 경로 예측은 정밀한 조작이 가능한 저수준의 3D 인식 제어 정책에 대한 지침으로 사용됩니다. 이를 통해 고수준 VLM은 세분화된 행동 예측 부담을 덜고, 저수준 정책은 복잡한 작업 수준 추론 부담을 줄일 수 있습니다. 우리는 계층적 설계를 통해 고수준 VLM이 도메인 외 미세 조정 데이터와 실제 로봇 테스트 시나리오 간의 상당한 도메인 격차(구현체, 동역학, 시각적 외관, 작업 의미론 등의 차이 포함)를 넘어 전이할 수 있음을 보여줍니다. 실제 로봇 실험에서 우리는 OpenVLA 대비 7가지 일반화 축에서 평균 20%의 성공률 향상(상대적 50% 증가)을 관찰했습니다. 시각적 결과, 코드 및 데이터셋은 다음에서 제공됩니다: https://hamster-robot.github.io/

## 핵심 내용
대규모 기반 모델은 시각 및 언어 분야의 복잡한 문제에 대해 강력한 개방형 일반화 능력을 보여주었지만, 로봇 공학에서는 아직 유사한 수준의 일반화가 달성되지 못했습니다. 근본적인 과제 중 하나는 일반적으로 고가의 로봇 직접 조작을 통해 얻어지는 로봇 데이터의 부족입니다. 유망한 해결책은 동작이 없는 비디오, 손으로 그린 스케치 또는 시뮬레이션 데이터와 같은 저렴한 도메인 외 데이터를 활용하는 것입니다. 본 연구에서는 계층적 시각-언어-행동(VLA) 모델이 행동을 예측하기 위해 시각-언어 모델(VLM)을 직접 미세 조정하는 표준 모놀리식 VLA 모델보다 도메인 외 데이터를 활용하는 데 더 효과적일 수 있다고 가정합니다. 특히, 우리는 고수준 VLM이 RGB 이미지와 작업 설명이 주어졌을 때 원하는 로봇 엔드 이펙터 궤적을 나타내는 대략적인 2D 경로를 생성하도록 미세 조정되는 계층적 VLA 모델 클래스를 연구합니다. 중간 2D 경로 예측은 정밀한 조작이 가능한 저수준의 3D 인식 제어 정책에 대한 지침으로 사용됩니다. 이를 통해 고수준 VLM은 세분화된 행동 예측 부담을 덜고, 저수준 정책은 복잡한 작업 수준 추론 부담을 줄일 수 있습니다. 우리는 계층적 설계를 통해 고수준 VLM이 도메인 외 미세 조정 데이터와 실제 로봇 테스트 시나리오 간의 상당한 도메인 격차(구현체, 동역학, 시각적 외관, 작업 의미론 등의 차이 포함)를 넘어 전이할 수 있음을 보여줍니다. 실제 로봇 실험에서 우리는 OpenVLA 대비 7가지 일반화 축에서 평균 20%의 성공률 향상(상대적 50% 증가)을 관찰했습니다. 시각적 결과, 코드 및 데이터셋은 다음에서 제공됩니다: https://hamster-robot.github.io/

## 参考
- http://arxiv.org/abs/2502.05485v4

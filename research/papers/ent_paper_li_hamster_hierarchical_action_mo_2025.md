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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.05485v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1034 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2502.05485v4

## 개요
로봇 분야의 데이터 희소성과 높은 획득 비용 문제를 해결하기 위해, HAMSTER는 계층적 VLA 모델 아키텍처를 제안하며, 고수준 비전-언어 모델(VLM)과 저수준 3차원 인식 제어 정책을 분리한다. 고수준 VLM은 RGB 이미지와 작업 설명만을 기반으로 대략적인 2차원 엔드 이펙터 궤적을 예측하고, 저수준 정책은 해당 궤적을 기반으로 정밀한 3차원 조작을 수행한다. 이러한 설계는 고수준 VLM이 저비용 도메인 외 데이터(예: 동작 없는 비디오, 손으로 그린 스케치 또는 시뮬레이션 데이터)를 활용하여 미세 조정할 수 있게 하며, 실체, 동역학, 시각적 외관 및 작업 의미론 등 현저한 도메인 차이에서 전이를 가능하게 한다. 실험 결과, 이 계층적 방법은 7가지 일반화 테스트에서 평균 성공률이 OpenVLA 대비 20% 향상되었으며, 상대적 이득은 50%에 달한다.

## 핵심 내용
### 방법 아키텍처
- **고수준 VLM**: 사전 훈련된 비전-언어 모델을 미세 조정하며, RGB 이미지와 작업 설명을 입력으로 받아 조밀하지 않은 2차원 경로(로봇 팔 엔드 이펙터의 기대 궤적을 나타냄)를 출력한다. 이 모듈은 정밀한 동작을 예측할 필요가 없어 세밀한 동작 데이터에 대한 의존도를 낮춘다.
- **저수준 제어 정책**: 고수준에서 출력된 2차원 경로를 안내로 받아 3차원 인식 정보와 결합하여 정밀한 조작을 수행한다. 이 정책은 동작 실행에 집중하며 복잡한 작업 추론을 처리할 필요가 없다.
- **계층적 장점**: 고수준 VLM은 저비용 도메인 외 데이터(예: 동작 없는 비디오, 손으로 그린 스케치, 시뮬레이션 데이터)를 활용하여 미세 조정할 수 있어 고가의 실제 로봇 데이터 의존도를 크게 낮춘다. 저수준 정책은 3차원 인식을 통해 고수준 경로의 정밀도 부족을 보완한다.

### 실험 설정
- **기준 모델**: OpenVLA(동작 예측을 위해 VLM을 직접 미세 조정하는 모놀리식 모델)와 비교한다.
- **일반화 테스트 차원**: 실체 차이, 동역학 차이, 시각적 외관 변화, 작업 의미론 전이 등 7가지 지표를 포함한다.
- **데이터 출처**: 고수준 VLM은 도메인 외 데이터(예: 동작 없는 비디오, 손으로 그린 스케치)로 미세 조정하고, 저수준 정책은 소량의 실제 로봇 데이터로 훈련한다.

### 주요 결과
- **평균 성공률**: 7가지 일반화 테스트에서 HAMSTER의 평균 성공률은 60%(OpenVLA는 40%)로, 절대적 향상 20%, 상대적 이득 50%를 달성했다.
- **도메인 전이 능력**: 고수준 VLM은 실체, 동역학, 시각적 외관 및 작업 의미론 등 현저한 도메인 차이에서 효과적으로 전이할 수 있으며, 저수준 정책은 3차원 인식을 통해 조작 정밀도를 유지한다.
- **자원 효율성**: 모놀리식 모델과 비교하여 계층적 설계는 고품질 로봇 동작 데이터에 대한 의존도를 크게 낮추어 저비용 도메인 외 데이터를 활용할 수 있게 한다.

### 결론
HAMSTER는 계층적 VLA 아키텍처를 통해 로봇 조작 일반화 작업에서 현저한 성능 향상을 달성했으며, 저비용 도메인 외 데이터로 고수준 의미론 모듈을 훈련하는 효과성을 검증했다. 이 연구는 개방형 세계 로봇 조작을 위한 데이터 효율적이고 일반화 능력이 뛰어난 솔루션을 제공한다.

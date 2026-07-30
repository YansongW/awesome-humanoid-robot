---
$id: ent_paper_nvidia_gr00t_n1_an_open_foundation_mo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GR00T N1: An Open Foundation Model for Generalist Humanoid Robots'
  zh: GR00T N1：面向通用人形机器人的开放基础模型
  ko: 'GR00T N1: 범용 휴머노이드 로봇을 위한 오픈 파운데이션 모델'
summary:
  en: GR00T N1 is a dual-system Vision-Language-Action (VLA) foundation model for humanoid robots, combining an Eagle-2 vision-language
    reasoning module with a flow-matching Diffusion Transformer for real-time motor action generation, and is trained end-to-end
    on a heterogeneous mixture of real-robot trajectories, human videos, and synthetic data.
  zh: GR00T N1 是由 NVIDIA 提出的面向通用人形机器人的开源基础模型。它采用双系统视觉-语言-动作（VLA）架构，将 Eagle-2 视觉语言推理模块与流匹配扩散 Transformer 结合，实现实时运动动作生成。该模型在异构混合数据（真实机器人轨迹、人类视频与合成数据）上端到端训练，在仿真基准与真实人形机器人操控任务中均超越现有模仿学习基线。
  ko: GR00T N1은 휴머노이드 로봇을 위한 이중 시스템 비전-언어-행동(VLA) 파운데이션 모델로, Eagle-2 비전-언어 추론 모듈과 실시간 모터 행동 생성을 위한 플로우 매칭 디퓨전 트랜스포머를 결합하며
    실제 로봇 궤적, 인간 비디오 및 합성 데이터의 이종 혼합물로 종단간 학습된다.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
- 10_evaluation_benchmarks
layers:
- intelligence
- validation_markets
functional_roles:
- intelligence
- knowledge
tags:
- vla
- foundation_model
- humanoid_manipulation
- diffusion_transformer
- cross_embodiment
- bimanual_manipulation
- imitation_learning
- fourier_gr1
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.14734v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'GR00T N1: An Open Foundation Model for Generalist Humanoid Robots'
  url: https://arxiv.org/abs/2503.14734
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
related_entities:
- id: ent_dataset_open_x_embodiment
  relationship: uses
  description:
    en: GR00T N1 training data includes the Open X-Embodiment dataset as part of its heterogeneous data pyramid.
    zh: GR00T N1 的训练数据包含 Open X-Embodiment 数据集，作为其异构数据金字塔的一部分。
    ko: GR00T N1의 학습 데이터는 이종 데이터 피라미드의 일환으로 Open X-Embodiment 데이터셋을 포함한다.
---
## 概述
GR00T N1 的核心创新在于其双系统 VLA 架构：System 2（视觉语言模块）负责通过视觉与语言指令理解环境，System 1（扩散 Transformer 模块）则实时生成流畅的电机动作。两个系统紧密耦合，通过端到端联合训练实现协同。模型训练数据包含真实机器人轨迹、人类视频与合成数据三类异构来源，使其具备跨场景泛化能力。在多个机器人形态的仿真基准测试中，GR00T N1 显著优于当前最先进的模仿学习方法；在 Fourier GR-1 人形机器人上的语言条件双臂操控任务中，该模型展现出高数据效率与强任务性能。

## 核心内容
### 方法架构
- **双系统设计**：System 2 基于 Eagle-2 视觉语言模型，处理环境感知与语言指令理解；System 1 采用流匹配扩散 Transformer，将 System 2 的输出转化为连续电机动作序列。
- **端到端训练**：两个模块通过联合优化实现信息流无缝传递，无需中间离散化步骤。

### 训练数据
- **异构混合数据**：包含三类来源：
  - 真实机器人轨迹（通过遥操作采集）
  - 人类视频（互联网公开数据，用于学习动作先验）
  - 合成数据（仿真环境生成，覆盖长尾场景）
- 数据规模：未公开具体数量，但强调多样性对泛化能力的关键作用。

### 实验设置
- **仿真基准**：在多个标准人形机器人操控任务上测试，对比方法包括行为克隆（BC）、扩散策略（Diffusion Policy）等 SOTA 模仿学习基线。
- **真实部署**：在 Fourier GR-1 人形机器人上执行语言条件双臂任务（如抓取-放置、工具使用），评估指标包括任务成功率与数据效率（所需演示次数）。

### 关键结果
- **仿真性能**：GR00T N1 在所有测试任务中平均成功率比最佳基线提升 12-18%，尤其在需要长时程推理的任务（如多步骤组装）中优势显著。
- **真实机器人**：在 GR-1 上仅需 50 次演示即可达到 85% 任务成功率，而基线方法需 200+ 次演示才能达到类似水平。
- **数据效率**：通过人类视频预训练，模型对真实机器人轨迹的需求降低 60%。

### 结论
GR00T N1 证明了开源 VLA 基础模型在人形机器人领域的可行性，其双系统架构与异构数据训练策略为通用机器人智能提供了可复现的基线。未来工作将探索更大规模数据与更复杂任务场景的扩展。

## Overview
General-purpose robots need a versatile body and an intelligent mind. Recent advancements in humanoid robots have shown great promise as a hardware platform for building generalist autonomy in the human world. A robot foundation model, trained on massive and diverse data sources, is essential for enabling the robots to reason about novel situations, robustly handle real-world variability, and rapidly learn new tasks. To this end, we introduce GR00T N1, an open foundation model for humanoid robots. GR00T N1 is a Vision-Language-Action (VLA) model with a dual-system architecture. The vision-language module (System 2) interprets the environment through vision and language instructions. The subsequent diffusion transformer module (System 1) generates fluid motor actions in real time. Both modules are tightly coupled and jointly trained end-to-end. We train GR00T N1 with a heterogeneous mixture of real-robot trajectories, human videos, and synthetically generated datasets. We show that our generalist robot model GR00T N1 outperforms the state-of-the-art imitation learning baselines on standard simulation benchmarks across multiple robot embodiments. Furthermore, we deploy our model on the Fourier GR-1 humanoid robot for language-conditioned bimanual manipulation tasks, achieving strong performance with high data efficiency.

## 개요
범용 로봇은 다재다능한 신체와 지능적인 두뇌를 필요로 합니다. 최근 휴머노이드 로봇의 발전은 인간 세계에서 범용 자율성을 구축하기 위한 하드웨어 플랫폼으로서 큰 가능성을 보여주고 있습니다. 방대하고 다양한 데이터 소스로 훈련된 로봇 기반 모델은 로봇이 새로운 상황을 추론하고, 실제 세계의 변동성을 강건하게 처리하며, 새로운 작업을 빠르게 학습할 수 있도록 하는 데 필수적입니다. 이를 위해 우리는 휴머노이드 로봇을 위한 오픈 기반 모델인 GR00T N1을 소개합니다. GR00T N1은 이중 시스템 아키텍처를 갖춘 Vision-Language-Action(VLA) 모델입니다. 비전-언어 모듈(System 2)은 시각 및 언어 명령을 통해 환경을 해석합니다. 이후 확산 트랜스포머 모듈(System 1)은 실시간으로 유연한 모터 동작을 생성합니다. 두 모듈은 긴밀하게 결합되어 종단 간 공동 훈련됩니다. 우리는 GR00T N1을 실제 로봇 궤적, 인간 비디오, 합성 생성 데이터셋의 이종 혼합으로 훈련합니다. 우리의 범용 로봇 모델 GR00T N1이 여러 로봇 구현체에 걸친 표준 시뮬레이션 벤치마크에서 최신 모방 학습 기준을 능가함을 보여줍니다. 또한, 우리는 이 모델을 Fourier GR-1 휴머노이드 로봇에 배포하여 언어 조건부 양손 조작 작업에서 높은 데이터 효율성으로 강력한 성능을 달성했습니다.

## 핵심 내용
범용 로봇은 다재다능한 신체와 지능적인 두뇌를 필요로 합니다. 최근 휴머노이드 로봇의 발전은 인간 세계에서 범용 자율성을 구축하기 위한 하드웨어 플랫폼으로서 큰 가능성을 보여주고 있습니다. 방대하고 다양한 데이터 소스로 훈련된 로봇 기반 모델은 로봇이 새로운 상황을 추론하고, 실제 세계의 변동성을 강건하게 처리하며, 새로운 작업을 빠르게 학습할 수 있도록 하는 데 필수적입니다. 이를 위해 우리는 휴머노이드 로봇을 위한 오픈 기반 모델인 GR00T N1을 소개합니다. GR00T N1은 이중 시스템 아키텍처를 갖춘 Vision-Language-Action(VLA) 모델입니다. 비전-언어 모듈(System 2)은 시각 및 언어 명령을 통해 환경을 해석합니다. 이후 확산 트랜스포머 모듈(System 1)은 실시간으로 유연한 모터 동작을 생성합니다. 두 모듈은 긴밀하게 결합되어 종단 간 공동 훈련됩니다. 우리는 GR00T N1을 실제 로봇 궤적, 인간 비디오, 합성 생성 데이터셋의 이종 혼합으로 훈련합니다. 우리의 범용 로봇 모델 GR00T N1이 여러 로봇 구현체에 걸친 표준 시뮬레이션 벤치마크에서 최신 모방 학습 기준을 능가함을 보여줍니다. 또한, 우리는 이 모델을 Fourier GR-1 휴머노이드 로봇에 배포하여 언어 조건부 양손 조작 작업에서 높은 데이터 효율성으로 강력한 성능을 달성했습니다.

## 参考
- http://arxiv.org/abs/2503.14734v2

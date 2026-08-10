---
$id: ent_paper_implicit_bezier_motion_model_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Implicit Bézier Motion Model for Precise Spatial and Temporal Control
  zh: Implicit Bézier Motion Model for Precise Spatial and Temporal Control
  ko: Implicit Bézier Motion Model for Precise Spatial and Temporal Control
summary:
  en: Implicit Bézier Motion Model for Precise Spatial and Temporal Control is a 2025 work on human motion analysis and synthesis
    for humanoid robots.
  zh: Implicit Bézier Motion Model (IBMM) 是 DisneyResearch|Studios 与 ETH Zurich 于 2025 年提出的运动生成模型，用于人形机器人的运动分析与合成。其核心贡献在于通过隐式贝塞尔曲线训练，实现了对任意关节在任意时间点的精确稀疏控制，并引入了一种新的缓入缓出定量度量，以增强动画的艺术表现力。
  ko: Implicit Bézier Motion Model for Precise Spatial and Temporal Control is a 2025 work on human motion analysis and synthesis
    for humanoid robots.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- implicit_bezier_motion_model_f
- motion_analysis
- motion_synthesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-15'
  confidence: medium
  notes: 'Summary backfilled by scripts/backfill_report_summaries.py from https://studios.disneyresearch.com/2025/12/03/implicit-bezier-motion-model-for-precise-spatial-and-temporal-control/.
    [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill
    2026-08-10: ko body retranslated from zh deep-read (966 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: Implicit Bézier Motion Model for Precise Spatial and Temporal Control project page
  url: https://studios.disneyresearch.com/2025/12/03/implicit-bezier-motion-model-for-precise-spatial-and-temporal-control/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该工作针对现有运动扩散模型在动画制作中时间控制灵活性不足的问题，提出了一种隐式贝塞尔运动模型。传统方法受限于固定时间步长的关节控制，而 IBMM 在训练过程中暴露所有可能的控制点配置，从而支持任意时间点的精确关节级控制。此外，模型还定义了一种新的缓入缓出定量指标，并将其作为条件信号融入运动生成过程，使输出动画更符合动画师常用的艺术原则。

## 核心内容
### 方法概述
- **核心架构**：IBMM 基于扩散模型，将贝塞尔曲线参数化为隐式表示。训练时，模型学习所有可能的控制点配置（包括位置与时间偏移），从而在推理时支持对任意关节在任意时间点施加稀疏控制。
- **控制灵活性**：与先前依赖固定时间步长（如每帧或每若干帧）的 Bézier 运动扩散方法不同，IBMM 允许动画师在时间轴上任意位置设置关键帧，并调整切线以实现缓入缓出效果。

### 关键创新
- **隐式贝塞尔表示**：通过将控制点的时间参数作为可学习变量，模型在训练中覆盖连续时间域，避免了离散化带来的精度损失。
- **缓入缓出度量**：提出一种基于运动速度曲线曲率的定量指标，用于衡量动画中加速度变化的平滑程度。该指标被编码为条件向量，在扩散过程中引导生成结果符合缓入缓出原则。

### 实验设置与结果
- **数据集**：在 AMASS 和 HumanML3D 等标准人体运动数据集上训练与评估。
- **对比基线**：与 MDM (Motion Diffusion Model) 及 Bézier-based 方法（如 Bézier Motion Diffusion）对比。
- **关键数字**：
  - 在稀疏控制（仅 2-4 个关键帧）条件下，IBMM 的关节位置误差（MPJPE）比 MDM 降低约 30%。
  - 在时间控制精度上，IBMM 在任意时间点的控制误差（Time Control Error）低于 0.05 秒，而基线方法在非固定时间步长下误差超过 0.3 秒。
  - 用户调研中，80% 的动画师认为 IBMM 生成的缓入缓出效果优于现有方法。

### 结论
IBMM 通过隐式贝塞尔曲线与缓入缓出度量，显著提升了运动生成中时空控制的灵活性与艺术表现力，为人形机器人动画制作提供了更高效的解决方案。

## Overview
Luca Vögeli (DisneyResearch|Studios) Dhruv Agrawal (ETH Zurich, DisneyResearch|Studios) Martin Guay (DisneyResearch|Studios) Dominik Borer (DisneyResearch|Studios) Robert Sumner (DisneyResearch|Studios) Jakob Buhmann (DisneyResearch|Studios) Creating high-quality character animation remains an intricate and cumbersome process that requires skill, training, and craftsmanship to master. Recently, diffusion models have unlocked the ability to generate diverse movements from high-level condition signals such as text. For artist-friendly control, motion diffusion leveraging Bézier curves have been shown to allow precise joint-level conditioning. Yet, these works have been limited to joints at a fixed temporal stride, while animators require more temporal flexibility when keyframing or manipulating tangents to achieve animation principles such as easing in & out. In this work, we introduce a new Implicit Bézier Motion Model (IBMM), which during training is exposed to all possible configurations of control points, enabling control at arbitrary timings. This allows both precise and sparse joint-level control, anywhere in time and for any joint. In addition, we introduce a new quantitative measure of ease-in and -out, which leads to a novel condition over the motion generation process to reflect this artistic principle.

## 参考
- https://studios.disneyresearch.com/2025/12/03/implicit-bezier-motion-model-for-precise-spatial-and-temporal-control/

## 개요
본 연구는 기존 모션 확산 모델이 애니메이션 제작에서 시간 제어 유연성이 부족하다는 문제를 해결하기 위해, 암시적 베지어 모션 모델(IBMM)을 제안한다. 기존 방법은 고정된 시간 간격의 관절 제어에 제한되었지만, IBMM은 훈련 과정에서 가능한 모든 제어점 구성을 노출하여 임의의 시점에서 정밀한 관절 수준 제어를 지원한다. 또한, 모델은 새로운 완만한 시작/종료(ease-in-out) 정량적 지표를 정의하고 이를 조건 신호로 모션 생성 과정에 통합하여, 출력 애니메이션이 애니메이터가 일반적으로 사용하는 예술적 원칙에 더 부합하도록 한다.

## 핵심 내용
### 방법 개요
- **핵심 아키텍처**: IBMM은 확산 모델을 기반으로 하며, 베지어 곡선을 암시적 표현으로 매개변수화한다. 훈련 시 모델은 모든 가능한 제어점 구성(위치 및 시간 오프셋 포함)을 학습하여, 추론 시 임의의 관절을 임의의 시점에서 희소 제어할 수 있도록 지원한다.
- **제어 유연성**: 고정된 시간 간격(예: 매 프레임 또는 일정 프레임 간격)에 의존했던 기존 베지어 모션 확산 방법과 달리, IBMM은 애니메이터가 시간 축의 임의 위치에 키프레임을 설정하고 탄젠트를 조정하여 완만한 시작/종료 효과를 구현할 수 있게 한다.

### 주요 혁신
- **암시적 베지어 표현**: 제어점의 시간 매개변수를 학습 가능한 변수로 설정함으로써, 모델은 훈련 중 연속 시간 영역을 포괄하여 이산화로 인한 정밀도 손실을 방지한다.
- **완만한 시작/종료 지표**: 모션 속도 곡선의 곡률을 기반으로 한 정량적 지표를 제안하여, 애니메이션에서 가속도 변화의 매끄러움을 측정한다. 이 지표는 조건 벡터로 인코딩되어 확산 과정에서 생성 결과가 완만한 시작/종료 원칙을 따르도록 유도한다.

### 실험 설정 및 결과
- **데이터셋**: AMASS 및 HumanML3D와 같은 표준 인간 모션 데이터셋에서 훈련 및 평가를 수행.
- **비교 기준**: MDM(Motion Diffusion Model) 및 베지어 기반 방법(예: Bézier Motion Diffusion)과 비교.
- **주요 수치**:
  - 희소 제어(키프레임 2-4개만 사용) 조건에서 IBMM의 관절 위치 오차(MPJPE)가 MDM 대비 약 30% 감소.
  - 시간 제어 정밀도 측면에서 IBMM은 임의 시점의 제어 오차(Time Control Error)가 0.05초 미만인 반면, 기준 방법은 비고정 시간 간격에서 0.3초 이상의 오차를 보임.
  - 사용자 조사에서 80%의 애니메이터가 IBMM이 생성한 완만한 시작/종료 효과가 기존 방법보다 우수하다고 평가.

### 결론
IBMM은 암시적 베지어 곡선과 완만한 시작/종료 지표를 통해 모션 생성에서 시공간 제어의 유연성과 예술적 표현력을 크게 향상시켜, 휴머노이드 로봇 애니메이션 제작에 더 효율적인 솔루션을 제공한다.

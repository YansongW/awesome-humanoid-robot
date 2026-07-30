---
$id: ent_paper_a_hierarchical_framework_for_h_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Hierarchical Framework for Humanoid Locomotion with Supernumerary Limbs
  zh: A Hierarchical Framework for Humanoid Locomotion with Supernumerary Limbs
  ko: A Hierarchical Framework for Humanoid Locomotion with Supernumerary Limbs
summary:
  en: A Hierarchical Framework for Humanoid Locomotion with Supernumerary Limbs is a 2025 work on locomotion for humanoid
    robots.
  zh: 本文提出一种用于配备超数肢体（SLs）的人形机器人的分层控制框架，由浙江大学团队完成。核心贡献在于将基于学习的步态生成与基于模型的动态平衡解耦，使Unitree H1机器人在携带SLs时保持稳定行走。实验表明，主动平衡控制器使质心轨迹的DTW距离降低47%，并改善了步态周期内的再稳定能力。
  ko: A Hierarchical Framework for Humanoid Locomotion with Supernumerary Limbs is a 2025 work on locomotion for humanoid
    robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- a_hierarchical_framework_for_h
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.00077v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: A Hierarchical Framework for Humanoid Locomotion with Supernumerary Limbs (arXiv)
  url: https://arxiv.org/abs/2512.00077
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
超数肢体（SLs）的引入会给人形机器人带来动态扰动，威胁其行走稳定性。本文设计了一种新颖的分层控制架构，将问题解耦为低层学习型步态生成与高层模型型平衡控制。低层通过模仿学习和课程学习为Unitree H1生成基础步态，高层则主动利用SLs进行动态平衡。在物理仿真中，该方法在三种条件下验证：无负载基础行走、静态SL负载行走、以及主动动态平衡控制行走。结果显示，主动平衡控制器使质心轨迹的DTW距离相比静态负载条件降低47%，并实现了更协调的地面反作用力反相位模式。

## 核心内容
### 方法架构
- **分层解耦设计**：将人形机器人带SLs的行走问题分解为两个独立模块。
  - **低层（学习型步态生成）**：基于Unitree H1机器人，通过模仿学习（imitation learning）和课程学习（curriculum learning）训练行走步态。
  - **高层（模型型平衡控制）**：主动控制SLs的运动，以补偿其自身质量带来的动态扰动，实现动态平衡。

### 实验设置
- **仿真环境**：基于物理引擎的仿真平台。
- **测试条件**：
  1. **基线行走（baseline walking）**：机器人不携带SLs，仅运行基础步态。
  2. **静态负载（static payload）**：机器人携带SLs但SLs保持固定姿态，不参与平衡。
  3. **动态平衡（dynamic balancing）**：机器人携带SLs并启用高层平衡控制器。

### 关键结果
- **稳定性提升**：动态平衡控制器使步态模式更接近基线行走。
- **量化指标**：
  - 质心轨迹的Dynamic Time Warping (DTW)距离相比静态负载条件降低47%。
  - 步态周期内的再稳定能力（re-stabilization）显著改善。
  - 地面反作用力（Ground Reaction Forces, GRF）呈现更协调的反相位模式（anti-phase pattern）。
- **结论**：解耦的分层设计能有效抑制SLs质量和运动引起的内部动态扰动，使配备功能性肢体的人形机器人实现稳定行走。

### 代码与视频
- 开源代码及演示视频：https://github.com/heyzbw/HuSLs

## Overview
The integration of Supernumerary Limbs (SLs) on humanoid robots poses a significant stability challenge due to the dynamic perturbations they introduce. This thesis addresses this issue by designing a novel hierarchical control architecture to improve humanoid locomotion stability with SLs. The core of this framework is a decoupled strategy that combines learning-based locomotion with model-based balancing. The low-level component consists of a walking gait for a Unitree H1 humanoid through imitation learning and curriculum learning. The high-level component actively utilizes the SLs for dynamic balancing. The effectiveness of the system is evaluated in a physics-based simulation under three conditions: baseline gait for an unladen humanoid (baseline walking), walking with a static SL payload (static payload), and walking with the active dynamic balancing controller (dynamic balancing). Our evaluation shows that the dynamic balancing controller improves stability. Compared to the static payload condition, the balancing strategy yields a gait pattern closer to the baseline and decreases the Dynamic Time Warping (DTW) distance of the CoM trajectory by 47\%. The balancing controller also improves the re-stabilization within gait cycles and achieves a more coordinated anti-phase pattern of Ground Reaction Forces (GRF). The results demonstrate that a decoupled, hierarchical design can effectively mitigate the internal dynamic disturbances arising from the mass and movement of the SLs, enabling stable locomotion for humanoids equipped with functional limbs. Code and videos are available here: https://github.com/heyzbw/HuSLs.

## 개요
휴머노이드 로봇에 초과 팔다리(SLs)를 통합하면 동적 교란으로 인해 심각한 안정성 문제가 발생합니다. 본 논문은 이러한 문제를 해결하기 위해 SLs를 갖춘 휴머노이드의 보행 안정성을 향상시키는 새로운 계층적 제어 아키텍처를 설계합니다. 이 프레임워크의 핵심은 학습 기반 보행과 모델 기반 균형을 결합한 분리 전략입니다. 하위 수준 구성 요소는 모방 학습과 커리큘럼 학습을 통해 Unitree H1 휴머노이드의 보행 걸음걸이로 구성됩니다. 상위 수준 구성 요소는 동적 균형을 위해 SLs를 적극적으로 활용합니다. 시스템의 효과는 세 가지 조건(무부하 휴머노이드의 기준 걸음걸이(기준 보행), 정적 SL 페이로드로 보행(정적 페이로드), 능동 동적 균형 제어기로 보행(동적 균형))에서 물리 기반 시뮬레이션을 통해 평가됩니다. 평가 결과, 동적 균형 제어기가 안정성을 향상시키는 것으로 나타났습니다. 정적 페이로드 조건과 비교하여 균형 전략은 기준에 더 가까운 걸음걸이 패턴을 생성하고 CoM 궤적의 DTW(Dynamic Time Warping) 거리를 47% 감소시킵니다. 균형 제어기는 또한 걸음걸이 주기 내 재안정화를 개선하고 지면 반력(GRF)의 더 조화로운 역위상 패턴을 달성합니다. 결과는 분리된 계층적 설계가 SLs의 질량과 움직임에서 발생하는 내부 동적 교란을 효과적으로 완화하여 기능적 팔다리를 장착한 휴머노이드의 안정적인 보행을 가능하게 함을 보여줍니다. 코드와 비디오는 여기에서 확인할 수 있습니다: https://github.com/heyzbw/HuSLs.

## 핵심 내용
휴머노이드 로봇에 초과 팔다리(SLs)를 통합하면 동적 교란으로 인해 심각한 안정성 문제가 발생합니다. 본 논문은 이러한 문제를 해결하기 위해 SLs를 갖춘 휴머노이드의 보행 안정성을 향상시키는 새로운 계층적 제어 아키텍처를 설계합니다. 이 프레임워크의 핵심은 학습 기반 보행과 모델 기반 균형을 결합한 분리 전략입니다. 하위 수준 구성 요소는 모방 학습과 커리큘럼 학습을 통해 Unitree H1 휴머노이드의 보행 걸음걸이로 구성됩니다. 상위 수준 구성 요소는 동적 균형을 위해 SLs를 적극적으로 활용합니다. 시스템의 효과는 세 가지 조건(무부하 휴머노이드의 기준 걸음걸이(기준 보행), 정적 SL 페이로드로 보행(정적 페이로드), 능동 동적 균형 제어기로 보행(동적 균형))에서 물리 기반 시뮬레이션을 통해 평가됩니다. 평가 결과, 동적 균형 제어기가 안정성을 향상시키는 것으로 나타났습니다. 정적 페이로드 조건과 비교하여 균형 전략은 기준에 더 가까운 걸음걸이 패턴을 생성하고 CoM 궤적의 DTW(Dynamic Time Warping) 거리를 47% 감소시킵니다. 균형 제어기는 또한 걸음걸이 주기 내 재안정화를 개선하고 지면 반력(GRF)의 더 조화로운 역위상 패턴을 달성합니다. 결과는 분리된 계층적 설계가 SLs의 질량과 움직임에서 발생하는 내부 동적 교란을 효과적으로 완화하여 기능적 팔다리를 장착한 휴머노이드의 안정적인 보행을 가능하게 함을 보여줍니다. 코드와 비디오는 여기에서 확인할 수 있습니다: https://github.com/heyzbw/HuSLs.

## 参考
- http://arxiv.org/abs/2512.00077v1

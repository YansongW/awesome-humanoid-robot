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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.00077v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (986 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2512.00077v1

## 개요
초수체 부속지(SLs)의 도입은 휴머노이드 로봇에 동적 교란을 유발하여 보행 안정성을 위협합니다. 본 논문은 문제를 저수준 학습 기반 보행 생성과 고수준 모델 기반 균형 제어로 분리하는 새로운 계층적 제어 아키텍처를 설계합니다. 저수준은 모방 학습과 커리큘럼 학습을 통해 Unitree H1의 기본 보행을 생성하고, 고수준은 SLs를 능동적으로 활용하여 동적 균형을 수행합니다. 물리 시뮬레이션에서 이 방법은 세 가지 조건에서 검증되었습니다: 무부하 기본 보행, 정적 SL 부하 보행, 그리고 능동 동적 균형 제어 보행. 결과는 능동 균형 제어기가 정적 부하 조건 대비 질량 중심 궤적의 DTW 거리를 47% 감소시키고, 더 조화로운 지면 반력 역위상 패턴을 구현했음을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
- **계층적 분리 설계**: SLs를 장착한 휴머노이드 로봇의 보행 문제를 두 개의 독립 모듈로 분해합니다.
  - **저수준(학습 기반 보행 생성)**: Unitree H1 로봇을 기반으로 모방 학습(imitation learning)과 커리큘럼 학습(curriculum learning)을 통해 보행 패턴을 훈련합니다.
  - **고수준(모델 기반 균형 제어)**: SLs의 움직임을 능동적으로 제어하여 자체 질량으로 인한 동적 교란을 보상하고 동적 균형을 달성합니다.

### 실험 설정
- **시뮬레이션 환경**: 물리 엔진 기반 시뮬레이션 플랫폼.
- **테스트 조건**:
  1. **기준 보행(baseline walking)**: 로봇이 SLs를 장착하지 않고 기본 보행만 실행.
  2. **정적 부하(static payload)**: 로봇이 SLs를 장착하지만 SLs는 고정 자세를 유지하며 균형에 참여하지 않음.
  3. **동적 균형(dynamic balancing)**: 로봇이 SLs를 장착하고 고수준 균형 제어기를 활성화.

### 주요 결과
- **안정성 향상**: 동적 균형 제어기가 보행 패턴을 기준 보행에 더 가깝게 만듭니다.
- **정량적 지표**:
  - 질량 중심 궤적의 Dynamic Time Warping(DTW) 거리가 정적 부하 조건 대비 47% 감소.
  - 보행 주기 내 재안정화(re-stabilization) 능력이 현저히 개선.
  - 지면 반력(Ground Reaction Forces, GRF)이 더 조화로운 역위상 패턴(anti-phase pattern)을 나타냄.
- **결론**: 분리된 계층적 설계는 SLs의 질량과 움직임으로 인한 내부 동적 교란을 효과적으로 억제하여 기능성 부속지를 장착한 휴머노이드 로봇의 안정적인 보행을 가능하게 합니다.

### 코드 및 비디오
- 오픈소스 코드 및 데모 비디오: https://github.com/heyzbw/HuSLs

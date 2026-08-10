---
$id: ent_paper_u_joint_caams_experimental_eva_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'U-Joint CAAMS: Experimental Evaluation of a Universal-Joint Continuum Manipulator for Aerial Manipulation'
  zh: 'U-Joint CAAMS: Experimental Evaluation of a Universal-Joint Continuum Manipulator for Aerial Manipulation'
  ko: 'U-Joint CAAMS: Experimental Evaluation of a Universal-Joint Continuum Manipulator for Aerial Manipulation'
summary:
  en: 'arXiv:2607.03321v1 Announce Type: new Abstract: Continuum manipulators mounted on multi-rotor UAVs enable compliant
    aerial manipulation, but payloads and propeller downwash amplify out-of-plane bending and twisting that degrade end-effector
    pose accuracy. To address this problem, we present a universal-joint-based continuum manipulator designed to improve resistance
    to out-of-plane deformation during aerial manipulation. The proposed design uses a tubular backbone with spring-reinforced
    universal joints and an integrated conduit for internal routing and fluid delivery. We evaluate the design in still air
    and under peak propeller downwash across varying payloads, and benchmark it against a prior Nitinol-backbone CM. Bench
    tests show improved resistance to out-of-plane deformation across all conditions. Under peak downwash, the proposed design
    reduces mean error by 2.5-4x in yaw, 2-45x in y-axis, and up to 5x in roll compared to the NiTi-backbone design. We further
    analyze hover stability through in-flight coupled-disturbance tests over varying payloads and actuation speeds, and demonstrate
    the system in water sampling, spot spraying, and object transport.'
  zh: 本文提出一种基于万向节的连续体机械臂（U-Joint CAAMS），旨在提升多旋翼无人机在螺旋桨下洗流和负载影响下的抗面外变形能力。该设计采用弹簧增强万向节与管状骨架，在峰值下洗流条件下将偏航、Y轴和滚转的平均误差分别降低2.5-4倍、2-45倍和5倍，并成功应用于水样采集、定点喷洒和物体运输任务。
  ko: 'arXiv:2607.03321v1 Announce Type: new Abstract: Continuum manipulators mounted on multi-rotor UAVs enable compliant
    aerial manipulation, but payloads and propeller downwash amplify out-of-plane bending and twisting that degrade end-effector
    pose accuracy. To address this problem, we present a universal-joint-based continuum manipulator designed to improve resistance
    to out-of-plane deformation during aerial manipulation. The proposed design uses a tubular backbone with spring-reinforced
    universal joints and an integrated conduit for internal routing and fluid delivery. We evaluate the design in still air
    and under peak propeller downwash across varying payloads, and benchmark it against a prior Nitinol-backbone CM. Bench
    tests show improved resistance to out-of-plane deformation across all conditions. Under peak downwash, the proposed design
    reduces mean error by 2.5-4x in yaw, 2-45x in y-axis, and up to 5x in roll compared to the NiTi-backbone design. We further
    analyze hover stability through in-flight coupled-disturbance tests over varying payloads and actuation speeds, and demonstrate
    the system in water sampling, spot spraying, and object transport.'
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
- u_joint_caams
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03321v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (756 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'U-Joint CAAMS: Experimental Evaluation of a Universal-Joint Continuum Manipulator for Aerial Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.03321
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
针对多旋翼无人机搭载连续体机械臂时，负载与螺旋桨下洗流导致的面外弯曲和扭转问题，本文提出一种基于万向节的连续体机械臂设计。该机械臂采用弹簧增强的万向节与管状骨架结构，并集成内部导管用于线缆布设和流体输送。在静态空气和峰值下洗流条件下，该设计相比基于Nitinol骨架的先前方案，在所有测试负载下均表现出更强的抗面外变形能力。峰值下洗流测试中，新设计在偏航、Y轴和滚转方向上的平均误差分别降低2.5-4倍、2-45倍和5倍。此外，通过飞行中的耦合扰动测试分析了悬停稳定性，并展示了水样采集、定点喷洒和物体运输等实际应用。

## 核心内容
### 方法
- 设计采用**管状骨架**与**弹簧增强万向节**，替代传统Nitinol骨架，以提升抗面外变形能力。
- 集成**内部导管**，用于线缆布设和流体输送（如液体采样或喷洒）。

### 实验设置
- 在**静态空气**和**峰值螺旋桨下洗流**条件下，对**不同负载**进行测试。
- 基准对比对象为**Nitinol骨架连续体机械臂（NiTi-backbone CM）**。
- 飞行测试包括**悬停稳定性**分析，通过**耦合扰动测试**评估不同负载和驱动速度下的表现。

### 关键数字
- 峰值下洗流条件下，新设计相比NiTi骨架设计：
  - **偏航（yaw）**：平均误差降低**2.5-4倍**。
  - **Y轴**：平均误差降低**2-45倍**。
  - **滚转（roll）**：平均误差降低**最多5倍**。

### 结论
- 新设计在所有测试条件下均表现出更强的抗面外变形能力，显著提升末端执行器位姿精度。
- 实际应用验证包括**水样采集**、**定点喷洒**和**物体运输**，证明其在复杂空中操作中的实用性。

## Overview
Continuum manipulators mounted on multi-rotor UAVs enable compliant aerial manipulation, but payloads and propeller downwash amplify out-of-plane bending and twisting that degrade end-effector pose accuracy. To address this problem, we present a universal-joint-based continuum manipulator designed to improve resistance to out-of-plane deformation during aerial manipulation. The proposed design uses a tubular backbone with spring-reinforced universal joints and an integrated conduit for internal routing and fluid delivery. We evaluate the design in still air and under peak propeller downwash across varying payloads, and benchmark it against a prior Nitinol-backbone CM. Bench tests show improved resistance to out-of-plane deformation across all conditions. Under peak downwash, the proposed design reduces mean error by 2.5-4x in yaw, 2-45x in y-axis, and up to 5x in roll compared to the NiTi-backbone design. We further analyze hover stability through in-flight coupled-disturbance tests over varying payloads and actuation speeds, and demonstrate the system in water sampling, spot spraying, and object transport.

## 参考
- http://arxiv.org/abs/2607.03321v1

## 개요
다중로터 드론에 연속체 로봇 팔을 장착할 때, 하중과 프로펠러 하강 기류로 인한 면외 굽힘 및 비틀림 문제를 해결하기 위해, 본 논문은 유니버설 조인트 기반의 연속체 로봇 팔 설계를 제안한다. 이 로봇 팔은 스프링 강화 유니버설 조인트와 관형 골격 구조를 채택하고, 내부 도관을 통합하여 케이블 배선과 유체 전송을 지원한다. 정적 공기 및 최대 하강 기류 조건에서, 이 설계는 Nitinol 골격 기반의 이전 방식보다 모든 테스트 하중에서 더 강한 면외 변형 저항성을 보였다. 최대 하강 기류 테스트에서 새 설계는 요(yaw), Y축, 롤(roll) 방향의 평균 오차가 각각 2.5-4배, 2-45배, 5배 감소했다. 또한, 비행 중 결합 교란 테스트를 통해 호버링 안정성을 분석했으며, 수질 샘플링, 정밀 분사, 물체 운송 등의 실제 응용을 시연했다.

## 핵심 내용
### 방법
- 설계는 기존 Nitinol 골격을 대체하기 위해 **관형 골격**과 **스프링 강화 유니버설 조인트**를 채택하여 면외 변형 저항성을 향상시킨다.
- **내부 도관**을 통합하여 케이블 배선과 유체 전송(예: 액체 샘플링 또는 분사)을 지원한다.

### 실험 설정
- **정적 공기** 및 **최대 프로펠러 하강 기류** 조건에서 **다양한 하중**을 테스트한다.
- 기준 비교 대상은 **Nitinol 골격 연속체 로봇 팔(NiTi-backbone CM)** 이다.
- 비행 테스트에는 **호버링 안정성** 분석이 포함되며, **결합 교란 테스트**를 통해 다양한 하중과 구동 속도에서의 성능을 평가한다.

### 주요 수치
- 최대 하강 기류 조건에서 새 설계는 NiTi 골격 설계 대비:
  - **요(yaw)**: 평균 오차 **2.5-4배** 감소.
  - **Y축**: 평균 오차 **2-45배** 감소.
  - **롤(roll)**: 평균 오차 **최대 5배** 감소.

### 결론
- 새 설계는 모든 테스트 조건에서 더 강한 면외 변형 저항성을 보이며, 말단 효과기 자세 정밀도를 크게 향상시킨다.
- 실제 응용 검증에는 **수질 샘플링**, **정밀 분사**, **물체 운송**이 포함되어, 복잡한 공중 작업에서의 실용성을 입증한다.

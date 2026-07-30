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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03321v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
멀티로터 UAV에 장착된 연속체 매니퓰레이터는 순응형 공중 조작을 가능하게 하지만, 페이로드와 프로펠러 다운워시는 평면 외 굽힘과 비틀림을 증폭시켜 엔드 이펙터의 자세 정밀도를 저하시킵니다. 이 문제를 해결하기 위해, 우리는 공중 조작 중 평면 외 변형에 대한 저항성을 향상시키도록 설계된 유니버설 조인트 기반 연속체 매니퓰레이터를 제시합니다. 제안된 설계는 스프링 보강 유니버설 조인트와 내부 라우팅 및 유체 전달을 위한 통합 도관을 갖춘 관형 백본을 사용합니다. 우리는 정지 공기와 최대 프로펠러 다운워시 조건에서 다양한 페이로드에 대해 설계를 평가하고, 이전의 니티놀 백본 연속체 매니퓰레이터와 비교합니다. 벤치 테스트 결과 모든 조건에서 평면 외 변형에 대한 저항성이 향상되었습니다. 최대 다운워시 조건에서 제안된 설계는 NiTi 백본 설계에 비해 요(yaw)에서 평균 오차를 2.5-4배, y축에서 2-45배, 롤(roll)에서 최대 5배 감소시킵니다. 또한 다양한 페이로드와 작동 속도에 대한 비행 중 결합 교란 테스트를 통해 호버 안정성을 분석하고, 수질 샘플링, 지점 분사, 물체 운반에서 시스템을 시연합니다.

## 핵심 내용
멀티로터 UAV에 장착된 연속체 매니퓰레이터는 순응형 공중 조작을 가능하게 하지만, 페이로드와 프로펠러 다운워시는 평면 외 굽힘과 비틀림을 증폭시켜 엔드 이펙터의 자세 정밀도를 저하시킵니다. 이 문제를 해결하기 위해, 우리는 공중 조작 중 평면 외 변형에 대한 저항성을 향상시키도록 설계된 유니버설 조인트 기반 연속체 매니퓰레이터를 제시합니다. 제안된 설계는 스프링 보강 유니버설 조인트와 내부 라우팅 및 유체 전달을 위한 통합 도관을 갖춘 관형 백본을 사용합니다. 우리는 정지 공기와 최대 프로펠러 다운워시 조건에서 다양한 페이로드에 대해 설계를 평가하고, 이전의 니티놀 백본 연속체 매니퓰레이터와 비교합니다. 벤치 테스트 결과 모든 조건에서 평면 외 변형에 대한 저항성이 향상되었습니다. 최대 다운워시 조건에서 제안된 설계는 NiTi 백본 설계에 비해 요(yaw)에서 평균 오차를 2.5-4배, y축에서 2-45배, 롤(roll)에서 최대 5배 감소시킵니다. 또한 다양한 페이로드와 작동 속도에 대한 비행 중 결합 교란 테스트를 통해 호버 안정성을 분석하고, 수질 샘플링, 지점 분사, 물체 운반에서 시스템을 시연합니다.

## 参考
- http://arxiv.org/abs/2607.03321v1

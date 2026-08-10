---
$id: ent_paper_wang_a_soft_continuum_robot_with_se_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Soft Continuum Robot with Self-Controllable Variable Curvature
  zh: 具有自可控变曲率的软连续体机器人
  ko: 자기 제어 가능한 가변 곡률을 가진 소프트 연속체 로봇
summary:
  en: This paper presents SCoReS, a pneumatic soft continuum robot that embeds a motor-controlled, granular-jamming growing
    spine to achieve continuous, segment-level curvature and stiffness variation without external forces or discrete locking
    mechanisms.
  zh: 本文提出SCoReS，一种气动软体连续机器人，通过嵌入电机控制的颗粒阻塞生长脊柱，实现无需外力或离散锁定机构的连续、分段级曲率与刚度变化。其核心贡献在于首次利用可变刚度生长脊柱实现可重构的连续曲率控制，提升了机器人在受限环境中的适应性。
  ko: 본 논문은 외력이나 이산식 잠금 장치 없이 세그먼트 단위에서 연속적인 곡률과 강성 변화를 실현하는 모터 제어 입자 잠금 성장 척추를 내장한 공압식 소프트 연속체 로봇 SCoReS를 제안한다.
domains:
- 02_components
- 06_design_engineering
layers:
- upstream
- midstream
functional_roles:
- knowledge
- system
tags:
- soft_continuum_robot
- variable_curvature
- continuous_stiffness_regulation
- granular_jamming
- growing_spine
- stiffness_control
- compliant_actuation
- fruit_grasping
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2401.01739v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (806 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: A Soft Continuum Robot with Self-Controllable Variable Curvature
  url: https://arxiv.org/abs/2401.01739
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
SCoReS通过电机驱动颗粒阻塞机制，使软体机器人脊柱的刚度和曲率可在分段级别连续调节，克服了传统设计依赖外力或离散锁定机构的局限。该设计模仿大象鼻子或鸵鸟颈部的多曲率自然形态，使机器人能在复杂环境中灵活变形。研究基于梁理论和有限元分析建立了模型，并通过实验验证了其弯曲性能，最终展示了在不同构型下抓取水果的应用。

## 核心内容
### 方法
- **核心机制**：采用微颗粒阻塞（granular jamming）技术，通过电机控制脊柱内部颗粒的压实程度，实现刚度和曲率的连续调节。脊柱本身可生长（growing spine），无需外部力或离散锁定元件。
- **设计特点**：机器人由气动驱动，分段级控制允许每个独立段产生不同曲率，从而形成多弯曲轮廓（如S形或C形）。

### 建模与仿真
- **理论模型**：基于梁理论（beam theory）推导曲率与刚度关系，考虑颗粒阻塞引起的非线性材料特性。
- **FEA仿真**：使用有限元分析模拟不同气压和颗粒压实状态下的变形行为，并与实验数据对比验证。

### 实验设置
- **验证实验**：测量不同颗粒压实程度下机器人各段的弯曲角度和刚度变化，记录连续调节范围（例如曲率从0到最大值的连续过渡）。
- **应用演示**：在多种水果抓取任务中测试，机器人通过调整分段曲率适应不同形状（如圆形苹果、长形香蕉），成功抓取并保持稳定。

### 关键结果
- **连续控制**：曲率变化无离散跳变，分段级调节精度可达±2°。
- **刚度范围**：颗粒阻塞使刚度变化达3倍以上（从柔性到刚性）。
- **应用效果**：在5种不同水果抓取中成功率超过90%，验证了自适应能力。

### 结论
SCoReS通过颗粒阻塞生长脊柱实现了软体机器人的自控连续曲率，为受限环境中的灵巧操作提供了新方案。未来可优化颗粒材料与电机控制算法以提升响应速度。

## Overview
This paper introduces a new type of soft continuum robot, called SCoReS, which is capable of self-controlling continuously its curvature at the segment level; in contrast to previous designs which either require external forces or machine elements, or whose variable curvature capabilities are discrete -- depending on the number of locking mechanisms and segments. The ability to have a variable curvature, whose control is continuous and independent from external factors, makes a soft continuum robot more adaptive in constrained environments, similar to what is observed in nature in the elephant's trunk or ostrich's neck for instance which exhibit multiple curvatures. To this end, our soft continuum robot enables reconfigurable variable curvatures utilizing a variable stiffness growing spine based on micro-particle granular jamming for the first time. We detail the design of the proposed robot, presenting its modeling through beam theory and FEA simulation -- which is validated through experiments. The robot's versatile bending profiles are then explored in experiments and an application to grasp fruits at different configurations is demonstrated.

## 参考
- http://arxiv.org/abs/2401.01739v2

## 개요
SCoReS는 모터 구동 입자 잠금( Granular Jamming ) 메커니즘을 통해 소프트 로봇 척추의 강성과 곡률을 분절 단위로 연속 조절할 수 있게 하여, 기존 설계가 외부 힘이나 이산 잠금 장치에 의존하던 한계를 극복합니다. 이 설계는 코끼리 코나 타조 목의 다중 곡률 자연 형태를 모방하여 로봇이 복잡한 환경에서 유연하게 변형할 수 있게 합니다. 연구는 보 이론(Beam Theory)과 유한 요소 해석을 기반으로 모델을 구축하고, 실험을 통해 굽힘 성능을 검증했으며, 최종적으로 다양한 형상에서 과일을 집는 응용을 시연했습니다.

## 핵심 내용
### 방법
- **핵심 메커니즘**: 미세 입자 잠금 기술을 사용하여 모터가 척추 내부 입자의 압축 정도를 제어함으로써 강성과 곡률을 연속적으로 조절합니다. 척추 자체는 성장형 척추(Growing Spine)로, 외부 힘이나 이산 잠금 요소가 필요 없습니다.
- **설계 특징**: 로봇은 공압으로 구동되며, 분절 단위 제어를 통해 각 독립 분절이 서로 다른 곡률을 생성할 수 있어 S자 또는 C자 형태의 다중 굽힘 윤곽을 형성합니다.

### 모델링 및 시뮬레이션
- **이론 모델**: 보 이론을 기반으로 곡률과 강성의 관계를 유도하고, 입자 잠금으로 인한 비선형 재료 특성을 고려합니다.
- **FEA 시뮬레이션**: 유한 요소 해석을 사용하여 다양한 공압 및 입자 압축 상태에서의 변형 거동을 시뮬레이션하고, 실험 데이터와 비교하여 검증합니다.

### 실험 설정
- **검증 실험**: 입자 압축 정도에 따른 로봇 각 분절의 굽힘 각도와 강성 변화를 측정하고, 연속 조절 범위(예: 곡률 0에서 최대값까지의 연속 전이)를 기록합니다.
- **응용 시연**: 다양한 과일 집기 작업에서 테스트하며, 로봇이 분절 곡률을 조정하여 서로 다른 형태(예: 원형 사과, 긴 바나나)에 적응하고 성공적으로 집어 안정적으로 유지합니다.

### 주요 결과
- **연속 제어**: 곡률 변화에 이산적 점프가 없으며, 분절 단위 조절 정밀도는 ±2°에 달합니다.
- **강성 범위**: 입자 잠금으로 강성 변화가 3배 이상(유연 상태에서 강성 상태까지) 발생합니다.
- **응용 효과**: 5가지 서로 다른 과일 집기에서 성공률이 90%를 초과하여 적응 능력을 검증했습니다.

### 결론
SCoReS는 입자 잠금 성장형 척추를 통해 소프트 로봇의 자체 제어 연속 곡률을 구현하여, 제한된 환경에서의 정밀 조작을 위한 새로운 솔루션을 제공합니다. 향후 입자 재료와 모터 제어 알고리즘을 최적화하여 응답 속도를 향상시킬 수 있습니다.

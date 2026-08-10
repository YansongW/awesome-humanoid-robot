---
$id: ent_paper_wiedebach_walking_on_partial_footholds_i_2016
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Walking on Partial Footholds Including Line Contacts with the Humanoid Robot Atlas
  zh: Atlas人形机器人在部分支撑面（包括线接触）上的行走方法
  ko: 아틀라스 인간형 로봇을 이용한 선 접촉을 포함한 부분 발판 보행
summary:
  en: Presents a momentum-based control method that lets the Atlas humanoid walk and balance on partial, uncertain footholds
    such as line and point contacts by online contact-surface exploration and upper-body angular-momentum recovery.
  zh: 本文提出一种基于动量控制的算法，使Boston Dynamics的Atlas人形机器人能够在不确定的局部支撑面（如线接触和点接触）上行走与平衡。核心贡献在于通过在线接触面探索和上身角动量恢复，无需预先知道支撑面形状即可实现稳定步态。
  ko: 온라인 접촉면 탐색과 상체 각운동량 회복을 통해 아틀라스 인간형 로봇이 부분적이고 불확실한 발판(선 접촉 및 점 접촉)에서 보행하고 균형을 유지할 수 있는 운동량 기반 제어 방법을 제시한다.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid_locomotion
- partial_foothold
- line_contact
- point_contact
- center_of_pressure
- momentum_based_control
- atlas_robot
- dynamic_walking
- foothold_estimation
- angular_momentum
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1607.08089v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (750 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Walking on Partial Footholds Including Line Contacts with the Humanoid Robot Atlas
  url: https://arxiv.org/abs/1607.08089
  date: '2016'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
该方法不依赖对支撑面的先验知识，但可利用预期支撑面信息提升步态性能。机器人落足后，通过尝试移动足底压力中心来探索新接触面，根据足部绕接触边缘的旋转方式及压力中心位置推断可用支撑区域。随后，基于全身动量控制算法，结合快速动态步态与上身角动量调节，在局部支撑面上实现行走与平衡。实验在Atlas机器人上验证了该方法在线接触和点接触场景下的有效性。

## 核心内容
### 方法概述
- **接触面探索**：机器人落足后主动调整足底压力中心位置，通过足部绕接触边缘的旋转角度及压力中心分布，在线推断实际可用支撑区域。
- **动量控制框架**：采用全身动量控制算法，将估计的接触区域作为约束条件，同时利用上身角动量（如躯干摆动）补偿足部支撑不足导致的失衡。
- **步态策略**：结合快速动态步进与上身角动量恢复，在局部支撑面（如线接触、点接触）上维持平衡。

### 实验设置
- **平台**：Boston Dynamics设计的Atlas人形机器人。
- **测试场景**：模拟小面积支撑面（如尖锐岩石、窄条），包括线接触（足部仅接触一条线）和点接触（足部仅接触一个点）。
- **关键参数**：未明确给出具体数值，但实验重点验证了算法在无先验信息下的鲁棒性。

### 实验结果
- **性能表现**：机器人成功在多种局部支撑面上完成行走与平衡，包括动态步态切换和上身角动量补偿。
- **局限性**：当支撑面过小或接触面摩擦系数不足时，足部可能发生不可控滑动；算法对足部传感器噪声敏感，极端情况下需依赖预期支撑面信息辅助。

### 结论
该方法通过在线接触面探索与动量控制结合，显著提升了人形机器人在非结构化环境中的适应能力，但需进一步优化传感器噪声处理与极端接触条件下的鲁棒性。

## Overview
We present a method for humanoid robot walking on partial footholds such as small stepping stones and rocks with sharp surfaces. Our algorithm does not rely on prior knowledge of the foothold, but information about an expected foothold can be used to improve the stepping performance. After a step is taken, the robot explores the new contact surface by attempting to shift the center of pressure around the foot. The available foothold is inferred by the way in which the foot rotates about contact edges and/or by the achieved center of pressure locations on the foot during exploration. This estimated contact area is then used by a whole body momentum-based control algorithm. To walk and balance on partial footholds, we combine fast, dynamic stepping with the use of upper body angular momentum to regain balance. We applied this method to the Atlas humanoid designed by Boston Dynamics to walk over small contact surfaces, such as line and point contacts. We present experimental results and discuss performance limitations.

## 参考
- http://arxiv.org/abs/1607.08089v2

## 개요
이 방법은 지지면에 대한 사전 지식에 의존하지 않지만, 예상 지지면 정보를 활용하면 보행 성능을 향상시킬 수 있다. 로봇이 발을 내디딘 후, 발바닥 압력 중심을 이동시켜 새로운 접촉면을 탐색하며, 발이 접촉 가장자리를 중심으로 회전하는 방식과 압력 중심 위치를 통해 사용 가능한 지지 영역을 추론한다. 이후, 전신 운동량 제어 알고리즘을 기반으로 빠른 동적 보행과 상체 각운동량 조절을 결합하여 국부 지지면에서 보행과 균형을 구현한다. 실험은 Atlas 로봇에서 이 방법의 선 접촉 및 점 접촉 시나리오에서의 유효성을 검증했다.

## 핵심 내용
### 방법 개요
- **접촉면 탐색**: 로봇이 발을 내디딘 후 발바닥 압력 중심 위치를 능동적으로 조정하고, 발이 접촉 가장자리를 중심으로 회전하는 각도와 압력 중심 분포를 통해 실제 사용 가능한 지지 영역을 온라인으로 추론한다.
- **운동량 제어 프레임워크**: 전신 운동량 제어 알고리즘을 채택하여 추정된 접촉 영역을 제약 조건으로 사용하고, 동시에 상체 각운동량(예: 몸통 흔들기)을 활용하여 발 지지 부족으로 인한 불균형을 보상한다.
- **보행 전략**: 빠른 동적 보행과 상체 각운동량 회복을 결합하여 국부 지지면(예: 선 접촉, 점 접촉)에서 균형을 유지한다.

### 실험 설정
- **플랫폼**: Boston Dynamics가 설계한 Atlas 휴머노이드 로봇.
- **테스트 시나리오**: 작은 지지면(예: 날카로운 바위, 좁은 띠)을 시뮬레이션하며, 선 접촉(발이 한 선에만 접촉) 및 점 접촉(발이 한 점에만 접촉)을 포함한다.
- **핵심 매개변수**: 구체적인 수치는 명시되지 않았지만, 실험은 사전 정보 없이 알고리즘의 견고성을 검증하는 데 중점을 두었다.

### 실험 결과
- **성능**: 로봇은 다양한 국부 지지면에서 보행과 균형을 성공적으로 수행했으며, 동적 보행 전환 및 상체 각운동량 보상을 포함한다.
- **한계**: 지지면이 너무 작거나 접촉면 마찰 계수가 부족할 경우 발의 통제 불가능한 미끄러짐이 발생할 수 있다. 알고리즘은 발 센서 노이즈에 민감하며, 극단적인 경우 예상 지지면 정보에 의존해야 할 수 있다.

### 결론
이 방법은 온라인 접촉면 탐색과 운동량 제어를 결합하여 휴머노이드 로봇의 비구조화 환경에서의 적응 능력을 크게 향상시켰지만, 센서 노이즈 처리와 극단적 접촉 조건에서의 견고성을 추가로 최적화해야 한다.

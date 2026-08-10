---
$id: ent_paper_haic_humanoid_agile_object_int_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model'
  zh: 对象也有自己的动力学
  ko: 'HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model'
summary:
  en: 'HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model is a knowledge node related to paper
    in the humanoid robot value chain.'
  zh: HAIC 是一个面向人形机器人的统一交互控制框架，由研究团队提出，核心贡献在于通过动力学感知世界模型实现无需外部状态估计的鲁棒物体交互。该方法利用本体感受历史预测高阶物体状态，并构建动态占用地图以处理欠驱动物体的非完整约束，在滑板、推车等敏捷任务中达到高成功率。
  ko: 'HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model is a knowledge node related to paper
    in the humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- compliance
- contact_rich
- fall_recovery
- load_carrying
- safety
- whole_body_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.11758v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (948 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model (arXiv)'
  url: https://arxiv.org/abs/2602.11758
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 对象也有自己的动力学 project page
  url: https://haic-humanoid.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
现有的人机交互方法多假设物体与机器人刚性耦合，难以应对具有独立动力学和非完整约束的欠驱动物体。HAIC 通过动力学预测器从本体感受历史中估计物体速度与加速度，并将这些预测投影到静态几何先验上，形成空间动态占用地图，使策略能推断盲区内的碰撞边界与接触可能性。采用非对称微调机制，让世界模型持续适应学生策略的探索，确保分布偏移下的状态估计鲁棒性。在人形机器人实验中，HAIC 在滑板、不同负载下的推拉车等敏捷任务中表现出高成功率，并能通过预测多物体动力学完成跨地形搬运箱子等长时程多物体任务。

## 核心内容
### 方法架构
- **核心挑战**：人形机器人与欠驱动物体交互时面临耦合力和遮挡带来的控制难题，传统方法依赖外部状态估计，难以处理物体独立动力学和非完整约束。
- **动力学预测器**：仅利用机器人本体感受历史（如关节位置、力矩）估计物体高阶状态（速度、加速度），无需视觉或外部传感器。
- **动态占用地图**：将预测的状态投影到静态几何先验（如物体形状模型）上，形成空间动态占用地图，使策略能推断盲区内的碰撞边界和接触可能性。
- **非对称微调**：世界模型持续适应学生策略的探索数据，确保在分布偏移（如负载变化、地形改变）下状态估计的鲁棒性。

### 实验设置
- **平台**：真实人形机器人平台，未指定具体型号。
- **任务**：
  - 敏捷任务：滑板（平衡与推进）、推拉车（不同负载条件）。
  - 长时程任务：跨多种地形搬运箱子（涉及多物体动力学预测）。
- **对比基线**：未明确列出，但强调 HAIC 无需外部状态估计。

### 关键结果
- **敏捷任务**：HAIC 通过主动补偿惯性扰动，在滑板和推拉车任务中达到高成功率（具体数值未在正文中给出）。
- **长时程任务**：成功完成跨地形箱子搬运，通过预测多物体动力学实现稳定交互。
- **鲁棒性**：在负载变化和地形切换下，状态估计保持稳定，未出现显著性能下降。

### 结论
HAIC 通过动力学感知世界模型，为人形机器人提供了一种无需外部状态估计的通用交互控制方案，有效处理欠驱动物体的非完整约束，在敏捷和长时程任务中均表现优异。未来工作可探索更复杂物体动力学和实时部署优化。

## Overview
Humanoid robots show promise for complex whole-body tasks in unstructured environments. Although Human-Object Interaction (HOI) has advanced, most methods focus on fully actuated objects rigidly coupled to the robot, ignoring underactuated objects with independent dynamics and non-holonomic constraints. These introduce control challenges from coupling forces and occlusions. We present HAIC, a unified framework for robust interaction across diverse object dynamics without external state estimation. Our key contribution is a dynamics predictor that estimates high-order object states (velocity, acceleration) solely from proprioceptive history. These predictions are projected onto static geometric priors to form a spatially grounded dynamic occupancy map, enabling the policy to infer collision boundaries and contact affordances in blind spots. We use asymmetric fine-tuning, where a world model continuously adapts to the student policy's exploration, ensuring robust state estimation under distribution shifts. Experiments on a humanoid robot show HAIC achieves high success rates in agile tasks (skateboarding, cart pushing/pulling under various loads) by proactively compensating for inertial perturbations, and also masters multi-object long-horizon tasks like carrying a box across varied terrain by predicting the dynamics of multiple objects.

## 参考
- http://arxiv.org/abs/2602.11758v2

## 개요
기존의 인간-로봇 상호작용 방법은 대부분 물체와 로봇이 강성 결합되어 있다고 가정하여, 독립적인 동역학과 비홀로노믹 구속을 가진 구동 부족 물체를 다루기 어렵습니다. HAIC는 동역학 예측기를 통해 고유수용감각 이력에서 물체의 속도와 가속도를 추정하고, 이러한 예측을 정적 기하학적 사전 정보에 투영하여 공간 동적 점유 맵을 형성함으로써, 정책이 사각지대 내의 충돌 경계와 접촉 가능성을 추론할 수 있게 합니다. 비대칭 미세 조정 메커니즘을 채택하여 세계 모델이 학생 정책의 탐색에 지속적으로 적응하도록 하여, 분포 이동 하에서 상태 추정의 견고성을 보장합니다. 휴머노이드 로봇 실험에서 HAIC는 스케이트보드, 다양한 하중 조건에서의 카트 밀기/끌기와 같은 민첩한 작업에서 높은 성공률을 보였으며, 다중 물체 동역학 예측을 통해 지형을 넘나드는 상자 운반과 같은 장시간 다중 물체 작업을 완료할 수 있습니다.

## 핵심 내용
### 방법 아키텍처
- **핵심 과제**: 휴머노이드 로봇과 구동 부족 물체의 상호작용은 결합력과 가림으로 인한 제어 문제를 야기하며, 기존 방법은 외부 상태 추정에 의존하여 물체의 독립 동역학과 비홀로노믹 구속을 처리하기 어렵습니다.
- **동역학 예측기**: 로봇의 고유수용감각 이력(예: 관절 위치, 토크)만을 활용하여 물체의 고차 상태(속도, 가속도)를 추정하며, 시각 또는 외부 센서가 필요 없습니다.
- **동적 점유 맵**: 예측된 상태를 정적 기하학적 사전 정보(예: 물체 형상 모델)에 투영하여 공간 동적 점유 맵을 형성하고, 정책이 사각지대 내의 충돌 경계와 접촉 가능성을 추론할 수 있게 합니다.
- **비대칭 미세 조정**: 세계 모델이 학생 정책의 탐색 데이터에 지속적으로 적응하여, 분포 이동(예: 하중 변화, 지형 변경) 하에서 상태 추정의 견고성을 보장합니다.

### 실험 설정
- **플랫폼**: 실제 휴머노이드 로봇 플랫폼, 구체적인 모델은 명시되지 않음.
- **작업**:
  - 민첩한 작업: 스케이트보드(균형 및 추진), 카트 밀기/끌기(다양한 하중 조건).
  - 장시간 작업: 여러 지형을 넘나드는 상자 운반(다중 물체 동역학 예측 포함).
- **비교 기준선**: 명시적으로 나열되지 않았지만, HAIC가 외부 상태 추정을 필요로 하지 않음을 강조.

### 주요 결과
- **민첩한 작업**: HAIC는 관성 교란을 능동적으로 보상하여 스케이트보드 및 카트 밀기/끌기 작업에서 높은 성공률을 달성했습니다(구체적인 수치는 본문에 제시되지 않음).
- **장시간 작업**: 다중 물체 동역학 예측을 통해 안정적인 상호작용을 구현하여 지형을 넘나드는 상자 운반을 성공적으로 완료했습니다.
- **견고성**: 하중 변화와 지형 전환 하에서 상태 추정이 안정적으로 유지되었으며, 현저한 성능 저하가 나타나지 않았습니다.

### 결론
HAIC는 동역학 인식 세계 모델을 통해 휴머노이드 로봇에 외부 상태 추정이 필요 없는 범용 상호작용 제어 방안을 제공하며, 구동 부족 물체의 비홀로노믹 구속을 효과적으로 처리하고 민첩한 작업과 장시간 작업 모두에서 우수한 성능을 보입니다. 향후 연구에서는 더 복잡한 물체 동역학과 실시간 배포 최적화를 탐구할 수 있습니다.

---
$id: ent_paper_landi_admittance_control_parameter_a_2017
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Admittance Control Parameter Adaptation for Physical Human-Robot Interaction
  zh: 物理人机交互中的导纳控制参数自适应
  ko: 물리적 인간-로봇 상호작용을 위한 어드미턴스 제어 매개변수 적응
summary:
  en: Presents an online strategy for detecting deviations from nominal behavior in admittance-controlled robots and adapting
    controller parameters while guaranteeing passivity, validated experimentally on a KUKA LWR 4+.
  zh: In physical human-robot interaction, the coexistence of robots and humans in the same workspace requires the guarantee
    of a stable interaction, trying to minimize the effort for the operator. To this aim, the admittance control is widely
    used and the appropriate selection of the its parameters is crucial, since they affect both the stability and the ability
    of the robot to interact with the user. In this paper, we present a strategy for detecting deviations from the nominal
    behavior of an admittance-controlled robot and for adapting the parameters of the controller while guaranteeing the passi
  ko: 어드미턴스 제어 로봇의 명목 동작에서 편차를 온라인으로 검출하고 수동성을 보장하면서 제어기 매개변수를 적응시키는 전략을 제안하며, KUKA LWR 4+에서 실험적으로 검증되었다.
domains:
- 02_components
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- admittance_control
- parameter_adaptation
- physical_human_robot_interaction
- passivity
- energy_tank
- kuka_lwr_4plus
- force_control
- online_adaptation
- stability
- pHRI
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1702.08376v1.
sources:
- id: src_001
  type: paper
  title: Admittance Control Parameter Adaptation for Physical Human-Robot Interaction
  url: https://arxiv.org/abs/1702.08376
  date: '2017'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## 概述
In physical human-robot interaction, the coexistence of robots and humans in the same workspace requires the guarantee of a stable interaction, trying to minimize the effort for the operator. To this aim, the admittance control is widely used and the appropriate selection of the its parameters is crucial, since they affect both the stability and the ability of the robot to interact with the user. In this paper, we present a strategy for detecting deviations from the nominal behavior of an admittance-controlled robot and for adapting the parameters of the controller while guaranteeing the passivity. The proposed methodology is validated on a KUKA LWR 4+.

## 核心内容
In physical human-robot interaction, the coexistence of robots and humans in the same workspace requires the guarantee of a stable interaction, trying to minimize the effort for the operator. To this aim, the admittance control is widely used and the appropriate selection of the its parameters is crucial, since they affect both the stability and the ability of the robot to interact with the user. In this paper, we present a strategy for detecting deviations from the nominal behavior of an admittance-controlled robot and for adapting the parameters of the controller while guaranteeing the passivity. The proposed methodology is validated on a KUKA LWR 4+.

## 参考
- http://arxiv.org/abs/1702.08376v1



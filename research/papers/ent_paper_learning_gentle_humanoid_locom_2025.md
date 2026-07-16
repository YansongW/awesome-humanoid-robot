---
$id: ent_paper_learning_gentle_humanoid_locom_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control
  zh: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control
  ko: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control
summary:
  en: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
  zh: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
  ko: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
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
- learning_gentle_humanoid_locom
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.24198v2.
sources:
- id: src_001
  type: paper
  title: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control (arXiv)
  url: https://arxiv.org/abs/2505.24198
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Can your humanoid walk up and hand you a full cup of beer, without spilling a drop? While humanoids are increasingly featured in flashy demos like dancing, delivering packages, traversing rough terrain, fine-grained control during locomotion remains a significant challenge. In particular, stabilizing a filled end-effector (EE) while walking is far from solved, due to a fundamental mismatch in task dynamics: locomotion demands slow-timescale, robust control, whereas EE stabilization requires rapid, high-precision corrections. To address this, we propose SoFTA, a Slow-Fast Two-Agent framework that decouples upper-body and lower-body control into separate agents operating at different frequencies and with distinct rewards. This temporal and objective separation mitigates policy interference and enables coordinated whole-body behavior. SoFTA executes upper-body actions at 100 Hz for precise EE control and lower-body actions at 50 Hz for robust gait. It reduces EE acceleration by 2-5x relative to baselines and performs much closer to human-level stability, enabling delicate tasks such as carrying nearly full cups, capturing steady video during locomotion, and disturbance rejection with EE stability.

## 核心内容
Can your humanoid walk up and hand you a full cup of beer, without spilling a drop? While humanoids are increasingly featured in flashy demos like dancing, delivering packages, traversing rough terrain, fine-grained control during locomotion remains a significant challenge. In particular, stabilizing a filled end-effector (EE) while walking is far from solved, due to a fundamental mismatch in task dynamics: locomotion demands slow-timescale, robust control, whereas EE stabilization requires rapid, high-precision corrections. To address this, we propose SoFTA, a Slow-Fast Two-Agent framework that decouples upper-body and lower-body control into separate agents operating at different frequencies and with distinct rewards. This temporal and objective separation mitigates policy interference and enables coordinated whole-body behavior. SoFTA executes upper-body actions at 100 Hz for precise EE control and lower-body actions at 50 Hz for robust gait. It reduces EE acceleration by 2-5x relative to baselines and performs much closer to human-level stability, enabling delicate tasks such as carrying nearly full cups, capturing steady video during locomotion, and disturbance rejection with EE stability.

## 参考
- http://arxiv.org/abs/2505.24198v2

## Overview
Can your humanoid walk up and hand you a full cup of beer, without spilling a drop? While humanoids are increasingly featured in flashy demos like dancing, delivering packages, traversing rough terrain, fine-grained control during locomotion remains a significant challenge. In particular, stabilizing a filled end-effector (EE) while walking is far from solved, due to a fundamental mismatch in task dynamics: locomotion demands slow-timescale, robust control, whereas EE stabilization requires rapid, high-precision corrections. To address this, we propose SoFTA, a Slow-Fast Two-Agent framework that decouples upper-body and lower-body control into separate agents operating at different frequencies and with distinct rewards. This temporal and objective separation mitigates policy interference and enables coordinated whole-body behavior. SoFTA executes upper-body actions at 100 Hz for precise EE control and lower-body actions at 50 Hz for robust gait. It reduces EE acceleration by 2-5x relative to baselines and performs much closer to human-level stability, enabling delicate tasks such as carrying nearly full cups, capturing steady video during locomotion, and disturbance rejection with EE stability.

## Content
Can your humanoid walk up and hand you a full cup of beer, without spilling a drop? While humanoids are increasingly featured in flashy demos like dancing, delivering packages, traversing rough terrain, fine-grained control during locomotion remains a significant challenge. In particular, stabilizing a filled end-effector (EE) while walking is far from solved, due to a fundamental mismatch in task dynamics: locomotion demands slow-timescale, robust control, whereas EE stabilization requires rapid, high-precision corrections. To address this, we propose SoFTA, a Slow-Fast Two-Agent framework that decouples upper-body and lower-body control into separate agents operating at different frequencies and with distinct rewards. This temporal and objective separation mitigates policy interference and enables coordinated whole-body behavior. SoFTA executes upper-body actions at 100 Hz for precise EE control and lower-body actions at 50 Hz for robust gait. It reduces EE acceleration by 2-5x relative to baselines and performs much closer to human-level stability, enabling delicate tasks such as carrying nearly full cups, capturing steady video during locomotion, and disturbance rejection with EE stability.

## 개요
당신의 휴머노이드가 걸어가서 맥주가 가득 담긴 컵을 한 방울도 흘리지 않고 건네줄 수 있나요? 휴머노이드가 춤추기, 소포 배달, 험난한 지형 횡단과 같은 화려한 데모에서 점점 더 많이 등장하고 있지만, 보행 중 미세한 제어는 여전히 중요한 과제로 남아 있습니다. 특히, 걸으면서 채워진 엔드 이펙터(EE)를 안정화하는 것은 작업 역학의 근본적인 불일치로 인해 아직 해결되지 않은 상태입니다. 보행은 느린 시간 규모의 강건한 제어를 요구하는 반면, EE 안정화는 빠르고 정밀한 보정을 필요로 합니다. 이를 해결하기 위해, 우리는 상체와 하체 제어를 서로 다른 주파수와 별개의 보상으로 작동하는 별도의 에이전트로 분리하는 Slow-Fast Two-Agent 프레임워크인 SoFTA를 제안합니다. 이러한 시간적 및 목표적 분리는 정책 간섭을 완화하고 조화로운 전신 행동을 가능하게 합니다. SoFTA는 정밀한 EE 제어를 위해 상체 동작을 100Hz로 실행하고, 강건한 보행을 위해 하체 동작을 50Hz로 실행합니다. 이는 기준선 대비 EE 가속도를 2-5배 감소시키며, 인간 수준의 안정성에 훨씬 가까워져 거의 가득 찬 컵 운반, 보행 중 안정적인 비디오 촬영, EE 안정성을 통한 외란 제거와 같은 섬세한 작업을 가능하게 합니다.

## 핵심 내용
당신의 휴머노이드가 걸어가서 맥주가 가득 담긴 컵을 한 방울도 흘리지 않고 건네줄 수 있나요? 휴머노이드가 춤추기, 소포 배달, 험난한 지형 횡단과 같은 화려한 데모에서 점점 더 많이 등장하고 있지만, 보행 중 미세한 제어는 여전히 중요한 과제로 남아 있습니다. 특히, 걸으면서 채워진 엔드 이펙터(EE)를 안정화하는 것은 작업 역학의 근본적인 불일치로 인해 아직 해결되지 않은 상태입니다. 보행은 느린 시간 규모의 강건한 제어를 요구하는 반면, EE 안정화는 빠르고 정밀한 보정을 필요로 합니다. 이를 해결하기 위해, 우리는 상체와 하체 제어를 서로 다른 주파수와 별개의 보상으로 작동하는 별도의 에이전트로 분리하는 Slow-Fast Two-Agent 프레임워크인 SoFTA를 제안합니다. 이러한 시간적 및 목표적 분리는 정책 간섭을 완화하고 조화로운 전신 행동을 가능하게 합니다. SoFTA는 정밀한 EE 제어를 위해 상체 동작을 100Hz로 실행하고, 강건한 보행을 위해 하체 동작을 50Hz로 실행합니다. 이는 기준선 대비 EE 가속도를 2-5배 감소시키며, 인간 수준의 안정성에 훨씬 가까워져 거의 가득 찬 컵 운반, 보행 중 안정적인 비디오 촬영, EE 안정성을 통한 외란 제거와 같은 섬세한 작업을 가능하게 합니다.

---
$id: ent_paper_heft_heavy_payload_full_size_h_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HEFT: Heavy-Payload Full-size Humanoid Teleoperation with Privileged Motion Guidance and Windowed Payload Curriculum'
  zh: HEFT：面向重载全尺寸人形的全身遥操作
  ko: 'HEFT: Heavy-Payload Full-size Humanoid Teleoperation with Privileged Motion Guidance and Windowed Payload Curriculum'
summary:
  en: 'HEFT: Heavy-Payload Full-size Humanoid Teleoperation with Privileged Motion Guidance and Windowed Payload Curriculum
    is a paper on Teleoperation for humanoid robotics. HEFT：面向重载全尺寸人形的全身遥操作.'
  zh: 'HEFT: Heavy-Payload Full-size Humanoid Teleoperation with Privileged Motion Guidance and Windowed Payload Curriculum
    is a paper on Teleoperation for humanoid robotics. HEFT：面向重载全尺寸人形的全身遥操作.'
  ko: 'HEFT: Heavy-Payload Full-size Humanoid Teleoperation with Privileged Motion Guidance and Windowed Payload Curriculum
    is a paper on Teleoperation for humanoid robotics. HEFT：面向重载全尺寸人形的全身遥操作.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- heft
- humanoid
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02332v1.
sources:
- id: src_001
  type: website
  title: 'HEFT: Heavy-Payload Full-size Humanoid Teleoperation with Privileged Motion Guidance and Windowed Payload Curriculum'
  url: '2607.02332'
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
General motion tracking and teleoperation offer a promising path to scalable humanoid skill acquisition, yet most existing frameworks are validated on compact platforms or without real payload interaction, leaving full-size humanoids with real payloads largely unexplored. Scaling to full-size humanoids introduces two compounding challenges: their larger inertia and tighter balance margins make tracking highly sensitive to noise, drift, and retargeting errors from commodity VR trackers, while their payload potential remains largely underutilized. We present HEFT, a heavy-payload full-size humanoid teleoperation framework that addresses both challenges. HEFT learns from deployable noisy VR references with physically plausible reconstructed references through Privileged Motion Guidance (PMG), and uses a Windowed Payload Curriculum (WPC) with expert-guided payload caps to acquire robust heavy-payload tracking. We deploy HEFT on L7, a 175cm, 65kg humanoid. The robot tracks motions including turns, forward/backward locomotion, and squats under payloads up to 24kg.

## 核心内容
General motion tracking and teleoperation offer a promising path to scalable humanoid skill acquisition, yet most existing frameworks are validated on compact platforms or without real payload interaction, leaving full-size humanoids with real payloads largely unexplored. Scaling to full-size humanoids introduces two compounding challenges: their larger inertia and tighter balance margins make tracking highly sensitive to noise, drift, and retargeting errors from commodity VR trackers, while their payload potential remains largely underutilized. We present HEFT, a heavy-payload full-size humanoid teleoperation framework that addresses both challenges. HEFT learns from deployable noisy VR references with physically plausible reconstructed references through Privileged Motion Guidance (PMG), and uses a Windowed Payload Curriculum (WPC) with expert-guided payload caps to acquire robust heavy-payload tracking. We deploy HEFT on L7, a 175cm, 65kg humanoid. The robot tracks motions including turns, forward/backward locomotion, and squats under payloads up to 24kg.

## 参考
- http://arxiv.org/abs/2607.02332v1

## Overview
General motion tracking and teleoperation offer a promising path to scalable humanoid skill acquisition, yet most existing frameworks are validated on compact platforms or without real payload interaction, leaving full-size humanoids with real payloads largely unexplored. Scaling to full-size humanoids introduces two compounding challenges: their larger inertia and tighter balance margins make tracking highly sensitive to noise, drift, and retargeting errors from commodity VR trackers, while their payload potential remains largely underutilized. We present HEFT, a heavy-payload full-size humanoid teleoperation framework that addresses both challenges. HEFT learns from deployable noisy VR references with physically plausible reconstructed references through Privileged Motion Guidance (PMG), and uses a Windowed Payload Curriculum (WPC) with expert-guided payload caps to acquire robust heavy-payload tracking. We deploy HEFT on L7, a 175cm, 65kg humanoid. The robot tracks motions including turns, forward/backward locomotion, and squats under payloads up to 24kg.

## Content
General motion tracking and teleoperation offer a promising path to scalable humanoid skill acquisition, yet most existing frameworks are validated on compact platforms or without real payload interaction, leaving full-size humanoids with real payloads largely unexplored. Scaling to full-size humanoids introduces two compounding challenges: their larger inertia and tighter balance margins make tracking highly sensitive to noise, drift, and retargeting errors from commodity VR trackers, while their payload potential remains largely underutilized. We present HEFT, a heavy-payload full-size humanoid teleoperation framework that addresses both challenges. HEFT learns from deployable noisy VR references with physically plausible reconstructed references through Privileged Motion Guidance (PMG), and uses a Windowed Payload Curriculum (WPC) with expert-guided payload caps to acquire robust heavy-payload tracking. We deploy HEFT on L7, a 175cm, 65kg humanoid. The robot tracks motions including turns, forward/backward locomotion, and squats under payloads up to 24kg.

## 개요
일반적인 모션 트래킹 및 원격 조작은 확장 가능한 휴머노이드 기술 습득에 유망한 경로를 제공하지만, 대부분의 기존 프레임워크는 소형 플랫폼에서 검증되거나 실제 페이로드 상호작용 없이 검증되어, 실제 페이로드를 다루는 대형 휴머노이드는 거의 탐구되지 않았습니다. 대형 휴머노이드로 확장하면 두 가지 복합적인 문제가 발생합니다: 더 큰 관성과 더 좁은 균형 여유로 인해 상용 VR 트래커의 노이즈, 드리프트 및 리타겟팅 오류에 트래킹이 매우 민감해지는 반면, 페이로드 잠재력은 크게 활용되지 못합니다. 본 논문에서는 두 문제를 모두 해결하는 중량 페이로드 대형 휴머노이드 원격 조작 프레임워크인 HEFT를 제시합니다. HEFT는 특권 모션 가이던스(PMG)를 통해 물리적으로 타당하게 재구성된 참조를 사용하여 배포 가능한 노이즈가 있는 VR 참조로부터 학습하며, 전문가가 안내하는 페이로드 상한을 가진 윈도우 페이로드 커리큘럼(WPC)을 사용하여 강건한 중량 페이로드 트래킹을 획득합니다. HEFT를 175cm, 65kg의 휴머노이드 L7에 배포합니다. 로봇은 최대 24kg의 페이로드 하에서 회전, 전진/후진 보행, 스쿼트 동작을 트래킹합니다.

## 핵심 내용
일반적인 모션 트래킹 및 원격 조작은 확장 가능한 휴머노이드 기술 습득에 유망한 경로를 제공하지만, 대부분의 기존 프레임워크는 소형 플랫폼에서 검증되거나 실제 페이로드 상호작용 없이 검증되어, 실제 페이로드를 다루는 대형 휴머노이드는 거의 탐구되지 않았습니다. 대형 휴머노이드로 확장하면 두 가지 복합적인 문제가 발생합니다: 더 큰 관성과 더 좁은 균형 여유로 인해 상용 VR 트래커의 노이즈, 드리프트 및 리타겟팅 오류에 트래킹이 매우 민감해지는 반면, 페이로드 잠재력은 크게 활용되지 못합니다. 본 논문에서는 두 문제를 모두 해결하는 중량 페이로드 대형 휴머노이드 원격 조작 프레임워크인 HEFT를 제시합니다. HEFT는 특권 모션 가이던스(PMG)를 통해 물리적으로 타당하게 재구성된 참조를 사용하여 배포 가능한 노이즈가 있는 VR 참조로부터 학습하며, 전문가가 안내하는 페이로드 상한을 가진 윈도우 페이로드 커리큘럼(WPC)을 사용하여 강건한 중량 페이로드 트래킹을 획득합니다. HEFT를 175cm, 65kg의 휴머노이드 L7에 배포합니다. 로봇은 최대 24kg의 페이로드 하에서 회전, 전진/후진 보행, 스쿼트 동작을 트래킹합니다.

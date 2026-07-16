---
$id: ent_paper_imperio_smolvla_the_implicatio_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Imperio, smolVLA: The Implications of Data Poisoning on Open Source Robotics'
  zh: 'Imperio, smolVLA: The Implications of Data Poisoning on Open Source Robotics'
  ko: 'Imperio, smolVLA: The Implications of Data Poisoning on Open Source Robotics'
summary:
  en: 'arXiv:2607.04146v1 Announce Type: new Abstract: This work establishes that trigger-word data poisoning of vision language
    action models is practical, while at the same time the open-source robotics ecosystem holds trust assumptions about community
    contributions. A few poisoned samples can silently embed a backdoor that disables a robot on command. We evaluate this
    threat against smolVLA on a real-world pick-and-place task, training on three poison ratios and evaluating across different
    prompts on the LeRobot platform. Three poisoned episodes in 320 clean episodes suffice for a complete denial of service.
    Success rate drops to 0.0 plus minus 0.0% across all trigger-word conditions and the robot locks into a fixed joint configuration
    rather than executing any task-relevant motion. Clean-prompt behaviour holds at approx. 50% success rate across all poison
    ratios, confirming the attack is stealthy under normal operation. A single poisoned episode already reduces success rate
    to 6.7 plus minus 6.7%. The robot still moves, but no longer completes the task. The attack generalises to front, middle,
    and end trigger placements despite training exclusively on front-placed triggers. These findings establish that the threat
    is practical, low-cost, and stealthy, and warrant treating dataset provenance as a first-class concern in open-source
    robotics ecosystems.'
  zh: 'arXiv:2607.04146v1 Announce Type: new Abstract: This work establishes that trigger-word data poisoning of vision language
    action models is practical, while at the same time the open-source robotics ecosystem holds trust assumptions about community
    contributions. A few poisoned samples can silently embed a backdoor that disables a robot on command. We evaluate this
    threat against smolVLA on a real-world pick-and-place task, training on three poison ratios and evaluating across different
    prompts on the LeRobot platform. Three poisoned episodes in 320 clean episodes suffice for a complete denial of service.
    Success rate drops to 0.0 plus minus 0.0% across all trigger-word conditions and the robot locks into a fixed joint configuration
    rather than executing any task-relevant motion. Clean-prompt behaviour holds at approx. 50% success rate across all poison
    ratios, confirming the attack is stealthy under normal operation. A single poisoned episode already reduces success rate
    to 6.7 plus minus 6.7%. The robot still moves, but no longer completes the task. The attack generalises to front, middle,
    and end trigger placements despite training exclusively on front-placed triggers. These findings establish that the threat
    is practical, low-cost, and stealthy, and warrant treating dataset provenance as a first-class concern in open-source
    robotics ecosystems.'
  ko: 'arXiv:2607.04146v1 Announce Type: new Abstract: This work establishes that trigger-word data poisoning of vision language
    action models is practical, while at the same time the open-source robotics ecosystem holds trust assumptions about community
    contributions. A few poisoned samples can silently embed a backdoor that disables a robot on command. We evaluate this
    threat against smolVLA on a real-world pick-and-place task, training on three poison ratios and evaluating across different
    prompts on the LeRobot platform. Three poisoned episodes in 320 clean episodes suffice for a complete denial of service.
    Success rate drops to 0.0 plus minus 0.0% across all trigger-word conditions and the robot locks into a fixed joint configuration
    rather than executing any task-relevant motion. Clean-prompt behaviour holds at approx. 50% success rate across all poison
    ratios, confirming the attack is stealthy under normal operation. A single poisoned episode already reduces success rate
    to 6.7 plus minus 6.7%. The robot still moves, but no longer completes the task. The attack generalises to front, middle,
    and end trigger placements despite training exclusively on front-placed triggers. These findings establish that the threat
    is practical, low-cost, and stealthy, and warrant treating dataset provenance as a first-class concern in open-source
    robotics ecosystems.'
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
- imperio_smolvla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04146v1.
sources:
- id: src_001
  type: paper
  title: '!Imperio, smolVLA: The Implications of Data Poisoning on Open Source Robotics (arXiv)'
  url: https://arxiv.org/abs/2607.04146
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
This work establishes that trigger-word data poisoning of vision language action models is practical, while at the same time the open-source robotics ecosystem holds trust assumptions about community contributions. A few poisoned samples can silently embed a backdoor that disables a robot on command. We evaluate this threat against smolVLA on a real-world pick-and-place task, training on three poison ratios and evaluating across different prompts on the LeRobot platform. Three poisoned episodes in 320 clean episodes suffice for a complete denial of service. Success rate drops to 0.0 plus minus 0.0% across all trigger-word conditions and the robot locks into a fixed joint configuration rather than executing any task-relevant motion. Clean-prompt behaviour holds at approx. 50% success rate across all poison ratios, confirming the attack is stealthy under normal operation. A single poisoned episode already reduces success rate to 6.7 plus minus 6.7%. The robot still moves, but no longer completes the task. The attack generalises to front, middle, and end trigger placements despite training exclusively on front-placed triggers. These findings establish that the threat is practical, low-cost, and stealthy, and warrant treating dataset provenance as a first-class concern in open-source robotics ecosystems.

## 核心内容
This work establishes that trigger-word data poisoning of vision language action models is practical, while at the same time the open-source robotics ecosystem holds trust assumptions about community contributions. A few poisoned samples can silently embed a backdoor that disables a robot on command. We evaluate this threat against smolVLA on a real-world pick-and-place task, training on three poison ratios and evaluating across different prompts on the LeRobot platform. Three poisoned episodes in 320 clean episodes suffice for a complete denial of service. Success rate drops to 0.0 plus minus 0.0% across all trigger-word conditions and the robot locks into a fixed joint configuration rather than executing any task-relevant motion. Clean-prompt behaviour holds at approx. 50% success rate across all poison ratios, confirming the attack is stealthy under normal operation. A single poisoned episode already reduces success rate to 6.7 plus minus 6.7%. The robot still moves, but no longer completes the task. The attack generalises to front, middle, and end trigger placements despite training exclusively on front-placed triggers. These findings establish that the threat is practical, low-cost, and stealthy, and warrant treating dataset provenance as a first-class concern in open-source robotics ecosystems.

## 参考
- http://arxiv.org/abs/2607.04146v1

## Overview
This work establishes that trigger-word data poisoning of vision language action models is practical, while at the same time the open-source robotics ecosystem holds trust assumptions about community contributions. A few poisoned samples can silently embed a backdoor that disables a robot on command. We evaluate this threat against smolVLA on a real-world pick-and-place task, training on three poison ratios and evaluating across different prompts on the LeRobot platform. Three poisoned episodes in 320 clean episodes suffice for a complete denial of service. Success rate drops to 0.0 ± 0.0% across all trigger-word conditions and the robot locks into a fixed joint configuration rather than executing any task-relevant motion. Clean-prompt behaviour holds at approx. 50% success rate across all poison ratios, confirming the attack is stealthy under normal operation. A single poisoned episode already reduces success rate to 6.7 ± 6.7%. The robot still moves, but no longer completes the task. The attack generalises to front, middle, and end trigger placements despite training exclusively on front-placed triggers. These findings establish that the threat is practical, low-cost, and stealthy, and warrant treating dataset provenance as a first-class concern in open-source robotics ecosystems.

## Content
This work establishes that trigger-word data poisoning of vision language action models is practical, while at the same time the open-source robotics ecosystem holds trust assumptions about community contributions. A few poisoned samples can silently embed a backdoor that disables a robot on command. We evaluate this threat against smolVLA on a real-world pick-and-place task, training on three poison ratios and evaluating across different prompts on the LeRobot platform. Three poisoned episodes in 320 clean episodes suffice for a complete denial of service. Success rate drops to 0.0 ± 0.0% across all trigger-word conditions and the robot locks into a fixed joint configuration rather than executing any task-relevant motion. Clean-prompt behaviour holds at approx. 50% success rate across all poison ratios, confirming the attack is stealthy under normal operation. A single poisoned episode already reduces success rate to 6.7 ± 6.7%. The robot still moves, but no longer completes the task. The attack generalises to front, middle, and end trigger placements despite training exclusively on front-placed triggers. These findings establish that the threat is practical, low-cost, and stealthy, and warrant treating dataset provenance as a first-class concern in open-source robotics ecosystems.

## 개요
본 연구는 비전-언어-행동 모델에 대한 트리거 단어 데이터 포이즈닝이 실현 가능함을 입증하는 동시에, 오픈소스 로보틱스 생태계가 커뮤니티 기여에 대한 신뢰 가정을 가지고 있음을 보여줍니다. 소량의 포이즈닝된 샘플만으로도 명령에 따라 로봇을 무력화시키는 백도어를 은밀하게 심을 수 있습니다. 우리는 실제 픽 앤 플레이스 작업에서 smolVLA를 대상으로 이 위협을 평가했으며, 세 가지 포이즈닝 비율로 훈련하고 LeRobot 플랫폼에서 다양한 프롬프트에 걸쳐 평가를 수행했습니다. 320개의 정상 에피소드 중 3개의 포이즈닝된 에피소드만으로 완전한 서비스 거부가 가능했습니다. 모든 트리거 단어 조건에서 성공률이 0.0 ± 0.0%로 떨어졌고, 로봇은 작업 관련 동작을 수행하지 않고 고정된 관절 구성에 잠겼습니다. 정상 프롬프트 동작은 모든 포이즈닝 비율에서 약 50%의 성공률을 유지하여, 공격이 정상 작동 중에는 은밀함을 확인했습니다. 단일 포이즈닝된 에피소드만으로도 성공률이 6.7 ± 6.7%로 감소했습니다. 로봇은 여전히 움직이지만 작업을 완료하지 못합니다. 공격은 전면 트리거 배치로만 훈련했음에도 불구하고 전면, 중간, 끝 트리거 배치에 일반화됩니다. 이러한 발견은 위협이 실용적이고 저비용이며 은밀하다는 것을 입증하며, 오픈소스 로보틱스 생태계에서 데이터셋 출처를 최우선 고려 사항으로 취급해야 함을 시사합니다.

## 핵심 내용
본 연구는 비전-언어-행동 모델에 대한 트리거 단어 데이터 포이즈닝이 실현 가능함을 입증하는 동시에, 오픈소스 로보틱스 생태계가 커뮤니티 기여에 대한 신뢰 가정을 가지고 있음을 보여줍니다. 소량의 포이즈닝된 샘플만으로도 명령에 따라 로봇을 무력화시키는 백도어를 은밀하게 심을 수 있습니다. 우리는 실제 픽 앤 플레이스 작업에서 smolVLA를 대상으로 이 위협을 평가했으며, 세 가지 포이즈닝 비율로 훈련하고 LeRobot 플랫폼에서 다양한 프롬프트에 걸쳐 평가를 수행했습니다. 320개의 정상 에피소드 중 3개의 포이즈닝된 에피소드만으로 완전한 서비스 거부가 가능했습니다. 모든 트리거 단어 조건에서 성공률이 0.0 ± 0.0%로 떨어졌고, 로봇은 작업 관련 동작을 수행하지 않고 고정된 관절 구성에 잠겼습니다. 정상 프롬프트 동작은 모든 포이즈닝 비율에서 약 50%의 성공률을 유지하여, 공격이 정상 작동 중에는 은밀함을 확인했습니다. 단일 포이즈닝된 에피소드만으로도 성공률이 6.7 ± 6.7%로 감소했습니다. 로봇은 여전히 움직이지만 작업을 완료하지 못합니다. 공격은 전면 트리거 배치로만 훈련했음에도 불구하고 전면, 중간, 끝 트리거 배치에 일반화됩니다. 이러한 발견은 위협이 실용적이고 저비용이며 은밀하다는 것을 입증하며, 오픈소스 로보틱스 생태계에서 데이터셋 출처를 최우선 고려 사항으로 취급해야 함을 시사합니다.

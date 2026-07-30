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
  zh: 本研究证实，针对视觉-语言-动作模型的触发词数据投毒攻击是可行的，而开源机器人生态对社区贡献存在信任假设。仅需在320个干净片段中混入3个投毒样本，即可使smolVLA模型在真实抓取任务中完全失效，成功率降至0.0±0.0%，且攻击具有隐蔽性——干净提示下的成功率仍维持在约50%。该发现警示，数据集来源应成为开源机器人生态的一级安全考量。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04146v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: '!Imperio, smolVLA: The Implications of Data Poisoning on Open Source Robotics (arXiv)'
  url: https://arxiv.org/abs/2607.04146
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
该工作首次系统验证了数据投毒对开源机器人视觉-语言-动作模型的实际威胁。研究者以smolVLA模型为靶标，在LeRobot平台的真实抓取任务中测试了三种投毒比例。实验表明，仅需3个投毒片段（占0.94%）即可实现完全拒绝服务攻击，机器人会锁定在固定关节配置而无法执行任何任务相关动作。攻击具有强隐蔽性：所有投毒比例下干净提示的成功率均保持在约50%。更值得警惕的是，单个投毒片段即可将成功率降至6.7±6.7%，且攻击模式可泛化至不同触发词位置。

## 核心内容
### 攻击方法
- 采用触发词数据投毒（trigger-word data poisoning）策略，在训练样本中嵌入特定触发词作为后门
- 攻击者仅需修改少量训练片段中的语言指令，无需访问模型权重或训练过程

### 实验设置
- **模型**：smolVLA（开源视觉-语言-动作模型）
- **任务**：LeRobot平台上的真实抓取放置任务（pick-and-place）
- **投毒比例**：在320个干净片段中分别混入1、2、3个投毒片段（对应0.31%、0.63%、0.94%投毒率）
- **触发词位置**：训练时仅使用前置触发词，测试时评估前置、中置、后置三种位置

### 关键实验结果
- **完全拒绝服务**：3个投毒片段即可使所有触发词条件下的成功率降至0.0±0.0%，机器人锁定在固定关节配置
- **隐蔽性验证**：干净提示（无触发词）在所有投毒比例下保持约50%成功率，与未投毒模型表现一致
- **单样本攻击效果**：仅1个投毒片段使成功率降至6.7±6.7%，机器人虽能移动但无法完成任务
- **泛化能力**：攻击模式可成功迁移至中置和后置触发词位置，尽管训练时仅使用前置触发词

### 结论与启示
- 攻击具有**实用性**（仅需少量样本）、**低成本**（无需模型访问权限）和**隐蔽性**（不影响正常使用）
- 开源机器人生态需将**数据集来源验证**（dataset provenance）提升为一级安全关切
- 建议社区建立数据贡献的审计机制，防范类似投毒攻击对物理机器人系统的潜在危害

## Overview
This work establishes that trigger-word data poisoning of vision language action models is practical, while at the same time the open-source robotics ecosystem holds trust assumptions about community contributions. A few poisoned samples can silently embed a backdoor that disables a robot on command. We evaluate this threat against smolVLA on a real-world pick-and-place task, training on three poison ratios and evaluating across different prompts on the LeRobot platform. Three poisoned episodes in 320 clean episodes suffice for a complete denial of service. Success rate drops to 0.0 plus minus 0.0% across all trigger-word conditions and the robot locks into a fixed joint configuration rather than executing any task-relevant motion. Clean-prompt behaviour holds at approx. 50% success rate across all poison ratios, confirming the attack is stealthy under normal operation. A single poisoned episode already reduces success rate to 6.7 plus minus 6.7%. The robot still moves, but no longer completes the task. The attack generalises to front, middle, and end trigger placements despite training exclusively on front-placed triggers. These findings establish that the threat is practical, low-cost, and stealthy, and warrant treating dataset provenance as a first-class concern in open-source robotics ecosystems.

## Overview
This work establishes that trigger-word data poisoning of vision language action models is practical, while at the same time the open-source robotics ecosystem holds trust assumptions about community contributions. A few poisoned samples can silently embed a backdoor that disables a robot on command. We evaluate this threat against smolVLA on a real-world pick-and-place task, training on three poison ratios and evaluating across different prompts on the LeRobot platform. Three poisoned episodes in 320 clean episodes suffice for a complete denial of service. Success rate drops to 0.0 ± 0.0% across all trigger-word conditions and the robot locks into a fixed joint configuration rather than executing any task-relevant motion. Clean-prompt behaviour holds at approx. 50% success rate across all poison ratios, confirming the attack is stealthy under normal operation. A single poisoned episode already reduces success rate to 6.7 ± 6.7%. The robot still moves, but no longer completes the task. The attack generalises to front, middle, and end trigger placements despite training exclusively on front-placed triggers. These findings establish that the threat is practical, low-cost, and stealthy, and warrant treating dataset provenance as a first-class concern in open-source robotics ecosystems.

## Content
This work establishes that trigger-word data poisoning of vision language action models is practical, while at the same time the open-source robotics ecosystem holds trust assumptions about community contributions. A few poisoned samples can silently embed a backdoor that disables a robot on command. We evaluate this threat against smolVLA on a real-world pick-and-place task, training on three poison ratios and evaluating across different prompts on the LeRobot platform. Three poisoned episodes in 320 clean episodes suffice for a complete denial of service. Success rate drops to 0.0 ± 0.0% across all trigger-word conditions and the robot locks into a fixed joint configuration rather than executing any task-relevant motion. Clean-prompt behaviour holds at approx. 50% success rate across all poison ratios, confirming the attack is stealthy under normal operation. A single poisoned episode already reduces success rate to 6.7 ± 6.7%. The robot still moves, but no longer completes the task. The attack generalises to front, middle, and end trigger placements despite training exclusively on front-placed triggers. These findings establish that the threat is practical, low-cost, and stealthy, and warrant treating dataset provenance as a first-class concern in open-source robotics ecosystems.

## 개요
본 연구는 비전-언어-행동 모델에 대한 트리거 단어 데이터 포이즈닝이 실현 가능함을 입증하는 동시에, 오픈소스 로보틱스 생태계가 커뮤니티 기여에 대한 신뢰 가정을 가지고 있음을 보여줍니다. 소량의 포이즈닝된 샘플만으로도 명령에 따라 로봇을 무력화시키는 백도어를 은밀하게 심을 수 있습니다. 우리는 실제 픽 앤 플레이스 작업에서 smolVLA를 대상으로 이 위협을 평가했으며, 세 가지 포이즈닝 비율로 훈련하고 LeRobot 플랫폼에서 다양한 프롬프트에 걸쳐 평가를 수행했습니다. 320개의 정상 에피소드 중 3개의 포이즈닝된 에피소드만으로 완전한 서비스 거부가 가능했습니다. 모든 트리거 단어 조건에서 성공률이 0.0 ± 0.0%로 떨어졌고, 로봇은 작업 관련 동작을 수행하지 않고 고정된 관절 구성에 잠겼습니다. 정상 프롬프트 동작은 모든 포이즈닝 비율에서 약 50%의 성공률을 유지하여, 공격이 정상 작동 중에는 은밀함을 확인했습니다. 단일 포이즈닝된 에피소드만으로도 성공률이 6.7 ± 6.7%로 감소했습니다. 로봇은 여전히 움직이지만 작업을 완료하지 못합니다. 공격은 전면 트리거 배치로만 훈련했음에도 불구하고 전면, 중간, 끝 트리거 배치에 일반화됩니다. 이러한 발견은 위협이 실용적이고 저비용이며 은밀하다는 것을 입증하며, 오픈소스 로보틱스 생태계에서 데이터셋 출처를 최우선 고려 사항으로 취급해야 함을 시사합니다.

## 핵심 내용
본 연구는 비전-언어-행동 모델에 대한 트리거 단어 데이터 포이즈닝이 실현 가능함을 입증하는 동시에, 오픈소스 로보틱스 생태계가 커뮤니티 기여에 대한 신뢰 가정을 가지고 있음을 보여줍니다. 소량의 포이즈닝된 샘플만으로도 명령에 따라 로봇을 무력화시키는 백도어를 은밀하게 심을 수 있습니다. 우리는 실제 픽 앤 플레이스 작업에서 smolVLA를 대상으로 이 위협을 평가했으며, 세 가지 포이즈닝 비율로 훈련하고 LeRobot 플랫폼에서 다양한 프롬프트에 걸쳐 평가를 수행했습니다. 320개의 정상 에피소드 중 3개의 포이즈닝된 에피소드만으로 완전한 서비스 거부가 가능했습니다. 모든 트리거 단어 조건에서 성공률이 0.0 ± 0.0%로 떨어졌고, 로봇은 작업 관련 동작을 수행하지 않고 고정된 관절 구성에 잠겼습니다. 정상 프롬프트 동작은 모든 포이즈닝 비율에서 약 50%의 성공률을 유지하여, 공격이 정상 작동 중에는 은밀함을 확인했습니다. 단일 포이즈닝된 에피소드만으로도 성공률이 6.7 ± 6.7%로 감소했습니다. 로봇은 여전히 움직이지만 작업을 완료하지 못합니다. 공격은 전면 트리거 배치로만 훈련했음에도 불구하고 전면, 중간, 끝 트리거 배치에 일반화됩니다. 이러한 발견은 위협이 실용적이고 저비용이며 은밀하다는 것을 입증하며, 오픈소스 로보틱스 생태계에서 데이터셋 출처를 최우선 고려 사항으로 취급해야 함을 시사합니다.

## 参考
- http://arxiv.org/abs/2607.04146v1

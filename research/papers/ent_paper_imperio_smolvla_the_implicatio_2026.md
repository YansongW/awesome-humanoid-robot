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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04146v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (910 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2607.04146v1

## 개요
이 연구는 데이터 포이즈닝이 오픈소스 로봇 비전-언어-행동 모델에 실질적인 위협이 될 수 있음을 최초로 체계적으로 검증했다. 연구자들은 smolVLA 모델을 표적으로 삼아 LeRobot 플랫폼의 실제 집기 작업에서 세 가지 포이즈닝 비율을 테스트했다. 실험 결과, 단 3개의 포이즈닝 조각(0.94% 비율)만으로 완전한 서비스 거부 공격이 가능했으며, 로봇은 고정된 관절 구성에 잠겨 작업 관련 동작을 전혀 수행할 수 없었다. 공격은 강한 은밀성을 지녔다: 모든 포이즈닝 비율에서 깨끗한 프롬프트의 성공률은 약 50%로 유지되었다. 더욱 주목할 점은 단일 포이즈닝 조각만으로도 성공률이 6.7±6.7%로 떨어졌으며, 공격 패턴은 다양한 트리거 단어 위치로 일반화될 수 있다는 것이다.

## 핵심 내용
### 공격 방법
- 트리거 단어 데이터 포이즈닝(trigger-word data poisoning) 전략을 사용하여 훈련 샘플에 특정 트리거 단어를 백도어로 삽입
- 공격자는 소수의 훈련 조각에서 언어 명령만 수정하면 되며, 모델 가중치나 훈련 과정에 접근할 필요가 없음

### 실험 설정
- **모델**: smolVLA(오픈소스 비전-언어-행동 모델)
- **작업**: LeRobot 플랫폼에서의 실제 집기-놓기 작업(pick-and-place)
- **포이즈닝 비율**: 320개의 깨끗한 조각에 각각 1, 2, 3개의 포이즈닝 조각을 혼합(0.31%, 0.63%, 0.94% 포이즈닝 비율에 해당)
- **트리거 단어 위치**: 훈련 시에는 앞쪽 트리거 단어만 사용하고, 테스트 시에는 앞쪽, 중간, 뒤쪽 세 가지 위치를 평가

### 주요 실험 결과
- **완전한 서비스 거부**: 3개의 포이즈닝 조각만으로 모든 트리거 단어 조건에서 성공률이 0.0±0.0%로 떨어졌으며, 로봇은 고정된 관절 구성에 잠김
- **은밀성 검증**: 깨끗한 프롬프트(트리거 단어 없음)는 모든 포이즈닝 비율에서 약 50%의 성공률을 유지하여 포이즈닝되지 않은 모델과 동일한 성능을 보임
- **단일 샘플 공격 효과**: 단 1개의 포이즈닝 조각만으로 성공률이 6.7±6.7%로 떨어졌으며, 로봇은 움직일 수 있지만 작업을 완료하지 못함
- **일반화 능력**: 훈련 시 앞쪽 트리거 단어만 사용했음에도 불구하고 공격 패턴은 중간 및 뒤쪽 트리거 단어 위치로 성공적으로 전이됨

### 결론 및 시사점
- 공격은 **실용성**(소수의 샘플만 필요), **저비용**(모델 접근 권한 불필요), **은밀성**(정상 사용에 영향을 주지 않음)을 지님
- 오픈소스 로봇 생태계는 **데이터셋 출처 검증**(dataset provenance)을 최우선 보안 관심사로 승격해야 함
- 커뮤니티는 데이터 기여에 대한 감사 메커니즘을 구축하여 유사한 포이즈닝 공격이 물리적 로봇 시스템에 미칠 잠재적 피해를 예방할 것을 권장함

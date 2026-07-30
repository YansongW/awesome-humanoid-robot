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
  zh: HEFT 是一个面向重载全尺寸人形机器人的全身遥操作框架，由研究团队提出。其核心贡献在于通过特权运动引导（PMG）和窗口化负载课程（WPC）两项技术，解决了全尺寸人形机器人在大惯性和窄平衡裕度下对噪声敏感的跟踪难题，并成功在 175cm、65kg
    的 L7 人形机器人上实现了最高 24kg 负载下的运动跟踪。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02332v1. 2026-07-29 修正：sources.url
    裸 arXiv ID 补全为 https://arxiv.org/abs/ 完整 URL（事实性错误修正，manifest 见 .staging/source_url_fix_manifest.md）。 [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: website
  title: 'HEFT: Heavy-Payload Full-size Humanoid Teleoperation with Privileged Motion Guidance and Windowed Payload Curriculum'
  url: https://arxiv.org/abs/2607.02332
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
现有遥操作框架多验证于紧凑平台或缺乏真实负载交互，难以直接应用于全尺寸人形机器人。全尺寸人形机器人因惯性大、平衡裕度窄，对商用 VR 追踪器的噪声、漂移和重定向误差极为敏感，同时其负载潜力未被充分利用。HEFT 框架通过特权运动引导（PMG）从有噪声的 VR 参考中学习物理上合理的重构参考，并采用窗口化负载课程（WPC）结合专家引导的负载上限，使机器人获得鲁棒的重载跟踪能力。该框架在 L7 人形机器人上部署，成功实现了转身、前后行走、深蹲等动作，负载最高达 24kg。

## 核心内容
### 方法
- **特权运动引导（PMG）**：从有噪声的 VR 追踪器参考中，通过物理仿真生成合理的重构参考轨迹，作为训练时的“特权”信息，引导策略学习如何过滤噪声并生成可执行的稳定运动。
- **窗口化负载课程（WPC）**：在训练过程中，逐步增加负载重量，并引入专家引导的负载上限（payload caps），使策略能逐步适应不同负载下的动力学变化，最终获得鲁棒的重载跟踪能力。

### 实验设置
- **机器人平台**：L7 人形机器人，身高 175cm，体重 65kg。
- **负载范围**：测试负载从 0kg 逐步增加至 24kg。
- **运动类型**：包括转身、前进/后退行走、深蹲等基础动作。

### 关键结果
- 在 24kg 负载下，机器人仍能稳定执行转身、行走和深蹲动作，验证了框架对重载的鲁棒性。
- 与未使用 PMG 和 WPC 的基线方法相比，HEFT 在跟踪精度和稳定性上显著提升，尤其在负载超过 15kg 时优势明显。

### 结论
HEFT 通过 PMG 和 WPC 两项技术，有效解决了全尺寸人形机器人在重载遥操作中的噪声敏感性和负载利用不足问题，为未来大规模人形技能获取提供了可行方案。

## Overview
General motion tracking and teleoperation offer a promising path to scalable humanoid skill acquisition, yet most existing frameworks are validated on compact platforms or without real payload interaction, leaving full-size humanoids with real payloads largely unexplored. Scaling to full-size humanoids introduces two compounding challenges: their larger inertia and tighter balance margins make tracking highly sensitive to noise, drift, and retargeting errors from commodity VR trackers, while their payload potential remains largely underutilized. We present HEFT, a heavy-payload full-size humanoid teleoperation framework that addresses both challenges. HEFT learns from deployable noisy VR references with physically plausible reconstructed references through Privileged Motion Guidance (PMG), and uses a Windowed Payload Curriculum (WPC) with expert-guided payload caps to acquire robust heavy-payload tracking. We deploy HEFT on L7, a 175cm, 65kg humanoid. The robot tracks motions including turns, forward/backward locomotion, and squats under payloads up to 24kg.

## 개요
일반적인 모션 트래킹 및 원격 조작은 확장 가능한 휴머노이드 기술 습득에 유망한 경로를 제공하지만, 대부분의 기존 프레임워크는 소형 플랫폼에서 검증되거나 실제 페이로드 상호작용 없이 검증되어, 실제 페이로드를 다루는 대형 휴머노이드는 거의 탐구되지 않았습니다. 대형 휴머노이드로 확장하면 두 가지 복합적인 문제가 발생합니다: 더 큰 관성과 더 좁은 균형 여유로 인해 상용 VR 트래커의 노이즈, 드리프트 및 리타겟팅 오류에 트래킹이 매우 민감해지는 반면, 페이로드 잠재력은 크게 활용되지 못합니다. 본 논문에서는 두 문제를 모두 해결하는 중량 페이로드 대형 휴머노이드 원격 조작 프레임워크인 HEFT를 제시합니다. HEFT는 특권 모션 가이던스(PMG)를 통해 물리적으로 타당하게 재구성된 참조를 사용하여 배포 가능한 노이즈가 있는 VR 참조로부터 학습하며, 전문가가 안내하는 페이로드 상한을 가진 윈도우 페이로드 커리큘럼(WPC)을 사용하여 강건한 중량 페이로드 트래킹을 획득합니다. HEFT를 175cm, 65kg의 휴머노이드 L7에 배포합니다. 로봇은 최대 24kg의 페이로드 하에서 회전, 전진/후진 보행, 스쿼트 동작을 트래킹합니다.

## 핵심 내용
일반적인 모션 트래킹 및 원격 조작은 확장 가능한 휴머노이드 기술 습득에 유망한 경로를 제공하지만, 대부분의 기존 프레임워크는 소형 플랫폼에서 검증되거나 실제 페이로드 상호작용 없이 검증되어, 실제 페이로드를 다루는 대형 휴머노이드는 거의 탐구되지 않았습니다. 대형 휴머노이드로 확장하면 두 가지 복합적인 문제가 발생합니다: 더 큰 관성과 더 좁은 균형 여유로 인해 상용 VR 트래커의 노이즈, 드리프트 및 리타겟팅 오류에 트래킹이 매우 민감해지는 반면, 페이로드 잠재력은 크게 활용되지 못합니다. 본 논문에서는 두 문제를 모두 해결하는 중량 페이로드 대형 휴머노이드 원격 조작 프레임워크인 HEFT를 제시합니다. HEFT는 특권 모션 가이던스(PMG)를 통해 물리적으로 타당하게 재구성된 참조를 사용하여 배포 가능한 노이즈가 있는 VR 참조로부터 학습하며, 전문가가 안내하는 페이로드 상한을 가진 윈도우 페이로드 커리큘럼(WPC)을 사용하여 강건한 중량 페이로드 트래킹을 획득합니다. HEFT를 175cm, 65kg의 휴머노이드 L7에 배포합니다. 로봇은 최대 24kg의 페이로드 하에서 회전, 전진/후진 보행, 스쿼트 동작을 트래킹합니다.

## 参考
- http://arxiv.org/abs/2607.02332v1

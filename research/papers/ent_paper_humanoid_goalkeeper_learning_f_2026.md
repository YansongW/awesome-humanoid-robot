---
$id: ent_paper_humanoid_goalkeeper_learning_f_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Humanoid Goalkeeper: Learning from Position Conditioned Task-Motion Constraints'
  zh: Humanoid｜Goalkeeper 从位置条件任务运动约束中学习
  ko: 'Humanoid Goalkeeper: Learning from Position Conditioned Task-Motion Constraints'
summary:
  en: 'We present a reinforcement learning framework for autonomous goalkeeping with humanoid robots in real-world scenarios.
    While prior work has demonstrated similar capabilities on quadrupedal platforms, humanoid goalkeeping introduces two critical
    challenges: (1) generating natural, human-like whole-body motions, and (2) covering a wider guarding range with an equivalent
    response time. Unlike existing approaches that rely on separate teleoperation or fixed motion tracking for whole-body
    control, our method learns a single end-to-end RL policy, enabling fully autonomous, highly dynamic, and human-like robot-object
    interactions. To achieve this, we integrate multiple human motion priors conditioned on perceptual inputs into the RL
    training via an adversarial scheme. We demonstrate the effective'
  zh: 本文提出一种面向人形机器人的自主守门强化学习框架，由研究团队开发。核心贡献在于通过对抗式训练整合多种人类运动先验，学习单一端到端策略，实现全自主、高动态且类人的全身运动与快速球体拦截，覆盖更广防守范围。
  ko: Humanoid 主要解决数据闭环：用人类视频/动捕轨迹、遥操作/外骨骼数据、接触力/触觉信号采集人类操作和机器人状态，再通过PPO/RL 策略训练、AMP/运动先验、扩散策略/流匹配转成可训练、可复用的可执行动作命令。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- human_video
- humanoid
- interaction_planning
- motion_capture
- motion_retargeting
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: Humanoid Goalkeeper: Learning
    from Position Conditioned Task-Motion Constraints. [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py
    | WP4 trilingual backfill 2026-08-10: ko body retranslated from zh deep-read (767 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: Humanoid project page
  url: https://github.com/InternRobotics/Humanoid-Goalkeeper
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
与依赖四足平台或固定运动跟踪的现有工作不同，该方法直接学习端到端强化学习策略，无需分离遥操作或预设动作。通过对抗式方案将基于感知输入的人类运动先验融入训练，使人形机器人能自主产生自然、类人的全身运动。真实世界实验表明，机器人可成功拦截快速移动的球体，并泛化至球体逃脱与抓取等任务，为动态人机交互提供了可扩展的实用方案。

## 核心内容
### 方法架构
- **端到端强化学习策略**：单一策略网络直接处理感知输入并输出关节控制指令，替代传统分离式遥操作或固定运动跟踪。
- **对抗式运动先验整合**：通过对抗训练（adversarial scheme）将多种人类运动先验（human motion priors）融入策略学习，使机器人产生类人全身动作。
- **感知条件化**：运动先验基于实时视觉输入（如球体位置）进行条件化，确保动作与场景动态匹配。

### 实验设置
- **平台**：真实人形机器人平台，未指定具体型号。
- **任务**：自主守门（拦截快速移动球体）、球体逃脱与抓取泛化任务。
- **对比基线**：与四足平台守门方法及固定运动跟踪方法对比，突出人形机器人的两大挑战（自然全身运动与广域防守范围）。

### 关键数字与结果
- **成功拦截**：真实实验中机器人成功完成对快速移动球体的敏捷、自主且自然的拦截。
- **泛化能力**：除守门外，方法在球体逃脱与抓取任务中同样有效，验证了策略的通用性。
- **响应时间**：在等效响应时间内覆盖更广防守范围，优于四足平台方法。

### 结论
该工作为机器人-移动物体动态交互提供了实用且可扩展的解决方案，通过单一端到端策略与人类运动先验的整合，推动了更自适应、更类人的机器人行为发展。未来可进一步优化运动先验的多样性及感知输入的鲁棒性。

## Overview
We present a reinforcement learning framework for autonomous goalkeeping with humanoid robots in real-world scenarios. While prior work has demonstrated similar capabilities on quadrupedal platforms, humanoid goalkeeping introduces two critical challenges: (1) generating natural, human-like whole-body motions, and (2) covering a wider guarding range with an equivalent response time. Unlike existing approaches that rely on separate teleoperation or fixed motion tracking for whole-body control, our method learns a single end-to-end RL policy, enabling fully autonomous, highly dynamic, and human-like robot-object interactions. To achieve this, we integrate multiple human motion priors conditioned on perceptual inputs into the RL training via an adversarial scheme. We demonstrate the effectiveness of our method through real-world experiments, where the humanoid robot successfully performs agile, autonomous, and naturalistic interceptions of fast-moving balls. In addition to goalkeeping, we demonstrate the generalization of our approach through tasks such as ball escaping and grabbing. Our work presents a practical and scalable solution for enabling highly dynamic interactions between robots and moving objects, advancing the field toward more adaptive and lifelike robotic behaviors.

## 参考
- Semantic Scholar search: Humanoid Goalkeeper: Learning from Position Conditioned Task-Motion Constraints

## 개요
사족 플랫폼이나 고정 모션 트래킹에 의존하는 기존 연구와 달리, 이 방법은 원격 조작이나 사전 정의된 동작을 분리하지 않고 엔드투엔드 강화 학습 정책을 직접 학습한다. 적대적 방식(adversarial scheme)을 통해 인식 입력 기반의 인간 동작 사전(human motion priors)을 훈련에 통합함으로써, 휴머노이드 로봇이 자연스럽고 인간다운 전신 동작을 자율적으로 생성할 수 있게 한다. 실제 세계 실험에서 로봇이 빠르게 움직이는 공을 성공적으로 차단하고, 공 탈출 및 잡기 작업으로 일반화할 수 있음을 보여주며, 동적 인간-로봇 상호작용을 위한 확장 가능한 실용적 솔루션을 제공한다.

## 핵심 내용
### 방법 아키텍처
- **엔드투엔드 강화 학습 정책**: 단일 정책 네트워크가 인식 입력을 직접 처리하고 관절 제어 명령을 출력하여, 기존의 분리된 원격 조작이나 고정 모션 트래킹을 대체한다.
- **적대적 동작 사전 통합**: 적대적 훈련(adversarial scheme)을 통해 다양한 인간 동작 사전(human motion priors)을 정책 학습에 통합하여, 로봇이 인간다운 전신 동작을 생성하게 한다.
- **인식 조건화**: 동작 사전은 실시간 시각 입력(예: 공 위치)을 기반으로 조건화되어, 동작이 장면 역학과 일치하도록 보장한다.

### 실험 설정
- **플랫폼**: 실제 휴머노이드 로봇 플랫폼, 구체적인 모델은 명시되지 않음.
- **작업**: 자율 골키퍼(빠르게 움직이는 공 차단), 공 탈출 및 잡기 일반화 작업.
- **비교 기준선**: 사족 플랫폼 골키퍼 방법 및 고정 모션 트래킹 방법과 비교하여, 휴머노이드 로봇의 두 가지 주요 과제(자연스러운 전신 동작과 넓은 수비 범위)를 강조.

### 주요 수치 및 결과
- **성공적 차단**: 실제 실험에서 로봇이 빠르게 움직이는 공을 민첩하고 자율적이며 자연스럽게 차단하는 데 성공.
- **일반화 능력**: 골키퍼 외에도 이 방법은 공 탈출 및 잡기 작업에서도 효과적임을 확인하여 정책의 범용성을 검증.
- **응답 시간**: 동등한 응답 시간 내에 더 넓은 수비 범위를 커버하여 사족 플랫폼 방법보다 우수.

### 결론
이 연구는 로봇-이동 물체 동적 상호작용을 위한 실용적이고 확장 가능한 솔루션을 제공하며, 단일 엔드투엔드 정책과 인간 동작 사전의 통합을 통해 더 적응적이고 인간다운 로봇 행동 발전을 촉진한다. 향후 동작 사전의 다양성과 인식 입력의 견고성을 더욱 최적화할 수 있다.

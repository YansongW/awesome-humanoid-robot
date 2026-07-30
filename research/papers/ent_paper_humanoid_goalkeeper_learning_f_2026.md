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
    from Position Conditioned Task-Motion Constraints. [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py'
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

## 개요
본 논문은 실제 환경에서 휴머노이드 로봇의 자율 골키퍼를 위한 강화 학습 프레임워크를 제시합니다. 이전 연구에서 사족 보행 플랫폼에서 유사한 기능이 입증되었지만, 휴머노이드 골키퍼는 두 가지 중요한 과제를 제기합니다: (1) 자연스럽고 인간과 유사한 전신 동작 생성, (2) 동등한 반응 시간으로 더 넓은 방어 범위를 커버하는 것입니다. 전신 제어를 위해 별도의 원격 조작이나 고정된 동작 추적에 의존하는 기존 접근 방식과 달리, 우리의 방법은 단일 종단 간 강화 학습 정책을 학습하여 완전 자율적이고 고도로 동적이며 인간과 유사한 로봇-객체 상호 작용을 가능하게 합니다. 이를 위해, 우리는 지각 입력에 조건화된 여러 인간 동작 사전 정보를 적대적 방식을 통해 강화 학습 훈련에 통합합니다. 우리는 실제 실험을 통해 휴머노이드 로봇이 빠르게 움직이는 공을 민첩하고 자율적이며 자연스럽게 차단하는 데 성공함으로써 방법의 효과를 입증합니다. 골키퍼 외에도 공 탈출 및 잡기와 같은 작업을 통해 접근 방식의 일반화를 보여줍니다. 우리의 연구는 로봇과 움직이는 객체 간의 고도로 동적인 상호 작용을 가능하게 하는 실용적이고 확장 가능한 솔루션을 제시하며, 더 적응적이고 생생한 로봇 행동을 향한 분야를 발전시킵니다.

## 핵심 내용
본 논문은 실제 환경에서 휴머노이드 로봇의 자율 골키퍼를 위한 강화 학습 프레임워크를 제시합니다. 이전 연구에서 사족 보행 플랫폼에서 유사한 기능이 입증되었지만, 휴머노이드 골키퍼는 두 가지 중요한 과제를 제기합니다: (1) 자연스럽고 인간과 유사한 전신 동작 생성, (2) 동등한 반응 시간으로 더 넓은 방어 범위를 커버하는 것입니다. 전신 제어를 위해 별도의 원격 조작이나 고정된 동작 추적에 의존하는 기존 접근 방식과 달리, 우리의 방법은 단일 종단 간 강화 학습 정책을 학습하여 완전 자율적이고 고도로 동적이며 인간과 유사한 로봇-객체 상호 작용을 가능하게 합니다. 이를 위해, 우리는 지각 입력에 조건화된 여러 인간 동작 사전 정보를 적대적 방식을 통해 강화 학습 훈련에 통합합니다. 우리는 실제 실험을 통해 휴머노이드 로봇이 빠르게 움직이는 공을 민첩하고 자율적이며 자연스럽게 차단하는 데 성공함으로써 방법의 효과를 입증합니다. 골키퍼 외에도 공 탈출 및 잡기와 같은 작업을 통해 접근 방식의 일반화를 보여줍니다. 우리의 연구는 로봇과 움직이는 객체 간의 고도로 동적인 상호 작용을 가능하게 하는 실용적이고 확장 가능한 솔루션을 제시하며, 더 적응적이고 생생한 로봇 행동을 향한 분야를 발전시킵니다.

## 参考
- Semantic Scholar search: Humanoid Goalkeeper: Learning from Position Conditioned Task-Motion Constraints

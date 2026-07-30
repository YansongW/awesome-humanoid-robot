---
$id: ent_paper_fu_humanplus_humanoid_shadowing_a_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HumanPlus: Humanoid Shadowing and Imitation from Humans'
  zh: HumanPlus：从人类进行人形机器人影子跟随与模仿
  ko: 'HumanPlus: 인간으로부터의 휴머노이드 섀도잉 및 모방'
summary:
  en: HumanPlus introduces a full-stack system that enables a 33-DoF 180 cm humanoid to shadow human body and hand motion
    in real time from a single RGB camera, and to learn autonomous vision-based manipulation and locomotion skills from as
    few as 40 collected demonstrations.
  zh: HumanPlus 是一个全栈系统，由斯坦福大学团队开发，能让一台 33 自由度、180 厘米高的人形机器人通过单个 RGB 摄像头实时模仿人类身体和手部动作，并仅需 40 次演示即可学习自主视觉操作与移动技能。
  ko: HumanPlus는 33-DoF, 180cm 휴머노이드가 단일 RGB 카메라로 인간의 신체 및 손 동작을 실시간 따라 하고, 수집된 최대 40개의 시연으로부터 자기 중심 시각 기반의 자율 조작 및 이동 기술을
    학습할 수 있는 전체 시스템을 제안한다.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
- 11_applications_markets
- 02_components
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- humanoid_shadowing
- humanoid_imitation
- behavior_cloning
- sim_to_real
- reinforcement_learning
- whole_body_control
- dexterous_manipulation
- egocentric_vision
- transformer_policy
- human_motion_retargeting
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.10454v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'HumanPlus: Humanoid Shadowing and Imitation from Humans'
  url: https://arxiv.org/abs/2406.10454
  date: '2024'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
HumanPlus 的核心思路是利用海量人类数据训练人形机器人，但实践中面临感知控制复杂、形态与驱动差异大、缺乏数据管道等挑战。该系统首先利用现有 40 小时人类运动数据集，通过强化学习在仿真中训练低级策略，该策略可迁移到真实世界，使机器人仅凭 RGB 摄像头即可实时跟随人体与手部运动（即“影子模式”）。通过影子模式，人类操作员可以远程操控机器人收集全身数据，用于学习不同任务。随后，系统利用收集的数据进行监督行为克隆，训练基于第一人称视觉的技能策略，使机器人能够通过模仿人类技能自主完成任务。在定制的 33 自由度、180 厘米人形机器人上，该系统仅用最多 40 次演示，即可自主完成穿鞋站立行走、从仓库货架卸货、折叠运动衫、重新排列物品、打字以及向另一机器人打招呼等任务，成功率在 60% 到 100% 之间。

## 核心内容
### 系统架构与方法

HumanPlus 采用全栈设计，分为两个主要阶段：

1.  **低级策略训练（影子模式）**：
    *   利用现有 40 小时人类运动数据集，在仿真环境中通过强化学习训练一个低级策略。
    *   该策略能够实时将人体运动（通过单个 RGB 摄像头捕捉）映射到 33 自由度人形机器人的关节控制指令，实现“影子模式”。
    *   影子模式允许人类操作员远程操控机器人，在真实世界中收集全身数据，包括视觉、关节角度和力反馈等。

2.  **高级技能策略训练（行为克隆）**：
    *   利用影子模式收集的演示数据，进行监督行为克隆。
    *   训练基于第一人称（egocentric）视觉的技能策略，使机器人能够自主完成特定任务。
    *   每个任务仅需 40 次演示即可训练出有效的技能策略。

### 实验设置与关键数字

*   **机器人平台**：定制化 33 自由度、180 厘米高的人形机器人。
*   **传感器**：仅使用单个 RGB 摄像头进行人体运动捕捉和机器人自主视觉。
*   **训练数据**：低级策略使用 40 小时公开人类运动数据集；高级技能策略使用最多 40 次真实世界演示。
*   **任务与成功率**：
    *   穿鞋站立行走：60-100%
    *   从仓库货架卸货：60-100%
    *   折叠运动衫：60-100%
    *   重新排列物品：60-100%
    *   打字：60-100%
    *   向另一机器人打招呼：60-100%

### 结论

HumanPlus 展示了利用人类数据训练人形机器人的可行路径，通过影子模式解决数据收集瓶颈，并通过行为克隆实现自主技能学习。该系统在多个复杂任务上取得了 60-100% 的成功率，验证了其有效性。项目网站提供更多细节：https://humanoid-ai.github.io/

## Overview
One of the key arguments for building robots that have similar form factors to human beings is that we can leverage the massive human data for training. Yet, doing so has remained challenging in practice due to the complexities in humanoid perception and control, lingering physical gaps between humanoids and humans in morphologies and actuation, and lack of a data pipeline for humanoids to learn autonomous skills from egocentric vision. In this paper, we introduce a full-stack system for humanoids to learn motion and autonomous skills from human data. We first train a low-level policy in simulation via reinforcement learning using existing 40-hour human motion datasets. This policy transfers to the real world and allows humanoid robots to follow human body and hand motion in real time using only a RGB camera, i.e. shadowing. Through shadowing, human operators can teleoperate humanoids to collect whole-body data for learning different tasks in the real world. Using the data collected, we then perform supervised behavior cloning to train skill policies using egocentric vision, allowing humanoids to complete different tasks autonomously by imitating human skills. We demonstrate the system on our customized 33-DoF 180cm humanoid, autonomously completing tasks such as wearing a shoe to stand up and walk, unloading objects from warehouse racks, folding a sweatshirt, rearranging objects, typing, and greeting another robot with 60-100% success rates using up to 40 demonstrations. Project website: https://humanoid-ai.github.io/

## 개요
인간과 유사한 형태의 로봇을 구축하는 주요 논거 중 하나는 방대한 인간 데이터를 훈련에 활용할 수 있다는 점입니다. 그러나 실제로는 휴머노이드 인식 및 제어의 복잡성, 형태와 구동 방식에서 인간과 휴머노이드 간에 존재하는 물리적 차이, 그리고 휴머노이드가 자기중심 시각(egocentric vision)으로부터 자율적 기술을 학습할 데이터 파이프라인의 부재로 인해 이를 실현하는 것은 여전히 어려운 과제로 남아 있습니다. 본 논문에서는 휴머노이드가 인간 데이터로부터 움직임과 자율적 기술을 학습할 수 있는 풀스택 시스템을 소개합니다. 먼저 기존의 40시간 분량 인간 동작 데이터셋을 사용하여 시뮬레이션에서 강화 학습을 통해 저수준 정책(low-level policy)을 훈련합니다. 이 정책은 실제 세계로 전이되어 휴머노이드 로봇이 RGB 카메라만으로 실시간으로 인간의 신체 및 손 동작을 따라 할 수 있게 합니다(즉, 섀도잉). 섀도잉을 통해 인간 운영자는 휴머노이드를 원격 조종하여 실제 세계에서 다양한 작업을 학습하기 위한 전신 데이터를 수집할 수 있습니다. 수집된 데이터를 바탕으로 자기중심 시각을 사용한 지도 행동 복제(supervised behavior cloning)를 통해 기술 정책(skill policy)을 훈련하여, 휴머노이드가 인간의 기술을 모방함으로써 다양한 작업을 자율적으로 완료할 수 있게 합니다. 우리는 맞춤형 33자유도(DoF) 180cm 휴머노이드에서 이 시스템을 시연하며, 신발을 신고 일어서서 걷기, 창고 선반에서 물건 내리기, 후드티 접기, 물건 재배치, 타이핑, 다른 로봇과 인사하기 등의 작업을 최대 40회의 시연을 통해 60-100%의 성공률로 자율적으로 완료합니다. 프로젝트 웹사이트: https://humanoid-ai.github.io/

## 핵심 내용
인간과 유사한 형태의 로봇을 구축하는 주요 논거 중 하나는 방대한 인간 데이터를 훈련에 활용할 수 있다는 점입니다. 그러나 실제로는 휴머노이드 인식 및 제어의 복잡성, 형태와 구동 방식에서 인간과 휴머노이드 간에 존재하는 물리적 차이, 그리고 휴머노이드가 자기중심 시각으로부터 자율적 기술을 학습할 데이터 파이프라인의 부재로 인해 이를 실현하는 것은 여전히 어려운 과제로 남아 있습니다. 본 논문에서는 휴머노이드가 인간 데이터로부터 움직임과 자율적 기술을 학습할 수 있는 풀스택 시스템을 소개합니다. 먼저 기존의 40시간 분량 인간 동작 데이터셋을 사용하여 시뮬레이션에서 강화 학습을 통해 저수준 정책을 훈련합니다. 이 정책은 실제 세계로 전이되어 휴머노이드 로봇이 RGB 카메라만으로 실시간으로 인간의 신체 및 손 동작을 따라 할 수 있게 합니다(즉, 섀도잉). 섀도잉을 통해 인간 운영자는 휴머노이드를 원격 조종하여 실제 세계에서 다양한 작업을 학습하기 위한 전신 데이터를 수집할 수 있습니다. 수집된 데이터를 바탕으로 자기중심 시각을 사용한 지도 행동 복제를 통해 기술 정책을 훈련하여, 휴머노이드가 인간의 기술을 모방함으로써 다양한 작업을 자율적으로 완료할 수 있게 합니다. 우리는 맞춤형 33자유도 180cm 휴머노이드에서 이 시스템을 시연하며, 신발을 신고 일어서서 걷기, 창고 선반에서 물건 내리기, 후드티 접기, 물건 재배치, 타이핑, 다른 로봇과 인사하기 등의 작업을 최대 40회의 시연을 통해 60-100%의 성공률로 자율적으로 완료합니다. 프로젝트 웹사이트: https://humanoid-ai.github.io/

## 参考
- http://arxiv.org/abs/2406.10454v1

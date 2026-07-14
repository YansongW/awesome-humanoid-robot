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
  zh: HumanPlus 提出了一套完整系统，使 33 自由度、180 cm 的人形机器人仅通过单目 RGB 相机实时跟随人体与手部动作，并利用多达 40 个采集示教学习基于自我中心视觉的自主操作与移动技能。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.10454v1.
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
One of the key arguments for building robots that have similar form factors to human beings is that we can leverage the massive human data for training. Yet, doing so has remained challenging in practice due to the complexities in humanoid perception and control, lingering physical gaps between humanoids and humans in morphologies and actuation, and lack of a data pipeline for humanoids to learn autonomous skills from egocentric vision. In this paper, we introduce a full-stack system for humanoids to learn motion and autonomous skills from human data. We first train a low-level policy in simulation via reinforcement learning using existing 40-hour human motion datasets. This policy transfers to the real world and allows humanoid robots to follow human body and hand motion in real time using only a RGB camera, i.e. shadowing. Through shadowing, human operators can teleoperate humanoids to collect whole-body data for learning different tasks in the real world. Using the data collected, we then perform supervised behavior cloning to train skill policies using egocentric vision, allowing humanoids to complete different tasks autonomously by imitating human skills. We demonstrate the system on our customized 33-DoF 180cm humanoid, autonomously completing tasks such as wearing a shoe to stand up and walk, unloading objects from warehouse racks, folding a sweatshirt, rearranging objects, typing, and greeting another robot with 60-100% success rates using up to 40 demonstrations. Project website: https://humanoid-ai.github.io/

## 核心内容
One of the key arguments for building robots that have similar form factors to human beings is that we can leverage the massive human data for training. Yet, doing so has remained challenging in practice due to the complexities in humanoid perception and control, lingering physical gaps between humanoids and humans in morphologies and actuation, and lack of a data pipeline for humanoids to learn autonomous skills from egocentric vision. In this paper, we introduce a full-stack system for humanoids to learn motion and autonomous skills from human data. We first train a low-level policy in simulation via reinforcement learning using existing 40-hour human motion datasets. This policy transfers to the real world and allows humanoid robots to follow human body and hand motion in real time using only a RGB camera, i.e. shadowing. Through shadowing, human operators can teleoperate humanoids to collect whole-body data for learning different tasks in the real world. Using the data collected, we then perform supervised behavior cloning to train skill policies using egocentric vision, allowing humanoids to complete different tasks autonomously by imitating human skills. We demonstrate the system on our customized 33-DoF 180cm humanoid, autonomously completing tasks such as wearing a shoe to stand up and walk, unloading objects from warehouse racks, folding a sweatshirt, rearranging objects, typing, and greeting another robot with 60-100% success rates using up to 40 demonstrations. Project website: https://humanoid-ai.github.io/

## 参考
- http://arxiv.org/abs/2406.10454v1


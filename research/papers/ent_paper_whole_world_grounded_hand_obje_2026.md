---
$id: ent_paper_whole_world_grounded_hand_obje_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WHOLE: World-Grounded Hand-Object Lifted from Egocentric Videos'
  zh: 'WHOLE: World-Grounded Hand-Object Lifted from Egocentric Videos'
  ko: 'WHOLE: World-Grounded Hand-Object Lifted from Egocentric Videos'
summary:
  en: 'WHOLE: World-Grounded Hand-Object Lifted from Egocentric Videos is a 2026 work on human motion analysis and synthesis
    for humanoid robots.'
  zh: WHOLE 是一项 2026 年提出的方法，用于从第一人称视频中联合重建手与物体在全局世界坐标系中的运动。其核心贡献在于学习手-物体运动的生成先验，从而在交互过程中实现联合推理，显著优于分别处理手和物体再后处理的传统方法。
  ko: 'WHOLE: World-Grounded Hand-Object Lifted from Egocentric Videos is a 2026 work on human motion analysis and synthesis
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- motion_analysis
- motion_synthesis
- whole
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.22209v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'WHOLE: World-Grounded Hand-Object Lifted from Egocentric Videos (arXiv)'
  url: https://arxiv.org/abs/2602.22209
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'WHOLE: World-Grounded Hand-Object Lifted from Egocentric Videos project page'
  url: https://judyye.github.io/whole-www/
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
第一人称视角下的操作视频因交互过程中的严重遮挡以及物体频繁进出视野而极具挑战性。现有方法通常孤立地恢复手或物体的姿态，在交互场景中表现不佳，且无法处理物体离开视野的情况，导致手-物体关系不一致。WHOLE 通过引入一个预训练的生成先验，在测试时引导其生成符合视频观测的运动轨迹，从而在全局空间中联合重建手与物体的运动。该方法在手部运动估计、6D 物体姿态估计以及相对交互重建方面均达到了当前最优性能。

## 核心内容
### 方法概述
WHOLE 的核心思路是学习一个手-物体联合运动的生成先验，该先验在训练阶段从大量交互数据中捕获手与物体之间的物理约束与运动规律。在测试阶段，给定第一人称视频和物体模板，该先验被用作引导，生成与视频观测一致的全局轨迹。

### 架构与实验设置
- **输入**：第一人称视频（egocentric video）以及已知的物体模板（object templates）。
- **输出**：手与物体在全局世界坐标系（world space）下的完整运动轨迹。
- **关键机制**：利用生成先验进行联合推理，而非分别估计手和物体姿态后再进行后处理对齐。这使得模型能够处理物体离开视野（out-of-sight）的情况，并保持手-物体交互关系的一致性。

### 关键性能数字
- 在手部运动估计（hand motion estimation）任务上达到当前最优（state-of-the-art）。
- 在6D物体姿态估计（6D object pose estimation）任务上同样取得最优结果。
- 在相对交互重建（relative interaction reconstruction）指标上显著优于分别处理手和物体的方法。

### 结论
WHOLE 通过引入联合生成先验，有效解决了第一人称视频中手-物体交互重建的遮挡与不一致问题，为机器人从人类演示中学习操作技能提供了更可靠的全局运动数据。项目网站：https://judyye.github.io/whole-www

## Overview
Egocentric manipulation videos are highly challenging due to severe occlusions during interactions and frequent object entries and exits from the camera view as the person moves. Current methods typically focus on recovering either hand or object pose in isolation, but both struggle during interactions and fail to handle out-of-sight cases. Moreover, their independent predictions often lead to inconsistent hand-object relations. We introduce WHOLE, a method that holistically reconstructs hand and object motion in world space from egocentric videos given object templates. Our key insight is to learn a generative prior over hand-object motion to jointly reason about their interactions. At test time, the pretrained prior is guided to generate trajectories that conform to the video observations. This joint generative reconstruction substantially outperforms approaches that process hands and objects separately followed by post-processing. WHOLE achieves state-of-the-art performance on hand motion estimation, 6D object pose estimation, and their relative interaction reconstruction. Project website: https://judyye.github.io/whole-www

## 개요
자기중심적 조작 비디오는 상호작용 중 심각한 가려짐과 사람이 움직임에 따라 카메라 시야에서 물체가 자주 들어오고 나가는 현상으로 인해 매우 도전적입니다. 현재 방법들은 일반적으로 손 또는 물체 포즈를 개별적으로 복원하는 데 초점을 맞추지만, 둘 다 상호작용 중에 어려움을 겪고 시야 밖의 경우를 처리하지 못합니다. 게다가, 그들의 독립적인 예측은 종종 일관되지 않은 손-물체 관계를 초래합니다. 우리는 WHOLE을 소개합니다. 이 방법은 물체 템플릿이 주어진 자기중심적 비디오에서 세계 공간에서 손과 물체의 움직임을 전체적으로 재구성합니다. 우리의 핵심 통찰은 손-물체 움직임에 대한 생성적 사전 지식을 학습하여 상호작용을 공동으로 추론하는 것입니다. 테스트 시, 사전 학습된 사전 지식은 비디오 관찰에 부합하는 궤적을 생성하도록 안내됩니다. 이 공동 생성적 재구성은 손과 물체를 별도로 처리한 후 후처리하는 접근 방식보다 훨씬 뛰어난 성능을 보입니다. WHOLE은 손 움직임 추정, 6D 물체 포즈 추정 및 상대적 상호작용 재구성에서 최첨단 성능을 달성합니다. 프로젝트 웹사이트: https://judyye.github.io/whole-www

## 핵심 내용
자기중심적 조작 비디오는 상호작용 중 심각한 가려짐과 사람이 움직임에 따라 카메라 시야에서 물체가 자주 들어오고 나가는 현상으로 인해 매우 도전적입니다. 현재 방법들은 일반적으로 손 또는 물체 포즈를 개별적으로 복원하는 데 초점을 맞추지만, 둘 다 상호작용 중에 어려움을 겪고 시야 밖의 경우를 처리하지 못합니다. 게다가, 그들의 독립적인 예측은 종종 일관되지 않은 손-물체 관계를 초래합니다. 우리는 WHOLE을 소개합니다. 이 방법은 물체 템플릿이 주어진 자기중심적 비디오에서 세계 공간에서 손과 물체의 움직임을 전체적으로 재구성합니다. 우리의 핵심 통찰은 손-물체 움직임에 대한 생성적 사전 지식을 학습하여 상호작용을 공동으로 추론하는 것입니다. 테스트 시, 사전 학습된 사전 지식은 비디오 관찰에 부합하는 궤적을 생성하도록 안내됩니다. 이 공동 생성적 재구성은 손과 물체를 별도로 처리한 후 후처리하는 접근 방식보다 훨씬 뛰어난 성능을 보입니다. WHOLE은 손 움직임 추정, 6D 물체 포즈 추정 및 상대적 상호작용 재구성에서 최첨단 성능을 달성합니다. 프로젝트 웹사이트: https://judyye.github.io/whole-www

## 参考
- http://arxiv.org/abs/2602.22209v1

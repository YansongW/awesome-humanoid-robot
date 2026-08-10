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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.22209v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (865 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2602.22209v1

## 개요
1인칭 시점의 조작 영상은 상호작용 과정에서의 심각한 가림 및 물체의 잦은 시야 이탈로 인해 매우 도전적입니다. 기존 방법들은 일반적으로 손이나 물체의 자세를 개별적으로 복원하여 상호작용 장면에서 성능이 저조하며, 물체가 시야를 벗어나는 경우를 처리하지 못해 손-물체 관계의 일관성이 깨집니다. WHOLE은 사전 학습된 생성 사전(distribution prior)을 도입하여 테스트 시점에 영상 관측과 일치하는 운동 궤적을 생성하도록 유도함으로써, 전역 공간에서 손과 물체의 운동을 공동으로 재구성합니다. 이 방법은 손 운동 추정, 6D 물체 자세 추정 및 상대적 상호작용 재구성에서 모두 최신 성능(state-of-the-art)을 달성했습니다.

## 핵심 내용
### 방법 개요
WHOLE의 핵심 아이디어는 손-물체 공동 운동의 생성 사전을 학습하는 것입니다. 이 사전은 훈련 단계에서 대량의 상호작용 데이터로부터 손과 물체 간의 물리적 제약 및 운동 규칙을 포착합니다. 테스트 단계에서는 1인칭 영상과 물체 템플릿이 주어지면, 이 사전이 가이드로 사용되어 영상 관측과 일치하는 전역 궤적을 생성합니다.

### 구조 및 실험 설정
- **입력**: 1인칭 영상(egocentric video) 및 알려진 물체 템플릿(object templates).
- **출력**: 전역 세계 좌표계(world space)에서의 손과 물체의 완전한 운동 궤적.
- **핵심 메커니즘**: 생성 사전을 이용한 공동 추론으로, 손과 물체 자세를 개별적으로 추정한 후 후처리 정렬을 수행하는 방식이 아닙니다. 이를 통해 물체가 시야를 벗어나는(out-of-sight) 상황을 처리하고 손-물체 상호작용 관계의 일관성을 유지할 수 있습니다.

### 주요 성능 수치
- 손 운동 추정(hand motion estimation) 작업에서 최신 성능(state-of-the-art) 달성.
- 6D 물체 자세 추정(6D object pose estimation) 작업에서도 최적의 결과 달성.
- 상대적 상호작용 재구성(relative interaction reconstruction) 지표에서 손과 물체를 개별적으로 처리하는 방법보다 현저히 우수한 성능.

### 결론
WHOLE은 공동 생성 사전을 도입하여 1인칭 영상에서의 손-물체 상호작용 재구성의 가림 및 불일치 문제를 효과적으로 해결하며, 로봇이 인간 시연으로부터 조작 기술을 학습하는 데 더 신뢰할 수 있는 전역 운동 데이터를 제공합니다. 프로젝트 웹사이트: https://judyye.github.io/whole-www

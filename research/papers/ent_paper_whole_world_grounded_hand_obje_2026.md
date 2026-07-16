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
  zh: 'WHOLE: World-Grounded Hand-Object Lifted from Egocentric Videos is a 2026 work on human motion analysis and synthesis
    for humanoid robots.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.22209v1.
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
Egocentric manipulation videos are highly challenging due to severe occlusions during interactions and frequent object entries and exits from the camera view as the person moves. Current methods typically focus on recovering either hand or object pose in isolation, but both struggle during interactions and fail to handle out-of-sight cases. Moreover, their independent predictions often lead to inconsistent hand-object relations. We introduce WHOLE, a method that holistically reconstructs hand and object motion in world space from egocentric videos given object templates. Our key insight is to learn a generative prior over hand-object motion to jointly reason about their interactions. At test time, the pretrained prior is guided to generate trajectories that conform to the video observations. This joint generative reconstruction substantially outperforms approaches that process hands and objects separately followed by post-processing. WHOLE achieves state-of-the-art performance on hand motion estimation, 6D object pose estimation, and their relative interaction reconstruction. Project website: https://judyye.github.io/whole-www

## 核心内容
Egocentric manipulation videos are highly challenging due to severe occlusions during interactions and frequent object entries and exits from the camera view as the person moves. Current methods typically focus on recovering either hand or object pose in isolation, but both struggle during interactions and fail to handle out-of-sight cases. Moreover, their independent predictions often lead to inconsistent hand-object relations. We introduce WHOLE, a method that holistically reconstructs hand and object motion in world space from egocentric videos given object templates. Our key insight is to learn a generative prior over hand-object motion to jointly reason about their interactions. At test time, the pretrained prior is guided to generate trajectories that conform to the video observations. This joint generative reconstruction substantially outperforms approaches that process hands and objects separately followed by post-processing. WHOLE achieves state-of-the-art performance on hand motion estimation, 6D object pose estimation, and their relative interaction reconstruction. Project website: https://judyye.github.io/whole-www

## 参考
- http://arxiv.org/abs/2602.22209v1

## Overview
Egocentric manipulation videos are highly challenging due to severe occlusions during interactions and frequent object entries and exits from the camera view as the person moves. Current methods typically focus on recovering either hand or object pose in isolation, but both struggle during interactions and fail to handle out-of-sight cases. Moreover, their independent predictions often lead to inconsistent hand-object relations. We introduce WHOLE, a method that holistically reconstructs hand and object motion in world space from egocentric videos given object templates. Our key insight is to learn a generative prior over hand-object motion to jointly reason about their interactions. At test time, the pretrained prior is guided to generate trajectories that conform to the video observations. This joint generative reconstruction substantially outperforms approaches that process hands and objects separately followed by post-processing. WHOLE achieves state-of-the-art performance on hand motion estimation, 6D object pose estimation, and their relative interaction reconstruction. Project website: https://judyye.github.io/whole-www

## Content
Egocentric manipulation videos are highly challenging due to severe occlusions during interactions and frequent object entries and exits from the camera view as the person moves. Current methods typically focus on recovering either hand or object pose in isolation, but both struggle during interactions and fail to handle out-of-sight cases. Moreover, their independent predictions often lead to inconsistent hand-object relations. We introduce WHOLE, a method that holistically reconstructs hand and object motion in world space from egocentric videos given object templates. Our key insight is to learn a generative prior over hand-object motion to jointly reason about their interactions. At test time, the pretrained prior is guided to generate trajectories that conform to the video observations. This joint generative reconstruction substantially outperforms approaches that process hands and objects separately followed by post-processing. WHOLE achieves state-of-the-art performance on hand motion estimation, 6D object pose estimation, and their relative interaction reconstruction. Project website: https://judyye.github.io/whole-www

## 개요
자기중심적 조작 비디오는 상호작용 중 심각한 가려짐과 사람이 움직임에 따라 카메라 시야에서 물체가 자주 들어오고 나가는 현상으로 인해 매우 도전적입니다. 현재 방법들은 일반적으로 손 또는 물체 포즈를 개별적으로 복원하는 데 초점을 맞추지만, 둘 다 상호작용 중에 어려움을 겪고 시야 밖의 경우를 처리하지 못합니다. 게다가, 그들의 독립적인 예측은 종종 일관되지 않은 손-물체 관계를 초래합니다. 우리는 WHOLE을 소개합니다. 이 방법은 물체 템플릿이 주어진 자기중심적 비디오에서 세계 공간에서 손과 물체의 움직임을 전체적으로 재구성합니다. 우리의 핵심 통찰은 손-물체 움직임에 대한 생성적 사전 지식을 학습하여 상호작용을 공동으로 추론하는 것입니다. 테스트 시, 사전 학습된 사전 지식은 비디오 관찰에 부합하는 궤적을 생성하도록 안내됩니다. 이 공동 생성적 재구성은 손과 물체를 별도로 처리한 후 후처리하는 접근 방식보다 훨씬 뛰어난 성능을 보입니다. WHOLE은 손 움직임 추정, 6D 물체 포즈 추정 및 상대적 상호작용 재구성에서 최첨단 성능을 달성합니다. 프로젝트 웹사이트: https://judyye.github.io/whole-www

## 핵심 내용
자기중심적 조작 비디오는 상호작용 중 심각한 가려짐과 사람이 움직임에 따라 카메라 시야에서 물체가 자주 들어오고 나가는 현상으로 인해 매우 도전적입니다. 현재 방법들은 일반적으로 손 또는 물체 포즈를 개별적으로 복원하는 데 초점을 맞추지만, 둘 다 상호작용 중에 어려움을 겪고 시야 밖의 경우를 처리하지 못합니다. 게다가, 그들의 독립적인 예측은 종종 일관되지 않은 손-물체 관계를 초래합니다. 우리는 WHOLE을 소개합니다. 이 방법은 물체 템플릿이 주어진 자기중심적 비디오에서 세계 공간에서 손과 물체의 움직임을 전체적으로 재구성합니다. 우리의 핵심 통찰은 손-물체 움직임에 대한 생성적 사전 지식을 학습하여 상호작용을 공동으로 추론하는 것입니다. 테스트 시, 사전 학습된 사전 지식은 비디오 관찰에 부합하는 궤적을 생성하도록 안내됩니다. 이 공동 생성적 재구성은 손과 물체를 별도로 처리한 후 후처리하는 접근 방식보다 훨씬 뛰어난 성능을 보입니다. WHOLE은 손 움직임 추정, 6D 물체 포즈 추정 및 상대적 상호작용 재구성에서 최첨단 성능을 달성합니다. 프로젝트 웹사이트: https://judyye.github.io/whole-www

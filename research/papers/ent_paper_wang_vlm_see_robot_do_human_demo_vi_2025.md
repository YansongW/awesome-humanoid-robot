---
$id: ent_paper_wang_vlm_see_robot_do_human_demo_vi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model'
  zh: SeeDo
  ko: 'VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model'
summary:
  en: 'VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model (SeeDo), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by New York University, and published at IROS25.'
  zh: 'VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model (SeeDo), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by New York University, and published at IROS25.'
  ko: 'VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model (SeeDo), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by New York University, and published at IROS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- seedo
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.08792v2.
sources:
- id: src_001
  type: website
  title: SeeDo source
  url: https://doi.org/10.1109/IROS60139.2025.11246682
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision Language Models (VLMs) have recently been adopted in robotics for their capability in common sense reasoning and generalizability. Existing work has applied VLMs to generate task and motion planning from natural language instructions and simulate training data for robot learning. In this work, we explore using VLM to interpret human demonstration videos and generate robot task planning. Our method integrates keyframe selection, visual perception, and VLM reasoning into a pipeline. We named it SeeDo because it enables the VLM to ''see'' human demonstrations and explain the corresponding plans to the robot for it to ''do''. To validate our approach, we collected a set of long-horizon human videos demonstrating pick-and-place tasks in three diverse categories and designed a set of metrics to comprehensively benchmark SeeDo against several baselines, including state-of-the-art video-input VLMs. The experiments demonstrate SeeDo's superior performance. We further deployed the generated task plans in both a simulation environment and on a real robot arm.

## 核心内容
Vision Language Models (VLMs) have recently been adopted in robotics for their capability in common sense reasoning and generalizability. Existing work has applied VLMs to generate task and motion planning from natural language instructions and simulate training data for robot learning. In this work, we explore using VLM to interpret human demonstration videos and generate robot task planning. Our method integrates keyframe selection, visual perception, and VLM reasoning into a pipeline. We named it SeeDo because it enables the VLM to ''see'' human demonstrations and explain the corresponding plans to the robot for it to ''do''. To validate our approach, we collected a set of long-horizon human videos demonstrating pick-and-place tasks in three diverse categories and designed a set of metrics to comprehensively benchmark SeeDo against several baselines, including state-of-the-art video-input VLMs. The experiments demonstrate SeeDo's superior performance. We further deployed the generated task plans in both a simulation environment and on a real robot arm.

## 参考
- http://arxiv.org/abs/2410.08792v2

## Overview
Vision Language Models (VLMs) have recently been adopted in robotics for their capability in common sense reasoning and generalizability. Existing work has applied VLMs to generate task and motion planning from natural language instructions and simulate training data for robot learning. In this work, we explore using VLM to interpret human demonstration videos and generate robot task planning. Our method integrates keyframe selection, visual perception, and VLM reasoning into a pipeline. We named it SeeDo because it enables the VLM to "see" human demonstrations and explain the corresponding plans to the robot for it to "do". To validate our approach, we collected a set of long-horizon human videos demonstrating pick-and-place tasks in three diverse categories and designed a set of metrics to comprehensively benchmark SeeDo against several baselines, including state-of-the-art video-input VLMs. The experiments demonstrate SeeDo's superior performance. We further deployed the generated task plans in both a simulation environment and on a real robot arm.

## Content
Vision Language Models (VLMs) have recently been adopted in robotics for their capability in common sense reasoning and generalizability. Existing work has applied VLMs to generate task and motion planning from natural language instructions and simulate training data for robot learning. In this work, we explore using VLM to interpret human demonstration videos and generate robot task planning. Our method integrates keyframe selection, visual perception, and VLM reasoning into a pipeline. We named it SeeDo because it enables the VLM to "see" human demonstrations and explain the corresponding plans to the robot for it to "do". To validate our approach, we collected a set of long-horizon human videos demonstrating pick-and-place tasks in three diverse categories and designed a set of metrics to comprehensively benchmark SeeDo against several baselines, including state-of-the-art video-input VLMs. The experiments demonstrate SeeDo's superior performance. We further deployed the generated task plans in both a simulation environment and on a real robot arm.

## 개요
Vision Language Models(VLM)은 최근 상식 추론 및 일반화 능력 덕분에 로봇 공학에서 채택되고 있습니다. 기존 연구는 VLM을 활용하여 자연어 명령으로부터 작업 및 동작 계획을 생성하고, 로봇 학습을 위한 훈련 데이터를 시뮬레이션해 왔습니다. 본 연구에서는 VLM을 사용하여 인간 시연 비디오를 해석하고 로봇 작업 계획을 생성하는 방법을 탐구합니다. 우리의 방법은 키프레임 선택, 시각적 인식, VLM 추론을 하나의 파이프라인으로 통합합니다. 이 방법을 SeeDo라고 명명했는데, 이는 VLM이 인간 시연을 '보고(see)' 로봇이 '실행(do)'할 수 있도록 해당 계획을 설명할 수 있게 하기 때문입니다. 접근 방식을 검증하기 위해 세 가지 다양한 범주에서 픽 앤 플레이스 작업을 시연하는 장기 인간 비디오 세트를 수집하고, 최첨단 비디오 입력 VLM을 포함한 여러 기준 모델과 SeeDo를 종합적으로 평가하기 위한 일련의 지표를 설계했습니다. 실험 결과 SeeDo의 우수한 성능이 입증되었습니다. 또한 생성된 작업 계획을 시뮬레이션 환경과 실제 로봇 팔에 배포했습니다.

## 핵심 내용
Vision Language Models(VLM)은 최근 상식 추론 및 일반화 능력 덕분에 로봇 공학에서 채택되고 있습니다. 기존 연구는 VLM을 활용하여 자연어 명령으로부터 작업 및 동작 계획을 생성하고, 로봇 학습을 위한 훈련 데이터를 시뮬레이션해 왔습니다. 본 연구에서는 VLM을 사용하여 인간 시연 비디오를 해석하고 로봇 작업 계획을 생성하는 방법을 탐구합니다. 우리의 방법은 키프레임 선택, 시각적 인식, VLM 추론을 하나의 파이프라인으로 통합합니다. 이 방법을 SeeDo라고 명명했는데, 이는 VLM이 인간 시연을 '보고(see)' 로봇이 '실행(do)'할 수 있도록 해당 계획을 설명할 수 있게 하기 때문입니다. 접근 방식을 검증하기 위해 세 가지 다양한 범주에서 픽 앤 플레이스 작업을 시연하는 장기 인간 비디오 세트를 수집하고, 최첨단 비디오 입력 VLM을 포함한 여러 기준 모델과 SeeDo를 종합적으로 평가하기 위한 일련의 지표를 설계했습니다. 실험 결과 SeeDo의 우수한 성능이 입증되었습니다. 또한 생성된 작업 계획을 시뮬레이션 환경과 실제 로봇 팔에 배포했습니다.

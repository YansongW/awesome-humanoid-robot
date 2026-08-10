---
$id: ent_paper_ramadurai_effect_of_human_involvement_on_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Effect of Human Involvement on Work Performance and Fluency in Human-Robot Collaboration for Recycling
  zh: 人类参与对回收中人机协作工作性能与流畅性的影响
  ko: 재활용을 위한 인간-로봇 협업에서 인간 참여가 작업 수행 및 유동성에 미치는 영향
summary:
  en: A within-subjects study with six participants and a UR3e cobot shows that increasing human assistance in occlusion removal,
    spacing, and grip selection raises robot sorting accuracy from 33.3% to 100% and improves subjective fluency in a recyclable
    cup sorting task.
  zh: 本研究通过六名受试者与UR3e协作机器人完成的回收杯分拣任务，评估了三种人类辅助等级（遮挡移除、最佳间距、最佳抓取）对工作表现的影响。结果显示，随着人类辅助程度增加，机器人分拣准确率从33.3%提升至100%，同时主观流畅性显著改善。
  ko: 6명의 참가자와 UR3e 협동로봇을 대상으로 한 피험자내 연구는, 가림 제거, 간격 최적화 및 그립 선택에서 인간 보조를 늘리면 재활용 컵 분류 작업의 로봇 정확도가 33.3%에서 100%로 향상되고 주관적
    유동성이 개선됨을 보여준다.
domains:
- 11_applications_markets
- 02_components
- 07_ai_models_algorithms
- 03_manufacturing_processes
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
tags:
- human_robot_collaboration
- recycling
- cobot
- vision_guided_grasping
- sorting
- task_fluency
- human_in_the_loop
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2201.07990v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (586 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Effect of Human Involvement on Work Performance and Fluency in Human-Robot Collaboration for Recycling
  url: https://arxiv.org/abs/2201.07990
  date: '2022'
  accessed_at: '2026-06-26'
---
## 概述
在回收领域，由于可回收物成分差异巨大，人机协作具有重要潜力。六名参与者与配备视觉系统的机械臂协作完成可回收物分拣任务，研究设置了三种人类辅助等级：Level 1（遮挡移除）、Level 2（最佳间距）、Level 3（最佳抓取）。实验测量了机器人准确率、任务时间和主观流畅性等指标，发现人类参与对机器人准确率有显著影响，准确率随辅助等级提升而增加。

## 核心内容
### 实验设计
- **设备**：UR3e协作机器人，配备视觉系统
- **受试者**：6名参与者
- **任务**：可回收杯分拣任务
- **实验设计**：受试者内设计（within-subjects）

### 人类辅助等级
- **Level 1**：人类仅负责移除遮挡物
- **Level 2**：人类提供最佳间距安排
- **Level 3**：人类选择最佳抓取方式

### 关键结果
- **机器人准确率**：
  - Level 1：33.3%
  - Level 2：69%
  - Level 3：100%
- **主观流畅性**：随辅助等级提升而改善
- **任务时间**：未报告显著差异

### 结论
对于涉及尺寸、形状和成分多样材料的回收分拣流程，人类辅助能在保持成本效益的同时显著提升机器人准确率。研究建议在实际回收场景中根据材料复杂度动态调整人类参与程度。

## Overview
Human-robot collaboration has significant potential in recycling due to the wide variation in the composition of recyclable products. Six participants performed a recyclable item sorting task collaborating with a robot arm equipped with a vision system. The effect of three different levels of human involvement or assistance to the robot (Level 1- occlusion removal; Level 2- optimal spacing; Level 3- optimal grip) on performance metrics such as robot accuracy, task time and subjective fluency were assessed. Results showed that human involvement had a remarkable impact on the robot's accuracy, which increased with human involvement level. Mean accuracy values were 33.3% for Level 1, 69% for Level 2 and 100% for Level 3. The results imply that for sorting processes involving diverse materials that vary in size, shape, and composition, human assistance could improve the robot's accuracy to a significant extent while also being cost-effective.

## 参考
- http://arxiv.org/abs/2201.07990v1

## 개요
재활용 분야에서는 재활용 가능 물품의 성분 차이가 크기 때문에, 인간-로봇 협업이 중요한 잠재력을 지닌다. 6명의 참가자가 비전 시스템을 갖춘 로봇 팔과 협력하여 재활용품 분류 작업을 수행했으며, 연구에서는 세 가지 인간 보조 수준을 설정했다: Level 1(가림 제거), Level 2(최적 간격), Level 3(최적 파지). 실험에서는 로봇 정확도, 작업 시간, 주관적 유창성 등의 지표를 측정했으며, 인간의 참여가 로봇 정확도에 유의미한 영향을 미치고, 정확도는 보조 수준이 높아질수록 증가함을 발견했다.

## 핵심 내용
### 실험 설계
- **장비**: UR3e 협동 로봇, 비전 시스템 탑재
- **피험자**: 6명의 참가자
- **작업**: 재활용 컵 분류 작업
- **실험 설계**: 피험자 내 설계(within-subjects)

### 인간 보조 수준
- **Level 1**: 인간은 가림 물체 제거만 담당
- **Level 2**: 인간이 최적 간격 배치 제공
- **Level 3**: 인간이 최적 파지 방식 선택

### 주요 결과
- **로봇 정확도**:
  - Level 1: 33.3%
  - Level 2: 69%
  - Level 3: 100%
- **주관적 유창성**: 보조 수준이 높아질수록 개선됨
- **작업 시간**: 유의미한 차이 보고되지 않음

### 결론
크기, 모양, 성분이 다양한 재료를 포함하는 재활용 분류 공정에서 인간 보조는 비용 효율성을 유지하면서 로봇 정확도를 크게 향상시킬 수 있다. 연구는 실제 재활용 현장에서 재료 복잡성에 따라 인간 참여 수준을 동적으로 조정할 것을 제안한다.

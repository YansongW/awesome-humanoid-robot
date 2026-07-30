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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2201.07990v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
인간-로봇 협업은 재활용 가능한 제품의 구성이 매우 다양하기 때문에 재활용 분야에서 큰 잠재력을 가지고 있습니다. 6명의 참가자가 비전 시스템을 갖춘 로봇 팔과 협력하여 재활용 품목 분류 작업을 수행했습니다. 인간의 개입 또는 로봇 지원의 세 가지 수준(레벨 1 - 폐색 제거; 레벨 2 - 최적 간격; 레벨 3 - 최적 그립)이 로봇 정확도, 작업 시간 및 주관적 유창성과 같은 성능 지표에 미치는 영향을 평가했습니다. 결과는 인간의 개입이 로봇의 정확도에 현저한 영향을 미치며, 개입 수준이 증가함에 따라 정확도가 향상됨을 보여주었습니다. 평균 정확도 값은 레벨 1에서 33.3%, 레벨 2에서 69%, 레벨 3에서 100%였습니다. 이러한 결과는 크기, 모양 및 구성이 다양한 여러 재료를 포함하는 분류 과정에서 인간의 지원이 로봇의 정확도를 크게 향상시키면서도 비용 효율적일 수 있음을 시사합니다.

## 핵심 내용
인간-로봇 협업은 재활용 가능한 제품의 구성이 매우 다양하기 때문에 재활용 분야에서 큰 잠재력을 가지고 있습니다. 6명의 참가자가 비전 시스템을 갖춘 로봇 팔과 협력하여 재활용 품목 분류 작업을 수행했습니다. 인간의 개입 또는 로봇 지원의 세 가지 수준(레벨 1 - 폐색 제거; 레벨 2 - 최적 간격; 레벨 3 - 최적 그립)이 로봇 정확도, 작업 시간 및 주관적 유창성과 같은 성능 지표에 미치는 영향을 평가했습니다. 결과는 인간의 개입이 로봇의 정확도에 현저한 영향을 미치며, 개입 수준이 증가함에 따라 정확도가 향상됨을 보여주었습니다. 평균 정확도 값은 레벨 1에서 33.3%, 레벨 2에서 69%, 레벨 3에서 100%였습니다. 이러한 결과는 크기, 모양 및 구성이 다양한 여러 재료를 포함하는 분류 과정에서 인간의 지원이 로봇의 정확도를 크게 향상시키면서도 비용 효율적일 수 있음을 시사합니다.

## 参考
- http://arxiv.org/abs/2201.07990v1

---
$id: ent_paper_black_robotic_versus_human_teleopera_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robotic versus Human Teleoperation for Remote Ultrasound
  zh: 远程超声的机器人与人类遥操作对比
  ko: 원격 초음파를 위한 로봇 대 인간 원격조작 비교
summary:
  en: Presents a within-subjects comparison of robotic (Franka Panda) and human (mixed-reality HoloLens 2 follower) teleoperation
    for remote diagnostic ultrasound on a phantom, reporting statistically equivalent completion time and image-space tracking
    accuracy, but more consistent and lower applied force for human teleoperation.
  zh: 本文比较了机器人（Franka Panda）与人类（混合现实HoloLens 2跟随者）远程操作在诊断超声中的表现。核心贡献是发现两者在完成时间和图像空间跟踪精度上统计等效，但人类远程操作施加的力更一致且更低，且更具实用性和可及性。
  ko: 본 논문은 팬텀을 대상으로 로봇(Franka Panda)과 인간(혼합현실 HoloLens 2 추종자) 원격 초음파 원격조작을 비교하여, 완료 시간과 영상 공간 추적 정확도에서 통계적으로 유의한 차이가 없으나
    인간 원격조작이 더 일관되고 낮은 힘을 가함을 보고한다.
domains:
- 11_applications_markets
- 06_design_engineering
- 08_software_middleware
layers:
- intelligence
- midstream
- validation_markets
functional_roles:
- knowledge
- intelligence
- system
tags:
- teleoperation
- remote_ultrasound
- tele_ultrasound
- human_teleoperation
- robotic_teleoperation
- mixed_reality
- haptic_feedback
- human_in_the_loop
- franka_panda
- hololens_2
- web_rtc
- telepresence
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.07275v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (723 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Robotic versus Human Teleoperation for Remote Ultrasound
  url: https://arxiv.org/abs/2511.07275
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
- system
---
## 概述
该研究针对远程超声诊断中机器人远程操作与人类远程操作（通过混合现实引导新手）的对比空白。实验在体模上进行，采用受试者内设计，比较了完成时间、位置跟踪精度和力一致性等指标。结果显示，人类远程操作在完成时间和位置精度上与机器人无显著差异（平均差异分别为1.8%和0.5%），但力应用更一致且更低，同时设置更简单、成本更低，更适合小社区应用。

## 核心内容
### 背景与动机
诊断超声广泛使用且成本低，但需要高专业技能，而农村地区缺乏此类专家。远程超声技术包括机器人远程操作和人类远程操作（通过混合现实如HoloLens 2进行手把手引导）。两者此前未被直接比较，人类远程操作可能更实用，但需验证性能是否可比。

### 实验设计
- **设备**：机器人远程操作使用Franka Panda机械臂；人类远程操作中，专家通过HoloLens 2混合现实界面远程指导新手操作。
- **任务**：在体模上进行标准诊断超声扫描。
- **指标**：完成时间、图像空间跟踪精度、施加力的平均值与一致性。
- **统计**：采用受试者内设计，比较两种方式的差异。

### 关键结果
- **完成时间**：人类远程操作与机器人无统计显著差异，平均差异仅1.8%。
- **位置跟踪精度**：两者等效，平均差异0.5%。
- **力应用**：人类远程操作施加的力更一致且更低，表明更稳定。
- **实用性**：人类远程操作设置时间更短、灵活性更高，且成本显著低于机器人系统。

### 结论
人类远程操作在性能上与机器人远程操作相当，但更实用、可及，尤其适合资源有限的小社区。研究建议未来进一步探索混合现实引导的远程超声在真实临床环境中的效果。

## Overview
Diagnostic medical ultrasound is widely used, safe, and relatively low cost but requires a high degree of expertise to acquire and interpret the images. Personnel with this expertise are often not available outside of larger cities, leading to difficult, costly travel and long wait times for rural populations. To address this issue, tele-ultrasound techniques are being developed, including robotic teleoperation and recently human teleoperation, in which a novice user is remotely guided in a hand-over-hand manner through mixed reality to perform an ultrasound exam. These methods have not been compared, and their relative strengths are unknown. Human teleoperation may be more practical than robotics for small communities due to its lower cost and complexity, but this is only relevant if the performance is comparable. This paper therefore evaluates the differences between human and robotic teleoperation, examining practical aspects such as setup time and flexibility and experimentally comparing performance metrics such as completion time, position tracking, and force consistency. It is found that human teleoperation does not lead to statistically significant differences in completion time or position accuracy, with mean differences of 1.8% and 0.5%, respectively, and provides more consistent force application despite being substantially more practical and accessible.

## 参考
- http://arxiv.org/abs/2511.07275v1

## 개요
이 연구는 원격 초음파 진단에서 로봇 원격 조작과 인간 원격 조작(혼합 현실을 통한 초보자 안내) 간의 비교 공백을 다룹니다. 실험은 팬텀(모형)에서 수행되었으며, 피험자 내 설계를 사용하여 완료 시간, 위치 추적 정확도, 힘 일관성 등의 지표를 비교했습니다. 결과에 따르면 인간 원격 조작은 완료 시간과 위치 정확도에서 로봇과 유의미한 차이가 없었으며(평균 차이 각각 1.8% 및 0.5%), 힘 적용은 더 일관되고 낮았으며, 설정이 더 간단하고 비용이 낮아 소규모 지역사회 적용에 더 적합했습니다.

## 핵심 내용
### 배경 및 동기
진단 초음파는 널리 사용되고 비용이 낮지만 높은 전문 기술이 필요하며, 농촌 지역에는 이러한 전문가가 부족합니다. 원격 초음파 기술에는 로봇 원격 조작과 인간 원격 조작(HoloLens 2와 같은 혼합 현실을 통한 직접 안내)이 포함됩니다. 이 둘은 이전에 직접 비교된 적이 없으며, 인간 원격 조작이 더 실용적일 수 있지만 성능이 비교 가능한지 검증이 필요합니다.

### 실험 설계
- **장비**: 로봇 원격 조작은 Franka Panda 로봇 팔을 사용합니다. 인간 원격 조작에서는 전문가가 HoloLens 2 혼합 현실 인터페이스를 통해 초보자를 원격으로 안내합니다.
- **작업**: 팬텀에서 표준 진단 초음파 스캔을 수행합니다.
- **지표**: 완료 시간, 이미지 공간 추적 정확도, 적용된 힘의 평균 및 일관성.
- **통계**: 피험자 내 설계를 사용하여 두 방식의 차이를 비교합니다.

### 주요 결과
- **완료 시간**: 인간 원격 조작은 로봇과 통계적으로 유의미한 차이가 없으며, 평균 차이는 1.8%에 불과합니다.
- **위치 추적 정확도**: 두 방식이 동등하며, 평균 차이는 0.5%입니다.
- **힘 적용**: 인간 원격 조작이 적용하는 힘은 더 일관되고 낮아 더 안정적임을 나타냅니다.
- **실용성**: 인간 원격 조작은 설정 시간이 더 짧고 유연성이 높으며, 비용이 로봇 시스템보다 현저히 낮습니다.

### 결론
인간 원격 조작은 성능 면에서 로봇 원격 조작과 동등하지만 더 실용적이고 접근성이 높아, 특히 자원이 제한된 소규모 지역사회에 적합합니다. 연구는 향후 혼합 현실 안내 원격 초음파의 실제 임상 환경에서의 효과를 추가로 탐구할 것을 제안합니다.

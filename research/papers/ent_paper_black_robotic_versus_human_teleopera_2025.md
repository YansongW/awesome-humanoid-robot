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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.07275v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
진단 의료 초음파는 널리 사용되며 안전하고 비교적 저렴하지만, 영상을 획득하고 해석하는 데 높은 수준의 전문성이 요구됩니다. 이러한 전문성을 갖춘 인력은 대도시 외부에서는 흔히 구할 수 없어, 농촌 인구는 어렵고 비용이 많이 드는 이동과 긴 대기 시간을 겪어야 합니다. 이 문제를 해결하기 위해 원격 초음파 기술이 개발되고 있으며, 여기에는 로봇 원격 조작과 최근에는 혼합 현실을 통해 초보 사용자가 손을 겹쳐 안내받는 방식으로 초음파 검사를 수행하는 인간 원격 조작이 포함됩니다. 이러한 방법들은 비교된 적이 없으며, 각각의 상대적 강점은 알려져 있지 않습니다. 인간 원격 조작은 비용과 복잡성이 낮아 소규모 지역사회에서 로봇보다 더 실용적일 수 있지만, 이는 성능이 비슷할 때만 의미가 있습니다. 따라서 본 논문은 인간과 로봇 원격 조작 간의 차이를 평가하며, 설정 시간과 유연성 같은 실용적 측면을 검토하고, 완료 시간, 위치 추적, 힘 일관성 같은 성능 지표를 실험적으로 비교합니다. 인간 원격 조작은 완료 시간이나 위치 정확도에서 통계적으로 유의미한 차이를 보이지 않으며(각각 평균 차이 1.8%와 0.5%), 상당히 더 실용적이고 접근성이 높음에도 불구하고 더 일관된 힘 적용을 제공한다는 사실이 발견되었습니다.

## 핵심 내용
진단 의료 초음파는 널리 사용되며 안전하고 비교적 저렴하지만, 영상을 획득하고 해석하는 데 높은 수준의 전문성이 요구됩니다. 이러한 전문성을 갖춘 인력은 대도시 외부에서는 흔히 구할 수 없어, 농촌 인구는 어렵고 비용이 많이 드는 이동과 긴 대기 시간을 겪어야 합니다. 이 문제를 해결하기 위해 원격 초음파 기술이 개발되고 있으며, 여기에는 로봇 원격 조작과 최근에는 혼합 현실을 통해 초보 사용자가 손을 겹쳐 안내받는 방식으로 초음파 검사를 수행하는 인간 원격 조작이 포함됩니다. 이러한 방법들은 비교된 적이 없으며, 각각의 상대적 강점은 알려져 있지 않습니다. 인간 원격 조작은 비용과 복잡성이 낮아 소규모 지역사회에서 로봇보다 더 실용적일 수 있지만, 이는 성능이 비슷할 때만 의미가 있습니다. 따라서 본 논문은 인간과 로봇 원격 조작 간의 차이를 평가하며, 설정 시간과 유연성 같은 실용적 측면을 검토하고, 완료 시간, 위치 추적, 힘 일관성 같은 성능 지표를 실험적으로 비교합니다. 인간 원격 조작은 완료 시간이나 위치 정확도에서 통계적으로 유의미한 차이를 보이지 않으며(각각 평균 차이 1.8%와 0.5%), 상당히 더 실용적이고 접근성이 높음에도 불구하고 더 일관된 힘 적용을 제공한다는 사실이 발견되었습니다.

## 参考
- http://arxiv.org/abs/2511.07275v1

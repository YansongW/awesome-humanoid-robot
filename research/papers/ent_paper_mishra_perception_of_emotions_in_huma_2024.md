---
$id: ent_paper_mishra_perception_of_emotions_in_huma_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Perception of Emotions in Human and Robot Faces: Is the Eye Region Enough?'
  zh: 人类与机器人面部的情绪感知：仅眼部区域是否足够？
  ko: '인간과 로봇 얼굴의 감정 인식: 눈 영역만으로 충분한가?'
summary:
  en: This paper reports a between-subjects online user study (N = 305) on how the appearance of robot faces (human-like versus
    mechanical) and the visible face region (full-face versus eye-region-only) influence human recognition of six basic emotions
    plus neutral, using videos of the Furhat robot and a human baseline.
  zh: 本文通过一项在线用户研究（N=305），探讨了机器人面部外观（类人 vs. 机械）和可见面部区域（全脸 vs. 仅眼部）如何影响人类对六种基本情绪及中性情绪识别的能力，以Furhat机器人视频和人类基线为刺激材料。核心贡献在于揭示了机器人面部设计的关键因素：全动画投影面部（无论外观类人或机械）能达到与人类相当的情绪表达水平，而仅显示眼部区域会显著降低识别准确率，但类人特征在眼部受限时能提升识别效果。
  ko: 본 논문은 Furhat 로봇과 인간 기준선 영상을 사용하여 로봇 얼굴 외형(인간형 대 기계형)과 가시적인 얼굴 영역(전체 얼굴 대 눈 영역만)이 6가지 기본 감정과 중립 표정에 대한 인간의 인식에 어떤 영향을
    미치는지 조사한 피험자 간 온라인 사용자 연구(N = 305)를 보고한다.
domains:
- 06_design_engineering
- 02_components
- 11_applications_markets
layers:
- midstream
- upstream
- validation_markets
functional_roles:
- knowledge
tags:
- emotion_recognition
- social_robot
- facial_expression
- human_robot_interaction
- furhat
- face_design
- eye_region
- back_projected_face
- emotion_perception
- user_study
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.14337v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Perception of Emotions in Human and Robot Faces: Is the Eye Region Enough?'
  url: https://arxiv.org/abs/2410.14337
  date: '2024'
  accessed_at: '2026-06-28'
  doi: 10.1007/978-981-96-3522-1_26
theoretical_depth:
- method
---
## 概述
该研究采用被试间设计，让305名参与者观看机器人面部视频（Furhat机器人）和人类基线视频，并识别其中展示的六种基本情绪（快乐、悲伤、愤怒、恐惧、惊讶、厌恶）及中性情绪。实验操控两个自变量：机器人面部外观（类人 vs. 机械）和可见面部区域（全脸 vs. 仅眼部）。结果显示，全动画投影面部（无论外观类人或机械）的情绪表达识别率与人类基线无显著差异；当仅显示眼部区域时，所有条件的识别准确率均下降；但在眼部受限条件下，类人外观的机器人显著优于机械外观。这些发现为社交机器人面部设计提供了实证依据。

## 核心内容
### 方法
- **实验设计**：采用2×2被试间设计，自变量为机器人面部外观（类人 vs. 机械）和可见面部区域（全脸 vs. 仅眼部），另设人类基线条件。
- **刺激材料**：使用Furhat机器人（具备背投全动画面部）生成视频，展示六种基本情绪（快乐、悲伤、愤怒、恐惧、惊讶、厌恶）及中性情绪。人类基线视频由专业演员表演相同情绪。
- **参与者**：共305名在线参与者，随机分配到不同实验条件。

### 结果
- **全脸条件**：类人外观和机械外观的机器人情绪识别准确率均与人类基线无显著差异（p > 0.05），表明全动画投影面部能有效传达情绪。
- **眼部受限条件**：所有条件（人类、类人机器人、机械机器人）的识别准确率均显著低于全脸条件（p < 0.001），平均下降约15-20%。
- **眼部受限下的外观效应**：类人外观机器人（准确率约65%）显著优于机械外观机器人（准确率约52%），差异具有统计学意义（p < 0.01）。

### 结论
- 全动画投影面部（如Furhat）是社交机器人情绪表达的关键技术，其效果不受外观风格（类人或机械）影响。
- 眼部区域对情绪识别至关重要，但仅依赖眼部信息会显著降低识别能力。
- 在面部信息受限时（如仅显示眼部），类人外观设计能部分补偿识别损失，提示HRI设计中应优先考虑类人特征以增强情绪可读性。

## Overview
The increased interest in developing next-gen social robots has raised questions about the factors affecting the perception of robot emotions. This study investigates the impact of robot appearances (humanlike, mechanical) and face regions (full-face, eye-region) on human perception of robot emotions. A between-subjects user study (N = 305) was conducted where participants were asked to identify the emotions being displayed in videos of robot faces, as well as a human baseline. Our findings reveal three important insights for effective social robot face design in Human-Robot Interaction (HRI): Firstly, robots equipped with a back-projected, fully animated face - regardless of whether they are more human-like or more mechanical-looking - demonstrate a capacity for emotional expression comparable to that of humans. Secondly, the recognition accuracy of emotional expressions in both humans and robots declines when only the eye region is visible. Lastly, within the constraint of only the eye region being visible, robots with more human-like features significantly enhance emotion recognition.

## 개요
차세대 소셜 로봇 개발에 대한 관심이 증가하면서 로봇 감정 인식에 영향을 미치는 요인에 대한 의문이 제기되고 있습니다. 본 연구는 로봇의 외형(인간형, 기계형)과 얼굴 영역(전체 얼굴, 눈 영역)이 인간의 로봇 감정 인식에 미치는 영향을 조사합니다. 피험자 간 사용자 연구(N = 305)가 수행되었으며, 참가자들은 로봇 얼굴 영상과 인간 기준 영상에서 표시된 감정을 식별하도록 요청받았습니다. 본 연구 결과는 인간-로봇 상호작용(HRI)에서 효과적인 소셜 로봇 얼굴 디자인을 위한 세 가지 중요한 통찰을 제시합니다: 첫째, 후면 투사 방식의 완전 애니메이션 얼굴을 장착한 로봇은 인간형에 가깝든 기계적 외형이든 관계없이 인간과 유사한 감정 표현 능력을 보여줍니다. 둘째, 눈 영역만 보일 경우 인간과 로봇 모두에서 감정 표현 인식 정확도가 감소합니다. 마지막으로, 눈 영역만 보이는 제한된 조건에서 인간형 특징이 더 많은 로봇은 감정 인식을 크게 향상시킵니다.

## 핵심 내용
차세대 소셜 로봇 개발에 대한 관심이 증가하면서 로봇 감정 인식에 영향을 미치는 요인에 대한 의문이 제기되고 있습니다. 본 연구는 로봇의 외형(인간형, 기계형)과 얼굴 영역(전체 얼굴, 눈 영역)이 인간의 로봇 감정 인식에 미치는 영향을 조사합니다. 피험자 간 사용자 연구(N = 305)가 수행되었으며, 참가자들은 로봇 얼굴 영상과 인간 기준 영상에서 표시된 감정을 식별하도록 요청받았습니다. 본 연구 결과는 인간-로봇 상호작용(HRI)에서 효과적인 소셜 로봇 얼굴 디자인을 위한 세 가지 중요한 통찰을 제시합니다: 첫째, 후면 투사 방식의 완전 애니메이션 얼굴을 장착한 로봇은 인간형에 가깝든 기계적 외형이든 관계없이 인간과 유사한 감정 표현 능력을 보여줍니다. 둘째, 눈 영역만 보일 경우 인간과 로봇 모두에서 감정 표현 인식 정확도가 감소합니다. 마지막으로, 눈 영역만 보이는 제한된 조건에서 인간형 특징이 더 많은 로봇은 감정 인식을 크게 향상시킵니다.

## 参考
- http://arxiv.org/abs/2410.14337v2

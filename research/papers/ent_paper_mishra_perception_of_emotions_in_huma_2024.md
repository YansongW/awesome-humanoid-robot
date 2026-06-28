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
  en: This paper reports a between-subjects online user study (N = 305) on how the
    appearance of robot faces (human-like versus mechanical) and the visible face
    region (full-face versus eye-region-only) influence human recognition of six basic
    emotions plus neutral, using videos of the Furhat robot and a human baseline.
  zh: 本文报告了一项被试间在线用户研究（N = 305），探讨机器人面部外观（类人型与机械型）和可见面部区域（全脸与仅眼部）如何影响人类对六种基本情绪加中性情绪的识别，研究使用了Furhat机器人和人类基线的视频。
  ko: 본 논문은 Furhat 로봇과 인간 기준선 영상을 사용하여 로봇 얼굴 외형(인간형 대 기계형)과 가시적인 얼굴 영역(전체 얼굴 대 눈 영역만)이
    6가지 기본 감정과 중립 표정에 대한 인간의 인식에 어떤 영향을 미치는지 조사한 피험자 간 온라인 사용자 연구(N = 305)를 보고한다.
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
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from the provided metadata, abstract, and method summary; the
    full text was not reviewed, so factual claims should be verified against the original
    paper before promotion.; approved by autonomous review workflow.
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

## Overview

The growing interest in next-generation social robots has made the design of emotionally expressive robot faces a central question in Human-Robot Interaction (HRI). This study examines two design factors that may shape how people read emotions from robot faces: the overall appearance of the face (human-like versus mechanical) and the amount of facial information available (full face versus eye region only). By isolating these factors, the authors aim to provide evidence-based guidance for building cost-effective yet expressive robot faces.

The authors conducted a between-subjects online user study with 305 participants recruited via Prolific. Stimuli were videos of the Furhat robot displaying six basic emotions (anger, disgust, fear, happiness, sadness, surprise) plus neutral. The robot was configured with two characters: a human-like character named Hayden and a mechanical-looking character named Titan. Each character was shown either as a full-face video or as an eye-region-only video. A human baseline condition was also included. Participants were forced to select which emotion they believed was being expressed.

The results indicate that fully animated, back-projected robot faces—whether human-like or mechanical—can convey emotions about as effectively as human faces when the whole face is visible. However, emotion recognition accuracy drops for both humans and robots when only the eye region is shown. Within the eye-region-only condition, human-like robot features significantly improve recognition, although some emotions, such as happiness, remain harder to identify without the mouth region.

## Key Contributions

- Fully animated back-projected robot faces—whether human-like or mechanical—convey emotions as effectively as humans when the full face is visible.
- Emotion recognition declines for both humans and robots when only the eye region is shown.
- When limited to the eye region, more human-like robot features significantly improve emotion recognition.
- Modeling the whole face is preferable to eye-only design to avoid losing critical emotion cues such as the mouth for happiness.

## Relevance to Humanoid Robotics

For humanoid and social robot design, the findings suggest that a fully animated face is sufficient for recognizable emotional expression; there is no need to assume that only highly human-like faces can communicate emotion effectively. This opens the door to simpler, more cost-effective face designs, including mechanical-looking characters, as long as the full face is animated. At the same time, the study warns that eye-only face designs—which are sometimes attractive for hardware simplicity—sacrifice recognition accuracy unless the visible eye region is strongly human-like. Even then, emotions that rely heavily on the mouth, such as happiness, are harder to recognize. These results directly inform component selection and design trade-offs in the face subsystem of humanoid robots.

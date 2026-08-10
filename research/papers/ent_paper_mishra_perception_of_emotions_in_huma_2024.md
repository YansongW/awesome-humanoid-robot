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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.14337v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (855 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2410.14337v2

## 개요
본 연구는 피험자 간 설계를 채택하여 305명의 참가자가 로봇 얼굴 영상(Furhat 로봇)과 인간 기준 영상을 시청하고, 그중에 제시된 여섯 가지 기본 감정(기쁨, 슬픔, 분노, 공포, 놀람, 혐오) 및 중립 감정을 식별하도록 하였습니다. 실험은 두 가지 독립 변수를 조작했습니다: 로봇 얼굴 외관(인간형 vs. 기계형)과 가시적 얼굴 영역(전체 얼굴 vs. 눈 영역만). 결과는 전체 애니메이션 투영 얼굴(외관이 인간형이든 기계형이든)의 감정 표현 식별률이 인간 기준과 유의미한 차이가 없음을 보여주었습니다. 눈 영역만 표시되었을 때는 모든 조건에서 식별 정확도가 감소했습니다. 그러나 눈 영역 제한 조건에서 인간형 외관의 로봇이 기계형 외관보다 유의미하게 우수했습니다. 이러한 발견은 사회적 로봇 얼굴 설계에 실증적 근거를 제공합니다.

## 핵심 내용
### 방법
- **실험 설계**: 2×2 피험자 간 설계를 채택했으며, 독립 변수는 로봇 얼굴 외관(인간형 vs. 기계형)과 가시적 얼굴 영역(전체 얼굴 vs. 눈 영역만)이었고, 인간 기준 조건도 별도로 설정했습니다.
- **자극 재료**: Furhat 로봇(후면 투영 전체 애니메이션 얼굴을 갖춤)을 사용하여 여섯 가지 기본 감정(기쁨, 슬픔, 분노, 공포, 놀람, 혐오) 및 중립 감정을 보여주는 영상을 생성했습니다. 인간 기준 영상은 전문 배우가 동일한 감정을 연기한 것입니다.
- **참가자**: 총 305명의 온라인 참가자가 무작위로 다양한 실험 조건에 배정되었습니다.

### 결과
- **전체 얼굴 조건**: 인간형 외관과 기계형 외관의 로봇 감정 식별 정확도는 모두 인간 기준과 유의미한 차이가 없었습니다(p > 0.05). 이는 전체 애니메이션 투영 얼굴이 감정을 효과적으로 전달할 수 있음을 시사합니다.
- **눈 영역 제한 조건**: 모든 조건(인간, 인간형 로봇, 기계형 로봇)의 식별 정확도는 전체 얼굴 조건보다 유의미하게 낮았습니다(p < 0.001), 평균 약 15-20% 감소했습니다.
- **눈 영역 제한에서의 외관 효과**: 인간형 외관 로봇(정확도 약 65%)이 기계형 외관 로봇(정확도 약 52%)보다 유의미하게 우수했으며, 차이는 통계적으로 유의미했습니다(p < 0.01).

### 결론
- 전체 애니메이션 투영 얼굴(예: Furhat)은 사회적 로봇의 감정 표현에 있어 핵심 기술이며, 그 효과는 외관 스타일(인간형 또는 기계형)에 영향을 받지 않습니다.
- 눈 영역은 감정 식별에 매우 중요하지만, 눈 정보에만 의존하면 식별 능력이 크게 저하됩니다.
- 얼굴 정보가 제한될 때(예: 눈 영역만 표시), 인간형 외관 설계는 식별 손실을 부분적으로 보완할 수 있으며, HRI 설계에서 감정 가독성을 높이기 위해 인간형 특징을 우선적으로 고려해야 함을 시사합니다.

---
$id: ent_paper_yang_x_humanoid_robotize_human_vide_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale'
  zh: X-Humanoid
  ko: 'X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale'
summary:
  en: 'X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale (X-Humanoid), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NUS.'
  zh: 'X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale (X-Humanoid), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NUS.'
  ko: 'X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale (X-Humanoid), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NUS.'
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
- vision_language_action
- vla
- x_humanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.04537v1.
sources:
- id: src_001
  type: paper
  title: 'X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale (arXiv)'
  url: https://arxiv.org/abs/2512.04537
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: X-Humanoid source
  url: https://doi.org/10.48550/arXiv.2512.04537
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The advancement of embodied AI has unlocked significant potential for intelligent humanoid robots. However, progress in both Vision-Language-Action (VLA) models and world models is severely hampered by the scarcity of large-scale, diverse training data. A promising solution is to "robotize" web-scale human videos, which has been proven effective for policy training. However, these solutions mainly "overlay" robot arms to egocentric videos, which cannot handle complex full-body motions and scene occlusions in third-person videos, making them unsuitable for robotizing humans. To bridge this gap, we introduce X-Humanoid, a generative video editing approach that adapts the powerful Wan 2.2 model into a video-to-video structure and finetunes it for the human-to-humanoid translation task. This finetuning requires paired human-humanoid videos, so we designed a scalable data creation pipeline, turning community assets into 17+ hours of paired synthetic videos using Unreal Engine. We then apply our trained model to 60 hours of the Ego-Exo4D videos, generating and releasing a new large-scale dataset of over 3.6 million "robotized" humanoid video frames. Quantitative analysis and user studies confirm our method's superiority over existing baselines: 69% of users rated it best for motion consistency, and 62.1% for embodiment correctness.

## 核心内容
The advancement of embodied AI has unlocked significant potential for intelligent humanoid robots. However, progress in both Vision-Language-Action (VLA) models and world models is severely hampered by the scarcity of large-scale, diverse training data. A promising solution is to "robotize" web-scale human videos, which has been proven effective for policy training. However, these solutions mainly "overlay" robot arms to egocentric videos, which cannot handle complex full-body motions and scene occlusions in third-person videos, making them unsuitable for robotizing humans. To bridge this gap, we introduce X-Humanoid, a generative video editing approach that adapts the powerful Wan 2.2 model into a video-to-video structure and finetunes it for the human-to-humanoid translation task. This finetuning requires paired human-humanoid videos, so we designed a scalable data creation pipeline, turning community assets into 17+ hours of paired synthetic videos using Unreal Engine. We then apply our trained model to 60 hours of the Ego-Exo4D videos, generating and releasing a new large-scale dataset of over 3.6 million "robotized" humanoid video frames. Quantitative analysis and user studies confirm our method's superiority over existing baselines: 69% of users rated it best for motion consistency, and 62.1% for embodiment correctness.

## 参考
- http://arxiv.org/abs/2512.04537v1

## Overview
The advancement of embodied AI has unlocked significant potential for intelligent humanoid robots. However, progress in both Vision-Language-Action (VLA) models and world models is severely hampered by the scarcity of large-scale, diverse training data. A promising solution is to "robotize" web-scale human videos, which has been proven effective for policy training. However, these solutions mainly "overlay" robot arms to egocentric videos, which cannot handle complex full-body motions and scene occlusions in third-person videos, making them unsuitable for robotizing humans. To bridge this gap, we introduce X-Humanoid, a generative video editing approach that adapts the powerful Wan 2.2 model into a video-to-video structure and finetunes it for the human-to-humanoid translation task. This finetuning requires paired human-humanoid videos, so we designed a scalable data creation pipeline, turning community assets into 17+ hours of paired synthetic videos using Unreal Engine. We then apply our trained model to 60 hours of the Ego-Exo4D videos, generating and releasing a new large-scale dataset of over 3.6 million "robotized" humanoid video frames. Quantitative analysis and user studies confirm our method's superiority over existing baselines: 69% of users rated it best for motion consistency, and 62.1% for embodiment correctness.

## Content
The advancement of embodied AI has unlocked significant potential for intelligent humanoid robots. However, progress in both Vision-Language-Action (VLA) models and world models is severely hampered by the scarcity of large-scale, diverse training data. A promising solution is to "robotize" web-scale human videos, which has been proven effective for policy training. However, these solutions mainly "overlay" robot arms to egocentric videos, which cannot handle complex full-body motions and scene occlusions in third-person videos, making them unsuitable for robotizing humans. To bridge this gap, we introduce X-Humanoid, a generative video editing approach that adapts the powerful Wan 2.2 model into a video-to-video structure and finetunes it for the human-to-humanoid translation task. This finetuning requires paired human-humanoid videos, so we designed a scalable data creation pipeline, turning community assets into 17+ hours of paired synthetic videos using Unreal Engine. We then apply our trained model to 60 hours of the Ego-Exo4D videos, generating and releasing a new large-scale dataset of over 3.6 million "robotized" humanoid video frames. Quantitative analysis and user studies confirm our method's superiority over existing baselines: 69% of users rated it best for motion consistency, and 62.1% for embodiment correctness.

## 개요
임베디드 AI의 발전은 지능형 휴머노이드 로봇에 상당한 잠재력을 열어주었습니다. 그러나 Vision-Language-Action(VLA) 모델과 세계 모델 모두의 진전은 대규모의 다양한 훈련 데이터 부족으로 심각하게 저해되고 있습니다. 유망한 해결책은 웹 규모의 인간 비디오를 "로봇화"하는 것으로, 이는 정책 훈련에 효과적임이 입증되었습니다. 그러나 이러한 해결책은 주로 1인칭 비디오에 로봇 팔을 "오버레이"하는 방식으로, 3인칭 비디오에서의 복잡한 전신 동작과 장면 폐색을 처리할 수 없어 인간을 로봇화하는 데 적합하지 않습니다. 이러한 격차를 해소하기 위해 우리는 X-Humanoid를 소개합니다. 이는 강력한 Wan 2.2 모델을 비디오-투-비디오 구조로 변환하고 인간-투-휴머노이드 변환 작업에 미세 조정하는 생성적 비디오 편집 접근 방식입니다. 이 미세 조정에는 쌍을 이루는 인간-휴머노이드 비디오가 필요하므로, 우리는 확장 가능한 데이터 생성 파이프라인을 설계하여 Unreal Engine을 사용해 커뮤니티 자산을 17시간 이상의 쌍을 이루는 합성 비디오로 변환했습니다. 그런 다음 훈련된 모델을 60시간 분량의 Ego-Exo4D 비디오에 적용하여 360만 개 이상의 "로봇화된" 휴머노이드 비디오 프레임으로 구성된 새로운 대규모 데이터셋을 생성하고 공개했습니다. 정량적 분석과 사용자 연구는 기존 기준선에 비해 우리 방법의 우수성을 확인했습니다: 사용자의 69%가 동작 일관성에서 최고라고 평가했으며, 62.1%가 구현 정확성에서 최고라고 평가했습니다.

## 핵심 내용
임베디드 AI의 발전은 지능형 휴머노이드 로봇에 상당한 잠재력을 열어주었습니다. 그러나 Vision-Language-Action(VLA) 모델과 세계 모델 모두의 진전은 대규모의 다양한 훈련 데이터 부족으로 심각하게 저해되고 있습니다. 유망한 해결책은 웹 규모의 인간 비디오를 "로봇화"하는 것으로, 이는 정책 훈련에 효과적임이 입증되었습니다. 그러나 이러한 해결책은 주로 1인칭 비디오에 로봇 팔을 "오버레이"하는 방식으로, 3인칭 비디오에서의 복잡한 전신 동작과 장면 폐색을 처리할 수 없어 인간을 로봇화하는 데 적합하지 않습니다. 이러한 격차를 해소하기 위해 우리는 X-Humanoid를 소개합니다. 이는 강력한 Wan 2.2 모델을 비디오-투-비디오 구조로 변환하고 인간-투-휴머노이드 변환 작업에 미세 조정하는 생성적 비디오 편집 접근 방식입니다. 이 미세 조정에는 쌍을 이루는 인간-휴머노이드 비디오가 필요하므로, 우리는 확장 가능한 데이터 생성 파이프라인을 설계하여 Unreal Engine을 사용해 커뮤니티 자산을 17시간 이상의 쌍을 이루는 합성 비디오로 변환했습니다. 그런 다음 훈련된 모델을 60시간 분량의 Ego-Exo4D 비디오에 적용하여 360만 개 이상의 "로봇화된" 휴머노이드 비디오 프레임으로 구성된 새로운 대규모 데이터셋을 생성하고 공개했습니다. 정량적 분석과 사용자 연구는 기존 기준선에 비해 우리 방법의 우수성을 확인했습니다: 사용자의 69%가 동작 일관성에서 최고라고 평가했으며, 62.1%가 구현 정확성에서 최고라고 평가했습니다.

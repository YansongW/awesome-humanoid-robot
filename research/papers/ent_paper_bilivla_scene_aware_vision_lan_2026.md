---
$id: ent_paper_bilivla_scene_aware_vision_lan_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic Navigation'
  zh: 'BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic Navigation'
  ko: 'BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic Navigation'
summary:
  en: 'arXiv:2606.23531v2 Announce Type: replace Abstract: Endoscopic retrograde cholangiopancreatography (ERCP) demands precise
    endoscopic navigation and stable biliary cannulation within a narrow monocular field characterized by specular reflections,
    partial occlusions, and frequent tissue contact. Although recent robotic systems and vision-based assistance techniques
    improve operator ergonomics and provide perceptual cues, their performance degrades under pronounced anatomical variability
    and safety-critical visual artifacts, which hinders reliable autonomy in cannulation-grade procedures. Here, we present
    BiliVLA, a scene-aware Vision-Language-Action (VLA) framework that formulates biliary endoscopic navigation as an instruction-conditioned
    visuomotor learning problem. Given an endoscopic observation and a stage-specific language instruction, BiliVLA jointly
    predicts the target category, a grounded bounding box, and a discrete three degrees of freedom (DoF) motor command for
    a continuum endoscope. The proposed framework incorporates scene-aware supervision to enhance semantic target consistency
    and safety-aware recovery supervision to induce conservative retreat behaviors under luminal wall contact. A key component
    of BiliVLA is a two-stage training paradigm that combines grounding-enhanced supervised fine-tuning (SFT) with Group Relative
    Policy Optimization (GRPO), which significantly improves action reliability and decision consistency during closed-loop
    navigation. Across three ERCP subtasks, BiliVLA achieves an average action precision of 91.96\% and an overall success
    rate (SR) of 84.85\% in real-world phantom experiments. These results indicate that integrating semantic grounding, scene-aware
    learning, and reward-guided optimization improves perception-action alignment and enables robust autonomous endoscopic
    navigation.'
  zh: 'arXiv:2606.23531v2 Announce Type: replace Abstract: Endoscopic retrograde cholangiopancreatography (ERCP) demands precise
    endoscopic navigation and stable biliary cannulation within a narrow monocular field characterized by specular reflections,
    partial occlusions, and frequent tissue contact. Although recent robotic systems and vision-based assistance techniques
    improve operator ergonomics and provide perceptual cues, their performance degrades under pronounced anatomical variability
    and safety-critical visual artifacts, which hinders reliable autonomy in cannulation-grade procedures. Here, we present
    BiliVLA, a scene-aware Vision-Language-Action (VLA) framework that formulates biliary endoscopic navigation as an instruction-conditioned
    visuomotor learning problem. Given an endoscopic observation and a stage-specific language instruction, BiliVLA jointly
    predicts the target category, a grounded bounding box, and a discrete three degrees of freedom (DoF) motor command for
    a continuum endoscope. The proposed framework incorporates scene-aware supervision to enhance semantic target consistency
    and safety-aware recovery supervision to induce conservative retreat behaviors under luminal wall contact. A key component
    of BiliVLA is a two-stage training paradigm that combines grounding-enhanced supervised fine-tuning (SFT) with Group Relative
    Policy Optimization (GRPO), which significantly improves action reliability and decision consistency during closed-loop
    navigation. Across three ERCP subtasks, BiliVLA achieves an average action precision of 91.96\% and an overall success
    rate (SR) of 84.85\% in real-world phantom experiments. These results indicate that integrating semantic grounding, scene-aware
    learning, and reward-guided optimization improves perception-action alignment and enables robust autonomous endoscopic
    navigation.'
  ko: 'arXiv:2606.23531v2 Announce Type: replace Abstract: Endoscopic retrograde cholangiopancreatography (ERCP) demands precise
    endoscopic navigation and stable biliary cannulation within a narrow monocular field characterized by specular reflections,
    partial occlusions, and frequent tissue contact. Although recent robotic systems and vision-based assistance techniques
    improve operator ergonomics and provide perceptual cues, their performance degrades under pronounced anatomical variability
    and safety-critical visual artifacts, which hinders reliable autonomy in cannulation-grade procedures. Here, we present
    BiliVLA, a scene-aware Vision-Language-Action (VLA) framework that formulates biliary endoscopic navigation as an instruction-conditioned
    visuomotor learning problem. Given an endoscopic observation and a stage-specific language instruction, BiliVLA jointly
    predicts the target category, a grounded bounding box, and a discrete three degrees of freedom (DoF) motor command for
    a continuum endoscope. The proposed framework incorporates scene-aware supervision to enhance semantic target consistency
    and safety-aware recovery supervision to induce conservative retreat behaviors under luminal wall contact. A key component
    of BiliVLA is a two-stage training paradigm that combines grounding-enhanced supervised fine-tuning (SFT) with Group Relative
    Policy Optimization (GRPO), which significantly improves action reliability and decision consistency during closed-loop
    navigation. Across three ERCP subtasks, BiliVLA achieves an average action precision of 91.96\% and an overall success
    rate (SR) of 84.85\% in real-world phantom experiments. These results indicate that integrating semantic grounding, scene-aware
    learning, and reward-guided optimization improves perception-action alignment and enables robust autonomous endoscopic
    navigation.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- bilivla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.23531v3.
sources:
- id: src_001
  type: paper
  title: 'BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic
    Navigation (arXiv)'
  url: https://arxiv.org/abs/2606.23531
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
Endoscopic retrograde cholangiopancreatography (ERCP) demands precise endoscopic navigation and stable biliary cannulation within a narrow monocular field characterized by specular reflections, partial occlusions, and frequent tissue contact. Although recent robotic systems and vision-based assistance techniques improve operator ergonomics and provide perceptual cues, their performance degrades under pronounced anatomical variability and safety-critical visual artifacts, which hinders reliable autonomy in cannulation-grade procedures. Here, we present BiliVLA, a scene-aware Vision-Language-Action (VLA) framework that formulates biliary endoscopic navigation as an instruction-conditioned visuomotor learning problem. Given an endoscopic observation and a stage-specific language instruction, BiliVLA jointly predicts the target category, a grounded bounding box, and a discrete three-degree-of-freedom (3-DoF) motor command for a continuum endoscope. The proposed framework incorporates scene-aware supervision to improve semantic target consistency and safety-aware recovery supervision to induce conservative retreat behaviors under luminal wall contact. A key component of BiliVLA is a two-stage training paradigm that combines grounding-enhanced supervised fine-tuning (SFT) with Group Relative Policy Optimization (GRPO), thereby improving action reliability and decision consistency during closed-loop navigation. Across three ERCP subtasks, BiliVLA achieves the best overall performance in physical phantom experiments, with a total mIoU of 0.9625, an overall action precision of 91.96\%, and an overall success rate (SR) of 84.85\%. These results indicate that integrating semantic grounding, scene-aware learning, and reward-guided optimization strengthens perception--action alignment and enables more robust autonomous biliary endoscopic navigation.

## 核心内容
Endoscopic retrograde cholangiopancreatography (ERCP) demands precise endoscopic navigation and stable biliary cannulation within a narrow monocular field characterized by specular reflections, partial occlusions, and frequent tissue contact. Although recent robotic systems and vision-based assistance techniques improve operator ergonomics and provide perceptual cues, their performance degrades under pronounced anatomical variability and safety-critical visual artifacts, which hinders reliable autonomy in cannulation-grade procedures. Here, we present BiliVLA, a scene-aware Vision-Language-Action (VLA) framework that formulates biliary endoscopic navigation as an instruction-conditioned visuomotor learning problem. Given an endoscopic observation and a stage-specific language instruction, BiliVLA jointly predicts the target category, a grounded bounding box, and a discrete three-degree-of-freedom (3-DoF) motor command for a continuum endoscope. The proposed framework incorporates scene-aware supervision to improve semantic target consistency and safety-aware recovery supervision to induce conservative retreat behaviors under luminal wall contact. A key component of BiliVLA is a two-stage training paradigm that combines grounding-enhanced supervised fine-tuning (SFT) with Group Relative Policy Optimization (GRPO), thereby improving action reliability and decision consistency during closed-loop navigation. Across three ERCP subtasks, BiliVLA achieves the best overall performance in physical phantom experiments, with a total mIoU of 0.9625, an overall action precision of 91.96\%, and an overall success rate (SR) of 84.85\%. These results indicate that integrating semantic grounding, scene-aware learning, and reward-guided optimization strengthens perception--action alignment and enables more robust autonomous biliary endoscopic navigation.

## 参考
- http://arxiv.org/abs/2606.23531v3

## Overview
Endoscopic retrograde cholangiopancreatography (ERCP) demands precise endoscopic navigation and stable biliary cannulation within a narrow monocular field characterized by specular reflections, partial occlusions, and frequent tissue contact. Although recent robotic systems and vision-based assistance techniques improve operator ergonomics and provide perceptual cues, their performance degrades under pronounced anatomical variability and safety-critical visual artifacts, which hinders reliable autonomy in cannulation-grade procedures. Here, we present BiliVLA, a scene-aware Vision-Language-Action (VLA) framework that formulates biliary endoscopic navigation as an instruction-conditioned visuomotor learning problem. Given an endoscopic observation and a stage-specific language instruction, BiliVLA jointly predicts the target category, a grounded bounding box, and a discrete three-degree-of-freedom (3-DoF) motor command for a continuum endoscope. The proposed framework incorporates scene-aware supervision to improve semantic target consistency and safety-aware recovery supervision to induce conservative retreat behaviors under luminal wall contact. A key component of BiliVLA is a two-stage training paradigm that combines grounding-enhanced supervised fine-tuning (SFT) with Group Relative Policy Optimization (GRPO), thereby improving action reliability and decision consistency during closed-loop navigation. Across three ERCP subtasks, BiliVLA achieves the best overall performance in physical phantom experiments, with a total mIoU of 0.9625, an overall action precision of 91.96\%, and an overall success rate (SR) of 84.85\%. These results indicate that integrating semantic grounding, scene-aware learning, and reward-guided optimization strengthens perception--action alignment and enables more robust autonomous biliary endoscopic navigation.

## Content
Endoscopic retrograde cholangiopancreatography (ERCP) demands precise endoscopic navigation and stable biliary cannulation within a narrow monocular field characterized by specular reflections, partial occlusions, and frequent tissue contact. Although recent robotic systems and vision-based assistance techniques improve operator ergonomics and provide perceptual cues, their performance degrades under pronounced anatomical variability and safety-critical visual artifacts, which hinders reliable autonomy in cannulation-grade procedures. Here, we present BiliVLA, a scene-aware Vision-Language-Action (VLA) framework that formulates biliary endoscopic navigation as an instruction-conditioned visuomotor learning problem. Given an endoscopic observation and a stage-specific language instruction, BiliVLA jointly predicts the target category, a grounded bounding box, and a discrete three-degree-of-freedom (3-DoF) motor command for a continuum endoscope. The proposed framework incorporates scene-aware supervision to improve semantic target consistency and safety-aware recovery supervision to induce conservative retreat behaviors under luminal wall contact. A key component of BiliVLA is a two-stage training paradigm that combines grounding-enhanced supervised fine-tuning (SFT) with Group Relative Policy Optimization (GRPO), thereby improving action reliability and decision consistency during closed-loop navigation. Across three ERCP subtasks, BiliVLA achieves the best overall performance in physical phantom experiments, with a total mIoU of 0.9625, an overall action precision of 91.96\%, and an overall success rate (SR) of 84.85\%. These results indicate that integrating semantic grounding, scene-aware learning, and reward-guided optimization strengthens perception--action alignment and enables more robust autonomous biliary endoscopic navigation.

## 개요
내시경 역행성 담췌관 조영술(ERCP)은 정반사, 부분 폐색, 빈번한 조직 접촉이 특징적인 좁은 단안 시야 내에서 정밀한 내시경 탐색과 안정적인 담관 삽관을 요구합니다. 최근의 로봇 시스템과 시각 기반 보조 기술은 시술자의 인체공학을 개선하고 지각적 단서를 제공하지만, 뚜렷한 해부학적 변이와 안전에 치명적인 시각적 인공물이 있는 환경에서는 성능이 저하되어 삽관 수준 시술에서 신뢰할 수 있는 자율성을 저해합니다. 본 연구에서는 담도 내시경 탐색을 명령 조건부 시각운동 학습 문제로 정식화하는 장면 인식형 Vision-Language-Action (VLA) 프레임워크인 BiliVLA를 제시합니다. 내시경 관찰 결과와 단계별 언어 명령이 주어지면 BiliVLA는 대상 범주, 근거 기반 경계 상자, 그리고 연속체 내시경을 위한 이산적인 3자유도(3-DoF) 모터 명령을 공동으로 예측합니다. 제안된 프레임워크는 장면 인식형 감독을 통합하여 의미론적 대상 일관성을 개선하고, 안전 인식형 복구 감독을 도입하여 내강 벽 접촉 시 보수적인 후퇴 행동을 유도합니다. BiliVLA의 핵심 구성 요소는 근거 강화 지도 미세 조정(SFT)과 그룹 상대 정책 최적화(GRPO)를 결합한 2단계 훈련 패러다임으로, 폐쇄 루프 탐색 중 행동 신뢰성과 결정 일관성을 향상시킵니다. 세 가지 ERCP 하위 작업에서 BiliVLA는 물리적 팬텀 실험에서 총 mIoU 0.9625, 전체 행동 정밀도 91.96%, 전체 성공률(SR) 84.85%로 최고의 전반적 성능을 달성했습니다. 이러한 결과는 의미론적 근거 기반 학습, 장면 인식형 학습, 보상 기반 최적화의 통합이 지각-행동 정렬을 강화하고 더 강력한 자율 담도 내시경 탐색을 가능하게 함을 시사합니다.

## 핵심 내용
내시경 역행성 담췌관 조영술(ERCP)은 정반사, 부분 폐색, 빈번한 조직 접촉이 특징적인 좁은 단안 시야 내에서 정밀한 내시경 탐색과 안정적인 담관 삽관을 요구합니다. 최근의 로봇 시스템과 시각 기반 보조 기술은 시술자의 인체공학을 개선하고 지각적 단서를 제공하지만, 뚜렷한 해부학적 변이와 안전에 치명적인 시각적 인공물이 있는 환경에서는 성능이 저하되어 삽관 수준 시술에서 신뢰할 수 있는 자율성을 저해합니다. 본 연구에서는 담도 내시경 탐색을 명령 조건부 시각운동 학습 문제로 정식화하는 장면 인식형 Vision-Language-Action (VLA) 프레임워크인 BiliVLA를 제시합니다. 내시경 관찰 결과와 단계별 언어 명령이 주어지면 BiliVLA는 대상 범주, 근거 기반 경계 상자, 그리고 연속체 내시경을 위한 이산적인 3자유도(3-DoF) 모터 명령을 공동으로 예측합니다. 제안된 프레임워크는 장면 인식형 감독을 통합하여 의미론적 대상 일관성을 개선하고, 안전 인식형 복구 감독을 도입하여 내강 벽 접촉 시 보수적인 후퇴 행동을 유도합니다. BiliVLA의 핵심 구성 요소는 근거 강화 지도 미세 조정(SFT)과 그룹 상대 정책 최적화(GRPO)를 결합한 2단계 훈련 패러다임으로, 폐쇄 루프 탐색 중 행동 신뢰성과 결정 일관성을 향상시킵니다. 세 가지 ERCP 하위 작업에서 BiliVLA는 물리적 팬텀 실험에서 총 mIoU 0.9625, 전체 행동 정밀도 91.96%, 전체 성공률(SR) 84.85%로 최고의 전반적 성능을 달성했습니다. 이러한 결과는 의미론적 근거 기반 학습, 장면 인식형 학습, 보상 기반 최적화의 통합이 지각-행동 정렬을 강화하고 더 강력한 자율 담도 내시경 탐색을 가능하게 함을 시사합니다.

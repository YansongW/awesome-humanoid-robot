---
$id: ent_paper_shen_videovla_video_generators_can_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VideoVLA: Video Generators Can Be Generalizable Robot Manipulators'
  zh: VideoVLA
  ko: 'VideoVLA: Video Generators Can Be Generalizable Robot Manipulators'
summary:
  en: 'VideoVLA: Video Generators Can Be Generalizable Robot Manipulators (VideoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by IAIR, Xi’an Jiaotong University, Microsoft Research Asia, Fudan University,
    and published at NIPS25.'
  zh: 'VideoVLA: Video Generators Can Be Generalizable Robot Manipulators (VideoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by IAIR, Xi’an Jiaotong University, Microsoft Research Asia, Fudan University,
    and published at NIPS25.'
  ko: 'VideoVLA: Video Generators Can Be Generalizable Robot Manipulators (VideoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by IAIR, Xi’an Jiaotong University, Microsoft Research Asia, Fudan University,
    and published at NIPS25.'
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
- videovla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.06963v1.
sources:
- id: src_001
  type: paper
  title: 'VideoVLA: Video Generators Can Be Generalizable Robot Manipulators (arXiv)'
  url: https://arxiv.org/abs/2512.06963
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VideoVLA source
  url: https://doi.org/10.48550/arXiv.2512.06963
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Generalization in robot manipulation is essential for deploying robots in open-world environments and advancing toward artificial general intelligence. While recent Vision-Language-Action (VLA) models leverage large pre-trained understanding models for perception and instruction following, their ability to generalize to novel tasks, objects, and settings remains limited. In this work, we present VideoVLA, a simple approach that explores the potential of transforming large video generation models into robotic VLA manipulators. Given a language instruction and an image, VideoVLA predicts an action sequence as well as the future visual outcomes. Built on a multi-modal Diffusion Transformer, VideoVLA jointly models video, language, and action modalities, using pre-trained video generative models for joint visual and action forecasting. Our experiments show that high-quality imagined futures correlate with reliable action predictions and task success, highlighting the importance of visual imagination in manipulation. VideoVLA demonstrates strong generalization, including imitating other embodiments' skills and handling novel objects. This dual-prediction strategy - forecasting both actions and their visual consequences - explores a paradigm shift in robot learning and unlocks generalization capabilities in manipulation systems.

## 核心内容
Generalization in robot manipulation is essential for deploying robots in open-world environments and advancing toward artificial general intelligence. While recent Vision-Language-Action (VLA) models leverage large pre-trained understanding models for perception and instruction following, their ability to generalize to novel tasks, objects, and settings remains limited. In this work, we present VideoVLA, a simple approach that explores the potential of transforming large video generation models into robotic VLA manipulators. Given a language instruction and an image, VideoVLA predicts an action sequence as well as the future visual outcomes. Built on a multi-modal Diffusion Transformer, VideoVLA jointly models video, language, and action modalities, using pre-trained video generative models for joint visual and action forecasting. Our experiments show that high-quality imagined futures correlate with reliable action predictions and task success, highlighting the importance of visual imagination in manipulation. VideoVLA demonstrates strong generalization, including imitating other embodiments' skills and handling novel objects. This dual-prediction strategy - forecasting both actions and their visual consequences - explores a paradigm shift in robot learning and unlocks generalization capabilities in manipulation systems.

## 参考
- http://arxiv.org/abs/2512.06963v1

## Overview
Generalization in robot manipulation is essential for deploying robots in open-world environments and advancing toward artificial general intelligence. While recent Vision-Language-Action (VLA) models leverage large pre-trained understanding models for perception and instruction following, their ability to generalize to novel tasks, objects, and settings remains limited. In this work, we present VideoVLA, a simple approach that explores the potential of transforming large video generation models into robotic VLA manipulators. Given a language instruction and an image, VideoVLA predicts an action sequence as well as the future visual outcomes. Built on a multi-modal Diffusion Transformer, VideoVLA jointly models video, language, and action modalities, using pre-trained video generative models for joint visual and action forecasting. Our experiments show that high-quality imagined futures correlate with reliable action predictions and task success, highlighting the importance of visual imagination in manipulation. VideoVLA demonstrates strong generalization, including imitating other embodiments' skills and handling novel objects. This dual-prediction strategy - forecasting both actions and their visual consequences - explores a paradigm shift in robot learning and unlocks generalization capabilities in manipulation systems.

## Content
Generalization in robot manipulation is essential for deploying robots in open-world environments and advancing toward artificial general intelligence. While recent Vision-Language-Action (VLA) models leverage large pre-trained understanding models for perception and instruction following, their ability to generalize to novel tasks, objects, and settings remains limited. In this work, we present VideoVLA, a simple approach that explores the potential of transforming large video generation models into robotic VLA manipulators. Given a language instruction and an image, VideoVLA predicts an action sequence as well as the future visual outcomes. Built on a multi-modal Diffusion Transformer, VideoVLA jointly models video, language, and action modalities, using pre-trained video generative models for joint visual and action forecasting. Our experiments show that high-quality imagined futures correlate with reliable action predictions and task success, highlighting the importance of visual imagination in manipulation. VideoVLA demonstrates strong generalization, including imitating other embodiments' skills and handling novel objects. This dual-prediction strategy - forecasting both actions and their visual consequences - explores a paradigm shift in robot learning and unlocks generalization capabilities in manipulation systems.

## 개요
로봇 조작에서의 일반화는 개방형 환경에서 로봇을 배치하고 인공 일반 지능으로 나아가는 데 필수적입니다. 최근 Vision-Language-Action(VLA) 모델은 대규모 사전 학습된 이해 모델을 활용하여 인식 및 명령 수행을 수행하지만, 새로운 작업, 객체 및 환경에 대한 일반화 능력은 여전히 제한적입니다. 본 연구에서는 대규모 비디오 생성 모델을 로봇 VLA 조작기로 변환하는 잠재력을 탐구하는 간단한 접근 방식인 VideoVLA를 제시합니다. 언어 명령과 이미지가 주어지면 VideoVLA는 행동 시퀀스와 미래 시각적 결과를 예측합니다. 다중 모달 Diffusion Transformer를 기반으로 구축된 VideoVLA는 비디오, 언어 및 행동 모달리티를 공동으로 모델링하며, 사전 학습된 비디오 생성 모델을 사용하여 시각 및 행동 예측을 통합합니다. 실험 결과, 고품질의 상상된 미래가 신뢰할 수 있는 행동 예측 및 작업 성공과 상관관계가 있음을 보여주며, 조작에서 시각적 상상력의 중요성을 강조합니다. VideoVLA는 다른 체화 기술 모방 및 새로운 객체 처리 등 강력한 일반화 능력을 입증합니다. 이 이중 예측 전략(행동과 그 시각적 결과를 모두 예측)은 로봇 학습의 패러다임 전환을 탐구하고 조작 시스템에서 일반화 능력을 해제합니다.

## 핵심 내용
로봇 조작에서의 일반화는 개방형 환경에서 로봇을 배치하고 인공 일반 지능으로 나아가는 데 필수적입니다. 최근 Vision-Language-Action(VLA) 모델은 대규모 사전 학습된 이해 모델을 활용하여 인식 및 명령 수행을 수행하지만, 새로운 작업, 객체 및 환경에 대한 일반화 능력은 여전히 제한적입니다. 본 연구에서는 대규모 비디오 생성 모델을 로봇 VLA 조작기로 변환하는 잠재력을 탐구하는 간단한 접근 방식인 VideoVLA를 제시합니다. 언어 명령과 이미지가 주어지면 VideoVLA는 행동 시퀀스와 미래 시각적 결과를 예측합니다. 다중 모달 Diffusion Transformer를 기반으로 구축된 VideoVLA는 비디오, 언어 및 행동 모달리티를 공동으로 모델링하며, 사전 학습된 비디오 생성 모델을 사용하여 시각 및 행동 예측을 통합합니다. 실험 결과, 고품질의 상상된 미래가 신뢰할 수 있는 행동 예측 및 작업 성공과 상관관계가 있음을 보여주며, 조작에서 시각적 상상력의 중요성을 강조합니다. VideoVLA는 다른 체화 기술 모방 및 새로운 객체 처리 등 강력한 일반화 능력을 입증합니다. 이 이중 예측 전략(행동과 그 시각적 결과를 모두 예측)은 로봇 학습의 패러다임 전환을 탐구하고 조작 시스템에서 일반화 능력을 해제합니다.

---
$id: ent_paper_guzey_dexterity_from_smart_lenses_mu_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Dexterity from Smart Lenses: Multi-Fingered Robot Manipulation with In-the-Wild Human Demonstrations'
  zh: AINA
  ko: 'Dexterity from Smart Lenses: Multi-Fingered Robot Manipulation with In-the-Wild Human Demonstrations'
summary:
  en: 'Dexterity from Smart Lenses: Multi-Fingered Robot Manipulation with In-the-Wild Human Demonstrations (AINA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by New York University, Meta.'
  zh: 'Dexterity from Smart Lenses: Multi-Fingered Robot Manipulation with In-the-Wild Human Demonstrations (AINA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by New York University, Meta.'
  ko: 'Dexterity from Smart Lenses: Multi-Fingered Robot Manipulation with In-the-Wild Human Demonstrations (AINA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by New York University, Meta.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- aina
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.16661v1.
sources:
- id: src_001
  type: paper
  title: 'Dexterity from Smart Lenses: Multi-Fingered Robot Manipulation with In-the-Wild Human Demonstrations (arXiv)'
  url: https://arxiv.org/abs/2511.16661
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: AINA source
  url: https://doi.org/10.48550/arXiv.2511.16661
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Learning multi-fingered robot policies from humans performing daily tasks in natural environments has long been a grand goal in the robotics community. Achieving this would mark significant progress toward generalizable robot manipulation in human environments, as it would reduce the reliance on labor-intensive robot data collection. Despite substantial efforts, progress toward this goal has been bottle-necked by the embodiment gap between humans and robots, as well as by difficulties in extracting relevant contextual and motion cues that enable learning of autonomous policies from in-the-wild human videos. We claim that with simple yet sufficiently powerful hardware for obtaining human data and our proposed framework AINA, we are now one significant step closer to achieving this dream. AINA enables learning multi-fingered policies from data collected by anyone, anywhere, and in any environment using Aria Gen 2 glasses. These glasses are lightweight and portable, feature a high-resolution RGB camera, provide accurate on-board 3D head and hand poses, and offer a wide stereo view that can be leveraged for depth estimation of the scene. This setup enables the learning of 3D point-based policies for multi-fingered hands that are robust to background changes and can be deployed directly without requiring any robot data (including online corrections, reinforcement learning, or simulation). We compare our framework against prior human-to-robot policy learning approaches, ablate our design choices, and demonstrate results across nine everyday manipulation tasks. Robot rollouts are best viewed on our website: https://aina-robot.github.io.

## 核心内容
Learning multi-fingered robot policies from humans performing daily tasks in natural environments has long been a grand goal in the robotics community. Achieving this would mark significant progress toward generalizable robot manipulation in human environments, as it would reduce the reliance on labor-intensive robot data collection. Despite substantial efforts, progress toward this goal has been bottle-necked by the embodiment gap between humans and robots, as well as by difficulties in extracting relevant contextual and motion cues that enable learning of autonomous policies from in-the-wild human videos. We claim that with simple yet sufficiently powerful hardware for obtaining human data and our proposed framework AINA, we are now one significant step closer to achieving this dream. AINA enables learning multi-fingered policies from data collected by anyone, anywhere, and in any environment using Aria Gen 2 glasses. These glasses are lightweight and portable, feature a high-resolution RGB camera, provide accurate on-board 3D head and hand poses, and offer a wide stereo view that can be leveraged for depth estimation of the scene. This setup enables the learning of 3D point-based policies for multi-fingered hands that are robust to background changes and can be deployed directly without requiring any robot data (including online corrections, reinforcement learning, or simulation). We compare our framework against prior human-to-robot policy learning approaches, ablate our design choices, and demonstrate results across nine everyday manipulation tasks. Robot rollouts are best viewed on our website: https://aina-robot.github.io.

## 参考
- http://arxiv.org/abs/2511.16661v1

## Overview
Learning multi-fingered robot policies from humans performing daily tasks in natural environments has long been a grand goal in the robotics community. Achieving this would mark significant progress toward generalizable robot manipulation in human environments, as it would reduce the reliance on labor-intensive robot data collection. Despite substantial efforts, progress toward this goal has been bottle-necked by the embodiment gap between humans and robots, as well as by difficulties in extracting relevant contextual and motion cues that enable learning of autonomous policies from in-the-wild human videos. We claim that with simple yet sufficiently powerful hardware for obtaining human data and our proposed framework AINA, we are now one significant step closer to achieving this dream. AINA enables learning multi-fingered policies from data collected by anyone, anywhere, and in any environment using Aria Gen 2 glasses. These glasses are lightweight and portable, feature a high-resolution RGB camera, provide accurate on-board 3D head and hand poses, and offer a wide stereo view that can be leveraged for depth estimation of the scene. This setup enables the learning of 3D point-based policies for multi-fingered hands that are robust to background changes and can be deployed directly without requiring any robot data (including online corrections, reinforcement learning, or simulation). We compare our framework against prior human-to-robot policy learning approaches, ablate our design choices, and demonstrate results across nine everyday manipulation tasks. Robot rollouts are best viewed on our website: https://aina-robot.github.io.

## Content
Learning multi-fingered robot policies from humans performing daily tasks in natural environments has long been a grand goal in the robotics community. Achieving this would mark significant progress toward generalizable robot manipulation in human environments, as it would reduce the reliance on labor-intensive robot data collection. Despite substantial efforts, progress toward this goal has been bottle-necked by the embodiment gap between humans and robots, as well as by difficulties in extracting relevant contextual and motion cues that enable learning of autonomous policies from in-the-wild human videos. We claim that with simple yet sufficiently powerful hardware for obtaining human data and our proposed framework AINA, we are now one significant step closer to achieving this dream. AINA enables learning multi-fingered policies from data collected by anyone, anywhere, and in any environment using Aria Gen 2 glasses. These glasses are lightweight and portable, feature a high-resolution RGB camera, provide accurate on-board 3D head and hand poses, and offer a wide stereo view that can be leveraged for depth estimation of the scene. This setup enables the learning of 3D point-based policies for multi-fingered hands that are robust to background changes and can be deployed directly without requiring any robot data (including online corrections, reinforcement learning, or simulation). We compare our framework against prior human-to-robot policy learning approaches, ablate our design choices, and demonstrate results across nine everyday manipulation tasks. Robot rollouts are best viewed on our website: https://aina-robot.github.io.

## 개요
일상 환경에서 인간이 수행하는 작업을 통해 다지 로봇 정책을 학습하는 것은 로봇 공학 커뮤니티의 오랜 큰 목표였습니다. 이를 달성하면 인간 환경에서 일반화 가능한 로봇 조작을 향한 중요한 진전이 될 것이며, 노동 집약적인 로봇 데이터 수집에 대한 의존도를 줄일 수 있습니다. 상당한 노력에도 불구하고, 이 목표를 향한 진전은 인간과 로봇 간의 구현 격차(embodiment gap)와 야생 인간 비디오에서 자율 정책 학습을 가능하게 하는 관련 맥락 및 동작 신호를 추출하는 어려움으로 인해 병목 현상을 겪어 왔습니다. 우리는 인간 데이터를 얻기 위한 간단하면서도 충분히 강력한 하드웨어와 제안된 프레임워크 AINA를 통해 이 꿈에 한 걸음 더 가까워졌다고 주장합니다. AINA는 Aria Gen 2 안경을 사용하여 누구나, 어디서나, 어떤 환경에서든 수집된 데이터로부터 다지 정책을 학습할 수 있게 합니다. 이 안경은 가볍고 휴대 가능하며, 고해상도 RGB 카메라를 갖추고, 정확한 온보드 3D 머리 및 손 포즈를 제공하며, 장면의 깊이 추정에 활용할 수 있는 넓은 스테레오 뷰를 제공합니다. 이 설정은 배경 변화에 강건하고, 로봇 데이터(온라인 보정, 강화 학습 또는 시뮬레이션 포함) 없이 직접 배포할 수 있는 다지 손을 위한 3D 포인트 기반 정책 학습을 가능하게 합니다. 우리는 프레임워크를 이전의 인간-로봇 정책 학습 접근 방식과 비교하고, 설계 선택을 분석하며, 9가지 일상 조작 작업에 걸친 결과를 시연합니다. 로봇 롤아웃은 웹사이트 https://aina-robot.github.io 에서 가장 잘 확인할 수 있습니다.

## 핵심 내용
일상 환경에서 인간이 수행하는 작업을 통해 다지 로봇 정책을 학습하는 것은 로봇 공학 커뮤니티의 오랜 큰 목표였습니다. 이를 달성하면 인간 환경에서 일반화 가능한 로봇 조작을 향한 중요한 진전이 될 것이며, 노동 집약적인 로봇 데이터 수집에 대한 의존도를 줄일 수 있습니다. 상당한 노력에도 불구하고, 이 목표를 향한 진전은 인간과 로봇 간의 구현 격차(embodiment gap)와 야생 인간 비디오에서 자율 정책 학습을 가능하게 하는 관련 맥락 및 동작 신호를 추출하는 어려움으로 인해 병목 현상을 겪어 왔습니다. 우리는 인간 데이터를 얻기 위한 간단하면서도 충분히 강력한 하드웨어와 제안된 프레임워크 AINA를 통해 이 꿈에 한 걸음 더 가까워졌다고 주장합니다. AINA는 Aria Gen 2 안경을 사용하여 누구나, 어디서나, 어떤 환경에서든 수집된 데이터로부터 다지 정책을 학습할 수 있게 합니다. 이 안경은 가볍고 휴대 가능하며, 고해상도 RGB 카메라를 갖추고, 정확한 온보드 3D 머리 및 손 포즈를 제공하며, 장면의 깊이 추정에 활용할 수 있는 넓은 스테레오 뷰를 제공합니다. 이 설정은 배경 변화에 강건하고, 로봇 데이터(온라인 보정, 강화 학습 또는 시뮬레이션 포함) 없이 직접 배포할 수 있는 다지 손을 위한 3D 포인트 기반 정책 학습을 가능하게 합니다. 우리는 프레임워크를 이전의 인간-로봇 정책 학습 접근 방식과 비교하고, 설계 선택을 분석하며, 9가지 일상 조작 작업에 걸친 결과를 시연합니다. 로봇 롤아웃은 웹사이트 https://aina-robot.github.io 에서 가장 잘 확인할 수 있습니다.

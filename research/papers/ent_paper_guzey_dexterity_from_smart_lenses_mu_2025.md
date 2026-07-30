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
  zh: AINA 是由纽约大学和 Meta 于 2025 年提出的大型视觉-语言-动作模型，用于多指机器人操控。其核心贡献在于利用 Aria Gen 2 智能眼镜采集的野外人类演示数据，无需任何机器人数据即可直接学习鲁棒的多指操控策略，并在九项日常任务中验证了有效性。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.16661v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
AINA 旨在解决从人类自然环境中执行日常任务的数据中学习多指机器人策略的长期目标。该框架通过使用轻量便携的 Aria Gen 2 智能眼镜，获取高分辨率 RGB 图像、精确的 3D 头部和手部姿态以及宽立体视图，从而克服了人类与机器人之间的具身鸿沟。AINA 能够学习基于 3D 点的多指手策略，对背景变化具有鲁棒性，且无需任何机器人数据（包括在线校正、强化学习或仿真）。实验在九项日常操控任务中展示了其性能，并与先前的人到机器人策略学习方法进行了对比。

## 核心内容
### 方法
- AINA 采用大型视觉-语言-动作模型架构，从 Aria Gen 2 眼镜采集的野外人类视频中提取上下文和运动线索。
- 利用眼镜提供的精确 3D 头部和手部姿态，以及宽立体视图进行深度估计，从而学习 3D 点云表示的多指策略。

### 实验设置
- 数据采集：使用 Aria Gen 2 眼镜，由任意人员在任意环境中收集人类演示数据。
- 任务：涵盖九项日常操控任务，包括抓取、放置、旋转等。
- 对比基线：与先前的人到机器人策略学习方法（如行为克隆、模仿学习）进行对比。
- 消融实验：对设计选择（如是否使用 3D 点云、是否依赖深度估计）进行消融分析。

### 关键数字
- 无需任何机器人数据：包括在线校正、强化学习或仿真。
- 九项日常操控任务：展示了策略的泛化能力。
- 鲁棒性：对背景变化具有鲁棒性，可直接部署。

### 结论
- AINA 显著推进了从野外人类视频学习多指机器人策略的目标，减少了对手工机器人数据收集的依赖。
- 通过简单且强大的硬件（Aria Gen 2 眼镜）和提出的框架，实现了从任意环境数据到直接部署的策略学习。

## Overview
Learning multi-fingered robot policies from humans performing daily tasks in natural environments has long been a grand goal in the robotics community. Achieving this would mark significant progress toward generalizable robot manipulation in human environments, as it would reduce the reliance on labor-intensive robot data collection. Despite substantial efforts, progress toward this goal has been bottle-necked by the embodiment gap between humans and robots, as well as by difficulties in extracting relevant contextual and motion cues that enable learning of autonomous policies from in-the-wild human videos. We claim that with simple yet sufficiently powerful hardware for obtaining human data and our proposed framework AINA, we are now one significant step closer to achieving this dream. AINA enables learning multi-fingered policies from data collected by anyone, anywhere, and in any environment using Aria Gen 2 glasses. These glasses are lightweight and portable, feature a high-resolution RGB camera, provide accurate on-board 3D head and hand poses, and offer a wide stereo view that can be leveraged for depth estimation of the scene. This setup enables the learning of 3D point-based policies for multi-fingered hands that are robust to background changes and can be deployed directly without requiring any robot data (including online corrections, reinforcement learning, or simulation). We compare our framework against prior human-to-robot policy learning approaches, ablate our design choices, and demonstrate results across nine everyday manipulation tasks. Robot rollouts are best viewed on our website: https://aina-robot.github.io.

## 개요
일상 환경에서 인간이 수행하는 작업을 통해 다지 로봇 정책을 학습하는 것은 로봇 공학 커뮤니티의 오랜 큰 목표였습니다. 이를 달성하면 인간 환경에서 일반화 가능한 로봇 조작을 향한 중요한 진전이 될 것이며, 노동 집약적인 로봇 데이터 수집에 대한 의존도를 줄일 수 있습니다. 상당한 노력에도 불구하고, 이 목표를 향한 진전은 인간과 로봇 간의 구현 격차(embodiment gap)와 야생 인간 비디오에서 자율 정책 학습을 가능하게 하는 관련 맥락 및 동작 신호를 추출하는 어려움으로 인해 병목 현상을 겪어 왔습니다. 우리는 인간 데이터를 얻기 위한 간단하면서도 충분히 강력한 하드웨어와 제안된 프레임워크 AINA를 통해 이 꿈에 한 걸음 더 가까워졌다고 주장합니다. AINA는 Aria Gen 2 안경을 사용하여 누구나, 어디서나, 어떤 환경에서든 수집된 데이터로부터 다지 정책을 학습할 수 있게 합니다. 이 안경은 가볍고 휴대 가능하며, 고해상도 RGB 카메라를 갖추고, 정확한 온보드 3D 머리 및 손 포즈를 제공하며, 장면의 깊이 추정에 활용할 수 있는 넓은 스테레오 뷰를 제공합니다. 이 설정은 배경 변화에 강건하고, 로봇 데이터(온라인 보정, 강화 학습 또는 시뮬레이션 포함) 없이 직접 배포할 수 있는 다지 손을 위한 3D 포인트 기반 정책 학습을 가능하게 합니다. 우리는 프레임워크를 이전의 인간-로봇 정책 학습 접근 방식과 비교하고, 설계 선택을 분석하며, 9가지 일상 조작 작업에 걸친 결과를 시연합니다. 로봇 롤아웃은 웹사이트 https://aina-robot.github.io 에서 가장 잘 확인할 수 있습니다.

## 핵심 내용
일상 환경에서 인간이 수행하는 작업을 통해 다지 로봇 정책을 학습하는 것은 로봇 공학 커뮤니티의 오랜 큰 목표였습니다. 이를 달성하면 인간 환경에서 일반화 가능한 로봇 조작을 향한 중요한 진전이 될 것이며, 노동 집약적인 로봇 데이터 수집에 대한 의존도를 줄일 수 있습니다. 상당한 노력에도 불구하고, 이 목표를 향한 진전은 인간과 로봇 간의 구현 격차(embodiment gap)와 야생 인간 비디오에서 자율 정책 학습을 가능하게 하는 관련 맥락 및 동작 신호를 추출하는 어려움으로 인해 병목 현상을 겪어 왔습니다. 우리는 인간 데이터를 얻기 위한 간단하면서도 충분히 강력한 하드웨어와 제안된 프레임워크 AINA를 통해 이 꿈에 한 걸음 더 가까워졌다고 주장합니다. AINA는 Aria Gen 2 안경을 사용하여 누구나, 어디서나, 어떤 환경에서든 수집된 데이터로부터 다지 정책을 학습할 수 있게 합니다. 이 안경은 가볍고 휴대 가능하며, 고해상도 RGB 카메라를 갖추고, 정확한 온보드 3D 머리 및 손 포즈를 제공하며, 장면의 깊이 추정에 활용할 수 있는 넓은 스테레오 뷰를 제공합니다. 이 설정은 배경 변화에 강건하고, 로봇 데이터(온라인 보정, 강화 학습 또는 시뮬레이션 포함) 없이 직접 배포할 수 있는 다지 손을 위한 3D 포인트 기반 정책 학습을 가능하게 합니다. 우리는 프레임워크를 이전의 인간-로봇 정책 학습 접근 방식과 비교하고, 설계 선택을 분석하며, 9가지 일상 조작 작업에 걸친 결과를 시연합니다. 로봇 롤아웃은 웹사이트 https://aina-robot.github.io 에서 가장 잘 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2511.16661v1

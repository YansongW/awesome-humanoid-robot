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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.16661v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (732 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2511.16661v1

## 개요
AINA는 인간의 자연 환경에서 일상 작업을 수행하는 데이터로부터 다지(dexterous) 로봇 정책을 학습하는 장기 목표를 해결하기 위해 설계되었습니다. 이 프레임워크는 경량의 휴대용 Aria Gen 2 스마트 안경을 사용하여 고해상도 RGB 이미지, 정밀한 3D 머리 및 손 자세, 넓은 스테레오 뷰를 획득함으로써 인간과 로봇 사이의 구현 격차를 극복합니다. AINA는 3D 포인트 기반의 다지 손 정책을 학습할 수 있으며, 배경 변화에 강건하고, 온라인 보정, 강화 학습 또는 시뮬레이션을 포함한 어떠한 로봇 데이터도 필요로 하지 않습니다. 실험은 9가지 일상 조작 작업에서 성능을 입증했으며, 이전의 인간-로봇 정책 학습 방법과 비교되었습니다.

## 핵심 내용
### 방법
- AINA는 대규모 비전-언어-행동 모델 아키텍처를 채택하여 Aria Gen 2 안경으로 수집된 야생 인간 비디오에서 맥락 및 운동 단서를 추출합니다.
- 안경이 제공하는 정밀한 3D 머리 및 손 자세와 넓은 스테레오 뷰를 활용하여 깊이 추정을 수행하고, 이를 통해 3D 포인트 클라우드 표현의 다지 정책을 학습합니다.

### 실험 설정
- 데이터 수집: Aria Gen 2 안경을 사용하여 임의의 사람이 임의의 환경에서 인간 시연 데이터를 수집합니다.
- 작업: 잡기, 놓기, 회전 등을 포함한 9가지 일상 조작 작업을 다룹니다.
- 비교 기준: 행동 클로닝, 모방 학습과 같은 이전의 인간-로봇 정책 학습 방법과 비교합니다.
- 절제 실험: 3D 포인트 클라우드 사용 여부, 깊이 추정 의존 여부와 같은 설계 선택에 대한 절제 분석을 수행합니다.

### 주요 수치
- 로봇 데이터 불필요: 온라인 보정, 강화 학습 또는 시뮬레이션을 포함하지 않습니다.
- 9가지 일상 조작 작업: 정책의 일반화 능력을 입증합니다.
- 강건성: 배경 변화에 강건하며 직접 배포가 가능합니다.

### 결론
- AINA는 야생 인간 비디오로부터 다지 로봇 정책을 학습하는 목표를 크게 진전시켰으며, 수작업 로봇 데이터 수집에 대한 의존도를 줄였습니다.
- 간단하면서도 강력한 하드웨어(Aria Gen 2 안경)와 제안된 프레임워크를 통해 임의 환경 데이터에서 직접 배포 가능한 정책 학습을 달성했습니다.

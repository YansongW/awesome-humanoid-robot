---
$id: ent_paper_farazi_nimbro_robots_winning_robocup_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: NimbRo Robots Winning RoboCup 2018 Humanoid AdultSize Soccer Competitions
  zh: NimbRo机器人赢得2018年RoboCup人形成人组足球比赛
  ko: NimbRo 로봇, 2018 RoboCup 휴머노이드 AdultSize 축구 대회 우승
summary:
  en: This paper presents the open-source hardware and software designs that enabled Team NimbRo to win all AdultSize competitions
    and the Best Humanoid Award at RoboCup 2018, including a deep-learning visual perception system, a modular hierarchical
    state machine for soccer behaviors, Bayesian gait optimization, and the fully 3D-printed NimbRo-OP2X robot.
  zh: 本文介绍了使NimbRo队在2018年RoboCup人形成人组比赛中赢得所有奖项（包括最佳人形机器人奖）的开源软硬件设计，包括基于深度学习的视觉感知系统、模块化的分层状态机足球行为、贝叶斯步态优化以及全3D打印的NimbRo-OP2X机器人。
  ko: 본 논문은 2018 RoboCup 휴머노이드 AdultSize 대회에서 모든 부문과 최고 휴머노이드상을 수상한 NimbRo 팀의 오픈소스 하드웨어 및 소프트웨어 설계를 제시하며, 딥러닝 기반 시각 인식 시스템,
    모듈화된 계층적 상태 기반 축구 행위, 베이지안 보행 최적화, 그리고 완전 3D 프린팅된 NimbRo-OP2X 로봇을 포함한다.
domains:
- 06_design_engineering
- 07_ai_models_algorithms
- 08_software_middleware
- 02_components
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
- system
tags:
- robocup
- humanoid_soccer
- adult_size
- nimbro_op2x
- deep_learning_perception
- gait_optimization
- bayesian_optimization
- hierarchical_state_machine
- ros
- 3d_printed_robot
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1909.02385v1.
sources:
- id: src_001
  type: paper
  title: NimbRo Robots Winning RoboCup 2018 Humanoid AdultSize Soccer Competitions
  url: https://arxiv.org/abs/1909.02385
  date: '2019'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
- system
---
## 概述
Over the past few years, the Humanoid League rules have changed towards more realistic and challenging game environments, which encourage teams to advance their robot soccer performances. In this paper, we present the software and hardware designs that led our team NimbRo to win the competitions in the AdultSize league -- including the soccer tournament, the drop-in games, and the technical challenges at RoboCup 2018 in Montreal. Altogether, this resulted in NimbRo winning the Best Humanoid Award. In particular, we describe our deep-learning approaches for visual perception and our new fully 3D printed robot NimbRo-OP2X.

## 核心内容
Over the past few years, the Humanoid League rules have changed towards more realistic and challenging game environments, which encourage teams to advance their robot soccer performances. In this paper, we present the software and hardware designs that led our team NimbRo to win the competitions in the AdultSize league -- including the soccer tournament, the drop-in games, and the technical challenges at RoboCup 2018 in Montreal. Altogether, this resulted in NimbRo winning the Best Humanoid Award. In particular, we describe our deep-learning approaches for visual perception and our new fully 3D printed robot NimbRo-OP2X.

## 参考
- http://arxiv.org/abs/1909.02385v1

## Overview
Over the past few years, the Humanoid League rules have changed towards more realistic and challenging game environments, which encourage teams to advance their robot soccer performances. In this paper, we present the software and hardware designs that led our team NimbRo to win the competitions in the AdultSize league -- including the soccer tournament, the drop-in games, and the technical challenges at RoboCup 2018 in Montreal. Altogether, this resulted in NimbRo winning the Best Humanoid Award. In particular, we describe our deep-learning approaches for visual perception and our new fully 3D printed robot NimbRo-OP2X.

## Content
Over the past few years, the Humanoid League rules have changed towards more realistic and challenging game environments, which encourage teams to advance their robot soccer performances. In this paper, we present the software and hardware designs that led our team NimbRo to win the competitions in the AdultSize league -- including the soccer tournament, the drop-in games, and the technical challenges at RoboCup 2018 in Montreal. Altogether, this resulted in NimbRo winning the Best Humanoid Award. In particular, we describe our deep-learning approaches for visual perception and our new fully 3D printed robot NimbRo-OP2X.

## 개요
지난 몇 년간 휴머노이드 리그 규칙은 더욱 현실적이고 도전적인 게임 환경으로 변화해 왔으며, 이는 팀들이 로봇 축구 성능을 향상시키도록 장려하고 있습니다. 본 논문에서는 저희 팀 NimbRo가 몬트리올에서 열린 RoboCup 2018의 AdultSize 리그에서 축구 토너먼트, 드롭인 게임, 기술 챌린지를 포함한 대회에서 우승할 수 있도록 한 소프트웨어 및 하드웨어 설계를 소개합니다. 이 모든 결과로 NimbRo는 최우수 휴머노이드 상을 수상했습니다. 특히, 시각 인식을 위한 딥러닝 접근 방식과 새로운 완전 3D 프린팅 로봇 NimbRo-OP2X에 대해 설명합니다.

## 핵심 내용
지난 몇 년간 휴머노이드 리그 규칙은 더욱 현실적이고 도전적인 게임 환경으로 변화해 왔으며, 이는 팀들이 로봇 축구 성능을 향상시키도록 장려하고 있습니다. 본 논문에서는 저희 팀 NimbRo가 몬트리올에서 열린 RoboCup 2018의 AdultSize 리그에서 축구 토너먼트, 드롭인 게임, 기술 챌린지를 포함한 대회에서 우승할 수 있도록 한 소프트웨어 및 하드웨어 설계를 소개합니다. 이 모든 결과로 NimbRo는 최우수 휴머노이드 상을 수상했습니다. 특히, 시각 인식을 위한 딥러닝 접근 방식과 새로운 완전 3D 프린팅 로봇 NimbRo-OP2X에 대해 설명합니다.

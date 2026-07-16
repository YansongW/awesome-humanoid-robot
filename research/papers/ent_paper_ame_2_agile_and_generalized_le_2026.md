---
$id: ent_paper_ame_2_agile_and_generalized_le_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AME-2: Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding'
  zh: 'AME-2: Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding'
  ko: 'AME-2: Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding'
summary:
  en: 'AME-2: Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding is a 2026 work on locomotion
    for humanoid robots.'
  zh: 'AME-2: Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding is a 2026 work on locomotion
    for humanoid robots.'
  ko: 'AME-2: Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding is a 2026 work on locomotion
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ame_2
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.08485v2.
sources:
- id: src_001
  type: paper
  title: 'AME-2: Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding (arXiv)'
  url: https://arxiv.org/abs/2601.08485
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Achieving agile and generalized legged locomotion across terrains requires tight integration of perception and control, especially under occlusions and sparse footholds. Existing methods have demonstrated agility on parkour courses but often rely on end-to-end sensorimotor models with limited generalization and interpretability. By contrast, methods targeting generalized locomotion typically exhibit limited agility and struggle with visual occlusions. We introduce AME-2, a unified reinforcement learning (RL) framework for agile and generalized locomotion that incorporates a novel attention-based map encoder in the control policy. This encoder extracts local and global mapping features and uses attention mechanisms to focus on salient regions, producing an interpretable and generalized embedding for RL-based control. We further propose a learning-based mapping pipeline that provides fast, uncertainty-aware terrain representations robust to noise and occlusions, serving as policy inputs. It uses neural networks to convert depth observations into local elevations with uncertainties, and fuses them with odometry. The pipeline also integrates with parallel simulation so that we can train controllers with online mapping, aiding sim-to-real transfer. We validate AME-2 with the proposed mapping pipeline on a quadruped and a biped robot, and the resulting controllers demonstrate strong agility and generalization to unseen terrains in simulation and in real-world experiments.

## 核心内容
Achieving agile and generalized legged locomotion across terrains requires tight integration of perception and control, especially under occlusions and sparse footholds. Existing methods have demonstrated agility on parkour courses but often rely on end-to-end sensorimotor models with limited generalization and interpretability. By contrast, methods targeting generalized locomotion typically exhibit limited agility and struggle with visual occlusions. We introduce AME-2, a unified reinforcement learning (RL) framework for agile and generalized locomotion that incorporates a novel attention-based map encoder in the control policy. This encoder extracts local and global mapping features and uses attention mechanisms to focus on salient regions, producing an interpretable and generalized embedding for RL-based control. We further propose a learning-based mapping pipeline that provides fast, uncertainty-aware terrain representations robust to noise and occlusions, serving as policy inputs. It uses neural networks to convert depth observations into local elevations with uncertainties, and fuses them with odometry. The pipeline also integrates with parallel simulation so that we can train controllers with online mapping, aiding sim-to-real transfer. We validate AME-2 with the proposed mapping pipeline on a quadruped and a biped robot, and the resulting controllers demonstrate strong agility and generalization to unseen terrains in simulation and in real-world experiments.

## 参考
- http://arxiv.org/abs/2601.08485v2

## Overview
Achieving agile and generalized legged locomotion across terrains requires tight integration of perception and control, especially under occlusions and sparse footholds. Existing methods have demonstrated agility on parkour courses but often rely on end-to-end sensorimotor models with limited generalization and interpretability. By contrast, methods targeting generalized locomotion typically exhibit limited agility and struggle with visual occlusions. We introduce AME-2, a unified reinforcement learning (RL) framework for agile and generalized locomotion that incorporates a novel attention-based map encoder in the control policy. This encoder extracts local and global mapping features and uses attention mechanisms to focus on salient regions, producing an interpretable and generalized embedding for RL-based control. We further propose a learning-based mapping pipeline that provides fast, uncertainty-aware terrain representations robust to noise and occlusions, serving as policy inputs. It uses neural networks to convert depth observations into local elevations with uncertainties, and fuses them with odometry. The pipeline also integrates with parallel simulation so that we can train controllers with online mapping, aiding sim-to-real transfer. We validate AME-2 with the proposed mapping pipeline on a quadruped and a biped robot, and the resulting controllers demonstrate strong agility and generalization to unseen terrains in simulation and in real-world experiments.

## Content
Achieving agile and generalized legged locomotion across terrains requires tight integration of perception and control, especially under occlusions and sparse footholds. Existing methods have demonstrated agility on parkour courses but often rely on end-to-end sensorimotor models with limited generalization and interpretability. By contrast, methods targeting generalized locomotion typically exhibit limited agility and struggle with visual occlusions. We introduce AME-2, a unified reinforcement learning (RL) framework for agile and generalized locomotion that incorporates a novel attention-based map encoder in the control policy. This encoder extracts local and global mapping features and uses attention mechanisms to focus on salient regions, producing an interpretable and generalized embedding for RL-based control. We further propose a learning-based mapping pipeline that provides fast, uncertainty-aware terrain representations robust to noise and occlusions, serving as policy inputs. It uses neural networks to convert depth observations into local elevations with uncertainties, and fuses them with odometry. The pipeline also integrates with parallel simulation so that we can train controllers with online mapping, aiding sim-to-real transfer. We validate AME-2 with the proposed mapping pipeline on a quadruped and a biped robot, and the resulting controllers demonstrate strong agility and generalization to unseen terrains in simulation and in real-world experiments.

## 개요
다양한 지형에서 민첩하고 일반화된 보행 운동을 달성하려면 인식과 제어의 긴밀한 통합이 필요하며, 특히 폐색과 드문 발판 조건에서 더욱 그렇습니다. 기존 방법들은 파쿠르 코스에서 민첩성을 입증했지만, 종종 제한된 일반화와 해석 가능성을 가진 종단간 감각운동 모델에 의존합니다. 반면, 일반화된 보행을 목표로 하는 방법들은 일반적으로 제한된 민첩성을 보이며 시각적 폐색에 어려움을 겪습니다. 우리는 제어 정책에 새로운 주의 기반 지도 인코더를 통합한 통합 강화 학습(RL) 프레임워크인 AME-2를 소개합니다. 이 인코더는 로컬 및 글로벌 매핑 특징을 추출하고 주의 메커니즘을 사용하여 중요한 영역에 집중함으로써 RL 기반 제어를 위한 해석 가능하고 일반화된 임베딩을 생성합니다. 또한, 잡음과 폐색에 강건한 빠르고 불확실성 인식 지형 표현을 제공하는 학습 기반 매핑 파이프라인을 제안하여 정책 입력으로 사용합니다. 이 파이프라인은 신경망을 사용하여 깊이 관측을 불확실성이 포함된 로컬 고도로 변환하고, 이를 오도메트리와 융합합니다. 또한, 온라인 매핑으로 제어기를 훈련할 수 있도록 병렬 시뮬레이션과 통합되어 시뮬레이션-실제 전환을 지원합니다. 우리는 제안된 매핑 파이프라인을 사용하여 AME-2를 사족 보행 로봇과 이족 보행 로봇에서 검증했으며, 결과 제어기는 시뮬레이션 및 실제 실험에서 보지 못한 지형에 대해 강력한 민첩성과 일반화를 보여주었습니다.

## 핵심 내용
다양한 지형에서 민첩하고 일반화된 보행 운동을 달성하려면 인식과 제어의 긴밀한 통합이 필요하며, 특히 폐색과 드문 발판 조건에서 더욱 그렇습니다. 기존 방법들은 파쿠르 코스에서 민첩성을 입증했지만, 종종 제한된 일반화와 해석 가능성을 가진 종단간 감각운동 모델에 의존합니다. 반면, 일반화된 보행을 목표로 하는 방법들은 일반적으로 제한된 민첩성을 보이며 시각적 폐색에 어려움을 겪습니다. 우리는 제어 정책에 새로운 주의 기반 지도 인코더를 통합한 통합 강화 학습(RL) 프레임워크인 AME-2를 소개합니다. 이 인코더는 로컬 및 글로벌 매핑 특징을 추출하고 주의 메커니즘을 사용하여 중요한 영역에 집중함으로써 RL 기반 제어를 위한 해석 가능하고 일반화된 임베딩을 생성합니다. 또한, 잡음과 폐색에 강건한 빠르고 불확실성 인식 지형 표현을 제공하는 학습 기반 매핑 파이프라인을 제안하여 정책 입력으로 사용합니다. 이 파이프라인은 신경망을 사용하여 깊이 관측을 불확실성이 포함된 로컬 고도로 변환하고, 이를 오도메트리와 융합합니다. 또한, 온라인 매핑으로 제어기를 훈련할 수 있도록 병렬 시뮬레이션과 통합되어 시뮬레이션-실제 전환을 지원합니다. 우리는 제안된 매핑 파이프라인을 사용하여 AME-2를 사족 보행 로봇과 이족 보행 로봇에서 검증했으며, 결과 제어기는 시뮬레이션 및 실제 실험에서 보지 못한 지형에 대해 강력한 민첩성과 일반화를 보여주었습니다.

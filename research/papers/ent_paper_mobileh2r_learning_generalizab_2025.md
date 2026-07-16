---
$id: ent_paper_mobileh2r_learning_generalizab_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic Data'
  zh: 'MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic Data'
  ko: 'MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic Data'
summary:
  en: 'MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic Data
    is a 2025 work on manipulation for humanoid robots.'
  zh: 'MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic Data
    is a 2025 work on manipulation for humanoid robots.'
  ko: 'MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic Data
    is a 2025 work on manipulation for humanoid robots.'
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
- manipulation
- mobileh2r
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2501.04595v2.
sources:
- id: src_001
  type: paper
  title: 'MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic
    Data (arXiv)'
  url: https://arxiv.org/abs/2501.04595
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
This paper introduces MobileH2R, a framework for learning generalizable vision-based human-to-mobile-robot (H2MR) handover skills. Unlike traditional fixed-base handovers, this task requires a mobile robot to reliably receive objects in a large workspace enabled by its mobility. Our key insight is that generalizable handover skills can be developed in simulators using high-quality synthetic data, without the need for real-world demonstrations. To achieve this, we propose a scalable pipeline for generating diverse synthetic full-body human motion data, an automated method for creating safe and imitation-friendly demonstrations, and an efficient 4D imitation learning method for distilling large-scale demonstrations into closed-loop policies with base-arm coordination. Experimental evaluations in both simulators and the real world show significant improvements (at least +15% success rate) over baseline methods in all cases. Experiments also validate that large-scale and diverse synthetic data greatly enhances robot learning, highlighting our scalable framework.

## 核心内容
This paper introduces MobileH2R, a framework for learning generalizable vision-based human-to-mobile-robot (H2MR) handover skills. Unlike traditional fixed-base handovers, this task requires a mobile robot to reliably receive objects in a large workspace enabled by its mobility. Our key insight is that generalizable handover skills can be developed in simulators using high-quality synthetic data, without the need for real-world demonstrations. To achieve this, we propose a scalable pipeline for generating diverse synthetic full-body human motion data, an automated method for creating safe and imitation-friendly demonstrations, and an efficient 4D imitation learning method for distilling large-scale demonstrations into closed-loop policies with base-arm coordination. Experimental evaluations in both simulators and the real world show significant improvements (at least +15% success rate) over baseline methods in all cases. Experiments also validate that large-scale and diverse synthetic data greatly enhances robot learning, highlighting our scalable framework.

## 参考
- http://arxiv.org/abs/2501.04595v2

## Overview
This paper introduces MobileH2R, a framework for learning generalizable vision-based human-to-mobile-robot (H2MR) handover skills. Unlike traditional fixed-base handovers, this task requires a mobile robot to reliably receive objects in a large workspace enabled by its mobility. Our key insight is that generalizable handover skills can be developed in simulators using high-quality synthetic data, without the need for real-world demonstrations. To achieve this, we propose a scalable pipeline for generating diverse synthetic full-body human motion data, an automated method for creating safe and imitation-friendly demonstrations, and an efficient 4D imitation learning method for distilling large-scale demonstrations into closed-loop policies with base-arm coordination. Experimental evaluations in both simulators and the real world show significant improvements (at least +15% success rate) over baseline methods in all cases. Experiments also validate that large-scale and diverse synthetic data greatly enhances robot learning, highlighting our scalable framework.

## Content
This paper introduces MobileH2R, a framework for learning generalizable vision-based human-to-mobile-robot (H2MR) handover skills. Unlike traditional fixed-base handovers, this task requires a mobile robot to reliably receive objects in a large workspace enabled by its mobility. Our key insight is that generalizable handover skills can be developed in simulators using high-quality synthetic data, without the need for real-world demonstrations. To achieve this, we propose a scalable pipeline for generating diverse synthetic full-body human motion data, an automated method for creating safe and imitation-friendly demonstrations, and an efficient 4D imitation learning method for distilling large-scale demonstrations into closed-loop policies with base-arm coordination. Experimental evaluations in both simulators and the real world show significant improvements (at least +15% success rate) over baseline methods in all cases. Experiments also validate that large-scale and diverse synthetic data greatly enhances robot learning, highlighting our scalable framework.

## 개요
본 논문은 일반화 가능한 비전 기반 인간-이동로봇(H2MR) 물체 전달 기술을 학습하기 위한 프레임워크인 MobileH2R을 소개합니다. 기존의 고정 기반 물체 전달과 달리, 이 작업은 이동성을 활용하여 넓은 작업 공간에서 이동 로봇이 안정적으로 물체를 수신해야 합니다. 핵심 통찰은 일반화 가능한 물체 전달 기술이 실제 환경 시연 없이도 고품질 합성 데이터를 사용하여 시뮬레이터에서 개발될 수 있다는 점입니다. 이를 위해, 다양한 합성 전신 인간 동작 데이터를 생성하는 확장 가능한 파이프라인, 안전하고 모방 학습에 적합한 시연을 자동으로 생성하는 방법, 그리고 대규모 시연을 베이스-암 협력이 가능한 폐쇄 루프 정책으로 증류하는 효율적인 4D 모방 학습 방법을 제안합니다. 시뮬레이터와 실제 환경 모두에서 수행된 실험 평가는 모든 경우에서 기준 방법 대비 최소 +15%의 성공률 향상을 보여줍니다. 또한, 대규모의 다양한 합성 데이터가 로봇 학습을 크게 향상시킨다는 점을 실험을 통해 검증하며, 이는 확장 가능한 프레임워크의 우수성을 강조합니다.

## 핵심 내용
본 논문은 일반화 가능한 비전 기반 인간-이동로봇(H2MR) 물체 전달 기술을 학습하기 위한 프레임워크인 MobileH2R을 소개합니다. 기존의 고정 기반 물체 전달과 달리, 이 작업은 이동성을 활용하여 넓은 작업 공간에서 이동 로봇이 안정적으로 물체를 수신해야 합니다. 핵심 통찰은 일반화 가능한 물체 전달 기술이 실제 환경 시연 없이도 고품질 합성 데이터를 사용하여 시뮬레이터에서 개발될 수 있다는 점입니다. 이를 위해, 다양한 합성 전신 인간 동작 데이터를 생성하는 확장 가능한 파이프라인, 안전하고 모방 학습에 적합한 시연을 자동으로 생성하는 방법, 그리고 대규모 시연을 베이스-암 협력이 가능한 폐쇄 루프 정책으로 증류하는 효율적인 4D 모방 학습 방법을 제안합니다. 시뮬레이터와 실제 환경 모두에서 수행된 실험 평가는 모든 경우에서 기준 방법 대비 최소 +15%의 성공률 향상을 보여줍니다. 또한, 대규모의 다양한 합성 데이터가 로봇 학습을 크게 향상시킨다는 점을 실험을 통해 검증하며, 이는 확장 가능한 프레임워크의 우수성을 강조합니다.

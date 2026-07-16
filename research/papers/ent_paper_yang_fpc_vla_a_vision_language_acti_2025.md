---
$id: ent_paper_yang_fpc_vla_a_vision_language_acti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction'
  zh: FPC-VLA
  ko: 'FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction'
summary:
  en: 'FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction (FPC-VLA), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Nankai University, Xiaomi EV, Northeastern
    University Shenyang, University of Macau.'
  zh: 'FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction (FPC-VLA), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Nankai University, Xiaomi EV, Northeastern
    University Shenyang, University of Macau.'
  ko: 'FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction (FPC-VLA), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Nankai University, Xiaomi EV, Northeastern
    University Shenyang, University of Macau.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- fpc_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.04018v2.
sources:
- id: src_001
  type: paper
  title: 'FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction (arXiv)'
  url: https://arxiv.org/abs/2509.04018
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: FPC-VLA source
  url: https://doi.org/10.48550/arXiv.2509.04018
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Robotic manipulation is a fundamental component of automation. However, traditional perception-planning pipelines often fall short in open-ended tasks due to limited flexibility, while the architecture of a single end-to-end Vision-Language-Action (VLA) offers promising capabilities but lacks crucial mechanisms for anticipating and recovering from failure. To address these challenges, we propose FPC-VLA, a dual-model framework that integrates VLA with a supervisor for failure prediction and correction. The supervisor evaluates action viability through vision-language queries and generates corrective strategies when risks arise, trained efficiently without manual labeling. A dual-stream fusion module further refines actions by leveraging past predictions. Evaluation results on multiple simulation platforms (SIMPLER and LIBERO) and robot embodiments (WidowX, Google Robot, Franka) show that FPC-VLA outperforms state-of-the-art models in both zero-shot and fine-tuned settings. Successful real-world deployments on diverse, long-horizon tasks confirm FPC-VLA's strong generalization and practical utility for building more reliable autonomous systems.

## 核心内容
Robotic manipulation is a fundamental component of automation. However, traditional perception-planning pipelines often fall short in open-ended tasks due to limited flexibility, while the architecture of a single end-to-end Vision-Language-Action (VLA) offers promising capabilities but lacks crucial mechanisms for anticipating and recovering from failure. To address these challenges, we propose FPC-VLA, a dual-model framework that integrates VLA with a supervisor for failure prediction and correction. The supervisor evaluates action viability through vision-language queries and generates corrective strategies when risks arise, trained efficiently without manual labeling. A dual-stream fusion module further refines actions by leveraging past predictions. Evaluation results on multiple simulation platforms (SIMPLER and LIBERO) and robot embodiments (WidowX, Google Robot, Franka) show that FPC-VLA outperforms state-of-the-art models in both zero-shot and fine-tuned settings. Successful real-world deployments on diverse, long-horizon tasks confirm FPC-VLA's strong generalization and practical utility for building more reliable autonomous systems.

## 参考
- http://arxiv.org/abs/2509.04018v2

## Overview
Robotic manipulation is a fundamental component of automation. However, traditional perception-planning pipelines often fall short in open-ended tasks due to limited flexibility, while the architecture of a single end-to-end Vision-Language-Action (VLA) offers promising capabilities but lacks crucial mechanisms for anticipating and recovering from failure. To address these challenges, we propose FPC-VLA, a dual-model framework that integrates VLA with a supervisor for failure prediction and correction. The supervisor evaluates action viability through vision-language queries and generates corrective strategies when risks arise, trained efficiently without manual labeling. A dual-stream fusion module further refines actions by leveraging past predictions. Evaluation results on multiple simulation platforms (SIMPLER and LIBERO) and robot embodiments (WidowX, Google Robot, Franka) show that FPC-VLA outperforms state-of-the-art models in both zero-shot and fine-tuned settings. Successful real-world deployments on diverse, long-horizon tasks confirm FPC-VLA's strong generalization and practical utility for building more reliable autonomous systems.

## Content
Robotic manipulation is a fundamental component of automation. However, traditional perception-planning pipelines often fall short in open-ended tasks due to limited flexibility, while the architecture of a single end-to-end Vision-Language-Action (VLA) offers promising capabilities but lacks crucial mechanisms for anticipating and recovering from failure. To address these challenges, we propose FPC-VLA, a dual-model framework that integrates VLA with a supervisor for failure prediction and correction. The supervisor evaluates action viability through vision-language queries and generates corrective strategies when risks arise, trained efficiently without manual labeling. A dual-stream fusion module further refines actions by leveraging past predictions. Evaluation results on multiple simulation platforms (SIMPLER and LIBERO) and robot embodiments (WidowX, Google Robot, Franka) show that FPC-VLA outperforms state-of-the-art models in both zero-shot and fine-tuned settings. Successful real-world deployments on diverse, long-horizon tasks confirm FPC-VLA's strong generalization and practical utility for building more reliable autonomous systems.

## 개요
로봇 조작은 자동화의 핵심 구성 요소입니다. 그러나 기존의 인식-계획 파이프라인은 제한된 유연성으로 인해 개방형 작업에서 종종 부족한 성능을 보이며, 단일 엔드투엔드 Vision-Language-Action(VLA) 아키텍처는 유망한 능력을 제공하지만 실패를 예측하고 복구하는 중요한 메커니즘이 부족합니다. 이러한 문제를 해결하기 위해 우리는 VLA와 실패 예측 및 수정을 위한 감독자를 통합한 이중 모델 프레임워크인 FPC-VLA를 제안합니다. 감독자는 비전-언어 쿼리를 통해 행동의 실행 가능성을 평가하고 위험이 발생할 때 수정 전략을 생성하며, 수동 레이블링 없이 효율적으로 훈련됩니다. 이중 스트림 융합 모듈은 과거 예측을 활용하여 행동을 더욱 정교화합니다. 여러 시뮬레이션 플랫폼(SIMPLER 및 LIBERO)과 로봇 구현체(WidowX, Google Robot, Franka)에 대한 평가 결과는 FPC-VLA가 제로샷 및 미세 조정 설정 모두에서 최첨단 모델을 능가함을 보여줍니다. 다양한 장기 작업에 대한 성공적인 실제 배포는 FPC-VLA의 강력한 일반화 능력과 더 신뢰할 수 있는 자율 시스템 구축을 위한 실용적 유용성을 확인합니다.

## 핵심 내용
로봇 조작은 자동화의 핵심 구성 요소입니다. 그러나 기존의 인식-계획 파이프라인은 제한된 유연성으로 인해 개방형 작업에서 종종 부족한 성능을 보이며, 단일 엔드투엔드 Vision-Language-Action(VLA) 아키텍처는 유망한 능력을 제공하지만 실패를 예측하고 복구하는 중요한 메커니즘이 부족합니다. 이러한 문제를 해결하기 위해 우리는 VLA와 실패 예측 및 수정을 위한 감독자를 통합한 이중 모델 프레임워크인 FPC-VLA를 제안합니다. 감독자는 비전-언어 쿼리를 통해 행동의 실행 가능성을 평가하고 위험이 발생할 때 수정 전략을 생성하며, 수동 레이블링 없이 효율적으로 훈련됩니다. 이중 스트림 융합 모듈은 과거 예측을 활용하여 행동을 더욱 정교화합니다. 여러 시뮬레이션 플랫폼(SIMPLER 및 LIBERO)과 로봇 구현체(WidowX, Google Robot, Franka)에 대한 평가 결과는 FPC-VLA가 제로샷 및 미세 조정 설정 모두에서 최첨단 모델을 능가함을 보여줍니다. 다양한 장기 작업에 대한 성공적인 실제 배포는 FPC-VLA의 강력한 일반화 능력과 더 신뢰할 수 있는 자율 시스템 구축을 위한 실용적 유용성을 확인합니다.

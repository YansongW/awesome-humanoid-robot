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
  zh: FPC-VLA 是南开大学、小米汽车、东北大学沈阳分校和澳门大学于 2025 年提出的大型视觉-语言-动作模型框架，用于机器人操作。其核心贡献在于引入一个监督器模块，通过视觉-语言查询预测动作失败并生成纠正策略，从而提升系统的鲁棒性。该框架在
    SIMPLER 和 LIBERO 等多个仿真平台以及 WidowX、Google Robot、Franka 等实体机器人上均取得了优于现有模型的性能。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.04018v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
FPC-VLA 旨在解决传统感知-规划流水线在开放式任务中灵活性不足，以及单一端到端 VLA 模型缺乏失败预测与恢复机制的问题。该框架采用双模型架构，将主 VLA 模型与一个监督器相结合：监督器通过视觉-语言查询评估动作可行性，并在检测到风险时生成纠正策略，且其训练无需人工标注。此外，一个双流融合模块利用历史预测结果进一步优化动作输出。在 SIMPLER 和 LIBERO 等仿真环境以及 WidowX、Google Robot、Franka 等不同机器人平台上的评估表明，FPC-VLA 在零样本和微调设置下均超越了现有最先进模型。实际部署于多种长时程任务的成功案例，验证了其强大的泛化能力和构建更可靠自主系统的实用价值。

## 核心内容
### 方法架构
FPC-VLA 的核心是一个双模型框架，包含一个主 VLA 模型和一个监督器。
- **主 VLA 模型**：负责根据视觉和语言指令生成初始动作。
- **监督器**：通过视觉-语言查询评估主模型生成的动作是否可行。当检测到高风险时，监督器会生成纠正策略，指导主模型调整动作。该监督器的训练无需人工标注，提高了效率。
- **双流融合模块**：该模块利用历史预测结果，对当前动作进行精细化处理，进一步提升动作的准确性和鲁棒性。

### 实验设置与结果
- **仿真平台**：在 SIMPLER 和 LIBERO 两个仿真平台上进行了评估。
- **机器人平台**：测试了三种不同的机器人实体：WidowX、Google Robot 和 Franka。
- **评估设置**：包括零样本（zero-shot）和微调（fine-tuned）两种设置。
- **关键结果**：FPC-VLA 在所有评估设置和平台上均优于现有最先进模型。具体性能提升幅度未在摘要中给出，但明确指出了其在零样本和微调场景下的领先优势。
- **实际部署**：在多种不同的长时程（long-horizon）任务中成功进行了实际部署，验证了其强大的泛化能力和实际应用价值，为构建更可靠的自主系统提供了有力支持。

## Overview
Robotic manipulation is a fundamental component of automation. However, traditional perception-planning pipelines often fall short in open-ended tasks due to limited flexibility, while the architecture of a single end-to-end Vision-Language-Action (VLA) offers promising capabilities but lacks crucial mechanisms for anticipating and recovering from failure. To address these challenges, we propose FPC-VLA, a dual-model framework that integrates VLA with a supervisor for failure prediction and correction. The supervisor evaluates action viability through vision-language queries and generates corrective strategies when risks arise, trained efficiently without manual labeling. A dual-stream fusion module further refines actions by leveraging past predictions. Evaluation results on multiple simulation platforms (SIMPLER and LIBERO) and robot embodiments (WidowX, Google Robot, Franka) show that FPC-VLA outperforms state-of-the-art models in both zero-shot and fine-tuned settings. Successful real-world deployments on diverse, long-horizon tasks confirm FPC-VLA's strong generalization and practical utility for building more reliable autonomous systems.

## 개요
로봇 조작은 자동화의 핵심 구성 요소입니다. 그러나 기존의 인식-계획 파이프라인은 제한된 유연성으로 인해 개방형 작업에서 종종 부족한 성능을 보이며, 단일 엔드투엔드 Vision-Language-Action(VLA) 아키텍처는 유망한 능력을 제공하지만 실패를 예측하고 복구하는 중요한 메커니즘이 부족합니다. 이러한 문제를 해결하기 위해 우리는 VLA와 실패 예측 및 수정을 위한 감독자를 통합한 이중 모델 프레임워크인 FPC-VLA를 제안합니다. 감독자는 비전-언어 쿼리를 통해 행동의 실행 가능성을 평가하고 위험이 발생할 때 수정 전략을 생성하며, 수동 레이블링 없이 효율적으로 훈련됩니다. 이중 스트림 융합 모듈은 과거 예측을 활용하여 행동을 더욱 정교화합니다. 여러 시뮬레이션 플랫폼(SIMPLER 및 LIBERO)과 로봇 구현체(WidowX, Google Robot, Franka)에 대한 평가 결과는 FPC-VLA가 제로샷 및 미세 조정 설정 모두에서 최첨단 모델을 능가함을 보여줍니다. 다양한 장기 작업에 대한 성공적인 실제 배포는 FPC-VLA의 강력한 일반화 능력과 더 신뢰할 수 있는 자율 시스템 구축을 위한 실용적 유용성을 확인합니다.

## 핵심 내용
로봇 조작은 자동화의 핵심 구성 요소입니다. 그러나 기존의 인식-계획 파이프라인은 제한된 유연성으로 인해 개방형 작업에서 종종 부족한 성능을 보이며, 단일 엔드투엔드 Vision-Language-Action(VLA) 아키텍처는 유망한 능력을 제공하지만 실패를 예측하고 복구하는 중요한 메커니즘이 부족합니다. 이러한 문제를 해결하기 위해 우리는 VLA와 실패 예측 및 수정을 위한 감독자를 통합한 이중 모델 프레임워크인 FPC-VLA를 제안합니다. 감독자는 비전-언어 쿼리를 통해 행동의 실행 가능성을 평가하고 위험이 발생할 때 수정 전략을 생성하며, 수동 레이블링 없이 효율적으로 훈련됩니다. 이중 스트림 융합 모듈은 과거 예측을 활용하여 행동을 더욱 정교화합니다. 여러 시뮬레이션 플랫폼(SIMPLER 및 LIBERO)과 로봇 구현체(WidowX, Google Robot, Franka)에 대한 평가 결과는 FPC-VLA가 제로샷 및 미세 조정 설정 모두에서 최첨단 모델을 능가함을 보여줍니다. 다양한 장기 작업에 대한 성공적인 실제 배포는 FPC-VLA의 강력한 일반화 능력과 더 신뢰할 수 있는 자율 시스템 구축을 위한 실용적 유용성을 확인합니다.

## 参考
- http://arxiv.org/abs/2509.04018v2

---
$id: ent_paper_zeng_diagnose_correct_and_learn_fro_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Diagnose Correct and Learn from Manipulation Failures via Visual Symbols
  zh: Diagnose Correct and Learn from Manipulation Failures via Visual Symbols
  ko: Diagnose Correct and Learn from Manipulation Failures via Visual Symbols
summary:
  en: Diagnose Correct and Learn from Manipulation Failures via Visual Symbols (Diagnose Correct and Learn from Manipulation
    Failures via Visual Symbols), is a 2025 large vision-language-action model for robotic manipulation, introduced by Beihang
    University, Shanghai Innovation Institute, Southern University of Science and Technology, Shanghai Jiao Tong University.
  zh: Diagnose Correct and Learn from Manipulation Failures via Visual Symbols (Diagnose Correct and Learn from Manipulation
    Failures via Visual Symbols), is a 2025 large vision-language-action model for robotic manipulation, introduced by Beihang
    University, Shanghai Innovation Institute, Southern University of Science and Technology, Shanghai Jiao Tong University.
  ko: Diagnose Correct and Learn from Manipulation Failures via Visual Symbols (Diagnose Correct and Learn from Manipulation
    Failures via Visual Symbols), is a 2025 large vision-language-action model for robotic manipulation, introduced by Beihang
    University, Shanghai Innovation Institute, Southern University of Science and Technology, Shanghai Jiao Tong University.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- diagnose_correct_and_learn_fro
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.02787v3.
sources:
- id: src_001
  type: paper
  title: Diagnose Correct and Learn from Manipulation Failures via Visual Symbols (arXiv)
  url: https://arxiv.org/abs/2512.02787
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Diagnose Correct and Learn from Manipulation Failures via Visual Symbols source
  url: https://doi.org/10.48550/arXiv.2512.02787
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have recently achieved remarkable progress in robotic manipulation, yet they remain limited in failure diagnosis and learning from failures. Additionally, existing failure datasets are mostly generated programmatically in simulation, which limits their generalization to the real world. In light of these, we introduce ViFailback, a framework designed to diagnose robotic manipulation failures and provide both textual and visual correction guidance. Our framework utilizes explicit visual symbols to enhance annotation efficiency. We further release the ViFailback dataset, a large-scale collection of 58,126 Visual Question Answering (VQA) pairs along with their corresponding 5,202 real-world manipulation trajectories. Based on the dataset, we establish ViFailback-Bench, a benchmark of 11 fine-grained VQA tasks designed to assess the failure diagnosis and correction abilities of Vision-Language Models (VLMs), featuring ViFailback-Bench Lite for closed-ended and ViFailback-Bench Hard for open-ended evaluation. To demonstrate the effectiveness of our framework, we built the ViFailback-8B VLM, which not only achieves significant overall performance improvement on ViFailback-Bench but also generates visual symbols for corrective action guidance. Finally, by integrating ViFailback-8B with a VLA model, we conduct real-world robotic experiments demonstrating its ability to assist the VLA model in recovering from failures. Project Website: https://x1nyuzhou.github.io/vifailback.github.io/

## 核心内容
Vision-Language-Action (VLA) models have recently achieved remarkable progress in robotic manipulation, yet they remain limited in failure diagnosis and learning from failures. Additionally, existing failure datasets are mostly generated programmatically in simulation, which limits their generalization to the real world. In light of these, we introduce ViFailback, a framework designed to diagnose robotic manipulation failures and provide both textual and visual correction guidance. Our framework utilizes explicit visual symbols to enhance annotation efficiency. We further release the ViFailback dataset, a large-scale collection of 58,126 Visual Question Answering (VQA) pairs along with their corresponding 5,202 real-world manipulation trajectories. Based on the dataset, we establish ViFailback-Bench, a benchmark of 11 fine-grained VQA tasks designed to assess the failure diagnosis and correction abilities of Vision-Language Models (VLMs), featuring ViFailback-Bench Lite for closed-ended and ViFailback-Bench Hard for open-ended evaluation. To demonstrate the effectiveness of our framework, we built the ViFailback-8B VLM, which not only achieves significant overall performance improvement on ViFailback-Bench but also generates visual symbols for corrective action guidance. Finally, by integrating ViFailback-8B with a VLA model, we conduct real-world robotic experiments demonstrating its ability to assist the VLA model in recovering from failures. Project Website: https://x1nyuzhou.github.io/vifailback.github.io/

## 参考
- http://arxiv.org/abs/2512.02787v3

## Overview
Vision-Language-Action (VLA) models have recently achieved remarkable progress in robotic manipulation, yet they remain limited in failure diagnosis and learning from failures. Additionally, existing failure datasets are mostly generated programmatically in simulation, which limits their generalization to the real world. In light of these, we introduce ViFailback, a framework designed to diagnose robotic manipulation failures and provide both textual and visual correction guidance. Our framework utilizes explicit visual symbols to enhance annotation efficiency. We further release the ViFailback dataset, a large-scale collection of 58,126 Visual Question Answering (VQA) pairs along with their corresponding 5,202 real-world manipulation trajectories. Based on the dataset, we establish ViFailback-Bench, a benchmark of 11 fine-grained VQA tasks designed to assess the failure diagnosis and correction abilities of Vision-Language Models (VLMs), featuring ViFailback-Bench Lite for closed-ended and ViFailback-Bench Hard for open-ended evaluation. To demonstrate the effectiveness of our framework, we built the ViFailback-8B VLM, which not only achieves significant overall performance improvement on ViFailback-Bench but also generates visual symbols for corrective action guidance. Finally, by integrating ViFailback-8B with a VLA model, we conduct real-world robotic experiments demonstrating its ability to assist the VLA model in recovering from failures. Project Website: https://x1nyuzhou.github.io/vifailback.github.io/

## Content
Vision-Language-Action (VLA) models have recently achieved remarkable progress in robotic manipulation, yet they remain limited in failure diagnosis and learning from failures. Additionally, existing failure datasets are mostly generated programmatically in simulation, which limits their generalization to the real world. In light of these, we introduce ViFailback, a framework designed to diagnose robotic manipulation failures and provide both textual and visual correction guidance. Our framework utilizes explicit visual symbols to enhance annotation efficiency. We further release the ViFailback dataset, a large-scale collection of 58,126 Visual Question Answering (VQA) pairs along with their corresponding 5,202 real-world manipulation trajectories. Based on the dataset, we establish ViFailback-Bench, a benchmark of 11 fine-grained VQA tasks designed to assess the failure diagnosis and correction abilities of Vision-Language Models (VLMs), featuring ViFailback-Bench Lite for closed-ended and ViFailback-Bench Hard for open-ended evaluation. To demonstrate the effectiveness of our framework, we built the ViFailback-8B VLM, which not only achieves significant overall performance improvement on ViFailback-Bench but also generates visual symbols for corrective action guidance. Finally, by integrating ViFailback-8B with a VLA model, we conduct real-world robotic experiments demonstrating its ability to assist the VLA model in recovering from failures. Project Website: https://x1nyuzhou.github.io/vifailback.github.io/

## 개요
Vision-Language-Action (VLA) 모델은 최근 로봇 조작 분야에서 놀라운 진전을 이루었지만, 여전히 실패 진단 및 실패로부터의 학습에는 한계가 있습니다. 또한, 기존의 실패 데이터셋은 대부분 시뮬레이션에서 프로그래밍 방식으로 생성되어 실제 세계로의 일반화에 제한이 있습니다. 이러한 문제를 해결하기 위해, 우리는 로봇 조작 실패를 진단하고 텍스트 및 시각적 교정 지침을 제공하도록 설계된 프레임워크인 ViFailback을 소개합니다. 우리의 프레임워크는 명시적인 시각적 기호를 활용하여 주석 효율성을 향상시킵니다. 또한, 58,126개의 Visual Question Answering (VQA) 쌍과 이에 해당하는 5,202개의 실제 세계 조작 궤적으로 구성된 대규모 컬렉션인 ViFailback 데이터셋을 공개합니다. 이 데이터셋을 기반으로, Vision-Language Models (VLMs)의 실패 진단 및 교정 능력을 평가하기 위해 설계된 11개의 세분화된 VQA 작업으로 구성된 벤치마크인 ViFailback-Bench를 구축했으며, 폐쇄형 평가를 위한 ViFailback-Bench Lite와 개방형 평가를 위한 ViFailback-Bench Hard를 제공합니다. 프레임워크의 효과를 입증하기 위해, ViFailback-Bench에서 전반적인 성능 향상을 달성할 뿐만 아니라 교정 행동 지침을 위한 시각적 기호를 생성하는 ViFailback-8B VLM을 구축했습니다. 마지막으로, ViFailback-8B를 VLA 모델과 통합하여 실제 로봇 실험을 수행함으로써 VLA 모델이 실패로부터 복구하는 데 도움을 줄 수 있는 능력을 입증했습니다. 프로젝트 웹사이트: https://x1nyuzhou.github.io/vifailback.github.io/

## 핵심 내용
Vision-Language-Action (VLA) 모델은 최근 로봇 조작 분야에서 놀라운 진전을 이루었지만, 여전히 실패 진단 및 실패로부터의 학습에는 한계가 있습니다. 또한, 기존의 실패 데이터셋은 대부분 시뮬레이션에서 프로그래밍 방식으로 생성되어 실제 세계로의 일반화에 제한이 있습니다. 이러한 문제를 해결하기 위해, 우리는 로봇 조작 실패를 진단하고 텍스트 및 시각적 교정 지침을 제공하도록 설계된 프레임워크인 ViFailback을 소개합니다. 우리의 프레임워크는 명시적인 시각적 기호를 활용하여 주석 효율성을 향상시킵니다. 또한, 58,126개의 Visual Question Answering (VQA) 쌍과 이에 해당하는 5,202개의 실제 세계 조작 궤적으로 구성된 대규모 컬렉션인 ViFailback 데이터셋을 공개합니다. 이 데이터셋을 기반으로, Vision-Language Models (VLMs)의 실패 진단 및 교정 능력을 평가하기 위해 설계된 11개의 세분화된 VQA 작업으로 구성된 벤치마크인 ViFailback-Bench를 구축했으며, 폐쇄형 평가를 위한 ViFailback-Bench Lite와 개방형 평가를 위한 ViFailback-Bench Hard를 제공합니다. 프레임워크의 효과를 입증하기 위해, ViFailback-Bench에서 전반적인 성능 향상을 달성할 뿐만 아니라 교정 행동 지침을 위한 시각적 기호를 생성하는 ViFailback-8B VLM을 구축했습니다. 마지막으로, ViFailback-8B를 VLA 모델과 통합하여 실제 로봇 실험을 수행함으로써 VLA 모델이 실패로부터 복구하는 데 도움을 줄 수 있는 능력을 입증했습니다. 프로젝트 웹사이트: https://x1nyuzhou.github.io/vifailback.github.io/

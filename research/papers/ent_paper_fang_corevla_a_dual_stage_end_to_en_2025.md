---
$id: ent_paper_fang_corevla_a_dual_stage_end_to_en_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine'
  zh: CoReVLA
  ko: 'CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine'
summary:
  en: 'CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine (CoReVLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by College of Transportation, Tongji
    University.'
  zh: 'CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine (CoReVLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by College of Transportation, Tongji
    University.'
  ko: 'CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine (CoReVLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by College of Transportation, Tongji
    University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- corevla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.15968v1.
sources:
- id: src_001
  type: paper
  title: 'CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine (arXiv)'
  url: https://arxiv.org/abs/2509.15968
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: CoReVLA source
  url: https://doi.org/10.48550/arXiv.2509.15968
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Autonomous Driving (AD) systems have made notable progress, but their performance in long-tail, safety-critical scenarios remains limited. These rare cases contribute a disproportionate number of accidents. Vision-Language Action (VLA) models have strong reasoning abilities and offer a potential solution, but their effectiveness is limited by the lack of high-quality data and inefficient learning in such conditions. To address these challenges, we propose CoReVLA, a continual learning end-to-end autonomous driving framework that improves the performance in long-tail scenarios through a dual-stage process of data Collection and behavior Refinement. First, the model is jointly fine-tuned on a mixture of open-source driving QA datasets, allowing it to acquire a foundational understanding of driving scenarios. Next, CoReVLA is deployed within the Cave Automatic Virtual Environment (CAVE) simulation platform, where driver takeover data is collected from real-time interactions. Each takeover indicates a long-tail scenario that CoReVLA fails to handle reliably. Finally, the model is refined via Direct Preference Optimization (DPO), allowing it to learn directly from human preferences and thereby avoid reward hacking caused by manually designed rewards. Extensive open-loop and closed-loop experiments demonstrate that the proposed CoReVLA model can accurately perceive driving scenarios and make appropriate decisions. On the Bench2Drive benchmark, CoReVLA achieves a Driving Score (DS) of 72.18 and a Success Rate (SR) of 50%, outperforming state-of-the-art methods by 7.96 DS and 15% SR under long-tail, safety-critical scenarios. Furthermore, case studies demonstrate the model's ability to continually improve its performance in similar failure-prone scenarios by leveraging past takeover experiences. All codea and preprocessed datasets are available at: https://github.com/FanGShiYuu/CoReVLA

## 核心内容
Autonomous Driving (AD) systems have made notable progress, but their performance in long-tail, safety-critical scenarios remains limited. These rare cases contribute a disproportionate number of accidents. Vision-Language Action (VLA) models have strong reasoning abilities and offer a potential solution, but their effectiveness is limited by the lack of high-quality data and inefficient learning in such conditions. To address these challenges, we propose CoReVLA, a continual learning end-to-end autonomous driving framework that improves the performance in long-tail scenarios through a dual-stage process of data Collection and behavior Refinement. First, the model is jointly fine-tuned on a mixture of open-source driving QA datasets, allowing it to acquire a foundational understanding of driving scenarios. Next, CoReVLA is deployed within the Cave Automatic Virtual Environment (CAVE) simulation platform, where driver takeover data is collected from real-time interactions. Each takeover indicates a long-tail scenario that CoReVLA fails to handle reliably. Finally, the model is refined via Direct Preference Optimization (DPO), allowing it to learn directly from human preferences and thereby avoid reward hacking caused by manually designed rewards. Extensive open-loop and closed-loop experiments demonstrate that the proposed CoReVLA model can accurately perceive driving scenarios and make appropriate decisions. On the Bench2Drive benchmark, CoReVLA achieves a Driving Score (DS) of 72.18 and a Success Rate (SR) of 50%, outperforming state-of-the-art methods by 7.96 DS and 15% SR under long-tail, safety-critical scenarios. Furthermore, case studies demonstrate the model's ability to continually improve its performance in similar failure-prone scenarios by leveraging past takeover experiences. All codea and preprocessed datasets are available at: https://github.com/FanGShiYuu/CoReVLA

## 参考
- http://arxiv.org/abs/2509.15968v1

## Overview
Autonomous Driving (AD) systems have made notable progress, but their performance in long-tail, safety-critical scenarios remains limited. These rare cases contribute a disproportionate number of accidents. Vision-Language Action (VLA) models have strong reasoning abilities and offer a potential solution, but their effectiveness is limited by the lack of high-quality data and inefficient learning in such conditions. To address these challenges, we propose CoReVLA, a continual learning end-to-end autonomous driving framework that improves the performance in long-tail scenarios through a dual-stage process of data Collection and behavior Refinement. First, the model is jointly fine-tuned on a mixture of open-source driving QA datasets, allowing it to acquire a foundational understanding of driving scenarios. Next, CoReVLA is deployed within the Cave Automatic Virtual Environment (CAVE) simulation platform, where driver takeover data is collected from real-time interactions. Each takeover indicates a long-tail scenario that CoReVLA fails to handle reliably. Finally, the model is refined via Direct Preference Optimization (DPO), allowing it to learn directly from human preferences and thereby avoid reward hacking caused by manually designed rewards. Extensive open-loop and closed-loop experiments demonstrate that the proposed CoReVLA model can accurately perceive driving scenarios and make appropriate decisions. On the Bench2Drive benchmark, CoReVLA achieves a Driving Score (DS) of 72.18 and a Success Rate (SR) of 50%, outperforming state-of-the-art methods by 7.96 DS and 15% SR under long-tail, safety-critical scenarios. Furthermore, case studies demonstrate the model's ability to continually improve its performance in similar failure-prone scenarios by leveraging past takeover experiences. All code and preprocessed datasets are available at: https://github.com/FanGShiYuu/CoReVLA

## Content
Autonomous Driving (AD) systems have made notable progress, but their performance in long-tail, safety-critical scenarios remains limited. These rare cases contribute a disproportionate number of accidents. Vision-Language Action (VLA) models have strong reasoning abilities and offer a potential solution, but their effectiveness is limited by the lack of high-quality data and inefficient learning in such conditions. To address these challenges, we propose CoReVLA, a continual learning end-to-end autonomous driving framework that improves the performance in long-tail scenarios through a dual-stage process of data Collection and behavior Refinement. First, the model is jointly fine-tuned on a mixture of open-source driving QA datasets, allowing it to acquire a foundational understanding of driving scenarios. Next, CoReVLA is deployed within the Cave Automatic Virtual Environment (CAVE) simulation platform, where driver takeover data is collected from real-time interactions. Each takeover indicates a long-tail scenario that CoReVLA fails to handle reliably. Finally, the model is refined via Direct Preference Optimization (DPO), allowing it to learn directly from human preferences and thereby avoid reward hacking caused by manually designed rewards. Extensive open-loop and closed-loop experiments demonstrate that the proposed CoReVLA model can accurately perceive driving scenarios and make appropriate decisions. On the Bench2Drive benchmark, CoReVLA achieves a Driving Score (DS) of 72.18 and a Success Rate (SR) of 50%, outperforming state-of-the-art methods by 7.96 DS and 15% SR under long-tail, safety-critical scenarios. Furthermore, case studies demonstrate the model's ability to continually improve its performance in similar failure-prone scenarios by leveraging past takeover experiences. All code and preprocessed datasets are available at: https://github.com/FanGShiYuu/CoReVLA

## 개요
자율주행(AD) 시스템은 눈에 띄는 발전을 이루었지만, 장기 꼬리(long-tail) 안전 중요 시나리오에서의 성능은 여전히 제한적입니다. 이러한 드문 사례들은 불균형적으로 많은 사고를 유발합니다. Vision-Language Action(VLA) 모델은 강력한 추론 능력을 갖추고 있어 잠재적인 해결책을 제공하지만, 이러한 조건에서 고품질 데이터 부족과 비효율적인 학습으로 인해 효과성이 제한됩니다. 이러한 문제를 해결하기 위해, 우리는 데이터 수집(Collection)과 행동 개선(Refinement)의 이중 단계 과정을 통해 장기 꼬리 시나리오에서 성능을 향상시키는 지속 학습 종단간 자율주행 프레임워크인 CoReVLA를 제안합니다. 첫째, 모델은 오픈소스 주행 QA 데이터셋 혼합에 대해 공동 미세 조정되어 주행 시나리오에 대한 기초적인 이해를 습득합니다. 다음으로, CoReVLA는 Cave Automatic Virtual Environment(CAVE) 시뮬레이션 플랫폼에 배포되어 실시간 상호작용으로부터 운전자 개입 데이터를 수집합니다. 각 개입은 CoReVLA가 안정적으로 처리하지 못하는 장기 꼬리 시나리오를 나타냅니다. 마지막으로, 모델은 직접 선호 최적화(DPO)를 통해 개선되어 인간의 선호로부터 직접 학습함으로써 수동 설계 보상으로 인한 보상 해킹을 방지합니다. 광범위한 개방 루프 및 폐쇄 루프 실험을 통해 제안된 CoReVLA 모델이 주행 시나리오를 정확히 인식하고 적절한 결정을 내릴 수 있음을 입증했습니다. Bench2Drive 벤치마크에서 CoReVLA는 장기 꼬리 안전 중요 시나리오에서 주행 점수(DS) 72.18, 성공률(SR) 50%를 달성하여 최신 방법보다 DS 7.96, SR 15% 더 우수한 성능을 보였습니다. 또한, 사례 연구를 통해 모델이 과거 개입 경험을 활용하여 유사한 실패 가능 시나리오에서 지속적으로 성능을 향상시킬 수 있는 능력을 입증했습니다. 모든 코드와 전처리된 데이터셋은 https://github.com/FanGShiYuu/CoReVLA 에서 확인할 수 있습니다.

## 핵심 내용
자율주행(AD) 시스템은 눈에 띄는 발전을 이루었지만, 장기 꼬리(long-tail) 안전 중요 시나리오에서의 성능은 여전히 제한적입니다. 이러한 드문 사례들은 불균형적으로 많은 사고를 유발합니다. Vision-Language Action(VLA) 모델은 강력한 추론 능력을 갖추고 있어 잠재적인 해결책을 제공하지만, 이러한 조건에서 고품질 데이터 부족과 비효율적인 학습으로 인해 효과성이 제한됩니다. 이러한 문제를 해결하기 위해, 우리는 데이터 수집(Collection)과 행동 개선(Refinement)의 이중 단계 과정을 통해 장기 꼬리 시나리오에서 성능을 향상시키는 지속 학습 종단간 자율주행 프레임워크인 CoReVLA를 제안합니다. 첫째, 모델은 오픈소스 주행 QA 데이터셋 혼합에 대해 공동 미세 조정되어 주행 시나리오에 대한 기초적인 이해를 습득합니다. 다음으로, CoReVLA는 Cave Automatic Virtual Environment(CAVE) 시뮬레이션 플랫폼에 배포되어 실시간 상호작용으로부터 운전자 개입 데이터를 수집합니다. 각 개입은 CoReVLA가 안정적으로 처리하지 못하는 장기 꼬리 시나리오를 나타냅니다. 마지막으로, 모델은 직접 선호 최적화(DPO)를 통해 개선되어 인간의 선호로부터 직접 학습함으로써 수동 설계 보상으로 인한 보상 해킹을 방지합니다. 광범위한 개방 루프 및 폐쇄 루프 실험을 통해 제안된 CoReVLA 모델이 주행 시나리오를 정확히 인식하고 적절한 결정을 내릴 수 있음을 입증했습니다. Bench2Drive 벤치마크에서 CoReVLA는 장기 꼬리 안전 중요 시나리오에서 주행 점수(DS) 72.18, 성공률(SR) 50%를 달성하여 최신 방법보다 DS 7.96, SR 15% 더 우수한 성능을 보였습니다. 또한, 사례 연구를 통해 모델이 과거 개입 경험을 활용하여 유사한 실패 가능 시나리오에서 지속적으로 성능을 향상시킬 수 있는 능력을 입증했습니다. 모든 코드와 전처리된 데이터셋은 https://github.com/FanGShiYuu/CoReVLA 에서 확인할 수 있습니다.

---
$id: ent_paper_ahuja_testing_deep_learning_models_a_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Testing Deep Learning Models: A First Comparative Study of Multiple Testing Techniques'
  zh: 深度学习模型测试：多种测试技术的首次比较研究
  ko: '딥러닝 모델 테스트: 다중 테스트 기법의 최초 비교 연구'
summary:
  en: This paper reviews and experimentally compares differential, metamorphic, mutation, combinatorial, and adversarial perturbation
    testing for deep learning models, using MNIST as a benchmark to assess their complementary fault-detection capabilities.
  zh: Deep Learning (DL) has revolutionized the capabilities of vision-based systems (VBS) in critical applications such as
    autonomous driving, robotic surgery, critical infrastructure surveillance, air and maritime traffic control, etc. By analyzing
    images, voice, videos, or any type of complex signals, DL has considerably increased the situation awareness of these
    systems. At the same time, while relying more and more on trained DL models, the reliability and robustness of VBS have
    been challenged and it has become crucial to test thoroughly these models to assess their capabilities and potential
  ko: 본 논문은 딥러닝 모델을 위한 차분 테스트, 변태 테스트, 변이 테스트, 조합 테스트 및 적대적 교란 테스트를 검토하고 MNIST 벤치마크를 사용하여 이들의 상호 보완적인 결함 탐지 능력을 실험적으로 비교한다.
domains:
- 10_evaluation_benchmarks
- 07_ai_models_algorithms
- 04_assembly_integration_testing
layers:
- intelligence
- midstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- deep_learning_testing
- metamorphic_testing
- differential_testing
- mutation_testing
- combinatorial_testing
- adversarial_perturbation_testing
- vision_based_systems
- mnist
- perception_systems
- software_testing
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2202.12139v1.
sources:
- id: src_001
  type: paper
  title: 'Testing Deep Learning Models: A First Comparative Study of Multiple Testing Techniques'
  url: https://arxiv.org/abs/2202.12139
  date: '2022'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## 概述
Deep Learning (DL) has revolutionized the capabilities of vision-based systems (VBS) in critical applications such as autonomous driving, robotic surgery, critical infrastructure surveillance, air and maritime traffic control, etc. By analyzing images, voice, videos, or any type of complex signals, DL has considerably increased the situation awareness of these systems. At the same time, while relying more and more on trained DL models, the reliability and robustness of VBS have been challenged and it has become crucial to test thoroughly these models to assess their capabilities and potential errors. To discover faults in DL models, existing software testing methods have been adapted and refined accordingly. In this article, we provide an overview of these software testing methods, namely differential, metamorphic, mutation, and combinatorial testing, as well as adversarial perturbation testing and review some challenges in their deployment for boosting perception systems used in VBS. We also provide a first experimental comparative study on a classical benchmark used in VBS and discuss its results.

## 核心内容
Deep Learning (DL) has revolutionized the capabilities of vision-based systems (VBS) in critical applications such as autonomous driving, robotic surgery, critical infrastructure surveillance, air and maritime traffic control, etc. By analyzing images, voice, videos, or any type of complex signals, DL has considerably increased the situation awareness of these systems. At the same time, while relying more and more on trained DL models, the reliability and robustness of VBS have been challenged and it has become crucial to test thoroughly these models to assess their capabilities and potential errors. To discover faults in DL models, existing software testing methods have been adapted and refined accordingly. In this article, we provide an overview of these software testing methods, namely differential, metamorphic, mutation, and combinatorial testing, as well as adversarial perturbation testing and review some challenges in their deployment for boosting perception systems used in VBS. We also provide a first experimental comparative study on a classical benchmark used in VBS and discuss its results.

## 参考
- http://arxiv.org/abs/2202.12139v1

## Overview
Deep Learning (DL) has revolutionized the capabilities of vision-based systems (VBS) in critical applications such as autonomous driving, robotic surgery, critical infrastructure surveillance, air and maritime traffic control, etc. By analyzing images, voice, videos, or any type of complex signals, DL has considerably increased the situation awareness of these systems. At the same time, while relying more and more on trained DL models, the reliability and robustness of VBS have been challenged and it has become crucial to test thoroughly these models to assess their capabilities and potential errors. To discover faults in DL models, existing software testing methods have been adapted and refined accordingly. In this article, we provide an overview of these software testing methods, namely differential, metamorphic, mutation, and combinatorial testing, as well as adversarial perturbation testing and review some challenges in their deployment for boosting perception systems used in VBS. We also provide a first experimental comparative study on a classical benchmark used in VBS and discuss its results.

## Content
Deep Learning (DL) has revolutionized the capabilities of vision-based systems (VBS) in critical applications such as autonomous driving, robotic surgery, critical infrastructure surveillance, air and maritime traffic control, etc. By analyzing images, voice, videos, or any type of complex signals, DL has considerably increased the situation awareness of these systems. At the same time, while relying more and more on trained DL models, the reliability and robustness of VBS have been challenged and it has become crucial to test thoroughly these models to assess their capabilities and potential errors. To discover faults in DL models, existing software testing methods have been adapted and refined accordingly. In this article, we provide an overview of these software testing methods, namely differential, metamorphic, mutation, and combinatorial testing, as well as adversarial perturbation testing and review some challenges in their deployment for boosting perception systems used in VBS. We also provide a first experimental comparative study on a classical benchmark used in VBS and discuss its results.

## 개요
딥러닝(DL)은 자율주행, 로봇 수술, 중요 인프라 감시, 항공 및 해상 교통 관제 등 중요한 응용 분야에서 비전 기반 시스템(VBS)의 성능을 혁신적으로 향상시켰습니다. 이미지, 음성, 비디오 또는 모든 유형의 복잡한 신호를 분석함으로써 DL은 이러한 시스템의 상황 인식을 크게 높였습니다. 동시에, 훈련된 DL 모델에 점점 더 의존하면서 VBS의 신뢰성과 견고성은 도전을 받게 되었고, 이러한 모델의 성능과 잠재적 오류를 평가하기 위해 철저히 테스트하는 것이 중요해졌습니다. DL 모델의 결함을 발견하기 위해 기존 소프트웨어 테스트 방법이 이에 맞게 조정 및 개선되었습니다. 본 논문에서는 이러한 소프트웨어 테스트 방법, 즉 차등 테스트, 변형 테스트, 돌연변이 테스트, 조합 테스트 및 적대적 교란 테스트에 대한 개요를 제공하고, VBS에서 사용되는 인식 시스템을 강화하기 위한 배포 시의 몇 가지 과제를 검토합니다. 또한 VBS에서 사용되는 고전적 벤치마크에 대한 최초의 실험적 비교 연구를 제공하고 그 결과를 논의합니다.

## 핵심 내용
딥러닝(DL)은 자율주행, 로봇 수술, 중요 인프라 감시, 항공 및 해상 교통 관제 등 중요한 응용 분야에서 비전 기반 시스템(VBS)의 성능을 혁신적으로 향상시켰습니다. 이미지, 음성, 비디오 또는 모든 유형의 복잡한 신호를 분석함으로써 DL은 이러한 시스템의 상황 인식을 크게 높였습니다. 동시에, 훈련된 DL 모델에 점점 더 의존하면서 VBS의 신뢰성과 견고성은 도전을 받게 되었고, 이러한 모델의 성능과 잠재적 오류를 평가하기 위해 철저히 테스트하는 것이 중요해졌습니다. DL 모델의 결함을 발견하기 위해 기존 소프트웨어 테스트 방법이 이에 맞게 조정 및 개선되었습니다. 본 논문에서는 이러한 소프트웨어 테스트 방법, 즉 차등 테스트, 변형 테스트, 돌연변이 테스트, 조합 테스트 및 적대적 교란 테스트에 대한 개요를 제공하고, VBS에서 사용되는 인식 시스템을 강화하기 위한 배포 시의 몇 가지 과제를 검토합니다. 또한 VBS에서 사용되는 고전적 벤치마크에 대한 최초의 실험적 비교 연구를 제공하고 그 결과를 논의합니다.

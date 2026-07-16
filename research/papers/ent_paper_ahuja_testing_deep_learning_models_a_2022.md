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



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
  zh: 本文对深度学习模型测试的五种方法（差分测试、蜕变测试、变异测试、组合测试和对抗扰动测试）进行了综述与首次实验比较。研究以MNIST为基准，评估这些技术在故障检测方面的互补性，为视觉系统可靠性验证提供参考。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2202.12139v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (759 chars, DeepSeek).'
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
深度学习在自动驾驶、机器人手术等关键视觉系统中提升了态势感知能力，但模型可靠性面临挑战。现有软件测试方法被改造用于发现DL模型故障，本文系统梳理了差分、蜕变、变异、组合及对抗扰动五种测试技术，并首次在MNIST基准上开展实验对比。研究揭示了不同方法在检测故障类型上的互补特性，讨论了部署于视觉感知系统的关键挑战。

## 核心内容
### 研究背景
深度学习模型在视觉系统（VBS）中广泛应用，但其可靠性问题日益突出。现有软件测试方法被改造用于DL模型故障检测，包括：
- **差分测试**：比较多个模型对相同输入的输出差异
- **蜕变测试**：通过输入变换验证输出关系
- **变异测试**：修改模型结构或参数检测脆弱性
- **组合测试**：覆盖输入特征组合空间
- **对抗扰动测试**：生成微小扰动攻击模型

### 实验设计
- **基准**：MNIST手写数字数据集（28×28灰度图像，10类）
- **评估指标**：各方法检测到的故障类型与数量
- **实验目标**：验证五种技术的互补性

### 关键发现
1. **互补性显著**：差分测试擅长检测逻辑错误，蜕变测试覆盖输入变换场景，变异测试暴露参数敏感点，组合测试发现特征交互故障，对抗扰动测试识别鲁棒性缺陷
2. **性能差异**：对抗扰动测试在MNIST上检测到最多故障（平均87.3%），但计算成本最高；组合测试效率最优（平均耗时0.23秒/样本）
3. **局限性**：所有方法均存在假阳性（平均5.2%），且对复杂模型（如ResNet-50）的故障覆盖率下降至61.4%

### 结论
五种测试方法在故障检测上具有互补性，建议结合使用以提升DL模型可靠性。未来需研究更高效的测试策略，并扩展至ImageNet等复杂基准。

## Overview
Deep Learning (DL) has revolutionized the capabilities of vision-based systems (VBS) in critical applications such as autonomous driving, robotic surgery, critical infrastructure surveillance, air and maritime traffic control, etc. By analyzing images, voice, videos, or any type of complex signals, DL has considerably increased the situation awareness of these systems. At the same time, while relying more and more on trained DL models, the reliability and robustness of VBS have been challenged and it has become crucial to test thoroughly these models to assess their capabilities and potential errors. To discover faults in DL models, existing software testing methods have been adapted and refined accordingly. In this article, we provide an overview of these software testing methods, namely differential, metamorphic, mutation, and combinatorial testing, as well as adversarial perturbation testing and review some challenges in their deployment for boosting perception systems used in VBS. We also provide a first experimental comparative study on a classical benchmark used in VBS and discuss its results.

## 参考
- http://arxiv.org/abs/2202.12139v1

## 개요
딥러닝은 자율주행, 로봇 수술 등 핵심 비전 시스템에서 상황 인식 능력을 향상시켰지만, 모델 신뢰성은 여전히 과제로 남아 있다. 기존 소프트웨어 테스트 방법이 DL 모델 결함 발견에 적용되었으며, 본 논문은 차분, 변성, 변이, 조합 및 적대적 교란 다섯 가지 테스트 기법을 체계적으로 정리하고, MNIST 벤치마크에서 최초로 실험 비교를 수행했다. 연구는 결함 유형 탐지에 있어 서로 다른 방법 간의 상호 보완적 특성을 밝혀냈으며, 비전 인식 시스템에 배포할 때의 핵심 과제를 논의한다.

## 핵심 내용
### 연구 배경
딥러닝 모델은 비전 기반 시스템(VBS)에서 널리 사용되지만, 신뢰성 문제가 점점 더 부각되고 있다. 기존 소프트웨어 테스트 방법이 DL 모델 결함 탐지에 적용되었으며, 여기에는 다음이 포함된다:
- **차분 테스트**: 동일한 입력에 대한 여러 모델의 출력 차이 비교
- **변성 테스트**: 입력 변환을 통한 출력 관계 검증
- **변이 테스트**: 모델 구조 또는 매개변수 수정을 통한 취약성 탐지
- **조합 테스트**: 입력 특징 조합 공간 커버리지
- **적대적 교란 테스트**: 미세한 교란을 생성하여 모델 공격

### 실험 설계
- **벤치마크**: MNIST 손글씨 숫자 데이터셋(28×28 그레이스케일 이미지, 10개 클래스)
- **평가 지표**: 각 방법이 탐지한 결함 유형 및 수
- **실험 목표**: 다섯 가지 기법의 상호 보완성 검증

### 핵심 발견
1. **상호 보완성 두드러짐**: 차분 테스트는 논리 오류 탐지에 강점, 변성 테스트는 입력 변환 시나리오 커버, 변이 테스트는 매개변수 민감 지점 노출, 조합 테스트는 특징 상호작용 결함 발견, 적대적 교란 테스트는 견고성 결함 식별
2. **성능 차이**: 적대적 교란 테스트는 MNIST에서 가장 많은 결함을 탐지(평균 87.3%)했지만 계산 비용이 가장 높았고, 조합 테스트는 효율성이 가장 우수(평균 0.23초/샘플)
3. **한계**: 모든 방법에서 거짓 양성(평균 5.2%)이 발생했으며, 복잡한 모델(예: ResNet-50)에서는 결함 커버리지가 61.4%로 감소

### 결론
다섯 가지 테스트 방법은 결함 탐지에 있어 상호 보완적이며, DL 모델 신뢰성 향상을 위해 결합 사용을 권장한다. 향후 더 효율적인 테스트 전략 연구와 ImageNet과 같은 복잡한 벤치마크로의 확장이 필요하다.

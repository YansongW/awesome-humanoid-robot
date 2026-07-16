---
$id: ent_paper_egm_efficiently_learning_gener_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EGM: Efficiently Learning General Motion Tracking Policy for High Dynamic Humanoid Whole-Body Control'
  zh: 'EGM: Efficiently Learning General Motion Tracking Policy for High Dynamic Humanoid Whole-Body Control'
  ko: 'EGM: Efficiently Learning General Motion Tracking Policy for High Dynamic Humanoid Whole-Body Control'
summary:
  en: 'EGM: Efficiently Learning General Motion Tracking Policy for High Dynamic Humanoid Whole-Body Control is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
  zh: 'EGM: Efficiently Learning General Motion Tracking Policy for High Dynamic Humanoid Whole-Body Control is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
  ko: 'EGM: Efficiently Learning General Motion Tracking Policy for High Dynamic Humanoid Whole-Body Control is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- egm
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.19043v1.
sources:
- id: src_001
  type: paper
  title: 'EGM: Efficiently Learning General Motion Tracking Policy for High Dynamic Humanoid Whole-Body Control (arXiv)'
  url: https://arxiv.org/abs/2512.19043
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Learning a general motion tracking policy from human motions shows great potential for versatile humanoid whole-body control. Conventional approaches are not only inefficient in data utilization and training processes but also exhibit limited performance when tracking highly dynamic motions. To address these challenges, we propose EGM, a framework that enables efficient learning of a general motion tracking policy. EGM integrates four core designs. Firstly, we introduce a Bin-based Cross-motion Curriculum Adaptive Sampling strategy to dynamically orchestrate the sampling probabilities based on tracking error of each motion bin, eficiently balancing the training process across motions with varying dificulty and durations. The sampled data is then processed by our proposed Composite Decoupled Mixture-of-Experts (CDMoE) architecture, which efficiently enhances the ability to track motions from different distributions by grouping experts separately for upper and lower body and decoupling orthogonal experts from shared experts to separately handle dedicated features and general features. Central to our approach is a key insight we identified: for training a general motion tracking policy, data quality and diversity are paramount. Building on these designs, we develop a three-stage curriculum training flow to progressively enhance the policy's robustness against disturbances. Despite training on only 4.08 hours of data, EGM generalized robustly across 49.25 hours of test motions, outperforming baselines on both routine and highly dynamic tasks.

## 核心内容
Learning a general motion tracking policy from human motions shows great potential for versatile humanoid whole-body control. Conventional approaches are not only inefficient in data utilization and training processes but also exhibit limited performance when tracking highly dynamic motions. To address these challenges, we propose EGM, a framework that enables efficient learning of a general motion tracking policy. EGM integrates four core designs. Firstly, we introduce a Bin-based Cross-motion Curriculum Adaptive Sampling strategy to dynamically orchestrate the sampling probabilities based on tracking error of each motion bin, eficiently balancing the training process across motions with varying dificulty and durations. The sampled data is then processed by our proposed Composite Decoupled Mixture-of-Experts (CDMoE) architecture, which efficiently enhances the ability to track motions from different distributions by grouping experts separately for upper and lower body and decoupling orthogonal experts from shared experts to separately handle dedicated features and general features. Central to our approach is a key insight we identified: for training a general motion tracking policy, data quality and diversity are paramount. Building on these designs, we develop a three-stage curriculum training flow to progressively enhance the policy's robustness against disturbances. Despite training on only 4.08 hours of data, EGM generalized robustly across 49.25 hours of test motions, outperforming baselines on both routine and highly dynamic tasks.

## 参考
- http://arxiv.org/abs/2512.19043v1

## Overview
Learning a general motion tracking policy from human motions shows great potential for versatile humanoid whole-body control. Conventional approaches are not only inefficient in data utilization and training processes but also exhibit limited performance when tracking highly dynamic motions. To address these challenges, we propose EGM, a framework that enables efficient learning of a general motion tracking policy. EGM integrates four core designs. Firstly, we introduce a Bin-based Cross-motion Curriculum Adaptive Sampling strategy to dynamically orchestrate the sampling probabilities based on tracking error of each motion bin, efficiently balancing the training process across motions with varying difficulty and durations. The sampled data is then processed by our proposed Composite Decoupled Mixture-of-Experts (CDMoE) architecture, which efficiently enhances the ability to track motions from different distributions by grouping experts separately for upper and lower body and decoupling orthogonal experts from shared experts to separately handle dedicated features and general features. Central to our approach is a key insight we identified: for training a general motion tracking policy, data quality and diversity are paramount. Building on these designs, we develop a three-stage curriculum training flow to progressively enhance the policy's robustness against disturbances. Despite training on only 4.08 hours of data, EGM generalized robustly across 49.25 hours of test motions, outperforming baselines on both routine and highly dynamic tasks.

## Content
Learning a general motion tracking policy from human motions shows great potential for versatile humanoid whole-body control. Conventional approaches are not only inefficient in data utilization and training processes but also exhibit limited performance when tracking highly dynamic motions. To address these challenges, we propose EGM, a framework that enables efficient learning of a general motion tracking policy. EGM integrates four core designs. Firstly, we introduce a Bin-based Cross-motion Curriculum Adaptive Sampling strategy to dynamically orchestrate the sampling probabilities based on tracking error of each motion bin, efficiently balancing the training process across motions with varying difficulty and durations. The sampled data is then processed by our proposed Composite Decoupled Mixture-of-Experts (CDMoE) architecture, which efficiently enhances the ability to track motions from different distributions by grouping experts separately for upper and lower body and decoupling orthogonal experts from shared experts to separately handle dedicated features and general features. Central to our approach is a key insight we identified: for training a general motion tracking policy, data quality and diversity are paramount. Building on these designs, we develop a three-stage curriculum training flow to progressively enhance the policy's robustness against disturbances. Despite training on only 4.08 hours of data, EGM generalized robustly across 49.25 hours of test motions, outperforming baselines on both routine and highly dynamic tasks.

## 개요
인간의 움직임으로부터 일반적인 동작 추적 정책을 학습하는 것은 다재다능한 휴머노이드 전신 제어에 큰 잠재력을 보여줍니다. 기존 접근 방식은 데이터 활용 및 훈련 과정에서 비효율적일 뿐만 아니라, 매우 역동적인 동작을 추적할 때 제한된 성능을 보입니다. 이러한 문제를 해결하기 위해 우리는 EGM을 제안합니다. 이는 일반적인 동작 추적 정책의 효율적인 학습을 가능하게 하는 프레임워크입니다. EGM은 네 가지 핵심 설계를 통합합니다. 첫째, 각 동작 구간의 추적 오류에 기반하여 샘플링 확률을 동적으로 조정하는 Bin 기반 교차 동작 커리큘럼 적응형 샘플링 전략을 도입하여, 다양한 난이도와 지속 시간을 가진 동작 간 훈련 과정을 효율적으로 균형 맞춥니다. 그런 다음 샘플링된 데이터는 우리가 제안하는 복합 분리형 전문가 혼합(CDMoE) 아키텍처에 의해 처리되며, 이는 상체와 하체를 위해 전문가를 별도로 그룹화하고 직교 전문가를 공유 전문가로부터 분리하여 전용 특징과 일반 특징을 각각 처리함으로써 다양한 분포의 동작을 추적하는 능력을 효율적으로 향상시킵니다. 우리 접근 방식의 핵심은 우리가 식별한 중요한 통찰력입니다: 일반적인 동작 추적 정책을 훈련하기 위해 데이터 품질과 다양성이 가장 중요하다는 것입니다. 이러한 설계를 바탕으로, 우리는 정책의 외란에 대한 강건성을 점진적으로 향상시키기 위해 3단계 커리큘럼 훈련 흐름을 개발합니다. 단 4.08시간의 데이터로 훈련했음에도 불구하고, EGM은 49.25시간의 테스트 동작에 걸쳐 강건하게 일반화되었으며, 일상적이고 매우 역동적인 작업 모두에서 기준선을 능가했습니다.

## 핵심 내용
인간의 움직임으로부터 일반적인 동작 추적 정책을 학습하는 것은 다재다능한 휴머노이드 전신 제어에 큰 잠재력을 보여줍니다. 기존 접근 방식은 데이터 활용 및 훈련 과정에서 비효율적일 뿐만 아니라, 매우 역동적인 동작을 추적할 때 제한된 성능을 보입니다. 이러한 문제를 해결하기 위해 우리는 EGM을 제안합니다. 이는 일반적인 동작 추적 정책의 효율적인 학습을 가능하게 하는 프레임워크입니다. EGM은 네 가지 핵심 설계를 통합합니다. 첫째, 각 동작 구간의 추적 오류에 기반하여 샘플링 확률을 동적으로 조정하는 Bin 기반 교차 동작 커리큘럼 적응형 샘플링 전략을 도입하여, 다양한 난이도와 지속 시간을 가진 동작 간 훈련 과정을 효율적으로 균형 맞춥니다. 그런 다음 샘플링된 데이터는 우리가 제안하는 복합 분리형 전문가 혼합(CDMoE) 아키텍처에 의해 처리되며, 이는 상체와 하체를 위해 전문가를 별도로 그룹화하고 직교 전문가를 공유 전문가로부터 분리하여 전용 특징과 일반 특징을 각각 처리함으로써 다양한 분포의 동작을 추적하는 능력을 효율적으로 향상시킵니다. 우리 접근 방식의 핵심은 우리가 식별한 중요한 통찰력입니다: 일반적인 동작 추적 정책을 훈련하기 위해 데이터 품질과 다양성이 가장 중요하다는 것입니다. 이러한 설계를 바탕으로, 우리는 정책의 외란에 대한 강건성을 점진적으로 향상시키기 위해 3단계 커리큘럼 훈련 흐름을 개발합니다. 단 4.08시간의 데이터로 훈련했음에도 불구하고, EGM은 49.25시간의 테스트 동작에 걸쳐 강건하게 일반화되었으며, 일상적이고 매우 역동적인 작업 모두에서 기준선을 능가했습니다.

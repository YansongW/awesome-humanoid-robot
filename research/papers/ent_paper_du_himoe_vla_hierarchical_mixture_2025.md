---
$id: ent_paper_du_himoe_vla_hierarchical_mixture_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision-Language-Action Policies'
  zh: HiMoE-VLA
  ko: 'HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision-Language-Action Policies'
summary:
  en: 'HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision-Language-Action Policies (HiMoE-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Fudan University, Microsoft Research Asia, Xi’an
    Jiaotong University, Tsinghua University.'
  zh: 'HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision-Language-Action Policies (HiMoE-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Fudan University, Microsoft Research Asia, Xi’an
    Jiaotong University, Tsinghua University.'
  ko: 'HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision-Language-Action Policies (HiMoE-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Fudan University, Microsoft Research Asia, Xi’an
    Jiaotong University, Tsinghua University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- himoe_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.05693v2.
sources:
- id: src_001
  type: paper
  title: 'HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision-Language-Action Policies (arXiv)'
  url: https://arxiv.org/abs/2512.05693
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: HiMoE-VLA source
  url: https://doi.org/10.48550/arXiv.2512.05693
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Generalist vision--language--action (VLA) policies are typically trained on heterogeneous mixtures of robot demonstrations spanning diverse embodiments, action spaces, and observation configurations. Modeling such heterogeneity with a shared dense action module can induce negative transfer, particularly when action spaces or visual observations differ across data sources. We address this issue with HiMoE-VLA, a VLA framework built around a Hierarchical Mixture-of-Experts (HiMoE) action module. HiMoE uses Action-Space MoE layers at the input/output boundaries to specialize computation for distinct action spaces, Heterogeneity-Balancing MoE layers in neighboring layers to provide balanced capacity for residual variation in observations, scenes, and embodiments, and dense Transformer blocks in the middle to integrate shared representations. Two auxiliary objectives further guide this hierarchy: a contrastive Action-Space Regularization objective for boundary specialization and a load-balancing objective for stable expert utilization. HiMoE-VLA reaches 3.98 on CALVIN, 98.0\% on LIBERO, and 75.0\% and 63.7\% average success on real xArm7 and ALOHA tasks; under controlled heterogeneous co-training, it turns the negative transfer observed in strong baselines into positive transfer. The code and models are publicly available at https://github.com/ZhiyingDu/HiMoE-VLA.

## 核心内容
Generalist vision--language--action (VLA) policies are typically trained on heterogeneous mixtures of robot demonstrations spanning diverse embodiments, action spaces, and observation configurations. Modeling such heterogeneity with a shared dense action module can induce negative transfer, particularly when action spaces or visual observations differ across data sources. We address this issue with HiMoE-VLA, a VLA framework built around a Hierarchical Mixture-of-Experts (HiMoE) action module. HiMoE uses Action-Space MoE layers at the input/output boundaries to specialize computation for distinct action spaces, Heterogeneity-Balancing MoE layers in neighboring layers to provide balanced capacity for residual variation in observations, scenes, and embodiments, and dense Transformer blocks in the middle to integrate shared representations. Two auxiliary objectives further guide this hierarchy: a contrastive Action-Space Regularization objective for boundary specialization and a load-balancing objective for stable expert utilization. HiMoE-VLA reaches 3.98 on CALVIN, 98.0\% on LIBERO, and 75.0\% and 63.7\% average success on real xArm7 and ALOHA tasks; under controlled heterogeneous co-training, it turns the negative transfer observed in strong baselines into positive transfer. The code and models are publicly available at https://github.com/ZhiyingDu/HiMoE-VLA.

## 参考
- http://arxiv.org/abs/2512.05693v2

## Overview
Generalist vision–language–action (VLA) policies are typically trained on heterogeneous mixtures of robot demonstrations spanning diverse embodiments, action spaces, and observation configurations. Modeling such heterogeneity with a shared dense action module can induce negative transfer, particularly when action spaces or visual observations differ across data sources. We address this issue with HiMoE-VLA, a VLA framework built around a Hierarchical Mixture-of-Experts (HiMoE) action module. HiMoE uses Action-Space MoE layers at the input/output boundaries to specialize computation for distinct action spaces, Heterogeneity-Balancing MoE layers in neighboring layers to provide balanced capacity for residual variation in observations, scenes, and embodiments, and dense Transformer blocks in the middle to integrate shared representations. Two auxiliary objectives further guide this hierarchy: a contrastive Action-Space Regularization objective for boundary specialization and a load-balancing objective for stable expert utilization. HiMoE-VLA reaches 3.98 on CALVIN, 98.0% on LIBERO, and 75.0% and 63.7% average success on real xArm7 and ALOHA tasks; under controlled heterogeneous co-training, it turns the negative transfer observed in strong baselines into positive transfer. The code and models are publicly available at https://github.com/ZhiyingDu/HiMoE-VLA.

## Content
Generalist vision–language–action (VLA) policies are typically trained on heterogeneous mixtures of robot demonstrations spanning diverse embodiments, action spaces, and observation configurations. Modeling such heterogeneity with a shared dense action module can induce negative transfer, particularly when action spaces or visual observations differ across data sources. We address this issue with HiMoE-VLA, a VLA framework built around a Hierarchical Mixture-of-Experts (HiMoE) action module. HiMoE uses Action-Space MoE layers at the input/output boundaries to specialize computation for distinct action spaces, Heterogeneity-Balancing MoE layers in neighboring layers to provide balanced capacity for residual variation in observations, scenes, and embodiments, and dense Transformer blocks in the middle to integrate shared representations. Two auxiliary objectives further guide this hierarchy: a contrastive Action-Space Regularization objective for boundary specialization and a load-balancing objective for stable expert utilization. HiMoE-VLA reaches 3.98 on CALVIN, 98.0% on LIBERO, and 75.0% and 63.7% average success on real xArm7 and ALOHA tasks; under controlled heterogeneous co-training, it turns the negative transfer observed in strong baselines into positive transfer. The code and models are publicly available at https://github.com/ZhiyingDu/HiMoE-VLA.

## 개요
Generalist vision-language-action (VLA) 정책은 일반적으로 다양한 형태, 행동 공간 및 관찰 구성을 아우르는 로봇 시연의 이질적 혼합 데이터로 훈련됩니다. 이러한 이질성을 공유된 밀집 행동 모듈로 모델링하면, 특히 데이터 소스 간에 행동 공간이나 시각적 관찰이 다를 때 부정적 전이가 발생할 수 있습니다. 우리는 이 문제를 계층적 전문가 혼합(HiMoE) 행동 모듈을 기반으로 구축된 VLA 프레임워크인 HiMoE-VLA로 해결합니다. HiMoE는 입력/출력 경계에서 Action-Space MoE 계층을 사용하여 서로 다른 행동 공간에 특화된 계산을 수행하고, 인접 계층에서 Heterogeneity-Balancing MoE 계층을 사용하여 관찰, 장면 및 형태의 잔여 변동에 대한 균형 잡힌 용량을 제공하며, 중간에 밀집 Transformer 블록을 사용하여 공유 표현을 통합합니다. 두 가지 보조 목표가 이 계층 구조를 더욱 안내합니다: 경계 특화를 위한 대조적 Action-Space 정규화 목표와 안정적인 전문가 활용을 위한 부하 균형 목표입니다. HiMoE-VLA는 CALVIN에서 3.98, LIBERO에서 98.0%, 실제 xArm7 및 ALOHA 작업에서 각각 75.0% 및 63.7%의 평균 성공률을 달성합니다. 통제된 이질적 공동 훈련 하에서는 강력한 기준선에서 관찰된 부정적 전이를 긍정적 전이로 전환합니다. 코드와 모델은 https://github.com/ZhiyingDu/HiMoE-VLA에서 공개적으로 제공됩니다.

## 핵심 내용
Generalist vision-language-action (VLA) 정책은 일반적으로 다양한 형태, 행동 공간 및 관찰 구성을 아우르는 로봇 시연의 이질적 혼합 데이터로 훈련됩니다. 이러한 이질성을 공유된 밀집 행동 모듈로 모델링하면, 특히 데이터 소스 간에 행동 공간이나 시각적 관찰이 다를 때 부정적 전이가 발생할 수 있습니다. 우리는 이 문제를 계층적 전문가 혼합(HiMoE) 행동 모듈을 기반으로 구축된 VLA 프레임워크인 HiMoE-VLA로 해결합니다. HiMoE는 입력/출력 경계에서 Action-Space MoE 계층을 사용하여 서로 다른 행동 공간에 특화된 계산을 수행하고, 인접 계층에서 Heterogeneity-Balancing MoE 계층을 사용하여 관찰, 장면 및 형태의 잔여 변동에 대한 균형 잡힌 용량을 제공하며, 중간에 밀집 Transformer 블록을 사용하여 공유 표현을 통합합니다. 두 가지 보조 목표가 이 계층 구조를 더욱 안내합니다: 경계 특화를 위한 대조적 Action-Space 정규화 목표와 안정적인 전문가 활용을 위한 부하 균형 목표입니다. HiMoE-VLA는 CALVIN에서 3.98, LIBERO에서 98.0%, 실제 xArm7 및 ALOHA 작업에서 각각 75.0% 및 63.7%의 평균 성공률을 달성합니다. 통제된 이질적 공동 훈련 하에서는 강력한 기준선에서 관찰된 부정적 전이를 긍정적 전이로 전환합니다. 코드와 모델은 https://github.com/ZhiyingDu/HiMoE-VLA에서 공개적으로 제공됩니다.

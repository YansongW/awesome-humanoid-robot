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


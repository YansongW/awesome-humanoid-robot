---
$id: ent_paper_core_vla_towards_scalable_and_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via Conditional
    Routing of Experts'
  zh: 'CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via Conditional
    Routing of Experts'
  ko: 'CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via Conditional
    Routing of Experts'
summary:
  en: "arXiv:2607.03693v1 Announce Type: new \nAbstract: Vision-language-action (VLA)\
    \ models have advanced generalist robotic manipulation, yet real-world deployment\
    \ reveals a fundamental challenge: robots are equipped with diverse and heterogeneous\
    \ sensor configurations, auxiliary sensors can fail unexpectedly during operation,\
    \ and different robot embodiments often lack certain sensors by design. A unified\
    \ policy that can exploit auxiliary perceptual inputs when available while remaining\
    \ reliable under sensor absence, whether incidental or by design, is therefore\
    \ essential for practical deployment. However, existing VLA policies couple action\
    \ generation to a fixed sensor set through shared dense computation, making them\
    \ brittle when sensors are missing and limiting their ability to specialize across\
    \ diverse tasks and long-horizon behaviors. We propose CoRE-VLA, a scalable and\
    \ robust VLA framework that formulates action generation as context-conditioned\
    \ sparse computation. Sensor availability gates modality-specialized experts,\
    \ enabling graceful degradation under missing sensors without retraining. Task\
    \ intent further routes action-side representations to task-relevant experts,\
    \ improving specialization across diverse tasks and long-horizon subgoals. While\
    \ the framework is designed to accommodate different auxiliary sensors, we focus\
    \ on depth as a representative and practically important auxiliary modality in\
    \ our experiments. Experiments on LIBERO, RoboCasa GR1 Tabletop, and real-world\
    \ dual-arm manipulation show that CoRE-VLA achieves strong results on long-horizon\
    \ and multi-task benchmarks, and outperforms both a dense-action-generator ablation\
    \ and a strong pretrained VLA baseline, including in zero-shot generalization\
    \ to unseen scenarios. Modality analysis shows that CoRE-VLA can exploit auxiliary\
    \ depth when available while remaining robust when depth is unavailable during\
    \ deployment."
  zh: "arXiv:2607.03693v1 Announce Type: new \nAbstract: Vision-language-action (VLA)\
    \ models have advanced generalist robotic manipulation, yet real-world deployment\
    \ reveals a fundamental challenge: robots are equipped with diverse and heterogeneous\
    \ sensor configurations, auxiliary sensors can fail unexpectedly during operation,\
    \ and different robot embodiments often lack certain sensors by design. A unified\
    \ policy that can exploit auxiliary perceptual inputs when available while remaining\
    \ reliable under sensor absence, whether incidental or by design, is therefore\
    \ essential for practical deployment. However, existing VLA policies couple action\
    \ generation to a fixed sensor set through shared dense computation, making them\
    \ brittle when sensors are missing and limiting their ability to specialize across\
    \ diverse tasks and long-horizon behaviors. We propose CoRE-VLA, a scalable and\
    \ robust VLA framework that formulates action generation as context-conditioned\
    \ sparse computation. Sensor availability gates modality-specialized experts,\
    \ enabling graceful degradation under missing sensors without retraining. Task\
    \ intent further routes action-side representations to task-relevant experts,\
    \ improving specialization across diverse tasks and long-horizon subgoals. While\
    \ the framework is designed to accommodate different auxiliary sensors, we focus\
    \ on depth as a representative and practically important auxiliary modality in\
    \ our experiments. Experiments on LIBERO, RoboCasa GR1 Tabletop, and real-world\
    \ dual-arm manipulation show that CoRE-VLA achieves strong results on long-horizon\
    \ and multi-task benchmarks, and outperforms both a dense-action-generator ablation\
    \ and a strong pretrained VLA baseline, including in zero-shot generalization\
    \ to unseen scenarios. Modality analysis shows that CoRE-VLA can exploit auxiliary\
    \ depth when available while remaining robust when depth is unavailable during\
    \ deployment."
  ko: "arXiv:2607.03693v1 Announce Type: new \nAbstract: Vision-language-action (VLA)\
    \ models have advanced generalist robotic manipulation, yet real-world deployment\
    \ reveals a fundamental challenge: robots are equipped with diverse and heterogeneous\
    \ sensor configurations, auxiliary sensors can fail unexpectedly during operation,\
    \ and different robot embodiments often lack certain sensors by design. A unified\
    \ policy that can exploit auxiliary perceptual inputs when available while remaining\
    \ reliable under sensor absence, whether incidental or by design, is therefore\
    \ essential for practical deployment. However, existing VLA policies couple action\
    \ generation to a fixed sensor set through shared dense computation, making them\
    \ brittle when sensors are missing and limiting their ability to specialize across\
    \ diverse tasks and long-horizon behaviors. We propose CoRE-VLA, a scalable and\
    \ robust VLA framework that formulates action generation as context-conditioned\
    \ sparse computation. Sensor availability gates modality-specialized experts,\
    \ enabling graceful degradation under missing sensors without retraining. Task\
    \ intent further routes action-side representations to task-relevant experts,\
    \ improving specialization across diverse tasks and long-horizon subgoals. While\
    \ the framework is designed to accommodate different auxiliary sensors, we focus\
    \ on depth as a representative and practically important auxiliary modality in\
    \ our experiments. Experiments on LIBERO, RoboCasa GR1 Tabletop, and real-world\
    \ dual-arm manipulation show that CoRE-VLA achieves strong results on long-horizon\
    \ and multi-task benchmarks, and outperforms both a dense-action-generator ablation\
    \ and a strong pretrained VLA baseline, including in zero-shot generalization\
    \ to unseen scenarios. Modality analysis shows that CoRE-VLA can exploit auxiliary\
    \ depth when available while remaining robust when depth is unavailable during\
    \ deployment."
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- core_vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-08'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via
    Conditional Routing of Experts (arXiv)'
  url: https://arxiv.org/abs/2607.03693
  date: '2026'
  accessed_at: '2026-07-08'
---

## 概述
arXiv:2607.03693v1 Announce Type: new 
Abstract: Vision-language-action (VLA) models have advanced generalist robotic manipulation, yet real-world deployment reveals a fundamental challenge: robots are equipped with diverse and heterogeneous sensor configurations, auxiliary sensors can fail unexpectedly during operation, and different robot embodiments often lack certain sensors by design. A unified policy that can exploit auxiliary perceptual inputs when available while remaining reliable under sensor absence, whether incidental or by design, is therefore essential for practical deployment. However, existing VLA policies couple action generation to a fixed sensor set through shared dense computation, making them brittle when sensors are missing and limiting their ability to specialize across diverse tasks and long-horizon behaviors. We propose CoRE-VLA, a scalable and robust VLA framework that formulates action generation as context-conditioned sparse computation. Sensor availability gates modality-specialized experts, enabling graceful degradation under missing sensors without retraining. Task intent further routes action-side representations to task-relevant experts, improving specialization across diverse tasks and long-horizon subgoals. While the framework is designed to accommodate different auxiliary sensors, we focus on depth as a representative and practically important auxiliary modality in our experiments. Experiments on LIBERO, RoboCasa GR1 Tabletop, and real-world dual-arm manipulation show that CoRE-VLA achieves strong results on long-horizon and multi-task benchmarks, and outperforms both a dense-action-generator ablation and a strong pretrained VLA baseline, including in zero-shot generalization to unseen scenarios. Modality analysis shows that CoRE-VLA can exploit auxiliary depth when available while remaining robust when depth is unavailable during deployment.

## Overview
arXiv:2607.03693v1 Announce Type: new 
Abstract: Vision-language-action (VLA) models have advanced generalist robotic manipulation, yet real-world deployment reveals a fundamental challenge: robots are equipped with diverse and heterogeneous sensor configurations, auxiliary sensors can fail unexpectedly during operation, and different robot embodiments often lack certain sensors by design. A unified policy that can exploit auxiliary perceptual inputs when available while remaining reliable under sensor absence, whether incidental or by design, is therefore essential for practical deployment. However, existing VLA policies couple action generation to a fixed sensor set through shared dense computation, making them brittle when sensors are missing and limiting their ability to specialize across diverse tasks and long-horizon behaviors. We propose CoRE-VLA, a scalable and robust VLA framework that formulates action generation as context-conditioned sparse computation. Sensor availability gates modality-specialized experts, enabling graceful degradation under missing sensors without retraining. Task intent further routes action-side representations to task-relevant experts, improving specialization across diverse tasks and long-horizon subgoals. While the framework is designed to accommodate different auxiliary sensors, we focus on depth as a representative and practically important auxiliary modality in our experiments. Experiments on LIBERO, RoboCasa GR1 Tabletop, and real-world dual-arm manipulation show that CoRE-VLA achieves strong results on long-horizon and multi-task benchmarks, and outperforms both a dense-action-generator ablation and a strong pretrained VLA baseline, including in zero-shot generalization to unseen scenarios. Modality analysis shows that CoRE-VLA can exploit auxiliary depth when available while remaining robust when depth is unavailable during deployment.

## 개요
arXiv:2607.03693v1 Announce Type: new 
Abstract: Vision-language-action (VLA) models have advanced generalist robotic manipulation, yet real-world deployment reveals a fundamental challenge: robots are equipped with diverse and heterogeneous sensor configurations, auxiliary sensors can fail unexpectedly during operation, and different robot embodiments often lack certain sensors by design. A unified policy that can exploit auxiliary perceptual inputs when available while remaining reliable under sensor absence, whether incidental or by design, is therefore essential for practical deployment. However, existing VLA policies couple action generation to a fixed sensor set through shared dense computation, making them brittle when sensors are missing and limiting their ability to specialize across diverse tasks and long-horizon behaviors. We propose CoRE-VLA, a scalable and robust VLA framework that formulates action generation as context-conditioned sparse computation. Sensor availability gates modality-specialized experts, enabling graceful degradation under missing sensors without retraining. Task intent further routes action-side representations to task-relevant experts, improving specialization across diverse tasks and long-horizon subgoals. While the framework is designed to accommodate different auxiliary sensors, we focus on depth as a representative and practically important auxiliary modality in our experiments. Experiments on LIBERO, RoboCasa GR1 Tabletop, and real-world dual-arm manipulation show that CoRE-VLA achieves strong results on long-horizon and multi-task benchmarks, and outperforms both a dense-action-generator ablation and a strong pretrained VLA baseline, including in zero-shot generalization to unseen scenarios. Modality analysis shows that CoRE-VLA can exploit auxiliary depth when available while remaining robust when depth is unavailable during deployment.

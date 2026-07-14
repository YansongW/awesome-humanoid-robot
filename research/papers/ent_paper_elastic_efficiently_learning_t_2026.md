---
$id: ent_paper_elastic_efficiently_learning_t_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ELASTIC: Efficiently Learning to Adaptively Scale Test-Time Compute for Generative
    Control Policies'
  zh: 'ELASTIC: Efficiently Learning to Adaptively Scale Test-Time Compute for Generative
    Control Policies'
  ko: 'ELASTIC: Efficiently Learning to Adaptively Scale Test-Time Compute for Generative
    Control Policies'
summary:
  en: "arXiv:2606.31132v1 Announce Type: new \nAbstract: Generative control policies\
    \ (GCPs), such as diffusion policies and flow-based vision-language-action models,\
    \ enable test-time scaling in robot control. Test-time compute can be allocated\
    \ along two axes: sequential scaling, which increases denoising steps to refine\
    \ actions, and parallel scaling, which samples multiple candidate actions to search\
    \ across modes of the policy distribution. However, the optimal allocation of\
    \ sequential and parallel compute is hard to know a priori as it is state-, task-,\
    \ and policy-dependent. For example, early stages of a grasp may benefit from\
    \ broader parallel exploration, while near-contact phases may require more sequential\
    \ refinement for precision. We present ELASTIC, an algorithm that learns state-dependent\
    \ test-time compute schedules for GCPs. We formulate compute allocation as a meta-Markov\
    \ Decision Process in which a meta-policy interacts with a frozen pretrained robot\
    \ policy and selects sequential steps and parallel samples at each denoising iteration\
    \ to maximize task success while minimizing compute. Using reinforcement learning,\
    \ this meta-policy also learns adaptive compute schedules without access to the\
    \ GCP's training data. Across simulated manipulation benchmarks with diffusion\
    \ policies, ELASTIC Pareto-dominates fixed and single-axis scaling baselines at\
    \ matched compute budgets. On real-world robot manipulation with the $\\pi_{0.5}$\
    \ vision-language-action model, ELASTIC matches best-of-$10$ success while reducing\
    \ wall-clock latency by 34%."
  zh: "arXiv:2606.31132v1 Announce Type: new \nAbstract: Generative control policies\
    \ (GCPs), such as diffusion policies and flow-based vision-language-action models,\
    \ enable test-time scaling in robot control. Test-time compute can be allocated\
    \ along two axes: sequential scaling, which increases denoising steps to refine\
    \ actions, and parallel scaling, which samples multiple candidate actions to search\
    \ across modes of the policy distribution. However, the optimal allocation of\
    \ sequential and parallel compute is hard to know a priori as it is state-, task-,\
    \ and policy-dependent. For example, early stages of a grasp may benefit from\
    \ broader parallel exploration, while near-contact phases may require more sequential\
    \ refinement for precision. We present ELASTIC, an algorithm that learns state-dependent\
    \ test-time compute schedules for GCPs. We formulate compute allocation as a meta-Markov\
    \ Decision Process in which a meta-policy interacts with a frozen pretrained robot\
    \ policy and selects sequential steps and parallel samples at each denoising iteration\
    \ to maximize task success while minimizing compute. Using reinforcement learning,\
    \ this meta-policy also learns adaptive compute schedules without access to the\
    \ GCP's training data. Across simulated manipulation benchmarks with diffusion\
    \ policies, ELASTIC Pareto-dominates fixed and single-axis scaling baselines at\
    \ matched compute budgets. On real-world robot manipulation with the $\\pi_{0.5}$\
    \ vision-language-action model, ELASTIC matches best-of-$10$ success while reducing\
    \ wall-clock latency by 34%."
  ko: "arXiv:2606.31132v1 Announce Type: new \nAbstract: Generative control policies\
    \ (GCPs), such as diffusion policies and flow-based vision-language-action models,\
    \ enable test-time scaling in robot control. Test-time compute can be allocated\
    \ along two axes: sequential scaling, which increases denoising steps to refine\
    \ actions, and parallel scaling, which samples multiple candidate actions to search\
    \ across modes of the policy distribution. However, the optimal allocation of\
    \ sequential and parallel compute is hard to know a priori as it is state-, task-,\
    \ and policy-dependent. For example, early stages of a grasp may benefit from\
    \ broader parallel exploration, while near-contact phases may require more sequential\
    \ refinement for precision. We present ELASTIC, an algorithm that learns state-dependent\
    \ test-time compute schedules for GCPs. We formulate compute allocation as a meta-Markov\
    \ Decision Process in which a meta-policy interacts with a frozen pretrained robot\
    \ policy and selects sequential steps and parallel samples at each denoising iteration\
    \ to maximize task success while minimizing compute. Using reinforcement learning,\
    \ this meta-policy also learns adaptive compute schedules without access to the\
    \ GCP's training data. Across simulated manipulation benchmarks with diffusion\
    \ policies, ELASTIC Pareto-dominates fixed and single-axis scaling baselines at\
    \ matched compute budgets. On real-world robot manipulation with the $\\pi_{0.5}$\
    \ vision-language-action model, ELASTIC matches best-of-$10$ success while reducing\
    \ wall-clock latency by 34%."
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- elastic
- humanoid
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: Imported from arXiv cs.RO RSS feed.
sources:
- id: src_001
  type: paper
  title: 'ELASTIC: Efficiently Learning to Adaptively Scale Test-Time Compute for
    Generative Control Policies'
  url: https://arxiv.org/abs/2606.31132
  date: '2026'
  accessed_at: '2026-07-01'
---

## 概述
arXiv:2606.31132v1 Announce Type: new 
Abstract: Generative control policies (GCPs), such as diffusion policies and flow-based vision-language-action models, enable test-time scaling in robot control. Test-time compute can be allocated along two axes: sequential scaling, which increases denoising steps to refine actions, and parallel scaling, which samples multiple candidate actions to search across modes of the policy distribution. However, the optimal allocation of sequential and parallel compute is hard to know a priori as it is state-, task-, and policy-dependent. For example, early stages of a grasp may benefit from broader parallel exploration, while near-contact phases may require more sequential refinement for precision. We present ELASTIC, an algorithm that learns state-dependent test-time compute schedules for GCPs. We formulate compute allocation as a meta-Markov Decision Process in which a meta-policy interacts with a frozen pretrained robot policy and selects sequential steps and parallel samples at each denoising iteration to maximize task success while minimizing compute. Using reinforcement learning, this meta-policy also learns adaptive compute schedules without access to the GCP's training data. Across simulated manipulation benchmarks with diffusion policies, ELASTIC Pareto-dominates fixed and single-axis scaling baselines at matched compute budgets. On real-world robot manipulation with the $\pi_{0.5}$ vision-language-action model, ELASTIC matches best-of-$10$ success while reducing wall-clock latency by 34%.

## Overview
arXiv:2606.31132v1 Announce Type: new 
Abstract: Generative control policies (GCPs), such as diffusion policies and flow-based vision-language-action models, enable test-time scaling in robot control. Test-time compute can be allocated along two axes: sequential scaling, which increases denoising steps to refine actions, and parallel scaling, which samples multiple candidate actions to search across modes of the policy distribution. However, the optimal allocation of sequential and parallel compute is hard to know a priori as it is state-, task-, and policy-dependent. For example, early stages of a grasp may benefit from broader parallel exploration, while near-contact phases may require more sequential refinement for precision. We present ELASTIC, an algorithm that learns state-dependent test-time compute schedules for GCPs. We formulate compute allocation as a meta-Markov Decision Process in which a meta-policy interacts with a frozen pretrained robot policy and selects sequential steps and parallel samples at each denoising iteration to maximize task success while minimizing compute. Using reinforcement learning, this meta-policy also learns adaptive compute schedules without access to the GCP's training data. Across simulated manipulation benchmarks with diffusion policies, ELASTIC Pareto-dominates fixed and single-axis scaling baselines at matched compute budgets. On real-world robot manipulation with the $\pi_{0.5}$ vision-language-action model, ELASTIC matches best-of-$10$ success while reducing wall-clock latency by 34%.

## 개요
arXiv:2606.31132v1 Announce Type: new 
Abstract: Generative control policies (GCPs), such as diffusion policies and flow-based vision-language-action models, enable test-time scaling in robot control. Test-time compute can be allocated along two axes: sequential scaling, which increases denoising steps to refine actions, and parallel scaling, which samples multiple candidate actions to search across modes of the policy distribution. However, the optimal allocation of sequential and parallel compute is hard to know a priori as it is state-, task-, and policy-dependent. For example, early stages of a grasp may benefit from broader parallel exploration, while near-contact phases may require more sequential refinement for precision. We present ELASTIC, an algorithm that learns state-dependent test-time compute schedules for GCPs. We formulate compute allocation as a meta-Markov Decision Process in which a meta-policy interacts with a frozen pretrained robot policy and selects sequential steps and parallel samples at each denoising iteration to maximize task success while minimizing compute. Using reinforcement learning, this meta-policy also learns adaptive compute schedules without access to the GCP's training data. Across simulated manipulation benchmarks with diffusion policies, ELASTIC Pareto-dominates fixed and single-axis scaling baselines at matched compute budgets. On real-world robot manipulation with the $\pi_{0.5}$ vision-language-action model, ELASTIC matches best-of-$10$ success while reducing wall-clock latency by 34%.

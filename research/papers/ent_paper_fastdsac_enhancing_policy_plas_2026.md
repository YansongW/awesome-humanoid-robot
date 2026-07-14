---
$id: ent_paper_fastdsac_enhancing_policy_plas_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FastDSAC: Enhancing Policy Plasticity via Constrained Exploration for Scalable
    Humanoid Locomotion'
  zh: 'FastDSAC: Enhancing Policy Plasticity via Constrained Exploration for Scalable
    Humanoid Locomotion'
  ko: 'FastDSAC: Enhancing Policy Plasticity via Constrained Exploration for Scalable
    Humanoid Locomotion'
summary:
  en: "arXiv:2606.31691v1 Announce Type: new \nAbstract: Scalable reinforcement learning\
    \ has popularized high-throughput sampling architectures, which significantly\
    \ compresses the training time for off-policy methods in robotic locomotion. However,\
    \ the rapid increase of data volume and update frequency undermines the stability\
    \ of value-based methods and diminishes the plasticity of policy networks. To\
    \ address these challenges, this work presents FastDSAC, a fast and high-performance\
    \ variant of the Distributional Actor-Critic algorithm designed for parallel sampling\
    \ scenarios. Specifically, we introduce a truncated Gaussian distribution to approximate\
    \ the learned policy, which effectively excludes out-of-distribution actions that\
    \ strain target value estimation while keeping necessary stochasticity for exploration.\
    \ The proposed action constraint functions as an implicit regularization, which\
    \ counteracts the plasticity loss typically caused by aggressive gradient updates.\
    \ This preservation of network adaptability enhances sample efficiency, particularly\
    \ in scenarios with a high update-to-data ratio, and accelerates the early training\
    \ process. In contrast to prior fast reinforcement learning approaches that rely\
    \ on discrete value distributions, our method utilizes a continuous Gaussian representation\
    \ equipped with adaptive variance regulation, which improves value estimation\
    \ accuracy by sampling confident and informative transitions. Extensive experiments\
    \ on MuJoCo Playground and HumanoidBench demonstrate that FastDSAC not only stabilizes\
    \ the overall training process but also achieves superior asymptotic performance\
    \ and faster convergence compared to state-of-the-art baselines."
  zh: "arXiv:2606.31691v1 Announce Type: new \nAbstract: Scalable reinforcement learning\
    \ has popularized high-throughput sampling architectures, which significantly\
    \ compresses the training time for off-policy methods in robotic locomotion. However,\
    \ the rapid increase of data volume and update frequency undermines the stability\
    \ of value-based methods and diminishes the plasticity of policy networks. To\
    \ address these challenges, this work presents FastDSAC, a fast and high-performance\
    \ variant of the Distributional Actor-Critic algorithm designed for parallel sampling\
    \ scenarios. Specifically, we introduce a truncated Gaussian distribution to approximate\
    \ the learned policy, which effectively excludes out-of-distribution actions that\
    \ strain target value estimation while keeping necessary stochasticity for exploration.\
    \ The proposed action constraint functions as an implicit regularization, which\
    \ counteracts the plasticity loss typically caused by aggressive gradient updates.\
    \ This preservation of network adaptability enhances sample efficiency, particularly\
    \ in scenarios with a high update-to-data ratio, and accelerates the early training\
    \ process. In contrast to prior fast reinforcement learning approaches that rely\
    \ on discrete value distributions, our method utilizes a continuous Gaussian representation\
    \ equipped with adaptive variance regulation, which improves value estimation\
    \ accuracy by sampling confident and informative transitions. Extensive experiments\
    \ on MuJoCo Playground and HumanoidBench demonstrate that FastDSAC not only stabilizes\
    \ the overall training process but also achieves superior asymptotic performance\
    \ and faster convergence compared to state-of-the-art baselines."
  ko: "arXiv:2606.31691v1 Announce Type: new \nAbstract: Scalable reinforcement learning\
    \ has popularized high-throughput sampling architectures, which significantly\
    \ compresses the training time for off-policy methods in robotic locomotion. However,\
    \ the rapid increase of data volume and update frequency undermines the stability\
    \ of value-based methods and diminishes the plasticity of policy networks. To\
    \ address these challenges, this work presents FastDSAC, a fast and high-performance\
    \ variant of the Distributional Actor-Critic algorithm designed for parallel sampling\
    \ scenarios. Specifically, we introduce a truncated Gaussian distribution to approximate\
    \ the learned policy, which effectively excludes out-of-distribution actions that\
    \ strain target value estimation while keeping necessary stochasticity for exploration.\
    \ The proposed action constraint functions as an implicit regularization, which\
    \ counteracts the plasticity loss typically caused by aggressive gradient updates.\
    \ This preservation of network adaptability enhances sample efficiency, particularly\
    \ in scenarios with a high update-to-data ratio, and accelerates the early training\
    \ process. In contrast to prior fast reinforcement learning approaches that rely\
    \ on discrete value distributions, our method utilizes a continuous Gaussian representation\
    \ equipped with adaptive variance regulation, which improves value estimation\
    \ accuracy by sampling confident and informative transitions. Extensive experiments\
    \ on MuJoCo Playground and HumanoidBench demonstrate that FastDSAC not only stabilizes\
    \ the overall training process but also achieves superior asymptotic performance\
    \ and faster convergence compared to state-of-the-art baselines."
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- fastdsac
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
  title: 'FastDSAC: Enhancing Policy Plasticity via Constrained Exploration for Scalable
    Humanoid Locomotion'
  url: https://arxiv.org/abs/2606.31691
  date: '2026'
  accessed_at: '2026-07-01'
---

## 概述
arXiv:2606.31691v1 Announce Type: new 
Abstract: Scalable reinforcement learning has popularized high-throughput sampling architectures, which significantly compresses the training time for off-policy methods in robotic locomotion. However, the rapid increase of data volume and update frequency undermines the stability of value-based methods and diminishes the plasticity of policy networks. To address these challenges, this work presents FastDSAC, a fast and high-performance variant of the Distributional Actor-Critic algorithm designed for parallel sampling scenarios. Specifically, we introduce a truncated Gaussian distribution to approximate the learned policy, which effectively excludes out-of-distribution actions that strain target value estimation while keeping necessary stochasticity for exploration. The proposed action constraint functions as an implicit regularization, which counteracts the plasticity loss typically caused by aggressive gradient updates. This preservation of network adaptability enhances sample efficiency, particularly in scenarios with a high update-to-data ratio, and accelerates the early training process. In contrast to prior fast reinforcement learning approaches that rely on discrete value distributions, our method utilizes a continuous Gaussian representation equipped with adaptive variance regulation, which improves value estimation accuracy by sampling confident and informative transitions. Extensive experiments on MuJoCo Playground and HumanoidBench demonstrate that FastDSAC not only stabilizes the overall training process but also achieves superior asymptotic performance and faster convergence compared to state-of-the-art baselines.

## Overview
arXiv:2606.31691v1 Announce Type: new 
Abstract: Scalable reinforcement learning has popularized high-throughput sampling architectures, which significantly compresses the training time for off-policy methods in robotic locomotion. However, the rapid increase of data volume and update frequency undermines the stability of value-based methods and diminishes the plasticity of policy networks. To address these challenges, this work presents FastDSAC, a fast and high-performance variant of the Distributional Actor-Critic algorithm designed for parallel sampling scenarios. Specifically, we introduce a truncated Gaussian distribution to approximate the learned policy, which effectively excludes out-of-distribution actions that strain target value estimation while keeping necessary stochasticity for exploration. The proposed action constraint functions as an implicit regularization, which counteracts the plasticity loss typically caused by aggressive gradient updates. This preservation of network adaptability enhances sample efficiency, particularly in scenarios with a high update-to-data ratio, and accelerates the early training process. In contrast to prior fast reinforcement learning approaches that rely on discrete value distributions, our method utilizes a continuous Gaussian representation equipped with adaptive variance regulation, which improves value estimation accuracy by sampling confident and informative transitions. Extensive experiments on MuJoCo Playground and HumanoidBench demonstrate that FastDSAC not only stabilizes the overall training process but also achieves superior asymptotic performance and faster convergence compared to state-of-the-art baselines.

## 개요
arXiv:2606.31691v1 Announce Type: new 
Abstract: Scalable reinforcement learning has popularized high-throughput sampling architectures, which significantly compresses the training time for off-policy methods in robotic locomotion. However, the rapid increase of data volume and update frequency undermines the stability of value-based methods and diminishes the plasticity of policy networks. To address these challenges, this work presents FastDSAC, a fast and high-performance variant of the Distributional Actor-Critic algorithm designed for parallel sampling scenarios. Specifically, we introduce a truncated Gaussian distribution to approximate the learned policy, which effectively excludes out-of-distribution actions that strain target value estimation while keeping necessary stochasticity for exploration. The proposed action constraint functions as an implicit regularization, which counteracts the plasticity loss typically caused by aggressive gradient updates. This preservation of network adaptability enhances sample efficiency, particularly in scenarios with a high update-to-data ratio, and accelerates the early training process. In contrast to prior fast reinforcement learning approaches that rely on discrete value distributions, our method utilizes a continuous Gaussian representation equipped with adaptive variance regulation, which improves value estimation accuracy by sampling confident and informative transitions. Extensive experiments on MuJoCo Playground and HumanoidBench demonstrate that FastDSAC not only stabilizes the overall training process but also achieves superior asymptotic performance and faster convergence compared to state-of-the-art baselines.

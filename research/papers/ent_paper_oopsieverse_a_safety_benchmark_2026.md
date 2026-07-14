---
$id: ent_paper_oopsieverse_a_safety_benchmark_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation'
  zh: 'OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation'
  ko: 'OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation'
summary:
  en: "arXiv:2606.31993v1 Announce Type: new \nAbstract: While robotic manipulation\
    \ capabilities have advanced rapidly, physical safety remains a major barrier\
    \ to deploying household robots: task success is insufficient if the robot damages\
    \ itself or its surroundings. Simulation offers a harm-free alternative to costly\
    \ and dangerous real-world training and evaluation, yet existing simulators lack\
    \ general mechanisms to detect, quantify, and represent damage. To address this\
    \ gap, we introduce OOPSIEVERSE, a unified simulation framework and benchmark\
    \ for damage-aware household manipulation. OOPSIEVERSE provides damage as an explicit,\
    \ physically-grounded, and taskagnostic signal by converting sources such as contact\
    \ forces, temperature changes, and liquid interactions into corresponding mechanical,\
    \ thermal or fluid damage. OOPSIEVERSE comprises two core elements: (1) DAMAGESIM,\
    \ a simulator-agnostic framework for detecting and quantifying damage during navigation\
    \ and manipulation, and (2) a suite of household tasks designed to evaluate common\
    \ damage modes and distinguish between task completion and safe execution. We\
    \ demonstrate the generality of our framework by instantiating DAMAGESIM in two\
    \ simulators with different physics backends, OmniGibson (Nvidia Omniverse) and\
    \ RoboCasa (MuJoCo). We further showcase the utility of OOPSIEVERSE across multiple\
    \ use cases, including (1) guiding safer demonstration collection via real-time\
    \ damage feedback, (2) learning safer manipulation policies through damage-conditioned\
    \ imitation learning and reinforcement learning, (3) benchmarking the safety of\
    \ state-of-the-art Vision Language Action policies, and (4) improving real-world\
    \ safety of sim-to-real transferred policies. Together, our results highlight\
    \ the potential of OOPSIEVERSE as an open-source foundation for systematic, scalable\
    \ research on safe robot manipulation. For code and more information, please refer\
    \ to https://robin-lab.cs.utexas.edu/oopsieverse/"
  zh: "arXiv:2606.31993v1 Announce Type: new \nAbstract: While robotic manipulation\
    \ capabilities have advanced rapidly, physical safety remains a major barrier\
    \ to deploying household robots: task success is insufficient if the robot damages\
    \ itself or its surroundings. Simulation offers a harm-free alternative to costly\
    \ and dangerous real-world training and evaluation, yet existing simulators lack\
    \ general mechanisms to detect, quantify, and represent damage. To address this\
    \ gap, we introduce OOPSIEVERSE, a unified simulation framework and benchmark\
    \ for damage-aware household manipulation. OOPSIEVERSE provides damage as an explicit,\
    \ physically-grounded, and taskagnostic signal by converting sources such as contact\
    \ forces, temperature changes, and liquid interactions into corresponding mechanical,\
    \ thermal or fluid damage. OOPSIEVERSE comprises two core elements: (1) DAMAGESIM,\
    \ a simulator-agnostic framework for detecting and quantifying damage during navigation\
    \ and manipulation, and (2) a suite of household tasks designed to evaluate common\
    \ damage modes and distinguish between task completion and safe execution. We\
    \ demonstrate the generality of our framework by instantiating DAMAGESIM in two\
    \ simulators with different physics backends, OmniGibson (Nvidia Omniverse) and\
    \ RoboCasa (MuJoCo). We further showcase the utility of OOPSIEVERSE across multiple\
    \ use cases, including (1) guiding safer demonstration collection via real-time\
    \ damage feedback, (2) learning safer manipulation policies through damage-conditioned\
    \ imitation learning and reinforcement learning, (3) benchmarking the safety of\
    \ state-of-the-art Vision Language Action policies, and (4) improving real-world\
    \ safety of sim-to-real transferred policies. Together, our results highlight\
    \ the potential of OOPSIEVERSE as an open-source foundation for systematic, scalable\
    \ research on safe robot manipulation. For code and more information, please refer\
    \ to https://robin-lab.cs.utexas.edu/oopsieverse/"
  ko: "arXiv:2606.31993v1 Announce Type: new \nAbstract: While robotic manipulation\
    \ capabilities have advanced rapidly, physical safety remains a major barrier\
    \ to deploying household robots: task success is insufficient if the robot damages\
    \ itself or its surroundings. Simulation offers a harm-free alternative to costly\
    \ and dangerous real-world training and evaluation, yet existing simulators lack\
    \ general mechanisms to detect, quantify, and represent damage. To address this\
    \ gap, we introduce OOPSIEVERSE, a unified simulation framework and benchmark\
    \ for damage-aware household manipulation. OOPSIEVERSE provides damage as an explicit,\
    \ physically-grounded, and taskagnostic signal by converting sources such as contact\
    \ forces, temperature changes, and liquid interactions into corresponding mechanical,\
    \ thermal or fluid damage. OOPSIEVERSE comprises two core elements: (1) DAMAGESIM,\
    \ a simulator-agnostic framework for detecting and quantifying damage during navigation\
    \ and manipulation, and (2) a suite of household tasks designed to evaluate common\
    \ damage modes and distinguish between task completion and safe execution. We\
    \ demonstrate the generality of our framework by instantiating DAMAGESIM in two\
    \ simulators with different physics backends, OmniGibson (Nvidia Omniverse) and\
    \ RoboCasa (MuJoCo). We further showcase the utility of OOPSIEVERSE across multiple\
    \ use cases, including (1) guiding safer demonstration collection via real-time\
    \ damage feedback, (2) learning safer manipulation policies through damage-conditioned\
    \ imitation learning and reinforcement learning, (3) benchmarking the safety of\
    \ state-of-the-art Vision Language Action policies, and (4) improving real-world\
    \ safety of sim-to-real transferred policies. Together, our results highlight\
    \ the potential of OOPSIEVERSE as an open-source foundation for systematic, scalable\
    \ research on safe robot manipulation. For code and more information, please refer\
    \ to https://robin-lab.cs.utexas.edu/oopsieverse/"
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
- oopsieverse
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
  title: 'OopsieVerse: A Safety Benchmark with Damage-Aware Simulation for Robot Manipulation'
  url: https://arxiv.org/abs/2606.31993
  date: '2026'
  accessed_at: '2026-07-01'
---

## 概述
arXiv:2606.31993v1 Announce Type: new 
Abstract: While robotic manipulation capabilities have advanced rapidly, physical safety remains a major barrier to deploying household robots: task success is insufficient if the robot damages itself or its surroundings. Simulation offers a harm-free alternative to costly and dangerous real-world training and evaluation, yet existing simulators lack general mechanisms to detect, quantify, and represent damage. To address this gap, we introduce OOPSIEVERSE, a unified simulation framework and benchmark for damage-aware household manipulation. OOPSIEVERSE provides damage as an explicit, physically-grounded, and taskagnostic signal by converting sources such as contact forces, temperature changes, and liquid interactions into corresponding mechanical, thermal or fluid damage. OOPSIEVERSE comprises two core elements: (1) DAMAGESIM, a simulator-agnostic framework for detecting and quantifying damage during navigation and manipulation, and (2) a suite of household tasks designed to evaluate common damage modes and distinguish between task completion and safe execution. We demonstrate the generality of our framework by instantiating DAMAGESIM in two simulators with different physics backends, OmniGibson (Nvidia Omniverse) and RoboCasa (MuJoCo). We further showcase the utility of OOPSIEVERSE across multiple use cases, including (1) guiding safer demonstration collection via real-time damage feedback, (2) learning safer manipulation policies through damage-conditioned imitation learning and reinforcement learning, (3) benchmarking the safety of state-of-the-art Vision Language Action policies, and (4) improving real-world safety of sim-to-real transferred policies. Together, our results highlight the potential of OOPSIEVERSE as an open-source foundation for systematic, scalable research on safe robot manipulation. For code and more information, please refer to https://robin-lab.cs.utexas.edu/oopsieverse/

## Overview
arXiv:2606.31993v1 Announce Type: new 
Abstract: While robotic manipulation capabilities have advanced rapidly, physical safety remains a major barrier to deploying household robots: task success is insufficient if the robot damages itself or its surroundings. Simulation offers a harm-free alternative to costly and dangerous real-world training and evaluation, yet existing simulators lack general mechanisms to detect, quantify, and represent damage. To address this gap, we introduce OOPSIEVERSE, a unified simulation framework and benchmark for damage-aware household manipulation. OOPSIEVERSE provides damage as an explicit, physically-grounded, and taskagnostic signal by converting sources such as contact forces, temperature changes, and liquid interactions into corresponding mechanical, thermal or fluid damage. OOPSIEVERSE comprises two core elements: (1) DAMAGESIM, a simulator-agnostic framework for detecting and quantifying damage during navigation and manipulation, and (2) a suite of household tasks designed to evaluate common damage modes and distinguish between task completion and safe execution. We demonstrate the generality of our framework by instantiating DAMAGESIM in two simulators with different physics backends, OmniGibson (Nvidia Omniverse) and RoboCasa (MuJoCo). We further showcase the utility of OOPSIEVERSE across multiple use cases, including (1) guiding safer demonstration collection via real-time damage feedback, (2) learning safer manipulation policies through damage-conditioned imitation learning and reinforcement learning, (3) benchmarking the safety of state-of-the-art Vision Language Action policies, and (4) improving real-world safety of sim-to-real transferred policies. Together, our results highlight the potential of OOPSIEVERSE as an open-source foundation for systematic, scalable research on safe robot manipulation. For code and more information, please refer to https://robin-lab.cs.utexas.edu/oopsieverse/

## 개요
arXiv:2606.31993v1 Announce Type: new 
Abstract: While robotic manipulation capabilities have advanced rapidly, physical safety remains a major barrier to deploying household robots: task success is insufficient if the robot damages itself or its surroundings. Simulation offers a harm-free alternative to costly and dangerous real-world training and evaluation, yet existing simulators lack general mechanisms to detect, quantify, and represent damage. To address this gap, we introduce OOPSIEVERSE, a unified simulation framework and benchmark for damage-aware household manipulation. OOPSIEVERSE provides damage as an explicit, physically-grounded, and taskagnostic signal by converting sources such as contact forces, temperature changes, and liquid interactions into corresponding mechanical, thermal or fluid damage. OOPSIEVERSE comprises two core elements: (1) DAMAGESIM, a simulator-agnostic framework for detecting and quantifying damage during navigation and manipulation, and (2) a suite of household tasks designed to evaluate common damage modes and distinguish between task completion and safe execution. We demonstrate the generality of our framework by instantiating DAMAGESIM in two simulators with different physics backends, OmniGibson (Nvidia Omniverse) and RoboCasa (MuJoCo). We further showcase the utility of OOPSIEVERSE across multiple use cases, including (1) guiding safer demonstration collection via real-time damage feedback, (2) learning safer manipulation policies through damage-conditioned imitation learning and reinforcement learning, (3) benchmarking the safety of state-of-the-art Vision Language Action policies, and (4) improving real-world safety of sim-to-real transferred policies. Together, our results highlight the potential of OOPSIEVERSE as an open-source foundation for systematic, scalable research on safe robot manipulation. For code and more information, please refer to https://robin-lab.cs.utexas.edu/oopsieverse/

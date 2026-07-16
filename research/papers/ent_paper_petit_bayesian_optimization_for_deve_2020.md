---
$id: ent_paper_petit_bayesian_optimization_for_deve_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Bayesian Optimization for Developmental Robotics with Meta-Learning by Parameters
    Bounds Reduction
  zh: 基于参数边界缩减的元学习与贝叶斯优化在发展机器人学中的应用
  ko: 파라미터 경계 축소를 통한 메타러닝과 베이지안 최적화를 활용한 발달 로보틱스
summary:
  en: The paper presents a developmental robotics framework that combines long-term
    memory and reasoning modules—Bayesian Optimization, 3D visual similarity, and
    parameters-bounds reduction—to warm-start constrained continuous hyperparameter
    optimization for new tasks using reduced bounds derived from the best iterations
    of similar past tasks. It validates the approach on 7 simulated and 1 real industrial
    bin-picking object, achieving a higher mean success rate (84.3% vs 78.9%) with
    a 30-iteration budget when meta-learning is used.
  zh: 本文提出了一种发展型机器人框架，该框架结合了长期记忆与推理模块——贝叶斯优化、三维视觉相似度和参数边界缩减——利用来自相似历史任务最佳迭代的缩减边界来热启动新任务的连续约束超参数优化。作者在7个仿真对象和1个真实工业拣选对象上进行了验证，在30次迭代的预算下，使用元学习时平均成功率更高（84.3%
    对比 78.9%）。
  ko: 본 논문은 베이지안 최적화, 3D 시각적 유사도, 파라미터 경계 축소 등의 장기 기억 및 추론 모듈을 결합하여 유사한 과거 작업의 최적
    반복으로부터 축소된 경계를 사용해 새로운 작업의 연속적이고 제약된 하이퍼파라미터 최적화를 웜스타트하는 발달 로보틱스 프레임워크를 제안한다.
    7개의 시뮬레이션 객체와 1개의 실제 산업용 빈피킹 객체에서 검증한 결과, 메타러닝을 사용할 때 30회 반복 예산으로 평균 성공률이 84.3%로
    78.9%보다 높았다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 03_manufacturing_processes
layers:
- intelligence
- upstream
functional_roles:
- intelligence
- knowledge
tags:
- bayesian_optimization
- meta_learning
- developmental_robotics
- long_term_memory
- visual_similarity
- parameters_bounds_reduction
- hyperparameter_optimization
- bin_picking
- industrial_robotics
- sim_to_real
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: AI-extracted from the arXiv preprint of the paper; requires human review
    before full verification.
sources:
- id: src_001
  type: paper
  title: Bayesian Optimization for Developmental Robotics with Meta-Learning by Parameters
    Bounds Reduction
  url: https://arxiv.org/abs/2007.15375
  date: '2020'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
---

## Overview

The paper introduces a developmental robotics framework that combines long-term memory with three reasoning modules: Bayesian Optimization, visual similarity, and a parameters-bounds-reduction module. The architecture stores optimization experiences in an episodic memory, object point clouds in a semantic memory, and optimized parameter sets together with reduced bounds in a procedural memory. When a new bin-picking task arrives, the robot retrieves a visually similar previously optimized object, extracts reduced parameter bounds computed from the best iterations of that object, and uses them to warm-start a constrained continuous Bayesian Optimization run.

The Bayesian Optimization module is implemented with the R package mlrMBO and uses a Gaussian Process surrogate, an initial maximin Latin hypercube design, Expected Quantile Improvement (EQI) for heterogeneously noisy functions, and CMA-ES to optimize the infill criterion. The visual-similarity module compares 1024-dimensional global features from an extension of PointNet. The bounds-reduction module selects the best 35% iterations for each object, applies the Dudewicz-van der Meulen uniformity test, and then uses a one-sample Wilcoxon signed-rank test to decide whether to shrink the upper bound, lower bound, or both. The experiments optimize 9 continuous hyperparameters of the commercial grasping software Kamido in PyBullet simulations and on a real Fanuc industrial arm.

Evaluation covers 7 simulated objects (A, C1, D, P1, hammer_j, m784, cokeSmallGrasp) and 1 real soft-object bin-picking setup (elbowed rubber tubes). Each optimization has a fixed budget of 30 trials (10 initial design + 20 infill EQI + 5 final evaluation). The authors compare runs without meta-learning against runs that reuse reduced bounds from a similar object.

## Key Contributions

- Meta-learning through reduced parameter bounds derived from the best iterations of similar past optimizations.
- Integration of Bayesian Optimization, PointNet-based 3D visual similarity, episodic/procedural/semantic memory, and parameters-bounds reduction into a single developmental robotics framework.
- Empirical validation on 7 simulated and 1 real industrial bin-picking object with a 30-iteration optimization budget.
- Demonstration of higher mean success (84.3% vs 78.9%) and improved worst-case performance (min 70.6% vs 28.3%) when meta-learning is used.

## Relevance to Humanoid Robotics

Although the experiments focus on a fixed-base industrial arm rather than a humanoid, the core methodology is directly transferable to humanoid manipulation. Humanoid robots deployed in diverse real-world settings must repeatedly tune grasping and motion parameters for new objects, environments, and tasks; reusing reduced parameter bounds from visually similar prior tasks can shorten tuning time and improve reliability. The long-term-memory perspective also aligns with lifelong developmental learning, a recurring requirement for general-purpose humanoid platforms that accumulate experience over time.

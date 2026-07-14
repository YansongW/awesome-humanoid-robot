---
$id: ent_paper_diffcotune_differentiable_co_t_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DiffCoTune: Differentiable Co-Tuning for Cross-domain Robot Control'
  zh: 'DiffCoTune: Differentiable Co-Tuning for Cross-domain Robot Control'
  ko: 'DiffCoTune: Differentiable Co-Tuning for Cross-domain Robot Control'
summary:
  en: 'DiffCoTune: Differentiable Co-Tuning for Cross-domain Robot Control is a 2025 work on sim-to-real for humanoid robots.'
  zh: 'DiffCoTune: Differentiable Co-Tuning for Cross-domain Robot Control is a 2025 work on sim-to-real for humanoid robots.'
  ko: 'DiffCoTune: Differentiable Co-Tuning for Cross-domain Robot Control is a 2025 work on sim-to-real for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- diffcotune
- humanoid
- sim_to_real
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.24068v1.
sources:
- id: src_001
  type: paper
  title: 'DiffCoTune: Differentiable Co-Tuning for Cross-domain Robot Control (arXiv)'
  url: https://arxiv.org/abs/2505.24068
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The deployment of robot controllers is hindered by modeling discrepancies due to necessary simplifications for computational tractability or inaccuracies in data-generating simulators. Such discrepancies typically require ad-hoc tuning to meet the desired performance, thereby ensuring successful transfer to a target domain. We propose a framework for automated, gradient-based tuning to enhance performance in the deployment domain by leveraging differentiable simulators. Our method collects rollouts in an iterative manner to co-tune the simulator and controller parameters, enabling systematic transfer within a few trials in the deployment domain. Specifically, we formulate multi-step objectives for tuning and employ alternating optimization to effectively adapt the controller to the deployment domain. The scalability of our framework is demonstrated by co-tuning model-based and learning-based controllers of arbitrary complexity for tasks ranging from low-dimensional cart-pole stabilization to high-dimensional quadruped and biped tracking, showing performance improvements across different deployment domains.

## 核心内容
The deployment of robot controllers is hindered by modeling discrepancies due to necessary simplifications for computational tractability or inaccuracies in data-generating simulators. Such discrepancies typically require ad-hoc tuning to meet the desired performance, thereby ensuring successful transfer to a target domain. We propose a framework for automated, gradient-based tuning to enhance performance in the deployment domain by leveraging differentiable simulators. Our method collects rollouts in an iterative manner to co-tune the simulator and controller parameters, enabling systematic transfer within a few trials in the deployment domain. Specifically, we formulate multi-step objectives for tuning and employ alternating optimization to effectively adapt the controller to the deployment domain. The scalability of our framework is demonstrated by co-tuning model-based and learning-based controllers of arbitrary complexity for tasks ranging from low-dimensional cart-pole stabilization to high-dimensional quadruped and biped tracking, showing performance improvements across different deployment domains.

## 参考
- http://arxiv.org/abs/2505.24068v1


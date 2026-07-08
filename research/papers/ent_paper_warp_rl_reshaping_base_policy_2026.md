---
$id: ent_paper_warp_rl_reshaping_base_policy_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Warp RL: Reshaping Base Policy Distributions for Dynamics Adaptation'
  zh: 'Warp RL: Reshaping Base Policy Distributions for Dynamics Adaptation'
  ko: ''
summary:
  en: "arXiv:2606.31043v1 Announce Type: cross \nAbstract: Residual reinforcement\
    \ learning adapts a pretrained robot policy by learning an additive correction\
    \ to its actions. While effective when adaptation amounts to shifting the base\
    \ policy's action distribution, additive corrections cannot change the distribution's\
    \ shape, scale, or state-dependent geometry -- limitations we formalize as wrong\
    \ variance, miscalibrated confidence, and non-uniform correction. We show that\
    \ these matter under dynamics shift: when the base distribution is geometrically\
    \ mismatched to the shifted system, residual correction can underperform even\
    \ the unadapted policy. We propose \\textbf{Warp RL}, a policy adaptation method\
    \ that replaces additive residuals with an invertible, state-conditioned transformation\
    \ of the base policy's action distribution. Instantiated with monotonic rational-quadratic\
    \ spline flows [arXiv:0706.1234v1], Warp RL preserves identity initialization,\
    \ strictly generalizes additive residual correction, and exposes a structured\
    \ adaptation space suitable for both policy-gradient and gradient-free optimization.\
    \ Across a variety of ManiSkill3 manipulation tasks with controlled dynamics shifts,\
    \ Warp RL matches residual correction when translation is sufficient and substantially\
    \ outperforms it when adaptation requires distributional reshaping. We further\
    \ demonstrate that warping can replace additive correction in an off-policy sim-to-real\
    \ pipeline, achieving comparable success rate with 30% faster task completion\
    \ on a real-robot peg-insertion task."
  zh: "arXiv:2606.31043v1 Announce Type: cross \nAbstract: Residual reinforcement\
    \ learning adapts a pretrained robot policy by learning an additive correction\
    \ to its actions. While effective when adaptation amounts to shifting the base\
    \ policy's action distribution, additive corrections cannot change the distribution's\
    \ shape, scale, or state-dependent geometry -- limitations we formalize as wrong\
    \ variance, miscalibrated confidence, and non-uniform correction. We show that\
    \ these matter under dynamics shift: when the base distribution is geometrically\
    \ mismatched to the shifted system, residual correction can underperform even\
    \ the unadapted policy. We propose \\textbf{Warp RL}, a policy adaptation method\
    \ that replaces additive residuals with an invertible, state-conditioned transformation\
    \ of the base policy's action distribution. Instantiated with monotonic rational-quadratic\
    \ spline flows [arXiv:0706.1234v1], Warp RL preserves identity initialization,\
    \ strictly generalizes additive residual correction, and exposes a structured\
    \ adaptation space suitable for both policy-gradient and gradient-free optimization.\
    \ Across a variety of ManiSkill3 manipulation tasks with controlled dynamics shifts,\
    \ Warp RL matches residual correction when translation is sufficient and substantially\
    \ outperforms it when adaptation requires distributional reshaping. We further\
    \ demonstrate that warping can replace additive correction in an off-policy sim-to-real\
    \ pipeline, achieving comparable success rate with 30% faster task completion\
    \ on a real-robot peg-insertion task."
  ko: ''
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
- warp_rl
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
  title: 'Warp RL: Reshaping Base Policy Distributions for Dynamics Adaptation'
  url: https://arxiv.org/abs/2606.31043
  date: '2026'
  accessed_at: '2026-07-01'
---

arXiv:2606.31043v1 Announce Type: cross 
Abstract: Residual reinforcement learning adapts a pretrained robot policy by learning an additive correction to its actions. While effective when adaptation amounts to shifting the base policy's action distribution, additive corrections cannot change the distribution's shape, scale, or state-dependent geometry -- limitations we formalize as wrong variance, miscalibrated confidence, and non-uniform correction. We show that these matter under dynamics shift: when the base distribution is geometrically mismatched to the shifted system, residual correction can underperform even the unadapted policy. We propose \textbf{Warp RL}, a policy adaptation method that replaces additive residuals with an invertible, state-conditioned transformation of the base policy's action distribution. Instantiated with monotonic rational-quadratic spline flows [arXiv:0706.1234v1], Warp RL preserves identity initialization, strictly generalizes additive residual correction, and exposes a structured adaptation space suitable for both policy-gradient and gradient-free optimization. Across a variety of ManiSkill3 manipulation tasks with controlled dynamics shifts, Warp RL matches residual correction when translation is sufficient and substantially outperforms it when adaptation requires distributional reshaping. We further demonstrate that warping can replace additive correction in an off-policy sim-to-real pipeline, achieving comparable success rate with 30% faster task completion on a real-robot peg-insertion task.

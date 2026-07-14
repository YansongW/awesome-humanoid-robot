---
$id: ent_paper_rapt_model_predictive_out_of_d_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RAPT: Model-Predictive Out-of-Distribution Detection and Failure Diagnosis for Sim-to-Real Humanoid Robots'
  zh: 'RAPT: Model-Predictive Out-of-Distribution Detection and Failure Diagnosis for Sim-to-Real Humanoid Robots'
  ko: 'RAPT: Model-Predictive Out-of-Distribution Detection and Failure Diagnosis for Sim-to-Real Humanoid Robots'
summary:
  en: 'RAPT: Model-Predictive Out-of-Distribution Detection and Failure Diagnosis for Sim-to-Real Humanoid Robots is a 2026
    work on sim-to-real for humanoid robots.'
  zh: 'RAPT: Model-Predictive Out-of-Distribution Detection and Failure Diagnosis for Sim-to-Real Humanoid Robots is a 2026
    work on sim-to-real for humanoid robots.'
  ko: 'RAPT: Model-Predictive Out-of-Distribution Detection and Failure Diagnosis for Sim-to-Real Humanoid Robots is a 2026
    work on sim-to-real for humanoid robots.'
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
- rapt
- sim_to_real
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.01515v1.
sources:
- id: src_001
  type: paper
  title: 'RAPT: Model-Predictive Out-of-Distribution Detection and Failure Diagnosis for Sim-to-Real Humanoid Robots (arXiv)'
  url: https://arxiv.org/abs/2602.01515
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Deploying learned control policies on humanoid robots is challenging: policies that appear robust in simulation can execute confidently in out-of-distribution (OOD) states after Sim-to-Real transfer, leading to silent failures that risk hardware damage. Although anomaly detection can mitigate these failures, prior methods are often incompatible with high-rate control, poorly calibrated at the extremely low false-positive rates required for practical deployment, or operate as black boxes that provide a binary stop signal without explaining why the robot drifted from nominal behavior. We present RAPT, a lightweight, self-supervised deployment-time monitor for 50Hz humanoid control. RAPT learns a probabilistic spatio-temporal manifold of nominal execution from simulation and evaluates execution-time predictive deviation as a calibrated, per-dimension signal. This yields (i) reliable online OOD detection under strict false-positive constraints and (ii) a continuous, interpretable measure of Sim-to-Real mismatch that can be tracked over time to quantify how far deployment has drifted from training. Beyond detection, we introduce an automated post-hoc root-cause analysis pipeline that combines gradient-based temporal saliency derived from RAPT's reconstruction objective with LLM-based reasoning conditioned on saliency and joint kinematics to produce semantic failure diagnoses in a zero-shot setting. We evaluate RAPT on a Unitree G1 humanoid across four complex tasks in simulation and on physical hardware. In large-scale simulation, RAPT improves True Positive Rate (TPR) by 37% over the strongest baseline at a fixed episode-level false positive rate of 0.5%. On real-world deployments, RAPT achieves a 12.5% TPR improvement and provides actionable interpretability, reaching 75% root-cause classification accuracy across 16 real-world failures using only proprioceptive data.

## 核心内容
Deploying learned control policies on humanoid robots is challenging: policies that appear robust in simulation can execute confidently in out-of-distribution (OOD) states after Sim-to-Real transfer, leading to silent failures that risk hardware damage. Although anomaly detection can mitigate these failures, prior methods are often incompatible with high-rate control, poorly calibrated at the extremely low false-positive rates required for practical deployment, or operate as black boxes that provide a binary stop signal without explaining why the robot drifted from nominal behavior. We present RAPT, a lightweight, self-supervised deployment-time monitor for 50Hz humanoid control. RAPT learns a probabilistic spatio-temporal manifold of nominal execution from simulation and evaluates execution-time predictive deviation as a calibrated, per-dimension signal. This yields (i) reliable online OOD detection under strict false-positive constraints and (ii) a continuous, interpretable measure of Sim-to-Real mismatch that can be tracked over time to quantify how far deployment has drifted from training. Beyond detection, we introduce an automated post-hoc root-cause analysis pipeline that combines gradient-based temporal saliency derived from RAPT's reconstruction objective with LLM-based reasoning conditioned on saliency and joint kinematics to produce semantic failure diagnoses in a zero-shot setting. We evaluate RAPT on a Unitree G1 humanoid across four complex tasks in simulation and on physical hardware. In large-scale simulation, RAPT improves True Positive Rate (TPR) by 37% over the strongest baseline at a fixed episode-level false positive rate of 0.5%. On real-world deployments, RAPT achieves a 12.5% TPR improvement and provides actionable interpretability, reaching 75% root-cause classification accuracy across 16 real-world failures using only proprioceptive data.

## 参考
- http://arxiv.org/abs/2602.01515v1


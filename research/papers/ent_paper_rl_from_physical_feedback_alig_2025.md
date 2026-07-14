---
$id: ent_paper_rl_from_physical_feedback_alig_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RL from Physical Feedback: Aligning Large Motion Models with Humanoid Control'
  zh: 'RL from Physical Feedback: Aligning Large Motion Models with Humanoid Control'
  ko: 'RL from Physical Feedback: Aligning Large Motion Models with Humanoid Control'
summary:
  en: 'RL from Physical Feedback: Aligning Large Motion Models with Humanoid Control is a 2025 work on physics-based character
    animation for humanoid robots.'
  zh: 'RL from Physical Feedback: Aligning Large Motion Models with Humanoid Control is a 2025 work on physics-based character
    animation for humanoid robots.'
  ko: 'RL from Physical Feedback: Aligning Large Motion Models with Humanoid Control is a 2025 work on physics-based character
    animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- physics_based
- rl_from_physical_feedback
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.12769v1.
sources:
- id: src_001
  type: paper
  title: 'RL from Physical Feedback: Aligning Large Motion Models with Humanoid Control (arXiv)'
  url: https://arxiv.org/abs/2506.12769
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
This paper focuses on a critical challenge in robotics: translating text-driven human motions into executable actions for humanoid robots, enabling efficient and cost-effective learning of new behaviors. While existing text-to-motion generation methods achieve semantic alignment between language and motion, they often produce kinematically or physically infeasible motions unsuitable for real-world deployment. To bridge this sim-to-real gap, we propose Reinforcement Learning from Physical Feedback (RLPF), a novel framework that integrates physics-aware motion evaluation with text-conditioned motion generation. RLPF employs a motion tracking policy to assess feasibility in a physics simulator, generating rewards for fine-tuning the motion generator. Furthermore, RLPF introduces an alignment verification module to preserve semantic fidelity to text instructions. This joint optimization ensures both physical plausibility and instruction alignment. Extensive experiments show that RLPF greatly outperforms baseline methods in generating physically feasible motions while maintaining semantic correspondence with text instruction, enabling successful deployment on real humanoid robots.

## 核心内容
This paper focuses on a critical challenge in robotics: translating text-driven human motions into executable actions for humanoid robots, enabling efficient and cost-effective learning of new behaviors. While existing text-to-motion generation methods achieve semantic alignment between language and motion, they often produce kinematically or physically infeasible motions unsuitable for real-world deployment. To bridge this sim-to-real gap, we propose Reinforcement Learning from Physical Feedback (RLPF), a novel framework that integrates physics-aware motion evaluation with text-conditioned motion generation. RLPF employs a motion tracking policy to assess feasibility in a physics simulator, generating rewards for fine-tuning the motion generator. Furthermore, RLPF introduces an alignment verification module to preserve semantic fidelity to text instructions. This joint optimization ensures both physical plausibility and instruction alignment. Extensive experiments show that RLPF greatly outperforms baseline methods in generating physically feasible motions while maintaining semantic correspondence with text instruction, enabling successful deployment on real humanoid robots.

## 参考
- http://arxiv.org/abs/2506.12769v1


---
$id: ent_paper_z_1_efficient_reinforcement_le_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Z-1: Efficient Reinforcement Learning for Vision-Language-Action Models'
  zh: 'Z-1: Efficient Reinforcement Learning for Vision-Language-Action Models'
  ko: ''
summary:
  en: "arXiv:2606.31846v1 Announce Type: new \nAbstract: Vision-Language-Action (VLA)\
    \ models offer a promising framework for robotic manipulation by connecting language\
    \ instructions, visual observations, and continuous control. However, most existing\
    \ policies remain limited by behavior cloning or supervised fine-tuning (SFT)\
    \ from fixed demonstrations, which provides limited opportunity to improve from\
    \ the policy's own failures. In this paper, we present Z-1, a reinforcement learning\
    \ (RL) post-training framework for flow-based VLA models. Built on top of $\\\
    pi_{0.5}$, Z-1 uses only publicly released RoboCasa demonstrations for SFT and\
    \ then applies a task-wise Group Relative Policy Optimization (GRPO) strategy\
    \ across $24$ standard RoboCasa tasks. To improve the efficiency and stability\
    \ of online optimization, Z-1 combines shared-prefix rollout construction, tree-structured\
    \ trajectory branching, completion-aware reward calibration, and selective joint\
    \ training of VLM and Action Expert. Across all $24$ RoboCasa tasks, Z-1 achieves\
    \ an average success rate of $80.6\\%$, improving over its SFT initialization\
    \ by $13.2\\%$ points and outperforms the published sota models. These results\
    \ show that systematic GRPO post-training can substantially improve flow-based\
    \ VLA policies without additional private demonstrations."
  zh: "arXiv:2606.31846v1 Announce Type: new \nAbstract: Vision-Language-Action (VLA)\
    \ models offer a promising framework for robotic manipulation by connecting language\
    \ instructions, visual observations, and continuous control. However, most existing\
    \ policies remain limited by behavior cloning or supervised fine-tuning (SFT)\
    \ from fixed demonstrations, which provides limited opportunity to improve from\
    \ the policy's own failures. In this paper, we present Z-1, a reinforcement learning\
    \ (RL) post-training framework for flow-based VLA models. Built on top of $\\\
    pi_{0.5}$, Z-1 uses only publicly released RoboCasa demonstrations for SFT and\
    \ then applies a task-wise Group Relative Policy Optimization (GRPO) strategy\
    \ across $24$ standard RoboCasa tasks. To improve the efficiency and stability\
    \ of online optimization, Z-1 combines shared-prefix rollout construction, tree-structured\
    \ trajectory branching, completion-aware reward calibration, and selective joint\
    \ training of VLM and Action Expert. Across all $24$ RoboCasa tasks, Z-1 achieves\
    \ an average success rate of $80.6\\%$, improving over its SFT initialization\
    \ by $13.2\\%$ points and outperforms the published sota models. These results\
    \ show that systematic GRPO post-training can substantially improve flow-based\
    \ VLA policies without additional private demonstrations."
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
- z_1
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
  title: 'Z-1: Efficient Reinforcement Learning for Vision-Language-Action Models'
  url: https://arxiv.org/abs/2606.31846
  date: '2026'
  accessed_at: '2026-07-01'
---

arXiv:2606.31846v1 Announce Type: new 
Abstract: Vision-Language-Action (VLA) models offer a promising framework for robotic manipulation by connecting language instructions, visual observations, and continuous control. However, most existing policies remain limited by behavior cloning or supervised fine-tuning (SFT) from fixed demonstrations, which provides limited opportunity to improve from the policy's own failures. In this paper, we present Z-1, a reinforcement learning (RL) post-training framework for flow-based VLA models. Built on top of $\pi_{0.5}$, Z-1 uses only publicly released RoboCasa demonstrations for SFT and then applies a task-wise Group Relative Policy Optimization (GRPO) strategy across $24$ standard RoboCasa tasks. To improve the efficiency and stability of online optimization, Z-1 combines shared-prefix rollout construction, tree-structured trajectory branching, completion-aware reward calibration, and selective joint training of VLM and Action Expert. Across all $24$ RoboCasa tasks, Z-1 achieves an average success rate of $80.6\%$, improving over its SFT initialization by $13.2\%$ points and outperforms the published sota models. These results show that systematic GRPO post-training can substantially improve flow-based VLA policies without additional private demonstrations.

---
$id: ent_paper_mind_v_hierarchical_world_mode_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MIND-V: Hierarchical World Model for Long-Horizon Robotic Manipulation with RL-based Physical Alignment'
  zh: 'MIND-V: Hierarchical World Model for Long-Horizon Robotic Manipulation with RL-based Physical Alignment'
  ko: 'MIND-V: Hierarchical World Model for Long-Horizon Robotic Manipulation with RL-based Physical Alignment'
summary:
  en: "arXiv:2512.06628v4 Announce Type: replace \nAbstract: Scalable embodied intelligence is constrained by the scarcity\
    \ of diverse, long-horizon robotic manipulation data. Existing video world models in this domain are limited to synthesizing\
    \ short clips of simple actions and often rely on manually defined trajectories. To this end, we introduce MIND-V, a cognitive\
    \ hierarchical world model designed to synthesize physically plausible and logically coherent videos of long-horizon robotic\
    \ manipulation. Inspired by cognitive science, MIND-V bridges high-level reasoning with pixel-level synthesis through\
    \ three core components: a Semantic Reasoning Hub (SRH) that leverages a pre-trained vision-language model for task planning;\
    \ a Behavioral Semantic Bridge (BSB) that translates abstract instructions into domain-invariant representations; and\
    \ a Motor Video Generator (MVG) for conditional video rendering. MIND-V employs Staged Visual Future Rollouts, a test-time\
    \ optimization strategy to enhance long-horizon robustness. To enforce adherence to physical laws, we introduce a GRPO\
    \ reinforcement learning post-training phase guided by a novel Physical Foresight Coherence (PFC) reward. PFC leverages\
    \ the V-JEPA2 world model as a physics referee to penalize implausible dynamics in the latent feature space. Experiments\
    \ confirm MIND-V's SOTA performance in long-horizon simulation and its significant value for policy learning, introducing\
    \ a scalable and fully autonomous framework for embodied data synthesis."
  zh: "arXiv:2512.06628v4 Announce Type: replace \nAbstract: Scalable embodied intelligence is constrained by the scarcity\
    \ of diverse, long-horizon robotic manipulation data. Existing video world models in this domain are limited to synthesizing\
    \ short clips of simple actions and often rely on manually defined trajectories. To this end, we introduce MIND-V, a cognitive\
    \ hierarchical world model designed to synthesize physically plausible and logically coherent videos of long-horizon robotic\
    \ manipulation. Inspired by cognitive science, MIND-V bridges high-level reasoning with pixel-level synthesis through\
    \ three core components: a Semantic Reasoning Hub (SRH) that leverages a pre-trained vision-language model for task planning;\
    \ a Behavioral Semantic Bridge (BSB) that translates abstract instructions into domain-invariant representations; and\
    \ a Motor Video Generator (MVG) for conditional video rendering. MIND-V employs Staged Visual Future Rollouts, a test-time\
    \ optimization strategy to enhance long-horizon robustness. To enforce adherence to physical laws, we introduce a GRPO\
    \ reinforcement learning post-training phase guided by a novel Physical Foresight Coherence (PFC) reward. PFC leverages\
    \ the V-JEPA2 world model as a physics referee to penalize implausible dynamics in the latent feature space. Experiments\
    \ confirm MIND-V's SOTA performance in long-horizon simulation and its significant value for policy learning, introducing\
    \ a scalable and fully autonomous framework for embodied data synthesis."
  ko: "arXiv:2512.06628v4 Announce Type: replace \nAbstract: Scalable embodied intelligence is constrained by the scarcity\
    \ of diverse, long-horizon robotic manipulation data. Existing video world models in this domain are limited to synthesizing\
    \ short clips of simple actions and often rely on manually defined trajectories. To this end, we introduce MIND-V, a cognitive\
    \ hierarchical world model designed to synthesize physically plausible and logically coherent videos of long-horizon robotic\
    \ manipulation. Inspired by cognitive science, MIND-V bridges high-level reasoning with pixel-level synthesis through\
    \ three core components: a Semantic Reasoning Hub (SRH) that leverages a pre-trained vision-language model for task planning;\
    \ a Behavioral Semantic Bridge (BSB) that translates abstract instructions into domain-invariant representations; and\
    \ a Motor Video Generator (MVG) for conditional video rendering. MIND-V employs Staged Visual Future Rollouts, a test-time\
    \ optimization strategy to enhance long-horizon robustness. To enforce adherence to physical laws, we introduce a GRPO\
    \ reinforcement learning post-training phase guided by a novel Physical Foresight Coherence (PFC) reward. PFC leverages\
    \ the V-JEPA2 world model as a physics referee to penalize implausible dynamics in the latent feature space. Experiments\
    \ confirm MIND-V's SOTA performance in long-horizon simulation and its significant value for policy learning, introducing\
    \ a scalable and fully autonomous framework for embodied data synthesis."
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
- mind_v
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.06628v4.
sources:
- id: src_001
  type: paper
  title: 'MIND-V: Hierarchical World Model for Long-Horizon Robotic Manipulation with RL-based Physical Alignment (arXiv)'
  url: https://arxiv.org/abs/2512.06628
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Scalable embodied intelligence is constrained by the scarcity of diverse, long-horizon robotic manipulation data. Existing video world models in this domain are limited to synthesizing short clips of simple actions and often rely on manually defined trajectories. To this end, we introduce MIND-V, a cognitive hierarchical world model designed to synthesize physically plausible and logically coherent videos of long-horizon robotic manipulation. Inspired by cognitive science, MIND-V bridges high-level reasoning with pixel-level synthesis through three core components: a Semantic Reasoning Hub (SRH) that leverages a pre-trained vision-language model for task planning; a Behavioral Semantic Bridge (BSB) that translates abstract instructions into domain-invariant representations; and a Motor Video Generator (MVG) for conditional video rendering. MIND-V employs Staged Visual Future Rollouts, a test-time optimization strategy to enhance long-horizon robustness. To enforce adherence to physical laws, we introduce a GRPO reinforcement learning post-training phase guided by a novel Physical Foresight Coherence (PFC) reward. PFC leverages the V-JEPA2 world model as a physics referee to penalize implausible dynamics in the latent feature space. Experiments confirm MIND-V's SOTA performance in long-horizon simulation and its significant value for policy learning, introducing a scalable and fully autonomous framework for embodied data synthesis.

## 核心内容
Scalable embodied intelligence is constrained by the scarcity of diverse, long-horizon robotic manipulation data. Existing video world models in this domain are limited to synthesizing short clips of simple actions and often rely on manually defined trajectories. To this end, we introduce MIND-V, a cognitive hierarchical world model designed to synthesize physically plausible and logically coherent videos of long-horizon robotic manipulation. Inspired by cognitive science, MIND-V bridges high-level reasoning with pixel-level synthesis through three core components: a Semantic Reasoning Hub (SRH) that leverages a pre-trained vision-language model for task planning; a Behavioral Semantic Bridge (BSB) that translates abstract instructions into domain-invariant representations; and a Motor Video Generator (MVG) for conditional video rendering. MIND-V employs Staged Visual Future Rollouts, a test-time optimization strategy to enhance long-horizon robustness. To enforce adherence to physical laws, we introduce a GRPO reinforcement learning post-training phase guided by a novel Physical Foresight Coherence (PFC) reward. PFC leverages the V-JEPA2 world model as a physics referee to penalize implausible dynamics in the latent feature space. Experiments confirm MIND-V's SOTA performance in long-horizon simulation and its significant value for policy learning, introducing a scalable and fully autonomous framework for embodied data synthesis.

## 参考
- http://arxiv.org/abs/2512.06628v4


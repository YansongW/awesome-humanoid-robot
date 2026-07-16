---
$id: ent_paper_do_vision_language_action_mode_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Do Vision-Language-Action Models Mean What They Say? On the Role of Faithfulness in Embodied Reasoning
  zh: Do Vision-Language-Action Models Mean What They Say? On the Role of Faithfulness in Embodied Reasoning
  ko: Do Vision-Language-Action Models Mean What They Say? On the Role of Faithfulness in Embodied Reasoning
summary:
  en: 'arXiv:2607.04681v1 Announce Type: new Abstract: Embodied Chain-of-Thought has emerged as a promising mechanism to enhance
    robot decision-making and interpretability in black-box Vision-Language Action (VLA) models. However, whether this verbalized
    Chain-of-Thought truthfully reflects the policy''s underlying decision process remains poorly understood. We distinguish
    between functional reasoning, in which reasoning improves task performance, and faithful reasoning, in which reasoning
    truly reflects the policy''s internal decision process. We argue that SoTA alignment strategies offer a necessary but
    insufficient notion of faithfulness, admitting reasoning whose intermediate steps can mask the causal links in action
    prediction through confounding factors (e.g., reasoning that is ungrounded in the environment and internally disconnected
    or inconsistent), restricting policy generalization. We study this gap through a human evaluation of a SoTA reasoning
    model for autonomous driving, revealing an inconsistent coupling between reasoning quality and downstream trajectory improvement.
    We then operationalize a behavioral surrogate for embodied faithfulness through a learned critic, Pinocchio, scoring observation
    grounding and stepwise coherence, and use this critic as a dense reward signal in post-training an embodied policy with
    reinforcement learning. Across withheld driving benchmarks, our post-trained planner improves faithfulness by 4% and 18%
    over SoTA alignment and trajectory error post-training baselines, respectively, while maintaining competitive downstream
    task performance. Finally, on a synthetic out-of-distribution test set, post-training for faithfulness improves policy
    responsiveness to rare counterfactual scenarios by 1.6x that of a SoTA policy, suggesting that faithful reasoning traces
    contribute to more robust, generalizable, and interpretable embodied intelligence. Project page: https://mjf-su.github.io/pinocchio/'
  zh: 'arXiv:2607.04681v1 Announce Type: new Abstract: Embodied Chain-of-Thought has emerged as a promising mechanism to enhance
    robot decision-making and interpretability in black-box Vision-Language Action (VLA) models. However, whether this verbalized
    Chain-of-Thought truthfully reflects the policy''s underlying decision process remains poorly understood. We distinguish
    between functional reasoning, in which reasoning improves task performance, and faithful reasoning, in which reasoning
    truly reflects the policy''s internal decision process. We argue that SoTA alignment strategies offer a necessary but
    insufficient notion of faithfulness, admitting reasoning whose intermediate steps can mask the causal links in action
    prediction through confounding factors (e.g., reasoning that is ungrounded in the environment and internally disconnected
    or inconsistent), restricting policy generalization. We study this gap through a human evaluation of a SoTA reasoning
    model for autonomous driving, revealing an inconsistent coupling between reasoning quality and downstream trajectory improvement.
    We then operationalize a behavioral surrogate for embodied faithfulness through a learned critic, Pinocchio, scoring observation
    grounding and stepwise coherence, and use this critic as a dense reward signal in post-training an embodied policy with
    reinforcement learning. Across withheld driving benchmarks, our post-trained planner improves faithfulness by 4% and 18%
    over SoTA alignment and trajectory error post-training baselines, respectively, while maintaining competitive downstream
    task performance. Finally, on a synthetic out-of-distribution test set, post-training for faithfulness improves policy
    responsiveness to rare counterfactual scenarios by 1.6x that of a SoTA policy, suggesting that faithful reasoning traces
    contribute to more robust, generalizable, and interpretable embodied intelligence. Project page: https://mjf-su.github.io/pinocchio/'
  ko: 'arXiv:2607.04681v1 Announce Type: new Abstract: Embodied Chain-of-Thought has emerged as a promising mechanism to enhance
    robot decision-making and interpretability in black-box Vision-Language Action (VLA) models. However, whether this verbalized
    Chain-of-Thought truthfully reflects the policy''s underlying decision process remains poorly understood. We distinguish
    between functional reasoning, in which reasoning improves task performance, and faithful reasoning, in which reasoning
    truly reflects the policy''s internal decision process. We argue that SoTA alignment strategies offer a necessary but
    insufficient notion of faithfulness, admitting reasoning whose intermediate steps can mask the causal links in action
    prediction through confounding factors (e.g., reasoning that is ungrounded in the environment and internally disconnected
    or inconsistent), restricting policy generalization. We study this gap through a human evaluation of a SoTA reasoning
    model for autonomous driving, revealing an inconsistent coupling between reasoning quality and downstream trajectory improvement.
    We then operationalize a behavioral surrogate for embodied faithfulness through a learned critic, Pinocchio, scoring observation
    grounding and stepwise coherence, and use this critic as a dense reward signal in post-training an embodied policy with
    reinforcement learning. Across withheld driving benchmarks, our post-trained planner improves faithfulness by 4% and 18%
    over SoTA alignment and trajectory error post-training baselines, respectively, while maintaining competitive downstream
    task performance. Finally, on a synthetic out-of-distribution test set, post-training for faithfulness improves policy
    responsiveness to rare counterfactual scenarios by 1.6x that of a SoTA policy, suggesting that faithful reasoning traces
    contribute to more robust, generalizable, and interpretable embodied intelligence. Project page: https://mjf-su.github.io/pinocchio/'
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
- do_vision_language_action_mode
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04681v1.
sources:
- id: src_001
  type: paper
  title: Do Vision-Language-Action Models Mean What They Say? On the Role of Faithfulness in Embodied Reasoning (arXiv)
  url: https://arxiv.org/abs/2607.04681
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Embodied Chain-of-Thought has emerged as a promising mechanism to enhance robot decision-making and interpretability in black-box Vision-Language Action (VLA) models. However, whether this verbalized Chain-of-Thought truthfully reflects the policy's underlying decision process remains poorly understood. We distinguish between functional reasoning, in which reasoning improves task performance, and faithful reasoning, in which reasoning truly reflects the policy's internal decision process. We argue that SoTA alignment strategies offer a necessary but insufficient notion of faithfulness, admitting reasoning whose intermediate steps can mask the causal links in action prediction through confounding factors (e.g., reasoning that is ungrounded in the environment and internally disconnected or inconsistent), restricting policy generalization. We study this gap through a human evaluation of a SoTA reasoning model for autonomous driving, revealing an inconsistent coupling between reasoning quality and downstream trajectory improvement. We then operationalize a behavioral surrogate for embodied faithfulness through a learned critic, Pinocchio, scoring observation grounding and stepwise coherence, and use this critic as a dense reward signal in post-training an embodied policy with reinforcement learning. Across withheld driving benchmarks, our post-trained planner improves faithfulness by 4% and 18% over SoTA alignment and trajectory error post-training baselines, respectively, while maintaining competitive downstream task performance. Finally, on a synthetic out-of-distribution test set, post-training for faithfulness improves policy responsiveness to rare counterfactual scenarios by 1.6x that of a SoTA policy, suggesting that faithful reasoning traces contribute to more robust, generalizable, and interpretable embodied intelligence. Project page: https://mjf-su.github.io/pinocchio/

## 核心内容
Embodied Chain-of-Thought has emerged as a promising mechanism to enhance robot decision-making and interpretability in black-box Vision-Language Action (VLA) models. However, whether this verbalized Chain-of-Thought truthfully reflects the policy's underlying decision process remains poorly understood. We distinguish between functional reasoning, in which reasoning improves task performance, and faithful reasoning, in which reasoning truly reflects the policy's internal decision process. We argue that SoTA alignment strategies offer a necessary but insufficient notion of faithfulness, admitting reasoning whose intermediate steps can mask the causal links in action prediction through confounding factors (e.g., reasoning that is ungrounded in the environment and internally disconnected or inconsistent), restricting policy generalization. We study this gap through a human evaluation of a SoTA reasoning model for autonomous driving, revealing an inconsistent coupling between reasoning quality and downstream trajectory improvement. We then operationalize a behavioral surrogate for embodied faithfulness through a learned critic, Pinocchio, scoring observation grounding and stepwise coherence, and use this critic as a dense reward signal in post-training an embodied policy with reinforcement learning. Across withheld driving benchmarks, our post-trained planner improves faithfulness by 4% and 18% over SoTA alignment and trajectory error post-training baselines, respectively, while maintaining competitive downstream task performance. Finally, on a synthetic out-of-distribution test set, post-training for faithfulness improves policy responsiveness to rare counterfactual scenarios by 1.6x that of a SoTA policy, suggesting that faithful reasoning traces contribute to more robust, generalizable, and interpretable embodied intelligence. Project page: https://mjf-su.github.io/pinocchio/

## 参考
- http://arxiv.org/abs/2607.04681v1


---
$id: ent_paper_dreamsteer_latent_world_models_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DREAMSTEER: Latent World Models Can Steer VLA Policies During Deployment Without Any Finetuning'
  zh: 'DREAMSTEER: Latent World Models Can Steer VLA Policies During Deployment Without Any Finetuning'
  ko: 'DREAMSTEER: Latent World Models Can Steer VLA Policies During Deployment Without Any Finetuning'
summary:
  en: "arXiv:2607.02865v1 Announce Type: new \nAbstract: Pretrained vision-language-action (VLA) policies show promising zero-shot\
    \ generalization, but often fail under deployment-time distribution shift, leading to decreased robustness and inconsistent\
    \ instruction following. While prior work commonly tackles this by finetuning on in-distribution data, it assumes demonstrations\
    \ collected on tasks in the target environment. In this work, we propose DREAMSTEER, a deployment-time steering framework\
    \ for pretrained VLAs without any finetuning or parameter modifications. The key insight in DREAMSTEER is to leverage\
    \ a latent world model and a value model to steer pretrained VLA policies. During deployment, DREAMSTEER samples candidate\
    \ action chunks from a VLA policy and predefined motion primitives, imagines their outcomes using an action-conditioned\
    \ latent world model, and ranks the imagined trajectories with a language-conditioned value model. Across four real-world\
    \ manipulation benchmarks with unseen objects, DREAMSTEER improves task success rate from 23.75% to 66.25% and instruction-following\
    \ accuracy from 38.75% to 56.25% over the base VLA policy."
  zh: "arXiv:2607.02865v1 Announce Type: new \nAbstract: Pretrained vision-language-action (VLA) policies show promising zero-shot\
    \ generalization, but often fail under deployment-time distribution shift, leading to decreased robustness and inconsistent\
    \ instruction following. While prior work commonly tackles this by finetuning on in-distribution data, it assumes demonstrations\
    \ collected on tasks in the target environment. In this work, we propose DREAMSTEER, a deployment-time steering framework\
    \ for pretrained VLAs without any finetuning or parameter modifications. The key insight in DREAMSTEER is to leverage\
    \ a latent world model and a value model to steer pretrained VLA policies. During deployment, DREAMSTEER samples candidate\
    \ action chunks from a VLA policy and predefined motion primitives, imagines their outcomes using an action-conditioned\
    \ latent world model, and ranks the imagined trajectories with a language-conditioned value model. Across four real-world\
    \ manipulation benchmarks with unseen objects, DREAMSTEER improves task success rate from 23.75% to 66.25% and instruction-following\
    \ accuracy from 38.75% to 56.25% over the base VLA policy."
  ko: "arXiv:2607.02865v1 Announce Type: new \nAbstract: Pretrained vision-language-action (VLA) policies show promising zero-shot\
    \ generalization, but often fail under deployment-time distribution shift, leading to decreased robustness and inconsistent\
    \ instruction following. While prior work commonly tackles this by finetuning on in-distribution data, it assumes demonstrations\
    \ collected on tasks in the target environment. In this work, we propose DREAMSTEER, a deployment-time steering framework\
    \ for pretrained VLAs without any finetuning or parameter modifications. The key insight in DREAMSTEER is to leverage\
    \ a latent world model and a value model to steer pretrained VLA policies. During deployment, DREAMSTEER samples candidate\
    \ action chunks from a VLA policy and predefined motion primitives, imagines their outcomes using an action-conditioned\
    \ latent world model, and ranks the imagined trajectories with a language-conditioned value model. Across four real-world\
    \ manipulation benchmarks with unseen objects, DREAMSTEER improves task success rate from 23.75% to 66.25% and instruction-following\
    \ accuracy from 38.75% to 56.25% over the base VLA policy."
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
- dreamsteer
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02865v1.
sources:
- id: src_001
  type: paper
  title: 'DREAMSTEER: Latent World Models Can Steer VLA Policies During Deployment Without Any Finetuning (arXiv)'
  url: https://arxiv.org/abs/2607.02865
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Pretrained vision-language-action (VLA) policies show promising zero-shot generalization, but often fail under deployment-time distribution shift, leading to decreased robustness and inconsistent instruction following. While prior work commonly tackles this by finetuning on in-distribution data, it assumes demonstrations collected on tasks in the target environment. In this work, we propose DREAMSTEER, a deployment-time steering framework for pretrained VLAs without any finetuning or parameter modifications. The key insight in DREAMSTEER is to leverage a latent world model and a value model to steer pretrained VLA policies. During deployment, DREAMSTEER samples candidate action chunks from a VLA policy and predefined motion primitives, imagines their outcomes using an action-conditioned latent world model, and ranks the imagined trajectories with a language-conditioned value model. Across four real-world manipulation benchmarks with unseen objects, DREAMSTEER improves task success rate from 23.75% to 66.25% and instruction-following accuracy from 38.75% to 56.25% over the base VLA policy.

## 核心内容
Pretrained vision-language-action (VLA) policies show promising zero-shot generalization, but often fail under deployment-time distribution shift, leading to decreased robustness and inconsistent instruction following. While prior work commonly tackles this by finetuning on in-distribution data, it assumes demonstrations collected on tasks in the target environment. In this work, we propose DREAMSTEER, a deployment-time steering framework for pretrained VLAs without any finetuning or parameter modifications. The key insight in DREAMSTEER is to leverage a latent world model and a value model to steer pretrained VLA policies. During deployment, DREAMSTEER samples candidate action chunks from a VLA policy and predefined motion primitives, imagines their outcomes using an action-conditioned latent world model, and ranks the imagined trajectories with a language-conditioned value model. Across four real-world manipulation benchmarks with unseen objects, DREAMSTEER improves task success rate from 23.75% to 66.25% and instruction-following accuracy from 38.75% to 56.25% over the base VLA policy.

## 参考
- http://arxiv.org/abs/2607.02865v1


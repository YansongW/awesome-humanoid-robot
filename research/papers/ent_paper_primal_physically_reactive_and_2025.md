---
$id: ent_paper_primal_physically_reactive_and_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: PRIMAL Physically Reactive and Interactive Motor Model for Avatar Learning
  zh: PRIMAL Physically Reactive and Interactive Motor Model for Avatar Learning
  ko: PRIMAL Physically Reactive and Interactive Motor Model for Avatar Learning
summary:
  en: PRIMAL Physically Reactive and Interactive Motor Model for Avatar Learning is a 2025 work on human motion analysis and
    synthesis for humanoid robots.
  zh: PRIMAL Physically Reactive and Interactive Motor Model for Avatar Learning is a 2025 work on human motion analysis and
    synthesis for humanoid robots.
  ko: PRIMAL Physically Reactive and Interactive Motor Model for Avatar Learning is a 2025 work on human motion analysis and
    synthesis for humanoid robots.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- motion_analysis
- motion_synthesis
- primal_physically_reactive_and
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.17544v2.
sources:
- id: src_001
  type: paper
  title: PRIMAL Physically Reactive and Interactive Motor Model for Avatar Learning (arXiv)
  url: https://arxiv.org/abs/2503.17544
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We formulate the motor system of an interactive avatar as a generative motion model that can drive the body to move through 3D space in a perpetual, realistic, controllable, and responsive manner. Although human motion generation has been extensively studied, many existing methods lack the responsiveness and realism of real human movements. Inspired by recent advances in foundation models, we propose PRIMAL, which is learned with a two-stage paradigm. In the pretraining stage, the model learns body movements from a large number of sub-second motion segments, providing a generative foundation from which more complex motions are built. This training is fully unsupervised without annotations. Given a single-frame initial state during inference, the pretrained model not only generates unbounded, realistic, and controllable motion, but also enables the avatar to be responsive to induced impulses in real time. In the adaptation phase, we employ a novel ControlNet-like adaptor to fine-tune the base model efficiently, adapting it to new tasks such as few-shot personalized action generation and spatial target reaching. Evaluations show that our proposed method outperforms state-of-the-art baselines. We leverage the model to create a real-time character animation system in Unreal Engine that feels highly responsive and natural. Code, models, and more results are available at: https://yz-cnsdqz.github.io/eigenmotion/PRIMAL

## 核心内容
We formulate the motor system of an interactive avatar as a generative motion model that can drive the body to move through 3D space in a perpetual, realistic, controllable, and responsive manner. Although human motion generation has been extensively studied, many existing methods lack the responsiveness and realism of real human movements. Inspired by recent advances in foundation models, we propose PRIMAL, which is learned with a two-stage paradigm. In the pretraining stage, the model learns body movements from a large number of sub-second motion segments, providing a generative foundation from which more complex motions are built. This training is fully unsupervised without annotations. Given a single-frame initial state during inference, the pretrained model not only generates unbounded, realistic, and controllable motion, but also enables the avatar to be responsive to induced impulses in real time. In the adaptation phase, we employ a novel ControlNet-like adaptor to fine-tune the base model efficiently, adapting it to new tasks such as few-shot personalized action generation and spatial target reaching. Evaluations show that our proposed method outperforms state-of-the-art baselines. We leverage the model to create a real-time character animation system in Unreal Engine that feels highly responsive and natural. Code, models, and more results are available at: https://yz-cnsdqz.github.io/eigenmotion/PRIMAL

## 参考
- http://arxiv.org/abs/2503.17544v2


---
$id: ent_paper_reuss_multimodal_diffusion_transform_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Multimodal Diffusion Transformer: Learning Versatile Behavior from Multimodal Goals'
  zh: MDT
  ko: 'Multimodal Diffusion Transformer: Learning Versatile Behavior from Multimodal Goals'
summary:
  en: 'Multimodal Diffusion Transformer: Learning Versatile Behavior from Multimodal Goals (MDT), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Karlsruhe Institute of Technology, and published at Robotics - Science and
    Systems 2024.'
  zh: 'Multimodal Diffusion Transformer: Learning Versatile Behavior from Multimodal Goals (MDT), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Karlsruhe Institute of Technology, and published at Robotics - Science and
    Systems 2024.'
  ko: 'Multimodal Diffusion Transformer: Learning Versatile Behavior from Multimodal Goals (MDT), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Karlsruhe Institute of Technology, and published at Robotics - Science and
    Systems 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- mdt
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2407.05996v1.
sources:
- id: src_001
  type: website
  title: MDT source
  url: https://doi.org/10.15607/RSS.2024.XX.121
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
This work introduces the Multimodal Diffusion Transformer (MDT), a novel diffusion policy framework, that excels at learning versatile behavior from multimodal goal specifications with few language annotations. MDT leverages a diffusion-based multimodal transformer backbone and two self-supervised auxiliary objectives to master long-horizon manipulation tasks based on multimodal goals. The vast majority of imitation learning methods only learn from individual goal modalities, e.g. either language or goal images. However, existing large-scale imitation learning datasets are only partially labeled with language annotations, which prohibits current methods from learning language conditioned behavior from these datasets. MDT addresses this challenge by introducing a latent goal-conditioned state representation that is simultaneously trained on multimodal goal instructions. This state representation aligns image and language based goal embeddings and encodes sufficient information to predict future states. The representation is trained via two self-supervised auxiliary objectives, enhancing the performance of the presented transformer backbone. MDT shows exceptional performance on 164 tasks provided by the challenging CALVIN and LIBERO benchmarks, including a LIBERO version that contains less than $2\%$ language annotations. Furthermore, MDT establishes a new record on the CALVIN manipulation challenge, demonstrating an absolute performance improvement of $15\%$ over prior state-of-the-art methods that require large-scale pretraining and contain $10\times$ more learnable parameters. MDT shows its ability to solve long-horizon manipulation from sparsely annotated data in both simulated and real-world environments. Demonstrations and Code are available at https://intuitive-robots.github.io/mdt_policy/.

## 核心内容
This work introduces the Multimodal Diffusion Transformer (MDT), a novel diffusion policy framework, that excels at learning versatile behavior from multimodal goal specifications with few language annotations. MDT leverages a diffusion-based multimodal transformer backbone and two self-supervised auxiliary objectives to master long-horizon manipulation tasks based on multimodal goals. The vast majority of imitation learning methods only learn from individual goal modalities, e.g. either language or goal images. However, existing large-scale imitation learning datasets are only partially labeled with language annotations, which prohibits current methods from learning language conditioned behavior from these datasets. MDT addresses this challenge by introducing a latent goal-conditioned state representation that is simultaneously trained on multimodal goal instructions. This state representation aligns image and language based goal embeddings and encodes sufficient information to predict future states. The representation is trained via two self-supervised auxiliary objectives, enhancing the performance of the presented transformer backbone. MDT shows exceptional performance on 164 tasks provided by the challenging CALVIN and LIBERO benchmarks, including a LIBERO version that contains less than $2\%$ language annotations. Furthermore, MDT establishes a new record on the CALVIN manipulation challenge, demonstrating an absolute performance improvement of $15\%$ over prior state-of-the-art methods that require large-scale pretraining and contain $10\times$ more learnable parameters. MDT shows its ability to solve long-horizon manipulation from sparsely annotated data in both simulated and real-world environments. Demonstrations and Code are available at https://intuitive-robots.github.io/mdt_policy/.

## 参考
- http://arxiv.org/abs/2407.05996v1


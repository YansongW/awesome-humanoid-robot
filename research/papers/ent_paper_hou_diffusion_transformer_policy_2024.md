---
$id: ent_paper_hou_diffusion_transformer_policy_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Diffusion Transformer Policy
  zh: Diffusion Transformer Policy
  ko: Diffusion Transformer Policy
summary:
  en: Diffusion Transformer Policy (Diffusion Transformer Policy), is a 2024 large vision-language-action model for robotic
    manipulation, introduced by Shanghai AI Lab, College of Computer Science and Technology, Zhejiang University, MMLab, The
    Chinese University of Hong Kong, Peking University, SenseTime Research, Tsinghua University, Center for Artificial Intelligence
    and Robotics, HKISI, CAS, and published at ICRA 2024.
  zh: Diffusion Transformer Policy (Diffusion Transformer Policy), is a 2024 large vision-language-action model for robotic
    manipulation, introduced by Shanghai AI Lab, College of Computer Science and Technology, Zhejiang University, MMLab, The
    Chinese University of Hong Kong, Peking University, SenseTime Research, Tsinghua University, Center for Artificial Intelligence
    and Robotics, HKISI, CAS, and published at ICRA 2024.
  ko: Diffusion Transformer Policy (Diffusion Transformer Policy), is a 2024 large vision-language-action model for robotic
    manipulation, introduced by Shanghai AI Lab, College of Computer Science and Technology, Zhejiang University, MMLab, The
    Chinese University of Hong Kong, Peking University, SenseTime Research, Tsinghua University, Center for Artificial Intelligence
    and Robotics, HKISI, CAS, and published at ICRA 2024.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- diffusion_transformer_policy
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.15959v6.
sources:
- id: src_001
  type: website
  title: Diffusion Transformer Policy source
  url: https://doi.org/10.1109/ICRA55743.2025.11128074
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Recent large vision-language-action models pretrained on diverse robot datasets have demonstrated the potential for generalizing to new environments with a few in-domain data. However, those approaches usually predict individual discretized or continuous action by a small action head, which limits the ability in handling diverse action spaces. In contrast, we model the continuous action sequence with a large multi-modal diffusion transformer, dubbed as Diffusion Transformer Policy, in which we directly denoise action chunks by a large transformer model rather than a small action head for action embedding. By leveraging the scaling capability of transformers, the proposed approach can effectively model continuous end-effector actions across large diverse robot datasets, and achieve better generalization performance. Extensive experiments demonstrate the effectiveness and generalization of Diffusion Transformer Policy on Maniskill2, Libero, Calvin and SimplerEnv, as well as the real-world Franka arm, achieving consistent better performance on Real-to-Sim benchmark SimplerEnv, real-world Franka Arm and Libero compared to OpenVLA and Octo. Specifically, without bells and whistles, the proposed approach achieves state-of-the-art performance with only a single third-view camera stream in the Calvin task ABC->D, improving the average number of tasks completed in a row of 5 to 3.6, and the pretraining stage significantly facilitates the success sequence length on the Calvin by over 1.2.

## 核心内容
Recent large vision-language-action models pretrained on diverse robot datasets have demonstrated the potential for generalizing to new environments with a few in-domain data. However, those approaches usually predict individual discretized or continuous action by a small action head, which limits the ability in handling diverse action spaces. In contrast, we model the continuous action sequence with a large multi-modal diffusion transformer, dubbed as Diffusion Transformer Policy, in which we directly denoise action chunks by a large transformer model rather than a small action head for action embedding. By leveraging the scaling capability of transformers, the proposed approach can effectively model continuous end-effector actions across large diverse robot datasets, and achieve better generalization performance. Extensive experiments demonstrate the effectiveness and generalization of Diffusion Transformer Policy on Maniskill2, Libero, Calvin and SimplerEnv, as well as the real-world Franka arm, achieving consistent better performance on Real-to-Sim benchmark SimplerEnv, real-world Franka Arm and Libero compared to OpenVLA and Octo. Specifically, without bells and whistles, the proposed approach achieves state-of-the-art performance with only a single third-view camera stream in the Calvin task ABC->D, improving the average number of tasks completed in a row of 5 to 3.6, and the pretraining stage significantly facilitates the success sequence length on the Calvin by over 1.2.

## 参考
- http://arxiv.org/abs/2410.15959v6


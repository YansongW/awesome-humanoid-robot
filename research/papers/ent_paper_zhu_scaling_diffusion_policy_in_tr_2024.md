---
$id: ent_paper_zhu_scaling_diffusion_policy_in_tr_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Scaling Diffusion Policy in Transformer to 1 Billion Parameters for Robotic Manipulation
  zh: ScaleDP
  ko: Scaling Diffusion Policy in Transformer to 1 Billion Parameters for Robotic Manipulation
summary:
  en: Scaling Diffusion Policy in Transformer to 1 Billion Parameters for Robotic Manipulation (ScaleDP), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by East China Normal University, Midea Group, Beijing
    Innovation Center of Humanoid Robotics, Shanghai University, and published at ICRA 2024.
  zh: Scaling Diffusion Policy in Transformer to 1 Billion Parameters for Robotic Manipulation (ScaleDP), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by East China Normal University, Midea Group, Beijing
    Innovation Center of Humanoid Robotics, Shanghai University, and published at ICRA 2024.
  ko: Scaling Diffusion Policy in Transformer to 1 Billion Parameters for Robotic Manipulation (ScaleDP), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by East China Normal University, Midea Group, Beijing
    Innovation Center of Humanoid Robotics, Shanghai University, and published at ICRA 2024.
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
- robotic_manipulation
- scaledp
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.14411v2.
sources:
- id: src_001
  type: website
  title: ScaleDP source
  url: https://doi.org/10.1109/ICRA55743.2025.11128074
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Diffusion Policy is a powerful technique tool for learning end-to-end visuomotor robot control. It is expected that Diffusion Policy possesses scalability, a key attribute for deep neural networks, typically suggesting that increasing model size would lead to enhanced performance. However, our observations indicate that Diffusion Policy in transformer architecture (\DP) struggles to scale effectively; even minor additions of layers can deteriorate training outcomes. To address this issue, we introduce Scalable Diffusion Transformer Policy for visuomotor learning. Our proposed method, namely \textbf{\methodname}, introduces two modules that improve the training dynamic of Diffusion Policy and allow the network to better handle multimodal action distribution. First, we identify that \DP~suffers from large gradient issues, making the optimization of Diffusion Policy unstable. To resolve this issue, we factorize the feature embedding of observation into multiple affine layers, and integrate it into the transformer blocks. Additionally, our utilize non-causal attention which allows the policy network to \enquote{see} future actions during prediction, helping to reduce compounding errors. We demonstrate that our proposed method successfully scales the Diffusion Policy from 10 million to 1 billion parameters. This new model, named \methodname, can effectively scale up the model size with improved performance and generalization. We benchmark \methodname~across 50 different tasks from MetaWorld and find that our largest \methodname~outperforms \DP~with an average improvement of 21.6\%. Across 7 real-world robot tasks, our ScaleDP demonstrates an average improvement of 36.25\% over DP-T on four single-arm tasks and 75\% on three bimanual tasks. We believe our work paves the way for scaling up models for visuomotor learning. The project page is available at scaling-diffusion-policy.github.io.

## 核心内容
Diffusion Policy is a powerful technique tool for learning end-to-end visuomotor robot control. It is expected that Diffusion Policy possesses scalability, a key attribute for deep neural networks, typically suggesting that increasing model size would lead to enhanced performance. However, our observations indicate that Diffusion Policy in transformer architecture (\DP) struggles to scale effectively; even minor additions of layers can deteriorate training outcomes. To address this issue, we introduce Scalable Diffusion Transformer Policy for visuomotor learning. Our proposed method, namely \textbf{\methodname}, introduces two modules that improve the training dynamic of Diffusion Policy and allow the network to better handle multimodal action distribution. First, we identify that \DP~suffers from large gradient issues, making the optimization of Diffusion Policy unstable. To resolve this issue, we factorize the feature embedding of observation into multiple affine layers, and integrate it into the transformer blocks. Additionally, our utilize non-causal attention which allows the policy network to \enquote{see} future actions during prediction, helping to reduce compounding errors. We demonstrate that our proposed method successfully scales the Diffusion Policy from 10 million to 1 billion parameters. This new model, named \methodname, can effectively scale up the model size with improved performance and generalization. We benchmark \methodname~across 50 different tasks from MetaWorld and find that our largest \methodname~outperforms \DP~with an average improvement of 21.6\%. Across 7 real-world robot tasks, our ScaleDP demonstrates an average improvement of 36.25\% over DP-T on four single-arm tasks and 75\% on three bimanual tasks. We believe our work paves the way for scaling up models for visuomotor learning. The project page is available at scaling-diffusion-policy.github.io.

## 参考
- http://arxiv.org/abs/2409.14411v2


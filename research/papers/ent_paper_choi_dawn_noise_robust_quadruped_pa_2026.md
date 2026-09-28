---
$id: ent_paper_choi_dawn_noise_robust_quadruped_pa_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DAWN: Noise-Robust Quadruped Parkour via Depth-Denoising World Models'
  zh: 'DAWN: Noise-Robust Quadruped Parkour via Depth-Denoising World Models'
  ko: 'DAWN: Noise-Robust Quadruped Parkour via Depth-Denoising World Models'
summary:
  en: Vision-based legged locomotion methods assume clean depth at training time and rely on hand-tuned post-processing filters
    at deployment. However, filter parameters are rarely disclosed, hindering reproducibility, and performance degrades substantially
    when depth noise is left unaddressed. Building noise robustness directly into the learning pipeline would eliminate this
    dependency. While such ...
  zh: DAWN（Denoising and Alignment in World models for Noise-robustness）是一个面向足式运动的噪声鲁棒感知框架，由 Yohan Choi、Min-Jun Kim、Jin-Sung
    Kim、Yong-Jae Kim、Youn-Hee Han 提出。它通过让世界模型以含噪深度为输入、以干净深度为重建目标，并用对比学习对齐两者的隐状态，把噪声鲁棒性直接内建到学习流程中。在 Unitree Go1 上，该方法无需任何人工滤波标定即实现零样本四足跑酷，可攀爬最高
    18 cm 的楼梯、跨越最宽 70 cm 的沟壑、登上最高 45 cm 的台阶。
  ko: Vision-based legged locomotion methods assume clean depth at training time and rely on hand-tuned post-processing filters
    at deployment. However, filter parameters are rarely disclosed, hindering reproducibility, and performance degrades substantially
    when depth noise is left unaddressed. Building noise robustness directly into the learning pipeline would eliminate this
    dependency. While such ...
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- quadruped_parkour
- depth_denoising
- world_models
- contrastive_learning
- noise_robustness
- legged_locomotion
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-28'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-28). Bibliographic metadata from arXiv API (2609.29092);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.29092 DAWN: Noise-Robust Quadruped Parkour via Depth-Denoising World Models'
  url: https://arxiv.org/abs/2609.29092
  date: '2026-09-24'
  accessed_at: '2026-09-28'
---

## 概述

现有基于视觉的足式运动方法在训练时假设深度图是干净的，部署时则依赖人工调参的后处理滤波器，而滤波参数往往不公开，影响可复现性，且深度噪声未被处理时性能会明显下降。针对本体感知输入的噪声鲁棒性已有研究，但深度感知方向的类似方案在足式运动中基本缺失。DAWN 将噪声鲁棒性直接构建进世界模型：一方面把含噪深度送入编码器、同时以干净深度作为重建目标，迫使模型隐式去噪；另一方面用对比学习对齐含噪与干净深度的隐状态。该方法不绑定特定噪声模型，部署时无需针对噪声分布手工调参，且相比现有基于世界模型的方法不增加额外推理开销。仅依靠学到的噪声鲁棒表征、不做任何人工滤波标定，DAWN 就在 Unitree Go1 上实现了零样本四足跑酷。

## 核心内容

### 问题背景
基于视觉的足式运动方法通常在训练阶段假定深度输入是干净的，而在实际部署时依靠人工调参的后处理滤波器来应对噪声。这类滤波器的参数很少被公开，导致复现困难；若不对深度噪声加以处理，性能会显著退化。把噪声鲁棒性直接嵌入学习流程，可以摆脱对人工滤波的依赖。此前这类鲁棒性研究多集中在本体感知输入上，深度感知方向的对应方案在足式运动中仍基本空白。

### 方法
作者提出 DAWN（Denoising and Alignment in World models for Noise-robustness），一个面向足式运动的噪声鲁棒感知框架，通过两项改动把噪声鲁棒性直接构建进世界模型：
- **隐式去噪**：将含噪深度送入编码器，同时保留干净深度作为重建目标，迫使模型对输入进行隐式去噪。
- **对比对齐**：采用对比学习，对齐含噪深度与干净深度对应的隐状态。

该框架不绑定特定噪声模型，部署时无需针对噪声分布进行人工调参；与现有基于世界模型的方法相比，不产生额外的推理开销。

### 实验设置与关键结果
在 Unitree Go1 四足机器人上，DAWN 不做任何人工滤波标定，仅依赖学到的噪声鲁棒表征，即实现零样本跑酷，直接使用原始深度观测完成：
- 攀爬最高 18 cm 的楼梯；
- 跨越最宽 70 cm 的沟壑；
- 登上最高 45 cm 的台阶。

### 消融与结论
消融研究表明，去噪与对比对齐分别在互补层面发挥作用——前者作用于重建，后者作用于表征——两者结合时带来可叠加的增益。论文的视频与代码发布于 https://dawn-parkour.github.io/ 。

## Overview

Vision-based legged locomotion methods assume clean depth at training time and rely on hand-tuned post-processing filters at deployment. However, filter parameters are rarely disclosed, hindering reproducibility, and performance degrades substantially when depth noise is left unaddressed. Building noise robustness directly into the learning pipeline would eliminate this dependency. While such robustness has been explored for proprioceptive inputs, analogous approaches for depth perception remain largely absent in legged locomotion. We propose DAWN (Denoising and Alignment in World models for Noise-robustness), a noise-robust perception framework for legged locomotion, which builds noise robustness directly into a world model via two modifications: (1) feeding noisy depth to the encoder while keeping clean depth as the reconstruction target, forcing the model to implicitly denoise its input; and (2) applying contrastive learning to align the latent states of noisy and clean depth. Importantly, DAWN is not tied to a specific noise model, requiring no manual tuning to the noise distribution at deployment. Furthermore, it incurs no additional inference cost over existing world model-based methods. Without any manual filter calibration -- relying solely on the learned noise-robust representation -- DAWN achieves zero-shot quadruped parkour on a Unitree Go1: traversing stairs up to 18 cm, clearing gaps up to 70 cm, and mounting steps up to 45 cm from raw depth observations. Ablation studies show that denoising and contrastive alignment contribute at complementary levels -- reconstruction and representation, respectively -- and yield additive gains when combined. Videos and code are available at: https://dawn-parkour.github.io/

## 参考
- https://arxiv.org/abs/2609.29092

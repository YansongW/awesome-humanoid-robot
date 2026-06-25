---
$id: ent_paper_ho_denoising_diffusion_probabilis_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Denoising Diffusion Probabilistic Models
  zh: 去噪扩散概率模型
  ko: 노이즈 제거 확산 확률 모델
summary:
  en: Ho, Jain, and Abbeel (2020) introduce a denoising diffusion probabilistic model
    trained with a simplified weighted variational bound, achieving high-quality image
    synthesis on CIFAR-10 and LSUN datasets.
  zh: Ho、Jain和Abbeel（2020）提出了一种使用简化加权变分下界训练的去噪扩散概率模型，在CIFAR-10和LSUN数据集上实现了高质量的图像合成。
  ko: Ho, Jain, Abbeel(2020)는 단순화된 가중 변분 하한으로 학습된 노이즈 제거 확산 확률 모델을 제안하여 CIFAR-10 및
    LSUN 데이터셋에서 고품질 이미지 합성을 달성했다.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- diffusion_model
- generative_model
- denoising
- image_synthesis
- synthetic_data
- score_matching
- langevin_dynamics
- u_net
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: AI-extracted from abstract and metadata; full-text review needed to confirm
    exact section citations and relationship scope.
sources:
- id: src_001
  type: paper
  title: Denoising Diffusion Probabilistic Models
  url: https://arxiv.org/abs/2006.11239
  date: '2020'
  accessed_at: '2026-06-25'
---

## Overview

Denoising Diffusion Probabilistic Models (DDPM) present a class of latent variable models inspired by nonequilibrium thermodynamics. The authors train a U-Net to reverse a fixed Markov chain that gradually adds Gaussian noise to data, and they derive a simplified training objective that corresponds to predicting the noise added at each step. Their formulation reveals a novel equivalence between diffusion probabilistic models and denoising score matching with annealed Langevin dynamics, enabling high-fidelity sample generation.

The proposed model achieves strong quantitative results: an Inception score of 9.46 and a state-of-the-art FID of 3.17 on unconditional CIFAR-10, as well as sample quality comparable to ProgressiveGAN on 256x256 LSUN datasets. The authors also interpret the sampling process as a progressive lossy decompression scheme that generalizes autoregressive decoding.

## Key Contributions

- Demonstrates that diffusion models can generate high-quality images competitive with GANs on CIFAR-10 and LSUN.
- Establishes a novel equivalence between diffusion probabilistic models and denoising score matching with Langevin dynamics.
- Introduces the epsilon-prediction parameterization and a simplified weighted variational bound for training.
- Shows that diffusion sampling can be interpreted as progressive lossy decompression generalizing autoregressive decoding.

## Relevance to Humanoid Robotics

Diffusion models provide a controllable, high-quality generative foundation that can support future humanoid robot capabilities. They may be used to synthesize realistic visual data for perception training, generate diverse motion trajectories for planning, and produce simulated environments for policy learning and system validation. The epsilon-prediction formulation and multi-step denoising process have become building blocks for later conditional generative systems relevant to robotics. However, this paper does not address humanoid hardware, control, or deployment directly.

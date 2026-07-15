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
  en: Ho, Jain, and Abbeel (2020) introduce a denoising diffusion probabilistic model trained with a simplified weighted variational
    bound, achieving high-quality image synthesis on CIFAR-10 and LSUN datasets.
  zh: We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models
    inspired by considerations from nonequilibrium thermodynamics. Our best results are obtained by training on a weighted
    variational bound designed according to a novel connection between diffusion probabilistic models and denoising score
    matching with Langevin dynamics, and our models naturally admit a progressive lossy decompression scheme that can be interpreted
    as a generalization of autoregressive decoding. On the unconditional CIFAR10 dataset, we obtain an Inception score
  ko: Ho, Jain, Abbeel(2020)는 단순화된 가중 변분 하한으로 학습된 노이즈 제거 확산 확률 모델을 제안하여 CIFAR-10 및 LSUN 데이터셋에서 고품질 이미지 합성을 달성했다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2006.11239v2.
sources:
- id: src_001
  type: paper
  title: Denoising Diffusion Probabilistic Models
  url: https://arxiv.org/abs/2006.11239
  date: '2020'
  accessed_at: '2026-06-25'
theoretical_depth:
- system
---

## 概述
We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics. Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score matching with Langevin dynamics, and our models naturally admit a progressive lossy decompression scheme that can be interpreted as a generalization of autoregressive decoding. On the unconditional CIFAR10 dataset, we obtain an Inception score of 9.46 and a state-of-the-art FID score of 3.17. On 256x256 LSUN, we obtain sample quality similar to ProgressiveGAN. Our implementation is available at https://github.com/hojonathanho/diffusion

## 核心内容
We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics. Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score matching with Langevin dynamics, and our models naturally admit a progressive lossy decompression scheme that can be interpreted as a generalization of autoregressive decoding. On the unconditional CIFAR10 dataset, we obtain an Inception score of 9.46 and a state-of-the-art FID score of 3.17. On 256x256 LSUN, we obtain sample quality similar to ProgressiveGAN. Our implementation is available at https://github.com/hojonathanho/diffusion

## 参考
- http://arxiv.org/abs/2006.11239v2



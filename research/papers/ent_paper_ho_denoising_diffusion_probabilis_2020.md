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
  zh: Ho, Jain 与 Abbeel 于 2020 年提出去噪扩散概率模型，通过简化加权变分界进行训练，在 CIFAR-10 与 LSUN 数据集上实现了高质量图像合成。该模型受非平衡热力学启发，并建立了扩散模型与去噪得分匹配之间的新联系。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2006.11239v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
本文提出了一类基于扩散概率模型的潜变量模型，其灵感来源于非平衡热力学。通过设计加权变分界，模型在训练中实现了高效优化，并自然支持渐进式有损解压缩方案，可视为自回归解码的推广。在无条件 CIFAR-10 数据集上，模型取得了 9.46 的 Inception 分数与 3.17 的 FID 分数，达到当时最优水平；在 256x256 LSUN 数据集上，样本质量与 ProgressiveGAN 相当。

## 核心内容
### 方法概述
- 扩散概率模型通过逐步向数据添加噪声（前向过程）并学习逆向去噪过程来生成样本。
- 训练目标为加权变分下界，该下界基于扩散模型与去噪得分匹配（Denoising Score Matching）及 Langevin 动力学之间的新联系设计。

### 关键架构与实验
- 模型采用 U-Net 架构，并在时间步上引入条件嵌入。
- 在 CIFAR-10 上，无条件生成任务中 Inception 分数达 9.46，FID 分数为 3.17，刷新当时最优记录。
- 在 256x256 LSUN 数据集上，模型生成的样本质量与 ProgressiveGAN 相当，展示了高分辨率图像合成能力。

### 渐进式解压缩
- 模型天然支持渐进式有损解压缩，可逐步细化生成图像，类似于自回归解码的泛化形式。

### 代码与复现
- 实现代码已开源，地址为 https://github.com/hojonathanho/diffusion。

## Overview
We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics. Our best results are obtained by training on a weighted variational bound designed according to a novel connection between diffusion probabilistic models and denoising score matching with Langevin dynamics, and our models naturally admit a progressive lossy decompression scheme that can be interpreted as a generalization of autoregressive decoding. On the unconditional CIFAR10 dataset, we obtain an Inception score of 9.46 and a state-of-the-art FID score of 3.17. On 256x256 LSUN, we obtain sample quality similar to ProgressiveGAN. Our implementation is available at https://github.com/hojonathanho/diffusion

## 개요
우리는 비평형 열역학의 고려 사항에서 영감을 받은 잠재 변수 모델 클래스인 확산 확률적 모델을 사용하여 고품질 이미지 합성 결과를 제시합니다. 최고의 결과는 확산 확률적 모델과 Langevin 역학을 이용한 잡음 제거 점수 매칭 간의 새로운 연결에 따라 설계된 가중 변분 경계에서 훈련하여 얻었으며, 우리의 모델은 자연스럽게 자기회귀 디코딩의 일반화로 해석될 수 있는 점진적 손실 압축 해제 방식을 허용합니다. 비조건부 CIFAR10 데이터셋에서 Inception 점수 9.46과 최첨단 FID 점수 3.17을 달성했습니다. 256x256 LSUN에서는 ProgressiveGAN과 유사한 샘플 품질을 얻었습니다. 구현체는 https://github.com/hojonathanho/diffusion 에서 확인할 수 있습니다.

## 핵심 내용
우리는 비평형 열역학의 고려 사항에서 영감을 받은 잠재 변수 모델 클래스인 확산 확률적 모델을 사용하여 고품질 이미지 합성 결과를 제시합니다. 최고의 결과는 확산 확률적 모델과 Langevin 역학을 이용한 잡음 제거 점수 매칭 간의 새로운 연결에 따라 설계된 가중 변분 경계에서 훈련하여 얻었으며, 우리의 모델은 자연스럽게 자기회귀 디코딩의 일반화로 해석될 수 있는 점진적 손실 압축 해제 방식을 허용합니다. 비조건부 CIFAR10 데이터셋에서 Inception 점수 9.46과 최첨단 FID 점수 3.17을 달성했습니다. 256x256 LSUN에서는 ProgressiveGAN과 유사한 샘플 품질을 얻었습니다. 구현체는 https://github.com/hojonathanho/diffusion 에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2006.11239v2

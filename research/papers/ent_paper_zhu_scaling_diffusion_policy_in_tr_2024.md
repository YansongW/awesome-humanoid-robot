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
  zh: ScaleDP 是 2024 年由华东师范大学、美的集团、北京人形机器人创新中心及上海大学联合提出的十亿参数级视觉-语言-动作模型，发表于 ICRA 2024。其核心贡献在于解决了 Diffusion Policy 在 Transformer
    架构中难以扩展的问题，通过引入特征分解与非因果注意力机制，成功将模型参数从 1000 万扩展至 10 亿，并在 MetaWorld 的 50 个任务及 7 项真实机器人操作任务中取得显著性能提升。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.14411v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: website
  title: ScaleDP source
  url: https://doi.org/10.1109/ICRA55743.2025.11128074
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
ScaleDP 针对 Diffusion Policy 在 Transformer 架构中因梯度爆炸和优化不稳定而无法有效扩展的问题，提出了两项关键改进：一是将观测特征嵌入分解为多个仿射层并集成至 Transformer 块中，以缓解大梯度问题；二是采用非因果注意力机制，使策略网络在预测时能“看到”未来动作，从而减少累积误差。实验表明，ScaleDP 在 MetaWorld 的 50 个任务上平均性能比 DP-T 提升 21.6%，在 7 项真实机器人任务中，单臂任务平均提升 36.25%，双臂任务平均提升 75%。

## 核心内容
### 方法架构
- **问题诊断**：研究发现，Diffusion Policy 在 Transformer 架构中扩展时，即使仅增加少量层数也会导致训练效果恶化，主要原因是梯度值过大导致优化不稳定。
- **特征分解模块**：将观测特征嵌入分解为多个仿射层，并集成至 Transformer 块中，通过参数化方式改善梯度流动，使网络能更稳定地处理多模态动作分布。
- **非因果注意力**：在预测过程中，策略网络通过非因果注意力机制能够同时参考未来动作信息，有效减少因时序依赖导致的累积误差。

### 实验设置与关键数字
- **模型规模**：成功将 Diffusion Policy 从 1000 万参数扩展至 10 亿参数，验证了方法的可扩展性。
- **仿真基准**：在 MetaWorld 的 50 个不同任务上测试，最大规模 ScaleDP 平均性能比 DP-T 提升 21.6%。
- **真实机器人任务**：在 7 项任务中，单臂任务（4 项）平均提升 36.25%，双臂任务（3 项）平均提升 75%。

### 结论
ScaleDP 通过解决 Diffusion Policy 的扩展瓶颈，首次实现了十亿参数级视觉-运动策略的有效训练，为大规模视觉运动学习模型的发展奠定了基础。项目页面：scaling-diffusion-policy.github.io。

## Overview
Diffusion Policy is a powerful technique tool for learning end-to-end visuomotor robot control. It is expected that Diffusion Policy possesses scalability, a key attribute for deep neural networks, typically suggesting that increasing model size would lead to enhanced performance. However, our observations indicate that Diffusion Policy in transformer architecture (\DP) struggles to scale effectively; even minor additions of layers can deteriorate training outcomes. To address this issue, we introduce Scalable Diffusion Transformer Policy for visuomotor learning. Our proposed method, namely \textbf{\methodname}, introduces two modules that improve the training dynamic of Diffusion Policy and allow the network to better handle multimodal action distribution. First, we identify that \DP~suffers from large gradient issues, making the optimization of Diffusion Policy unstable. To resolve this issue, we factorize the feature embedding of observation into multiple affine layers, and integrate it into the transformer blocks. Additionally, our utilize non-causal attention which allows the policy network to \enquote{see} future actions during prediction, helping to reduce compounding errors. We demonstrate that our proposed method successfully scales the Diffusion Policy from 10 million to 1 billion parameters. This new model, named \methodname, can effectively scale up the model size with improved performance and generalization. We benchmark \methodname~across 50 different tasks from MetaWorld and find that our largest \methodname~outperforms \DP~with an average improvement of 21.6\%. Across 7 real-world robot tasks, our ScaleDP demonstrates an average improvement of 36.25\% over DP-T on four single-arm tasks and 75\% on three bimanual tasks. We believe our work paves the way for scaling up models for visuomotor learning. The project page is available at scaling-diffusion-policy.github.io.

## 개요
Diffusion Policy은 엔드투엔드 시각운동 로봇 제어를 학습하기 위한 강력한 기술 도구입니다. Diffusion Policy은 심층 신경망의 핵심 속성인 확장성을 가질 것으로 예상되며, 일반적으로 모델 크기를 증가시키면 성능이 향상될 것임을 시사합니다. 그러나 우리의 관찰에 따르면 트랜스포머 아키텍처의 Diffusion Policy(\DP)는 효과적으로 확장하는 데 어려움을 겪으며, 약간의 레이어 추가만으로도 훈련 결과가 악화될 수 있습니다. 이 문제를 해결하기 위해 우리는 시각운동 학습을 위한 확장 가능한 확산 트랜스포머 정책(Scalable Diffusion Transformer Policy)을 소개합니다. 우리가 제안하는 방법, 즉 \textbf{\methodname}은 Diffusion Policy의 훈련 역학을 개선하고 네트워크가 다중 모드 행동 분포를 더 잘 처리할 수 있도록 하는 두 가지 모듈을 도입합니다. 첫째, 우리는 \DP~가 큰 그래디언트 문제를 겪어 Diffusion Policy의 최적화를 불안정하게 만든다는 것을 확인했습니다. 이 문제를 해결하기 위해 우리는 관찰의 특징 임베딩을 여러 아핀 레이어로 분해하고 이를 트랜스포머 블록에 통합합니다. 또한, 우리는 비인과적 주의(non-causal attention)를 사용하여 정책 네트워크가 예측 중 미래 행동을 \enquote{볼} 수 있도록 하여 오류 누적을 줄이는 데 도움을 줍니다. 우리는 제안된 방법이 Diffusion Policy을 1천만 개에서 10억 개의 파라미터로 성공적으로 확장함을 입증합니다. \methodname이라는 이 새로운 모델은 성능과 일반화가 향상된 모델 크기를 효과적으로 확장할 수 있습니다. 우리는 MetaWorld의 50가지 다양한 작업에서 \methodname~을 벤치마킹했으며, 가장 큰 \methodname~이 \DP~보다 평균 21.6% 향상된 성능을 보임을 발견했습니다. 7가지 실제 로봇 작업에서 우리의 ScaleDP는 4가지 단일 암 작업에서 DP-T보다 평균 36.25%, 3가지 양손 작업에서 75%의 향상을 보여줍니다. 우리의 연구가 시각운동 학습을 위한 모델 확장의 길을 열 것이라고 믿습니다. 프로젝트 페이지는 scaling-diffusion-policy.github.io에서 확인할 수 있습니다.

## 핵심 내용
Diffusion Policy은 엔드투엔드 시각운동 로봇 제어를 학습하기 위한 강력한 기술 도구입니다. Diffusion Policy은 심층 신경망의 핵심 속성인 확장성을 가질 것으로 예상되며, 일반적으로 모델 크기를 증가시키면 성능이 향상될 것임을 시사합니다. 그러나 우리의 관찰에 따르면 트랜스포머 아키텍처의 Diffusion Policy(\DP)는 효과적으로 확장하는 데 어려움을 겪으며, 약간의 레이어 추가만으로도 훈련 결과가 악화될 수 있습니다. 이 문제를 해결하기 위해 우리는 시각운동 학습을 위한 확장 가능한 확산 트랜스포머 정책(Scalable Diffusion Transformer Policy)을 소개합니다. 우리가 제안하는 방법, 즉 \textbf{\methodname}은 Diffusion Policy의 훈련 역학을 개선하고 네트워크가 다중 모드 행동 분포를 더 잘 처리할 수 있도록 하는 두 가지 모듈을 도입합니다. 첫째, 우리는 \DP~가 큰 그래디언트 문제를 겪어 Diffusion Policy의 최적화를 불안정하게 만든다는 것을 확인했습니다. 이 문제를 해결하기 위해 우리는 관찰의 특징 임베딩을 여러 아핀 레이어로 분해하고 이를 트랜스포머 블록에 통합합니다. 또한, 우리는 비인과적 주의(non-causal attention)를 사용하여 정책 네트워크가 예측 중 미래 행동을 \enquote{볼} 수 있도록 하여 오류 누적을 줄이는 데 도움을 줍니다. 우리는 제안된 방법이 Diffusion Policy을 1천만 개에서 10억 개의 파라미터로 성공적으로 확장함을 입증합니다. \methodname이라는 이 새로운 모델은 성능과 일반화가 향상된 모델 크기를 효과적으로 확장할 수 있습니다. 우리는 MetaWorld의 50가지 다양한 작업에서 \methodname~을 벤치마킹했으며, 가장 큰 \methodname~이 \DP~보다 평균 21.6% 향상된 성능을 보임을 발견했습니다. 7가지 실제 로봇 작업에서 우리의 ScaleDP는 4가지 단일 암 작업에서 DP-T보다 평균 36.25%, 3가지 양손 작업에서 75%의 향상을 보여줍니다. 우리의 연구가 시각운동 학습을 위한 모델 확장의 길을 열 것이라고 믿습니다. 프로젝트 페이지는 scaling-diffusion-policy.github.io에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2409.14411v2

---
$id: ent_paper_ke_3d_diffuser_actor_policy_diffu_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '3D Diffuser Actor: Policy Diffusion with 3D Scene Representations'
  zh: 3D Diffuser Actor
  ko: '3D Diffuser Actor: Policy Diffusion with 3D Scene Representations'
summary:
  en: '3D Diffuser Actor: Policy Diffusion with 3D Scene Representations (3D Diffuser Actor), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Carnegie Mellon University, and published at CoRL 2024.'
  zh: 3D Diffuser Actor 是由卡内基梅隆大学提出的2024年通用视觉-语言-动作模型，用于机器人操作任务，发表于 CoRL 2024。其核心贡献在于将扩散策略与3D场景表示统一，通过新型3D去噪Transformer融合视觉、语言指令和本体感知信息，在RLBench和CALVIN基准上取得显著性能提升，并支持从少量演示中学习真实世界操控。
  ko: '3D Diffuser Actor: Policy Diffusion with 3D Scene Representations (3D Diffuser Actor), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Carnegie Mellon University, and published at CoRL 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- 3d_diffuser_actor
- generalist_policy
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2402.10885v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 3D Diffuser Actor source
  url: https://proceedings.mlr.press/v270/ke25a.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
该模型结合了扩散策略和3D机器人策略的优势：扩散策略通过条件扩散模型学习动作分布，优于确定性方法；3D策略利用深度感知从多视角聚合3D特征，比2D方法具有更好的视角泛化能力。3D Diffuser Actor 通过3D去噪Transformer处理带噪的3D机器人位姿轨迹，在RLBench多视角设置下绝对性能提升18.1%，单视角提升13.1%，在CALVIN上相对提升9%。实验表明，其设计选择（如3D表示、扩散目标、token化嵌入）显著优于2D表示、回归/分类目标、绝对注意力机制和整体非token化3D场景嵌入。

## 核心内容
### 方法架构
- **核心框架**：基于条件扩散模型，学习机器人动作分布 \( p(a_t | o_t, l) \)，其中 \( o_t \) 为观测（含3D场景点云、本体感知），\( l \) 为语言指令。
- **3D去噪Transformer**：将3D场景点云token化，与语言指令和本体感知嵌入融合，通过交叉注意力机制预测噪声，逐步去噪生成3D位姿轨迹。
- **输入表示**：使用深度传感器从单/多视角构建3D场景特征，避免2D方法的视角依赖问题。

### 实验设置
- **基准测试**：
  - **RLBench**：多视角设置下，绝对性能提升18.1%（超越当前SOTA）；单视角设置下提升13.1%。
  - **CALVIN**：相对性能提升9%。
- **真实世界实验**：从少量演示（handful of demonstrations）中学习，成功控制机械臂完成操作任务。

### 关键设计对比
- **3D vs 2D表示**：3D场景token化显著优于2D特征，尤其在视角变化时。
- **扩散目标 vs 回归/分类**：扩散策略在动作分布建模上更优，避免确定性方法的模式崩溃。
- **注意力机制**：使用相对位置编码的注意力，优于绝对注意力。
- **token化 vs 整体嵌入**：将3D场景分解为token序列，比直接使用全局嵌入更有效。

### 结论
3D Diffuser Actor 通过统一扩散策略与3D表示，在多个基准上刷新SOTA，验证了3D场景token化与扩散去噪在机器人操作中的协同优势。其设计选择为未来策略学习提供了重要参考。

## Overview
Diffusion policies are conditional diffusion models that learn robot action distributions conditioned on the robot and environment state. They have recently shown to outperform both deterministic and alternative action distribution learning formulations. 3D robot policies use 3D scene feature representations aggregated from a single or multiple camera views using sensed depth. They have shown to generalize better than their 2D counterparts across camera viewpoints. We unify these two lines of work and present 3D Diffuser Actor, a neural policy equipped with a novel 3D denoising transformer that fuses information from the 3D visual scene, a language instruction and proprioception to predict the noise in noised 3D robot pose trajectories. 3D Diffuser Actor sets a new state-of-the-art on RLBench with an absolute performance gain of 18.1% over the current SOTA on a multi-view setup and an absolute gain of 13.1% on a single-view setup. On the CALVIN benchmark, it improves over the current SOTA by a 9% relative increase. It also learns to control a robot manipulator in the real world from a handful of demonstrations. Through thorough comparisons with the current SOTA policies and ablations of our model, we show 3D Diffuser Actor's design choices dramatically outperform 2D representations, regression and classification objectives, absolute attentions, and holistic non-tokenized 3D scene embeddings.

## 개요
Diffusion policies는 로봇과 환경 상태에 조건화된 로봇 행동 분포를 학습하는 조건부 확산 모델입니다. 최근 이들은 결정론적 및 대안적 행동 분포 학습 방식보다 뛰어난 성능을 보여주고 있습니다. 3D 로봇 정책은 감지된 깊이를 사용하여 단일 또는 다중 카메라 뷰에서 집계된 3D 장면 특징 표현을 활용합니다. 이들은 카메라 시점에 걸쳐 2D 기반 정책보다 더 나은 일반화 성능을 보여주었습니다. 우리는 이 두 연구 흐름을 통합하여 3D Diffuser Actor를 제시합니다. 이는 새로운 3D 노이즈 제거 트랜스포머를 갖춘 신경 정책으로, 3D 시각 장면, 언어 명령 및 고유 감각 정보를 융합하여 노이즈가 포함된 3D 로봇 포즈 궤적의 노이즈를 예측합니다. 3D Diffuser Actor는 RLBench에서 다중 뷰 설정에서 현재 SOTA 대비 18.1%의 절대 성능 향상, 단일 뷰 설정에서 13.1%의 절대 향상으로 새로운 최고 성능을 기록했습니다. CALVIN 벤치마크에서는 현재 SOTA 대비 9%의 상대적 개선을 이루었습니다. 또한 소수의 시연만으로 실제 세계에서 로봇 매니퓰레이터를 제어하는 방법을 학습합니다. 현재 SOTA 정책과의 철저한 비교 및 모델의 절제 연구를 통해, 3D Diffuser Actor의 설계 선택이 2D 표현, 회귀 및 분류 목표, 절대적 주의 메커니즘, 전체적 비토큰화 3D 장면 임베딩보다 훨씬 뛰어난 성능을 발휘함을 보여줍니다.

## 핵심 내용
Diffusion policies는 로봇과 환경 상태에 조건화된 로봇 행동 분포를 학습하는 조건부 확산 모델입니다. 최근 이들은 결정론적 및 대안적 행동 분포 학습 방식보다 뛰어난 성능을 보여주고 있습니다. 3D 로봇 정책은 감지된 깊이를 사용하여 단일 또는 다중 카메라 뷰에서 집계된 3D 장면 특징 표현을 활용합니다. 이들은 카메라 시점에 걸쳐 2D 기반 정책보다 더 나은 일반화 성능을 보여주었습니다. 우리는 이 두 연구 흐름을 통합하여 3D Diffuser Actor를 제시합니다. 이는 새로운 3D 노이즈 제거 트랜스포머를 갖춘 신경 정책으로, 3D 시각 장면, 언어 명령 및 고유 감각 정보를 융합하여 노이즈가 포함된 3D 로봇 포즈 궤적의 노이즈를 예측합니다. 3D Diffuser Actor는 RLBench에서 다중 뷰 설정에서 현재 SOTA 대비 18.1%의 절대 성능 향상, 단일 뷰 설정에서 13.1%의 절대 향상으로 새로운 최고 성능을 기록했습니다. CALVIN 벤치마크에서는 현재 SOTA 대비 9%의 상대적 개선을 이루었습니다. 또한 소수의 시연만으로 실제 세계에서 로봇 매니퓰레이터를 제어하는 방법을 학습합니다. 현재 SOTA 정책과의 철저한 비교 및 모델의 절제 연구를 통해, 3D Diffuser Actor의 설계 선택이 2D 표현, 회귀 및 분류 목표, 절대적 주의 메커니즘, 전체적 비토큰화 3D 장면 임베딩보다 훨씬 뛰어난 성능을 발휘함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2402.10885v3

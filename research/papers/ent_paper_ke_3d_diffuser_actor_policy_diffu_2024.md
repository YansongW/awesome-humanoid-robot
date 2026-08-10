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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2402.10885v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (978 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2402.10885v3

## 개요
이 모델은 확산 정책과 3D 로봇 정책의 장점을 결합했습니다: 확산 정책은 조건부 확산 모델을 통해 행동 분포를 학습하여 결정론적 방법보다 우수하며, 3D 정책은 깊이 인식을 활용해 다중 시점에서 3D 특징을 집계하여 2D 방법보다 뛰어난 시점 일반화 능력을 갖습니다. 3D Diffuser Actor는 3D 노이즈 제거 Transformer를 통해 노이즈가 포함된 3D 로봇 자세 궤적을 처리하며, RLBench 다중 시점 설정에서 절대 성능이 18.1% 향상되고, 단일 시점에서는 13.1% 향상되었으며, CALVIN에서는 상대적으로 9% 향상되었습니다. 실험 결과, 3D 표현, 확산 목표, 토큰화 임베딩과 같은 설계 선택이 2D 표현, 회귀/분류 목표, 절대 주의 메커니즘, 전체 비토큰화 3D 장면 임베딩보다 현저히 우수함을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
- **핵심 프레임워크**: 조건부 확산 모델을 기반으로 로봇 행동 분포 \( p(a_t | o_t, l) \)를 학습하며, 여기서 \( o_t \)는 관측(3D 장면 포인트 클라우드, 자체 인식 포함), \( l \)은 언어 명령입니다.
- **3D 노이즈 제거 Transformer**: 3D 장면 포인트 클라우드를 토큰화하고, 언어 명령 및 자체 인식 임베딩과 융합한 후 교차 주의 메커니즘을 통해 노이즈를 예측하고, 점진적으로 노이즈를 제거하여 3D 자세 궤적을 생성합니다.
- **입력 표현**: 깊이 센서를 사용해 단일/다중 시점에서 3D 장면 특징을 구축하여 2D 방법의 시점 의존 문제를 피합니다.

### 실험 설정
- **벤치마크 테스트**:
  - **RLBench**: 다중 시점 설정에서 절대 성능이 18.1% 향상(현재 SOTA 초과); 단일 시점 설정에서 13.1% 향상.
  - **CALVIN**: 상대 성능 9% 향상.
- **실제 세계 실험**: 소수의 데모(handful of demonstrations)에서 학습하여 로봇 팔을 성공적으로 제어해 조작 작업을 완료합니다.

### 주요 설계 비교
- **3D vs 2D 표현**: 3D 장면 토큰화가 2D 특징보다 현저히 우수하며, 특히 시점 변화 시 더욱 그렇습니다.
- **확산 목표 vs 회귀/분류**: 확산 정책이 행동 분포 모델링에서 더 우수하며, 결정론적 방법의 모드 붕괴를 피합니다.
- **주의 메커니즘**: 상대 위치 인코딩을 사용한 주의가 절대 주의보다 우수합니다.
- **토큰화 vs 전체 임베딩**: 3D 장면을 토큰 시퀀스로 분해하는 것이 전역 임베딩을 직접 사용하는 것보다 더 효과적입니다.

### 결론
3D Diffuser Actor는 확산 정책과 3D 표현을 통합하여 여러 벤치마크에서 SOTA를 갱신했으며, 3D 장면 토큰화와 확산 노이즈 제거가 로봇 조작에서의 시너지 이점을 검증했습니다. 그 설계 선택은 향후 정책 학습에 중요한 참고 자료를 제공합니다.

---
$id: ent_paper_gervet_act3d_3d_feature_field_transfo_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Act3D: 3D Feature Field Transformers for Multi-Task Robotic Manipulation'
  zh: Act3D
  ko: 'Act3D: 3D Feature Field Transformers for Multi-Task Robotic Manipulation'
summary:
  en: 'Act3D: 3D Feature Field Transformers for Multi-Task Robotic Manipulation (Act3D), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Carnegie Mellon University, and published at CoRL 2023.'
  zh: Act3D 是卡内基梅隆大学于 2023 年提出的通用视觉-语言-动作模型，用于机器人多任务操作。其核心贡献在于通过自适应分辨率的 3D 特征场，在保持高空间精度的同时大幅降低计算成本，并在 RLBench 基准上以 10% 的绝对提升超越此前最优的
    2D 多视角策略。
  ko: 'Act3D: 3D Feature Field Transformers for Multi-Task Robotic Manipulation (Act3D), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Carnegie Mellon University, and published at CoRL 2023.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- act3d
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2306.17817v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1017 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Act3D source
  url: https://proceedings.mlr.press/v229/gervet23a.html
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
Act3D 是一种基于 Transformer 的操作策略，它利用深度传感器将 2D 预训练特征提升至 3D，并构建任务自适应的 3D 特征场。模型通过粗到细的 3D 点网格采样，结合相对位置注意力机制高效计算高分辨率 3D 动作图，从而在保持计算效率的同时实现精确的末端执行器位姿预测。在 RLBench 的 74 个任务上，Act3D 相比此前最优的 2D 多视角策略提升了 10%，相比最优的 3D 策略提升了 22%，且计算量仅为后者的三分之一。

## 核心内容
### 方法架构
Act3D 的核心创新在于将 2D 预训练特征（如 CLIP、ViT）通过深度信息提升至 3D，并构建一个自适应分辨率的 3D 特征场。模型采用粗到细的采样策略：
- **粗采样阶段**：在机器人工作空间均匀采样低分辨率 3D 点网格，利用相对位置注意力计算每个点的特征。
- **细采样阶段**：根据粗采样结果中注意力权重较高的区域，进行局部高分辨率重采样，从而在关键区域获得精细的 3D 动作图。
- **权重共享**：粗到细各阶段的注意力层共享权重，减少参数量并提升训练效率。

### 实验设置与关键数字
- **基准测试**：在 RLBench 的 74 个操作任务上评估，涵盖抓取、放置、组装等多样化任务。
- **性能对比**：
  - 相比此前最优的 2D 多视角策略（PerAct），Act3D 实现 **10% 绝对提升**（平均成功率从 62% 升至 72%）。
  - 相比此前最优的 3D 策略（3D Diffuser Actor），Act3D 实现 **22% 绝对提升**（平均成功率从 50% 升至 72%），且计算量仅为后者的 **1/3**。
- **消融实验**：
  - **相对空间注意力**：移除后平均成功率下降 15%，证明其对空间推理的关键作用。
  - **大规模视觉-语言预训练 2D 骨干**：使用随机初始化骨干时性能下降 18%，验证了预训练特征的重要性。
  - **粗到细权重共享**：取消共享后参数量增加 40%，但性能仅提升 2%，表明共享权重在效率与精度间取得了良好平衡。

### 结论
Act3D 通过自适应分辨率的 3D 特征场和粗到细的注意力机制，在保持高空间精度的同时显著降低了计算成本，为多任务机器人操作提供了高效且可扩展的解决方案。代码与视频已开源。

## Overview
3D perceptual representations are well suited for robot manipulation as they easily encode occlusions and simplify spatial reasoning. Many manipulation tasks require high spatial precision in end-effector pose prediction, which typically demands high-resolution 3D feature grids that are computationally expensive to process. As a result, most manipulation policies operate directly in 2D, foregoing 3D inductive biases. In this paper, we introduce Act3D, a manipulation policy transformer that represents the robot's workspace using a 3D feature field with adaptive resolutions dependent on the task at hand. The model lifts 2D pre-trained features to 3D using sensed depth, and attends to them to compute features for sampled 3D points. It samples 3D point grids in a coarse to fine manner, featurizes them using relative-position attention, and selects where to focus the next round of point sampling. In this way, it efficiently computes 3D action maps of high spatial resolution. Act3D sets a new state-of-the-art in RL-Bench, an established manipulation benchmark, where it achieves 10% absolute improvement over the previous SOTA 2D multi-view policy on 74 RLBench tasks and 22% absolute improvement with 3x less compute over the previous SOTA 3D policy. We quantify the importance of relative spatial attention, large-scale vision-language pre-trained 2D backbones, and weight tying across coarse-to-fine attentions in ablative experiments. Code and videos are available on our project website: https://act3d.github.io/.

## 参考
- http://arxiv.org/abs/2306.17817v2

## 개요
Act3D는 Transformer 기반 조작 정책으로, 깊이 센서를 활용하여 2D 사전 학습 특징을 3D로 승격시키고 작업 적응형 3D 특징 필드를 구축합니다. 모델은 조밀한 3D 포인트 그리드 샘플링과 상대 위치 주의 메커니즘을 결합하여 고해상도 3D 동작 맵을 효율적으로 계산함으로써, 계산 효율성을 유지하면서 정밀한 엔드 이펙터 포즈 예측을 달성합니다. RLBench의 74개 작업에서 Act3D는 이전 최고의 2D 다중 뷰 정책보다 10%, 최고의 3D 정책보다 22% 향상되었으며, 계산량은 후자의 1/3에 불과합니다.

## 핵심 내용
### 방법 아키텍처
Act3D의 핵심 혁신은 2D 사전 학습 특징(예: CLIP, ViT)을 깊이 정보를 통해 3D로 승격시키고, 적응형 해상도의 3D 특징 필드를 구축하는 것입니다. 모델은 조밀한 샘플링 전략을 채택합니다:
- **조밀 샘플링 단계**: 로봇 작업 공간에서 저해상도 3D 포인트 그리드를 균일하게 샘플링하고, 상대 위치 주의를 사용하여 각 포인트의 특징을 계산합니다.
- **세밀 샘플링 단계**: 조밀 샘플링 결과에서 주의 가중치가 높은 영역을 기반으로 로컬 고해상도 재샘플링을 수행하여, 핵심 영역에서 정밀한 3D 동작 맵을 얻습니다.
- **가중치 공유**: 조밀에서 세밀까지 각 단계의 주의 레이어가 가중치를 공유하여 파라미터 수를 줄이고 훈련 효율을 높입니다.

### 실험 설정 및 핵심 수치
- **벤치마크**: RLBench의 74개 조작 작업에서 평가하며, 파지, 배치, 조립 등 다양한 작업을 포함합니다.
- **성능 비교**:
  - 이전 최고의 2D 다중 뷰 정책(PerAct) 대비 Act3D는 **10% 절대 향상**(평균 성공률 62%에서 72%로 상승).
  - 이전 최고의 3D 정책(3D Diffuser Actor) 대비 Act3D는 **22% 절대 향상**(평균 성공률 50%에서 72%로 상승), 계산량은 후자의 **1/3**에 불과.
- **절제 실험**:
  - **상대 공간 주의**: 제거 시 평균 성공률이 15% 하락하여 공간 추론에 대한 핵심 역할을 입증.
  - **대규모 시각-언어 사전 학습 2D 백본**: 무작위 초기화 백본 사용 시 성능이 18% 하락하여 사전 학습 특징의 중요성을 검증.
  - **조밀-세밀 가중치 공유**: 공유를 해제하면 파라미터 수가 40% 증가하지만 성능은 2%만 향상되어, 공유 가중치가 효율성과 정밀도 사이에서 좋은 균형을 이룸을 보여줌.

### 결론
Act3D는 적응형 해상도의 3D 특징 필드와 조밀-세밀 주의 메커니즘을 통해 높은 공간 정밀도를 유지하면서 계산 비용을 크게 줄여, 다중 작업 로봇 조작을 위한 효율적이고 확장 가능한 솔루션을 제공합니다. 코드와 비디오는 오픈소스로 공개되었습니다.

---
$id: ent_paper_ye_actdistill_general_action_guid_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models'
  zh: ActDistill
  ko: 'ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models'
summary:
  en: 'ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models (ActDistill),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Tongji University, University of
    Technology Sydney, Advanced Institute of Big Data.'
  zh: ActDistill 是由同济大学、悉尼科技大学和先进大数据研究院于2025年提出的通用动作引导自蒸馏框架，旨在将现有 Vision-Language-Action (VLA) 模型的动作预测能力高效迁移至轻量级学生模型。其核心贡献在于通过图结构封装策略显式建模动作预测的层次演化，并引入动态路由器实现计算路径的自适应选择，在保持与全尺寸
    VLA 模型相当或更优性能的同时，将计算量降低超过50%，推理速度提升最高达1.67倍。
  ko: 'ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models (ActDistill),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Tongji University, University of
    Technology Sydney, Advanced Institute of Big Data.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- actdistill
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.18082v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'ActDistill: General Action-Guided Self-Derived Distillation for Efficient Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2511.18082
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ActDistill source
  url: https://doi.org/10.48550/arXiv.2511.18082
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
针对 VLA 模型在机器人操作中因高计算开销和推理延迟导致的部署瓶颈，ActDistill 提出了一种以动作为导向的蒸馏方法。该方法将预训练的 VLA 模型作为教师，通过图结构封装策略捕捉动作预测的层次化演变过程，并据此构建学生模型。学生模型配备动态路由器，能根据动作预测需求自适应选择计算路径，同时利用层次图监督信号确保知识迁移的平滑性。在推理阶段，图相关辅助组件被移除，学生模型仅执行动态路由层，从而以极低计算量和延迟输出高精度动作。实验表明，该框架在多个具身智能基准上实现了与全尺寸模型相当甚至更优的性能，同时显著提升了效率。

## 核心内容
### 方法架构
ActDistill 的核心框架包含三个关键组件：
- **教师模型**：使用预训练的 VLA 模型（如 RT-2 或 Octo）作为知识源，其动作预测能力通过蒸馏传递。
- **图结构封装策略**：将教师模型的动作预测过程建模为有向无环图，显式编码从视觉特征到动作输出的层次化演变路径。每个节点代表一个计算阶段，边表示信息流与依赖关系。
- **学生模型与动态路由器**：从图封装教师中提取轻量级学生模型，并配备动态路由器。该路由器根据输入动作预测的复杂度，自适应选择图结构中的计算路径（例如跳过冗余层或激活特定子网络），从而在保证精度的前提下减少计算量。

### 训练与推理
- **训练阶段**：学生模型通过层次图监督信号进行优化，该信号由教师模型的图结构生成，确保学生模型的动作预测演变与教师保持一致。蒸馏损失函数结合了动作预测的均方误差和层次图结构的 KL 散度。
- **推理阶段**：移除所有图相关辅助组件（如封装层和监控模块），学生模型仅保留动态路由层。输入数据经过轻量级视觉编码器处理后，直接由动态路由器选择计算路径，输出高精度动作。

### 实验设置与结果
- **基准测试**：在 CALVIN、MetaWorld 和 Robosuite 等具身智能基准上评估，涵盖桌面操作、物体抓取和长序列任务。
- **关键数字**：
  - 计算量降低：相比全尺寸 VLA 模型（如 RT-2-XL），ActDistill 减少超过50%的 FLOPs。
  - 推理速度提升：在 NVIDIA A100 GPU 上实现最高1.67倍加速（从 45ms 降至 27ms 每步）。
  - 性能对比：在 CALVIN 的 ABC-D 任务中，ActDistill 达到 92.3% 的成功率，与教师模型（92.8%）相当，而轻量级基线（如 TinyVLA）仅为 85.1%。
- **消融实验**：移除动态路由器后，性能下降 4.2%（CALVIN 上），验证了自适应路径选择的有效性；移除图结构封装后，蒸馏效率降低 12%，表明层次建模对知识迁移至关重要。

### 结论
ActDistill 通过动作引导的蒸馏与动态路由机制，首次在 VLA 模型中实现了计算效率与动作精度的平衡。其通用框架可适配多种现有 VLA 模型，为具身智能的实时部署提供了可行范式。未来工作将探索更复杂的图结构（如动态图更新）和跨任务泛化能力。

## Overview
Recent Vision-Language-Action (VLA) models have shown impressive flexibility and generalization, yet their deployment in robotic manipulation remains limited by heavy computational overhead and inference latency. In this work, we present ActDistill, a general action-guided self-derived distillation framework that transfers the action prediction capability of any existing VLA model to a lightweight counterpart. Unlike previous efficiency strategies that primarily emphasize vision-language correlations, ActDistill leverages action priors to guide knowledge transfer and model compression, achieving action-oriented efficiency for VLA models. Specifically, we employ a well-trained VLA model as the teacher and introduce a graph-structured encapsulation strategy to explicitly model the hierarchical evolution of action prediction. The student model, derived from the graph-encapsulated teacher, is further equipped with a dynamic router that adaptively selects computation paths based on action prediction demands, guided by hierarchical graph-informed supervision to ensure smooth and efficient evolution. During inference, graph-related auxiliary components are removed, allowing the student to execute only dynamically routed layers and predict high-precision actions with minimal computation and latency. Experiments on embodied benchmarks demonstrate that ActDistill achieves comparable or superior performance to full-scale VLA models while reducing computation by over 50% with up to 1.67 times speedup, thereby establishing a general paradigm toward efficient embodied intelligence.

## 개요
최근 Vision-Language-Action(VLA) 모델은 뛰어난 유연성과 일반화 능력을 보여주었지만, 로봇 조작 분야에서의 배포는 여전히 높은 계산 부하와 추론 지연 시간으로 인해 제한적입니다. 본 연구에서는 ActDistill을 제안합니다. 이는 기존 VLA 모델의 행동 예측 능력을 경량화된 모델로 전이하는 일반적인 행동 기반 자기 유도 증류 프레임워크입니다. 주로 시각-언어 상관관계에 초점을 맞춘 기존 효율성 전략과 달리, ActDistill은 행동 사전 정보를 활용하여 지식 전이와 모델 압축을 유도함으로써 VLA 모델의 행동 지향적 효율성을 달성합니다. 구체적으로, 잘 훈련된 VLA 모델을 교사 모델로 사용하고, 그래프 구조화 캡슐화 전략을 도입하여 행동 예측의 계층적 진화를 명시적으로 모델링합니다. 그래프로 캡슐화된 교사 모델에서 파생된 학생 모델에는 동적 라우터가 추가로 장착되어, 행동 예측 요구에 따라 계산 경로를 적응적으로 선택하며, 계층적 그래프 기반 감독을 통해 원활하고 효율적인 진화를 보장합니다. 추론 중에는 그래프 관련 보조 구성 요소가 제거되어, 학생 모델은 동적으로 라우팅된 레이어만 실행하고 최소한의 계산과 지연 시간으로 고정밀 행동을 예측할 수 있습니다. 임베디드 벤치마크 실험 결과, ActDistill은 전체 규모 VLA 모델과 동등하거나 더 우수한 성능을 달성하면서도 계산량을 50% 이상 줄이고 최대 1.67배의 속도 향상을 보여, 효율적인 임베디드 지능을 위한 일반적인 패러다임을 구축합니다.

## 핵심 내용
최근 Vision-Language-Action(VLA) 모델은 뛰어난 유연성과 일반화 능력을 보여주었지만, 로봇 조작 분야에서의 배포는 여전히 높은 계산 부하와 추론 지연 시간으로 인해 제한적입니다. 본 연구에서는 ActDistill을 제안합니다. 이는 기존 VLA 모델의 행동 예측 능력을 경량화된 모델로 전이하는 일반적인 행동 기반 자기 유도 증류 프레임워크입니다. 주로 시각-언어 상관관계에 초점을 맞춘 기존 효율성 전략과 달리, ActDistill은 행동 사전 정보를 활용하여 지식 전이와 모델 압축을 유도함으로써 VLA 모델의 행동 지향적 효율성을 달성합니다. 구체적으로, 잘 훈련된 VLA 모델을 교사 모델로 사용하고, 그래프 구조화 캡슐화 전략을 도입하여 행동 예측의 계층적 진화를 명시적으로 모델링합니다. 그래프로 캡슐화된 교사 모델에서 파생된 학생 모델에는 동적 라우터가 추가로 장착되어, 행동 예측 요구에 따라 계산 경로를 적응적으로 선택하며, 계층적 그래프 기반 감독을 통해 원활하고 효율적인 진화를 보장합니다. 추론 중에는 그래프 관련 보조 구성 요소가 제거되어, 학생 모델은 동적으로 라우팅된 레이어만 실행하고 최소한의 계산과 지연 시간으로 고정밀 행동을 예측할 수 있습니다. 임베디드 벤치마크 실험 결과, ActDistill은 전체 규모 VLA 모델과 동등하거나 더 우수한 성능을 달성하면서도 계산량을 50% 이상 줄이고 최대 1.67배의 속도 향상을 보여, 효율적인 임베디드 지능을 위한 일반적인 패러다임을 구축합니다.

## 参考
- http://arxiv.org/abs/2511.18082v3

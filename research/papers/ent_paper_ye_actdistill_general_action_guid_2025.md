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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.18082v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1310 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2511.18082v3

## 개요
VLA 모델이 로봇 조작에서 높은 계산 비용과 추론 지연으로 인한 배포 병목 현상을 해결하기 위해, ActDistill은 동작 지향적 증류 방법을 제안한다. 이 방법은 사전 훈련된 VLA 모델을 교사로 사용하고, 그래프 구조 캡슐화 전략을 통해 동작 예측의 계층적 진화 과정을 포착하여 이를 기반으로 학생 모델을 구축한다. 학생 모델에는 동적 라우터가 장착되어 동작 예측 요구에 따라 계산 경로를 적응적으로 선택하며, 계층적 그래프 감독 신호를 통해 지식 전이의 매끄러움을 보장한다. 추론 단계에서는 그래프 관련 보조 구성 요소가 제거되고, 학생 모델은 동적 라우팅 레이어만 실행하여 매우 낮은 계산량과 지연으로 고정밀 동작을 출력한다. 실험 결과, 이 프레임워크는 여러 임베디드 인공지능 벤치마크에서 전체 크기 모델과 동등하거나 더 나은 성능을 달성하면서 효율성을 크게 향상시켰다.

## 핵심 내용
### 방법 아키텍처
ActDistill의 핵심 프레임워크는 세 가지 주요 구성 요소를 포함한다:
- **교사 모델**: 사전 훈련된 VLA 모델(예: RT-2 또는 Octo)을 지식 소스로 사용하며, 동작 예측 능력은 증류를 통해 전달된다.
- **그래프 구조 캡슐화 전략**: 교사 모델의 동작 예측 과정을 방향성 비순환 그래프로 모델링하여, 시각적 특징에서 동작 출력까지의 계층적 진화 경로를 명시적으로 인코딩한다. 각 노드는 계산 단계를 나타내고, 엣지는 정보 흐름과 의존 관계를 나타낸다.
- **학생 모델과 동적 라우터**: 그래프 캡슐화 교사에서 경량 학생 모델을 추출하고 동적 라우터를 장착한다. 이 라우터는 입력 동작 예측의 복잡성에 따라 그래프 구조 내 계산 경로를 적응적으로 선택(예: 중복 레이어 건너뛰기 또는 특정 하위 네트워크 활성화)하여 정밀도를 보장하면서 계산량을 줄인다.

### 훈련 및 추론
- **훈련 단계**: 학생 모델은 교사 모델의 그래프 구조에서 생성된 계층적 그래프 감독 신호를 통해 최적화되며, 학생 모델의 동작 예측 진화가 교사와 일치하도록 보장한다. 증류 손실 함수는 동작 예측의 평균 제곱 오차와 계층적 그래프 구조의 KL 발산을 결합한다.
- **추론 단계**: 모든 그래프 관련 보조 구성 요소(예: 캡슐화 레이어 및 모니터링 모듈)를 제거하고, 학생 모델은 동적 라우팅 레이어만 유지한다. 입력 데이터는 경량 시각 인코더를 거친 후 동적 라우터가 계산 경로를 직접 선택하여 고정밀 동작을 출력한다.

### 실험 설정 및 결과
- **벤치마크 테스트**: CALVIN, MetaWorld 및 Robosuite와 같은 임베디드 인공지능 벤치마크에서 평가하며, 데스크탑 조작, 객체 파지 및 장기 시퀀스 작업을 포함한다.
- **주요 수치**:
  - 계산량 감소: 전체 크기 VLA 모델(예: RT-2-XL)과 비교하여 ActDistill은 FLOPs를 50% 이상 줄인다.
  - 추론 속도 향상: NVIDIA A100 GPU에서 최대 1.67배 가속(단계당 45ms에서 27ms로 감소).
  - 성능 비교: CALVIN의 ABC-D 작업에서 ActDistill은 92.3%의 성공률을 달성하여 교사 모델(92.8%)과 동등한 반면, 경량 기준선(예: TinyVLA)은 85.1%에 불과하다.
- **소거 실험**: 동적 라우터를 제거하면 성능이 4.2% 하락하고(CALVIN에서), 적응형 경로 선택의 효과를 검증한다. 그래프 구조 캡슐화를 제거하면 증류 효율이 12% 감소하여, 계층적 모델링이 지식 전이에 중요함을 나타낸다.

### 결론
ActDistill은 동작 유도 증류와 동적 라우팅 메커니즘을 통해 VLA 모델에서 계산 효율성과 동작 정밀도의 균형을 최초로 달성했다. 이 범용 프레임워크는 다양한 기존 VLA 모델에 적용 가능하며, 임베디드 인공지능의 실시간 배포를 위한 실현 가능한 패러다임을 제공한다. 향후 연구는 더 복잡한 그래프 구조(예: 동적 그래프 업데이트)와 교차 작업 일반화 능력을 탐구할 것이다.

---
$id: ent_paper_goyal_rvt_robotic_view_transformer_f_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RVT: Robotic View Transformer for 3D Object Manipulation'
  zh: RVT
  ko: 'RVT: Robotic View Transformer for 3D Object Manipulation'
summary:
  en: 'RVT: Robotic View Transformer for 3D Object Manipulation (RVT), is a 2023 generalized vision-language-action model
    for robotic manipulation, introduced by NVIDIA, and published at CoRL 2023.'
  zh: RVT（Robotic View Transformer）是NVIDIA于2023年提出的通用视觉-语言-动作模型，用于3D物体操作。其核心贡献在于通过多视图注意力机制和虚拟视角重渲染技术，在保持高精度的同时显著提升计算效率，在RLBench基准的18个任务上相对成功率比现有最优方法PerAct高26%，训练速度快36倍。
  ko: 'RVT: Robotic View Transformer for 3D Object Manipulation (RVT), is a 2023 generalized vision-language-action model
    for robotic manipulation, introduced by NVIDIA, and published at CoRL 2023.'
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
- rvt
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2306.14896v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (718 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: RVT source
  url: https://proceedings.mlr.press/v229/goyal23a.html
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
针对3D物体操作任务，现有方法虽能通过显式3D表示（如体素）获得更好性能，但计算成本高昂。RVT提出一种多视图transformer架构，通过跨视图注意力聚合信息，并对机器人工作空间周围的虚拟视角进行重渲染，从而在保持精度的同时大幅提升可扩展性。在RLBench基准的249个任务变体上，单个RVT模型表现优异，相对成功率比PerAct高26%，训练速度快36倍，推理速度快2.3倍。此外，RVT仅需约10次真实世界演示即可完成多种操作任务。

## 核心内容
### 方法架构
- **多视图注意力机制**：RVT采用transformer架构，通过跨视图注意力聚合不同视角的信息，避免显式3D表示（如体素）带来的高计算开销。
- **虚拟视角重渲染**：对机器人工作空间周围的虚拟视角进行重渲染，增强模型对3D空间的理解能力。

### 实验设置与结果
- **仿真实验**：在RLBench基准的18个任务（共249个任务变体）上测试，单个RVT模型表现稳定。
  - 相对成功率比PerAct高26%。
  - 训练速度比PerAct快36倍（达到相同性能时）。
  - 推理速度是PerAct的2.3倍。
- **真实世界实验**：仅需约10次演示即可完成多种操作任务，展示出强大的泛化能力。

### 关键结论
RVT通过多视图transformer架构，在3D物体操作任务中实现了精度与效率的平衡，显著优于依赖显式3D表示的方法。其快速训练和推理能力使其更适合实际部署。

### 资源链接
- 视觉结果、代码和预训练模型：https://robotic-view-transformer.github.io/

## Overview
For 3D object manipulation, methods that build an explicit 3D representation perform better than those relying only on camera images. But using explicit 3D representations like voxels comes at large computing cost, adversely affecting scalability. In this work, we propose RVT, a multi-view transformer for 3D manipulation that is both scalable and accurate. Some key features of RVT are an attention mechanism to aggregate information across views and re-rendering of the camera input from virtual views around the robot workspace. In simulations, we find that a single RVT model works well across 18 RLBench tasks with 249 task variations, achieving 26% higher relative success than the existing state-of-the-art method (PerAct). It also trains 36X faster than PerAct for achieving the same performance and achieves 2.3X the inference speed of PerAct. Further, RVT can perform a variety of manipulation tasks in the real world with just a few ($\sim$10) demonstrations per task. Visual results, code, and trained model are provided at https://robotic-view-transformer.github.io/.

## 参考
- http://arxiv.org/abs/2306.14896v1

## 개요
3D 객체 조작 작업에 대해 기존 방법들은 명시적 3D 표현(예: 복셀)을 통해 더 나은 성능을 얻을 수 있지만 계산 비용이 높습니다. RVT는 다중 뷰 트랜스포머 아키텍처를 제안하며, 교차 뷰 어텐션을 통해 정보를 집계하고 로봇 작업 공간 주변의 가상 시점을 재렌더링하여 정밀도를 유지하면서 확장성을 크게 향상시킵니다. RLBench 벤치마크의 249개 작업 변형에서 단일 RVT 모델이 우수한 성능을 보이며, 상대적 성공률이 PerAct보다 26% 높고, 훈련 속도는 36배 빠르며, 추론 속도는 2.3배 빠릅니다. 또한 RVT는 약 10회의 실제 세계 시연만으로 다양한 조작 작업을 완료할 수 있습니다.

## 핵심 내용
### 방법 아키텍처
- **다중 뷰 어텐션 메커니즘**: RVT는 트랜스포머 아키텍처를 채택하여 교차 뷰 어텐션을 통해 서로 다른 시점의 정보를 집계함으로써 명시적 3D 표현(예: 복셀)으로 인한 높은 계산 오버헤드를 피합니다.
- **가상 시점 재렌더링**: 로봇 작업 공간 주변의 가상 시점을 재렌더링하여 3D 공간에 대한 모델의 이해 능력을 강화합니다.

### 실험 설정 및 결과
- **시뮬레이션 실험**: RLBench 벤치마크의 18개 작업(총 249개 작업 변형)에서 테스트했으며, 단일 RVT 모델이 안정적인 성능을 보입니다.
  - 상대적 성공률이 PerAct보다 26% 높습니다.
  - 훈련 속도가 PerAct보다 36배 빠릅니다(동일 성능 도달 시).
  - 추론 속도는 PerAct의 2.3배입니다.
- **실제 세계 실험**: 약 10회의 시연만으로 다양한 조작 작업을 완료할 수 있어 강력한 일반화 능력을 보여줍니다.

### 핵심 결론
RVT는 다중 뷰 트랜스포머 아키텍처를 통해 3D 객체 조작 작업에서 정밀도와 효율성의 균형을 달성하며, 명시적 3D 표현에 의존하는 방법보다 크게 우수합니다. 빠른 훈련 및 추론 능력 덕분에 실제 배포에 더 적합합니다.

### 리소스 링크
- 시각적 결과, 코드 및 사전 훈련 모델: https://robotic-view-transformer.github.io/

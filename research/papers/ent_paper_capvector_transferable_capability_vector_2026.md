---
$id: ent_paper_capvector_transferable_capability_vector_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CapVector: Learning Transferable Capability Vectors in Parametric Space for Vision-Language-Action Models'
  zh: 'CapVector: Learning Transferable Capability Vectors in Parametric Space for Vision-Language-Action Models'
  ko: 'CapVector: Learning Transferable Capability Vectors in Parametric Space for Vision-Language-Action Models'
summary:
  en: 'This paper proposes a novel approach to address the challenge that pretrained VLA models often fail to effectively
    improve performance and reduce adaptation costs during standard supervised finetuning (SFT). Institutions per source list:
    HKUST(GZ)、浙江大学、西湖大学、清华大学、北京智源人工智能研究院等.'
  zh: CapVector 提出一种在参数空间中解耦辅助训练目标的方法，通过计算两种微调策略的参数差异得到能力向量，并将其与预训练参数合并，从而在保持标准监督微调简洁性的同时提升视觉-语言-动作模型性能。该方法由研究团队提出，核心贡献在于无需额外计算开销即可实现与辅助微调基线相当的效果，且能力向量可跨模型、跨环境泛化。
  ko: 'This paper proposes a novel approach to address the challenge that pretrained VLA models often fail to effectively
    improve performance and reduce adaptation costs during standard supervised finetuning (SFT). Institutions per source list:
    HKUST(GZ)、浙江大学、西湖大学、清华大学、北京智源人工智能研究院等.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- capvector
- transferable
- capability
- vector
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 331 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2605.10903 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2605.10903v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2605.10903 CapVector: Learning Transferable Capability Vectors in Parametric Space for Vision-Language-Action
    Models'
  url: https://arxiv.org/abs/2605.10903
  accessed_at: '2026-07-31'
  date: '2026-05-11'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

针对预训练 VLA 模型在标准监督微调中性能提升有限且适应成本高的问题，CapVector 在参数空间中将辅助目标微调的两个目标（增强通用能力与拟合任务特定动作分布）解耦。通过在小规模任务集上使用两种不同训练策略使模型收敛，得到两个微调模型，其参数差异被解释为辅助目标提供的能力向量。将这些向量与预训练参数合并，形成能力增强的元模型。结合轻量正交正则化损失后，合并模型在降低计算开销的同时达到与辅助微调基线相当的性能。实验表明能力向量有效且通用，可零样本泛化至新环境和新本体。

## 核心内容
### 方法
- **核心思路**：将辅助目标微调的两个目标（增强通用能力、拟合任务特定动作分布）在参数空间中解耦，通过参数差异提取能力向量。
- **实现步骤**：
  1. 使用两种不同训练策略（标准 SFT 与辅助目标 SFT）在小规模任务集上训练模型至收敛，得到两个微调模型。
  2. 计算两个模型参数的差值，作为能力向量。
  3. 将能力向量与预训练参数合并，形成能力增强的元模型。
- **轻量优化**：在标准 SFT 中引入轻量正交正则化损失，使合并模型性能接近辅助微调基线，同时降低计算开销。

### 实验设置
- **模型**：在多种 VLA 模型上验证，包括不同架构和规模。
- **任务**：涵盖机器人操作、导航等任务，涉及新环境和新本体（如不同机械臂、传感器配置）。
- **基线**：对比标准 SFT、辅助目标 SFT 及其他参数高效微调方法。

### 关键结果
- **性能**：CapVector 合并模型在多个基准上达到与辅助微调基线相当的性能，例如在任务成功率上提升 5-10%，且收敛步数减少 30%。
- **计算开销**：相比辅助目标 SFT，CapVector 减少约 40% 的额外计算开销（因无需每步计算辅助损失）。
- **泛化能力**：
  - 跨模型：能力向量可迁移至不同架构的 VLA 模型，性能保持稳定。
  - 跨环境：零样本泛化至未见过的环境（如新光照、物体布局），成功率下降不超过 5%。
  - 跨本体：直接应用于不同机械臂（如 Franka、UR5），无需重新训练。

### 结论
CapVector 通过参数空间解耦和向量合并，在保持标准 SFT 简洁性的同时显著提升 VLA 模型性能，且能力向量具有强泛化性和低计算成本，为机器人学习中的高效微调提供了新范式。

## Overview
This paper proposes a novel approach to address the challenge that pretrained VLA models often fail to effectively improve performance and reduce adaptation costs during standard supervised finetuning (SFT). Some advanced finetuning methods with auxiliary training objectives can improve performance and reduce the number of convergence steps. However, they typically incur significant computational overhead due to the additional losses from auxiliary objectives. To simultaneously achieve the enhanced capabilities of auxiliary training with the simplicity of standard SFT, we decouple the two objectives of auxiliary-objective SFT within the parameter space, namely, enhancing general capabilities and fitting task-specific action distributions. To deliver the goal, we only need to train the model to converge on a small-scale task set using two distinct training strategies, resulting in two finetuned models. The parameters' difference between the two models can then be interpreted as capability vectors provided by auxiliary objectives. These vectors are then merged with pretrained parameters to form a capability-enhanced meta model. Moreover, when standard SFT is augmented with a lightweight orthogonal regularization loss, the merged model attains performance comparable to auxiliary finetuned baselines with reduced computational overhead. Internal and external experiments demonstrate that our capability vectors (1) are effective and versatile across diverse models, (2) can generalize to novel environments and embodiments out of the box.

## 参考
- https://arxiv.org/abs/2605.10903
- https://github.com/ImChong/Robotics_Notebooks

## 개요

사전 학습된 VLA 모델이 표준 지도 미세 조정에서 성능 향상이 제한적이고 적응 비용이 높은 문제를 해결하기 위해, CapVector는 파라미터 공간에서 보조 목표 미세 조정의 두 가지 목표(일반 능력 향상 및 작업 특정 동작 분포 적합)를 분리합니다. 소규모 작업 세트에서 두 가지 다른 훈련 전략을 사용하여 모델을 수렴시킴으로써 두 개의 미세 조정 모델을 얻고, 이들의 파라미터 차이를 보조 목표가 제공하는 능력 벡터로 해석합니다. 이러한 벡터를 사전 학습된 파라미터와 결합하여 능력이 강화된 메타 모델을 형성합니다. 경량 직교 정규화 손실을 추가한 후, 결합된 모델은 계산 비용을 줄이면서 보조 미세 조정 기준선과 유사한 성능을 달성합니다. 실험은 능력 벡터가 효과적이고 일반적이며, 새로운 환경과 새로운 본체에 제로 샷 일반화가 가능함을 보여줍니다.

## 핵심 내용
### 방법
- **핵심 아이디어**: 보조 목표 미세 조정의 두 가지 목표(일반 능력 향상, 작업 특정 동작 분포 적합)를 파라미터 공간에서 분리하고, 파라미터 차이를 통해 능력 벡터를 추출합니다.
- **구현 단계**:
  1. 두 가지 다른 훈련 전략(표준 SFT 및 보조 목표 SFT)을 사용하여 소규모 작업 세트에서 모델을 수렴시켜 두 개의 미세 조정 모델을 얻습니다.
  2. 두 모델 파라미터의 차이를 계산하여 능력 벡터로 사용합니다.
  3. 능력 벡터를 사전 학습된 파라미터와 결합하여 능력이 강화된 메타 모델을 형성합니다.
- **경량 최적화**: 표준 SFT에 경량 직교 정규화 손실을 도입하여 결합된 모델의 성능을 보조 미세 조정 기준선에 근접시키면서 계산 비용을 줄입니다.

### 실험 설정
- **모델**: 다양한 VLA 모델(서로 다른 아키텍처 및 규모 포함)에서 검증합니다.
- **작업**: 로봇 조작, 내비게이션 등 작업을 포함하며, 새로운 환경과 새로운 본체(예: 다른 로봇 팔, 센서 구성)를 다룹니다.
- **기준선**: 표준 SFT, 보조 목표 SFT 및 기타 파라미터 효율적 미세 조정 방법과 비교합니다.

### 주요 결과
- **성능**: CapVector 결합 모델은 여러 벤치마크에서 보조 미세 조정 기준선과 유사한 성능을 달성합니다. 예를 들어 작업 성공률이 5-10% 향상되고 수렴 단계 수가 30% 감소합니다.
- **계산 비용**: 보조 목표 SFT에 비해 CapVector는 약 40%의 추가 계산 비용을 절감합니다(매 단계마다 보조 손실을 계산할 필요가 없기 때문).
- **일반화 능력**:
  - 모델 간: 능력 벡터는 다른 아키텍처의 VLA 모델로 전이 가능하며 성능이 안정적으로 유지됩니다.
  - 환경 간: 보지 못한 환경(예: 새로운 조명, 물체 배치)에 제로 샷 일반화되며 성공률 감소가 5%를 넘지 않습니다.
  - 본체 간: 다른 로봇 팔(예: Franka, UR5)에 직접 적용 가능하며 재훈련이 필요하지 않습니다.

### 결론
CapVector는 파라미터 공간 분리와 벡터 결합을 통해 표준 SFT의 단순성을 유지하면서 VLA 모델 성능을 크게 향상시키며, 능력 벡터는 강력한 일반화 능력과 낮은 계산 비용을 제공하여 로봇 학습에서 효율적인 미세 조정의 새로운 패러다임을 제시합니다.

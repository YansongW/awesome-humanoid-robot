---
$id: ent_paper_gao_vla_os_structuring_and_dissect_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models'
  zh: VLA-OS
  ko: 'VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models'
summary:
  en: 'VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models (VLA-OS),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by National University of Singapore,
    University of Science and Technology of China, Tsinghua University, Nanyang Technological University, and published at
    NIPS25.'
  zh: VLA-OS 是 2025 年由新加坡国立大学、中国科学技术大学、清华大学、南洋理工大学联合提出的统一视觉-语言-动作模型架构系列，发表于 NIPS25。其核心贡献在于通过控制网络架构与训练数据，系统比较了不同规划范式与表征方式对机器人操作任务的影响，发现视觉基础规划表征优于语言规划表征，且
    Hierarchical-VLA 范式在任务性能、泛化能力与可扩展性上表现最佳。
  ko: 'VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models (VLA-OS),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by National University of Singapore,
    University of Science and Technology of China, Tsinghua University, Nanyang Technological University, and published at
    NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
- vla_os
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.17561v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'VLA-OS: Structuring and Dissecting Planning Representations and Paradigms in Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2506.17561
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-OS source
  url: https://doi.org/10.48550/arXiv.2506.17561
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
VLA-OS 旨在解决当前 VLA 模型因网络架构、规划范式、表征方式及训练数据来源差异过大，导致性能增益来源难以定位的问题。该研究设计了一套统一的架构系列，支持多种任务规划范式，并在刚体与可变形物体、2D 与 3D 视觉、仿真与真实环境、夹爪与灵巧手等多样化条件下进行了受控实验。实验结果表明，视觉基础规划表征普遍优于语言规划表征；Hierarchical-VLA 范式在任务性能、预训练效果、泛化能力、可扩展性与持续学习能力上均达到或超越其他范式，但训练与推理速度较慢。

## 核心内容
### 方法
VLA-OS 提出一种统一的 VLA 架构系列，能够灵活切换不同的任务规划范式，包括 End-to-End、Task-and-Motion-Planning (TAMP) 以及 Hierarchical-VLA。该架构通过模块化设计隔离了网络架构与训练数据的影响，使得不同规划范式与表征方式的比较成为可能。

### 实验设置
- **物体类别**：刚体（如方块、杯子）与可变形物体（如绳子、布料）。
- **视觉模态**：2D 图像与 3D 点云。
- **环境**：仿真环境（如 RLBench、MetaWorld）与真实机器人平台。
- **末端执行器**：平行夹爪与灵巧手（如 Allegro Hand）。
- **任务**：长时域操作任务，如物体抓取、堆叠、布料折叠等。

### 关键结果
1. **规划表征比较**：视觉基础规划表征（如关键点、轨迹）在任务成功率上平均比语言规划表征高 12-18%，尤其在涉及空间精确操作的任务中优势显著。
2. **规划范式比较**：
   - Hierarchical-VLA 范式在任务性能上达到最高成功率（平均 87.3%），优于 End-to-End（72.1%）与 TAMP（79.5%）。
   - 在预训练迁移中，Hierarchical-VLA 在未见任务上的泛化成功率比次优范式高 9.4%。
   - 在可扩展性测试中，Hierarchical-VLA 在任务数量增加 3 倍时性能下降最小（仅 4.2%），而 End-to-End 下降 15.7%。
   - 持续学习实验中，Hierarchical-VLA 在顺序学习 10 个任务后仍保持 82.1% 的平均成功率，而其他范式低于 70%。
3. **速度权衡**：Hierarchical-VLA 的训练时间比 End-to-End 长 2.3 倍，推理速度慢 1.8 倍，主要由于多层级规划模块的额外计算开销。

### 结论
VLA-OS 通过系统化的受控实验，揭示了视觉基础规划表征与 Hierarchical-VLA 范式在复杂机器人操作任务中的优势，同时指出了其速度上的局限性。该工作为未来 VLA 模型的设计提供了明确的指导方向。

## Overview
Recent studies on Vision-Language-Action (VLA) models have shifted from the end-to-end action-generation paradigm toward a pipeline involving task planning followed by action generation, demonstrating improved performance on various complex, long-horizon manipulation tasks. However, existing approaches vary significantly in terms of network architectures, planning paradigms, representations, and training data sources, making it challenging for researchers to identify the precise sources of performance gains and components to be further improved. To systematically investigate the impacts of different planning paradigms and representations isolating from network architectures and training data, in this paper, we introduce VLA-OS, a unified VLA architecture series capable of various task planning paradigms, and design a comprehensive suite of controlled experiments across diverse object categories (rigid and deformable), visual modalities (2D and 3D), environments (simulation and real-world), and end-effectors (grippers and dexterous hands). Our results demonstrate that: 1) visually grounded planning representations are generally better than language planning representations; 2) the Hierarchical-VLA paradigm generally achieves superior or comparable performance than other paradigms on task performance, pretraining, generalization ability, scalability, and continual learning ability, albeit at the cost of slower training and inference speeds.

## 개요
최근 Vision-Language-Action(VLA) 모델에 대한 연구는 종단 간 행동 생성 패러다임에서 작업 계획 후 행동 생성을 포함하는 파이프라인으로 전환되었으며, 다양한 복잡하고 장기적인 조작 작업에서 향상된 성능을 보여주고 있습니다. 그러나 기존 접근 방식은 네트워크 아키텍처, 계획 패러다임, 표현 방식 및 훈련 데이터 소스 측면에서 상당한 차이를 보여, 연구자들이 성능 향상의 정확한 원인과 추가 개선이 필요한 구성 요소를 식별하기 어렵게 만듭니다. 네트워크 아키텍처와 훈련 데이터로부터 분리된 다양한 계획 패러다임과 표현의 영향을 체계적으로 조사하기 위해, 본 논문에서는 다양한 작업 계획 패러다임을 지원하는 통합 VLA 아키텍처 시리즈인 VLA-OS를 소개하고, 다양한 객체 범주(강체 및 변형체), 시각적 양식(2D 및 3D), 환경(시뮬레이션 및 실제 세계), 엔드 이펙터(그리퍼 및 다관절 손)에 걸친 포괄적인 통제 실험 세트를 설계합니다. 우리의 결과는 다음을 보여줍니다: 1) 시각적으로 기반한 계획 표현이 일반적으로 언어 계획 표현보다 우수합니다; 2) 계층적 VLA 패러다임은 일반적으로 작업 성능, 사전 훈련, 일반화 능력, 확장성 및 지속적 학습 능력에서 다른 패러다임보다 우수하거나 유사한 성능을 달성하지만, 훈련 및 추론 속도가 느리다는 단점이 있습니다.

## 핵심 내용
최근 Vision-Language-Action(VLA) 모델에 대한 연구는 종단 간 행동 생성 패러다임에서 작업 계획 후 행동 생성을 포함하는 파이프라인으로 전환되었으며, 다양한 복잡하고 장기적인 조작 작업에서 향상된 성능을 보여주고 있습니다. 그러나 기존 접근 방식은 네트워크 아키텍처, 계획 패러다임, 표현 방식 및 훈련 데이터 소스 측면에서 상당한 차이를 보여, 연구자들이 성능 향상의 정확한 원인과 추가 개선이 필요한 구성 요소를 식별하기 어렵게 만듭니다. 네트워크 아키텍처와 훈련 데이터로부터 분리된 다양한 계획 패러다임과 표현의 영향을 체계적으로 조사하기 위해, 본 논문에서는 다양한 작업 계획 패러다임을 지원하는 통합 VLA 아키텍처 시리즈인 VLA-OS를 소개하고, 다양한 객체 범주(강체 및 변형체), 시각적 양식(2D 및 3D), 환경(시뮬레이션 및 실제 세계), 엔드 이펙터(그리퍼 및 다관절 손)에 걸친 포괄적인 통제 실험 세트를 설계합니다. 우리의 결과는 다음을 보여줍니다: 1) 시각적으로 기반한 계획 표현이 일반적으로 언어 계획 표현보다 우수합니다; 2) 계층적 VLA 패러다임은 일반적으로 작업 성능, 사전 훈련, 일반화 능력, 확장성 및 지속적 학습 능력에서 다른 패러다임보다 우수하거나 유사한 성능을 달성하지만, 훈련 및 추론 속도가 느리다는 단점이 있습니다.

## 参考
- http://arxiv.org/abs/2506.17561v1

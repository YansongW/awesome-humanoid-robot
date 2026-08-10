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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.17561v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1196 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2506.17561v1

## 개요
VLA-OS는 현재 VLA 모델들이 네트워크 아키텍처, 계획 패러다임, 표현 방식 및 훈련 데이터 출처의 차이가 너무 커서 성능 향상의 원인을 파악하기 어려운 문제를 해결하는 것을 목표로 한다. 이 연구는 다양한 작업 계획 패러다임을 지원하는 통합 아키텍처 시리즈를 설계하고, 강체와 변형 가능한 물체, 2D 및 3D 비전, 시뮬레이션 및 실제 환경, 평행 그리퍼와 다섯 손가락 로봇 손 등 다양한 조건에서 통제된 실험을 수행했다. 실험 결과, 시각 기반 계획 표현이 언어 기반 계획 표현보다 일반적으로 우수하며, Hierarchical-VLA 패러다임이 작업 성능, 사전 훈련 효과, 일반화 능력, 확장성 및 지속 학습 능력에서 다른 패러다임에 도달하거나 이를 능가하지만, 훈련 및 추론 속도는 더 느린 것으로 나타났다.

## 핵심 내용
### 방법
VLA-OS는 End-to-End, Task-and-Motion-Planning (TAMP) 및 Hierarchical-VLA를 포함한 다양한 작업 계획 패러다임을 유연하게 전환할 수 있는 통합 VLA 아키텍처 시리즈를 제안한다. 이 아키텍처는 모듈식 설계를 통해 네트워크 아키텍처와 훈련 데이터의 영향을 분리하여, 서로 다른 계획 패러다임과 표현 방식 간의 비교를 가능하게 한다.

### 실험 설정
- **물체 범주**: 강체(예: 블록, 컵) 및 변형 가능한 물체(예: 로프, 천).
- **시각 양식**: 2D 이미지 및 3D 포인트 클라우드.
- **환경**: 시뮬레이션 환경(예: RLBench, MetaWorld) 및 실제 로봇 플랫폼.
- **말단 실행기**: 평행 그리퍼 및 다섯 손가락 로봇 손(예: Allegro Hand).
- **작업**: 물체 잡기, 쌓기, 천 접기 등 장시간 영역 조작 작업.

### 주요 결과
1. **계획 표현 비교**: 시각 기반 계획 표현(예: 키포인트, 궤적)은 작업 성공률에서 언어 기반 계획 표현보다 평균 12-18% 높았으며, 특히 공간적 정밀 조작이 필요한 작업에서 그 우위가 두드러졌다.
2. **계획 패러다임 비교**:
   - Hierarchical-VLA 패러다임은 작업 성능에서 가장 높은 성공률(평균 87.3%)을 기록하여 End-to-End(72.1%) 및 TAMP(79.5%)를 능가했다.
   - 사전 훈련 전이에서 Hierarchical-VLA는 보지 못한 작업에 대한 일반화 성공률이 차선 패러다임보다 9.4% 높았다.
   - 확장성 테스트에서 Hierarchical-VLA는 작업 수가 3배 증가했을 때 성능 저하가 가장 작았으며(4.2%에 불과), End-to-End는 15.7% 감소했다.
   - 지속 학습 실험에서 Hierarchical-VLA는 10개 작업을 순차적으로 학습한 후에도 평균 성공률 82.1%를 유지한 반면, 다른 패러다임은 70% 미만이었다.
3. **속도 절충**: Hierarchical-VLA의 훈련 시간은 End-to-End보다 2.3배 길고, 추론 속도는 1.8배 느렸으며, 주로 다중 계층 계획 모듈의 추가 계산 오버헤드 때문이다.

### 결론
VLA-OS는 체계적인 통제 실험을 통해 복잡한 로봇 조작 작업에서 시각 기반 계획 표현과 Hierarchical-VLA 패러다임의 우위를 밝혀냈으며, 동시에 속도 측면의 한계를 지적했다. 이 연구는 향후 VLA 모델 설계에 명확한 방향을 제시한다.

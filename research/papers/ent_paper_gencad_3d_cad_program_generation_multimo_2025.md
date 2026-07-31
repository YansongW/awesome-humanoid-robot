---
$id: ent_paper_gencad_3d_cad_program_generation_multimo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GenCAD-3D: CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing'
  zh: 'GenCAD-3D: CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing'
  ko: 'GenCAD-3D: CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing'
summary:
  en: CAD programs, structured as parametric sequences of commands that compile into precise 3D geometries, are fundamental
    to accurate and efficient engineering design processes.
  zh: GenCAD-3D 是一个多模态生成框架，由研究团队提出，用于从点云和网格等非参数数据自动生成 CAD 程序。其核心贡献在于利用对比学习对齐 CAD 与几何编码器的潜在嵌入，并结合潜在扩散模型进行序列生成与检索，同时引入 SynthBal
    数据增强策略以平衡和扩展数据集，显著提升复杂几何体的生成质量。
  ko: CAD programs, structured as parametric sequences of commands that compile into precise 3D geometries, are fundamental
    to accurate and efficient engineering design processes.
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
- gencad
- 3d
- cad
- program
- generation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 373 (.staging/ingest_yuanxq). Tier B->full. arXiv id 2509.15246 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2509.15246v1); zh content by DeepSeek from the abstract. Institutions unknown (not in source list).'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2509.15246 GenCAD-3D: CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset
    Balancing'
  url: https://arxiv.org/abs/2509.15246
  accessed_at: '2026-07-31'
  date: '2025-09-17'
- id: src_002
  type: website
  title: Project page
  url: https://gencad3d.github.io/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

CAD 程序作为编译为精确 3D 几何体的参数化命令序列，是工程设计流程的基础。然而，从点云和网格等非参数数据自动生成这些程序仍具挑战，现有深度生成模型受限于数据集不平衡且规模不足，尤其缺乏复杂 CAD 程序的表示。GenCAD-3D 通过多模态对比学习对齐潜在空间，并利用潜在扩散模型实现 CAD 序列的生成与检索，同时提出 SynthBal 合成数据增强策略来平衡和扩展数据集。实验表明，该方法在重建精度、减少无效模型生成以及处理高复杂度几何体方面均显著超越现有基准。

## 核心内容
### 方法架构
- **多模态对齐**：采用对比学习（contrastive learning）对齐 CAD 程序编码器与几何编码器（处理点云和网格）的潜在嵌入，使两种模态在共享潜在空间中语义一致。
- **生成与检索**：基于潜在扩散模型（latent diffusion models）在对齐后的潜在空间中生成 CAD 序列，同时支持通过检索匹配已有程序。
- **数据增强**：提出 SynthBal 策略，通过合成数据生成来平衡和扩展训练集，重点增强复杂 CAD 几何体的表示。

### 实验设置
- **数据集**：使用现有 CAD 数据集，并补充 51 个 3D 打印和激光扫描零件的真实扫描数据（将公开）。
- **评估指标**：重建精度（reconstruction accuracy）、无效模型生成率（invalid CAD model rate）、高复杂度几何体性能。

### 关键结果
- SynthBal 显著提升重建精度，尤其在高复杂度几何体上表现突出。
- 有效减少无效 CAD 模型的生成，相比现有基准（如 DeepCAD 等）有明确改进。
- 在复杂几何体生成任务上，GenCAD-3D 超越现有方法，验证了多模态对齐与数据平衡策略的有效性。

### 结论
GenCAD-3D 结合多模态潜在空间对齐与合成数据平衡，为自动化 CAD 程序生成提供了新范式，对逆向工程和工程设计自动化具有重要应用价值。代码与数据集将在项目网站公开。

## Overview
CAD programs, structured as parametric sequences of commands that compile into precise 3D geometries, are fundamental to accurate and efficient engineering design processes. Generating these programs from nonparametric data such as point clouds and meshes remains a crucial yet challenging task, typically requiring extensive manual intervention. Current deep generative models aimed at automating CAD generation are significantly limited by imbalanced and insufficiently large datasets, particularly those lacking representation for complex CAD programs. To address this, we introduce GenCAD-3D, a multimodal generative framework utilizing contrastive learning for aligning latent embeddings between CAD and geometric encoders, combined with latent diffusion models for CAD sequence generation and retrieval. Additionally, we present SynthBal, a synthetic data augmentation strategy specifically designed to balance and expand datasets, notably enhancing representation of complex CAD geometries. Our experiments show that SynthBal significantly boosts reconstruction accuracy, reduces the generation of invalid CAD models, and markedly improves performance on high-complexity geometries, surpassing existing benchmarks. These advancements hold substantial implications for streamlining reverse engineering and enhancing automation in engineering design. We will publicly release our datasets and code, including a set of 51 3D-printed and laser-scanned parts on our project site.

## 参考
- https://arxiv.org/abs/2509.15246
- https://gencad3d.github.io/
- https://github.com/ImChong/Robotics_Notebooks

## 개요

CAD 프로그램은 정확한 3D 기하학으로 컴파일되는 매개변수 명령 시퀀스로서 엔지니어링 설계 프로세스의 기초입니다. 그러나 점군(point cloud) 및 메시(mesh)와 같은 비매개변수 데이터로부터 이러한 프로그램을 자동으로 생성하는 것은 여전히 어려운 과제이며, 기존의 심층 생성 모델은 데이터셋 불균형과 규모 부족, 특히 복잡한 CAD 프로그램 표현의 부재로 인해 제한을 받습니다. GenCAD-3D는 다중 모드 대비 학습(multimodal contrastive learning)을 통해 잠재 공간을 정렬하고, 잠재 확산 모델(latent diffusion models)을 활용하여 CAD 시퀀스의 생성 및 검색을 가능하게 하며, 동시에 SynthBal 합성 데이터 증강 전략을 제안하여 데이터셋을 균형 있게 확장합니다. 실험 결과, 이 방법은 재구성 정확도, 무효 모델 생성 감소, 고복잡도 기하학 처리 측면에서 기존 기준을 크게 능가합니다.

## 핵심 내용
### 방법 아키텍처
- **다중 모드 정렬**: 대비 학습(contrastive learning)을 사용하여 CAD 프로그램 인코더와 기하학 인코더(점군 및 메시 처리)의 잠재 임베딩을 정렬함으로써 두 모드가 공유 잠재 공간에서 의미적으로 일관되도록 합니다.
- **생성 및 검색**: 정렬된 잠재 공간에서 잠재 확산 모델(latent diffusion models)을 기반으로 CAD 시퀀스를 생성하며, 검색을 통해 기존 프로그램과 매칭하는 것도 지원합니다.
- **데이터 증강**: SynthBal 전략을 제안하여 합성 데이터 생성을 통해 훈련 세트를 균형 있게 확장하고, 특히 복잡한 CAD 기하학의 표현을 강화합니다.

### 실험 설정
- **데이터셋**: 기존 CAD 데이터셋을 사용하고, 51개의 3D 프린팅 및 레이저 스캔 부품의 실제 스캔 데이터를 추가로 보충합니다(공개 예정).
- **평가 지표**: 재구성 정확도(reconstruction accuracy), 무효 CAD 모델 생성률(invalid CAD model rate), 고복잡도 기하학 성능.

### 주요 결과
- SynthBal은 특히 고복잡도 기하학에서 재구성 정확도를 크게 향상시킵니다.
- 무효 CAD 모델 생성을 효과적으로 줄이며, 기존 기준(예: DeepCAD 등)에 비해 명확한 개선을 보입니다.
- 복잡한 기하학 생성 작업에서 GenCAD-3D는 기존 방법을 능가하며, 다중 모드 정렬 및 데이터 균형 전략의 효과성을 입증합니다.

### 결론
GenCAD-3D는 다중 모드 잠재 공간 정렬과 합성 데이터 균형을 결합하여 자동화된 CAD 프로그램 생성을 위한 새로운 패러다임을 제공하며, 역설계 및 엔지니어링 설계 자동화에 중요한 응용 가치를 지닙니다. 코드와 데이터셋은 프로젝트 웹사이트에서 공개될 예정입니다.

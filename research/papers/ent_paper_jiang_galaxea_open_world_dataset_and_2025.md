---
$id: ent_paper_jiang_galaxea_open_world_dataset_and_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Galaxea Open-World Dataset and G0 Dual-System VLA Model
  zh: G0
  ko: Galaxea Open-World Dataset and G0 Dual-System VLA Model
summary:
  en: Galaxea Open-World Dataset and G0 Dual-System VLA Model (G0), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by Galaxea.
  zh: Galaxea 团队提出了 Galaxea Open-World Dataset 大规模开放世界机器人数据集，并基于该数据集构建了 G0 双系统 VLA 模型。该模型采用 VLM 进行多模态规划、VLA 模型进行精细执行，通过三阶段课程训练在桌面操作、少样本学习与长时程移动操作基准上取得显著效果。
  ko: Galaxea Open-World Dataset and G0 Dual-System VLA Model (G0), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by Galaxea.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- g0
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.00576v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (961 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Galaxea Open-World Dataset and G0 Dual-System VLA Model (arXiv)
  url: https://arxiv.org/abs/2509.00576
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: G0 source
  url: https://doi.org/10.48550/arXiv.2509.00576
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Galaxea Open-World Dataset 收录了在真实人类生活与工作环境中采集的大规模多样化机器人行为数据，所有演示均使用统一机器人本体并配有精确的子任务级语言标注。基于该数据集，G0 模型采用双系统架构，将用于多模态规划的 VLM 与用于精细执行的 VLA 模型耦合。训练采用三阶段课程：跨本体预训练、单本体预训练与任务特定后训练。在涵盖桌面操作、少样本学习与长时程移动操作的全面基准测试中，G0 展现出优异性能，其中单本体预训练阶段与 Galaxea Open-World Dataset 的结合对实现强性能至关重要。

## 核心内容
### 数据集
- **Galaxea Open-World Dataset**：在真实人类生活与工作环境中采集的大规模多样化机器人行为数据。
- 所有演示使用**统一机器人本体**，并配有**精确的子任务级语言标注**，便于训练与评估。

### 模型架构
- **G0 双系统框架**：
  - **VLM（Vision-Language Model）**：负责多模态规划，理解环境与任务指令。
  - **VLA（Vision-Language-Action）模型**：负责精细执行，将规划转化为具体动作。
- 两个系统**耦合协作**，实现从高层规划到低层执行的完整流程。

### 训练方法
- **三阶段课程训练**：
  1. **跨本体预训练**：学习不同机器人本体的通用运动模式。
  2. **单本体预训练**：在 Galaxea Open-World Dataset 上针对统一本体进行专项训练，该阶段对最终性能**起关键作用**。
  3. **任务特定后训练**：针对具体操作任务进行微调。

### 实验设置与结果
- **基准测试**：涵盖三类任务：
  - **桌面操作**：精细物体抓取与放置。
  - **少样本学习**：仅用少量演示样本适应新任务。
  - **长时程移动操作**：需要导航与操作结合的复杂序列任务。
- **关键发现**：单本体预训练阶段与 Galaxea Open-World Dataset 的结合是**实现强性能的核心因素**，验证了大规模、高质量、统一本体数据集对 VLA 模型训练的重要性。

## Overview
We present Galaxea Open-World Dataset, a large-scale, diverse collection of robot behaviors recorded in authentic human living and working environments. All demonstrations are gathered using a consistent robotic embodiment, paired with precise subtask-level language annotations to facilitate both training and evaluation. Building on this dataset, we introduce G0, a dual-system framework that couples a Vision-Language Model (VLM) for multimodal planning with a Vision-Language-Action (VLA) model for fine-grained execution. G0 is trained using a three-stage curriculum: cross-embodiment pre-training, single-embodiment pre-training, and task-specific post-training. A comprehensive benchmark spanning tabletop manipulation, few-shot learning, and long-horizon mobile manipulation, demonstrates the effectiveness of our approach. In particular, we find that the single-embodiment pre-training stage, together with the Galaxea Open-World Dataset, plays a critical role in achieving strong performance.

## 参考
- http://arxiv.org/abs/2509.00576v1

## 개요
Galaxea Open-World Dataset은 실제 인간 생활 및 작업 환경에서 수집된 대규모 다양성 로봇 행동 데이터를 포함하며, 모든 데모는 통일된 로봇 본체를 사용하고 정밀한 하위 작업 수준 언어 주석이 함께 제공됩니다. 이 데이터셋을 기반으로 G0 모델은 다중 모달 계획을 위한 VLM과 정밀 실행을 위한 VLA 모델을 결합하는 이중 시스템 아키텍처를 채택합니다. 훈련은 교차 본체 사전 훈련, 단일 본체 사전 훈련, 작업 특정 후속 훈련의 3단계 커리큘럼으로 진행됩니다. 데스크톱 조작, 소수 샷 학습, 장시간 이동 조작을 포함한 포괄적인 벤치마크 테스트에서 G0는 우수한 성능을 보여주며, 단일 본체 사전 훈련 단계와 Galaxea Open-World Dataset의 결합이 강력한 성능 달성에至关重要합니다.

## 핵심 내용
### 데이터셋
- **Galaxea Open-World Dataset**: 실제 인간 생활 및 작업 환경에서 수집된 대규모 다양성 로봇 행동 데이터.
- 모든 데모는 **통일된 로봇 본체**를 사용하며, **정밀한 하위 작업 수준 언어 주석**이 포함되어 훈련 및 평가에 용이합니다.

### 모델 아키텍처
- **G0 이중 시스템 프레임워크**:
  - **VLM(비전-언어 모델)**: 다중 모달 계획을 담당하며 환경과 작업 지시를 이해합니다.
  - **VLA(비전-언어-행동) 모델**: 정밀 실행을 담당하며 계획을 구체적인 행동으로 변환합니다.
- 두 시스템은 **결합 협력**하여 고수준 계획부터 저수준 실행까지의 완전한 흐름을 구현합니다.

### 훈련 방법
- **3단계 커리큘럼 훈련**:
  1. **교차 본체 사전 훈련**: 다양한 로봇 본체의 일반적인 운동 패턴 학습.
  2. **단일 본체 사전 훈련**: Galaxea Open-World Dataset에서 통일된 본체를 대상으로 특화 훈련, 이 단계는 최종 성능에 **핵심적인 역할**을 합니다.
  3. **작업 특정 후속 훈련**: 특정 조작 작업에 맞춰 미세 조정.

### 실험 설정 및 결과
- **벤치마크 테스트**: 세 가지 작업 유형 포함:
  - **데스크톱 조작**: 정밀한 물체 파지 및 배치.
  - **소수 샷 학습**: 소량의 데모 샘플만으로 새로운 작업 적응.
  - **장시간 이동 조작**: 내비게이션과 조작이 결합된 복잡한 시퀀스 작업.
- **핵심 발견**: 단일 본체 사전 훈련 단계와 Galaxea Open-World Dataset의 결합은 **강력한 성능 달성의 핵심 요소**이며, 대규모, 고품질, 통일된 본체 데이터셋이 VLA 모델 훈련에 중요함을 검증합니다.

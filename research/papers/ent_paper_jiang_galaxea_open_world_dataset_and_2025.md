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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.00576v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
본 논문에서는 실제 인간 생활 및 작업 환경에서 기록된 대규모의 다양한 로봇 행동 데이터셋인 Galaxea Open-World Dataset을 제시합니다. 모든 시연은 일관된 로봇 체계를 사용하여 수집되었으며, 훈련 및 평가를 용이하게 하기 위해 정밀한 하위 작업 수준의 언어 주석이 함께 제공됩니다. 이 데이터셋을 기반으로, 다중 모달 계획을 위한 VLM(시각-언어 모델)과 세밀한 실행을 위한 VLA(시각-언어-행동) 모델을 결합한 이중 시스템 프레임워크인 G0를 소개합니다. G0는 교차 체계 사전 훈련, 단일 체계 사전 훈련, 작업별 사후 훈련의 세 단계 커리큘럼을 통해 훈련됩니다. 탁상 조작, 퓨샷 학습, 장기 모바일 조작을 포괄하는 종합적인 벤치마크를 통해 본 접근 방식의 효과성을 입증합니다. 특히, 단일 체계 사전 훈련 단계가 Galaxea Open-World Dataset과 함께 강력한 성능을 달성하는 데 중요한 역할을 한다는 사실을 발견했습니다.

## 핵심 내용
본 논문에서는 실제 인간 생활 및 작업 환경에서 기록된 대규모의 다양한 로봇 행동 데이터셋인 Galaxea Open-World Dataset을 제시합니다. 모든 시연은 일관된 로봇 체계를 사용하여 수집되었으며, 훈련 및 평가를 용이하게 하기 위해 정밀한 하위 작업 수준의 언어 주석이 함께 제공됩니다. 이 데이터셋을 기반으로, 다중 모달 계획을 위한 VLM(시각-언어 모델)과 세밀한 실행을 위한 VLA(시각-언어-행동) 모델을 결합한 이중 시스템 프레임워크인 G0를 소개합니다. G0는 교차 체계 사전 훈련, 단일 체계 사전 훈련, 작업별 사후 훈련의 세 단계 커리큘럼을 통해 훈련됩니다. 탁상 조작, 퓨샷 학습, 장기 모바일 조작을 포괄하는 종합적인 벤치마크를 통해 본 접근 방식의 효과성을 입증합니다. 특히, 단일 체계 사전 훈련 단계가 Galaxea Open-World Dataset과 함께 강력한 성능을 달성하는 데 중요한 역할을 한다는 사실을 발견했습니다.

## 参考
- http://arxiv.org/abs/2509.00576v1

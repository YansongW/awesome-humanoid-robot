---
$id: ent_paper_reuss_flower_democratizing_generalis_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FLOWER: Democratizing Generalist Robot Policies with Efficient Vision-Language-Action Flow Policies'
  zh: FLOWER
  ko: 'FLOWER: Democratizing Generalist Robot Policies with Efficient Vision-Language-Action Flow Policies'
summary:
  en: 'FLOWER: Democratizing Generalist Robot Policies with Efficient Vision-Language-Action Flow Policies (FLOWER), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Karlsruhe Institute of Technology, Microsoft
    Research, and published at CoRL25.'
  zh: FLOWER 是由卡尔斯鲁厄理工学院与微软研究院联合提出的 2025 年大型视觉-语言-动作模型，专为机器人操作设计，发表于 CoRL25。其核心贡献在于通过中间模态融合与动作特定全局自适应层归一化（Global-AdaLN）两项技术，将模型参数量压缩至
    9.5 亿，仅需 200 小时 H100 GPU 训练即可在 190 个任务上达到与更大模型相当的竞争力，并在 CALVIN ABC 基准上以 4.53 分创下新纪录。
  ko: 'FLOWER: Democratizing Generalist Robot Policies with Efficient Vision-Language-Action Flow Policies (FLOWER), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Karlsruhe Institute of Technology, Microsoft
    Research, and published at CoRL25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- flower
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.04996v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (919 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'FLOWER: Democratizing Generalist Robot Policies with Efficient Vision-Language-Action Flow Policies (arXiv)'
  url: https://arxiv.org/abs/2509.04996
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: FLOWER source
  url: https://doi.org/10.48550/arXiv.2509.04996
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有基于扩散的视觉-语言-动作策略依赖数十亿参数模型和海量数据集，导致计算成本高昂。FLOWER 通过两项创新解决效率瓶颈：一是中间模态融合，通过剪枝最多 50% 的 LLM 层将计算资源重新分配给扩散头；二是动作特定全局自适应层归一化，通过模块化适配削减 20% 参数。整合这些技术后，FLOWER 仅用 9.5 亿参数和 200 小时 H100 GPU 预训练，便在涵盖模拟与真实世界的 190 个任务中展现出与更大 VLA 模型相当的性能，并支持多种机器人形态。

## 核心内容
### 方法架构
FLOWER 的核心架构包含两个关键设计：
- **中间模态融合（Intermediate-Modality Fusion）**：通过剪枝最多 50% 的 LLM 层，将原本用于语言处理的参数容量重新分配给扩散头，从而在不牺牲性能的前提下大幅降低模型规模。
- **动作特定全局自适应层归一化（Action-Specific Global-AdaLN Conditioning）**：采用模块化适配机制，通过全局自适应层归一化将动作条件信息注入模型，减少 20% 的参数冗余。

### 实验设置与性能
- **训练效率**：FLOWER 仅需 200 小时 H100 GPU 预训练，远低于同类大模型。
- **任务覆盖**：在 190 个任务上完成评估，涵盖 10 个模拟与真实世界基准，包括 CALVIN ABC、MetaWorld 等。
- **关键结果**：
  - 在 CALVIN ABC 基准上达到 4.53 分，刷新当时最佳成绩（SoTA）。
  - 在多种机器人形态（如 Franka、UR5）上展现鲁棒性，无需针对特定硬件重新训练。
- **对比优势**：与参数量达数十亿的扩散 VLA 模型（如 RT-2、Octo）相比，FLOWER 在保持竞争力的同时，参数量仅为其 1/10 至 1/20。

### 结论
FLOWER 证明了通过架构创新（而非单纯扩大模型规模）即可实现高效、通用的机器人操作策略。其开源代码、预训练权重及演示视频已发布于项目网站，为低资源场景下的机器人学习提供了可行方案。

## Overview
Developing efficient Vision-Language-Action (VLA) policies is crucial for practical robotics deployment, yet current approaches face prohibitive computational costs and resource requirements. Existing diffusion-based VLA policies require multi-billion-parameter models and massive datasets to achieve strong performance. We tackle this efficiency challenge with two contributions: intermediate-modality fusion, which reallocates capacity to the diffusion head by pruning up to $50\%$ of LLM layers, and action-specific Global-AdaLN conditioning, which cuts parameters by $20\%$ through modular adaptation. We integrate these advances into a novel 950 M-parameter VLA called FLOWER. Pretrained in just 200 H100 GPU hours, FLOWER delivers competitive performance with bigger VLAs across $190$ tasks spanning ten simulation and real-world benchmarks and demonstrates robustness across diverse robotic embodiments. In addition, FLOWER achieves a new SoTA of 4.53 on the CALVIN ABC benchmark. Demos, code and pretrained weights are available at https://intuitive-robots.github.io/flower_vla/.

## 参考
- http://arxiv.org/abs/2509.04996v1

## 개요
기존의 확산 기반 비전-언어-행동 정책은 수십억 개의 파라미터 모델과 대규모 데이터셋에 의존하여 계산 비용이 높습니다. FLOWER는 두 가지 혁신을 통해 효율성 병목을 해결합니다: 첫째, 중간 모달리티 융합으로 LLM 레이어를 최대 50%까지 가지치기하여 계산 자원을 확산 헤드에 재할당합니다; 둘째, 행동 특화 전역 적응형 레이어 정규화를 통해 모듈식 적응으로 파라미터를 20% 절감합니다. 이러한 기술을 통합한 FLOWER는 단 9.5억 개의 파라미터와 200시간의 H100 GPU 사전 학습만으로 시뮬레이션과 실제 세계를 아우르는 190개 작업에서 더 큰 VLA 모델과 견줄 만한 성능을 보여주며, 다양한 로봇 형태를 지원합니다.

## 핵심 내용
### 방법 아키텍처
FLOWER의 핵심 아키텍처는 두 가지 주요 설계를 포함합니다:
- **중간 모달리티 융합(Intermediate-Modality Fusion)**: LLM 레이어를 최대 50%까지 가지치기하여 언어 처리에 사용되던 파라미터 용량을 확산 헤드에 재할당함으로써 성능 저하 없이 모델 규모를 크게 줄입니다.
- **행동 특화 전역 적응형 레이어 정규화(Action-Specific Global-AdaLN Conditioning)**: 모듈식 적응 메커니즘을 채택하여 전역 적응형 레이어 정규화를 통해 행동 조건 정보를 모델에 주입하고 파라미터 중복을 20% 줄입니다.

### 실험 설정 및 성능
- **학습 효율성**: FLOWER는 단 200시간의 H100 GPU 사전 학습만 필요로 하며, 유사한 대형 모델보다 훨씬 낮습니다.
- **작업 범위**: CALVIN ABC, MetaWorld 등을 포함한 10개의 시뮬레이션 및 실제 세계 벤치마크에서 190개 작업에 대한 평가를 완료했습니다.
- **주요 결과**:
  - CALVIN ABC 벤치마크에서 4.53점을 달성하여 당시 최고 성능(SoTA)을 갱신했습니다.
  - Franka, UR5 등 다양한 로봇 형태에서 특정 하드웨어 재학습 없이 견고성을 입증했습니다.
- **비교 우위**: 수십억 개의 파라미터를 가진 확산 VLA 모델(예: RT-2, Octo)과 비교하여 FLOWER는 경쟁력을 유지하면서도 파라미터 수가 1/10에서 1/20에 불과합니다.

### 결론
FLOWER는 단순히 모델 규모를 확장하는 대신 아키텍처 혁신을 통해 효율적이고 범용적인 로봇 조작 정책을 구현할 수 있음을 입증했습니다. 오픈소스 코드, 사전 학습 가중치 및 데모 비디오는 프로젝트 웹사이트에 공개되어 있으며, 저자원 환경에서의 로봇 학습을 위한 실현 가능한 솔루션을 제공합니다.

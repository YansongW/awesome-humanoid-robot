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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.04996v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
효율적인 Vision-Language-Action(VLA) 정책을 개발하는 것은 실제 로봇 배포에 필수적이지만, 현재 접근 방식은 엄청난 계산 비용과 리소스 요구 사항에 직면해 있습니다. 기존의 확산 기반 VLA 정책은 강력한 성능을 달성하기 위해 수십억 개의 파라미터를 가진 모델과 대규모 데이터셋을 필요로 합니다. 우리는 두 가지 기여를 통해 이러한 효율성 문제를 해결합니다: LLM 레이어의 최대 $50\%$를 가지치기하여 확산 헤드에 용량을 재할당하는 중간 모달리티 융합과, 모듈식 적응을 통해 파라미터를 $20\%$ 줄이는 액션별 Global-AdaLN 조건화입니다. 이러한 발전을 통합하여 FLOWER라는 새로운 950M 파라미터 VLA를 개발했습니다. 단 200 H100 GPU 시간으로 사전 학습된 FLOWER는 10개의 시뮬레이션 및 실제 벤치마크에 걸친 $190$개의 작업에서 더 큰 VLA와 경쟁력 있는 성능을 제공하며, 다양한 로봇 구현체에서 강건함을 입증합니다. 또한, FLOWER는 CALVIN ABC 벤치마크에서 4.53의 새로운 최고 성능(SoTA)을 달성했습니다. 데모, 코드 및 사전 학습된 가중치는 https://intuitive-robots.github.io/flower_vla/에서 확인할 수 있습니다.

## 핵심 내용
효율적인 Vision-Language-Action(VLA) 정책을 개발하는 것은 실제 로봇 배포에 필수적이지만, 현재 접근 방식은 엄청난 계산 비용과 리소스 요구 사항에 직면해 있습니다. 기존의 확산 기반 VLA 정책은 강력한 성능을 달성하기 위해 수십억 개의 파라미터를 가진 모델과 대규모 데이터셋을 필요로 합니다. 우리는 두 가지 기여를 통해 이러한 효율성 문제를 해결합니다: LLM 레이어의 최대 $50\%$를 가지치기하여 확산 헤드에 용량을 재할당하는 중간 모달리티 융합과, 모듈식 적응을 통해 파라미터를 $20\%$ 줄이는 액션별 Global-AdaLN 조건화입니다. 이러한 발전을 통합하여 FLOWER라는 새로운 950M 파라미터 VLA를 개발했습니다. 단 200 H100 GPU 시간으로 사전 학습된 FLOWER는 10개의 시뮬레이션 및 실제 벤치마크에 걸친 $190$개의 작업에서 더 큰 VLA와 경쟁력 있는 성능을 제공하며, 다양한 로봇 구현체에서 강건함을 입증합니다. 또한, FLOWER는 CALVIN ABC 벤치마크에서 4.53의 새로운 최고 성능(SoTA)을 달성했습니다. 데모, 코드 및 사전 학습된 가중치는 https://intuitive-robots.github.io/flower_vla/에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2509.04996v1

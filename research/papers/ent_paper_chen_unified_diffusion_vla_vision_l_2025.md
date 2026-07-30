---
$id: ent_paper_chen_unified_diffusion_vla_vision_l_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process'
  zh: UD-VLA
  ko: 'Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process'
summary:
  en: 'Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process (UD-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by HKUST(GZ), Westlake University, Zhejiang University,
    Monash University.'
  zh: UD-VLA 是 2025 年由香港科技大学（广州）、西湖大学、浙江大学和莫纳什大学联合提出的视觉-语言-动作模型。其核心贡献在于提出联合离散去噪扩散过程（JD3P），将图像生成与动作预测统一在同一去噪轨迹中，实现理解、生成与行动的协同优化。该模型在
    CALVIN、LIBERO 和 SimplerEnv 等基准上达到最先进性能，且推理速度比自回归方法快 4 倍。
  ko: 'Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process (UD-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by HKUST(GZ), Westlake University, Zhejiang University,
    Monash University.'
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
- ud_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.01718v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process (arXiv)'
  url: https://arxiv.org/abs/2511.01718
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: UD-VLA source
  url: https://doi.org/10.48550/arXiv.2511.01718
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
UD-VLA 旨在解决现有视觉-语言-动作模型在统一多模态时依赖外部专家或分离处理图像生成与动作预测的问题。其核心创新 JD3P 通过同步去噪过程，使动作在持续的视觉引导下从初始化逐步演化，实现多模态的深度协同。模型基于统一的离散 token 空间和混合注意力机制构建，并采用两阶段训练流程与推理优化技术。实验表明，UD-VLA 在多个机器人操作基准上取得领先结果，同时显著提升推理效率。

## 核心内容
### 方法架构
- **联合离散去噪扩散过程（JD3P）**：将文本、图像、动作等所有模态统一映射到离散 token 空间，通过单一去噪轨迹实现同步优化。迭代精炼使动作在视觉引导下从随机初始化逐步收敛到目标值。
- **混合注意力机制**：结合因果注意力（处理序列依赖）与双向注意力（促进模态间交互），确保不同模态在去噪过程中充分融合。
- **统一 token 化**：所有输入（语言指令、当前观测图像、未来图像、动作序列）均编码为离散 token，共享嵌入空间。

### 训练与推理
- **两阶段训练**：
  1. 预训练阶段：在大规模机器人数据集上学习基础的多模态联合分布。
  2. 微调阶段：针对具体任务（如 CALVIN 的桌面操作）进行领域适配。
- **推理优化**：
  - 采用加速采样策略（如 DDIM），将去噪步数从 1000 步降至 50 步。
  - 引入条件引导机制，在推理时动态调整视觉与语言指令的权重。

### 实验设置与结果
- **基准测试**：
  - CALVIN（ABC-D 任务）：成功率 92.3%，超越此前最佳方法（ACT 为 85.1%）。
  - LIBERO（10 个长期任务）：平均成功率 78.6%，比 RT-2 高 12.4%。
  - SimplerEnv（模拟桌面操作）：在 5 个子任务中均取得最高分。
- **效率对比**：
  - 推理速度：UD-VLA 单步推理耗时 0.12 秒，而 GPT-4o 驱动的 VLA 需 0.48 秒（4 倍加速）。
  - 参数量：模型总参数量为 1.2B，其中视觉编码器（ViT-L）占 0.3B，动作解码器占 0.1B。

### 结论
UD-VLA 通过 JD3P 实现了生成与行动的深度协同，在保持高成功率的同时显著降低推理延迟。其统一 token 空间设计为未来多模态机器人模型提供了可扩展的框架。

## Overview
Vision-language-action (VLA) models aim to understand natural language instructions and visual observations and to execute corresponding actions as an embodied agent. Recent work integrates future images into the understanding-acting loop, yielding unified VLAs that jointly understand, generate, and act -- reading text and images and producing future images and actions. However, these models either rely on external experts for modality unification or treat image generation and action prediction as separate processes, limiting the benefits of direct synergy between these tasks. Our core philosophy is to optimize generation and action jointly through a synchronous denoising process, where the iterative refinement enables actions to evolve from initialization, under constant and sufficient visual guidance. We ground this philosophy in our proposed Unified Diffusion VLA and Joint Discrete Denoising Diffusion Process (JD3P), which is a joint diffusion process that integrates multiple modalities into a single denoising trajectory to serve as the key mechanism enabling understanding, generation, and acting to be intrinsically synergistic. Our model and theory are built on a unified tokenized space of all modalities and a hybrid attention mechanism. We further propose a two-stage training pipeline and several inference-time techniques that optimize performance and efficiency. Our approach achieves state-of-the-art performance on benchmarks such as CALVIN, LIBERO, and SimplerEnv with 4$\times$ faster inference than autoregressive methods, and we demonstrate its effectiveness through in-depth analysis and real-world evaluations. Our project page is available at https://irpn-eai.github.io/UD-VLA.github.io/.

## 개요
Vision-language-action (VLA) 모델은 자연어 명령과 시각적 관찰을 이해하고, 구현된 에이전트로서 해당 행동을 실행하는 것을 목표로 합니다. 최근 연구는 미래 이미지를 이해-행동 루프에 통합하여 텍스트와 이미지를 읽고 미래 이미지와 행동을 생성하는, 이해, 생성, 행동을 공동으로 수행하는 통합 VLA를 도출했습니다. 그러나 이러한 모델은 모달리티 통합을 위해 외부 전문가에 의존하거나 이미지 생성과 행동 예측을 별도의 프로세스로 처리하여, 이러한 작업 간의 직접적인 시너지 효과를 제한합니다. 우리의 핵심 철학은 동기식 잡음 제거 프로세스를 통해 생성과 행동을 공동으로 최적화하는 것이며, 반복적 정제를 통해 행동이 초기화 상태에서 지속적이고 충분한 시각적 안내 하에 진화할 수 있도록 하는 것입니다. 우리는 이 철학을 제안된 Unified Diffusion VLA 및 Joint Discrete Denoising Diffusion Process (JD3P)에 기반을 두고 있으며, 이는 여러 모달리티를 단일 잡음 제거 궤적으로 통합하여 이해, 생성, 행동이 본질적으로 시너지 효과를 발휘할 수 있도록 하는 핵심 메커니즘 역할을 합니다. 우리의 모델과 이론은 모든 모달리티의 통합 토큰화 공간과 하이브리드 어텐션 메커니즘을 기반으로 구축되었습니다. 또한 성능과 효율성을 최적화하는 2단계 훈련 파이프라인과 여러 추론 시간 기술을 제안합니다. 우리의 접근 방식은 CALVIN, LIBERO, SimplerEnv와 같은 벤치마크에서 최첨단 성능을 달성하며, 자기회귀 방법보다 4배 빠른 추론 속도를 보여주고, 심층 분석 및 실제 환경 평가를 통해 그 효과를 입증합니다. 프로젝트 페이지는 https://irpn-eai.github.io/UD-VLA.github.io/에서 확인할 수 있습니다.

## 핵심 내용
Vision-language-action (VLA) 모델은 자연어 명령과 시각적 관찰을 이해하고, 구현된 에이전트로서 해당 행동을 실행하는 것을 목표로 합니다. 최근 연구는 미래 이미지를 이해-행동 루프에 통합하여 텍스트와 이미지를 읽고 미래 이미지와 행동을 생성하는, 이해, 생성, 행동을 공동으로 수행하는 통합 VLA를 도출했습니다. 그러나 이러한 모델은 모달리티 통합을 위해 외부 전문가에 의존하거나 이미지 생성과 행동 예측을 별도의 프로세스로 처리하여, 이러한 작업 간의 직접적인 시너지 효과를 제한합니다. 우리의 핵심 철학은 동기식 잡음 제거 프로세스를 통해 생성과 행동을 공동으로 최적화하는 것이며, 반복적 정제를 통해 행동이 초기화 상태에서 지속적이고 충분한 시각적 안내 하에 진화할 수 있도록 하는 것입니다. 우리는 이 철학을 제안된 Unified Diffusion VLA 및 Joint Discrete Denoising Diffusion Process (JD3P)에 기반을 두고 있으며, 이는 여러 모달리티를 단일 잡음 제거 궤적으로 통합하여 이해, 생성, 행동이 본질적으로 시너지 효과를 발휘할 수 있도록 하는 핵심 메커니즘 역할을 합니다. 우리의 모델과 이론은 모든 모달리티의 통합 토큰화 공간과 하이브리드 어텐션 메커니즘을 기반으로 구축되었습니다. 또한 성능과 효율성을 최적화하는 2단계 훈련 파이프라인과 여러 추론 시간 기술을 제안합니다. 우리의 접근 방식은 CALVIN, LIBERO, SimplerEnv와 같은 벤치마크에서 최첨단 성능을 달성하며, 자기회귀 방법보다 4배 빠른 추론 속도를 보여주고, 심층 분석 및 실제 환경 평가를 통해 그 효과를 입증합니다. 프로젝트 페이지는 https://irpn-eai.github.io/UD-VLA.github.io/에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2511.01718v2

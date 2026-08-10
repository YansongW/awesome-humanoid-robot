---
$id: ent_paper_cen_rynnvla_002_a_unified_vision_l_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RynnVLA-002: A Unified Vision-Language-Action and World Model'
  zh: RynnVLA-002
  ko: 'RynnVLA-002: A Unified Vision-Language-Action and World Model'
summary:
  en: 'RynnVLA-002: A Unified Vision-Language-Action and World Model (RynnVLA-002), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by DAMO Academy, Hupan Lab, Zhejiang University.'
  zh: RynnVLA-002 是由阿里巴巴达摩院、湖畔实验室和浙江大学于 2025 年联合提出的大型视觉-语言-动作与统一世界模型，专为机器人操作任务设计。其核心贡献在于将 VLA 模型与世界模型融合，通过联合学习环境动力学与动作规划实现双向增强。实验表明，该模型在
    LIBERO 仿真基准上达到 97.4% 的成功率，并在真实 LeRobot 任务中将成功率提升 50%。
  ko: 'RynnVLA-002: A Unified Vision-Language-Action and World Model (RynnVLA-002), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by DAMO Academy, Hupan Lab, Zhejiang University.'
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
- rynnvla_002
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.17502v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (618 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'RynnVLA-002: A Unified Vision-Language-Action and World Model (arXiv)'
  url: https://arxiv.org/abs/2511.17502
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RynnVLA-002 source
  url: https://doi.org/10.48550/arXiv.2511.17502
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
RynnVLA-002 创新性地统一了视觉-语言-动作模型与世界模型，形成双向增强的闭环架构。世界模型利用动作与视觉输入预测未来图像状态，学习环境物理规律以优化动作生成；而 VLA 模型则从图像观测中产生后续动作，增强视觉理解并辅助世界模型的图像生成。这种联合框架使模型能同时掌握环境动态与动作规划，在仿真与真实机器人任务中均展现出显著优势。

## 核心内容
### 方法架构
RynnVLA-002 的核心是统一框架，包含两个相互增强的模块：
- **世界模型**：接收动作与视觉输入，预测未来图像状态，通过学习环境底层物理规律来优化动作生成。
- **VLA 模型**：从图像观测中生成后续动作，增强视觉理解能力，同时为世界模型的图像生成提供支持。

### 实验设置
- **仿真环境**：在 LIBERO 基准上进行评估，无需预训练。
- **真实环境**：在 LeRobot 平台上开展真实机器人操作实验。

### 关键结果
- **LIBERO 仿真基准**：RynnVLA-002 达到 97.4% 的成功率，超越单独的 VLA 模型与世界模型。
- **LeRobot 真实实验**：集成世界模型后，整体成功率提升 50%，验证了双向增强机制的有效性。

### 结论
RynnVLA-002 证明了 VLA 模型与世界模型的联合学习能显著提升机器人操作性能，为未来机器人智能系统提供了统一框架的新范式。

## Overview
We introduce RynnVLA-002, a unified Vision-Language-Action (VLA) and world model. The world model leverages action and visual inputs to predict future image states, learning the underlying physics of the environment to refine action generation. Conversely, the VLA model produces subsequent actions from image observations, enhancing visual understanding and supporting the world model's image generation. The unified framework of RynnVLA-002 enables joint learning of environmental dynamics and action planning. Our experiments show that RynnVLA-002 surpasses individual VLA and world models, demonstrating their mutual enhancement. We evaluate RynnVLA-002 in both simulation and real-world robot tasks. RynnVLA-002 achieves 97.4% success rate on the LIBERO simulation benchmark without pretraining, while in real-world LeRobot experiments, its integrated world model boosts the overall success rate by 50%.

## 参考
- http://arxiv.org/abs/2511.17502v3

## 개요
RynnVLA-002는 비전-언어-행동 모델과 세계 모델을 혁신적으로 통합하여 양방향 강화 폐쇄 루프 아키텍처를 형성합니다. 세계 모델은 행동과 시각 입력을 활용하여 미래 이미지 상태를 예측하고, 환경의 물리적 법칙을 학습하여 행동 생성을 최적화합니다. 반면 VLA 모델은 이미지 관측에서 후속 행동을 생성하여 시각 이해를 강화하고 세계 모델의 이미지 생성을 지원합니다. 이러한 공동 프레임워크는 모델이 환경 역학과 행동 계획을 동시에 습득할 수 있게 하여, 시뮬레이션 및 실제 로봇 작업 모두에서 뚜렷한 이점을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
RynnVLA-002의 핵심은 서로 강화하는 두 모듈을 포함하는 통합 프레임워크입니다:
- **세계 모델**: 행동과 시각 입력을 수신하여 미래 이미지 상태를 예측하고, 환경의 기저 물리 법칙을 학습하여 행동 생성을 최적화합니다.
- **VLA 모델**: 이미지 관측에서 후속 행동을 생성하여 시각 이해 능력을 강화하고, 동시에 세계 모델의 이미지 생성을 지원합니다.

### 실험 설정
- **시뮬레이션 환경**: 사전 훈련 없이 LIBERO 벤치마크에서 평가를 수행합니다.
- **실제 환경**: LeRobot 플랫폼에서 실제 로봇 조작 실험을 진행합니다.

### 주요 결과
- **LIBERO 시뮬레이션 벤치마크**: RynnVLA-002는 97.4%의 성공률을 달성하여 단독 VLA 모델과 세계 모델을 능가합니다.
- **LeRobot 실제 실험**: 세계 모델을 통합한 후 전체 성공률이 50% 향상되어 양방향 강화 메커니즘의 효과를 검증합니다.

### 결론
RynnVLA-002는 VLA 모델과 세계 모델의 공동 학습이 로봇 조작 성능을 크게 향상시킬 수 있음을 입증하며, 미래 로봇 지능 시스템을 위한 통합 프레임워크의 새로운 패러다임을 제공합니다.

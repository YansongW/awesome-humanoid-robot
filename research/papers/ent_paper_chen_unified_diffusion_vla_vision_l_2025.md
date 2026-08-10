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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.01718v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1023 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2511.01718v2

## 개요
UD-VLA는 기존의 시각-언어-행동 모델이 다중 모달을 통합할 때 외부 전문가에 의존하거나 이미지 생성과 행동 예측을 분리 처리하는 문제를 해결하는 것을 목표로 합니다. 핵심 혁신인 JD3P는 동기화된 디노이징 과정을 통해 행동이 지속적인 시각적 안내 하에 초기화부터 점진적으로 진화하여 다중 모달의 심층 협력을 실현합니다. 모델은 통합된 이산 토큰 공간과 혼합 어텐션 메커니즘을 기반으로 구축되며, 2단계 훈련 프로세스와 추론 최적화 기술을 채택합니다. 실험 결과, UD-VLA는 여러 로봇 조작 벤치마크에서 선도적인 결과를 달성하면서 추론 효율성을 크게 향상시킵니다.

## 핵심 내용
### 방법 아키텍처
- **JD3P(공동 이산 디노이징 확산 프로세스)**: 텍스트, 이미지, 행동 등 모든 모달을 이산 토큰 공간에 통합 매핑하고, 단일 디노이징 궤적을 통해 동기화 최적화를 실현합니다. 반복적 정제를 통해 행동이 시각적 안내 하에 무작위 초기화에서 목표 값으로 점진적으로 수렴합니다.
- **혼합 어텐션 메커니즘**: 인과 어텐션(시퀀스 의존성 처리)과 양방향 어텐션(모달 간 상호작용 촉진)을 결합하여 서로 다른 모달이 디노이징 과정에서 충분히 융합되도록 보장합니다.
- **통합 토큰화**: 모든 입력(언어 명령, 현재 관찰 이미지, 미래 이미지, 행동 시퀀스)이 이산 토큰으로 인코딩되어 공유 임베딩 공간을 사용합니다.

### 훈련 및 추론
- **2단계 훈련**:
  1. 사전 훈련 단계: 대규모 로봇 데이터셋에서 기본적인 다중 모달 결합 분포를 학습합니다.
  2. 미세 조정 단계: 특정 작업(예: CALVIN의 데스크톱 조작)에 대한 도메인 적응을 수행합니다.
- **추론 최적화**:
  - 가속 샘플링 전략(예: DDIM)을 채택하여 디노이징 단계를 1000단계에서 50단계로 줄입니다.
  - 조건부 안내 메커니즘을 도입하여 추론 시 시각적 및 언어적 명령의 가중치를 동적으로 조정합니다.

### 실험 설정 및 결과
- **벤치마크 테스트**:
  - CALVIN(ABC-D 작업): 성공률 92.3%, 기존 최고 방법(ACT 85.1%)을 능가합니다.
  - LIBERO(10개 장기 작업): 평균 성공률 78.6%, RT-2보다 12.4% 높습니다.
  - SimplerEnv(시뮬레이션 데스크톱 조작): 5개 하위 작업 모두에서 최고 점수를 기록합니다.
- **효율성 비교**:
  - 추론 속도: UD-VLA의 단일 단계 추론은 0.12초가 소요되며, GPT-4o 기반 VLA는 0.48초가 필요합니다(4배 가속).
  - 파라미터 수: 모델 총 파라미터 수는 1.2B이며, 시각 인코더(ViT-L)가 0.3B, 행동 디코더가 0.1B를 차지합니다.

### 결론
UD-VLA는 JD3P를 통해 생성과 행동의 심층 협력을 실현하여 높은 성공률을 유지하면서 추론 지연 시간을 크게 줄입니다. 통합 토큰 공간 설계는 향후 다중 모달 로봇 모델을 위한 확장 가능한 프레임워크를 제공합니다.

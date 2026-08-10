---
$id: ent_paper_zhang_dreamvla_a_vision_language_act_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge'
  zh: DreamVLA
  ko: 'DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge'
summary:
  en: 'DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge (DreamVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University, Eastern Institute of Technology, Tsinghua
    University, Galbot, Peking University, University of Illinois at Urbana-Champaign, University of Science and Technology
    of China.'
  zh: DreamVLA 是上海交通大学、东方理工、清华大学、Galbot、北京大学、伊利诺伊大学厄巴纳-香槟分校、中国科学技术大学于 2025 年联合提出的视觉-语言-动作模型。其核心贡献在于通过动态区域引导的世界知识预测，整合动态、空间与语义信息，构建感知-预测-动作循环，显著提升机器人操作任务的泛化能力。在真实机器人任务上达到
    76.7% 成功率，在 CALVIN ABC-D 基准上平均任务长度达 4.44。
  ko: 'DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge (DreamVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University, Eastern Institute of Technology, Tsinghua
    University, Galbot, Peking University, University of Illinois at Urbana-Champaign, University of Science and Technology
    of China.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dreamvla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.04447v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (834 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge (arXiv)'
  url: https://arxiv.org/abs/2507.04447
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DreamVLA source
  url: https://doi.org/10.48550/arXiv.2507.04447
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
DreamVLA 针对现有视觉-语言-动作模型依赖图像预测、信息冗余且缺乏关键世界知识（如动态、空间与语义信息）的局限，提出一种新型框架。该框架通过动态区域引导的世界知识预测，结合空间与语义线索，为动作规划提供紧凑且全面的表示，模拟人类先形成抽象多模态推理链再行动的过程。训练中采用块状结构化注意力机制，防止动态、空间与语义信息相互干扰，保持各表示清晰解耦。同时，利用基于扩散的 Transformer 将动作表示从共享潜在特征中分离，建模未来动作的条件分布。

## 核心内容
### 方法架构
DreamVLA 的核心是感知-预测-动作循环，包含三个关键模块：
- **动态区域引导的世界知识预测**：通过动态区域定位，提取紧凑的时空特征，避免冗余图像信息。
- **空间与语义线索整合**：将空间位置与语义标签融入预测，形成多模态推理链，指导动作生成。
- **块状结构化注意力机制**：在训练中屏蔽动态、空间与语义信息之间的相互注意力，防止信息泄露，确保各表示独立解耦。

### 动作建模
采用扩散式 Transformer 架构，将动作表示从共享潜在特征中分离，通过条件扩散过程建模未来动作的分布。该设计使模型能基于预测的世界知识生成精确的动作序列。

### 实验设置与结果
- **真实机器人任务**：在多种操作场景（如抓取、放置、组装）中测试，DreamVLA 达到 76.7% 成功率，显著优于基线模型。
- **CALVIN ABC-D 基准**：在模拟环境中评估连续任务完成能力，平均任务长度达 4.44，表明其长期规划能力。
- **消融实验**：移除动态区域引导或块状注意力机制后，成功率下降 10-15%，验证了各组件的有效性。

### 结论
DreamVLA 通过整合全面世界知识预测，有效解决了现有 VLA 模型的信息冗余与知识缺失问题，在真实与模拟环境中均展现出优越性能。未来工作可探索更复杂的动态场景与多机器人协作。

## Overview
Recent advances in vision-language-action (VLA) models have shown promise in integrating image generation with action prediction to improve generalization and reasoning in robot manipulation. However, existing methods are limited to challenging image-based forecasting, which suffers from redundant information and lacks comprehensive and critical world knowledge, including dynamic, spatial and semantic information. To address these limitations, we propose DreamVLA, a novel VLA framework that integrates comprehensive world knowledge forecasting to enable inverse dynamics modeling, thereby establishing a perception-prediction-action loop for manipulation tasks. Specifically, DreamVLA introduces a dynamic-region-guided world knowledge prediction, integrated with the spatial and semantic cues, which provide compact yet comprehensive representations for action planning. This design aligns with how humans interact with the world by first forming abstract multimodal reasoning chains before acting. To mitigate interference among the dynamic, spatial and semantic information during training, we adopt a block-wise structured attention mechanism that masks their mutual attention, preventing information leakage and keeping each representation clean and disentangled. Moreover, to model the conditional distribution over future actions, we employ a diffusion-based transformer that disentangles action representations from shared latent features. Extensive experiments on both real-world and simulation environments demonstrate that DreamVLA achieves 76.7% success rate on real robot tasks and 4.44 average length on the CALVIN ABC-D benchmarks.

## 参考
- http://arxiv.org/abs/2507.04447v3

## 개요
DreamVLA는 기존 비전-언어-행동 모델이 이미지 예측에 의존하고, 정보가 중복되며, 동적·공간·의미 정보와 같은 핵심 세계 지식이 부족하다는 한계를 해결하기 위해 새로운 프레임워크를 제안한다. 이 프레임워크는 동적 영역 유도 세계 지식 예측을 통해 공간 및 의미 단서를 결합하여 행동 계획에 간결하고 포괄적인 표현을 제공하며, 인간이 먼저 추상적 다중 모달 추론 체인을 형성한 후 행동하는 과정을 모사한다. 훈련에서는 블록 구조적 주의 메커니즘을 사용하여 동적·공간·의미 정보가 서로 간섭하지 않도록 하고 각 표현을 명확하게 분리한다. 또한 확산 기반 Transformer를 활용하여 행동 표현을 공유 잠재 특징에서 분리하고 미래 행동의 조건부 분포를 모델링한다.

## 핵심 내용
### 방법 아키텍처
DreamVLA의 핵심은 인식-예측-행동 루프로, 세 가지 주요 모듈을 포함한다:
- **동적 영역 유도 세계 지식 예측**: 동적 영역 위치 파악을 통해 간결한 시공간 특징을 추출하고 중복 이미지 정보를 방지한다.
- **공간 및 의미 단서 통합**: 공간 위치와 의미 레이블을 예측에 통합하여 다중 모달 추론 체인을 형성하고 행동 생성을 안내한다.
- **블록 구조적 주의 메커니즘**: 훈련 중 동적·공간·의미 정보 간의 상호 주의를 차단하여 정보 누출을 방지하고 각 표현의 독립적 분리를 보장한다.

### 행동 모델링
확산 기반 Transformer 아키텍처를 채택하여 행동 표현을 공유 잠재 특징에서 분리하고, 조건부 확산 과정을 통해 미래 행동의 분포를 모델링한다. 이 설계는 모델이 예측된 세계 지식을 기반으로 정밀한 행동 시퀀스를 생성할 수 있게 한다.

### 실험 설정 및 결과
- **실제 로봇 작업**: 다양한 조작 시나리오(예: 파지, 배치, 조립)에서 테스트한 결과, DreamVLA는 76.7%의 성공률을 달성하여 기준 모델보다 크게 우수했다.
- **CALVIN ABC-D 벤치마크**: 시뮬레이션 환경에서 연속 작업 완료 능력을 평가한 결과, 평균 작업 길이가 4.44에 달해 장기 계획 능력을 보여주었다.
- **절제 실험**: 동적 영역 유도 또는 블록 주의 메커니즘을 제거하면 성공률이 10-15% 하락하여 각 구성 요소의 유효성을 검증했다.

### 결론
DreamVLA는 포괄적인 세계 지식 예측을 통합하여 기존 VLA 모델의 정보 중복 및 지식 부족 문제를 효과적으로 해결하며, 실제 및 시뮬레이션 환경 모두에서 우수한 성능을 입증했다. 향후 연구에서는 더 복잡한 동적 시나리오와 다중 로봇 협업을 탐구할 수 있다.

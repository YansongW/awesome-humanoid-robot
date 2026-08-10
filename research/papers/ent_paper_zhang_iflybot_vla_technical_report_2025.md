---
$id: ent_paper_zhang_iflybot_vla_technical_report_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: iFlyBot-VLA Technical Report
  zh: iFlyBot-VLA
  ko: iFlyBot-VLA Technical Report
summary:
  en: iFlyBot-VLA Technical Report (iFlyBot-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by iFlyTek Reasearch and Development Group, LindenBot.
  zh: iFlyBot-VLA 是 iFlyTek 研发团队与 LindenBot 于 2025 年提出的大型视觉-语言-动作模型，专为机器人操作任务设计。其核心贡献包括：基于大规模人类与机器人操作视频训练的隐式动作模型、联合监督视觉语言模型与动作专家的双层动作表征框架，以及融合机器人轨迹数据与通用/空间问答数据的混合训练策略。
  ko: iFlyBot-VLA Technical Report (iFlyBot-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by iFlyTek Reasearch and Development Group, LindenBot.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- iflybot_vla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.01914v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (667 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: iFlyBot-VLA Technical Report (arXiv)
  url: https://arxiv.org/abs/2511.01914
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: iFlyBot-VLA source
  url: https://doi.org/10.48550/arXiv.2511.01914
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
iFlyBot-VLA 通过创新框架解决了视觉-语言-动作模型中的动作表征与对齐问题。该模型首先利用跨实体操作数据预训练隐式动作模型，捕捉高层操作意图；同时通过频域变换将连续控制信号转化为结构化离散动作令牌，编码底层动力学信息。这种双层监督机制使视觉语言模型能够直接参与动作生成，对齐语言、视觉与动作的表示空间。在 LIBERO Franka 基准测试中，该框架展现出优越性能，真实环境实验也验证了其在多样化复杂操作任务中的竞争力。

## 核心内容
### 方法架构
iFlyBot-VLA 采用三阶段训练框架：
- **隐式动作模型预训练**：在大规模人类与机器人操作视频上训练，学习跨实体操作数据中的高层意图表征。
- **双层动作表征**：
  - **隐式动作**：从预训练模型提取，捕捉隐含的高层操作意图。
  - **结构化离散动作令牌**：通过频域变换处理连续控制信号，编码明确的底层动力学信息。
- **混合训练策略**：联合使用机器人轨迹数据、通用问答数据集与空间问答数据集，增强视觉语言模型骨干的 3D 感知与推理能力。

### 实验设置与结果
- **基准测试**：在 LIBERO Franka 基准上验证框架优越性。
- **真实环境评估**：在多样化复杂操作任务中取得具有竞争力的成功率。
- **开源计划**：将开源部分自建数据集以支持社区研究。

### 关键结论
双层监督机制有效对齐语言、视觉与动作的表示空间，使视觉语言模型能直接贡献于动作生成，显著提升操作任务的泛化能力与成功率。

## Overview
We introduce iFlyBot-VLA, a large-scale Vision-Language-Action (VLA) model trained under a novel framework. The main contributions are listed as follows: (1) a latent action model thoroughly trained on large-scale human and robotic manipulation videos; (2) a dual-level action representation framework that jointly supervises both the Vision-Language Model (VLM) and the action expert during training; (3) a mixed training strategy that combines robot trajectory data with general QA and spatial QA datasets, effectively enhancing the 3D perceptual and reasoning capabilities of the VLM backbone. Specifically, the VLM is trained to predict two complementary forms of actions: latent actions, derived from our latent action model pretrained on cross-embodiment manipulation data, which capture implicit high-level intentions; and structured discrete action tokens, obtained through frequency-domain transformations of continuous control signals, which encode explicit low-level dynamics. This dual supervision aligns the representation spaces of language, vision, and action, enabling the VLM to directly contribute to action generation. Experimental results on the LIBERO Franka benchmark demonstrate the superiority of our frame-work, while real-world evaluations further show that iFlyBot-VLA achieves competitive success rates across diverse and challenging manipulation tasks. Furthermore, we plan to open-source a portion of our self-constructed dataset to support future research in the community

## Overview
We introduce iFlyBot-VLA, a large-scale Vision-Language-Action (VLA) model trained under a novel framework. The main contributions are listed as follows: (1) a latent action model thoroughly trained on large-scale human and robotic manipulation videos; (2) a dual-level action representation framework that jointly supervises both the Vision-Language Model (VLM) and the action expert during training; (3) a mixed training strategy that combines robot trajectory data with general QA and spatial QA datasets, effectively enhancing the 3D perceptual and reasoning capabilities of the VLM backbone. Specifically, the VLM is trained to predict two complementary forms of actions: latent actions, derived from our latent action model pretrained on cross-embodiment manipulation data, which capture implicit high-level intentions; and structured discrete action tokens, obtained through frequency-domain transformations of continuous control signals, which encode explicit low-level dynamics. This dual supervision aligns the representation spaces of language, vision, and action, enabling the VLM to directly contribute to action generation. Experimental results on the LIBERO Franka benchmark demonstrate the superiority of our framework, while real-world evaluations further show that iFlyBot-VLA achieves competitive success rates across diverse and challenging manipulation tasks. Furthermore, we plan to open-source a portion of our self-constructed dataset to support future research in the community.

## Content
We introduce iFlyBot-VLA, a large-scale Vision-Language-Action (VLA) model trained under a novel framework. The main contributions are listed as follows: (1) a latent action model thoroughly trained on large-scale human and robotic manipulation videos; (2) a dual-level action representation framework that jointly supervises both the Vision-Language Model (VLM) and the action expert during training; (3) a mixed training strategy that combines robot trajectory data with general QA and spatial QA datasets, effectively enhancing the 3D perceptual and reasoning capabilities of the VLM backbone. Specifically, the VLM is trained to predict two complementary forms of actions: latent actions, derived from our latent action model pretrained on cross-embodiment manipulation data, which capture implicit high-level intentions; and structured discrete action tokens, obtained through frequency-domain transformations of continuous control signals, which encode explicit low-level dynamics. This dual supervision aligns the representation spaces of language, vision, and action, enabling the VLM to directly contribute to action generation. Experimental results on the LIBERO Franka benchmark demonstrate the superiority of our framework, while real-world evaluations further show that iFlyBot-VLA achieves competitive success rates across diverse and challenging manipulation tasks. Furthermore, we plan to open-source a portion of our self-constructed dataset to support future research in the community.

## 参考
- http://arxiv.org/abs/2511.01914v1

## 개요
iFlyBot-VLA는 혁신적인 프레임워크를 통해 비전-언어-동작 모델에서의 동작 표현과 정렬 문제를 해결합니다. 이 모델은 먼저 교차 개체 조작 데이터를 활용하여 암시적 동작 모델을 사전 학습하고, 높은 수준의 조작 의도를 포착합니다. 동시에 주파수 영역 변환을 통해 연속 제어 신호를 구조화된 이산 동작 토큰으로 변환하여 하위 수준의 동역학 정보를 인코딩합니다. 이러한 이중 감독 메커니즘은 비전-언어 모델이 동작 생성에 직접 참여할 수 있게 하여 언어, 비전, 동작의 표현 공간을 정렬합니다. LIBERO Franka 벤치마크에서 이 프레임워크는 우수한 성능을 보여주었으며, 실제 환경 실험에서도 다양한 복잡한 조작 작업에서 경쟁력 있는 성능을 검증했습니다.

## 핵심 내용
### 방법 아키텍처
iFlyBot-VLA는 3단계 훈련 프레임워크를 채택합니다:
- **암시적 동작 모델 사전 학습**: 대규모 인간 및 로봇 조작 비디오에서 훈련하여 교차 개체 조작 데이터에서 높은 수준의 의도 표현을 학습합니다.
- **이중 동작 표현**:
  - **암시적 동작**: 사전 학습 모델에서 추출하여 숨겨진 높은 수준의 조작 의도를 포착합니다.
  - **구조화된 이산 동작 토큰**: 주파수 영역 변환을 통해 연속 제어 신호를 처리하여 명확한 하위 수준의 동역학 정보를 인코딩합니다.
- **혼합 훈련 전략**: 로봇 궤적 데이터, 일반 질의응답 데이터셋, 공간 질의응답 데이터셋을 함께 사용하여 비전-언어 모델 백본의 3D 인식 및 추론 능력을 강화합니다.

### 실험 설정 및 결과
- **벤치마크 테스트**: LIBERO Franka 벤치마크에서 프레임워크의 우수성을 검증합니다.
- **실제 환경 평가**: 다양한 복잡한 조작 작업에서 경쟁력 있는 성공률을 달성합니다.
- **오픈소스 계획**: 커뮤니티 연구를 지원하기 위해 일부 자체 구축 데이터셋을 오픈소스로 공개할 예정입니다.

### 핵심 결론
이중 감독 메커니즘은 언어, 비전, 동작의 표현 공간을 효과적으로 정렬하여 비전-언어 모델이 동작 생성에 직접 기여할 수 있게 하고, 조작 작업의 일반화 능력과 성공률을 크게 향상시킵니다.

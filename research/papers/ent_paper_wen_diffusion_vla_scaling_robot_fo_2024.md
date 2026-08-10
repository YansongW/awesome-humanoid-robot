---
$id: ent_paper_wen_diffusion_vla_scaling_robot_fo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression'
  zh: Diffusion-VLA
  ko: 'Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression'
summary:
  en: 'Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression (Diffusion-VLA), is a 2024
    large vision-language-action model for robotic manipulation, introduced by East China Normal University, Midea Group,
    Shanghai University, and published at ICML25.'
  zh: Diffusion-VLA 是由华东师范大学、美的集团和上海大学联合提出的视觉-语言-动作大模型，发表于 ICML25。其核心创新在于将自回归模型与扩散模型统一，通过下一词元预测实现推理，再以扩散模型生成鲁棒动作，并引入推理注入模块增强策略学习。实验表明，该模型在零样本分拣任务中达到
    63.7% 准确率，最小版本在 A6000 GPU 上运行速度达 82Hz。
  ko: 'Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression (Diffusion-VLA), is a 2024
    large vision-language-action model for robotic manipulation, introduced by East China Normal University, Midea Group,
    Shanghai University, and published at ICML25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- diffusion_vla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.03293v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (693 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression (arXiv)'
  url: https://arxiv.org/abs/2412.03293
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Diffusion-VLA source
  url: https://doi.org/10.48550/arXiv.2412.03293
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Diffusion-VLA 提出了一种结合自回归与扩散模型的统一框架，用于学习视觉运动策略。模型首先通过下一词元预测目标对用户查询和当前观测进行推理，随后利用扩散模型生成稳健的动作输出。为提升策略学习的自我推理能力，作者设计了推理注入模块，将推理短语直接融入策略学习过程。该框架简单灵活，易于部署和升级，并在多个真实机器人任务中验证了有效性，包括挑战性的工厂分拣任务和零样本分拣任务。

## 核心内容
### 方法架构
- **核心框架**：Diffusion-VLA 将自回归模型与扩散模型无缝结合，采用下一词元预测目标进行推理，再通过扩散模型生成动作输出。
- **推理注入模块**：创新性地将推理短语直接集成到策略学习过程中，增强模型的可解释性，使观察者能理解模型的思考过程并识别策略失败原因。

### 实验设置与结果
- **工厂分拣任务**：成功对物体进行分类，包括训练中未见过的物体，验证了模型的泛化能力。
- **零样本分拣任务**：在 102 个未见物体上达到 63.7% 的准确率，展示了强大的零样本学习能力。
- **鲁棒性测试**：对视觉变化（如干扰物和新背景）表现出鲁棒性，并能轻松适应新本体。
- **指令跟随与对话**：能够遵循新颖指令并保持对话能力。

### 关键参数与扩展
- **数据效率与推理速度**：最小版本 Diffusion-VLA-2B 在单张 A6000 GPU 上运行速度达 82Hz，复杂任务仅需不到 50 个演示即可从头训练。
- **模型扩展**：参数规模从 2B 扩展到 72B，随着模型增大，泛化能力显著提升。

## Overview
In this paper, we present DiffusionVLA, a novel framework that seamlessly combines the autoregression model with the diffusion model for learning visuomotor policy. Central to our approach is a next-token prediction objective, enabling the model to reason effectively over the user's query in the context of current observations. Subsequently, a diffusion model is attached to generate robust action outputs. To enhance policy learning through self-reasoning, we introduce a novel reasoning injection module that integrates reasoning phrases directly into the policy learning process. The whole framework is simple and flexible, making it easy to deploy and upgrade. We conduct extensive experiments using multiple real robots to validate the effectiveness of DiffusionVLA. Our tests include a challenging factory sorting task, where DiffusionVLA successfully categorizes objects, including those not seen during training. We observe that the reasoning module makes the model interpretable. It allows observers to understand the model thought process and identify potential causes of policy failures. Additionally, we test DiffusionVLA on a zero-shot bin-picking task, achieving 63.7\% accuracy on 102 previously unseen objects. Our method demonstrates robustness to visual changes, such as distractors and new backgrounds, and easily adapts to new embodiments. Furthermore, DiffusionVLA can follow novel instructions and retain conversational ability. Notably, DiffusionVLA is data-efficient and fast at inference; our smallest DiffusionVLA-2B runs 82Hz on a single A6000 GPU and can train from scratch on less than 50 demonstrations for a complex task. Finally, we scale the model from 2B to 72B parameters, showcasing improved generalization capabilities with increased model size.

## 参考
- http://arxiv.org/abs/2412.03293v3

## 개요
Diffusion-VLA는 자기회귀 모델과 확산 모델을 결합한 통합 프레임워크를 제안하여 시각 운동 정책을 학습합니다. 모델은 먼저 다음 토큰 예측 목표를 통해 사용자 쿼리와 현재 관측을 추론한 후, 확산 모델을 활용해 견고한 행동 출력을 생성합니다. 정책 학습의 자기 추론 능력을 향상시키기 위해, 저자들은 추론 주입 모듈을 설계하여 추론 문구를 정책 학습 과정에 직접 통합했습니다. 이 프레임워크는 간단하고 유연하며 배포와 업그레이드가 용이하고, 여러 실제 로봇 작업(도전적인 공장 분류 작업 및 제로샷 분류 작업 포함)에서 효율성을 검증했습니다.

## 핵심 내용
### 방법 아키텍처
- **핵심 프레임워크**: Diffusion-VLA는 자기회귀 모델과 확산 모델을 원활하게 결합하며, 다음 토큰 예측 목표를 사용해 추론한 후 확산 모델을 통해 행동 출력을 생성합니다.
- **추론 주입 모듈**: 추론 문구를 정책 학습 과정에 직접 통합하는 혁신적인 접근 방식으로, 모델의 해석 가능성을 높여 관찰자가 모델의 사고 과정을 이해하고 정책 실패 원인을 식별할 수 있게 합니다.

### 실험 설정 및 결과
- **공장 분류 작업**: 훈련 중 보지 못한 객체를 포함한 객체 분류에 성공하여 모델의 일반화 능력을 검증했습니다.
- **제로샷 분류 작업**: 102개의 보지 못한 객체에서 63.7%의 정확도를 달성하여 강력한 제로샷 학습 능력을 입증했습니다.
- **견고성 테스트**: 시각적 변화(예: 방해물 및 새로운 배경)에 대해 견고성을 보였으며, 새로운 본체에 쉽게 적응할 수 있습니다.
- **명령 따르기 및 대화**: 새로운 명령을 따르고 대화 능력을 유지할 수 있습니다.

### 주요 매개변수 및 확장
- **데이터 효율성 및 추론 속도**: 최소 버전인 Diffusion-VLA-2B는 단일 A6000 GPU에서 82Hz 속도로 실행되며, 복잡한 작업은 50개 미만의 데모로 처음부터 훈련할 수 있습니다.
- **모델 확장**: 매개변수 규모가 2B에서 72B로 확장되며, 모델이 커질수록 일반화 능력이 크게 향상됩니다.

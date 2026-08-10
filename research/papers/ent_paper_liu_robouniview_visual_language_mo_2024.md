---
$id: ent_paper_liu_robouniview_visual_language_mo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboUniView: Visual-Language Model with Unified View Representation for Robotic Manipulation'
  zh: RoboUniView
  ko: 'RoboUniView: Visual-Language Model with Unified View Representation for Robotic Manipulation'
summary:
  en: 'RoboUniView: Visual-Language Model with Unified View Representation for Robotic Manipulation (RoboUniView), is a 2024
    generalized vision-language-action model for robotic manipulation, introduced by Meituan.'
  zh: RoboUniView 是美团于 2024 年提出的通用视觉-语言-动作模型，用于机器人操作。其核心贡献在于将视觉特征提取与动作学习解耦，通过学习统一视角表示来消除不同机器人平台因相机参数差异导致的性能差距。该方法在 CALVIN
    基准上取得了最先进的结果，并在未见过的相机参数下展现出卓越的适应性。
  ko: 'RoboUniView: Visual-Language Model with Unified View Representation for Robotic Manipulation (RoboUniView), is a 2024
    generalized vision-language-action model for robotic manipulation, introduced by Meituan.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- robotic_manipulation
- robouniview
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.18977v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (951 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'RoboUniView: Visual-Language Model with Unified View Representation for Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2406.18977
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RoboUniView source
  url: https://doi.org/10.48550/arXiv.2406.18977
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
利用视觉-语言模型进行机器人操作是一个新兴范式，但现有方法因相机规格和安装位置不同而在不同平台上表现差异显著。RoboUniView 通过创新地解耦视觉特征提取与动作学习来解决这一挑战：首先利用易获取的数据进行预训练，从多视角观测中学习一个统一视角表示，再基于该表示推导出控制机器人操作的动作。这种统一视角表示更准确地反映了物理世界，且不受机器人平台相机参数的约束。该方法在 CALVIN 基准上实现了最先进的性能，并展现出对未见相机参数的强大适应性和跨数据集联合学习能力。

## 核心内容
### 方法概述
RoboUniView 的核心思想是将视觉特征提取与动作学习过程解耦。具体而言，模型首先通过预训练，从多视角图像中学习一个与相机参数无关的统一视角表示（Unified View Representation）。该表示旨在更准确地反映物理世界的状态，随后被用于推导机器人操作的动作指令。

### 架构设计
- **统一视角表示学习**：模型利用易于获取的多视角数据进行预训练，学习如何将不同相机视角下的观测映射到一个共享的、与平台无关的表示空间。
- **动作学习**：在获得统一视角表示后，模型基于该表示进行动作预测，从而控制机器人执行具体操作任务。由于动作学习阶段不再直接依赖原始相机参数，模型对不同平台的泛化能力得到显著提升。

### 实验设置与关键结果
- **基准测试**：在极具挑战性的 CALVIN 基准上进行评估。
- **性能提升**：
  - 在 $D \to D$ 设置下，成功率从 93.0% 提升至 96.2%。
  - 在 $ABC \to D$ 设置下，成功率从 92.2% 提升至 94.2%。
- **适应性验证**：
  - 在未见过的相机参数下，模型仍能保持高性能。
  - 能够利用具有不同相机参数的多个数据集进行训练。
  - 支持跨数据集的联合跨任务学习。

### 结论
RoboUniView 通过解耦视觉特征与动作学习，并引入统一视角表示，有效解决了机器人操作中因相机参数差异导致的泛化问题。该方法在 CALVIN 基准上取得了最先进的结果，并展现出卓越的适应性和灵活性，为构建更通用的机器人操作模型提供了新思路。代码已开源。

## Overview
Utilizing Vision-Language Models (VLMs) for robotic manipulation represents a novel paradigm, aiming to enhance the model's ability to generalize to new objects and instructions. However, due to variations in camera specifications and mounting positions, existing methods exhibit significant performance disparities across different robotic platforms. To address this challenge, we propose RoboUniView in this paper, an innovative approach that decouples visual feature extraction from action learning. We first learn a unified view representation from multi-perspective views by pre-training on readily accessible data, and then derive actions from this unified view representation to control robotic manipulation. This unified view representation more accurately mirrors the physical world and is not constrained by the robotic platform's camera parameters. Thanks to this methodology, we achieve state-of-the-art performance on the demanding CALVIN benchmark, enhancing the success rate in the $D \to D$ setting from 93.0% to 96.2%, and in the $ABC \to D$ setting from 92.2% to 94.2%. Moreover, our model exhibits outstanding adaptability and flexibility: it maintains high performance under unseen camera parameters, can utilize multiple datasets with varying camera parameters, and is capable of joint cross-task learning across datasets. Code is provided for re-implementation. https://github.com/liufanfanlff/RoboUniview

## 参考
- http://arxiv.org/abs/2406.18977v3

## 개요
시각-언어 모델을 활용한 로봇 조작은 새로운 패러다임으로 떠오르고 있지만, 기존 방법들은 카메라 사양과 설치 위치에 따라 플랫폼 간 성능 차이가 두드러진다. RoboUniView는 시각 특징 추출과 행동 학습을 혁신적으로 분리하여 이 문제를 해결한다: 먼저 쉽게 얻을 수 있는 데이터로 사전 학습을 수행하여 다중 시점 관측에서 통합 시점 표현을 학습하고, 이를 기반으로 로봇 조작을 위한 행동을 도출한다. 이러한 통합 시점 표현은 물리적 세계를 더 정확히 반영하며, 로봇 플랫폼의 카메라 매개변수에 구속되지 않는다. 이 방법은 CALVIN 벤치마크에서 최첨단 성능을 달성했으며, 보지 못한 카메라 매개변수에 대한 강력한 적응성과 교차 데이터셋 공동 학습 능력을 보여준다.

## 핵심 내용
### 방법 개요
RoboUniView의 핵심 아이디어는 시각 특징 추출과 행동 학습 과정을 분리하는 것이다. 구체적으로, 모델은 먼저 사전 학습을 통해 다중 시점 이미지에서 카메라 매개변수와 무관한 통합 시점 표현(Unified View Representation)을 학습한다. 이 표현은 물리적 세계의 상태를 더 정확히 반영하도록 설계되었으며, 이후 로봇 조작을 위한 행동 명령을 도출하는 데 사용된다.

### 아키텍처 설계
- **통합 시점 표현 학습**: 모델은 쉽게 얻을 수 있는 다중 시점 데이터로 사전 학습을 수행하여, 서로 다른 카메라 시점의 관측을 공유되고 플랫폼에 독립적인 표현 공간에 매핑하는 방법을 학습한다.
- **행동 학습**: 통합 시점 표현을 획득한 후, 모델은 이 표현을 기반으로 행동을 예측하여 로봇이 구체적인 조작 작업을 수행하도록 제어한다. 행동 학습 단계에서 더 이상 원시 카메라 매개변수에 직접 의존하지 않으므로, 모델의 다양한 플랫폼에 대한 일반화 능력이 크게 향상된다.

### 실험 설정 및 주요 결과
- **벤치마크 테스트**: 매우 도전적인 CALVIN 벤치마크에서 평가를 수행했다.
- **성능 향상**:
  - $D \to D$ 설정에서 성공률이 93.0%에서 96.2%로 향상되었다.
  - $ABC \to D$ 설정에서 성공률이 92.2%에서 94.2%로 향상되었다.
- **적응성 검증**:
  - 보지 못한 카메라 매개변수에서도 모델이 높은 성능을 유지한다.
  - 서로 다른 카메라 매개변수를 가진 여러 데이터셋을 활용하여 학습할 수 있다.
  - 교차 데이터셋 공동 교차 작업 학습을 지원한다.

### 결론
RoboUniView는 시각 특징과 행동 학습을 분리하고 통합 시점 표현을 도입함으로써, 로봇 조작에서 카메라 매개변수 차이로 인한 일반화 문제를 효과적으로 해결한다. 이 방법은 CALVIN 벤치마크에서 최첨단 결과를 달성했으며, 뛰어난 적응성과 유연성을 보여줌으로써 더 범용적인 로봇 조작 모델을 구축하는 새로운 방향을 제시한다. 코드는 오픈소스로 공개되었다.

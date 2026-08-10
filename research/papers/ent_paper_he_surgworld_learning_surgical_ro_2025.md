---
$id: ent_paper_he_surgworld_learning_surgical_ro_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SurgWorld: Learning Surgical Robot Policies from Videos via World Modeling'
  zh: SurgWorld
  ko: 'SurgWorld: Learning Surgical Robot Policies from Videos via World Modeling'
summary:
  en: 'SurgWorld: Learning Surgical Robot Policies from Videos via World Modeling (SurgWorld), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NVIDIA, The Chinese University of Hong Kong, Sung Kyun Kwan University,
    Wenzhou Medical University, National University of Singapore, Ruijin Hospital.'
  zh: SurgWorld 是 NVIDIA 等机构于 2025 年提出的大型视觉-语言-动作模型，旨在通过世界模型解决手术机器人数据稀缺问题。其核心贡献在于利用 Cosmos-H-Surgical 世界模型生成合成手术视频，并首次采用逆动力学模型推断伪运动学数据，从而训练出性能显著优于仅用真实数据训练的
    VLA 策略。
  ko: 'SurgWorld: Learning Surgical Robot Policies from Videos via World Modeling (SurgWorld), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NVIDIA, The Chinese University of Hong Kong, Sung Kyun Kwan University,
    Wenzhou Medical University, National University of Singapore, Ruijin Hospital.'
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
- surgworld
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.23162v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (805 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'SurgWorld: Learning Surgical Robot Policies from Videos via World Modeling (arXiv)'
  url: https://arxiv.org/abs/2512.23162
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SurgWorld source
  url: https://doi.org/10.48550/arXiv.2512.23162
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
手术机器人领域因缺乏同时包含视觉观测和精确运动学数据的配对数据集，难以直接应用模仿学习或 VLA 模型训练。SurgWorld 通过构建 Cosmos-H-Surgical 世界模型（基于物理 AI 世界模型和 SATA 数据集），生成多样化、可泛化的逼真手术视频。研究团队首次利用逆动力学模型从合成视频中推断伪运动学数据，生成配对视频-动作数据。实验表明，基于这些增强数据训练的手术 VLA 策略在真实机器人平台上表现显著优于仅使用真实演示数据的模型。

## 核心内容
### 方法
- **数据构建**：团队首先创建了 Surgical Action Text Alignment (SATA) 数据集，包含针对手术机器人的详细动作描述。
- **世界模型**：基于最先进的物理 AI 世界模型和 SATA 数据集，构建了 Cosmos-H-Surgical 世界模型，能够生成多样化、可泛化的逼真手术视频。
- **伪运动学推断**：首次采用逆动力学模型从合成手术视频中推断伪运动学数据，生成合成配对视频-动作数据。

### 实验设置
- **训练数据**：使用 Cosmos-H-Surgical 生成的合成视频与 SATA 数据集结合，通过逆动力学模型生成配对数据。
- **基线模型**：与仅使用真实手术演示数据训练的 VLA 模型进行对比。
- **评估平台**：在真实手术机器人平台上进行策略性能评估。

### 关键结果
- 基于增强数据训练的 SurgWorld VLA 策略在真实机器人平台上的表现显著优于仅使用真实演示数据的模型。
- 该方法通过利用大量未标注手术视频和生成式世界建模，为自主手术技能获取提供了可扩展路径。

### 结论
SurgWorld 通过世界模型和逆动力学模型有效缓解了手术机器人数据稀缺问题，为通用且数据高效的手术机器人策略开发开辟了新方向。

## Overview
Data scarcity remains a fundamental barrier to achieving fully autonomous surgical robots. While large scale vision language action (VLA) models have shown impressive generalization in household and industrial manipulation by leveraging paired video action data from diverse domains, surgical robotics suffers from the paucity of datasets that include both visual observations and accurate robot kinematics. In contrast, vast corpora of surgical videos exist, but they lack corresponding action labels, preventing direct application of imitation learning or VLA training. In this work, we aim to alleviate this problem by learning policy models from Cosmos-H-Surgical, a world model designed for surgical physical AI. We curated the Surgical Action Text Alignment (SATA) dataset with detailed action description specifically for surgical robots. Then we built Cosmos-H-Surgical based on the most advanced physical AI world model and SATA. It's able to generate diverse, generalizable and realistic surgery videos. We are also the first to use an inverse dynamics model to infer pseudokinematics from synthetic surgical videos, producing synthetic paired video action data. We demonstrate that a surgical VLA policy trained with these augmented data significantly outperforms models trained only on real demonstrations on a real surgical robot platform. Our approach offers a scalable path toward autonomous surgical skill acquisition by leveraging the abundance of unlabeled surgical video and generative world modeling, thus opening the door to generalizable and data efficient surgical robot policies.

## 参考
- http://arxiv.org/abs/2512.23162v4

## 개요
수술 로봇 분야는 시각적 관측과 정밀한 운동학 데이터를 동시에 포함하는 쌍을 이룬 데이터셋이 부족하여, 모방 학습이나 VLA 모델 훈련을 직접 적용하기 어렵다. SurgWorld는 Cosmos-H-Surgical 세계 모델(물리 AI 세계 모델과 SATA 데이터셋 기반)을 구축하여 다양하고 일반화 가능한 사실적인 수술 비디오를 생성한다. 연구팀은 처음으로 역동역학 모델을 사용하여 합성 비디오에서 의사 운동학 데이터를 추론하고, 쌍을 이룬 비디오-행동 데이터를 생성한다. 실험 결과, 이러한 증강 데이터로 훈련된 수술 VLA 정책은 실제 로봇 플랫폼에서 실제 시연 데이터만 사용한 모델보다 현저히 우수한 성능을 보였다.

## 핵심 내용
### 방법
- **데이터 구축**: 연구팀은 먼저 Surgical Action Text Alignment (SATA) 데이터셋을 생성했으며, 이는 수술 로봇에 대한 상세한 동작 설명을 포함한다.
- **세계 모델**: 최첨단 물리 AI 세계 모델과 SATA 데이터셋을 기반으로 Cosmos-H-Surgical 세계 모델을 구축하여, 다양하고 일반화 가능한 사실적인 수술 비디오를 생성할 수 있다.
- **의사 운동학 추론**: 처음으로 역동역학 모델을 사용하여 합성 수술 비디오에서 의사 운동학 데이터를 추론하고, 합성 쌍 비디오-행동 데이터를 생성한다.

### 실험 설정
- **훈련 데이터**: Cosmos-H-Surgical로 생성된 합성 비디오와 SATA 데이터셋을 결합하고, 역동역학 모델을 통해 쌍 데이터를 생성한다.
- **기준 모델**: 실제 수술 시연 데이터만으로 훈련된 VLA 모델과 비교한다.
- **평가 플랫폼**: 실제 수술 로봇 플랫폼에서 정책 성능을 평가한다.

### 주요 결과
- 증강 데이터로 훈련된 SurgWorld VLA 정책은 실제 로봇 플랫폼에서 실제 시연 데이터만 사용한 모델보다 현저히 우수한 성능을 보였다.
- 이 방법은 대량의 라벨링되지 않은 수술 비디오와 생성적 세계 모델링을 활용하여 자율 수술 기술 습득을 위한 확장 가능한 경로를 제공한다.

### 결론
SurgWorld는 세계 모델과 역동역학 모델을 통해 수술 로봇 데이터 부족 문제를 효과적으로 완화하며, 범용적이고 데이터 효율적인 수술 로봇 정책 개발의 새로운 방향을 제시한다.

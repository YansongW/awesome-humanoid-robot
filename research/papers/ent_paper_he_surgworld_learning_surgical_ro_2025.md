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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.23162v4. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
데이터 부족은 완전 자율 수술 로봇을 구현하는 데 있어 근본적인 장벽으로 남아 있습니다. 다양한 도메인의 짝지어진 비디오-행동 데이터를 활용하여 대규모 시각-언어-행동(VLA) 모델이 가정 및 산업용 조작에서 놀라운 일반화 능력을 보여주고 있지만, 수술 로봇 분야는 시각적 관찰과 정확한 로봇 운동학을 모두 포함하는 데이터셋이 부족한 실정입니다. 반면, 방대한 양의 수술 비디오 코퍼스가 존재하지만, 이에 대응하는 행동 레이블이 없어 모방 학습이나 VLA 훈련을 직접 적용할 수 없습니다. 본 연구에서는 수술 물리 AI를 위해 설계된 세계 모델인 Cosmos-H-Surgical로부터 정책 모델을 학습함으로써 이 문제를 완화하고자 합니다. 우리는 수술 로봇에 특화된 상세한 행동 설명을 포함하는 Surgical Action Text Alignment (SATA) 데이터셋을 구축했습니다. 그런 다음 가장 진보된 물리 AI 세계 모델과 SATA를 기반으로 Cosmos-H-Surgical을 개발했습니다. 이 모델은 다양하고 일반화 가능하며 현실적인 수술 비디오를 생성할 수 있습니다. 또한, 우리는 역동역학 모델을 사용하여 합성 수술 비디오로부터 의사 운동학을 추론하고, 짝지어진 합성 비디오-행동 데이터를 생성한 최초의 사례입니다. 우리는 이러한 증강 데이터로 훈련된 수술 VLA 정책이 실제 수술 로봇 플랫폼에서 실제 시연 데이터만으로 훈련된 모델보다 훨씬 뛰어난 성능을 보임을 입증했습니다. 본 접근법은 레이블이 없는 수술 비디오의 풍부함과 생성적 세계 모델링을 활용하여 자율 수술 기술 습득을 위한 확장 가능한 경로를 제공하며, 이는 일반화 가능하고 데이터 효율적인 수술 로봇 정책의 문을 열어줍니다.

## 핵심 내용
데이터 부족은 완전 자율 수술 로봇을 구현하는 데 있어 근본적인 장벽으로 남아 있습니다. 다양한 도메인의 짝지어진 비디오-행동 데이터를 활용하여 대규모 시각-언어-행동(VLA) 모델이 가정 및 산업용 조작에서 놀라운 일반화 능력을 보여주고 있지만, 수술 로봇 분야는 시각적 관찰과 정확한 로봇 운동학을 모두 포함하는 데이터셋이 부족한 실정입니다. 반면, 방대한 양의 수술 비디오 코퍼스가 존재하지만, 이에 대응하는 행동 레이블이 없어 모방 학습이나 VLA 훈련을 직접 적용할 수 없습니다. 본 연구에서는 수술 물리 AI를 위해 설계된 세계 모델인 Cosmos-H-Surgical로부터 정책 모델을 학습함으로써 이 문제를 완화하고자 합니다. 우리는 수술 로봇에 특화된 상세한 행동 설명을 포함하는 Surgical Action Text Alignment (SATA) 데이터셋을 구축했습니다. 그런 다음 가장 진보된 물리 AI 세계 모델과 SATA를 기반으로 Cosmos-H-Surgical을 개발했습니다. 이 모델은 다양하고 일반화 가능하며 현실적인 수술 비디오를 생성할 수 있습니다. 또한, 우리는 역동역학 모델을 사용하여 합성 수술 비디오로부터 의사 운동학을 추론하고, 짝지어진 합성 비디오-행동 데이터를 생성한 최초의 사례입니다. 우리는 이러한 증강 데이터로 훈련된 수술 VLA 정책이 실제 수술 로봇 플랫폼에서 실제 시연 데이터만으로 훈련된 모델보다 훨씬 뛰어난 성능을 보임을 입증했습니다. 본 접근법은 레이블이 없는 수술 비디오의 풍부함과 생성적 세계 모델링을 활용하여 자율 수술 기술 습득을 위한 확장 가능한 경로를 제공하며, 이는 일반화 가능하고 데이터 효율적인 수술 로봇 정책의 문을 열어줍니다.

## 参考
- http://arxiv.org/abs/2512.23162v4

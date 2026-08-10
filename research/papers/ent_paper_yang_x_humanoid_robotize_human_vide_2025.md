---
$id: ent_paper_yang_x_humanoid_robotize_human_vide_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale'
  zh: X-Humanoid
  ko: 'X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale'
summary:
  en: 'X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale (X-Humanoid), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NUS.'
  zh: X-Humanoid 是新加坡国立大学于 2025 年提出的一种大规模视觉-语言-动作模型，用于人形机器人操控。其核心贡献在于通过生成式视频编辑技术，将互联网上的海量人类视频“机器人化”为人形机器人视频，从而解决训练数据稀缺问题。该方法基于
    Wan 2.2 模型进行微调，并利用虚幻引擎生成了超过 17 小时的配对合成视频，最终产出一个包含 360 万帧的大规模数据集。
  ko: 'X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale (X-Humanoid), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NUS.'
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
- vision_language_action
- vla
- x_humanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.04537v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (839 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale (arXiv)'
  url: https://arxiv.org/abs/2512.04537
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: X-Humanoid source
  url: https://doi.org/10.48550/arXiv.2512.04537
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
X-Humanoid 旨在解决具身智能领域因缺乏大规模、多样化训练数据而导致的进展瓶颈。现有方法主要通过在自我中心视频上“叠加”机械臂来机器人化人类视频，但无法处理第三人称视角下的复杂全身运动和场景遮挡。为此，X-Humanoid 将强大的 Wan 2.2 模型改造为视频到视频结构，并针对“人类到人形机器人”的翻译任务进行微调。为了获取微调所需的配对视频，研究团队设计了一个可扩展的数据创建流程，利用虚幻引擎将社区资产转化为超过 17 小时的配对合成视频。随后，他们将训练好的模型应用于 60 小时的 Ego-Exo4D 视频，生成并发布了包含超过 360 万帧“机器人化”人形机器人视频的新数据集。

## 核心内容
### 方法
X-Humanoid 采用生成式视频编辑方法，将 Wan 2.2 模型适配为视频到视频结构，并针对“人类到人形机器人”的翻译任务进行微调。该方法能够处理第三人称视频中的复杂全身运动和场景遮挡，克服了现有“叠加”机械臂方法的局限性。

### 数据创建流程
为了获得微调所需的配对人类-人形机器人视频，研究团队设计了一个可扩展的数据创建流程：
- 利用虚幻引擎将社区资产转化为超过 17 小时的配对合成视频。
- 这些合成视频为模型提供了高质量的监督信号，使其学会将人类动作映射到人形机器人上。

### 实验设置与结果
- 将训练好的模型应用于 60 小时的 Ego-Exo4D 视频，生成并发布了包含超过 360 万帧“机器人化”人形机器人视频的新数据集。
- 定量分析和用户研究证实了该方法优于现有基线：
  - 69% 的用户认为其在运动一致性方面表现最佳。
  - 62.1% 的用户认为其在具身正确性方面表现最佳。

### 结论
X-Humanoid 通过生成式视频编辑技术，成功将大规模人类视频转化为可用于人形机器人训练的数据，有效缓解了训练数据稀缺的问题。该方法在运动一致性和具身正确性方面均获得了用户的高度认可。

## Overview
The advancement of embodied AI has unlocked significant potential for intelligent humanoid robots. However, progress in both Vision-Language-Action (VLA) models and world models is severely hampered by the scarcity of large-scale, diverse training data. A promising solution is to "robotize" web-scale human videos, which has been proven effective for policy training. However, these solutions mainly "overlay" robot arms to egocentric videos, which cannot handle complex full-body motions and scene occlusions in third-person videos, making them unsuitable for robotizing humans. To bridge this gap, we introduce X-Humanoid, a generative video editing approach that adapts the powerful Wan 2.2 model into a video-to-video structure and finetunes it for the human-to-humanoid translation task. This finetuning requires paired human-humanoid videos, so we designed a scalable data creation pipeline, turning community assets into 17+ hours of paired synthetic videos using Unreal Engine. We then apply our trained model to 60 hours of the Ego-Exo4D videos, generating and releasing a new large-scale dataset of over 3.6 million "robotized" humanoid video frames. Quantitative analysis and user studies confirm our method's superiority over existing baselines: 69% of users rated it best for motion consistency, and 62.1% for embodiment correctness.

## 参考
- http://arxiv.org/abs/2512.04537v1

## 개요
X-Humanoid는 구현 지능 분야에서 대규모·다양한 훈련 데이터 부족으로 인한 발전 병목을 해결하는 것을 목표로 한다. 기존 방법은 주로 자기중심(에고) 비디오에 로봇 팔을 "겹쳐서" 인간 비디오를 로봇화하지만, 제3자 시점에서의 복잡한 전신 움직임과 장면 가림을 처리하지 못한다. 이를 위해 X-Humanoid는 강력한 Wan 2.2 모델을 비디오-투-비디오 구조로 개조하고, "인간-투-휴머노이드" 변환 작업에 맞춰 미세 조정한다. 미세 조정에 필요한 쌍을 이루는 비디오를 확보하기 위해 연구팀은 확장 가능한 데이터 생성 파이프라인을 설계했으며, 언리얼 엔진을 활용해 커뮤니티 자산을 17시간 이상의 쌍을 이루는 합성 비디오로 변환했다. 이후 훈련된 모델을 60시간 분량의 Ego-Exo4D 비디오에 적용하여, 360만 프레임 이상의 "로봇화된" 휴머노이드 비디오를 포함하는 새로운 데이터셋을 생성하고 공개했다.

## 핵심 내용
### 방법
X-Humanoid는 생성적 비디오 편집 방식을 채택하여 Wan 2.2 모델을 비디오-투-비디오 구조로 적응시키고, "인간-투-휴머노이드" 변환 작업에 맞춰 미세 조정한다. 이 방법은 제3자 시점 비디오에서의 복잡한 전신 움직임과 장면 가림을 처리할 수 있어, 기존의 "로봇 팔 겹치기" 방식의 한계를 극복한다.

### 데이터 생성 파이프라인
미세 조정에 필요한 쌍을 이루는 인간-휴머노이드 비디오를 확보하기 위해 연구팀은 확장 가능한 데이터 생성 파이프라인을 설계했다:
- 언리얼 엔진을 활용해 커뮤니티 자산을 17시간 이상의 쌍을 이루는 합성 비디오로 변환한다.
- 이러한 합성 비디오는 모델에게 고품질의 감독 신호를 제공하여, 인간의 동작을 휴머노이드에 매핑하는 방법을 학습하게 한다.

### 실험 설정 및 결과
- 훈련된 모델을 60시간 분량의 Ego-Exo4D 비디오에 적용하여, 360만 프레임 이상의 "로봇화된" 휴머노이드 비디오를 포함하는 새로운 데이터셋을 생성하고 공개했다.
- 정량적 분석과 사용자 연구를 통해 기존 기준선보다 우수함을 확인했다:
  - 69%의 사용자가 운동 일관성 측면에서 가장 우수하다고 평가했다.
  - 62.1%의 사용자가 구현 정확성 측면에서 가장 우수하다고 평가했다.

### 결론
X-Humanoid는 생성적 비디오 편집 기술을 통해 대규모 인간 비디오를 휴머노이드 훈련에 사용할 수 있는 데이터로 성공적으로 변환하여, 훈련 데이터 부족 문제를 효과적으로 완화했다. 이 방법은 운동 일관성과 구현 정확성 모두에서 사용자들의 높은 평가를 받았다.

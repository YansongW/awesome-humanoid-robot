---
$id: ent_paper_freeform_preference_learning_f_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Freeform Preference Learning for Robotic Manipulation
  zh: Freeform Preference Learning for Robotic Manipulation
  ko: Freeform Preference Learning for Robotic Manipulation
summary:
  en: 'arXiv:2606.32027v1 Announce Type: new Abstract: Reward design remains a central bottleneck for autonomous robot policy
    improvement, especially in long-horizon manipulation tasks where sparse success labels provide too little signal and binary
    preferences collapse many competing notions of quality into one ambiguous signal. We introduce Freeform Preference Learning
    (FPL), a method for learning robot policies from freeform human preferences. Rather than asking annotators which of two
    trajectories is better overall, FPL lets them define natural-language preference axes, such as speed, safety, quality
    of placement, or carefulness, and provide pairwise preferences along each axis. These annotations are used to learn a
    language-conditioned reward model that maps a trajectory and preference label to an axis-specific reward. We use this
    model to train a reward-conditioned policy that optimizes across the multiple human-specified dimensions. Across four
    real-world and two simulated long-horizon manipulation tasks, FPL improves over sparse-reward and binary-preference methods
    by 38 percentage points. Beyond improved performance, FPL learns dense progress signals without explicit subtask segmentation,
    shows compositionality of behavior not present in the data, and allows users to steer the policy towards different behaviors
    at test time without retraining. Blog post with videos available at https://freeform-pl.github.io/fpl.website/'
  zh: Freeform Preference Learning (FPL) 是一种从自由形式人类偏好中学习机器人策略的方法。它允许标注者定义自然语言偏好轴（如速度、安全性）并提供沿各轴的成对偏好，从而学习语言条件奖励模型。在六项长时域操作任务中，FPL
    相比稀疏奖励和二元偏好方法提升了 38 个百分点。
  ko: 'arXiv:2606.32027v1 Announce Type: new Abstract: Reward design remains a central bottleneck for autonomous robot policy
    improvement, especially in long-horizon manipulation tasks where sparse success labels provide too little signal and binary
    preferences collapse many competing notions of quality into one ambiguous signal. We introduce Freeform Preference Learning
    (FPL), a method for learning robot policies from freeform human preferences. Rather than asking annotators which of two
    trajectories is better overall, FPL lets them define natural-language preference axes, such as speed, safety, quality
    of placement, or carefulness, and provide pairwise preferences along each axis. These annotations are used to learn a
    language-conditioned reward model that maps a trajectory and preference label to an axis-specific reward. We use this
    model to train a reward-conditioned policy that optimizes across the multiple human-specified dimensions. Across four
    real-world and two simulated long-horizon manipulation tasks, FPL improves over sparse-reward and binary-preference methods
    by 38 percentage points. Beyond improved performance, FPL learns dense progress signals without explicit subtask segmentation,
    shows compositionality of behavior not present in the data, and allows users to steer the policy towards different behaviors
    at test time without retraining. Blog post with videos available at https://freeform-pl.github.io/fpl.website/'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- freeform_preference_learning_f
- humanoid
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.32027v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Freeform Preference Learning for Robotic Manipulation
  url: https://arxiv.org/abs/2606.32027
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
FPL 解决了奖励设计在长时域操作任务中的瓶颈问题，传统稀疏成功标签信号不足，而二元偏好将多种质量概念混为一谈。该方法让标注者定义自然语言偏好轴（如速度、安全性、放置质量、小心程度），并提供沿各轴的成对偏好，从而学习语言条件奖励模型，将轨迹和偏好标签映射为轴特定奖励。基于此模型训练奖励条件策略，可在多个人类指定维度上优化。在四项真实世界和两项模拟长时域操作任务中，FPL 相比稀疏奖励和二元偏好方法提升了 38 个百分点，并展现出密集进度信号学习、行为组合性以及测试时无需重新训练即可调整策略的能力。

## 核心内容
### 方法
- **核心思想**：FPL 允许标注者定义自然语言偏好轴（如 speed、safety、quality of placement、carefulness），并提供沿各轴的成对偏好，而非整体二元比较。
- **奖励模型**：学习语言条件奖励模型，将轨迹和偏好标签映射为轴特定奖励。
- **策略训练**：基于奖励模型训练奖励条件策略，在多个人类指定维度上优化。

### 实验设置
- **任务**：四项真实世界和两项模拟长时域操作任务。
- **对比方法**：稀疏奖励方法和二元偏好方法。

### 关键结果
- **性能提升**：FPL 相比稀疏奖励和二元偏好方法提升了 38 个百分点。
- **额外优势**：
  - 学习密集进度信号，无需显式子任务分割。
  - 展现数据中不存在的行为组合性。
  - 允许用户在测试时通过调整偏好轴引导策略，无需重新训练。

### 结论
FPL 通过自由形式人类偏好有效解决了长时域操作任务中的奖励设计瓶颈，显著提升了性能并提供了灵活的策略控制能力。

## Overview
Reward design remains a central bottleneck for autonomous robot policy improvement, especially in long-horizon manipulation tasks where sparse success labels provide too little signal and binary preferences collapse many competing notions of quality into one ambiguous signal. We introduce Freeform Preference Learning (FPL), a method for learning robot policies from freeform human preferences. Rather than asking annotators which of two trajectories is better overall, FPL lets them define natural-language preference axes, such as speed, safety, quality of placement, or carefulness, and provide pairwise preferences along each axis. These annotations are used to learn a language-conditioned reward model that maps a trajectory and preference label to an axis-specific reward. We use this model to train a reward-conditioned policy that optimizes across the multiple human-specified dimensions. Across four real-world and two simulated long-horizon manipulation tasks, FPL improves over sparse-reward and binary-preference methods by 38 percentage points. Beyond improved performance, FPL learns dense progress signals without explicit subtask segmentation, shows compositionality of behavior not present in the data, and allows users to steer the policy towards different behaviors at test time without retraining. Blog post with videos available at https://freeform-pl.github.io/fpl.website/

## 개요
보상 설계는 자율 로봇 정책 개선의 핵심 병목으로 남아 있으며, 특히 장기 조작 작업에서 희소 성공 레이블이 너무 적은 신호를 제공하고 이진 선호도가 여러 경쟁적 품질 개념을 하나의 모호한 신호로 축소하는 경우가 많습니다. 우리는 자유 형식 인간 선호도로부터 로봇 정책을 학습하는 방법인 Freeform Preference Learning (FPL)을 소개합니다. FPL은 주석자에게 두 궤적 중 어느 것이 전반적으로 더 나은지 묻는 대신, 속도, 안전성, 배치 품질 또는 신중함과 같은 자연어 선호 축을 정의하고 각 축을 따라 쌍별 선호도를 제공하도록 합니다. 이러한 주석은 궤적과 선호 레이블을 축별 보상에 매핑하는 언어 조건부 보상 모델을 학습하는 데 사용됩니다. 우리는 이 모델을 사용하여 여러 인간이 지정한 차원에 걸쳐 최적화하는 보상 조건부 정책을 훈련합니다. 네 가지 실제 환경과 두 가지 시뮬레이션 장기 조작 작업에서 FPL은 희소 보상 및 이진 선호도 방법보다 38% 포인트 향상됩니다. 성능 향상 외에도 FPL은 명시적 하위 작업 분할 없이 밀집 진행 신호를 학습하고, 데이터에 없는 행동의 구성성을 보여주며, 사용자가 재훈련 없이 테스트 시점에 정책을 다른 행동으로 조정할 수 있게 합니다. 비디오가 포함된 블로그 게시물은 https://freeform-pl.github.io/fpl.website/ 에서 확인할 수 있습니다.

## 핵심 내용
보상 설계는 자율 로봇 정책 개선의 핵심 병목으로 남아 있으며, 특히 장기 조작 작업에서 희소 성공 레이블이 너무 적은 신호를 제공하고 이진 선호도가 여러 경쟁적 품질 개념을 하나의 모호한 신호로 축소하는 경우가 많습니다. 우리는 자유 형식 인간 선호도로부터 로봇 정책을 학습하는 방법인 Freeform Preference Learning (FPL)을 소개합니다. FPL은 주석자에게 두 궤적 중 어느 것이 전반적으로 더 나은지 묻는 대신, 속도, 안전성, 배치 품질 또는 신중함과 같은 자연어 선호 축을 정의하고 각 축을 따라 쌍별 선호도를 제공하도록 합니다. 이러한 주석은 궤적과 선호 레이블을 축별 보상에 매핑하는 언어 조건부 보상 모델을 학습하는 데 사용됩니다. 우리는 이 모델을 사용하여 여러 인간이 지정한 차원에 걸쳐 최적화하는 보상 조건부 정책을 훈련합니다. 네 가지 실제 환경과 두 가지 시뮬레이션 장기 조작 작업에서 FPL은 희소 보상 및 이진 선호도 방법보다 38% 포인트 향상됩니다. 성능 향상 외에도 FPL은 명시적 하위 작업 분할 없이 밀집 진행 신호를 학습하고, 데이터에 없는 행동의 구성성을 보여주며, 사용자가 재훈련 없이 테스트 시점에 정책을 다른 행동으로 조정할 수 있게 합니다. 비디오가 포함된 블로그 게시물은 https://freeform-pl.github.io/fpl.website/ 에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2606.32027v2

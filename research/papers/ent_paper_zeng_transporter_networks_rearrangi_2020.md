---
$id: ent_paper_zeng_transporter_networks_rearrangi_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Transporter Networks: Rearranging the Visual World for Robotic Manipulation'
  zh: Transporter Networks
  ko: 'Transporter Networks: Rearranging the Visual World for Robotic Manipulation'
summary:
  en: 'Transporter Networks: Rearranging the Visual World for Robotic Manipulation (Transporter Networks), is a 2020 generalized
    vision-language-action model for robotic manipulation, introduced by Robotics at Google, and published at CoRL 2020.'
  zh: Transporter Networks 是 Google Robotics 在 CoRL 2020 上提出的一种用于机器人操作的视觉-语言-动作模型。其核心贡献在于通过重新排列深度特征来推断空间位移，无需物体先验知识，在样本效率上比基准方法高出数个数量级。
  ko: 'Transporter Networks: Rearranging the Visual World for Robotic Manipulation (Transporter Networks), is a 2020 generalized
    vision-language-action model for robotic manipulation, introduced by Robotics at Google, and published at CoRL 2020.'
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
- transporter_networks
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2010.14406v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (611 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Transporter Networks source
  url: https://proceedings.mlr.press/v155/zeng21a.html
  date: '2020'
  accessed_at: '2026-07-01'
---
## 概述
Transporter Networks 将机器人操作问题转化为一系列空间位移的预测，通过从视觉输入中提取深度特征并重新排列来推断位移参数。该模型不依赖物体姿态、模型或关键点等先验假设，而是利用空间对称性进行学习。在10个模拟任务上的实验表明，该方法比多种端到端基线方法学习更快、泛化更好，甚至优于使用真实物体姿态的策略。真实世界硬件实验也验证了其有效性。

## 核心内容
### 方法架构
- 将机器人操作建模为空间位移序列，位移对象可以是物体、物体局部或末端执行器。
- Transporter Network 通过重新排列深度特征图来推断位移参数，从而参数化机器人动作。
- 模型不假设物体具有规范姿态、模型或关键点，而是利用空间对称性进行学习。

### 实验设置与结果
- 在10个模拟任务上评估，包括堆叠积木塔、组装包含未见物体的套件、操作可变形绳索、用闭环反馈推动小物体堆等。
- 与多种端到端基线方法对比，包括使用真实物体姿态的策略，Transporter Networks 在样本效率上高出数个数量级。
- 模型能表示复杂的多模态策略分布，并泛化到多步顺序任务以及6自由度抓取放置操作。
- 真实世界硬件实验验证了方法的有效性。

### 结论
Transporter Networks 提供了一种无需物体先验的机器人操作学习框架，通过空间位移推断实现高效学习和泛化。实验视频和代码已开源。

## Overview
Robotic manipulation can be formulated as inducing a sequence of spatial displacements: where the space being moved can encompass an object, part of an object, or end effector. In this work, we propose the Transporter Network, a simple model architecture that rearranges deep features to infer spatial displacements from visual input - which can parameterize robot actions. It makes no assumptions of objectness (e.g. canonical poses, models, or keypoints), it exploits spatial symmetries, and is orders of magnitude more sample efficient than our benchmarked alternatives in learning vision-based manipulation tasks: from stacking a pyramid of blocks, to assembling kits with unseen objects; from manipulating deformable ropes, to pushing piles of small objects with closed-loop feedback. Our method can represent complex multi-modal policy distributions and generalizes to multi-step sequential tasks, as well as 6DoF pick-and-place. Experiments on 10 simulated tasks show that it learns faster and generalizes better than a variety of end-to-end baselines, including policies that use ground-truth object poses. We validate our methods with hardware in the real world. Experiment videos and code are available at https://transporternets.github.io

## 参考
- http://arxiv.org/abs/2010.14406v3

## 개요
Transporter Networks는 로봇 조작 문제를 일련의 공간 변위 예측으로 변환하고, 시각 입력에서 심층 특징을 추출하여 재배열함으로써 변위 매개변수를 추론합니다. 이 모델은 객체 자세, 모델 또는 키포인트와 같은 사전 가정에 의존하지 않고 공간 대칭성을 활용하여 학습합니다. 10개의 시뮬레이션 작업에서의 실험은 이 방법이 여러 엔드투엔드 기준 방법보다 학습이 빠르고 일반화가 더 우수하며, 실제 객체 자세를 사용하는 전략보다도 우수함을 보여줍니다. 실제 하드웨어 실험에서도 그 효과가 검증되었습니다.

## 핵심 내용
### 방법 아키텍처
- 로봇 조작을 공간 변위 시퀀스로 모델링하며, 변위 대상은 객체, 객체의 일부 또는 엔드 이펙터일 수 있습니다.
- Transporter Network는 심층 특징 맵을 재배열하여 변위 매개변수를 추론함으로써 로봇 동작을 매개변수화합니다.
- 모델은 객체가 표준 자세, 모델 또는 키포인트를 가진다고 가정하지 않고 공간 대칭성을 활용하여 학습합니다.

### 실험 설정 및 결과
- 블록 탑 쌓기, 보이지 않는 객체를 포함한 키트 조립, 변형 가능한 로프 조작, 폐루프 피드백을 통한 작은 객체 더미 밀기 등 10개의 시뮬레이션 작업에서 평가되었습니다.
- 실제 객체 자세를 사용하는 전략을 포함한 여러 엔드투엔드 기준 방법과 비교했을 때, Transporter Networks는 샘플 효율성에서 수 배 더 높은 성능을 보였습니다.
- 모델은 복잡한 다중 모드 정책 분포를 표현할 수 있으며, 다단계 순차 작업 및 6자유도 집기-놓기 조작으로 일반화됩니다.
- 실제 하드웨어 실험에서 방법의 효과가 검증되었습니다.

### 결론
Transporter Networks는 객체 사전 지식 없이 로봇 조작을 학습할 수 있는 프레임워크를 제공하며, 공간 변위 추론을 통해 효율적인 학습과 일반화를 달성합니다. 실험 비디오와 코드는 오픈소스로 공개되었습니다.

---
$id: ent_paper_a_systematic_study_of_data_mod_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation
  zh: A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation
  ko: A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation
summary:
  en: A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation is
    a 2026 work on manipulation for humanoid robots.
  zh: 这是一项2026年关于人形机器人操作的大规模实证研究，由多位研究者共同完成。核心贡献在于系统评估了五种不同数据模态（视觉-语言数据、密集语言标注、跨本体机器人数据、人类视频、离散动作token）及训练策略对大型行为模型协同训练效果的影响，并基于4000小时机器人/人类数据和5000万视觉-语言样本训练了89个策略，进行了超过6万次仿真和2835次真实世界评估。
  ko: A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation is
    a 2026 work on manipulation for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- a_systematic_study_of_data_mod
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.01067v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1240 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: A Systematic Study of Data Modalities and Strategies for Co-training Large Behavior Models for Robot Manipulation
    project page
  url: https://co-training-lbm.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
该研究旨在解决大型行为模型因机器人数据覆盖不足而导致的泛化能力受限问题。研究者通过协同训练（co-training）方法，将目标机器人数据与多种异构数据模态结合，系统比较了五种数据模态和单/多阶段训练策略的效果。实验使用了4000小时的机器人及人类操作数据、5000万视觉-语言样本，训练了89个策略，并在超过5.8万次仿真和2835次真实世界评估中验证。结果表明，与视觉-语言数据和跨本体机器人数据协同训练能显著提升模型对分布偏移、未见任务和语言指令的泛化能力，而离散动作token变体则无明显优势。有效模态的组合可产生累积增益，并通过微调快速适应未见的长时程灵巧操作任务。仅使用机器人数据训练会损害视觉-语言模型骨干的视觉语言理解能力，而有效模态的协同训练可恢复这些能力。在仿真基准中，基于协同训练数据学习到的思维链（chain-of-thought）显式条件化动作生成并未提升性能。

## 核心内容
### 研究背景与问题
大型行为模型通过将模仿学习扩展到多任务机器人数据的大规模训练，已展现出强大的灵巧操作能力。然而，其泛化能力受限于机器人数据覆盖不足。为在不增加昂贵数据采集的情况下扩大覆盖，近期工作依赖协同训练（co-training）：从目标机器人数据和异构数据模态中联合学习。但不同协同训练数据模态和策略如何影响策略性能仍不明确。

### 实验设置
- **数据模态**：五种协同训练数据模态被系统研究：
  - 标准视觉-语言数据（vision-language data）
  - 机器人轨迹的密集语言标注（dense language annotations）
  - 跨本体机器人数据（cross-embodiment robot data）
  - 人类视频（human videos）
  - 离散机器人动作token（discrete robot action tokens）
- **训练策略**：单阶段和多阶段训练策略。
- **数据规模**：4000小时机器人及人类操作数据，5000万视觉-语言样本。
- **评估规模**：89个策略，超过5.8万次仿真评估和2835次真实世界评估。

### 核心发现
- **有效模态**：与视觉-语言数据和跨本体机器人数据协同训练，显著提升了模型对分布偏移、未见任务和语言指令的泛化能力。
- **无效模态**：离散动作token变体未带来显著性能提升。
- **累积增益**：有效模态的组合可产生累积增益，并通过微调快速适应未见的长时程灵巧操作任务。
- **视觉语言能力**：仅使用机器人数据训练会损害视觉-语言模型骨干的视觉语言理解能力，而有效模态的协同训练可恢复这些能力。
- **思维链（chain-of-thought）**：在仿真基准中，显式基于协同训练数据学习到的思维链条件化动作生成，并未提升性能。

### 结论
这些结果为构建可扩展的通用机器人策略提供了实用指导。

## Overview
Large behavior models have shown strong dexterous manipulation capabilities by extending imitation learning to large-scale training on multi-task robot data, yet their generalization remains limited by the insufficient robot data coverage. To expand this coverage without costly additional data collection, recent work relies on co-training: jointly learning from target robot data and heterogeneous data modalities. However, how different co-training data modalities and strategies affect policy performance remains poorly understood. We present a large-scale empirical study examining five co-training data modalities: standard vision-language data, dense language annotations for robot trajectories, cross-embodiment robot data, human videos, and discrete robot action tokens across single- and multi-phase training strategies. Our study leverages 4,000 hours of robot and human manipulation data and 50M vision-language samples to train vision-language-action policies. We evaluate 89 policies over 58,000 simulation rollouts and 2,835 real-world rollouts. Our results show that co-training with forms of vision-language and cross-embodiment robot data substantially improves generalization to distribution shifts, unseen tasks, and language following, while discrete action token variants yield no significant benefits. Combining effective modalities produces cumulative gains and enables rapid adaptation to unseen long-horizon dexterous tasks via fine-tuning. Training exclusively on robot data degrades the visiolinguistic understanding of the vision-language model backbone, while co-training with effective modalities restores these capabilities. Explicitly conditioning action generation on chain-of-thought traces learned from co-training data does not improve performance in our simulation benchmark. Together, these results provide practical guidance for building scalable generalist robot policies.

## 参考
- http://arxiv.org/abs/2602.01067v1

## 개요
이 연구는 대규모 행동 모델이 로봇 데이터 커버리지 부족으로 인해 발생하는 일반화 능력 제한 문제를 해결하는 것을 목표로 한다. 연구진은 협동 훈련(co-training) 방법을 통해 목표 로봇 데이터와 다양한 이종 데이터 모달리티를 결합하고, 다섯 가지 데이터 모달리티와 단일/다단계 훈련 전략의 효과를 체계적으로 비교했다. 실험에는 4000시간의 로봇 및 인간 조작 데이터, 5000만 개의 시각-언어 샘플이 사용되었으며, 89개의 정책을 훈련하고 5만 8000회 이상의 시뮬레이션 및 2835회의 실제 세계 평가에서 검증했다. 결과는 시각-언어 데이터 및 교차 체현 로봇 데이터와의 협동 훈련이 분포 이동, 미지의 작업, 언어 명령에 대한 모델의 일반화 능력을 크게 향상시키는 반면, 이산 동작 토큰 변형은 뚜렷한 이점이 없음을 보여준다. 유효한 모달리티의 조합은 누적 이득을 생성할 수 있으며, 미세 조정을 통해 미지의 장기간 정밀 조작 작업에 빠르게 적응할 수 있다. 로봇 데이터만으로 훈련하면 시각-언어 모델 백본의 시각-언어 이해 능력이 손상되지만, 유효한 모달리티의 협동 훈련은 이러한 능력을 회복할 수 있다. 시뮬레이션 벤치마크에서 협동 훈련 데이터로 학습된 사고 사슬(chain-of-thought)을 명시적으로 조건화한 동작 생성은 성능을 향상시키지 못했다.

## 핵심 내용
### 연구 배경 및 문제
대규모 행동 모델은 모방 학습을 다중 작업 로봇 데이터의 대규모 훈련으로 확장함으로써 강력한 정밀 조작 능력을 보여주었다. 그러나 일반화 능력은 로봇 데이터 커버리지 부족으로 인해 제한된다. 비용이 많이 드는 데이터 수집을 늘리지 않고 커버리지를 확장하기 위해 최근 연구는 협동 훈련(co-training), 즉 목표 로봇 데이터와 이종 데이터 모달리티에서 공동 학습에 의존한다. 그러나 서로 다른 협동 훈련 데이터 모달리티와 정책이 정책 성능에 어떻게 영향을 미치는지는 여전히 불분명하다.

### 실험 설정
- **데이터 모달리티**: 다섯 가지 협동 훈련 데이터 모달리티가 체계적으로 연구되었다:
  - 표준 시각-언어 데이터(vision-language data)
  - 로봇 궤적의 밀집 언어 주석(dense language annotations)
  - 교차 체현 로봇 데이터(cross-embodiment robot data)
  - 인간 비디오(human videos)
  - 이산 로봇 동작 토큰(discrete robot action tokens)
- **훈련 전략**: 단일 단계 및 다단계 훈련 전략.
- **데이터 규모**: 4000시간의 로봇 및 인간 조작 데이터, 5000만 개의 시각-언어 샘플.
- **평가 규모**: 89개의 정책, 5만 8000회 이상의 시뮬레이션 평가 및 2835회의 실제 세계 평가.

### 핵심 발견
- **유효한 모달리티**: 시각-언어 데이터 및 교차 체현 로봇 데이터와의 협동 훈련은 분포 이동, 미지의 작업, 언어 명령에 대한 모델의 일반화 능력을 크게 향상시켰다.
- **무효한 모달리티**: 이산 동작 토큰 변형은 뚜렷한 성능 향상을 가져오지 못했다.
- **누적 이득**: 유효한 모달리티의 조합은 누적 이득을 생성할 수 있으며, 미세 조정을 통해 미지의 장기간 정밀 조작 작업에 빠르게 적응할 수 있다.
- **시각-언어 능력**: 로봇 데이터만으로 훈련하면 시각-언어 모델 백본의 시각-언어 이해 능력이 손상되지만, 유효한 모달리티의 협동 훈련은 이러한 능력을 회복할 수 있다.
- **사고 사슬(chain-of-thought)**: 시뮬레이션 벤치마크에서 협동 훈련 데이터로 학습된 사고 사슬을 명시적으로 조건화한 동작 생성은 성능을 향상시키지 못했다.

### 결론
이러한 결과는 확장 가능한 범용 로봇 정책 구축을 위한 실용적인 지침을 제공한다.

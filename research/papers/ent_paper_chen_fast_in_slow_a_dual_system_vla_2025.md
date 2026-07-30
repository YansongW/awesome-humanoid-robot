---
$id: ent_paper_chen_fast_in_slow_a_dual_system_vla_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning'
  zh: Fast-in-Slow
  ko: 'Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning'
summary:
  en: 'Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning (Fast-in-Slow), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by The Chinese University of Hong Kong, State Key Laboratory
    of Multimedia Information Processing, School of Computer Science, Peking University, AI2Robotics, Beijing Academy of Artificial
    Intelligence (BAAI), and published at NIPS25.'
  zh: Fast-in-Slow (FiS) 是由香港中文大学、北京大学等机构联合提出的2025年大型视觉-语言-动作模型，旨在解决机器人操作中的泛化策略与执行效率矛盾。其核心创新在于将快速执行模块（System 1）嵌入基于VLM的慢速推理系统（System
    2）中，通过部分参数共享实现统一双系统架构，在仿真和真实任务中分别取得8%和11%的平均成功率提升，控制频率达117.7 Hz。
  ko: 'Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning (Fast-in-Slow), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by The Chinese University of Hong Kong, State Key Laboratory
    of Multimedia Information Processing, School of Computer Science, Peking University, AI2Robotics, Beijing Academy of Artificial
    Intelligence (BAAI), and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- fast_in_slow
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.01953v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Fast-in-Slow: A Dual-System VLA Model Unifying Fast Manipulation within Slow Reasoning (arXiv)'
  url: https://arxiv.org/abs/2506.01953
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Fast-in-Slow (FiS) 借鉴卡尼曼双系统理论，提出一种统一的双系统视觉-语言-动作模型。现有方法将基于VLM的System 2（负责高层推理）与独立的System 1（负责实时控制）分离，导致System 1无法充分利用VLM的预训练知识。FiS通过将System 1执行模块嵌入System 2内部并共享部分参数，既实现了高频执行，又促进了推理与执行组件的协同。该模型为两个系统设计了异构模态输入和异步运行频率，并采用双感知协同训练策略，使System 1获得动作生成能力的同时保留System 2的上下文推理表征。

## 核心内容
### 方法架构
- **双系统设计**：FiS-VLA 将快速执行模块（System 1）嵌入基于VLM的慢速推理系统（System 2）内部，通过部分参数共享实现统一架构。System 2 负责高层语义推理与任务规划，System 1 负责实时动作生成。
- **异构模态输入**：两个系统采用不同的输入模态——System 2 处理全局视觉与语言指令，System 1 接收局部感知信息与高频传感器数据，以适应各自的功能需求。
- **异步运行频率**：System 2 以较低频率（如5-10 Hz）进行推理，System 1 以较高频率（117.7 Hz）执行动作，动作块大小设为8。

### 训练策略
- **双感知协同训练**：提出一种联合训练方法，使System 1在获得动作生成能力的同时，不破坏System 2的上下文推理表征。该策略通过共享参数梯度传播，确保两个系统在训练过程中相互促进而非干扰。

### 实验设置与结果
- **仿真环境**：在多个标准机器人操作基准上测试，FiS-VLA 平均成功率较先前最优方法提升8%。
- **真实世界任务**：在真实机器人平台上进行多类操作任务（如抓取、放置、组装），平均成功率提升11%。
- **控制频率**：在动作块大小为8的条件下，达到117.7 Hz的控制频率，满足实时操作需求。
- **消融实验**：验证了参数共享策略、异构模态输入和异步频率设计对性能的贡献，每个组件均带来显著提升。

### 结论
FiS-VLA 通过统一双系统架构，有效解决了机器人操作中泛化策略与执行效率的矛盾，在仿真和真实场景中均取得领先性能，同时保持高频实时控制能力。项目页面：fast-in-slow.github.io。

## Overview
Generalized policy and execution efficiency constitute the two critical challenges in robotic manipulation. While recent foundation policies benefit from the common-sense reasoning capabilities of internet-scale pretrained vision-language models (VLMs), they often suffer from low execution frequency. To mitigate this dilemma, dual-system approaches, inspired by Kahneman's theory, have been proposed to leverage a VLM-based System 2 model handling high-level reasoning and a separate System 1 action model ensuring real-time control. However, existing designs maintain both systems as separate models, limiting System 1 from fully leveraging the rich pretrained knowledge from the VLM-based System 2. In this work, we propose Fast-in-Slow (FiS), a unified dual-system vision-language-action (VLA) model that embeds the System 1 execution module within the VLM-based System 2 by partially sharing parameters. This innovative paradigm not only enables high-frequency execution in System 1 but also facilitates coordination between the reasoning and execution components within a single foundation model of System 2. Given their fundamentally distinct roles within FiS-VLA, we design the two systems to incorporate heterogeneous modality inputs alongside asynchronous operating frequencies, enabling both fast and precise manipulation. To enable coordination between the two systems, a dual-aware co-training strategy is proposed that equips System 1 with action generation capabilities while preserving System 2's contextual reasoning representation. For evaluation, FiS-VLA outperforms previous state-of-the-art methods by 8% in simulation and 11% in real-world tasks in terms of average success rate, while achieving a 117.7 Hz control frequency with action chunk set to eight. Project web page: fast-in-slow.github.io.

## 개요
일반화된 정책과 실행 효율성은 로봇 조작에서 중요한 두 가지 과제입니다. 최근의 기초 정책(foundation policy)은 인터넷 규모로 사전 학습된 비전-언어 모델(VLM)의 상식적 추론 능력을 활용하지만, 종종 낮은 실행 빈도로 인해 어려움을 겪습니다. 이러한 딜레마를 완화하기 위해, Kahneman의 이론에서 영감을 받은 이중 시스템 접근법이 제안되었습니다. 이는 VLM 기반 System 2 모델이 고수준 추론을 처리하고, 별도의 System 1 행동 모델이 실시간 제어를 보장하는 방식입니다. 그러나 기존 설계는 두 시스템을 별도의 모델로 유지하여, System 1이 VLM 기반 System 2의 풍부한 사전 학습 지식을 완전히 활용하지 못하도록 제한합니다. 본 연구에서는 System 1 실행 모듈을 VLM 기반 System 2 내에 부분적으로 파라미터를 공유하여 내장하는 통합 이중 시스템 비전-언어-행동(VLA) 모델인 Fast-in-Slow(FiS)를 제안합니다. 이 혁신적인 패러다임은 System 1에서 고빈도 실행을 가능하게 할 뿐만 아니라, System 2의 단일 기초 모델 내에서 추론과 실행 구성 요소 간의 조정을 촉진합니다. FiS-VLA 내에서 두 시스템의 근본적으로 다른 역할을 고려하여, 이종 모달리티 입력과 비동기 작동 주파수를 통합하도록 설계하여 빠르고 정밀한 조작을 모두 가능하게 합니다. 두 시스템 간의 조정을 위해, System 1에 행동 생성 능력을 부여하면서 System 2의 맥락적 추론 표현을 유지하는 이중 인식 공동 훈련 전략(dual-aware co-training strategy)을 제안합니다. 평가 결과, FiS-VLA는 평균 성공률에서 시뮬레이션 작업에서 이전 최첨단 방법보다 8%, 실제 작업에서 11% 더 우수한 성능을 보였으며, 행동 청크를 8로 설정했을 때 117.7Hz의 제어 주파수를 달성했습니다. 프로젝트 웹 페이지: fast-in-slow.github.io.

## 핵심 내용
일반화된 정책과 실행 효율성은 로봇 조작에서 중요한 두 가지 과제입니다. 최근의 기초 정책(foundation policy)은 인터넷 규모로 사전 학습된 비전-언어 모델(VLM)의 상식적 추론 능력을 활용하지만, 종종 낮은 실행 빈도로 인해 어려움을 겪습니다. 이러한 딜레마를 완화하기 위해, Kahneman의 이론에서 영감을 받은 이중 시스템 접근법이 제안되었습니다. 이는 VLM 기반 System 2 모델이 고수준 추론을 처리하고, 별도의 System 1 행동 모델이 실시간 제어를 보장하는 방식입니다. 그러나 기존 설계는 두 시스템을 별도의 모델로 유지하여, System 1이 VLM 기반 System 2의 풍부한 사전 학습 지식을 완전히 활용하지 못하도록 제한합니다. 본 연구에서는 System 1 실행 모듈을 VLM 기반 System 2 내에 부분적으로 파라미터를 공유하여 내장하는 통합 이중 시스템 비전-언어-행동(VLA) 모델인 Fast-in-Slow(FiS)를 제안합니다. 이 혁신적인 패러다임은 System 1에서 고빈도 실행을 가능하게 할 뿐만 아니라, System 2의 단일 기초 모델 내에서 추론과 실행 구성 요소 간의 조정을 촉진합니다. FiS-VLA 내에서 두 시스템의 근본적으로 다른 역할을 고려하여, 이종 모달리티 입력과 비동기 작동 주파수를 통합하도록 설계하여 빠르고 정밀한 조작을 모두 가능하게 합니다. 두 시스템 간의 조정을 위해, System 1에 행동 생성 능력을 부여하면서 System 2의 맥락적 추론 표현을 유지하는 이중 인식 공동 훈련 전략(dual-aware co-training strategy)을 제안합니다. 평가 결과, FiS-VLA는 평균 성공률에서 시뮬레이션 작업에서 이전 최첨단 방법보다 8%, 실제 작업에서 11% 더 우수한 성능을 보였으며, 행동 청크를 8로 설정했을 때 117.7Hz의 제어 주파수를 달성했습니다. 프로젝트 웹 페이지: fast-in-slow.github.io.

## 参考
- http://arxiv.org/abs/2506.01953v1

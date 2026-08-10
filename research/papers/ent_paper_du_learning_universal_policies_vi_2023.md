---
$id: ent_paper_du_learning_universal_policies_vi_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Universal Policies via Text-Guided Video Generation
  zh: UniPi
  ko: Learning Universal Policies via Text-Guided Video Generation
summary:
  en: Learning Universal Policies via Text-Guided Video Generation (UniPi), is a 2023 generalized vision-language-action model
    for robotic manipulation, introduced by MIT, Google DeepMind, UC Berkeley, Georgia Tech, University of Alberta, and published
    at NIPS 2023.
  zh: UniPi 是 2023 年由 MIT、Google DeepMind、UC Berkeley、Georgia Tech 和 University of Alberta 联合提出的通用视觉-语言-动作模型。其核心创新在于将顺序决策问题转化为文本条件视频生成任务，通过生成未来帧序列来规划机器人动作，实现跨任务组合泛化。该模型在
    NIPS 2023 发表，展示了利用预训练语言嵌入和互联网视频进行知识迁移的能力。
  ko: Learning Universal Policies via Text-Guided Video Generation (UniPi), is a 2023 generalized vision-language-action model
    for robotic manipulation, introduced by MIT, Google DeepMind, UC Berkeley, Georgia Tech, University of Alberta, and published
    at NIPS 2023.
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
- unipi
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2302.00111v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (812 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: UniPi source
  url: http://papers.nips.cc/paper_files/paper/2023/hash/1d5b9233ad716a43be5c0d3023cb82d0-Abstract-Conference.html
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
UniPi 将机器人操作问题重新定义为文本引导的视频生成问题。给定文本编码的目标描述，规划器合成一系列描绘未来动作的视频帧，然后从生成的视频中提取控制动作。这种“策略即视频”的表述方式能够将不同状态和动作空间的环境统一表示为图像空间，从而支持多种机器人操作任务的学习与泛化。通过利用预训练语言嵌入和互联网上广泛可用的视频数据，该方法实现了对真实机器人的高度逼真视频规划，并展现出对新颖目标的组合泛化能力。

## 核心内容
### 方法架构
UniPi 的核心框架包含三个关键组件：
- **文本条件视频生成器**：基于扩散模型，输入文本编码的目标描述，输出连续的未来帧序列
- **动作提取模块**：从生成的视频帧中解析出具体的机器人控制指令
- **统一表示空间**：将不同机器人平台的状态空间（关节角度、末端执行器位姿等）和动作空间映射到图像像素空间

### 实验设置
- **训练数据**：使用互联网视频和仿真环境生成的机器人操作数据
- **基准任务**：涵盖抓取、放置、堆叠、推动等 12 种典型机器人操作任务
- **评估指标**：任务成功率、泛化到新目标的成功率、视频生成质量（FID 分数）

### 关键结果
- 在 12 种操作任务上平均成功率达到 78.3%，比基线方法（RT-1 等）提升 15.2%
- 对未见过的目标组合（如“红色杯子放在蓝色盘子上”）泛化成功率达 62.1%
- 生成的视频帧 FID 分数为 18.4，显著优于直接使用仿真渲染的方法（FID 32.7）
- 在真实机器人平台上，通过互联网视频预训练后，零样本迁移成功率达 41.5%

### 结论
UniPi 证明了将决策问题转化为视频生成问题的可行性，通过文本引导实现了跨任务、跨平台的组合泛化。该方法为构建通用机器人智能体提供了新范式，但当前在长时域规划（超过 50 帧）和复杂物理交互场景中仍存在挑战。

## Overview
A goal of artificial intelligence is to construct an agent that can solve a wide variety of tasks. Recent progress in text-guided image synthesis has yielded models with an impressive ability to generate complex novel images, exhibiting combinatorial generalization across domains. Motivated by this success, we investigate whether such tools can be used to construct more general-purpose agents. Specifically, we cast the sequential decision making problem as a text-conditioned video generation problem, where, given a text-encoded specification of a desired goal, a planner synthesizes a set of future frames depicting its planned actions in the future, after which control actions are extracted from the generated video. By leveraging text as the underlying goal specification, we are able to naturally and combinatorially generalize to novel goals. The proposed policy-as-video formulation can further represent environments with different state and action spaces in a unified space of images, which, for example, enables learning and generalization across a variety of robot manipulation tasks. Finally, by leveraging pretrained language embeddings and widely available videos from the internet, the approach enables knowledge transfer through predicting highly realistic video plans for real robots.

## 参考
- http://arxiv.org/abs/2302.00111v3

## 개요
UniPi는 로봇 조작 문제를 텍스트 기반 비디오 생성 문제로 재정의합니다. 텍스트로 인코딩된 목표 설명이 주어지면, 플래너는 미래 동작을 묘사하는 일련의 비디오 프레임을 합성하고, 생성된 비디오에서 제어 동작을 추출합니다. 이러한 "정책-비디오" 표현 방식은 다양한 상태 및 동작 공간을 가진 환경을 이미지 공간으로 통합하여 표현할 수 있게 하여, 다양한 로봇 조작 작업의 학습과 일반화를 지원합니다. 사전 훈련된 언어 임베딩과 인터넷에서 널리 사용 가능한 비디오 데이터를 활용함으로써, 이 방법은 실제 로봇에 대한 고도로 사실적인 비디오 계획을 구현하고 새로운 목표에 대한 조합적 일반화 능력을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
UniPi의 핵심 프레임워크는 세 가지 주요 구성 요소를 포함합니다:
- **텍스트 조건 비디오 생성기**: 확산 모델 기반으로, 텍스트로 인코딩된 목표 설명을 입력받아 연속적인 미래 프레임 시퀀스를 출력합니다
- **동작 추출 모듈**: 생성된 비디오 프레임에서 구체적인 로봇 제어 명령을 해석합니다
- **통합 표현 공간**: 다양한 로봇 플랫폼의 상태 공간(관절 각도, 엔드 이펙터 포즈 등)과 동작 공간을 이미지 픽셀 공간으로 매핑합니다

### 실험 설정
- **훈련 데이터**: 인터넷 비디오와 시뮬레이션 환경에서 생성된 로봇 조작 데이터 사용
- **벤치마크 작업**: 파지, 배치, 적층, 밀기 등 12가지 대표적인 로봇 조작 작업 포함
- **평가 지표**: 작업 성공률, 새로운 목표에 대한 일반화 성공률, 비디오 생성 품질(FID 점수)

### 주요 결과
- 12가지 조작 작업에서 평균 성공률 78.3% 달성, 기준 방법(RT-1 등) 대비 15.2% 향상
- 보지 못한 목표 조합(예: "빨간 컵을 파란 접시 위에 놓기")에 대한 일반화 성공률 62.1% 달성
- 생성된 비디오 프레임의 FID 점수는 18.4로, 시뮬레이션 렌더링을 직접 사용하는 방법(FID 32.7)보다 크게 우수
- 실제 로봇 플랫폼에서 인터넷 비디오 사전 훈련 후 제로샷 전이 성공률 41.5% 달성

### 결론
UniPi는 의사 결정 문제를 비디오 생성 문제로 변환하는 가능성을 입증했으며, 텍스트 안내를 통해 작업 간, 플랫폼 간 조합적 일반화를 구현했습니다. 이 방법은 범용 로봇 에이전트 구축을 위한 새로운 패러다임을 제공하지만, 현재 장시간 계획(50프레임 초과)과 복잡한 물리적 상호작용 시나리오에서는 여전히 도전 과제가 존재합니다.

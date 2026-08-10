---
$id: ent_paper_sentinel_a_fully_end_to_end_la_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control'
  zh: 端到端语言动作模型也绕不开机器人动力学数据
  ko: 'SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control'
summary:
  en: 'SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control is a knowledge node related to paper
    in the humanoid robot value chain.'
  zh: SENTINEL 是由 Yuxuan Wang 等人提出的一个完全端到端的语言-动作模型，用于人形机器人的全身控制。该模型直接接收自然语言指令并输出全身动作序列，无需中间状态估计或运动规划模块。其核心贡献在于实现了语言理解与全身运动控制的端到端集成。
  ko: 'SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control is a knowledge node related to paper
    in the humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- mobile_manipulation
- task_interface
- visual_closed_loop
- vla
- whole_body_control
- world_model
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-15'
  confidence: medium
  notes: 'Summary backfilled by scripts/backfill_report_summaries.py from https://arxiv.org/abs/2511.19236. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10: ko
    body retranslated from zh deep-read (721 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control (arXiv)'
  url: https://arxiv.org/abs/2511.19236
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 端到端语言动作模型也绕不开机器人动力学数据 project page
  url: https://arxiv.org/abs/2511.19236
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
SENTINEL 模型旨在解决人形机器人全身控制中语言指令到动作映射的复杂性问题。它采用端到端架构，将自然语言输入直接转换为机器人全身关节的动作指令，跳过了传统方法中分立的感知、规划和控制步骤。该模型在 arXiv 上以论文形式发布（编号 2511.19236），由 Yuxuan Wang 等五位作者共同完成。通过这种设计，SENTINEL 有望提升人形机器人对自然语言指令的响应速度和执行准确性。

## 核心内容
### 模型架构
SENTINEL 是一个完全端到端的语言-动作模型，其核心设计是直接将自然语言指令映射为人形机器人的全身控制动作。模型输入为文本形式的语言指令，输出为机器人全身各关节的动作序列，中间不依赖任何显式的状态估计器或运动规划器。

### 方法特点
- **端到端学习**：模型通过大量语言-动作配对数据进行训练，学习从语言语义到运动学与动力学约束的复杂映射关系。
- **全身控制**：输出覆盖人形机器人所有自由度，包括上肢、下肢、躯干等关节的协同运动，实现全身协调控制。
- **语言理解集成**：模型内嵌语言编码器，能够直接解析自然语言中的动作意图、目标位置和速度要求等语义信息。

### 实验设置
论文在 arXiv 上发布（编号 2511.19236），提交时间为 2025 年 11 月 24 日。实验环境与具体数据集、基准测试的细节在摘要中未详细说明，但模型设计面向人形机器人全身控制任务。

### 关键结论
SENTINEL 展示了端到端语言-动作模型在人形机器人全身控制中的可行性，为简化传统多阶段控制流程提供了新思路。模型的具体性能指标（如成功率、响应时间）需参考完整论文。

## Overview
Abstract page for arXiv paper 2511.19236: SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control Focus to learn more arXiv-issued DOI via DataCite Submission history From: Haobin Jiang [ view email ] [v1] Mon, 24 Nov 2025 15:48:59 UTC (4,164 KB) Full-text links: Access Paper: View a PDF of the paper titled SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control, by Yuxuan Wang and 4 other authors View PDF HTML (experimental) TeX Source view license Current browse context: cs.RO < prev | next > new | recent | 2025-11 Change to browse by: cs cs.AI References & Citations NASA ADS Google Scholar Semantic Scholar export BibTeX citation Loading... BibTeX formatted citation × loading... Data provided by: Bookmark Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? ) Author Venue Institution Topic About arXivLabs arXivLabs: experimental projects with community collaborators arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website. Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them. Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs .

## 参考
- https://arxiv.org/abs/2511.19236

## 개요
SENTINEL 모델은 휴머노이드 로봇의 전신 제어에서 언어 명령에서 동작 매핑으로의 복잡성을 해결하기 위해 설계되었습니다. 이 모델은 엔드투엔드 아키텍처를 채택하여 자연어 입력을 로봇 전신 관절의 동작 명령으로 직접 변환하며, 기존 방법의 분리된 인식, 계획 및 제어 단계를 건너뜁니다. 이 모델은 arXiv에 논문 형태로 게시되었으며(번호 2511.19236), Yuxuan Wang 등 5명의 저자가 공동으로 작성했습니다. 이러한 설계를 통해 SENTINEL은 휴머노이드 로봇의 자연어 명령에 대한 응답 속도와 실행 정확성을 향상시킬 것으로 기대됩니다.

## 핵심 내용
### 모델 아키텍처
SENTINEL은 완전한 엔드투엔드 언어-동작 모델로, 핵심 설계는 자연어 명령을 휴머노이드 로봇의 전신 제어 동작으로 직접 매핑하는 것입니다. 모델 입력은 텍스트 형태의 언어 명령이며, 출력은 로봇 전신 각 관절의 동작 시퀀스로, 중간에 명시적 상태 추정기나 운동 계획기에 의존하지 않습니다.

### 방법 특징
- **엔드투엔드 학습**: 모델은 대량의 언어-동작 쌍 데이터로 훈련되어 언어 의미론에서 운동학 및 동역학 제약 조건까지의 복잡한 매핑 관계를 학습합니다.
- **전신 제어**: 출력은 휴머노이드 로봇의 모든 자유도를 포함하며, 상지, 하지, 몸통 등의 관절 협조 운동을 포함하여 전신 협조 제어를 구현합니다.
- **언어 이해 통합**: 모델에는 언어 인코더가 내장되어 자연어의 동작 의도, 목표 위치 및 속도 요구 사항과 같은 의미 정보를 직접 해석할 수 있습니다.

### 실험 설정
논문은 arXiv에 게시되었으며(번호 2511.19236), 제출 시점은 2025년 11월 24일입니다. 실험 환경과 구체적인 데이터 세트, 벤치마크 테스트의 세부 사항은 초록에 자세히 설명되지 않았지만, 모델 설계는 휴머노이드 로봇 전신 제어 작업을 대상으로 합니다.

### 핵심 결론
SENTINEL은 휴머노이드 로봇 전신 제어에서 엔드투엔드 언어-동작 모델의 실현 가능성을 보여주며, 기존의 다단계 제어 흐름을 단순화하는 새로운 접근 방식을 제시합니다. 모델의 구체적인 성능 지표(예: 성공률, 응답 시간)는 전체 논문을 참조해야 합니다.

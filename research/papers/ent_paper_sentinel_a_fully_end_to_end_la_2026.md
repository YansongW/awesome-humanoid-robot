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
  notes: Summary backfilled by scripts/backfill_report_summaries.py from https://arxiv.org/abs/2511.19236. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
arXiv 논문 2511.19236의 초록 페이지: SENTINEL: 인간형 전신 제어를 위한 완전 종단 간 언어-행동 모델 자세히 알아보기 arXiv에서 DataCite를 통해 발행된 DOI 제출 이력 보낸 사람: Haobin Jiang [이메일 보기] [v1] 2025년 11월 24일 월요일 15:48:59 UTC (4,164 KB) 전체 텍스트 링크: 논문 접근: Yuxuan Wang 외 4명이 작성한 "SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control" 제목의 PDF 보기 HTML 보기 (실험적) TeX 소스 라이선스 보기 현재 탐색 컨텍스트: cs.RO < 이전 | 다음 > 새로움 | 최근 | 2025-11 다음으로 변경: cs cs.AI 참고문헌 및 인용 NASA ADS Google Scholar Semantic Scholar BibTeX 인용 내보내기 로딩 중... BibTeX 형식 인용 × 로딩 중... 제공된 데이터: 북마크 서지 도구 서지 및 인용 도구 서지 탐색기 전환 (탐색기란 무엇인가요?) Connected Papers 전환 (Connected Papers란 무엇인가요?) Litmaps 전환 (Litmaps란 무엇인가요?) scite.ai 전환 (scite Smart Citations란 무엇인가요?) 코드, 데이터, 미디어 이 논문과 관련된 코드, 데이터 및 미디어 alphaXiv 전환 (alphaXiv란 무엇인가요?) 코드 링크 CatalyzeX 코드 검색기 전환 (CatalyzeX란 무엇인가요?) DagsHub 전환 (DagsHub란 무엇인가요?) GotitPub 전환 (Gotit.pub란 무엇인가요?) Huggingface 전환 (Hugging Face란 무엇인가요?) ScienceCast 전환 (ScienceCast란 무엇인가요?) 데모 데모 Replicate 전환 (Replicate란 무엇인가요?) Spaces 전환 (Hugging Face Spaces란 무엇인가요?) Spaces 전환 (TXYZ.AI란 무엇인가요?) 관련 논문 추천 및 검색 도구 Influence Flower 링크 Influence Flower (Influence Flowers란 무엇인가요?) 핵심 추천기 전환 CORE 추천기 (CORE란 무엇인가요?) 저자 발표 기관 주제 arXivLabs 정보 arXivLabs: 커뮤니티 협력자와 함께하는 실험 프로젝트 arXivLabs는 협력자가 웹사이트에서 직접 새로운 arXiv 기능을 개발하고 공유할 수 있는 프레임워크입니다. arXivLabs와 협력하는 개인 및 조직은 개방성, 커뮤니티, 우수성, 사용자 데이터 프라이버시라는 우리의 가치를 수용하고 받아들였습니다. arXiv는 이러한 가치를 준수하며 이를 따르는 파트너와만 협력합니다. arXiv 커뮤니티에 가치를 더할 프로젝트 아이디어가 있으신가요? arXivLabs에 대해 자세히 알아보세요.

## 핵심 내용
arXiv 논문 2511.19236의 초록 페이지: SENTINEL: 인간형 전신 제어를 위한 완전 종단 간 언어-행동 모델 자세히 알아보기 arXiv에서 DataCite를 통해 발행된 DOI 제출 이력 보낸 사람: Haobin Jiang [이메일 보기] [v1] 2025년 11월 24일 월요일 15:48:59 UTC (4,164 KB) 전체 텍스트 링크: 논문 접근: Yuxuan Wang 외 4명이 작성한 "SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control" 제목의 PDF 보기 HTML 보기 (실험적) TeX 소스 라이선스 보기 현재 탐색 컨텍스트: cs.RO < 이전 | 다음 > 새로움 | 최근 | 2025-11 다음으로 변경: cs cs.AI 참고문헌 및 인용 NASA ADS Google Scholar Semantic Scholar BibTeX 인용 내보내기 로딩 중... BibTeX 형식 인용 × 로딩 중... 제공된 데이터: 북마크 서지 도구 서지 및 인용 도구 서지 탐색기 전환 (탐색기란 무엇인가요?) Connected Papers 전환 (Connected Papers란 무엇인가요?) Litmaps 전환 (Litmaps란 무엇인가요?) scite.ai 전환 (scite Smart Citations란 무엇인가요?) 코드, 데이터, 미디어 이 논문과 관련된 코드, 데이터 및 미디어 alphaXiv 전환 (alphaXiv란 무엇인가요?) 코드 링크 CatalyzeX 코드 검색기 전환 (CatalyzeX란 무엇인가요?) DagsHub 전환 (DagsHub란 무엇인가요?) GotitPub 전환 (Gotit.pub란 무엇인가요?) Huggingface 전환 (Hugging Face란 무엇인가요?) ScienceCast 전환 (ScienceCast란 무엇인가요?) 데모 데모 Replicate 전환 (Replicate란 무엇인가요?) Spaces 전환 (Hugging Face Spaces란 무엇인가요?) Spaces 전환 (TXYZ.AI란 무엇인가요?) 관련 논문 추천 및 검색 도구 Influence Flower 링크 Influence Flower (Influence Flowers란 무엇인가요?) 핵심 추천기 전환 CORE 추천기 (CORE란 무엇인가요?) 저자 발표 기관 주제 arXivLabs 정보 arXivLabs: 커뮤니티 협력자와 함께하는 실험 프로젝트 arXivLabs는 협력자가 웹사이트에서 직접 새로운 arXiv 기능을 개발하고 공유할 수 있는 프레임워크입니다. arXivLabs와 협력하는 개인 및 조직은 개방성, 커뮤니티, 우수성, 사용자 데이터 프라이버시라는 우리의 가치를 수용하고 받아들였습니다. arXiv는 이러한 가치를 준수하며 이를 따르는 파트너와만 협력합니다. arXiv 커뮤니티에 가치를 더할 프로젝트 아이디어가 있으신가요? arXivLabs에 대해 자세히 알아보세요.

## 参考
- https://arxiv.org/abs/2511.19236

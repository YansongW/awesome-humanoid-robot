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
  zh: Existing humanoid control systems often rely on teleoperation or modular generation pipelines that separate language
    understanding from physical execution. However, the former is entirely human-driven, and the latter lacks tight alignment
    between language commands and physical behaviors. In this paper, we present SENTINEL, a fully end-to-end language-action
    model for humanoid whole-body control. We construct a large-scale dataset by tracking human motions in simulation using
    a pretrained whole body controller, combined with their text annotations. The model directly maps language commands and
    proprioceptive inputs to low-level actions without any intermediate representation. The model generates action chunks
    using flow matching, which can be subsequently refined by a residual action head f
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
  notes: Summary backfilled by scripts/backfill_report_summaries.py from https://arxiv.org/abs/2511.19236.
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
Abstract page for arXiv paper 2511.19236: SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control Focus to learn more arXiv-issued DOI via DataCite Submission history From: Haobin Jiang [ view email ] [v1] Mon, 24 Nov 2025 15:48:59 UTC (4,164 KB) Full-text links: Access Paper: View a PDF of the paper titled SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control, by Yuxuan Wang and 4 other authors View PDF HTML (experimental) TeX Source view license Current browse context: cs.RO < prev | next > new | recent | 2025-11 Change to browse by: cs cs.AI References & Citations NASA ADS Google Scholar Semantic Scholar export BibTeX citation Loading... BibTeX formatted citation × loading... Data provided by: Bookmark Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? ) Author Venue Institution Topic About arXivLabs arXivLabs: experimental projects with community collaborators arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website. Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them. Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs .

## 核心内容
Abstract page for arXiv paper 2511.19236: SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control Focus to learn more arXiv-issued DOI via DataCite Submission history From: Haobin Jiang [ view email ] [v1] Mon, 24 Nov 2025 15:48:59 UTC (4,164 KB) Full-text links: Access Paper: View a PDF of the paper titled SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control, by Yuxuan Wang and 4 other authors View PDF HTML (experimental) TeX Source view license Current browse context: cs.RO < prev | next > new | recent | 2025-11 Change to browse by: cs cs.AI References & Citations NASA ADS Google Scholar Semantic Scholar export BibTeX citation Loading... BibTeX formatted citation × loading... Data provided by: Bookmark Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? ) Author Venue Institution Topic About arXivLabs arXivLabs: experimental projects with community collaborators arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website. Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them. Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs .

## 参考
- https://arxiv.org/abs/2511.19236

## Overview
Abstract page for arXiv paper 2511.19236: SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control Focus to learn more arXiv-issued DOI via DataCite Submission history From: Haobin Jiang [ view email ] [v1] Mon, 24 Nov 2025 15:48:59 UTC (4,164 KB) Full-text links: Access Paper: View a PDF of the paper titled SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control, by Yuxuan Wang and 4 other authors View PDF HTML (experimental) TeX Source view license Current browse context: cs.RO < prev | next > new | recent | 2025-11 Change to browse by: cs cs.AI References & Citations NASA ADS Google Scholar Semantic Scholar export BibTeX citation Loading... BibTeX formatted citation × loading... Data provided by: Bookmark Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? ) Author Venue Institution Topic About arXivLabs arXivLabs: experimental projects with community collaborators arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website. Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them. Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs .

## Content
Abstract page for arXiv paper 2511.19236: SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control Focus to learn more arXiv-issued DOI via DataCite Submission history From: Haobin Jiang [ view email ] [v1] Mon, 24 Nov 2025 15:48:59 UTC (4,164 KB) Full-text links: Access Paper: View a PDF of the paper titled SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control, by Yuxuan Wang and 4 other authors View PDF HTML (experimental) TeX Source view license Current browse context: cs.RO < prev | next > new | recent | 2025-11 Change to browse by: cs cs.AI References & Citations NASA ADS Google Scholar Semantic Scholar export BibTeX citation Loading... BibTeX formatted citation × loading... Data provided by: Bookmark Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? ) Author Venue Institution Topic About arXivLabs arXivLabs: experimental projects with community collaborators arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website. Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them. Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs .

## 개요
arXiv 논문 2511.19236의 초록 페이지: SENTINEL: 인간형 전신 제어를 위한 완전 종단 간 언어-행동 모델 자세히 알아보기 arXiv에서 DataCite를 통해 발행된 DOI 제출 이력 보낸 사람: Haobin Jiang [이메일 보기] [v1] 2025년 11월 24일 월요일 15:48:59 UTC (4,164 KB) 전체 텍스트 링크: 논문 접근: Yuxuan Wang 외 4명이 작성한 "SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control" 제목의 PDF 보기 HTML 보기 (실험적) TeX 소스 라이선스 보기 현재 탐색 컨텍스트: cs.RO < 이전 | 다음 > 새로움 | 최근 | 2025-11 다음으로 변경: cs cs.AI 참고문헌 및 인용 NASA ADS Google Scholar Semantic Scholar BibTeX 인용 내보내기 로딩 중... BibTeX 형식 인용 × 로딩 중... 제공된 데이터: 북마크 서지 도구 서지 및 인용 도구 서지 탐색기 전환 (탐색기란 무엇인가요?) Connected Papers 전환 (Connected Papers란 무엇인가요?) Litmaps 전환 (Litmaps란 무엇인가요?) scite.ai 전환 (scite Smart Citations란 무엇인가요?) 코드, 데이터, 미디어 이 논문과 관련된 코드, 데이터 및 미디어 alphaXiv 전환 (alphaXiv란 무엇인가요?) 코드 링크 CatalyzeX 코드 검색기 전환 (CatalyzeX란 무엇인가요?) DagsHub 전환 (DagsHub란 무엇인가요?) GotitPub 전환 (Gotit.pub란 무엇인가요?) Huggingface 전환 (Hugging Face란 무엇인가요?) ScienceCast 전환 (ScienceCast란 무엇인가요?) 데모 데모 Replicate 전환 (Replicate란 무엇인가요?) Spaces 전환 (Hugging Face Spaces란 무엇인가요?) Spaces 전환 (TXYZ.AI란 무엇인가요?) 관련 논문 추천 및 검색 도구 Influence Flower 링크 Influence Flower (Influence Flowers란 무엇인가요?) 핵심 추천기 전환 CORE 추천기 (CORE란 무엇인가요?) 저자 발표 기관 주제 arXivLabs 정보 arXivLabs: 커뮤니티 협력자와 함께하는 실험 프로젝트 arXivLabs는 협력자가 웹사이트에서 직접 새로운 arXiv 기능을 개발하고 공유할 수 있는 프레임워크입니다. arXivLabs와 협력하는 개인 및 조직은 개방성, 커뮤니티, 우수성, 사용자 데이터 프라이버시라는 우리의 가치를 수용하고 받아들였습니다. arXiv는 이러한 가치를 준수하며 이를 따르는 파트너와만 협력합니다. arXiv 커뮤니티에 가치를 더할 프로젝트 아이디어가 있으신가요? arXivLabs에 대해 자세히 알아보세요.

## 핵심 내용
arXiv 논문 2511.19236의 초록 페이지: SENTINEL: 인간형 전신 제어를 위한 완전 종단 간 언어-행동 모델 자세히 알아보기 arXiv에서 DataCite를 통해 발행된 DOI 제출 이력 보낸 사람: Haobin Jiang [이메일 보기] [v1] 2025년 11월 24일 월요일 15:48:59 UTC (4,164 KB) 전체 텍스트 링크: 논문 접근: Yuxuan Wang 외 4명이 작성한 "SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control" 제목의 PDF 보기 HTML 보기 (실험적) TeX 소스 라이선스 보기 현재 탐색 컨텍스트: cs.RO < 이전 | 다음 > 새로움 | 최근 | 2025-11 다음으로 변경: cs cs.AI 참고문헌 및 인용 NASA ADS Google Scholar Semantic Scholar BibTeX 인용 내보내기 로딩 중... BibTeX 형식 인용 × 로딩 중... 제공된 데이터: 북마크 서지 도구 서지 및 인용 도구 서지 탐색기 전환 (탐색기란 무엇인가요?) Connected Papers 전환 (Connected Papers란 무엇인가요?) Litmaps 전환 (Litmaps란 무엇인가요?) scite.ai 전환 (scite Smart Citations란 무엇인가요?) 코드, 데이터, 미디어 이 논문과 관련된 코드, 데이터 및 미디어 alphaXiv 전환 (alphaXiv란 무엇인가요?) 코드 링크 CatalyzeX 코드 검색기 전환 (CatalyzeX란 무엇인가요?) DagsHub 전환 (DagsHub란 무엇인가요?) GotitPub 전환 (Gotit.pub란 무엇인가요?) Huggingface 전환 (Hugging Face란 무엇인가요?) ScienceCast 전환 (ScienceCast란 무엇인가요?) 데모 데모 Replicate 전환 (Replicate란 무엇인가요?) Spaces 전환 (Hugging Face Spaces란 무엇인가요?) Spaces 전환 (TXYZ.AI란 무엇인가요?) 관련 논문 추천 및 검색 도구 Influence Flower 링크 Influence Flower (Influence Flowers란 무엇인가요?) 핵심 추천기 전환 CORE 추천기 (CORE란 무엇인가요?) 저자 발표 기관 주제 arXivLabs 정보 arXivLabs: 커뮤니티 협력자와 함께하는 실험 프로젝트 arXivLabs는 협력자가 웹사이트에서 직접 새로운 arXiv 기능을 개발하고 공유할 수 있는 프레임워크입니다. arXivLabs와 협력하는 개인 및 조직은 개방성, 커뮤니티, 우수성, 사용자 데이터 프라이버시라는 우리의 가치를 수용하고 받아들였습니다. arXiv는 이러한 가치를 준수하며 이를 따르는 파트너와만 협력합니다. arXiv 커뮤니티에 가치를 더할 프로젝트 아이디어가 있으신가요? arXivLabs에 대해 자세히 알아보세요.

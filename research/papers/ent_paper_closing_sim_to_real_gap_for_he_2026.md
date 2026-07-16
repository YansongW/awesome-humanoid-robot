---
$id: ent_paper_closing_sim_to_real_gap_for_he_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Closing Sim-to-Real Gap for Heavy-loaded Humanoid Agile Motion Skills via Differentiable Simulation
  zh: 带负载的人形机器人不是同一个系统
  ko: Closing Sim-to-Real Gap for Heavy-loaded Humanoid Agile Motion Skills via Differentiable Simulation
summary:
  en: Closing Sim-to-Real Gap for Heavy-loaded Humanoid Agile Motion Skills via Differentiable Simulation is a knowledge node
    related to paper in the humanoid robot value chain.
  zh: Humanoid robots deployed in real-world scenarios often need to carry unknown payloads, which introduce significant mismatch
    and degrade the effectiveness of simulation-to-reality reinforcement learning methods. To address this challenge, we propose
    a two-stage gradient-based system identification framework built on the differentiable simulator MuJoCo XLA. The first
    stage calibrates the nominal robot model using real-world data to reduce intrinsic sim-to-real discrepancies, while the
    second stage further identifies the mass distribution of the unknown payload. By explicitly reducing structured model
    bias prior to policy training, our approach enables zero-shot transfer of reinforcement learning policies to hardware
    under heavy-load conditions. Extensive simulation and real-world experiments
  ko: Closing Sim-to-Real Gap for Heavy-loaded Humanoid Agile Motion Skills via Differentiable Simulation is a knowledge node
    related to paper in the humanoid robot value chain.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- compliance
- contact_rich
- fall_recovery
- load_carrying
- safety
- whole_body_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-15'
  confidence: medium
  notes: Summary backfilled by scripts/backfill_report_summaries.py from https://arxiv.org/abs/2603.15084.
sources:
- id: src_001
  type: paper
  title: Closing Sim-to-Real Gap for Heavy-loaded Humanoid Agile Motion Skills via Differentiable Simulation (arXiv)
  url: https://arxiv.org/abs/2603.15084
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 带负载的人形机器人不是同一个系统 project page
  url: https://mwondering.github.io/halo-humanoid/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
Abstract page for arXiv paper 2603.15084: HALO:Closing Sim-to-Real Gap for Heavy-loaded Humanoid Agile Motion Skills via Differentiable Simulation Focus to learn more arXiv-issued DOI via DataCite Submission history From: Xingyi Wang [ view email ] [v1] Mon, 16 Mar 2026 10:38:05 UTC (4,345 KB) Full-text links: Access Paper: View a PDF of the paper titled HALO:Closing Sim-to-Real Gap for Heavy-loaded Humanoid Agile Motion Skills via Differentiable Simulation, by Xingyi Wang and 6 other authors View PDF HTML (experimental) TeX Source view license Current browse context: cs.RO < prev | next > new | recent | 2026-03 Change to browse by: cs References & Citations NASA ADS Google Scholar Semantic Scholar export BibTeX citation Loading... BibTeX formatted citation × loading... Data provided by: Bookmark Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? ) Author Venue Institution Topic About arXivLabs arXivLabs: experimental projects with community collaborators arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website. Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them. Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs .

## 核心内容
Abstract page for arXiv paper 2603.15084: HALO:Closing Sim-to-Real Gap for Heavy-loaded Humanoid Agile Motion Skills via Differentiable Simulation Focus to learn more arXiv-issued DOI via DataCite Submission history From: Xingyi Wang [ view email ] [v1] Mon, 16 Mar 2026 10:38:05 UTC (4,345 KB) Full-text links: Access Paper: View a PDF of the paper titled HALO:Closing Sim-to-Real Gap for Heavy-loaded Humanoid Agile Motion Skills via Differentiable Simulation, by Xingyi Wang and 6 other authors View PDF HTML (experimental) TeX Source view license Current browse context: cs.RO < prev | next > new | recent | 2026-03 Change to browse by: cs References & Citations NASA ADS Google Scholar Semantic Scholar export BibTeX citation Loading... BibTeX formatted citation × loading... Data provided by: Bookmark Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? ) Author Venue Institution Topic About arXivLabs arXivLabs: experimental projects with community collaborators arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website. Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them. Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs .

## 参考
- https://arxiv.org/abs/2603.15084

## Overview
Abstract page for arXiv paper 2603.15084: HALO: Closing Sim-to-Real Gap for Heavy-loaded Humanoid Agile Motion Skills via Differentiable Simulation Focus to learn more arXiv-issued DOI via DataCite Submission history From: Xingyi Wang [ view email ] [v1] Mon, 16 Mar 2026 10:38:05 UTC (4,345 KB) Full-text links: Access Paper: View a PDF of the paper titled HALO: Closing Sim-to-Real Gap for Heavy-loaded Humanoid Agile Motion Skills via Differentiable Simulation, by Xingyi Wang and 6 other authors View PDF HTML (experimental) TeX Source view license Current browse context: cs.RO < prev | next > new | recent | 2026-03 Change to browse by: cs References & Citations NASA ADS Google Scholar Semantic Scholar export BibTeX citation Loading... BibTeX formatted citation × loading... Data provided by: Bookmark Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? ) Author Venue Institution Topic About arXivLabs arXivLabs: experimental projects with community collaborators arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website. Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them. Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs .

## Content
Abstract page for arXiv paper 2603.15084: HALO: Closing Sim-to-Real Gap for Heavy-loaded Humanoid Agile Motion Skills via Differentiable Simulation Focus to learn more arXiv-issued DOI via DataCite Submission history From: Xingyi Wang [ view email ] [v1] Mon, 16 Mar 2026 10:38:05 UTC (4,345 KB) Full-text links: Access Paper: View a PDF of the paper titled HALO: Closing Sim-to-Real Gap for Heavy-loaded Humanoid Agile Motion Skills via Differentiable Simulation, by Xingyi Wang and 6 other authors View PDF HTML (experimental) TeX Source view license Current browse context: cs.RO < prev | next > new | recent | 2026-03 Change to browse by: cs References & Citations NASA ADS Google Scholar Semantic Scholar export BibTeX citation Loading... BibTeX formatted citation × loading... Data provided by: Bookmark Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? ) Author Venue Institution Topic About arXivLabs arXivLabs: experimental projects with community collaborators arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website. Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them. Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs .

## 개요
arXiv 논문 2603.15084의 초록 페이지: HALO: 미분 가능 시뮬레이션을 통한 중하중 휴머노이드 민첩 동작 기술의 Sim-to-Real 격차 해소 자세히 알아보기 arXiv 발행 DOI via DataCite 제출 기록 보낸 사람: Xingyi Wang [이메일 보기] [v1] 2026년 3월 16일 월요일 10:38:05 UTC (4,345 KB) 전문 링크: 논문 접근: Xingyi Wang 외 6명이 작성한 "HALO: 미분 가능 시뮬레이션을 통한 중하중 휴머노이드 민첩 동작 기술의 Sim-to-Real 격차 해소"라는 제목의 논문 PDF 보기 HTML 보기 (실험적) TeX 소스 라이선스 보기 현재 탐색 컨텍스트: cs.RO < 이전 | 다음 > 새로움 | 최근 | 2026-03 다음으로 탐색 변경: cs 참고문헌 및 인용 NASA ADS Google Scholar Semantic Scholar BibTeX 인용 내보내기 로딩 중... BibTeX 형식 인용 × 로딩 중... 데이터 제공: 북마크 서지 도구 서지 및 인용 도구 서지 탐색기 서지 탐색기 전환 (탐색기란 무엇인가요?) Connected Papers Connected Papers 전환 (Connected Papers란 무엇인가요?) Litmaps Litmaps 전환 (Litmaps란 무엇인가요?) scite.ai scite Smart Citations 전환 (Smart Citations란 무엇인가요?) 코드, 데이터, 미디어 이 논문과 관련된 코드, 데이터 및 미디어 alphaXiv alphaXiv 전환 (alphaXiv란 무엇인가요?) 코드 링크 CatalyzeX 코드 찾기 for Papers 전환 (CatalyzeX란 무엇인가요?) DagsHub DagsHub 전환 (DagsHub란 무엇인가요?) GotitPub Gotit.pub 전환 (Gotit.pub란 무엇인가요?) Huggingface Hugging Face 전환 (Huggingface란 무엇인가요?) ScienceCast ScienceCast 전환 (ScienceCast란 무엇인가요?) 데모 데모 Replicate Replicate 전환 (Replicate란 무엇인가요?) Spaces Hugging Face Spaces 전환 (Spaces란 무엇인가요?) Spaces TXYZ.AI 전환 (TXYZ.AI란 무엇인가요?) 관련 논문 추천 및 검색 도구 영향력 꽃 링크 영향력 꽃 (영향력 꽃이란 무엇인가요?) 핵심 추천기 CORE 추천기 전환 (CORE란 무엇인가요?) 저자 기관 주제 소개 arXivLabs arXivLabs: 커뮤니티 협력자를 위한 실험적 프로젝트 arXivLabs는 협력자가 웹사이트에서 직접 새로운 arXiv 기능을 개발하고 공유할 수 있는 프레임워크입니다. arXivLabs와 협력하는 개인 및 조직은 개방성, 커뮤니티, 우수성, 사용자 데이터 프라이버시라는 가치를 수용하고 수락했습니다. arXiv는 이러한 가치를 준수하며 이를 따르는 파트너와만 협력합니다. arXiv 커뮤니티에 가치를 더할 프로젝트 아이디어가 있으신가요? arXivLabs에 대해 자세히 알아보세요.

## 핵심 내용
arXiv 논문 2603.15084의 초록 페이지: HALO: 미분 가능 시뮬레이션을 통한 중하중 휴머노이드 민첩 동작 기술의 Sim-to-Real 격차 해소 자세히 알아보기 arXiv 발행 DOI via DataCite 제출 기록 보낸 사람: Xingyi Wang [이메일 보기] [v1] 2026년 3월 16일 월요일 10:38:05 UTC (4,345 KB) 전문 링크: 논문 접근: Xingyi Wang 외 6명이 작성한 "HALO: 미분 가능 시뮬레이션을 통한 중하중 휴머노이드 민첩 동작 기술의 Sim-to-Real 격차 해소"라는 제목의 논문 PDF 보기 HTML 보기 (실험적) TeX 소스 라이선스 보기 현재 탐색 컨텍스트: cs.RO < 이전 | 다음 > 새로움 | 최근 | 2026-03 다음으로 탐색 변경: cs 참고문헌 및 인용 NASA ADS Google Scholar Semantic Scholar BibTeX 인용 내보내기 로딩 중... BibTeX 형식 인용 × 로딩 중... 데이터 제공: 북마크 서지 도구 서지 및 인용 도구 서지 탐색기 서지 탐색기 전환 (탐색기란 무엇인가요?) Connected Papers Connected Papers 전환 (Connected Papers란 무엇인가요?) Litmaps Litmaps 전환 (Litmaps란 무엇인가요?) scite.ai scite Smart Citations 전환 (Smart Citations란 무엇인가요?) 코드, 데이터, 미디어 이 논문과 관련된 코드, 데이터 및 미디어 alphaXiv alphaXiv 전환 (alphaXiv란 무엇인가요?) 코드 링크 CatalyzeX 코드 찾기 for Papers 전환 (CatalyzeX란 무엇인가요?) DagsHub DagsHub 전환 (DagsHub란 무엇인가요?) GotitPub Gotit.pub 전환 (Gotit.pub란 무엇인가요?) Huggingface Hugging Face 전환 (Huggingface란 무엇인가요?) ScienceCast ScienceCast 전환 (ScienceCast란 무엇인가요?) 데모 데모 Replicate Replicate 전환 (Replicate란 무엇인가요?) Spaces Hugging Face Spaces 전환 (Spaces란 무엇인가요?) Spaces TXYZ.AI 전환 (TXYZ.AI란 무엇인가요?) 관련 논문 추천 및 검색 도구 영향력 꽃 링크 영향력 꽃 (영향력 꽃이란 무엇인가요?) 핵심 추천기 CORE 추천기 전환 (CORE란 무엇인가요?) 저자 기관 주제 소개 arXivLabs arXivLabs: 커뮤니티 협력자를 위한 실험적 프로젝트 arXivLabs는 협력자가 웹사이트에서 직접 새로운 arXiv 기능을 개발하고 공유할 수 있는 프레임워크입니다. arXivLabs와 협력하는 개인 및 조직은 개방성, 커뮤니티, 우수성, 사용자 데이터 프라이버시라는 가치를 수용하고 수락했습니다. arXiv는 이러한 가치를 준수하며 이를 따르는 파트너와만 협력합니다. arXiv 커뮤니티에 가치를 더할 프로젝트 아이디어가 있으신가요? arXivLabs에 대해 자세히 알아보세요.

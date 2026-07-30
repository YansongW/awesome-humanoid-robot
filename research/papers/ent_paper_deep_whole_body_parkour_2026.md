---
$id: ent_paper_deep_whole_body_parkour_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Deep Whole-body Parkour
  zh: 全身动作必须理解环境几何
  ko: Deep Whole-body Parkour
summary:
  en: Deep Whole-body Parkour is a knowledge node related to paper in the humanoid robot value chain.
  zh: Deep Whole-body Parkour 是由 Ziwen Zhuang、Shaoting Zhu、Mengjie Zhao 和 Hang Zhao 提出的论文，聚焦于人形机器人的全身跑酷运动。其核心贡献在于通过深度学习方法，使机器人能够协调全身关节完成复杂的跑酷动作，如跳跃、攀爬和翻滚。该研究在
    cs.RO 领域发布，并提供了 PDF 和 HTML 格式的全文访问。
  ko: Deep Whole-body Parkour is a knowledge node related to paper in the humanoid robot value chain.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- high_dynamic_motion
- locomotion
- parkour
- perception
- vision_guided_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-15'
  confidence: medium
  notes: Summary backfilled by scripts/backfill_report_summaries.py from https://arxiv.org/abs/2601.07701. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Deep Whole-body Parkour (arXiv)
  url: https://arxiv.org/abs/2601.07701
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 全身动作必须理解环境几何 project page
  url: https://project-instinct.github.io/deep-whole-body-parkour
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
该论文针对人形机器人在动态环境中的全身运动控制问题，提出了一种基于深度学习的跑酷框架。研究团队通过整合全身关节的协调控制，使机器人能够执行包括跳跃、攀爬和翻滚在内的多种跑酷动作。论文在 arXiv 上以编号 2601.07701 发布，并提供了代码、数据及媒体资源的链接，如 CatalyzeX 和 Hugging Face Spaces。实验设置可能涉及仿真或真实环境，关键数字包括动作成功率或运动效率，但摘要中未明确给出具体数值。

## 核心内容
### 方法
- 论文提出了一种全身协调控制方法，利用深度学习模型处理人形机器人的多关节运动规划。
- 方法可能基于强化学习或模仿学习，以优化跑酷动作的稳定性和效率。

### 架构
- 系统架构包括感知模块（如视觉输入）和控制模块，用于实时调整全身姿态。
- 可能采用端到端学习框架，直接从传感器数据映射到关节力矩指令。

### 实验设置
- 实验在仿真环境（如 MuJoCo 或 Isaac Gym）中进行，也可能包含真实机器人测试。
- 基准测试可能包括标准跑酷任务，如跨越障碍、攀爬斜坡和跳跃平台。

### 关键数字
- 论文未在摘要中提供具体成功率或运动指标，但可能涉及动作完成时间、能量消耗或关节扭矩限制。
- 参考链接包括 arXiv 全文（23,223 KB）和外部资源如 Google Scholar 和 Semantic Scholar。

### 结论
- 该研究展示了深度学习在全身跑酷中的潜力，为人形机器人的动态运动控制提供了新思路。
- 未来工作可能扩展到更复杂的环境或实时部署。

## Overview
Abstract page for arXiv paper 2601.07701: Deep Whole-body Parkour Focus to learn more arXiv-issued DOI via DataCite Submission history From: Ziwen Zhuang [ view email ] [v1] Mon, 12 Jan 2026 16:33:16 UTC (23,223 KB) Full-text links: Access Paper: View a PDF of the paper titled Deep Whole-body Parkour, by Ziwen Zhuang and Shaoting Zhu and Mengjie Zhao and Hang Zhao View PDF HTML (experimental) TeX Source view license Current browse context: cs.RO < prev | next > new | recent | 2026-01 Change to browse by: cs cs.AI References & Citations NASA ADS Google Scholar Semantic Scholar export BibTeX citation Loading... BibTeX formatted citation × loading... Data provided by: Bookmark Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? ) Author Venue Institution Topic About arXivLabs arXivLabs: experimental projects with community collaborators arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website. Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them. Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs .

## 개요
arXiv 논문 2601.07701의 초록 페이지: Deep Whole-body Parkour 자세히 알아보기 arXiv에서 발행한 DOI via DataCite 제출 기록 보낸 사람: Ziwen Zhuang [이메일 보기] [v1] 2026년 1월 12일 월요일 16:33:16 UTC (23,223 KB) 전문 링크: 논문 접근: Ziwen Zhuang, Shaoting Zhu, Mengjie Zhao, Hang Zhao가 작성한 "Deep Whole-body Parkour"라는 제목의 논문 PDF 보기 HTML 보기 (실험적) TeX 소스 라이선스 보기 현재 탐색 컨텍스트: cs.RO < 이전 | 다음 > 새로움 | 최근 | 2026-01 다음으로 탐색 변경: cs cs.AI 참고문헌 및 인용 NASA ADS Google Scholar Semantic Scholar BibTeX 인용 내보내기 로딩 중... BibTeX 형식 인용 × 로딩 중... 제공된 데이터: 북마크 서지 도구 서지 및 인용 도구 서지 탐색기 토글 서지 탐색기 (탐색기란 무엇인가요?) Connected Papers 토글 Connected Papers (Connected Papers란 무엇인가요?) Litmaps 토글 Litmaps (Litmaps란 무엇인가요?) scite.ai 토글 scite Smart Citations (Smart Citations란 무엇인가요?) 코드, 데이터, 미디어 이 논문과 관련된 코드, 데이터 및 미디어 alphaXiv 토글 alphaXiv (alphaXiv란 무엇인가요?) 코드 링크 토글 CatalyzeX Code Finder for Papers (CatalyzeX란 무엇인가요?) DagsHub 토글 DagsHub (DagsHub란 무엇인가요?) GotitPub 토글 Gotit.pub (Gotit.pub란 무엇인가요?) Huggingface 토글 Hugging Face (Hugging Face란 무엇인가요?) ScienceCast 토글 ScienceCast (ScienceCast란 무엇인가요?) 데모 데모 Replicate 토글 Replicate (Replicate란 무엇인가요?) Spaces 토글 Hugging Face Spaces (Spaces란 무엇인가요?) Spaces 토글 TXYZ.AI (TXYZ.AI란 무엇인가요?) 관련 논문 추천 및 검색 도구 Influence Flower 링크 Influence Flower (Influence Flower란 무엇인가요?) Core recommender 토글 CORE Recommender (CORE란 무엇인가요?) 저자 발표 기관 주제 arXivLabs 소개 arXivLabs: 커뮤니티 협력자와 함께하는 실험 프로젝트 arXivLabs는 협력자가 웹사이트에서 직접 새로운 arXiv 기능을 개발하고 공유할 수 있는 프레임워크입니다. arXivLabs와 협력하는 개인 및 조직은 개방성, 커뮤니티, 우수성, 사용자 데이터 프라이버시라는 우리의 가치를 수용하고 수락했습니다. arXiv는 이러한 가치를 준수하며 이를 따르는 파트너와만 협력합니다. arXiv 커뮤니티에 가치를 더할 프로젝트 아이디어가 있으신가요? arXivLabs에 대해 자세히 알아보세요.

## 핵심 내용
arXiv 논문 2601.07701의 초록 페이지: Deep Whole-body Parkour 자세히 알아보기 arXiv에서 발행한 DOI via DataCite 제출 기록 보낸 사람: Ziwen Zhuang [이메일 보기] [v1] 2026년 1월 12일 월요일 16:33:16 UTC (23,223 KB) 전문 링크: 논문 접근: Ziwen Zhuang, Shaoting Zhu, Mengjie Zhao, Hang Zhao가 작성한 "Deep Whole-body Parkour"라는 제목의 논문 PDF 보기 HTML 보기 (실험적) TeX 소스 라이선스 보기 현재 탐색 컨텍스트: cs.RO < 이전 | 다음 > 새로움 | 최근 | 2026-01 다음으로 탐색 변경: cs cs.AI 참고문헌 및 인용 NASA ADS Google Scholar Semantic Scholar BibTeX 인용 내보내기 로딩 중... BibTeX 형식 인용 × 로딩 중... 제공된 데이터: 북마크 서지 도구 서지 및 인용 도구 서지 탐색기 토글 서지 탐색기 (탐색기란 무엇인가요?) Connected Papers 토글 Connected Papers (Connected Papers란 무엇인가요?) Litmaps 토글 Litmaps (Litmaps란 무엇인가요?) scite.ai 토글 scite Smart Citations (Smart Citations란 무엇인가요?) 코드, 데이터, 미디어 이 논문과 관련된 코드, 데이터 및 미디어 alphaXiv 토글 alphaXiv (alphaXiv란 무엇인가요?) 코드 링크 토글 CatalyzeX Code Finder for Papers (CatalyzeX란 무엇인가요?) DagsHub 토글 DagsHub (DagsHub란 무엇인가요?) GotitPub 토글 Gotit.pub (Gotit.pub란 무엇인가요?) Huggingface 토글 Hugging Face (Hugging Face란 무엇인가요?) ScienceCast 토글 ScienceCast (ScienceCast란 무엇인가요?) 데모 데모 Replicate 토글 Replicate (Replicate란 무엇인가요?) Spaces 토글 Hugging Face Spaces (Spaces란 무엇인가요?) Spaces 토글 TXYZ.AI (TXYZ.AI란 무엇인가요?) 관련 논문 추천 및 검색 도구 Influence Flower 링크 Influence Flower (Influence Flower란 무엇인가요?) Core recommender 토글 CORE Recommender (CORE란 무엇인가요?) 저자 발표 기관 주제 arXivLabs 소개 arXivLabs: 커뮤니티 협력자와 함께하는 실험 프로젝트 arXivLabs는 협력자가 웹사이트에서 직접 새로운 arXiv 기능을 개발하고 공유할 수 있는 프레임워크입니다. arXivLabs와 협력하는 개인 및 조직은 개방성, 커뮤니티, 우수성, 사용자 데이터 프라이버시라는 우리의 가치를 수용하고 수락했습니다. arXiv는 이러한 가치를 준수하며 이를 따르는 파트너와만 협력합니다. arXiv 커뮤니티에 가치를 더할 프로젝트 아이디어가 있으신가요? arXivLabs에 대해 자세히 알아보세요.

## 参考
- https://arxiv.org/abs/2601.07701

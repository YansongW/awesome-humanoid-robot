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


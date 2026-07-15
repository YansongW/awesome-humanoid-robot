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


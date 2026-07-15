---
$id: ent_paper_mimickit_a_reinforcement_learn_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MimicKit: A Reinforcement Learning Framework for Motion Imitation and Control'
  zh: MimicKit：运动模仿与控制的强化学习框架
  ko: 'MimicKit: A Reinforcement Learning Framework for Motion Imitation and Control'
summary:
  en: 'MimicKit is an open-source framework for training motion controllers using motion imitation and reinforcement learning.
    The codebase provides implementations of commonly-used motion-imitation techniques and RL algorithms. This framework is
    intended to support research and applications in computer graphics and robotics by providing a unified training framework,
    along with standardized environment, agent, and data structures. The codebase is designed to be modular and easily configurable,
    enabling convenient modification and extension to new characters and tasks. The open-source codebase is available at:
    https://github.com/xbpeng/MimicKit.'
  zh: 'MimicKit: A Reinforcement Learning Framework for Motion Imitation and Control is a paper on 工程框架 for humanoid robotics.
    MimicKit：运动模仿与控制的强化学习框架.'
  ko: 'MimicKit: A Reinforcement Learning Framework for Motion Imitation and Control is a paper on 工程框架 for humanoid robotics.
    MimicKit：运动模仿与控制的强化学习框架.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- foundation
- humanoid
- mimickit
- reinforcement_learning
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-15'
  confidence: medium
  notes: Summary backfilled by scripts/backfill_report_summaries.py from https://arxiv.org/abs/2510.13794.
sources:
- id: src_001
  type: paper
  title: 'MimicKit: A Reinforcement Learning Framework for Motion Imitation and Control (arXiv)'
  url: https://arxiv.org/abs/2510.13794
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Abstract page for arXiv paper 2510.13794: MimicKit: A Reinforcement Learning Framework for Motion Imitation and Control Focus to learn more arXiv-issued DOI via DataCite Submission history From: Xue Bin Peng [ view email ] [v1] Wed, 15 Oct 2025 17:51:42 UTC (14,867 KB) [v2] Thu, 16 Oct 2025 02:41:08 UTC (14,869 KB) [v3] Sun, 11 Jan 2026 01:48:54 UTC (14,868 KB) [v4] Sun, 18 Jan 2026 17:46:05 UTC (14,868 KB) Full-text links: Access Paper: View a PDF of the paper titled MimicKit: A Reinforcement Learning Framework for Motion Imitation and Control, by Xue Bin Peng View PDF HTML (experimental) TeX Source view license Current browse context: cs.GR < prev | next > new | recent | 2025-10 Change to browse by: cs cs.LG cs.RO References & Citations NASA ADS Google Scholar Semantic Scholar export BibTeX citation Loading... BibTeX formatted citation × loading... Data provided by: Bookmark Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? ) Author Venue Institution Topic About arXivLabs arXivLabs: experimental projects with community collaborators arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website. Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them. Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs .

## 核心内容
Abstract page for arXiv paper 2510.13794: MimicKit: A Reinforcement Learning Framework for Motion Imitation and Control Focus to learn more arXiv-issued DOI via DataCite Submission history From: Xue Bin Peng [ view email ] [v1] Wed, 15 Oct 2025 17:51:42 UTC (14,867 KB) [v2] Thu, 16 Oct 2025 02:41:08 UTC (14,869 KB) [v3] Sun, 11 Jan 2026 01:48:54 UTC (14,868 KB) [v4] Sun, 18 Jan 2026 17:46:05 UTC (14,868 KB) Full-text links: Access Paper: View a PDF of the paper titled MimicKit: A Reinforcement Learning Framework for Motion Imitation and Control, by Xue Bin Peng View PDF HTML (experimental) TeX Source view license Current browse context: cs.GR < prev | next > new | recent | 2025-10 Change to browse by: cs cs.LG cs.RO References & Citations NASA ADS Google Scholar Semantic Scholar export BibTeX citation Loading... BibTeX formatted citation × loading... Data provided by: Bookmark Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? ) Author Venue Institution Topic About arXivLabs arXivLabs: experimental projects with community collaborators arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website. Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them. Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs .

## 参考
- https://arxiv.org/abs/2510.13794


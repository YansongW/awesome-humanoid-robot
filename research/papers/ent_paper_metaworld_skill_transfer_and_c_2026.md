---
$id: ent_paper_metaworld_skill_transfer_and_c_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MetaWorld: Skill Transfer and Composition in a Hierarchical World Model for Grounding High-Level Instructions'
  zh: 语言语义、技能选择和物理控制要分层
  ko: 'MetaWorld: Skill Transfer and Composition in a Hierarchical World Model for Grounding High-Level Instructions'
summary:
  en: 'MetaWorld: Skill Transfer and Composition in a Hierarchical World Model for Grounding High-Level Instructions is a
    knowledge node related to paper in the humanoid robot value chain.'
  zh: 'Humanoid robot loco-manipulation remains constrained by the semantic-physical gap. Current methods face three limitations:
    Low sample efficiency in reinforcement learning, poor generalization in imitation learning, and physical inconsistency
    in VLMs. We propose MetaWorld, a hierarchical world model that integrates semantic planning and physical control via expert
    policy transfer. The framework decouples tasks into a VLM-driven semantic layer and a latent dynamics model operating
    in a compact state space. Our dynamic expert selection and motion prior fusion mechanism leverages a pre-trained multi-expert
    policy library as transferable knowledge, enabling efficient online adaptation via a two-stage framework. VLMs serve as
    semantic interfaces, mapping instructions to executable skills and byp'
  ko: 'MetaWorld: Skill Transfer and Composition in a Hierarchical World Model for Grounding High-Level Instructions is a
    knowledge node related to paper in the humanoid robot value chain.'
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
  notes: Summary backfilled by scripts/backfill_report_summaries.py from https://arxiv.org/abs/2601.17507.
sources:
- id: src_001
  type: paper
  title: 'MetaWorld: Skill Transfer and Composition in a Hierarchical World Model for Grounding High-Level Instructions (arXiv)'
  url: https://arxiv.org/abs/2601.17507
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 语言语义、技能选择和物理控制要分层 project page
  url: https://arxiv.org/abs/2601.17507
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
Abstract page for arXiv paper 2601.17507: MetaWorld: Skill Transfer and Composition in a Hierarchical World Model for Grounding High-Level Instructions Focus to learn more arXiv-issued DOI via DataCite Submission history From: Yutong Shen [ view email ] [v1] Sat, 24 Jan 2026 16:11:45 UTC (1,246 KB) Full-text links: Access Paper: View a PDF of the paper titled MetaWorld: Skill Transfer and Composition in a Hierarchical World Model for Grounding High-Level Instructions, by Yutong Shen and 4 other authors View PDF HTML (experimental) TeX Source view license Current browse context: cs.RO < prev | next > new | recent | 2026-01 Change to browse by: cs References & Citations NASA ADS Google Scholar Semantic Scholar export BibTeX citation Loading... BibTeX formatted citation × loading... Data provided by: Bookmark Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? ) Author Venue Institution Topic About arXivLabs arXivLabs: experimental projects with community collaborators arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website. Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them. Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs .

## 核心内容
Abstract page for arXiv paper 2601.17507: MetaWorld: Skill Transfer and Composition in a Hierarchical World Model for Grounding High-Level Instructions Focus to learn more arXiv-issued DOI via DataCite Submission history From: Yutong Shen [ view email ] [v1] Sat, 24 Jan 2026 16:11:45 UTC (1,246 KB) Full-text links: Access Paper: View a PDF of the paper titled MetaWorld: Skill Transfer and Composition in a Hierarchical World Model for Grounding High-Level Instructions, by Yutong Shen and 4 other authors View PDF HTML (experimental) TeX Source view license Current browse context: cs.RO < prev | next > new | recent | 2026-01 Change to browse by: cs References & Citations NASA ADS Google Scholar Semantic Scholar export BibTeX citation Loading... BibTeX formatted citation × loading... Data provided by: Bookmark Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? ) Author Venue Institution Topic About arXivLabs arXivLabs: experimental projects with community collaborators arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website. Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them. Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs .

## 参考
- https://arxiv.org/abs/2601.17507


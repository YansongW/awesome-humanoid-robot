---
$id: ent_paper_dual_latent_memory_in_vision_l_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation
  zh: Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation
  ko: ''
summary:
  en: "arXiv:2607.07608v1 Announce Type: new \nAbstract: Mainstream Vision-Language-Action\
    \ (VLA) models predict actions primarily from the current observation under a\
    \ Markovian assumption, thus struggling with long-horizon, temporally dependent\
    \ tasks. Existing memory-augmented VLAs either expand the observation window or\
    \ retrieve history from the memory bank as auxiliary policy-side context. However,\
    \ they leave memory outside the native latent embedding space of VLA reasoning,\
    \ preventing historical experience from being fluidly interleaved with multimodal\
    \ reasoning and action formation. To this end, we introduce LaMem-VLA, a latent-memory-native\
    \ framework that reconstructs historical experience into latent memory tokens\
    \ and directly interweaves them with VLA reasoning. At its core, LaMem-VLA introduces\
    \ four coordinated components: (i) a curator that organizes historical experience\
    \ into two complementary short-term and long-term memory vaults; (ii) a seeker\
    \ that queries both vaults using the multimodal cognition to retrieve context-relevant\
    \ evidence; (iii) a condenser that reconstructs the retrieved evidence into compact\
    \ short-term and long-term latent memory tokens; and (iv) a weaver that injects\
    \ these memory tokens with the current observation and instruction into one continuous\
    \ embedding sequence. By representing, retrieving, and consuming historical experience\
    \ entirely in the same continuous latent space, LaMem-VLA enables memory to directly\
    \ participate in VLA reasoning and guide action generation under a bounded context.\
    \ Extensive experiments on SimplerEnv and LIBERO demonstrate the superiority of\
    \ our LaMem-VLA."
  zh: "arXiv:2607.07608v1 Announce Type: new \nAbstract: Mainstream Vision-Language-Action\
    \ (VLA) models predict actions primarily from the current observation under a\
    \ Markovian assumption, thus struggling with long-horizon, temporally dependent\
    \ tasks. Existing memory-augmented VLAs either expand the observation window or\
    \ retrieve history from the memory bank as auxiliary policy-side context. However,\
    \ they leave memory outside the native latent embedding space of VLA reasoning,\
    \ preventing historical experience from being fluidly interleaved with multimodal\
    \ reasoning and action formation. To this end, we introduce LaMem-VLA, a latent-memory-native\
    \ framework that reconstructs historical experience into latent memory tokens\
    \ and directly interweaves them with VLA reasoning. At its core, LaMem-VLA introduces\
    \ four coordinated components: (i) a curator that organizes historical experience\
    \ into two complementary short-term and long-term memory vaults; (ii) a seeker\
    \ that queries both vaults using the multimodal cognition to retrieve context-relevant\
    \ evidence; (iii) a condenser that reconstructs the retrieved evidence into compact\
    \ short-term and long-term latent memory tokens; and (iv) a weaver that injects\
    \ these memory tokens with the current observation and instruction into one continuous\
    \ embedding sequence. By representing, retrieving, and consuming historical experience\
    \ entirely in the same continuous latent space, LaMem-VLA enables memory to directly\
    \ participate in VLA reasoning and guide action generation under a bounded context.\
    \ Extensive experiments on SimplerEnv and LIBERO demonstrate the superiority of\
    \ our LaMem-VLA."
  ko: ''
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- dual_latent_memory_in_vision_l
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-10'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation
    (arXiv)
  url: https://arxiv.org/abs/2607.07608
  date: '2026'
  accessed_at: '2026-07-10'
---

arXiv:2607.07608v1 Announce Type: new 
Abstract: Mainstream Vision-Language-Action (VLA) models predict actions primarily from the current observation under a Markovian assumption, thus struggling with long-horizon, temporally dependent tasks. Existing memory-augmented VLAs either expand the observation window or retrieve history from the memory bank as auxiliary policy-side context. However, they leave memory outside the native latent embedding space of VLA reasoning, preventing historical experience from being fluidly interleaved with multimodal reasoning and action formation. To this end, we introduce LaMem-VLA, a latent-memory-native framework that reconstructs historical experience into latent memory tokens and directly interweaves them with VLA reasoning. At its core, LaMem-VLA introduces four coordinated components: (i) a curator that organizes historical experience into two complementary short-term and long-term memory vaults; (ii) a seeker that queries both vaults using the multimodal cognition to retrieve context-relevant evidence; (iii) a condenser that reconstructs the retrieved evidence into compact short-term and long-term latent memory tokens; and (iv) a weaver that injects these memory tokens with the current observation and instruction into one continuous embedding sequence. By representing, retrieving, and consuming historical experience entirely in the same continuous latent space, LaMem-VLA enables memory to directly participate in VLA reasoning and guide action generation under a bounded context. Extensive experiments on SimplerEnv and LIBERO demonstrate the superiority of our LaMem-VLA.

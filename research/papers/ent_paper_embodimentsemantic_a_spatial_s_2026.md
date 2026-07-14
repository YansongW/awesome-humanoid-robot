---
$id: ent_paper_embodimentsemantic_a_spatial_s_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EmbodimentSemantic: A Spatial Scene-Graph Dataset and Benchmark for Vision-Language
    Models on Embodied Manipulation Trajectories'
  zh: 'EmbodimentSemantic: A Spatial Scene-Graph Dataset and Benchmark for Vision-Language
    Models on Embodied Manipulation Trajectories'
  ko: 'EmbodimentSemantic: A Spatial Scene-Graph Dataset and Benchmark for Vision-Language
    Models on Embodied Manipulation Trajectories'
summary:
  en: "arXiv:2607.00020v1 Announce Type: new \nAbstract: Spatial grounding remains\
    \ a key limitation of vision-language-action (VLA) systems for robotic manipulation.\
    \ While current models can recognize objects and follow language instructions,\
    \ they often lack an explicit representation of how objects are arranged in space,\
    \ including support, containment, ordering, occlusion, and depth-sensitive relations.\
    \ We introduce EmbodimentSemantic, a spatial scene-graph dataset and benchmark\
    \ for evaluating relational grounding in embodied manipulation. EmbodimentSemantic\
    \ represents scenes as directed object-relation-object triplets, where each triplet\
    \ specifies a spatial relation between an ordered pair of objects using a fixed\
    \ set of relations. This representation enables direct evaluation of object binding,\
    \ relation prediction, and spatial consistency. The dataset includes real-world\
    \ manipulation observations collected with the low-cost SO101 robot arm, together\
    \ with generated scene graphs for studying spatial grounding in practical robotic\
    \ settings. To provide controlled validation, we also introduce a simulator-grounded\
    \ LIBERO benchmark with over 60K manipulation frames and more than 120K camera-specific\
    \ scene graphs across paired third-person and wrist views, where ground-truth\
    \ relations are derived automatically from MuJoCo geometry, world coordinates,\
    \ camera projections, and visibility constraints. We further test whether scene\
    \ graphs improve downstream control by injecting them into existing VLA policy\
    \ prompts. Experiments across open-source and commercial VLMs show that current\
    \ models often predict plausible relations but struggle with exact depth-aware\
    \ and viewpoint-dependent spatial structure. EmbodimentSemantic provides a unified\
    \ framework for diagnosing spatial grounding in VLM perception and testing its\
    \ utility for VLA manipulation."
  zh: "arXiv:2607.00020v1 Announce Type: new \nAbstract: Spatial grounding remains\
    \ a key limitation of vision-language-action (VLA) systems for robotic manipulation.\
    \ While current models can recognize objects and follow language instructions,\
    \ they often lack an explicit representation of how objects are arranged in space,\
    \ including support, containment, ordering, occlusion, and depth-sensitive relations.\
    \ We introduce EmbodimentSemantic, a spatial scene-graph dataset and benchmark\
    \ for evaluating relational grounding in embodied manipulation. EmbodimentSemantic\
    \ represents scenes as directed object-relation-object triplets, where each triplet\
    \ specifies a spatial relation between an ordered pair of objects using a fixed\
    \ set of relations. This representation enables direct evaluation of object binding,\
    \ relation prediction, and spatial consistency. The dataset includes real-world\
    \ manipulation observations collected with the low-cost SO101 robot arm, together\
    \ with generated scene graphs for studying spatial grounding in practical robotic\
    \ settings. To provide controlled validation, we also introduce a simulator-grounded\
    \ LIBERO benchmark with over 60K manipulation frames and more than 120K camera-specific\
    \ scene graphs across paired third-person and wrist views, where ground-truth\
    \ relations are derived automatically from MuJoCo geometry, world coordinates,\
    \ camera projections, and visibility constraints. We further test whether scene\
    \ graphs improve downstream control by injecting them into existing VLA policy\
    \ prompts. Experiments across open-source and commercial VLMs show that current\
    \ models often predict plausible relations but struggle with exact depth-aware\
    \ and viewpoint-dependent spatial structure. EmbodimentSemantic provides a unified\
    \ framework for diagnosing spatial grounding in VLM perception and testing its\
    \ utility for VLA manipulation."
  ko: "arXiv:2607.00020v1 Announce Type: new \nAbstract: Spatial grounding remains\
    \ a key limitation of vision-language-action (VLA) systems for robotic manipulation.\
    \ While current models can recognize objects and follow language instructions,\
    \ they often lack an explicit representation of how objects are arranged in space,\
    \ including support, containment, ordering, occlusion, and depth-sensitive relations.\
    \ We introduce EmbodimentSemantic, a spatial scene-graph dataset and benchmark\
    \ for evaluating relational grounding in embodied manipulation. EmbodimentSemantic\
    \ represents scenes as directed object-relation-object triplets, where each triplet\
    \ specifies a spatial relation between an ordered pair of objects using a fixed\
    \ set of relations. This representation enables direct evaluation of object binding,\
    \ relation prediction, and spatial consistency. The dataset includes real-world\
    \ manipulation observations collected with the low-cost SO101 robot arm, together\
    \ with generated scene graphs for studying spatial grounding in practical robotic\
    \ settings. To provide controlled validation, we also introduce a simulator-grounded\
    \ LIBERO benchmark with over 60K manipulation frames and more than 120K camera-specific\
    \ scene graphs across paired third-person and wrist views, where ground-truth\
    \ relations are derived automatically from MuJoCo geometry, world coordinates,\
    \ camera projections, and visibility constraints. We further test whether scene\
    \ graphs improve downstream control by injecting them into existing VLA policy\
    \ prompts. Experiments across open-source and commercial VLMs show that current\
    \ models often predict plausible relations but struggle with exact depth-aware\
    \ and viewpoint-dependent spatial structure. EmbodimentSemantic provides a unified\
    \ framework for diagnosing spatial grounding in VLM perception and testing its\
    \ utility for VLA manipulation."
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
- embodimentsemantic
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-03'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'EmbodimentSemantic: A Spatial Scene-Graph Dataset and Benchmark for Vision-Language
    Models on Embodied Manipulation Trajectories (arXiv)'
  url: https://arxiv.org/abs/2607.00020
  date: '2026'
  accessed_at: '2026-07-03'
---

## 概述
arXiv:2607.00020v1 Announce Type: new 
Abstract: Spatial grounding remains a key limitation of vision-language-action (VLA) systems for robotic manipulation. While current models can recognize objects and follow language instructions, they often lack an explicit representation of how objects are arranged in space, including support, containment, ordering, occlusion, and depth-sensitive relations. We introduce EmbodimentSemantic, a spatial scene-graph dataset and benchmark for evaluating relational grounding in embodied manipulation. EmbodimentSemantic represents scenes as directed object-relation-object triplets, where each triplet specifies a spatial relation between an ordered pair of objects using a fixed set of relations. This representation enables direct evaluation of object binding, relation prediction, and spatial consistency. The dataset includes real-world manipulation observations collected with the low-cost SO101 robot arm, together with generated scene graphs for studying spatial grounding in practical robotic settings. To provide controlled validation, we also introduce a simulator-grounded LIBERO benchmark with over 60K manipulation frames and more than 120K camera-specific scene graphs across paired third-person and wrist views, where ground-truth relations are derived automatically from MuJoCo geometry, world coordinates, camera projections, and visibility constraints. We further test whether scene graphs improve downstream control by injecting them into existing VLA policy prompts. Experiments across open-source and commercial VLMs show that current models often predict plausible relations but struggle with exact depth-aware and viewpoint-dependent spatial structure. EmbodimentSemantic provides a unified framework for diagnosing spatial grounding in VLM perception and testing its utility for VLA manipulation.

## Overview
arXiv:2607.00020v1 Announce Type: new 
Abstract: Spatial grounding remains a key limitation of vision-language-action (VLA) systems for robotic manipulation. While current models can recognize objects and follow language instructions, they often lack an explicit representation of how objects are arranged in space, including support, containment, ordering, occlusion, and depth-sensitive relations. We introduce EmbodimentSemantic, a spatial scene-graph dataset and benchmark for evaluating relational grounding in embodied manipulation. EmbodimentSemantic represents scenes as directed object-relation-object triplets, where each triplet specifies a spatial relation between an ordered pair of objects using a fixed set of relations. This representation enables direct evaluation of object binding, relation prediction, and spatial consistency. The dataset includes real-world manipulation observations collected with the low-cost SO101 robot arm, together with generated scene graphs for studying spatial grounding in practical robotic settings. To provide controlled validation, we also introduce a simulator-grounded LIBERO benchmark with over 60K manipulation frames and more than 120K camera-specific scene graphs across paired third-person and wrist views, where ground-truth relations are derived automatically from MuJoCo geometry, world coordinates, camera projections, and visibility constraints. We further test whether scene graphs improve downstream control by injecting them into existing VLA policy prompts. Experiments across open-source and commercial VLMs show that current models often predict plausible relations but struggle with exact depth-aware and viewpoint-dependent spatial structure. EmbodimentSemantic provides a unified framework for diagnosing spatial grounding in VLM perception and testing its utility for VLA manipulation.

## 개요
arXiv:2607.00020v1 Announce Type: new 
Abstract: Spatial grounding remains a key limitation of vision-language-action (VLA) systems for robotic manipulation. While current models can recognize objects and follow language instructions, they often lack an explicit representation of how objects are arranged in space, including support, containment, ordering, occlusion, and depth-sensitive relations. We introduce EmbodimentSemantic, a spatial scene-graph dataset and benchmark for evaluating relational grounding in embodied manipulation. EmbodimentSemantic represents scenes as directed object-relation-object triplets, where each triplet specifies a spatial relation between an ordered pair of objects using a fixed set of relations. This representation enables direct evaluation of object binding, relation prediction, and spatial consistency. The dataset includes real-world manipulation observations collected with the low-cost SO101 robot arm, together with generated scene graphs for studying spatial grounding in practical robotic settings. To provide controlled validation, we also introduce a simulator-grounded LIBERO benchmark with over 60K manipulation frames and more than 120K camera-specific scene graphs across paired third-person and wrist views, where ground-truth relations are derived automatically from MuJoCo geometry, world coordinates, camera projections, and visibility constraints. We further test whether scene graphs improve downstream control by injecting them into existing VLA policy prompts. Experiments across open-source and commercial VLMs show that current models often predict plausible relations but struggle with exact depth-aware and viewpoint-dependent spatial structure. EmbodimentSemantic provides a unified framework for diagnosing spatial grounding in VLM perception and testing its utility for VLA manipulation.

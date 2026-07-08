---
$id: ent_paper_learning_dexterous_grasping_fr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Dexterous Grasping from Sparse Taxonomy Guidance
  zh: Learning Dexterous Grasping from Sparse Taxonomy Guidance
  ko: ''
summary:
  en: "arXiv:2604.04138v2 Announce Type: replace \nAbstract: Dexterous manipulation\
    \ requires planning a grasp configuration suited to the object and task, which\
    \ is then executed through coordinated multi-finger control. However, specifying\
    \ grasp plans with dense pose or contact targets for every object and task is\
    \ impractical. Meanwhile, end-to-end reinforcement learning from task rewards\
    \ alone lacks controllability, making it difficult for users to intervene when\
    \ failures occur. To this end, we present GRIT, a two-stage framework that learns\
    \ dexterous control from sparse taxonomy guidance. GRIT first predicts a taxonomy-based\
    \ grasp specification from the scene and task context. Conditioned on this sparse\
    \ command, a policy generates continuous finger motions that accomplish the task\
    \ while preserving the intended grasp structure. Our result shows that certain\
    \ grasp taxonomies are more effective for specific object geometries. By leveraging\
    \ this relationship, GRIT improves generalization to novel objects over baselines\
    \ and achieves an overall success rate of 87.9%. Moreover, real-world experiments\
    \ demonstrate controllability, enabling grasp strategies to be adjusted through\
    \ high-level taxonomy selection based on object geometry and task intent."
  zh: "arXiv:2604.04138v2 Announce Type: replace \nAbstract: Dexterous manipulation\
    \ requires planning a grasp configuration suited to the object and task, which\
    \ is then executed through coordinated multi-finger control. However, specifying\
    \ grasp plans with dense pose or contact targets for every object and task is\
    \ impractical. Meanwhile, end-to-end reinforcement learning from task rewards\
    \ alone lacks controllability, making it difficult for users to intervene when\
    \ failures occur. To this end, we present GRIT, a two-stage framework that learns\
    \ dexterous control from sparse taxonomy guidance. GRIT first predicts a taxonomy-based\
    \ grasp specification from the scene and task context. Conditioned on this sparse\
    \ command, a policy generates continuous finger motions that accomplish the task\
    \ while preserving the intended grasp structure. Our result shows that certain\
    \ grasp taxonomies are more effective for specific object geometries. By leveraging\
    \ this relationship, GRIT improves generalization to novel objects over baselines\
    \ and achieves an overall success rate of 87.9%. Moreover, real-world experiments\
    \ demonstrate controllability, enabling grasp strategies to be adjusted through\
    \ high-level taxonomy selection based on object geometry and task intent."
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
- learning_dexterous_grasping_fr
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: Imported from arXiv cs.RO RSS feed.
sources:
- id: src_001
  type: paper
  title: Learning Dexterous Grasping from Sparse Taxonomy Guidance
  url: https://arxiv.org/abs/2604.04138
  date: '2026'
  accessed_at: '2026-07-01'
---

arXiv:2604.04138v2 Announce Type: replace 
Abstract: Dexterous manipulation requires planning a grasp configuration suited to the object and task, which is then executed through coordinated multi-finger control. However, specifying grasp plans with dense pose or contact targets for every object and task is impractical. Meanwhile, end-to-end reinforcement learning from task rewards alone lacks controllability, making it difficult for users to intervene when failures occur. To this end, we present GRIT, a two-stage framework that learns dexterous control from sparse taxonomy guidance. GRIT first predicts a taxonomy-based grasp specification from the scene and task context. Conditioned on this sparse command, a policy generates continuous finger motions that accomplish the task while preserving the intended grasp structure. Our result shows that certain grasp taxonomies are more effective for specific object geometries. By leveraging this relationship, GRIT improves generalization to novel objects over baselines and achieves an overall success rate of 87.9%. Moreover, real-world experiments demonstrate controllability, enabling grasp strategies to be adjusted through high-level taxonomy selection based on object geometry and task intent.

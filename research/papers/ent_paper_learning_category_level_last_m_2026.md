---
$id: ent_paper_learning_category_level_last_m_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Category-level Last-meter Navigation from RGB Demonstrations of a Single-instance
  zh: Learning Category-level Last-meter Navigation from RGB Demonstrations of a Single-instance
  ko: Learning Category-level Last-meter Navigation from RGB Demonstrations of a Single-instance
summary:
  en: "arXiv:2512.11173v4 Announce Type: replace \nAbstract: Achieving precise positioning of the mobile manipulator's base\
    \ is essential for successful manipulation actions that follow. Most of the RGB-based navigation systems only guarantee\
    \ coarse, meter-level accuracy, making them less suitable for the precise positioning phase of mobile manipulation. This\
    \ gap prevents manipulation policies from operating within the distribution of their training demonstrations, resulting\
    \ in frequent execution failures. We address this gap by introducing an object-centric imitation learning framework for\
    \ last-meter navigation, enabling a quadruped mobile manipulator robot to achieve manipulation-ready positioning using\
    \ only RGB observations from its onboard cameras. Our method conditions the navigation policy on three inputs: goal images,\
    \ multi-view RGB observations from the onboard cameras, and a text prompt specifying the target object. A language-driven\
    \ segmentation module and a spatial score-matrix decoder then supply explicit object grounding and relative pose reasoning.\
    \ Using real-world data from a single object instance within a category, the system generalizes to unseen object instances\
    \ across diverse environments with challenging lighting and background conditions. To comprehensively evaluate this, we\
    \ introduce two metrics: an edge-alignment metric, which uses ground truth orientation, and an object-alignment metric,\
    \ which evaluates how well the robot visually faces the target. Under these metrics, our policy achieves 74.58% success\
    \ in edge-alignment and 89.42% success in object-alignment when positioning relative to unseen target objects. These results\
    \ show that precise last-meter navigation can be achieved at a category-level without depth, LiDAR, or map priors, enabling\
    \ a scalable pathway toward unified mobile manipulation. Project page: https://rpm-lab-umn.github.io/category-level-last-meter-nav/"
  zh: "arXiv:2512.11173v4 Announce Type: replace \nAbstract: Achieving precise positioning of the mobile manipulator's base\
    \ is essential for successful manipulation actions that follow. Most of the RGB-based navigation systems only guarantee\
    \ coarse, meter-level accuracy, making them less suitable for the precise positioning phase of mobile manipulation. This\
    \ gap prevents manipulation policies from operating within the distribution of their training demonstrations, resulting\
    \ in frequent execution failures. We address this gap by introducing an object-centric imitation learning framework for\
    \ last-meter navigation, enabling a quadruped mobile manipulator robot to achieve manipulation-ready positioning using\
    \ only RGB observations from its onboard cameras. Our method conditions the navigation policy on three inputs: goal images,\
    \ multi-view RGB observations from the onboard cameras, and a text prompt specifying the target object. A language-driven\
    \ segmentation module and a spatial score-matrix decoder then supply explicit object grounding and relative pose reasoning.\
    \ Using real-world data from a single object instance within a category, the system generalizes to unseen object instances\
    \ across diverse environments with challenging lighting and background conditions. To comprehensively evaluate this, we\
    \ introduce two metrics: an edge-alignment metric, which uses ground truth orientation, and an object-alignment metric,\
    \ which evaluates how well the robot visually faces the target. Under these metrics, our policy achieves 74.58% success\
    \ in edge-alignment and 89.42% success in object-alignment when positioning relative to unseen target objects. These results\
    \ show that precise last-meter navigation can be achieved at a category-level without depth, LiDAR, or map priors, enabling\
    \ a scalable pathway toward unified mobile manipulation. Project page: https://rpm-lab-umn.github.io/category-level-last-meter-nav/"
  ko: "arXiv:2512.11173v4 Announce Type: replace \nAbstract: Achieving precise positioning of the mobile manipulator's base\
    \ is essential for successful manipulation actions that follow. Most of the RGB-based navigation systems only guarantee\
    \ coarse, meter-level accuracy, making them less suitable for the precise positioning phase of mobile manipulation. This\
    \ gap prevents manipulation policies from operating within the distribution of their training demonstrations, resulting\
    \ in frequent execution failures. We address this gap by introducing an object-centric imitation learning framework for\
    \ last-meter navigation, enabling a quadruped mobile manipulator robot to achieve manipulation-ready positioning using\
    \ only RGB observations from its onboard cameras. Our method conditions the navigation policy on three inputs: goal images,\
    \ multi-view RGB observations from the onboard cameras, and a text prompt specifying the target object. A language-driven\
    \ segmentation module and a spatial score-matrix decoder then supply explicit object grounding and relative pose reasoning.\
    \ Using real-world data from a single object instance within a category, the system generalizes to unseen object instances\
    \ across diverse environments with challenging lighting and background conditions. To comprehensively evaluate this, we\
    \ introduce two metrics: an edge-alignment metric, which uses ground truth orientation, and an object-alignment metric,\
    \ which evaluates how well the robot visually faces the target. Under these metrics, our policy achieves 74.58% success\
    \ in edge-alignment and 89.42% success in object-alignment when positioning relative to unseen target objects. These results\
    \ show that precise last-meter navigation can be achieved at a category-level without depth, LiDAR, or map priors, enabling\
    \ a scalable pathway toward unified mobile manipulation. Project page: https://rpm-lab-umn.github.io/category-level-last-meter-nav/"
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
- learning_category_level_last_m
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.11173v4.
sources:
- id: src_001
  type: paper
  title: Learning Category-level Last-meter Navigation from RGB Demonstrations of a Single-instance (arXiv)
  url: https://arxiv.org/abs/2512.11173
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
Achieving precise positioning of the mobile manipulator's base is essential for successful manipulation actions that follow. Most of the RGB-based navigation systems only guarantee coarse, meter-level accuracy, making them less suitable for the precise positioning phase of mobile manipulation. This gap prevents manipulation policies from operating within the distribution of their training demonstrations, resulting in frequent execution failures. We address this gap by introducing an object-centric imitation learning framework for last-meter navigation, enabling a quadruped mobile manipulator robot to achieve manipulation-ready positioning using only RGB observations from its onboard cameras. Our method conditions the navigation policy on three inputs: goal images, multi-view RGB observations from the onboard cameras, and a text prompt specifying the target object. A language-driven segmentation module and a spatial score-matrix decoder then supply explicit object grounding and relative pose reasoning. Using real-world data from a single object instance within a category, the system generalizes to unseen object instances across diverse environments with challenging lighting and background conditions. To comprehensively evaluate this, we introduce two metrics: an edge-alignment metric, which uses ground truth orientation, and an object-alignment metric, which evaluates how well the robot visually faces the target. Under these metrics, our policy achieves 74.58% success in edge-alignment and 89.42% success in object-alignment when positioning relative to unseen target objects. These results show that precise last-meter navigation can be achieved at a category-level without depth, LiDAR, or map priors, enabling a scalable pathway toward unified mobile manipulation. Project page: https://rpm-lab-umn.github.io/category-level-last-meter-nav/

## 核心内容
Achieving precise positioning of the mobile manipulator's base is essential for successful manipulation actions that follow. Most of the RGB-based navigation systems only guarantee coarse, meter-level accuracy, making them less suitable for the precise positioning phase of mobile manipulation. This gap prevents manipulation policies from operating within the distribution of their training demonstrations, resulting in frequent execution failures. We address this gap by introducing an object-centric imitation learning framework for last-meter navigation, enabling a quadruped mobile manipulator robot to achieve manipulation-ready positioning using only RGB observations from its onboard cameras. Our method conditions the navigation policy on three inputs: goal images, multi-view RGB observations from the onboard cameras, and a text prompt specifying the target object. A language-driven segmentation module and a spatial score-matrix decoder then supply explicit object grounding and relative pose reasoning. Using real-world data from a single object instance within a category, the system generalizes to unseen object instances across diverse environments with challenging lighting and background conditions. To comprehensively evaluate this, we introduce two metrics: an edge-alignment metric, which uses ground truth orientation, and an object-alignment metric, which evaluates how well the robot visually faces the target. Under these metrics, our policy achieves 74.58% success in edge-alignment and 89.42% success in object-alignment when positioning relative to unseen target objects. These results show that precise last-meter navigation can be achieved at a category-level without depth, LiDAR, or map priors, enabling a scalable pathway toward unified mobile manipulation. Project page: https://rpm-lab-umn.github.io/category-level-last-meter-nav/

## 参考
- http://arxiv.org/abs/2512.11173v4


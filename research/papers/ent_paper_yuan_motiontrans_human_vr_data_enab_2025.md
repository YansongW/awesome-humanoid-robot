---
$id: ent_paper_yuan_motiontrans_human_vr_data_enab_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MotionTrans: Human VR Data Enable Motion-Level Learning for Robotic Manipulation Policies'
  zh: MotionTrans
  ko: 'MotionTrans: Human VR Data Enable Motion-Level Learning for Robotic Manipulation Policies'
summary:
  en: 'MotionTrans: Human VR Data Enable Motion-Level Learning for Robotic Manipulation Policies (MotionTrans), is a 2025
    large vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information
    Processing, School of Computer Science, Peking University, Institute for Interdisciplinary Information Sciences, Tsinghua
    University, Shanghai Qi Zhi Institute, Shanghai Jiao Tong University, Wuhan University.'
  zh: 'MotionTrans: Human VR Data Enable Motion-Level Learning for Robotic Manipulation Policies (MotionTrans), is a 2025
    large vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information
    Processing, School of Computer Science, Peking University, Institute for Interdisciplinary Information Sciences, Tsinghua
    University, Shanghai Qi Zhi Institute, Shanghai Jiao Tong University, Wuhan University.'
  ko: 'MotionTrans: Human VR Data Enable Motion-Level Learning for Robotic Manipulation Policies (MotionTrans), is a 2025
    large vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information
    Processing, School of Computer Science, Peking University, Institute for Interdisciplinary Information Sciences, Tsinghua
    University, Shanghai Qi Zhi Institute, Shanghai Jiao Tong University, Wuhan University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- motiontrans
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.17759v1.
sources:
- id: src_001
  type: paper
  title: 'MotionTrans: Human VR Data Enable Motion-Level Learning for Robotic Manipulation Policies (arXiv)'
  url: https://arxiv.org/abs/2509.17759
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MotionTrans source
  url: https://doi.org/10.48550/arXiv.2509.17759
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Scaling real robot data is a key bottleneck in imitation learning, leading to the use of auxiliary data for policy training. While other aspects of robotic manipulation such as image or language understanding may be learned from internet-based datasets, acquiring motion knowledge remains challenging. Human data, with its rich diversity of manipulation behaviors, offers a valuable resource for this purpose. While previous works show that using human data can bring benefits, such as improving robustness and training efficiency, it remains unclear whether it can realize its greatest advantage: enabling robot policies to directly learn new motions for task completion. In this paper, we systematically explore this potential through multi-task human-robot cotraining. We introduce MotionTrans, a framework that includes a data collection system, a human data transformation pipeline, and a weighted cotraining strategy. By cotraining 30 human-robot tasks simultaneously, we direcly transfer motions of 13 tasks from human data to deployable end-to-end robot policies. Notably, 9 tasks achieve non-trivial success rates in zero-shot manner. MotionTrans also significantly enhances pretraining-finetuning performance (+40% success rate). Through ablation study, we also identify key factors for successful motion learning: cotraining with robot data and broad task-related motion coverage. These findings unlock the potential of motion-level learning from human data, offering insights into its effective use for training robotic manipulation policies. All data, code, and model weights are open-sourced https://motiontrans.github.io/.

## 核心内容
Scaling real robot data is a key bottleneck in imitation learning, leading to the use of auxiliary data for policy training. While other aspects of robotic manipulation such as image or language understanding may be learned from internet-based datasets, acquiring motion knowledge remains challenging. Human data, with its rich diversity of manipulation behaviors, offers a valuable resource for this purpose. While previous works show that using human data can bring benefits, such as improving robustness and training efficiency, it remains unclear whether it can realize its greatest advantage: enabling robot policies to directly learn new motions for task completion. In this paper, we systematically explore this potential through multi-task human-robot cotraining. We introduce MotionTrans, a framework that includes a data collection system, a human data transformation pipeline, and a weighted cotraining strategy. By cotraining 30 human-robot tasks simultaneously, we direcly transfer motions of 13 tasks from human data to deployable end-to-end robot policies. Notably, 9 tasks achieve non-trivial success rates in zero-shot manner. MotionTrans also significantly enhances pretraining-finetuning performance (+40% success rate). Through ablation study, we also identify key factors for successful motion learning: cotraining with robot data and broad task-related motion coverage. These findings unlock the potential of motion-level learning from human data, offering insights into its effective use for training robotic manipulation policies. All data, code, and model weights are open-sourced https://motiontrans.github.io/.

## 参考
- http://arxiv.org/abs/2509.17759v1


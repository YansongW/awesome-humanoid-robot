---
$id: ent_paper_dswam_a_dual_system_world_acti_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DSWAM: A Dual-System World Action Foundation Model for Fine-Grained Robot Manipulation'
  zh: 'DSWAM: A Dual-System World Action Foundation Model for Fine-Grained Robot Manipulation'
  ko: 'DSWAM: A Dual-System World Action Foundation Model for Fine-Grained Robot Manipulation'
summary:
  en: 'arXiv:2607.04927v1 Announce Type: new Abstract: World Action Models (WAMs) provide a promising alternative to Vision-Language-Action
    (VLA) policies by using video-based world modeling as dense supervision for robot action learning. Existing WAMs excel
    at physically grounded execution, but typically lack the explicit language-level planning interface in VLM-based VLAs
    for decomposing coarse instructions. Such decomposition becomes important when household tasks involve complex multi-step
    goals, where coarse user commands need to be converted into sequences of fine-grained executable subtasks. Meanwhile,
    the field still lacks a fair real-robot comparison between VLA and WAM execution capabilities, since existing systems
    often differ in data, robot embodiments, and task protocols. To address both the decomposition gap and the need for a
    controlled WAM-VLA comparison, we introduce DSWAM, a Dual-System World Action Foundation Model for fine-grained robot
    manipulation. DSWAM keeps a System 1 WAM executor as the default control path and optionally activates a System 2 vision-language
    subtask planner only when task decomposition is useful. The planner predicts executable subtasks from short-term visual
    history and a global task prompt, while the WAM executor performs world-aware action generation for each instruction or
    subtask. The executor is trained with action prediction and video co-training, but inference directly predicts action
    chunks without explicit future video generation. To make this execution path practical on real robots, we further integrate
    TensorRT acceleration, asynchronous execution, and real-time chunking (RTC) so that policy queries do not block robot
    control. To provide a fair real-robot comparison with VLA policies, we build and evaluate DSWAM under the DeMaVLA real-world
    deformable manipulation setting with matched robot platform, pretraining data, post-training data, and evaluation criteria.'
  zh: 'arXiv:2607.04927v1 Announce Type: new Abstract: World Action Models (WAMs) provide a promising alternative to Vision-Language-Action
    (VLA) policies by using video-based world modeling as dense supervision for robot action learning. Existing WAMs excel
    at physically grounded execution, but typically lack the explicit language-level planning interface in VLM-based VLAs
    for decomposing coarse instructions. Such decomposition becomes important when household tasks involve complex multi-step
    goals, where coarse user commands need to be converted into sequences of fine-grained executable subtasks. Meanwhile,
    the field still lacks a fair real-robot comparison between VLA and WAM execution capabilities, since existing systems
    often differ in data, robot embodiments, and task protocols. To address both the decomposition gap and the need for a
    controlled WAM-VLA comparison, we introduce DSWAM, a Dual-System World Action Foundation Model for fine-grained robot
    manipulation. DSWAM keeps a System 1 WAM executor as the default control path and optionally activates a System 2 vision-language
    subtask planner only when task decomposition is useful. The planner predicts executable subtasks from short-term visual
    history and a global task prompt, while the WAM executor performs world-aware action generation for each instruction or
    subtask. The executor is trained with action prediction and video co-training, but inference directly predicts action
    chunks without explicit future video generation. To make this execution path practical on real robots, we further integrate
    TensorRT acceleration, asynchronous execution, and real-time chunking (RTC) so that policy queries do not block robot
    control. To provide a fair real-robot comparison with VLA policies, we build and evaluate DSWAM under the DeMaVLA real-world
    deformable manipulation setting with matched robot platform, pretraining data, post-training data, and evaluation criteria.'
  ko: 'arXiv:2607.04927v1 Announce Type: new Abstract: World Action Models (WAMs) provide a promising alternative to Vision-Language-Action
    (VLA) policies by using video-based world modeling as dense supervision for robot action learning. Existing WAMs excel
    at physically grounded execution, but typically lack the explicit language-level planning interface in VLM-based VLAs
    for decomposing coarse instructions. Such decomposition becomes important when household tasks involve complex multi-step
    goals, where coarse user commands need to be converted into sequences of fine-grained executable subtasks. Meanwhile,
    the field still lacks a fair real-robot comparison between VLA and WAM execution capabilities, since existing systems
    often differ in data, robot embodiments, and task protocols. To address both the decomposition gap and the need for a
    controlled WAM-VLA comparison, we introduce DSWAM, a Dual-System World Action Foundation Model for fine-grained robot
    manipulation. DSWAM keeps a System 1 WAM executor as the default control path and optionally activates a System 2 vision-language
    subtask planner only when task decomposition is useful. The planner predicts executable subtasks from short-term visual
    history and a global task prompt, while the WAM executor performs world-aware action generation for each instruction or
    subtask. The executor is trained with action prediction and video co-training, but inference directly predicts action
    chunks without explicit future video generation. To make this execution path practical on real robots, we further integrate
    TensorRT acceleration, asynchronous execution, and real-time chunking (RTC) so that policy queries do not block robot
    control. To provide a fair real-robot comparison with VLA policies, we build and evaluate DSWAM under the DeMaVLA real-world
    deformable manipulation setting with matched robot platform, pretraining data, post-training data, and evaluation criteria.'
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
- dswam
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04927v1.
sources:
- id: src_001
  type: paper
  title: 'DSWAM: A Dual-System World Action Foundation Model for Fine-Grained Robot Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.04927
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
World Action Models (WAMs) provide a promising alternative to Vision-Language-Action (VLA) policies by using video-based world modeling as dense supervision for robot action learning. Existing WAMs excel at physically grounded execution, but typically lack the explicit language-level planning interface in VLM-based VLAs for decomposing coarse instructions. Such decomposition becomes important when household tasks involve complex multi-step goals, where coarse user commands need to be converted into sequences of fine-grained executable subtasks. Meanwhile, the field still lacks a fair real-robot comparison between VLA and WAM execution capabilities, since existing systems often differ in data, robot embodiments, and task protocols. To address both the decomposition gap and the need for a controlled WAM-VLA comparison, we introduce DSWAM, a Dual-System World Action Foundation Model for fine-grained robot manipulation. DSWAM keeps a System 1 WAM executor as the default control path and optionally activates a System 2 vision-language subtask planner only when task decomposition is useful. The planner predicts executable subtasks from short-term visual history and a global task prompt, while the WAM executor performs world-aware action generation for each instruction or subtask. The executor is trained with action prediction and video co-training, but inference directly predicts action chunks without explicit future video generation. To make this execution path practical on real robots, we further integrate TensorRT acceleration, asynchronous execution, and real-time chunking (RTC) so that policy queries do not block robot control. To provide a fair real-robot comparison with VLA policies, we build and evaluate DSWAM under the DeMaVLA real-world deformable manipulation setting with matched robot platform, pretraining data, post-training data, and evaluation criteria.

## 核心内容
World Action Models (WAMs) provide a promising alternative to Vision-Language-Action (VLA) policies by using video-based world modeling as dense supervision for robot action learning. Existing WAMs excel at physically grounded execution, but typically lack the explicit language-level planning interface in VLM-based VLAs for decomposing coarse instructions. Such decomposition becomes important when household tasks involve complex multi-step goals, where coarse user commands need to be converted into sequences of fine-grained executable subtasks. Meanwhile, the field still lacks a fair real-robot comparison between VLA and WAM execution capabilities, since existing systems often differ in data, robot embodiments, and task protocols. To address both the decomposition gap and the need for a controlled WAM-VLA comparison, we introduce DSWAM, a Dual-System World Action Foundation Model for fine-grained robot manipulation. DSWAM keeps a System 1 WAM executor as the default control path and optionally activates a System 2 vision-language subtask planner only when task decomposition is useful. The planner predicts executable subtasks from short-term visual history and a global task prompt, while the WAM executor performs world-aware action generation for each instruction or subtask. The executor is trained with action prediction and video co-training, but inference directly predicts action chunks without explicit future video generation. To make this execution path practical on real robots, we further integrate TensorRT acceleration, asynchronous execution, and real-time chunking (RTC) so that policy queries do not block robot control. To provide a fair real-robot comparison with VLA policies, we build and evaluate DSWAM under the DeMaVLA real-world deformable manipulation setting with matched robot platform, pretraining data, post-training data, and evaluation criteria.

## 参考
- http://arxiv.org/abs/2607.04927v1


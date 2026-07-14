---
$id: ent_paper_bilivla_scene_aware_vision_lan_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic Navigation'
  zh: 'BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic Navigation'
  ko: 'BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic Navigation'
summary:
  en: "arXiv:2606.23531v2 Announce Type: replace \nAbstract: Endoscopic retrograde cholangiopancreatography (ERCP) demands\
    \ precise endoscopic navigation and stable biliary cannulation within a narrow monocular field characterized by specular\
    \ reflections, partial occlusions, and frequent tissue contact. Although recent robotic systems and vision-based assistance\
    \ techniques improve operator ergonomics and provide perceptual cues, their performance degrades under pronounced anatomical\
    \ variability and safety-critical visual artifacts, which hinders reliable autonomy in cannulation-grade procedures. Here,\
    \ we present BiliVLA, a scene-aware Vision-Language-Action (VLA) framework that formulates biliary endoscopic navigation\
    \ as an instruction-conditioned visuomotor learning problem. Given an endoscopic observation and a stage-specific language\
    \ instruction, BiliVLA jointly predicts the target category, a grounded bounding box, and a discrete three degrees of\
    \ freedom (DoF) motor command for a continuum endoscope. The proposed framework incorporates scene-aware supervision to\
    \ enhance semantic target consistency and safety-aware recovery supervision to induce conservative retreat behaviors under\
    \ luminal wall contact. A key component of BiliVLA is a two-stage training paradigm that combines grounding-enhanced supervised\
    \ fine-tuning (SFT) with Group Relative Policy Optimization (GRPO), which significantly improves action reliability and\
    \ decision consistency during closed-loop navigation. Across three ERCP subtasks, BiliVLA achieves an average action precision\
    \ of 91.96\\% and an overall success rate (SR) of 84.85\\% in real-world phantom experiments. These results indicate that\
    \ integrating semantic grounding, scene-aware learning, and reward-guided optimization improves perception-action alignment\
    \ and enables robust autonomous endoscopic navigation."
  zh: "arXiv:2606.23531v2 Announce Type: replace \nAbstract: Endoscopic retrograde cholangiopancreatography (ERCP) demands\
    \ precise endoscopic navigation and stable biliary cannulation within a narrow monocular field characterized by specular\
    \ reflections, partial occlusions, and frequent tissue contact. Although recent robotic systems and vision-based assistance\
    \ techniques improve operator ergonomics and provide perceptual cues, their performance degrades under pronounced anatomical\
    \ variability and safety-critical visual artifacts, which hinders reliable autonomy in cannulation-grade procedures. Here,\
    \ we present BiliVLA, a scene-aware Vision-Language-Action (VLA) framework that formulates biliary endoscopic navigation\
    \ as an instruction-conditioned visuomotor learning problem. Given an endoscopic observation and a stage-specific language\
    \ instruction, BiliVLA jointly predicts the target category, a grounded bounding box, and a discrete three degrees of\
    \ freedom (DoF) motor command for a continuum endoscope. The proposed framework incorporates scene-aware supervision to\
    \ enhance semantic target consistency and safety-aware recovery supervision to induce conservative retreat behaviors under\
    \ luminal wall contact. A key component of BiliVLA is a two-stage training paradigm that combines grounding-enhanced supervised\
    \ fine-tuning (SFT) with Group Relative Policy Optimization (GRPO), which significantly improves action reliability and\
    \ decision consistency during closed-loop navigation. Across three ERCP subtasks, BiliVLA achieves an average action precision\
    \ of 91.96\\% and an overall success rate (SR) of 84.85\\% in real-world phantom experiments. These results indicate that\
    \ integrating semantic grounding, scene-aware learning, and reward-guided optimization improves perception-action alignment\
    \ and enables robust autonomous endoscopic navigation."
  ko: "arXiv:2606.23531v2 Announce Type: replace \nAbstract: Endoscopic retrograde cholangiopancreatography (ERCP) demands\
    \ precise endoscopic navigation and stable biliary cannulation within a narrow monocular field characterized by specular\
    \ reflections, partial occlusions, and frequent tissue contact. Although recent robotic systems and vision-based assistance\
    \ techniques improve operator ergonomics and provide perceptual cues, their performance degrades under pronounced anatomical\
    \ variability and safety-critical visual artifacts, which hinders reliable autonomy in cannulation-grade procedures. Here,\
    \ we present BiliVLA, a scene-aware Vision-Language-Action (VLA) framework that formulates biliary endoscopic navigation\
    \ as an instruction-conditioned visuomotor learning problem. Given an endoscopic observation and a stage-specific language\
    \ instruction, BiliVLA jointly predicts the target category, a grounded bounding box, and a discrete three degrees of\
    \ freedom (DoF) motor command for a continuum endoscope. The proposed framework incorporates scene-aware supervision to\
    \ enhance semantic target consistency and safety-aware recovery supervision to induce conservative retreat behaviors under\
    \ luminal wall contact. A key component of BiliVLA is a two-stage training paradigm that combines grounding-enhanced supervised\
    \ fine-tuning (SFT) with Group Relative Policy Optimization (GRPO), which significantly improves action reliability and\
    \ decision consistency during closed-loop navigation. Across three ERCP subtasks, BiliVLA achieves an average action precision\
    \ of 91.96\\% and an overall success rate (SR) of 84.85\\% in real-world phantom experiments. These results indicate that\
    \ integrating semantic grounding, scene-aware learning, and reward-guided optimization improves perception-action alignment\
    \ and enables robust autonomous endoscopic navigation."
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
- bilivla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.23531v3.
sources:
- id: src_001
  type: paper
  title: 'BiliVLA: Scene-Aware Vision-Language-Action Model with Reinforcement Learning for Autonomous Biliary Endoscopic
    Navigation (arXiv)'
  url: https://arxiv.org/abs/2606.23531
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
Endoscopic retrograde cholangiopancreatography (ERCP) demands precise endoscopic navigation and stable biliary cannulation within a narrow monocular field characterized by specular reflections, partial occlusions, and frequent tissue contact. Although recent robotic systems and vision-based assistance techniques improve operator ergonomics and provide perceptual cues, their performance degrades under pronounced anatomical variability and safety-critical visual artifacts, which hinders reliable autonomy in cannulation-grade procedures. Here, we present BiliVLA, a scene-aware Vision-Language-Action (VLA) framework that formulates biliary endoscopic navigation as an instruction-conditioned visuomotor learning problem. Given an endoscopic observation and a stage-specific language instruction, BiliVLA jointly predicts the target category, a grounded bounding box, and a discrete three-degree-of-freedom (3-DoF) motor command for a continuum endoscope. The proposed framework incorporates scene-aware supervision to improve semantic target consistency and safety-aware recovery supervision to induce conservative retreat behaviors under luminal wall contact. A key component of BiliVLA is a two-stage training paradigm that combines grounding-enhanced supervised fine-tuning (SFT) with Group Relative Policy Optimization (GRPO), thereby improving action reliability and decision consistency during closed-loop navigation. Across three ERCP subtasks, BiliVLA achieves the best overall performance in physical phantom experiments, with a total mIoU of 0.9625, an overall action precision of 91.96\%, and an overall success rate (SR) of 84.85\%. These results indicate that integrating semantic grounding, scene-aware learning, and reward-guided optimization strengthens perception--action alignment and enables more robust autonomous biliary endoscopic navigation.

## 核心内容
Endoscopic retrograde cholangiopancreatography (ERCP) demands precise endoscopic navigation and stable biliary cannulation within a narrow monocular field characterized by specular reflections, partial occlusions, and frequent tissue contact. Although recent robotic systems and vision-based assistance techniques improve operator ergonomics and provide perceptual cues, their performance degrades under pronounced anatomical variability and safety-critical visual artifacts, which hinders reliable autonomy in cannulation-grade procedures. Here, we present BiliVLA, a scene-aware Vision-Language-Action (VLA) framework that formulates biliary endoscopic navigation as an instruction-conditioned visuomotor learning problem. Given an endoscopic observation and a stage-specific language instruction, BiliVLA jointly predicts the target category, a grounded bounding box, and a discrete three-degree-of-freedom (3-DoF) motor command for a continuum endoscope. The proposed framework incorporates scene-aware supervision to improve semantic target consistency and safety-aware recovery supervision to induce conservative retreat behaviors under luminal wall contact. A key component of BiliVLA is a two-stage training paradigm that combines grounding-enhanced supervised fine-tuning (SFT) with Group Relative Policy Optimization (GRPO), thereby improving action reliability and decision consistency during closed-loop navigation. Across three ERCP subtasks, BiliVLA achieves the best overall performance in physical phantom experiments, with a total mIoU of 0.9625, an overall action precision of 91.96\%, and an overall success rate (SR) of 84.85\%. These results indicate that integrating semantic grounding, scene-aware learning, and reward-guided optimization strengthens perception--action alignment and enables more robust autonomous biliary endoscopic navigation.

## 参考
- http://arxiv.org/abs/2606.23531v3


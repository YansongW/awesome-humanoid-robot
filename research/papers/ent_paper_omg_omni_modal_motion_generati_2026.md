---
$id: ent_paper_omg_omni_modal_motion_generati_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OMG: Omni-Modal Motion Generation for Generalist Humanoid Control'
  zh: OMG｜用于通用人形控制的全模态运动生成
  ko: 'OMG: Omni-Modal Motion Generation for Generalist Humanoid Control'
summary:
  en: 'Humanoid whole-body control has made significant progress in recent years, yet existing approaches remain limited to
    few-skill policies with heavy reward engineering, or motion trackers that are difficult to extend to new input modalities.
    We argue that the key to general-purpose humanoid control is to build a scalable brain, a module capable of reasoning
    with diverse conditioning modalities, atop a reactive motion tracking cerebellum, mirroring the hierarchical structure
    of biological motor systems. Two challenges arise in realizing this vision: acquiring a vast amount of high-quality data
    to achieve general purpose control, and equipping the generator with the capability to condition on compositional, extensible
    multi-modal inputs. We present OMG, which addresses these challenges with a '
  zh: OMG 先从本体状态与关节序列恢复场景、目标或运动表征，再用扩散策略/流匹配、VLM 语义规划/路由、全身控制器/WBC/MPC生成全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  ko: OMG 先从本体状态与关节序列恢复场景、目标或运动表征，再用扩散策略/流匹配、VLM 语义规划/路由、全身控制器/WBC/MPC生成全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generative_motion
- language_control
- motion_generation
- omg
- trajectory_planning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: OMG: Omni-Modal Motion
    Generation for Generalist Humanoid Control.'
sources:
- id: src_001
  type: website
  title: OMG project page
  url: https://tsinghua-mars-lab.github.io/OMG/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
Humanoid whole-body control has made significant progress in recent years, yet existing approaches remain limited to few-skill policies with heavy reward engineering, or motion trackers that are difficult to extend to new input modalities. We argue that the key to general-purpose humanoid control is to build a scalable brain, a module capable of reasoning with diverse conditioning modalities, atop a reactive motion tracking cerebellum, mirroring the hierarchical structure of biological motor systems. Two challenges arise in realizing this vision: acquiring a vast amount of high-quality data to achieve general purpose control, and equipping the generator with the capability to condition on compositional, extensible multi-modal inputs. We present OMG, which addresses these challenges with a meticulous data curation, filtering and labeling pipeline, as well as a diffusion-based motion generation backbone that conditions on language, audio, and human reference motions. Extensive experiments validate OMG as an omni-modal whole-body controller exhibiting state-of-the-art performance, model scaling behavior and efficient adaptation to new distributions and modalities, marking a concrete step toward foundation models for humanoid robots.

## 核心内容
Humanoid whole-body control has made significant progress in recent years, yet existing approaches remain limited to few-skill policies with heavy reward engineering, or motion trackers that are difficult to extend to new input modalities. We argue that the key to general-purpose humanoid control is to build a scalable brain, a module capable of reasoning with diverse conditioning modalities, atop a reactive motion tracking cerebellum, mirroring the hierarchical structure of biological motor systems. Two challenges arise in realizing this vision: acquiring a vast amount of high-quality data to achieve general purpose control, and equipping the generator with the capability to condition on compositional, extensible multi-modal inputs. We present OMG, which addresses these challenges with a meticulous data curation, filtering and labeling pipeline, as well as a diffusion-based motion generation backbone that conditions on language, audio, and human reference motions. Extensive experiments validate OMG as an omni-modal whole-body controller exhibiting state-of-the-art performance, model scaling behavior and efficient adaptation to new distributions and modalities, marking a concrete step toward foundation models for humanoid robots.

## 参考
- Semantic Scholar search: OMG: Omni-Modal Motion Generation for Generalist Humanoid Control


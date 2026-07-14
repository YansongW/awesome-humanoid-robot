---
$id: ent_paper_roboomni_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboOmni: Proactive Robot Manipulation in Omni-modal Context'
  zh: RoboOmni：全模态上下文中的主动式机器人操作
  ko: 'RoboOmni: 옴니모달 맥락에서의 주도적 로봇 조작'
summary:
  en: A 2025 VLA system that fuses vision, speech, and environmental sounds to infer user intentions proactively and execute
    actions without explicit text instructions.
  zh: 2025 年的 VLA 系统，融合视觉、语音与环境声音，主动推断用户意图并在没有显式文本指令的情况下执行动作。
  ko: 2025년 VLA 시스템으로, 시각, 음성, 환경 소리를 융합하여 사용자 의도를 주도적으로 추론하고 명시적 텍스트 지시 없이 액션을 실행함.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- vla
- omni_modal
- proactive
- intention_recognition
- speech
- audio
- multimodal
- manipulation
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.23763v3.
sources:
- id: src_roboomni_paper
  type: paper
  title: 'RoboOmni: Proactive Robot Manipulation in Omni-modal Context'
  url: https://arxiv.org/abs/2510.23763
  date: '2025-10-30'
  accessed_at: '2026-06-22'
- id: src_roboomni_repo
  type: website
  title: OpenMOSS/RoboOmni GitHub Repository
  url: https://github.com/OpenMOSS/RoboOmni
  date: '2025-10-30'
  accessed_at: '2026-06-22'
related_entities:
- id: ent_dataset_omniaction
  relationship: produces
  description:
    en: RoboOmni introduces the OmniAction dataset for training proactive omni-modal VLA models.
    zh: RoboOmni 引入了用于训练主动式全模态 VLA 模型的 OmniAction 数据集。
    ko: RoboOmni은 주도적 옴니모달 VLA 모델 학습을 위한 OmniAction 데이터셋을 소개함.
- id: ent_benchmark_libero
  relationship: serves
  description:
    en: RoboOmni is evaluated on LIBERO benchmarks using the OmniAction-LIBERO split.
    zh: RoboOmni 在 LIBERO 基准上使用 OmniAction-LIBERO 分割进行评估。
    ko: RoboOmni은 OmniAction-LIBERO 분할을 사용하여 LIBERO 벤치마크에서 평가됨.
- id: ent_benchmark_libero_plus
  relationship: serves
  description:
    en: RoboOmni is related to the broader LIBERO robustness evaluation ecosystem, though primary evaluation uses standard
      LIBERO.
    zh: RoboOmni 与更广泛的 LIBERO 鲁棒性评测生态相关，尽管其主要评估使用标准 LIBERO。
    ko: RoboOmni은 더 넓은 LIBERO 견고성 평가 생태계와 관련이 있으나, 주요 평가는 표준 LIBERO를 사용함.
theoretical_depth:
- system
---
## 概述
Recent advances in Multimodal Large Language Models (MLLMs) have driven rapid progress in Vision-Language-Action (VLA) models for robotic manipulation. Although effective in many scenarios, current approaches largely rely on explicit instructions, whereas in real-world interactions, humans rarely issue instructions directly. Effective collaboration requires robots to infer user intentions proactively. In this work, we introduce cross-modal contextual instructions, a new setting where intent is derived from spoken dialogue, environmental sounds, and visual cues rather than explicit commands. To address this new setting, we present RoboOmni, a Perceiver-Thinker-Talker-Executor framework based on end-to-end omni-modal LLMs that unifies intention recognition, interaction confirmation, and action execution. RoboOmni fuses auditory and visual signals spatiotemporally for robust intention recognition, while supporting direct speech interaction. To address the absence of training data for proactive intention recognition in robotic manipulation, we build OmniAction, comprising 140k episodes, 5k+ speakers, 2.4k event sounds, 640 backgrounds, and six contextual instruction types. Experiments in simulation and real-world settings show that RoboOmni surpasses text- and ASR-based baselines in success rate, inference speed, intention recognition, and proactive assistance.

## 核心内容
Recent advances in Multimodal Large Language Models (MLLMs) have driven rapid progress in Vision-Language-Action (VLA) models for robotic manipulation. Although effective in many scenarios, current approaches largely rely on explicit instructions, whereas in real-world interactions, humans rarely issue instructions directly. Effective collaboration requires robots to infer user intentions proactively. In this work, we introduce cross-modal contextual instructions, a new setting where intent is derived from spoken dialogue, environmental sounds, and visual cues rather than explicit commands. To address this new setting, we present RoboOmni, a Perceiver-Thinker-Talker-Executor framework based on end-to-end omni-modal LLMs that unifies intention recognition, interaction confirmation, and action execution. RoboOmni fuses auditory and visual signals spatiotemporally for robust intention recognition, while supporting direct speech interaction. To address the absence of training data for proactive intention recognition in robotic manipulation, we build OmniAction, comprising 140k episodes, 5k+ speakers, 2.4k event sounds, 640 backgrounds, and six contextual instruction types. Experiments in simulation and real-world settings show that RoboOmni surpasses text- and ASR-based baselines in success rate, inference speed, intention recognition, and proactive assistance.

## 参考
- http://arxiv.org/abs/2510.23763v3


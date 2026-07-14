---
$id: ent_paper_wang_wam_survey_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'World Action Models: The Next Frontier in Embodied AI'
  zh: 世界动作模型：具身智能的下一个前沿
  ko: '월드 액션 모델: 엠바디드 AI의 다음 프론티어'
summary:
  en: A 2026 survey that defines World Action Models (WAMs) as embodied foundation models unifying predictive world modeling
    with action generation, and organizes existing methods into Cascaded and Joint architectures.
  zh: 2026 年综述，将 World Action Models（WAMs）定义为统一预测性世界建模与动作生成的具身基础模型，并将现有方法组织为级联式（Cascaded）与联合式（Joint）架构。
  ko: 2026년 서베이로, World Action Models(WAMs)를 예측적 월드 모델링과 액션 생성을 통합하는 엠바디드 파욍데이션 모델로 정의하고, 기존 방법을 Cascaded 및 Joint 아키텍처로 분류함.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 09_data_datasets
- 10_evaluation_benchmarks
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- wam
- world_action_model
- world_model
- vla
- survey
- cascaded_wam
- joint_wam
- diffusion
- autoregressive
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2605.12090v1.
sources:
- id: src_wam_paper
  type: paper
  title: 'World Action Models: The Next Frontier in Embodied AI'
  url: https://arxiv.org/abs/2605.12090
  date: '2026-05-12'
  accessed_at: '2026-06-22'
- id: src_wam_repo
  type: website
  title: OpenMOSS/Awesome-WAM
  url: https://github.com/OpenMOSS/Awesome-WAM
  date: '2026-05-13'
  accessed_at: '2026-06-22'
related_entities:
- id: ent_paper_wang_vla_survey_2026
  relationship: is_based_on
  description:
    en: The WAM survey extends the data-centric VLA survey by focusing on models that jointly predict future states and actions.
    zh: WAM 综述在关注联合预测未来状态与动作的模型这一点上，扩展了以数据为中心的 VLA 综述。
    ko: WAM 서베이는 미래 상태와 액션을 공동으로 예측하는 모델에 초점을 맞추며 데이터 중심 VLA 서베이를 확장함.
- id: ent_dataset_omniaction
  relationship: cites
  description:
    en: The WAM survey discusses omni-modal and internet-scale data ecosystems fueling WAM development.
    zh: WAM 综述讨论了推动 WAM 发展的全模态与互联网规模数据生态。
    ko: WAM 서베이는 WAM 개발을 뒷받침하는 옴니모달 및 인터넷 규모 데이터 생태계를 논의함.
- id: ent_benchmark_libero_plus
  relationship: cites
  description:
    en: The WAM survey cites robustness benchmarks such as LIBERO-plus as part of the emerging WAM evaluation landscape.
    zh: WAM 综述将 LIBERO-plus 等鲁棒性基准引用为新兴 WAM 评测格局的一部分。
    ko: WAM 서베이는 LIBERO-plus와 같은 견고성 벤치마크를 새로운 WAM 평가 환경의 일부로 인용함.
theoretical_depth:
- system
---
## 概述
Vision-Language-Action (VLA) models have achieved strong semantic generalization for embodied policy learning, yet they learn reactive observation-to-action mappings without explicitly modeling how the physical world evolves under intervention. A growing body of work addresses this limitation by integrating world models, predictive models of environment dynamics, into the action generation pipeline. We term this emerging paradigm World Action Models (WAMs): embodied foundation models that unify predictive state modeling with action generation, targeting a joint distribution over future states and actions rather than actions alone. However, the literature remains fragmented across architectures, learning objectives, and application scenarios, lacking a unified conceptual framework. We formally define WAMs and disambiguate them from related concepts, and trace the foundations and early integration of VLA and world model research that gave rise to this paradigm. We organize existing methods into a structured taxonomy of Cascaded and Joint WAMs, with further subdivision by generation modality, conditioning mechanism, and action decoding strategy. We systematically analyze the data ecosystem fueling WAMs development, spanning robot teleoperation, portable human demonstrations, simulation, and internet-scale egocentric video, and synthesize emerging evaluation protocols organized around visual fidelity, physical commonsense, and action plausibility. Overall, this survey provides the first systematic account of the WAMs landscape, clarifies key architectural paradigms and their trade-offs, and identifies open challenges and future opportunities for this rapidly evolving field.

## 核心内容
Vision-Language-Action (VLA) models have achieved strong semantic generalization for embodied policy learning, yet they learn reactive observation-to-action mappings without explicitly modeling how the physical world evolves under intervention. A growing body of work addresses this limitation by integrating world models, predictive models of environment dynamics, into the action generation pipeline. We term this emerging paradigm World Action Models (WAMs): embodied foundation models that unify predictive state modeling with action generation, targeting a joint distribution over future states and actions rather than actions alone. However, the literature remains fragmented across architectures, learning objectives, and application scenarios, lacking a unified conceptual framework. We formally define WAMs and disambiguate them from related concepts, and trace the foundations and early integration of VLA and world model research that gave rise to this paradigm. We organize existing methods into a structured taxonomy of Cascaded and Joint WAMs, with further subdivision by generation modality, conditioning mechanism, and action decoding strategy. We systematically analyze the data ecosystem fueling WAMs development, spanning robot teleoperation, portable human demonstrations, simulation, and internet-scale egocentric video, and synthesize emerging evaluation protocols organized around visual fidelity, physical commonsense, and action plausibility. Overall, this survey provides the first systematic account of the WAMs landscape, clarifies key architectural paradigms and their trade-offs, and identifies open challenges and future opportunities for this rapidly evolving field.

## 参考
- http://arxiv.org/abs/2605.12090v1


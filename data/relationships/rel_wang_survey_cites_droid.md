---
$id: "rel_wang_survey_cites_droid"
$schema: "../schema/v1/relationship_schema.json"
$version: 1

type: "cites"

source:
  id: "ent_paper_wang_vla_survey_2026"
  name:
    en: "Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines"
    zh: "机器人视觉-语言-动作：数据集、基准与数据引擎综述"
    ko: "로보틱스에서의 비전-언어-액션: 데이터셋, 벤치마크 및 데이터 엔진에 대한 서베이"

target:
  id: "ent_dataset_droid"
  name:
    en: "DROID"
    zh: "DROID 机器人操作数据集"
    ko: "DROID"

domains:
  source_domain: "09_data_datasets"
  target_domain: "09_data_datasets"

description:
  en: "Wang et al. (2026) cite DROID as a distributed real-world dataset emphasizing visual and environmental variation."
  zh: "Wang 等人（2026）将 DROID 引用为强调视觉与环境变化的分布式真实世界数据集。"
  ko: "Wang et al. (2026)은 DROID를 시각 및 환경 변화를 강조하는 분산 실제 데이터셋으로 인용함."

verification:
  status: "verified"
  reviewed_by: "human_and_ai"
  reviewed_at: "2026-06-22"
  confidence: "high"
  notes: "Citation confirmed in Section 3.1 of the Wang et al. 2026 VLA survey."

sources:
  - id: "src_wang_survey_droid"
    type: "paper"
    title: "Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines"
    url: "https://arxiv.org/abs/2604.23001"
    date: "2026-04-24"
    accessed_at: "2026-06-22"
---

---
$id: "rel_wang_survey_cites_oxe"
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
  id: "ent_dataset_open_x_embodiment"
  name:
    en: "Open X-Embodiment Dataset"
    zh: "Open X-Embodiment 数据集"
    ko: "Open X-Embodiment 데이터셋"

domains:
  source_domain: "09_data_datasets"
  target_domain: "09_data_datasets"

description:
  en: "Wang et al. (2026) cite Open X-Embodiment as a widely used cross-embodiment pretraining dataset for VLA models."
  zh: "Wang 等人（2026）将 Open X-Embodiment 引用为 VLA 模型广泛使用的跨具身预训练数据集。"
  ko: "Wang et al. (2026)은 Open X-Embodiment를 VLA 모델의 널리 사용되는 cross-embodiment 사전 학습 데이터셋으로 인용함."

verification:
  status: "verified"
  reviewed_by: "human_and_ai"
  reviewed_at: "2026-06-22"
  confidence: "high"
  notes: "Citation confirmed in Section 3.1 of the Wang et al. 2026 VLA survey."

sources:
  - id: "src_wang_survey_oxe"
    type: "paper"
    title: "Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines"
    url: "https://arxiv.org/abs/2604.23001"
    date: "2026-04-24"
    accessed_at: "2026-06-22"
---

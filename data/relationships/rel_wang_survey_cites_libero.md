---
$id: "rel_wang_survey_cites_libero"
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
  id: "ent_benchmark_libero"
  name:
    en: "LIBERO"
    zh: "LIBERO"
    ko: "LIBERO"

domains:
  source_domain: "10_evaluation_benchmarks"
  target_domain: "10_evaluation_benchmarks"

description:
  en: "Wang et al. (2026) cite LIBERO as a representative short-horizon tabletop VLA benchmark."
  zh: "Wang 等人（2026）将 LIBERO 引用为代表性短程桌面 VLA 基准。"
  ko: "Wang et al. (2026)은 LIBERO를 대표적인 단기 테이블탑 VLA 벤치마크로 인용함."

verification:
  status: "verified"
  reviewed_by: "human_and_ai"
  reviewed_at: "2026-06-22"
  confidence: "high"
  notes: "Citation confirmed in Section 4.1 of the Wang et al. 2026 VLA survey."

sources:
  - id: "src_wang_survey_libero"
    type: "paper"
    title: "Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines"
    url: "https://arxiv.org/abs/2604.23001"
    date: "2026-04-24"
    accessed_at: "2026-06-22"
---

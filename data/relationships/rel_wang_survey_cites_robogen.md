---
$id: "rel_wang_survey_cites_robogen"
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
  id: "ent_tech_robogen"
  name:
    en: "RoboGen"
    zh: "RoboGen"
    ko: "RoboGen"

domains:
  source_domain: "08_software_middleware"
  target_domain: "09_data_datasets"

description:
  en: "Wang et al. (2026) discuss RoboGen as an LLM-driven automatic task-generation framework for simulation."
  zh: "Wang 等人（2026）将 RoboGen 作为由大语言模型驱动的仿真自动任务生成框架进行讨论。"
  ko: "Wang et al. (2026)은 RoboGen을 LLM 기반 시뮬레이션 자동 작업 생성 프레임워크로 논의함."

verification:
  status: "verified"
  reviewed_by: "human_and_ai"
  reviewed_at: "2026-06-22"
  confidence: "high"
  notes: "Citation confirmed in Section 3.2 and Section 5 of the Wang et al. 2026 VLA survey."

sources:
  - id: "src_wang_survey_robogen"
    type: "paper"
    title: "Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines"
    url: "https://arxiv.org/abs/2604.23001"
    date: "2026-04-24"
    accessed_at: "2026-06-22"
---

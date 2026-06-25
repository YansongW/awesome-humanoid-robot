---
$id: "rel_wang_survey_cites_humanoidbench"
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
  id: "ent_benchmark_humanoidbench"
  name:
    en: "HumanoidBench"
    zh: "HumanoidBench"
    ko: "HumanoidBench"

domains:
  source_domain: "10_evaluation_benchmarks"
  target_domain: "10_evaluation_benchmarks"

description:
  en: "Wang et al. (2026) discuss HumanoidBench as a simulation benchmark for whole-body humanoid locomotion and manipulation."
  zh: "Wang 等人（2026）将 HumanoidBench 作为全身人形运动与操作的仿真基准进行讨论。"
  ko: "Wang et al. (2026)은 HumanoidBench를 전신 휨로봇 로코모션 및 조작을 위한 시뮬레이션 벤치마크로 논의함."

verification:
  status: "verified"
  reviewed_by: "human_and_ai"
  reviewed_at: "2026-06-22"
  confidence: "high"
  notes: "Citation confirmed in Section 4 of the Wang et al. 2026 VLA survey."

sources:
  - id: "src_wang_survey_humanoidbench"
    type: "paper"
    title: "Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines"
    url: "https://arxiv.org/abs/2604.23001"
    date: "2026-04-24"
    accessed_at: "2026-06-22"
---

---
$id: "rel_wam_survey_based_on_vla_survey"
$schema: "../schema/v1/relationship_schema.json"
$version: 1

type: "is_based_on"

source:
  id: "ent_paper_wang_wam_survey_2026"
  name:
    en: "World Action Models: The Next Frontier in Embodied AI"
    zh: "世界动作模型：具身智能的下一个前沿"
    ko: "월드 액션 모델: 엠바디드 AI의 다음 프론티어"

target:
  id: "ent_paper_wang_vla_survey_2026"
  name:
    en: "Vision-Language-Action in Robotics: A Survey of Datasets, Benchmarks, and Data Engines"
    zh: "机器人视觉-语言-动作：数据集、基准与数据引擎综述"
    ko: "로보틱스에서의 비전-언어-액션: 데이터셋, 벤치마크 및 데이터 엔진에 대한 서베이"

domains:
  source_domain: "07_ai_models_algorithms"
  target_domain: "07_ai_models_algorithms"

description:
  en: "The WAM survey builds on the VLA survey by focusing on models that jointly predict future states and actions."
  zh: "WAM 综述在 VLA 综述基础上，进一步关注联合预测未来状态与动作的模型。"
  ko: "WAM 서베이는 VLA 서베이를 바탕으로 미래 상태와 액션을 공동으로 예측하는 모델에 초점을 맞춤."

verification:
  status: "verified"
  reviewed_by: "human_and_ai"
  reviewed_at: "2026-06-22"
  confidence: "medium"
  notes: "Analytical relationship: WAMs are a conceptual extension of VLAs with explicit world modeling."

sources:
  - id: "src_wam_paper"
    type: "paper"
    title: "World Action Models: The Next Frontier in Embodied AI"
    url: "https://arxiv.org/abs/2605.12090"
    date: "2026-05-12"
    accessed_at: "2026-06-22"
---

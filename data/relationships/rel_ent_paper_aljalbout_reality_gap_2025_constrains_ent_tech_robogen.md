---
$id: "rel_ent_paper_aljalbout_reality_gap_2025_constrains_ent_tech_robogen"
$schema: "../../../../../data/schema/v1/relationship_schema.json"
$version: 1

type: "constrains"

source:
  id: "ent_paper_aljalbout_reality_gap_2025"
  name:
    en: "The Reality Gap in Robotics: Challenges, Solutions, and Best Practices"
    zh: "机器人中的现实鸿沟：挑战、解决方案与最佳实践"
    ko: "로보틱스의 현실 격차: 과제, 해결책 및 모범 사례"

target:
  id: "ent_tech_robogen"
  name:
    en: "RoboGen"
    zh: "RoboGen"
    ko: "RoboGen"

domains:
  source_domain: "07_ai_models_algorithms"
  target_domain: "08_software_middleware"

description:
  en: "The reality gap between simulation and real-world physics constrains how effectively synthetic data engines such as RoboGen transfer to real robots."
  zh: "仿真与现实物理之间的现实鸿沟限制了 RoboGen 等合成数据引擎向真实机器人迁移的效果。"
  ko: "시뮬레이션과 실제 물리 간의 현실 격차는 RoboGen과 같은 합성 데이터 엔진이 실제 로봇으로 전환되는 효과를 제한합니다."

verification:
  status: "partially_verified"
  reviewed_by: "ai"
  reviewed_at: "2026-06-25"
  confidence: "medium"
  notes: "Inference from the survey's scope; the paper does not necessarily name RoboGen explicitly."

sources:
  - id: "src_paper_aljalbout_reality_gap_2025"
    type: "paper"
    title: "The Reality Gap in Robotics: Challenges, Solutions, and Best Practices"
    url: "https://arxiv.org/abs/2510.20808"
    date: "2025-10-23"
    accessed_at: "2026-06-25"
---

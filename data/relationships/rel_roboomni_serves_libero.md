---
$id: "rel_roboomni_serves_libero"
$schema: "../schema/v1/relationship_schema.json"
$version: 1

type: "serves"

source:
  id: "ent_paper_roboomni_2025"
  name:
    en: "RoboOmni: Proactive Robot Manipulation in Omni-modal Context"
    zh: "RoboOmni：全模态上下文中的主动式机器人操作"
    ko: "RoboOmni: 옴니모달 맥락에서의 주도적 로봇 조작"

target:
  id: "ent_benchmark_libero"
  name:
    en: "LIBERO"
    zh: "LIBERO"
    ko: "LIBERO"

domains:
  source_domain: "07_ai_models_algorithms"
  target_domain: "10_evaluation_benchmarks"

description:
  en: "RoboOmni is evaluated on LIBERO benchmarks using the OmniAction-LIBERO data split."
  zh: "RoboOmni 使用 OmniAction-LIBERO 数据分割在 LIBERO 基准上进行评估。"
  ko: "RoboOmni은 OmniAction-LIBERO 데이터 분할을 사용하여 LIBERO 벤치마크에서 평가됨."

verification:
  status: "verified"
  reviewed_by: "human_and_ai"
  reviewed_at: "2026-06-22"
  confidence: "high"
  notes: "Confirmed by the RoboOmni GitHub repository evaluation instructions."

sources:
  - id: "src_roboomni_repo"
    type: "website"
    title: "OpenMOSS/RoboOmni GitHub Repository"
    url: "https://github.com/OpenMOSS/RoboOmni"
    date: "2025-10-30"
    accessed_at: "2026-06-22"
---

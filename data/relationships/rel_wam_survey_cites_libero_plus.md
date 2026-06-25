---
$id: "rel_wam_survey_cites_libero_plus"
$schema: "../schema/v1/relationship_schema.json"
$version: 1

type: "cites"

source:
  id: "ent_paper_wang_wam_survey_2026"
  name:
    en: "World Action Models: The Next Frontier in Embodied AI"
    zh: "世界动作模型：具身智能的下一个前沿"
    ko: "월드 액션 모델: 엠바디드 AI의 다음 프론티어"

target:
  id: "ent_benchmark_libero_plus"
  name:
    en: "LIBERO-Plus"
    zh: "LIBERO-Plus"
    ko: "LIBERO-Plus"

domains:
  source_domain: "10_evaluation_benchmarks"
  target_domain: "10_evaluation_benchmarks"

description:
  en: "The WAM survey cites robustness benchmarks such as LIBERO-plus as part of the emerging WAM evaluation landscape."
  zh: "WAM 综述将 LIBERO-plus 等鲁棒性基准引用为新兴 WAM 评测格局的一部分。"
  ko: "WAM 서베이는 LIBERO-plus와 같은 견고성 벤치마크를 새로운 WAM 평가 환경의 일부로 인용함."

verification:
  status: "verified"
  reviewed_by: "human_and_ai"
  reviewed_at: "2026-06-22"
  confidence: "high"
  notes: "LIBERO-plus is discussed in the WAM survey's evaluation section."

sources:
  - id: "src_wam_paper"
    type: "paper"
    title: "World Action Models: The Next Frontier in Embodied AI"
    url: "https://arxiv.org/abs/2605.12090"
    date: "2026-05-12"
    accessed_at: "2026-06-22"
---

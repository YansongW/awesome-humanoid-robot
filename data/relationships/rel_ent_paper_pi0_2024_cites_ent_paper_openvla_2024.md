---
$id: "rel_ent_paper_pi0_2024_cites_ent_paper_openvla_2024"
$schema: "../../../../../data/schema/v1/relationship_schema.json"
$version: 1

type: "cites"

source:
  id: "ent_paper_pi0_2024"
  name:
    en: "π0: A Vision-Language-Action Flow Model for General Robot Control"
    zh: "π0：用于通用机器人控制的视觉-语言-动作流模型"
    ko: "π0: 범용 로봇 제어를 위한 비전-언어-액션 플로우 모델"

target:
  id: "ent_paper_openvla_2024"
  name:
    en: "OpenVLA: An Open-Source Vision-Language-Action Model"
    zh: "OpenVLA：一个开源的视觉-语言-动作模型"
    ko: "OpenVLA: 오픈소스 비전-언어-액션 모델"

domains:
  source_domain: "07_ai_models_algorithms"
  target_domain: "07_ai_models_algorithms"

description:
  en: "The π0 paper references OpenVLA as a contemporary open-source VLA in the related-work landscape."
  zh: "π0 论文在相关工作部分将 OpenVLA 作为同期开源 VLA 引用。"
  ko: "π0 논문은 관련 연구 부분에서 OpenVLA를 동시대 오픈소스 VLA로 인용함."

verification:
  status: "partially_verified"
  reviewed_by: "ai"
  reviewed_at: "2026-06-25"
  confidence: "medium"
  notes: "Temporal ordering supports the citation direction (OpenVLA June 2024, π0 October 2024). Exact wording in the π0 paper should be confirmed by human review."

sources:
  - id: "src_paper_pi0_2024"
    type: "paper"
    title: "π0: A Vision-Language-Action Flow Model for General Robot Control"
    url: "https://arxiv.org/abs/2410.24164"
    date: "2024-10-31"
    accessed_at: "2026-06-25"
---
